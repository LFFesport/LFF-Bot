#!/usr/bin/env python3
"""
Ligue Française de Fortnite (LFF) - Engine & Manager
Gestionnaire des classements Power Ranking, du suivi des rosters et du palmarès historique des clubs français.
"""

import json
import os
import sys
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

def show_palmares():
    palmares = load_json("palmares.json")
    if not palmares:
        print("[!] Aucun fichier palmares.json trouvé.")
        return

    print("=" * 80)
    print(" 🏆 PALMARÈS HISTORIQUE DE LA LIGUE FRANÇAISE DE FORTNITE (2018 - 2025) 🏆")
    print("=" * 80)
    for p in palmares:
        print(f"\n📅 ANNÉE {p['year']} : {p['era'].upper()}")
        print(f"   🥇 CHAMPION DE FRANCE : {p['champion']['name']} ({p['champion']['tag']})")
        print(f"   👥 Roster clé : {', '.join(p['roster'])}")
        print(f"   🏆 Podium officiel :")
        for pos in p['podium']:
            print(f"      {pos['rank']}. {pos['club']} ({pos['points_estimate']}) - {pos['key_factor']}")
        print(f"   ⚔️  Tournois majeurs : {', '.join(p['key_tournaments'])}")
        print(f"   📝 Décision LFF : {p['verdict']}")
        print("-" * 80)

def list_clubs():
    clubs = load_json("clubs.json")
    if not clubs:
        print("[!] Aucun fichier clubs.json trouvé.")
        return

    print("=" * 80)
    print(" 🛡️ CLUBS ENREGISTRÉS DANS LA LIGUE FRANÇAISE DE FORTNITE (LFF) 🛡️")
    print("=" * 80)
    t1 = [c for c in clubs if c.get("tier") == "Tier 1"]
    t2 = [c for c in clubs if c.get("tier") == "Tier 2"]

    print("\n--- [ DIVISION ÉLITE (TIER 1 / HISTORIQUES) ] ---")
    for c in t1:
        status_icon = "🟢" if c["status"] == "Active" else "🏛️"
        print(f" {status_icon} [{c['tag']}] {c['name']:<20} | Fondé: {c['founded_year']} | Statut: {c['status']}")
        print(f"    ℹ️  {c['description']}")

    print("\n--- [ DIVISION CHALLENGER / SUB-TOP (TIER 2) ] ---")
    for c in t2:
        logo_info = f"Logo dispo" if c.get("logo_path") else "Logo générique"
        print(f" 🟢 [{c['tag']}] {c['name']:<20} | {c['x_handle']} | {logo_info}")
        print(f"    ℹ️  {c['description']}")

def show_roster(club_id):
    rosters_data = load_json("rosters.json")
    clubs = {c["id"]: c for c in load_json("clubs.json") or []}

    if not rosters_data:
        print("[!] Données des rosters manquantes.")
        return

    club = clubs.get(club_id)
    if not club:
        print(f"[!] Club inconnu : {club_id}. Utilisez --clubs pour voir la liste.")
        return

    print("=" * 70)
    print(f" 📋 ROSTER ACTUEL : {club['name']} [{club['tag']}]")
    print("=" * 70)

    players = rosters_data.get("active_rosters", {}).get(club_id, [])
    if not players:
        print("   (Aucun joueur actuellement sous contrat actif répertorié)")
    else:
        for idx, pl in enumerate(players, 1):
            print(f"   {idx}. {pl['ign']} ({pl.get('country', 'FR')}) - Rôle: {pl.get('role', 'Starter')} (depuis {pl.get('contract_start')})")

    # Historique des mouvements de ce club
    print("\n📜 Historique récent des transferts pour ce club :")
    transfers = [t for t in rosters_data.get("transfers_log", []) if t.get("club_id") == club_id]
    if not transfers:
        print("   (Aucun transfert archivé dans le log récent)")
    else:
        for t in transfers:
            type_symbol = "📥" if t["type"] == "Arrival" else "📤"
            print(f"   {type_symbol} [{t['date']}] {t['type']} : {t['player_ign']} (Source: {t.get('source', 'N/A')})")

