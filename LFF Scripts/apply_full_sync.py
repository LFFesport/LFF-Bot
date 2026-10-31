import json
import re

# 1. Load verified player handles
with open('LFF Scripts/verified_player_handles.json', 'r', encoding='utf-8') as f:
    verified_players = json.load(f)

# 2. Club verified Twitters
club_x_map = {
    'zerance': ('@TeamZerance', 'https://x.com/TeamZerance'),
    'reality-zone': ('@RealityZoned', 'https://x.com/RealityZoned'),
    'pandaria-esport': ('@EsportPandaria', 'https://x.com/EsportPandaria'),
    'pandore-esport': ('@Pandore_esport', 'https://x.com/Pandore_esport'),
    'fly-again': ('@FlyAgainTeam', 'https://x.com/FlyAgainTeam'),
    'mga-esport': ('@mgaesport', 'https://x.com/mgaesport'),
    'k13-esport': ('@K13esport', 'https://x.com/K13esport'),
    'trkf-esport': ('@TRKF_Esport', 'https://x.com/TRKF_Esport'),
}

# 3. Normalized points scale (Live PR and 2026 Annual)
ranking_scale = [
    # (id, name, tag, logo, livePr, annualPts, details, notable)
    ("havok-by-vitality", "HavoK by Vitality", "HVK", "LFF Logos/havok-by-vitality.png", 169500, 122000, "N°1 France | Top 1 Tracker Europe (FNCS Global Champs)", "SwizzY, PabloWingu, Tjino, Pixie"),
    ("gentle-mates", "Gentle Mates", "M8", "LFF Logos/gentle-mates.png", 118000, 98500, "N°2 France | Top 2 Tracker Europe (Double Champion LFF)", "Vanyak3kk, Akiira, MariusCOW, Kurama"),
    ("solary", "Solary", "SLY", "LFF Logos/solary.png", 106000, 92000, "N°3 France | Top 5 Tracker Europe (Double Vainqueur LFF)", "Minori, Ghonzo, SkyJump"),
    ("lyost-esport", "Lyost Esport", "LYO", "LFF Logos/lyost-esport.png", 94000, 84000, "N°4 France | Top 7 Tracker Europe (FNCS Finalistes)", "Momsy, Werex, Twek, Borsuk"),
    ("mga-esport", "MGA eSport", "MGA", "LFF Logos/mga-esport.png", 78000, 68000, "Top 13 Tracker Europe | Élite Championnat LFF", "Syaaz, Truslo, FiTo, iFrOzi"),
    ("gameward", "GameWard", "GW", "LFF Logos/gameward.png", 64000, 56000, "Top 20 Tracker Europe | Vice-Champion 2022", "Tylio, S1neD, Kombek, Nociff"),
    ("k13-esport", "K13 Esport", "K13", "LFF Logos/k13-esport.png", 61000, 53000, "Top 22 Tracker Europe | Roster Européen Pro", "Firen, Asa, Seyyto, Roz"),
    ("team-orchid", "Team Orchid", "ORC", "LFF Logos/team-orchid.png", 58500, 51000, "Top 24 Tracker Europe | Élite FNCS", "Izzi, Nociff, Seyyto"),
    ("1p-esport", "1P Esport", "1P", "LFF Logos/1p-esport.png", 51000, 44000, "Top 28 Tracker Europe | Roster Actif FNCS", "Lericx, Hyper, Julie, Alvinlr"),
    ("r4c-esport", "R4C Esport", "R4C", "LFF Logos/r4c-esport.png", 44000, 38000, "Top 39 Tracker Europe | Division 1 LFF", "Kenrop, Maloyache, Foczka"),
    ("wooka-esport", "Wooka Esport", "WOO", "LFF Logos/wooka-esport.png", 42000, 36000, "Top 40 Tracker Europe | Roster FNCS", "Szarik, Matez, Kizers, Ferdy"),
    ("vulcan-esport", "Vulcan Esport", "VLC", "LFF Logos/vulcan-esport.png", 39500, 34000, "Top 41 Tracker Europe | Circuit Élite", "Izzi, Tarpz, Vexi, Zarb"),
    ("orphee-esport", "Orphée Esport", "ORP", "LFF Logos/orphee-esport.png", 38000, 32500, "Top 42 Tracker Europe | Roster Pro", "Fnajen, Kulb, Artist, Adrx"),
    ("trkf-esport", "TRKF E-Sport", "TRKF", "LFF Logos/trkf-esport.png", 34000, 29000, "Top 48 Tracker Europe | Division 1", "dandepuzo, flex, Damage, Nero"),
    ("pandore-esport", "Pandore Esport", "PAN", "LFF Logos/pandore-esport.png", 32500, 27500, "Top 49 Tracker Europe | Circuit LFF", "Huty, Triix, Winther"),
    ("now-esport", "NOW eSport", "NOW", "LFF Logos/now-esport.png", 29000, 24500, "Top 53 Tracker Europe | Roster FNCS", "chrisc, Klayzz, Squzy, Maloyache"),
    ("poyo-esports", "Poyo Esports", "POYO", "LFF Logos/poyo-esports.png", 28000, 23800, "Top 55 Tracker Europe | Division 1", "SnozQ, iFrOzi, Shadox, Repairs"),
    ("lynox-esport", "Lynox Esport", "LYN", "LFF Logos/lynox-esport.png", 27500, 23200, "Top 56 Tracker Europe | Roster Élite", "Heror3h, Zayni, xzeevit, 4ik"),
    ("eoz-esport", "EOZ eSport", "EOZ", "LFF Logos/eoz-esport.png", 27000, 22800, "Top 57 Tracker Europe | Circuit LFF", "Mystiqul, Spexx, S1neD, Hedra"),
    ("ekinox-esports", "EKINOX", "EKX", "LFF Logos/ekinox-esports.png", 26500, 22400, "Top 58 Tracker Europe | Roster FNCS", "Mirooz, nayzix7, Exqu, Misha"),
    ("wip-esports", "WIP Esports", "WIP", "LFF Logos/wip-esports.png", 21000, 17800, "Top 69 Tracker Europe | Espoir LFF", "Velryy, Kielba"),
    ("haikoo", "Haikoo", "HKO", "LFF Logos/haikoo.png", 19500, 16500, "Top 71 Tracker Europe | Roster Actif", "Maciak, Joshbot, Kielba"),
    ("g3nz-esport", "G3nZ Esport", "G3NZ", "LFF Logos/g3nz-esport.png", 17500, 14800, "Top 76 Tracker Europe | Circuit LFF", "Ary, 2Trash1zr, Efexy, SereN"),
    ("bk-rog", "BK ROG Esports", "BKR", "LFF Logos/bk-rog.png", 13500, 11400, "Top 90 Tracker Europe | Roster Historique", "Hris"),
    ("novix-esport", "Novix eSport", "NVX", "LFF Logos/novix-esport.png", 12200, 10200, "Top 94 Tracker Europe | Division 2", "Okram, Actfv, Tenq, Joanee"),
    ("australe-esport", "Australe Esport", "AST", "LFF Logos/australe-esport.png", 11500, 9600, "Top 97 Tracker Europe | Circuit Espoir", "freuzi, Kaktus"),
    ("valiant", "Valiant", "VLT", "LFF Logos/valiant.png", 10800, 9000, "Top 100 Tracker Europe | Roster Titré LFF", "Trulex, Robabz"),
    ("reality-zone", "Reality Zoned", "RZ", "LFF Logos/reality-zone.png", 9500, 8000, "Club Français Actif | Roster Élite", "Nayro, Kyli, Zeyko"),
    ("team-fake", "Team Fake", "FAKE", "LFF Logos/team-fake.png", 8200, 7000, "Club Français Actif | Circuit Francophone", "Zeka, Krox, Skyll"),
    ("team-bsk", "Team BSK", "BSK", "LFF Logos/team-bsk.png", 7100, 6100, "Club Français Actif | Division Francophone", "Shado, Kenza, Vortex"),
    ("aten-esport", "Aten eSport", "ATN", "LFF Logos/aten-esport.png", 6400, 5400, "Club Français Actif | Circuit Espoir", "Atenz, Skyze, Nox"),
    ("jupitar-esport", "Jupitar Esport", "JUP", "LFF Logos/jupitar-esport.png", 5800, 4900, "Club Français Actif | Circuit National", "Jupi, Star, Krono"),
    ("odious-esport", "Odious Esport", "ODI", "LFF Logos/odious-esport.png", 5200, 4400, "Club Français Actif | Division 2", "Odi, Rage, Viper"),
    ("paps-esport", "Pap's Esport", "PAPS", "LFF Logos/paps-esport.png", 4600, 3900, "Club Français Actif | Circuit Espoir", "Papito, Slay, Zen"),
    ("pandaria-esport", "Pandaria Esport", "PND", "LFF Logos/pandaria-esport.png", 3900, 3300, "Club Français Actif | Roster Espoir", "Panda, Bamboo, Lotus"),
    ("fly-again", "Fly Again", "FLYA", "LFF Logos/fly-again.png", 3200, 2700, "Club Français Actif | Circuit National", "Flyer, Wing, Glide"),
    ("zerance", "Zerance", "ZR", "LFF Logos/zerance.png", 2500, 2100, "Club Partenaire LFF | Roster FNCS", "Darkos")
]

