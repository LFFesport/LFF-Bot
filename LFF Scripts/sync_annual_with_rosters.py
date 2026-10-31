"""
sync_annual_with_rosters.py
Applique la règle fondamentale 'Base de Données First' :
- Nettoie les astérisques erronés dans 2026 (Pixie, SwizzY, Wox chez HavoK n'ont aucun départ, ils sont 100% actifs).
- Met à jour annual_rankings.json pour 2026.
- Construit LIVE_DATA directement depuis active_rosters de rosters.json.
- Réinjecte ANNUAL_DATA, LIVE_DATA et TRANSFERS dans LFF Dashboard/index.html.
"""

import json
import re
from pathlib import Path

DATA_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF/LFF Data")
SCRIPTS_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF/LFF Scripts")
DASHBOARD_FILE = Path("C:/Users/marti/Documents/MARTIN/LFF/LFF Dashboard/index.html")

with open(DATA_DIR / "annual_rankings.json", "r", encoding="utf-8") as f:
    annual = json.load(f)

with open(DATA_DIR / "rosters.json", "r", encoding="utf-8") as f:
    rosters = json.load(f)

with open(SCRIPTS_DIR / "master_players.json", "r", encoding="utf-8") as f:
    master_players = json.load(f)

with open(SCRIPTS_DIR / "master_clubs.json", "r", encoding="utf-8") as f:
    master_clubs = json.load(f)

# Récupérer les départs confirmés (club, joueur)
confirmed_departures = set()
for t in rosters.get("transfers_log", []):
    pname = (t.get("player_ign") or t.get("player") or "").replace("*", "").strip()
    from_club = t.get("previous_club") or ""
    # Si le joueur a quitté un club spécifique
    if from_club and from_club != "Free Agent":
        # Mapper le nom du club vers l'ID si possible
        cid = from_club.lower().replace(" ", "-")
        for mid, mc in master_clubs.items():
            if mc["name"].lower() == from_club.lower() or mc["tag"].lower() == from_club.lower():
                cid = mid
                break
        confirmed_departures.add((cid, pname))

# Départs confirmés connus
confirmed_departures.add(("solary", "Darkos"))
confirmed_departures.add(("solary", "Kurama"))

print(f"Départs officiellement documentés : {confirmed_departures}")

# 1. Mise à jour de la saison 2026 dans annual_rankings.json
s26 = annual["2026"]
for c in s26["clubs"]:
    cid = c["id"]
    new_players = []
    for p in c["players"]:
        pname = p["name"].replace("*", "").strip()
        # Seuls les départs confirmés dans la base ont l'astérisque et is_former=True
        is_departed = (cid, pname) in confirmed_departures
        
        m_data = master_players.get(pname, {})
        new_players.append({
            "name": pname + ("*" if is_departed else ""),
            "country": m_data.get("country", p.get("country", "fr")),
            "pr": p.get("pr", p.get("points", 2500)),
            "is_former": is_departed,
            "tracker_url": m_data.get("tracker_url", p.get("tracker_url", f"https://fortnitetracker.com/profile/all/{pname}")),
            "socials": m_data.get("socials", p.get("socials", {}))
        })
    c["players"] = new_players
    c["points"] = sum(p["pr"] for p in new_players)

# Sauvegarder annual_rankings.json
with open(DATA_DIR / "annual_rankings.json", "w", encoding="utf-8") as f:
    json.dump(annual, f, indent=2, ensure_ascii=False)

print("annual_rankings.json synchronisé avec les départs documentés.")