def record_transfer(club_id, player_ign, t_type="Arrival", source="@FortniteFraActu"):
    rosters_data = load_json("rosters.json") or {"transfers_log": [], "active_rosters": {}}
    today = datetime.now().strftime("%Y-%m-%d")

    entry = {
        "date": today,
        "player_ign": player_ign,
        "player_name": player_ign,
        "type": t_type,
        "club_id": club_id,
        "previous_club": "Inconnu" if t_type == "Arrival" else club_id,
        "source": source,
        "status": "Confirmed"
    }

    rosters_data["transfers_log"].insert(0, entry)

    if t_type == "Arrival":
        club_roster = rosters_data["active_rosters"].setdefault(club_id, [])
        # Check if already in roster
        if not any(p["ign"].lower() == player_ign.lower() for p in club_roster):
            club_roster.append({
                "ign": player_ign,
                "country": "FR",
                "role": "Starter",
                "ftn_tracker_slug": player_ign,
                "contract_start": today
            })
    elif t_type == "Departure":
        club_roster = rosters_data["active_rosters"].get(club_id, [])
        rosters_data["active_rosters"][club_id] = [p for p in club_roster if p["ign"].lower() != player_ign.lower()]

    save_json("rosters.json", rosters_data)
    print(f"✅ Mouvement enregistré avec succès : {player_ign} ({t_type}) chez {club_id} le {today} (Source: {source})")

def export_markdown_report():
    palmares = load_json("palmares.json") or []
    clubs = load_json("clubs.json") or []
    rosters = load_json("rosters.json") or {}

    md_content = """# 🏆 LIGUE FRANÇAISE DE FORTNITE (LFF)
*Le classement officiel de référence des clubs d'esport français sur Fortnite*

---

## 📖 1. Présentation & Mission de la LFF
La **Ligue Française de Fortnite (LFF)** a pour vocation d'établir la hiérarchie officielle des structures esportives françaises engagées sur Fortnite.
Inspiré des systèmes de **Power Ranking (PR)** de *Fortnite Tracker* et de la *Fortnite Esports Wiki (Fandom)*, le classement de la LFF évalue la régularité, le talent et les performances des clubs lors des compétitions officielles (FNCS, Cash Cups, DreamHack, Global Championships).

Le but ultime est de décerner à la fin de chaque année civile le prestigieux titre de **Club Champion de France de Fortnite**.

---

## 🏛️ 2. Le Palmarès Historique Année par Année (2018 - 2025)

| Année | Club Champion | Tag | Joueurs clés / Roster | Faits d'armes majeurs | Dauphin (Top 2) |
| :---: | :--- | :---: | :--- | :--- | :--- |
"""

    for p in palmares:
        champ = p["champion"]
        roster_str = ", ".join(p["roster"][:3]) + ("..." if len(p["roster"]) > 3 else "")
        p2 = p["podium"][1]["club"] if len(p["podium"]) > 1 else "N/A"
        md_content += f"| **{p['year']}** | **{champ['name']}** | `{champ['tag']}` | {roster_str} | {p['podium'][0]['key_factor']} | {p2} |\n"

    md_content += """
---

## ⚖️ 3. Règlement Officiel de la LFF : Modèle de Power Ranking Club

### A. Règle d'or anti-mercenariat (« No Buying PR »)
À l'instar du système de référence de Fandom Esports et du Championnat des Constructeurs de Formule 1 :
1. **Points attribués sous contrat uniquement** : Un club n'engrange de points PR qu'à travers les compétitions jouées par un joueur **pendant** sa période de contrat officiel.
2. **Aucun rachat rétroactif** : Si un club recrute un joueur en milieu d'année avec 40 000 points PR, le club ne bénéficie pas de ses points passés. Le joueur commence à marquer pour le club dès la date officielle de signature.
3. **Points acquis inaliénables** : Si un joueur quitte le club le 31 juillet, les points qu'il a rapportés entre le 1er janvier et le 31 juillet restent définitivement acquis au club dans le classement de la saison en cours.

### B. Éligibilité des Rosters : 100% Ouvert à l'International
* **Règle fondamentale** : Les joueurs sous contrat avec un club français **n'ont pas besoin d'être français**.
* Tout joueur professionnel étranger (européen ou international) signé dans un club français rapporte **l'intégralité de ses points de Power Ranking** à son club, avec les mêmes barèmes qu'un joueur tricolore.
* *Exemples historiques :* Le roster galactique 2024 de la **Karmine Corp** composé de Malibuca (RU), Merstach (LV), Veno (UK) et SwizzY (RU) a rapporté 100% de ses points au club français pour le sacrer Champion de France 2024. De même pour les recrues internationales de **Gentle Mates** ou de **Solary**.

### C. Formule de Calcul du Power Ranking LFF
Deux classements coexistent pour une visibilité totale :
* **Classement Annuel (LFF Championship)** : Cumul des points officiels marqués au cours de l'année civile (1er janvier au 31 décembre). Pour garantir l'équité entre clubs de tailles différentes, seuls les points des **Top 4 joueurs les plus performants** du club sont retenus par tranche de tournois.
* **Classement Dynamique (LFF Live PR)** : Moyenne pondérée du PR instantané des joueurs actifs actuels du club (pour visualiser la force de frappe du club aujourd'hui).

---

## 🔍 4. Protocole de Veille & Contrôle des Transferts
Pour garantir l'exactitude des effectifs en continu, la veille repose sur trois piliers :
1. **Le compte X `@FortniteFraActu`** : L'alerte en temps réel des départs (*parting ways*), annonces de recherche de structure (*LF Org*) et signatures officielles (*signing*).
2. **Liquipedia Fortnite (`Portal:Teams/Europe` et `Category:French_Teams`)** : Validation encyclopédique de l'officialisation du contrat et des dates d'arrivée/départ.
3. **Fortnite Tracker (`fortnitetracker.com/esports`)** : Récupération des scores de Power Ranking et attribution des performances de tournois (FNCS, Cash Cups, etc.).

---

## 🛡️ 5. Annuaire des Clubs Engagés (LFF Roster)
"""

    for c in clubs:
        md_content += f"### {c['name']} (`{c['tag']}`)\n"
        md_content += f"- **Division / Tier** : {c.get('tier', 'N/A')}\n"
        md_content += f"- **Statut** : {c.get('status', 'Active')}\n"
        md_content += f"- **Réseaux / Contact** : {c.get('x_handle', 'N/A')}\n"
        if c.get("liquipedia_url"):
            md_content += f"- **Liquipedia** : [{c['name']}]({c['liquipedia_url']})\n"
        if c.get("logo_path"):
            md_content += f"- **Logo enregistré** : `{c['logo_path']}`\n"
        md_content += f"- **Description** : {c.get('description', '')}\n\n"

    report_path = BASE_DIR / "CLASSEMENT_LFF.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"📄 Rapport complet exporté dans : {report_path}")