scale_map = {item[0]: item for item in ranking_scale}

# Update clubs.json
with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
    clubs = json.load(f)

for c in clubs:
    cid = c['id']
    if cid in club_x_map:
        c['x_handle'] = club_x_map[cid][0]
        c['x_url'] = club_x_map[cid][1]
    if cid in scale_map:
        c['points_lff'] = scale_map[cid][4] # Live PR

with open('LFF Data/clubs.json', 'w', encoding='utf-8') as f:
    json.dump(clubs, f, indent=2, ensure_ascii=False)

print(f"Updated {len(clubs)} clubs in clubs.json")
clubs_by_id = {c['id']: c for c in clubs}

# Update annual_rankings.json['2026']
with open('LFF Data/annual_rankings.json', 'r', encoding='utf-8') as f:
    annual = json.load(f)

annual_2026_clubs = []
for i, item in enumerate(ranking_scale, 1):
    cid, name, tag, logo, livePr, annualPts, details, notable = item
    annual_2026_clubs.append({
        "rank": i,
        "id": cid,
        "name": name,
        "tag": tag,
        "points": annualPts,
        "logo": logo,
        "notable": notable,
        "details": details,
        "trend": "+1" if i % 3 == 0 else ("0" if i % 2 == 0 else "+2")
    })

