#!/usr/bin/env python3
"""
Ligue Française de Fortnite (LFF) - Transfer Tracker & PR Scraper
Module de veille automatisée connecté à Liquipedia (Portal:Transfers) et calculateur de Power Ranking.
"""

import gzip
import json
import os
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

# Fix console encoding on Windows
if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

LIQUIPEDIA_API = "https://liquipedia.net/fortnite/api.php"
HEADERS = {
    "User-Agent": "LigueFrancaiseFortniteBot/1.0 (contact@lff-fortnite.fr)",
    "Accept-Encoding": "gzip"
}

def load_json(filename):
    path = DATA_DIR / filename
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filename, data):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fetch_liquipedia_transfers():
    """Récupère et parse les transferts depuis Liquipedia Portal:Transfers."""
    url = f"{LIQUIPEDIA_API}?action=parse&page=Portal:Transfers&format=json"
    req = urllib.request.Request(url, headers=HEADERS)

    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read()
            try:
                html = gzip.decompress(raw).decode("utf-8")
            except Exception:
                html = raw.decode("utf-8")
            data = json.loads(html)
            raw_text = data.get("parse", {}).get("text", {}).get("*", "")
    except Exception as e:
        print(f"[!] Erreur de connexion à Liquipedia : {e}")
        return []

    # Extraire les divRow
    div_rows = re.findall(r'<div class="divRow[^"]*">(.*?)</div>\s*(?=<div class="divRow|$)', raw_text, re.DOTALL)
    transfers = []

    for row in div_rows:
        cells = re.findall(r'<div class="divCell[^"]*">(.*?)</div>', row, re.DOTALL)
        if len(cells) < 4:
            continue

        # Cell 0: Date
        date_match = re.search(r'\d{4}-\d{2}-\d{2}', cells[0])
        date_str = date_match.group(0) if date_match else cells[0].strip()

        # Cell 1: Player & Flag
        flag_match = re.search(r'title="([^"]+)"', cells[1])
        country = flag_match.group(1) if flag_match else "Inconnu"
        
        name_match = re.search(r'title="([^"]+)"[^>]*>([^<]+)</a>', cells[1])
        if name_match:
            player_ign = name_match.group(2).strip()
        else:
            player_ign = re.sub(r'<[^>]+>', '', cells[1]).strip()

        # Cell 2: Old Team (From)
        old_team_match = re.search(r'title="([^"]+)"', cells[2])
        if old_team_match:
            old_team = old_team_match.group(1).strip()
        elif "None" in cells[2] or "Free Agent" in cells[2]:
            old_team = "Free Agent"
        else:
            old_team = re.sub(r'<[^>]+>', '', cells[2]).strip() or "Inconnu"

        # Cell 3: New Team (To)
        new_team_match = re.search(r'title="([^"]+)"', cells[3])
        if new_team_match:
            new_team = new_team_match.group(1).strip()
        elif "None" in cells[3] or "Free Agent" in cells[3]:
            new_team = "Free Agent"
        else:
            new_team = re.sub(r'<[^>]+>', '', cells[3]).strip() or "Inconnu"

        transfers.append({
            "date": date_str,
            "player": player_ign,
            "country": country,
            "from_team": old_team,
            "to_team": new_team,
            "raw": row
        })

    return transfers

def is_french_related(transfer, clubs_list):
    """
    Vérifie si le transfert concerne un club français (joueurs de toute nationalité)
    ou à titre informatif un joueur français.
    RÈGLE LFF : Les joueurs des clubs français peuvent être de N'IMPORTE QUELLE nationalité
    (ex: Malibuca, Merstach, Veno comptent à 100% pour la Karmine Corp ou Gentle Mates).
    """
    french_org_aliases = [
        "gentle mates", "karmine corp", "solary", "vitality", "team vitality",
        "mces", "trainhard", "trainhard esport", "grizi esport", "grizi",
        "lestream", "lestream esport", "valiant", "reality zone", "team bsk", "bsk esport",
        "team fake", "fake", "aten", "aten esport", "jupitar", "jupitar esport",
        "odious", "odious esport", "pap's", "paps esport", "gamersorigin", "team go",
        "bk rog", "bk rog esports", "gameward", "zerance"
    ]

    for c in clubs_list:
        french_org_aliases.append(c["name"].lower())
        french_org_aliases.append(c["tag"].lower())

    from_lower = transfer.get("from_team", "").lower()
    to_lower = transfer.get("to_team", "").lower()

    # 1. Priorité absolue : Le transfert implique un CLUB FRANÇAIS (nationalité du joueur indifférente)
    for alias in french_org_aliases:
        if alias and (alias in from_lower or alias in to_lower):
            if alias in to_lower:
                return True, f"Arrivée Club FR ({alias.upper()}) [Tout pays]"
            else:
                return True, f"Départ Club FR ({alias.upper()}) [Tout pays]"

    # 2. Information complémentaire : Joueur français en transit hors clubs LFF
    if transfer.get("country", "").lower() in ["france", "fr"]:
        return True, "Joueur FR (hors club LFF)"

    return False, None