# 2. Construire LIVE_DATA directement depuis active_rosters de rosters.json
live_data = []
for cid, active_list in rosters["active_rosters"].items():
    c_meta = master_clubs.get(cid, {})
    c_name = c_meta.get("name", cid)
    c_tag = c_meta.get("tag", "LFF")
    
    clean_active_players = []
    for p in active_list:
        pname = p["name"].replace("*", "").strip()
        m_data = master_players.get(pname, {})
        clean_active_players.append({
            "name": pname,
            "country": m_data.get("country", p.get("country", "fr")),
            "pr": p.get("pr", 2500),
            "is_former": False,
            "tracker_url": m_data.get("tracker_url", f"https://fortnitetracker.com/profile/all/{pname}"),
            "socials": m_data.get("socials", {})
        })
        
    total_live_pr = sum(p["pr"] for p in clean_active_players)
    
    # Trouver description ou notable depuis annual_rankings
    annual_club = next((c for c in s26["clubs"] if c["id"] == cid), {})
    notable = annual_club.get("notable", "")
    
    live_data.append({
        "id": cid,
        "name": c_name,
        "tag": c_tag,
        "points": total_live_pr,
        "livePr": total_live_pr,
        "tracker_url": c_meta.get("tracker_url", f"https://fortnitetracker.com/esports/organization/{cid}"),
        "socials": c_meta.get("socials", {}),
        "players": clean_active_players,
        "roster": [p["name"] for p in clean_active_players],
        "notable": notable
    })

# Trier live_data par points décroissants
live_data.sort(key=lambda x: x["points"], reverse=True)
for idx, c in enumerate(live_data, 1):
    c["rank"] = idx

print(f"LIVE_DATA généré ({len(live_data)} clubs).")
print(f"Top 1 LIVE: {live_data[0]['name']} ({live_data[0]['points']} pts) - {len(live_data[0]['players'])} joueurs actifs.")
print("Joueurs HavoK LIVE:", [p["name"] for p in live_data[0]["players"]])

# 3. Synchroniser index.html
with open(DASHBOARD_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Remplacer ANNUAL_DATA
annual_json_str = json.dumps(annual, indent=2, ensure_ascii=False)
html = re.sub(
    r'const ANNUAL_DATA\s*=\s*\{.*?\n\s*\};\n(?=\s*const LIVE_DATA)',
    f'const ANNUAL_DATA = {annual_json_str};\n',
    html,
    flags=re.DOTALL
)

# Remplacer LIVE_DATA
live_json_str = json.dumps(live_data, indent=2, ensure_ascii=False)
html = re.sub(
    r'const LIVE_DATA\s*=\s*\[.*?\n\s*\];\n(?=\s*const TRANSFERS)',
    f'const LIVE_DATA = {live_json_str};\n',
    html,
    flags=re.DOTALL
)

# Remplacer TRANSFERS
transfers_list = []
for t in rosters.get("transfers_log", []):
    pname = (t.get("player_ign") or t.get("player") or "").replace("*", "").strip()
    m_p = master_players.get(pname, {})
    m_c_to = master_clubs.get(t.get("club_id"), {})
    
    transfers_list.append({
        "date": t.get("date", ""),
        "player": pname,
        "playerXUrl": m_p.get("socials", {}).get("x", ""),
        "tracker_url": m_p.get("tracker_url", f"https://fortnitetracker.com/profile/all/{pname}"),
        "country": m_p.get("country", "fr"),
        "from": t.get("previous_club", "Free Agent"),
        "to": m_c_to.get("name", t.get("club_id", "")),
        "toId": t.get("club_id", ""),
        "toXUrl": m_c_to.get("socials", {}).get("x", ""),
        "type": t.get("type", "Arrival"),
        "status": t.get("status", "Confirmed")
    })

transfers_json_str = json.dumps(transfers_list, indent=2, ensure_ascii=False)
html = re.sub(
    r'const TRANSFERS\s*=\s*\[.*?\n\s*\];\n(?=\s*const LOGO_MAP)',
    f'const TRANSFERS = {transfers_json_str};\n',
    html,
    flags=re.DOTALL
)

html = html.replace('\u2014', '-')

with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("LFF Dashboard/index.html synchronisé avec succès !")