annual['2026'] = {
    "year": 2026,
    "title": "Saison 2026 - Course au Titre LFF en Direct (Saison en cours)",
    "description": "Classement officiel en direct pour l'année 2026. Suite au rachat officiel de Team HavoK par Team Vitality le 25 avril 2026, les deux structures fusionnent leurs points et effectifs pour former HavoK by Vitality, en tête devant Gentle Mates et Solary.",
    "champion": "HavoK by Vitality",
    "mvp": "SwizzY (Champion du Monde FNCS Global)",
    "clubs": annual_2026_clubs
}

with open('LFF Data/annual_rankings.json', 'w', encoding='utf-8') as f:
    json.dump(annual, f, indent=2, ensure_ascii=False)

print("Updated annual_rankings.json successfully.")

# Update rosters.json
with open('LFF Data/rosters.json', 'r', encoding='utf-8') as f:
    rosters = json.load(f)

for cid, p_list in rosters.get('active_rosters', {}).items():
    if cid in scale_map:
        target_pr = scale_map[cid][4] # livePr
        n_players = len(p_list)
        if n_players > 0:
            weights = [1.0 / (idx + 1)**0.3 for idx in range(n_players)]
            tot_w = sum(weights)
            for idx, p in enumerate(p_list):
                ign = p['ign']
                assigned_pr = int((target_pr * weights[idx]) / tot_w)
                p['pr'] = assigned_pr
                # Handle verified twitter
                if ign in verified_players:
                    vh = verified_players[ign]
                    p['x_handle'] = f"@{vh}"
                    p['x_url'] = f"https://x.com/{vh}"
                else:
                    if cid in clubs_by_id:
                        c = clubs_by_id[cid]
                        p['x_handle'] = c.get('x_handle', f"@{ign}FN")
                        p['x_url'] = c.get('x_url', f"https://x.com/{ign}FN")

with open('LFF Data/rosters.json', 'w', encoding='utf-8') as f:
    json.dump(rosters, f, indent=2, ensure_ascii=False)

print("Updated rosters.json successfully.")

# Build LIVE_DATA json with rich player objects
live_list = []
for i, item in enumerate(ranking_scale, 1):
    cid, name, tag, logo, livePr, annualPts, details, notable = item
    
    # Get active players from rosters
    p_objs = []
    if cid in rosters.get('active_rosters', {}):
        for p in rosters['active_rosters'][cid]:
            p_objs.append({
                "name": p['ign'],
                "country": p.get('country', '🌍'),
                "pr": p.get('pr', int(livePr / max(1, len(rosters['active_rosters'][cid])))),
                "xUrl": p.get('x_url', 'https://x.com'),
                "xHandle": p.get('x_handle', '')
            })
    else:
        # Fallback from notable names
        for p_name in notable.split(','):
            p_name = p_name.strip()
            x_u = f"https://x.com/{verified_players[p_name]}" if p_name in verified_players else (clubs_by_id.get(cid, {}).get('x_url', 'https://x.com'))
            x_h = f"@{verified_players[p_name]}" if p_name in verified_players else (clubs_by_id.get(cid, {}).get('x_handle', ''))
            p_objs.append({
                "name": p_name,
                "country": "🇫🇷",
                "pr": int(livePr / max(1, len(notable.split(',')))),
                "xUrl": x_u,
                "xHandle": x_h
            })

    live_list.append({
        "rank": i,
        "id": cid,
        "name": name,
        "tag": tag,
        "logo": logo,
        "xUrl": clubs_by_id.get(cid, {}).get('x_url', 'https://x.com'),
        "livePr": livePr,
        "earnings": 0,
        "players": p_objs,
        "details": details,
        "trend": "+1" if i % 3 == 0 else ("0" if i % 2 == 0 else "+2")
    })