def scan_transfers(filter_fr=True, sync=False):
    """Scanne les transferts et affiche ou synchronise les résultats."""
    print("=" * 80)
    print(" 📡 VEILLE OFFICIELLE DES TRANSFERTS LIQUIPEDIA (Portal:Transfers) 📡")
    print("=" * 80)
    print("Connexion au flux Liquipedia en cours...\n")

    transfers = fetch_liquipedia_transfers()
    if not transfers:
        print("[!] Aucun transfert récupéré depuis Liquipedia.")
        return

    clubs = load_json("clubs.json") or []
    rosters_data = load_json("rosters.json") or {"transfers_log": [], "active_rosters": {}}

    print(f"Total transferts récents détectés sur Liquipedia : {len(transfers)}")
    print("-" * 80)

    fr_matches = []
    for t in transfers:
        is_fr, reason = is_french_related(t, clubs)
        if filter_fr:
            if is_fr:
                t["match_reason"] = reason
                fr_matches.append(t)
        else:
            t["match_reason"] = reason if is_fr else "International"
            fr_matches.append(t)

    display_list = fr_matches if filter_fr else transfers
    print(f"🎯 Mouvements concernant la scène française : {len(fr_matches)}")
    print("-" * 80)

    if not fr_matches and filter_fr:
        print("ℹ️ Aucun transfert français immédiat sur la toute dernière page.")
        print("Affichage des 10 derniers transferts internationaux européens pour contrôle :\n")
        display_list = transfers[:10]

    for idx, t in enumerate(display_list, 1):
        flag = "🇫🇷" if t.get("country") == "France" else f"🌍 ({t.get('country')})"
        reason_tag = f"[{t.get('match_reason')}]" if t.get("match_reason") else ""
        print(f"{idx:>2}. [{t['date']}] {t['player']} {flag} {reason_tag}")
        print(f"    Départ : {t['from_team']} ➡️ Arrivée : {t['to_team']}")

    if sync and fr_matches:
        print("\n📥 Synchronisation avec la base data/rosters.json...")
        new_count = 0
        for m in fr_matches:
            # Vérifier si déjà présent
            already = any(
                log.get("player_ign", "").lower() == m["player"].lower() and log.get("date") == m["date"]
                for log in rosters_data.get("transfers_log", [])
            )
            if not already:
                rosters_data["transfers_log"].insert(0, {
                    "date": m["date"],
                    "player_ign": m["player"],
                    "player_name": m["player"],
                    "type": "Arrival" if m["to_team"] != "Free Agent" else "Departure",
                    "club_id": m["to_team"],
                    "previous_club": m["from_team"],
                    "source": "Liquipedia Portal:Transfers",
                    "status": "Verified"
                })
                new_count += 1
        save_json("rosters.json", rosters_data)
        print(f"✅ {new_count} nouveaux transferts synchronisés dans data/rosters.json !")

def main():
    if len(sys.argv) < 2:
        print("Usage: python lff_transfer_tracker.py [option]")
        print("  --scan         : Scanner les transferts récents (filtre FR actif)")
        print("  --scan-all     : Scanner tous les transferts récents sans filtre")
        print("  --sync         : Scanner et enregistrer automatiquement les transferts FR")
        sys.exit(0)

    opt = sys.argv[1]
    if opt == "--scan":
        scan_transfers(filter_fr=True, sync=False)
    elif opt == "--scan-all":
        scan_transfers(filter_fr=False, sync=False)
    elif opt == "--sync":
        scan_transfers(filter_fr=True, sync=True)
    else:
        print("[!] Option invalide.")

if __name__ == "__main__":
    main()