def sync_liquipedia_transfers():
    """Appelle le scanner de transferts Liquipedia et met à jour les rosters."""
    try:
        from lff_transfer_tracker import scan_transfers
        scan_transfers(filter_fr=True, sync=True)
    except Exception as e:
        print(f"[!] Erreur lors de la synchronisation Liquipedia : {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python lff_engine.py [option]")
        print("  --palmares         : Afficher le palmarès historique (2018-2025)")
        print("  --clubs            : Lister tous les clubs LFF répertoriés")
        print("  --roster <club_id> : Afficher l'effectif actuel d'un club")
        print("  --export           : Générer le document récapitulatif CLASSEMENT_LFF.md")
        print("  --sync-liquipedia  : Scanner et synchroniser les transferts depuis Liquipedia")
        print("  --add-arrival <club_id> <player_ign>   : Enregistrer manuellement une arrivée")
        print("  --add-departure <club_id> <player_ign> : Enregistrer manuellement un départ")
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--palmares":
        show_palmares()
    elif arg == "--clubs":
        list_clubs()
    elif arg == "--roster" and len(sys.argv) >= 3:
        show_roster(sys.argv[2])
    elif arg == "--export":
        export_markdown_report()
    elif arg == "--sync-liquipedia":
        sync_liquipedia_transfers()
    elif arg == "--add-arrival" and len(sys.argv) >= 4:
        record_transfer(sys.argv[2], sys.argv[3], t_type="Arrival")
    elif arg == "--add-departure" and len(sys.argv) >= 4:
        record_transfer(sys.argv[2], sys.argv[3], t_type="Departure")
    else:
        print("[!] Commande non reconnue.")

if __name__ == "__main__":
    main()