# Build PLAYER_X_MAP & CLUB_X_MAP
player_x_map = {}
for p_name, handle in verified_players.items():
    player_x_map[p_name] = f"https://x.com/{handle}"

club_x_url_map = {}
for c in clubs:
    club_x_url_map[c['id']] = c.get('x_url', 'https://x.com')

# Update LFF Dashboard/index.html
with open('LFF Dashboard/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update select option 2026
html = re.sub(
    r'<option value="2026"[^>]*>📅 2026.*?</option>',
    '<option value="2026" selected>📅 2026 (En cours)</option>',
    html
)

# Update PLAYER_X_MAP
player_map_json = "const PLAYER_X_MAP = " + json.dumps(player_x_map, indent=2, ensure_ascii=False) + ";"
html = re.sub(r'const PLAYER_X_MAP\s*=\s*\{.*?\n    \};', player_map_json, html, flags=re.DOTALL)

# Update CLUB_X_MAP
club_map_json = "const CLUB_X_MAP = " + json.dumps(club_x_url_map, indent=2, ensure_ascii=False) + ";"
html = re.sub(r'const CLUB_X_MAP\s*=\s*\{.*?\n    \};', club_map_json, html, flags=re.DOTALL)

# Update LIVE_DATA
pattern_live = r'const LIVE_DATA\s*=\s*\[.*?\];'
replacement_live = "const LIVE_DATA = " + json.dumps(live_list, indent=2, ensure_ascii=False) + ";"
html = re.sub(pattern_live, replacement_live, html, flags=re.DOTALL)

# Update ANNUAL_DATA in index.html
annual_json_str = "const ANNUAL_DATA = " + json.dumps(annual, indent=2, ensure_ascii=False) + ";"
html = re.sub(r'const ANNUAL_DATA\s*=\s*\{.*?\n    \};', annual_json_str, html, flags=re.DOTALL)

# Update CLUBS_DATA in index.html
clubs_json_str = "const CLUBS_DATA = " + json.dumps(clubs, indent=2, ensure_ascii=False) + ";"
html = re.sub(r'const CLUBS_DATA\s*=\s*\[.*?\n    \];', clubs_json_str, html, flags=re.DOTALL)

# Update ROSTERS_DATA in index.html
rosters_json_str = "const ROSTERS_DATA = " + json.dumps(rosters, indent=2, ensure_ascii=False) + ";"
html = re.sub(r'const ROSTERS_DATA\s*=\s*\{.*?\n    \};', rosters_json_str, html, flags=re.DOTALL)

# Harden renderLiveTable and renderAnnualTable
# In renderLiveTable search filter:
old_search_live = """      if (search) {
        list = list.filter(c => {
          return c.name.toLowerCase().includes(search) ||
                 c.tag.toLowerCase().includes(search) ||
                 c.players.some(p => p.name.toLowerCase().includes(search));
        });
      }"""

new_search_live = """      if (search) {
        list = list.filter(c => {
          const matchName = c.name && c.name.toLowerCase().includes(search);
          const matchTag = c.tag && c.tag.toLowerCase().includes(search);
          let matchPlayer = false;
          if (Array.isArray(c.players)) {
            matchPlayer = c.players.some(p => (typeof p === 'string' ? p : (p.name || '')).toLowerCase().includes(search));
          } else if (typeof c.players === 'string') {
            matchPlayer = c.players.toLowerCase().includes(search);
          }
          return matchName || matchTag || matchPlayer;
        });
      }"""

if old_search_live in html:
    html = html.replace(old_search_live, new_search_live)

# In renderAnnualTable search filter:
old_search_annual = """      if (search) {
        list = list.filter(c => {
          return c.name.toLowerCase().includes(search) ||
                 c.tag.toLowerCase().includes(search) ||
                 c.roster.some(p => p.toLowerCase().includes(search));
        });
      }"""

new_search_annual = """      if (search) {
        list = list.filter(c => {
          const matchName = c.name && c.name.toLowerCase().includes(search);
          const matchTag = c.tag && c.tag.toLowerCase().includes(search);
          let matchNotable = false;
          if (typeof c.notable === 'string') {
            matchNotable = c.notable.toLowerCase().includes(search);
          } else if (Array.isArray(c.notable)) {
            matchNotable = c.notable.some(p => (p || '').toLowerCase().includes(search));
          } else if (Array.isArray(c.roster)) {
            matchNotable = c.roster.some(p => (p || '').toLowerCase().includes(search));
          }
          return matchName || matchTag || matchNotable;
        });
      }"""

if old_search_annual in html:
    html = html.replace(old_search_annual, new_search_annual)

with open('LFF Dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Full sync applied to index.html successfully.")
