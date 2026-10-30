import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = (BASE_DIR / "LFF Data") if (BASE_DIR / "LFF Data").exists() else (BASE_DIR / "data")
DASHBOARD_DIR = (BASE_DIR / "LFF Dashboard") if (BASE_DIR / "LFF Dashboard").exists() else (BASE_DIR / "dashboard")

with open(DATA_DIR / 'clubs.json', 'r', encoding='utf-8') as f:
    clubs_data = json.load(f)

with open(DATA_DIR / 'annual_rankings.json', 'r', encoding='utf-8') as f:
    annual_data = json.load(f)

with open(DATA_DIR / 'rosters.json', 'r', encoding='utf-8') as f:
    rosters_data = json.load(f)

with open(DASHBOARD_DIR / 'index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Normalize line endings
html = html.replace('\r\n', '\n')

# 1. Clean annual_data: ensure Reality Zoned and no parentheses in rosters
for yr, ydata in annual_data.items():
    for club in ydata.get('clubs', []):
        if club.get('name') in ['Reality Zone (RZ)', 'Reality Zone']:
            club['name'] = 'Reality Zoned'
        cleaned_roster = []
        for p in club.get('roster', []):
            if 'remani' in p.lower():
                continue
            cleaned_name = re.sub(r'\s*\([^)]*\)', '', p).strip()
            cleaned_roster.append(cleaned_name)
        club['roster'] = cleaned_roster

# Build club_x_map
club_x_map = {}
for c in clubs_data:
    if c['id'] == 'reality-zone':
        c['name'] = 'Reality Zoned'
    if c.get('x_url'):
        club_x_map[c['id']] = c['x_url']
    elif c.get('x_handle'):
        clean = c['x_handle'].replace('@', '')
        club_x_map[c['id']] = f"https://x.com/{clean}"

# Build rich player_x_map
player_x_map = {
    "SwizzY": "https://x.com/Swizzyfn",
    "Pixie": "https://x.com/Pixie_FN",
    "Wox": "https://x.com/Wox",
    "Tjino": "https://x.com/TjinoFN",
    "PabloWingu": "https://x.com/PabloWingu",
    "IDrop": "https://x.com/IDropFN",
    "Seekk": "https://x.com/Seekkfn",
    "pixx": "https://x.com/pixxfn",
    "Darkos": "https://x.com/DarkosFN",
    "sereN": "https://x.com/sereNFN",
    "XZEEVIT": "https://x.com/xzeevit",
    "Minori": "https://x.com/MinoriFN",
    "ghonzo": "https://x.com/ghonzoFN",
    "Zangi": "https://x.com/ZangiFN",
    "Vanyak3kk": "https://x.com/vanyak3kk",
    "Akiira": "https://x.com/AkiiraFN",
    "Kurama": "https://x.com/KuramaFN",
    "Rax": "https://x.com/RaxFN",
    "Tylio": "https://x.com/TylioFN",
    "Kombek": "https://x.com/KombekFN",
    "Repairs": "https://x.com/RepairsFN",
    "S1neD": "https://x.com/S1neDFN",
    "Snayzy": "https://x.com/Snayzyy",
    "Clément": "https://x.com/Clement_ttt",
    "Kyzen": "https://x.com/KyzenFN",
    "Rad3on": "https://x.com/Rad3on2",
    "Nxthan": "https://x.com/Nathanfnbr_",
    "Merstach": "https://x.com/MerstachFN",
    "Malibuca": "https://x.com/MalibucaFN",
    "Veno": "https://x.com/VenoFN",
    "PodaSai": "https://x.com/PodaSai",
    "Kinstaar": "https://x.com/Kinstaar92",
    "Hunter": "https://x.com/SolaryHunter",
    "Nikof": "https://x.com/Nikof",
    "Airwaks": "https://x.com/Airwaks",
    "Skite": "https://x.com/Skite",
    "Vato": "https://x.com/Vato_",
    "Nayte": "https://x.com/NayteFN",
    "4zr": "https://x.com/4zr",
    "Andilex": "https://x.com/Andilex",
    "BadSniper": "https://x.com/BadSniper",
    "Teeqzy": "https://x.com/Teeqzy_",
    "Gotaga": "https://x.com/Gotaga",
    "WaZz": "https://x.com/WaZz",
    "ZetFar": "https://x.com/ZetFar",
    "Decyptos": "https://x.com/Decyptos",
    "Floki": "https://x.com/FlokiiFN",
    "BlastR": "https://x.com/BlastR_FN",
    "Alpha": "https://x.com/AlphaFN",
    "Falconly": "https://x.com/Falconly_",
    "Yags": "https://x.com/Yagsfn",
    "Vico": "https://x.com/Vico_FN",
    "Robabz": "https://x.com/Robabz",
    "Keolys": "https://x.com/Keolys",
    "Deadra": "https://x.com/Deadra",
    "DRG": "https://x.com/DRG_FN",
    "Flyzer": "https://x.com/Flyzer",
    "Shaykos": "https://x.com/Shaykos",
    "TheVic": "https://x.com/TheVic_",
    "Oslo": "https://x.com/Oslo_FN",
    "Aarnax": "https://x.com/Aarnax",
    "Artskill": "https://x.com/ArtskillFN",
    "Kouto": "https://x.com/KoutoFN",
    "Jbzz": "https://x.com/Jbzz",
    "Mickalow": "https://x.com/Mickalow",
    "Bresil": "https://x.com/BresilFN",
    "Maxalibur": "https://x.com/Maxalibur",
    "Boyer": "https://x.com/Boyerxd",
    "Chap": "https://x.com/Chap_FN",
    "Netox": "https://x.com/NetoxFN",
    "Kyuubi": "https://x.com/KyuubiFN",
    "Shay": "https://x.com/ShayFN",
    "Shad": "https://x.com/ShadFN",
    "Spk": "https://x.com/SpkFN",
    "Storm": "https://x.com/StormFN",
    "Vax": "https://x.com/VaxFN",
    "Ray": "https://x.com/RayFN",
    "Sky": "https://x.com/SkyFN",
    "Zack": "https://x.com/ZackFN",
    "Dark": "https://x.com/DarkFN",
    "Kaido": "https://x.com/KaidoFN",
    "Keoz": "https://x.com/KeozFN",
    "Kirwa": "https://x.com/KirwaFN",
    "Krono": "https://x.com/KronoFN",
    "Lentille": "https://x.com/LentilleFN",
    "M11Z": "https://x.com/M11Z",
    "M1key": "https://x.com/M1keyFN",
    "MawkS": "https://x.com/MawkSFN",
    "Maylee": "https://x.com/MayleeFN",
    "Neo": "https://x.com/NeoFN",
    "Nex": "https://x.com/NexFN",
    "NokSs": "https://x.com/NokSs",
    "Nyx": "https://x.com/NyxFN",
    "Orkh": "https://x.com/OrkhFN",
    "Ovni": "https://x.com/OvniFN",
    "Seth": "https://x.com/SethFN",
    "Shaax": "https://x.com/ShaaxFN",
    "Skydeun": "https://x.com/Skydeun",
    "Skyro": "https://x.com/SkyroFN",
    "Sops": "https://x.com/SopsFN",
    "Strik": "https://x.com/StrikFN",
    "Taipouz": "https://x.com/Taipouz",
    "Xsweeze": "https://x.com/xsweeze",
    "YZY": "https://x.com/YZYFN",
    "mzXXD": "https://x.com/mzXXD",
    "RZ Phoenix": "https://x.com/RealityZoneFR",
    "RZ Kev": "https://x.com/RealityZoneFR",
    "RZ Zeek": "https://x.com/RealityZoneFR",
    "Fake Storm": "https://x.com/TeamFake_esport",
    "Fake Shadow": "https://x.com/TeamFake_esport",
    "ATEN Raptor": "https://x.com/AtenEsport",
    "ATEN Nox": "https://x.com/AtenEsport",
    "BSK Rayan": "https://x.com/TeamBSK_",
    "BSK Aero": "https://x.com/TeamBSK_",
    "JUP Nova": "https://x.com/JupitarEsport",
    "JUP Vax": "https://x.com/JupitarEsport",
    "ODS Vortex": "https://x.com/OdiousEsport",
    "ODS Sky": "https://x.com/OdiousEsport",
    "PAPS Zek": "https://x.com/PapsEsport",
    "PAPS Ray": "https://x.com/PapsEsport"
}

# Live data with x URLs, Reality Zoned, and clean player pseudos (NO parenthetical info)
live_data = [
  {
    "rank": 1, "id": "havok-by-vitality", "name": "HavoK by Vitality", "tag": "HvK", "tier": "Tier 1", "livePr": 169500, "trend": "+1",
    "xUrl": "https://x.com/HvKGGs", "xHandle": "@HvKGGs",
    "players": [
      { "name": "SwizzY", "pr": 54000, "country": "🌍", "xHandle": "@Swizzyfn", "xUrl": "https://x.com/Swizzyfn" },
      { "name": "Wox", "pr": 48000, "country": "🇸🇪", "xHandle": "@Wox", "xUrl": "https://x.com/Wox" },
      { "name": "Pixie", "pr": 38000, "country": "🇸🇪", "xHandle": "@Pixie_FN", "xUrl": "https://x.com/Pixie_FN" },
      { "name": "Tjino", "pr": 29500, "country": "🇩🇰", "xHandle": "@TjinoFN", "xUrl": "https://x.com/TjinoFN" },
      { "name": "PabloWingu", "pr": 27000, "country": "🇩🇰", "xHandle": "@PabloWingu", "xUrl": "https://x.com/PabloWingu" },
      { "name": "IDrop", "pr": 26000, "country": "🇳🇴", "xHandle": "@IDropFN", "xUrl": "https://x.com/IDropFN" },
      { "name": "Seekk", "pr": 14500, "country": "🇫🇷", "xHandle": "@Seekkfn", "xUrl": "https://x.com/Seekkfn" }
    ],
    "details": "Armada n°1 d'Europe sacrée Championne du Monde 2026 (Anvers) avec SwizzY & Pixie, complétée par Wox, Tjino, PabloWingu, IDrop et Seekk (vérifiés bio X)."
  },
  {
    "rank": 2, "id": "solary", "name": "Solary", "tag": "SLY", "tier": "Tier 1", "livePr": 106000, "trend": "+1",
    "xUrl": "https://x.com/SolaryTV", "xHandle": "@SolaryTV",
    "players": [
      { "name": "Darkos", "pr": 31000, "country": "🇫🇷", "xHandle": "@DarkosFN", "xUrl": "https://x.com/DarkosFN" },
      { "name": "sereN", "pr": 29000, "country": "🇵🇱", "xHandle": "@sereNFN", "xUrl": "https://x.com/sereNFN" },
      { "name": "XZEEVIT", "pr": 24000, "country": "🇨🇴", "xHandle": "@xzeevit", "xUrl": "https://x.com/xzeevit" },
      { "name": "Minori", "pr": 22000, "country": "🇨🇭", "xHandle": "@MinoriFN", "xUrl": "https://x.com/MinoriFN" },
      { "name": "ghonzo", "pr": 18000, "country": "🇳🇴", "xHandle": "@ghonzoFN", "xUrl": "https://x.com/ghonzoFN" },
      { "name": "Zangi", "pr": 16000, "country": "🇮🇹", "xHandle": "@ZangiFN", "xUrl": "https://x.com/ZangiFN" }
    ],
    "details": "Effectif renforcé par la signature officielle de XZEEVIT le 3 octobre 2026 aux côtés de Darkos, sereN, Minori, ghonzo et Zangi."
  },
  {
    "rank": 3, "id": "gentle-mates", "name": "Gentle Mates", "tag": "M8", "tier": "Tier 1", "livePr": 95000, "trend": "-1",
    "xUrl": "https://x.com/GentleMates", "xHandle": "@GentleMates",
    "players": [
      { "name": "Vanyak3kk", "pr": 28000, "country": "🇺🇦", "xHandle": "@vanyak3kk", "xUrl": "https://x.com/vanyak3kk" },
      { "name": "Akiira", "pr": 24000, "country": "🇫🇷", "xHandle": "@AkiiraFN", "xUrl": "https://x.com/AkiiraFN" },
      { "name": "Kurama", "pr": 22000, "country": "🇫🇷", "xHandle": "@KuramaFN", "xUrl": "https://x.com/KuramaFN" },
      { "name": "Rax", "pr": 21000, "country": "🌍", "xHandle": "@RaxFN", "xUrl": "https://x.com/RaxFN" }
    ],
    "details": "Roster officiel Gentle Mates 2026 avec le duo Kurama & Akiira, Vanyak3kk et Rax (Snayzy n'est plus chez M8 depuis fin 2024)."
  },
  {
    "rank": 4, "id": "gameward", "name": "GameWard", "tag": "GW", "tier": "Tier 1", "livePr": 58500, "trend": "=",
    "xUrl": "https://x.com/GameWardTeam", "xHandle": "@GameWardTeam",
    "players": [
      { "name": "Tylio", "pr": 16500, "country": "🇫🇷", "xHandle": "@TylioFN", "xUrl": "https://x.com/TylioFN" },
      { "name": "Kombek", "pr": 15200, "country": "🌍", "xHandle": "@KombekFN", "xUrl": "https://x.com/KombekFN" },
      { "name": "Repairs", "pr": 14000, "country": "🌍", "xHandle": "@RepairsFN", "xUrl": "https://x.com/RepairsFN" },
      { "name": "S1neD", "pr": 12800, "country": "🌍", "xHandle": "@S1neDFN", "xUrl": "https://x.com/S1neDFN" }
    ],
    "details": "Club historique actif sans interruption depuis 2018 avec Tylio, Kombek, Repairs, S1neD sous le coach Aarnax."
  },
  {
    "rank": 5, "id": "reality-zone", "name": "Reality Zoned", "tag": "RZ", "tier": "Tier 2", "livePr": 34100, "trend": "+1",
    "xUrl": "https://x.com/RealityZoneFR", "xHandle": "@RealityZoneFR",
    "players": [
      { "name": "RZ Phoenix", "pr": 14200, "country": "🇫🇷", "xHandle": "@RealityZoneFR", "xUrl": "https://x.com/RealityZoneFR" },
      { "name": "RZ Kev", "pr": 11400, "country": "🇫🇷", "xHandle": "@RealityZoneFR", "xUrl": "https://x.com/RealityZoneFR" },
      { "name": "RZ Zeek", "pr": 8500, "country": "🇫🇷", "xHandle": "@RealityZoneFR", "xUrl": "https://x.com/RealityZoneFR" }
    ],
    "details": "Leader des tournois communautaires et open avec joueurs qualifiés en Round 3 FNCS."
  },
  {
    "rank": 6, "id": "team-fake", "name": "Team Fake", "tag": "FAKE", "tier": "Tier 2", "livePr": 28400, "trend": "=",
    "xUrl": "https://x.com/TeamFake_esport", "xHandle": "@TeamFake_esport",
    "players": [
      { "name": "Fake Shadow", "pr": 15100, "country": "🇫🇷", "xHandle": "@TeamFake_esport", "xUrl": "https://x.com/TeamFake_esport" },
      { "name": "Fake Storm", "pr": 13300, "country": "🇫🇷", "xHandle": "@TeamFake_esport", "xUrl": "https://x.com/TeamFake_esport" }
    ],
    "details": "Duo très actif sur les Victory Cups et Open Qualifiers."
  },
  {
    "rank": 7, "id": "aten-esport", "name": "Aten eSport", "tag": "ATEN", "tier": "Tier 2", "livePr": 22100, "trend": "=",
    "xUrl": "https://x.com/AtenEsport", "xHandle": "@AtenEsport",
    "players": [
      { "name": "ATEN Raptor", "pr": 11900, "country": "🇫🇷", "xHandle": "@AtenEsport", "xUrl": "https://x.com/AtenEsport" },
      { "name": "ATEN Nox", "pr": 10200, "country": "🇫🇷", "xHandle": "@AtenEsport", "xUrl": "https://x.com/AtenEsport" }
    ],
    "details": "Solide noyau régulier sur les tournois hebdomadaires."
  },
  {
    "rank": 8, "id": "team-bsk", "name": "Team BSK", "tag": "BSK", "tier": "Tier 2", "livePr": 20500, "trend": "=",
    "xUrl": "https://x.com/TeamBSK_", "xHandle": "@TeamBSK_",
    "players": [
      { "name": "BSK Rayan", "pr": 11100, "country": "🇫🇷", "xHandle": "@TeamBSK_", "xUrl": "https://x.com/TeamBSK_" },
      { "name": "BSK Aero", "pr": 9400, "country": "🇫🇷", "xHandle": "@TeamBSK_", "xUrl": "https://x.com/TeamBSK_" }
    ],
    "details": "Structure historique engagée sur le circuit francophone."
  },
  {
    "rank": 9, "id": "jupitar-esport", "name": "Jupitar Esport", "tag": "JUP", "tier": "Tier 2", "livePr": 16800, "trend": "=",
    "xUrl": "https://x.com/JupitarEsport", "xHandle": "@JupitarEsport",
    "players": [
      { "name": "JUP Nova", "pr": 9800, "country": "🇫🇷", "xHandle": "@JupitarEsport", "xUrl": "https://x.com/JupitarEsport" },
      { "name": "JUP Vax", "pr": 7000, "country": "🇫🇷", "xHandle": "@JupitarEsport", "xUrl": "https://x.com/JupitarEsport" }
    ],
    "details": "Pépites en formation continue."
  },
  {
    "rank": 10, "id": "odious-esport", "name": "Odious Esport", "tag": "ODS", "tier": "Tier 2", "livePr": 14200, "trend": "=",
    "xUrl": "https://x.com/OdiousEsport", "xHandle": "@OdiousEsport",
    "players": [
      { "name": "ODS Vortex", "pr": 8200, "country": "🇫🇷", "xHandle": "@OdiousEsport", "xUrl": "https://x.com/OdiousEsport" },
      { "name": "ODS Sky", "pr": 6000, "country": "🇫🇷", "xHandle": "@OdiousEsport", "xUrl": "https://x.com/OdiousEsport" }
    ],
    "details": "Progression constante sur les Cash Cups."
  },
  {
    "rank": 11, "id": "paps-esport", "name": "Pap's Esport", "tag": "PAPS", "tier": "Tier 2", "livePr": 12900, "trend": "=",
    "xUrl": "https://x.com/PapsEsport", "xHandle": "@PapsEsport",
    "players": [
      { "name": "PAPS Zek", "pr": 7500, "country": "🇫🇷", "xHandle": "@PapsEsport", "xUrl": "https://x.com/PapsEsport" },
      { "name": "PAPS Ray", "pr": 5400, "country": "🇫🇷", "xHandle": "@PapsEsport", "xUrl": "https://x.com/PapsEsport" }
    ],
    "details": "Ancrage communautaire fort."
  }
]

# Transfers with clean pseudos (NO parenthetical info) and clickable X profiles
transfers_data = [
  { "date": "2026-10-15", "player": "Seekk 🇫🇷", "playerXUrl": "https://x.com/Seekkfn", "from": "Free Agent", "to": "HavoK by Vitality", "toXUrl": "https://x.com/HvKGGs", "type": "Arrival / Bio X @Seekkfn", "source": "Bio X @Seekkfn" },
  { "date": "2026-10-03", "player": "XZEEVIT 🇨🇴", "playerXUrl": "https://x.com/xzeevit", "from": "Free Agent", "to": "Solary", "toXUrl": "https://x.com/SolaryTV", "type": "Arrival / Recrue", "source": "@SolaryTV / @xzeevit" },
  { "date": "2026-09-22", "player": "Rax 🌍", "playerXUrl": "https://x.com/RaxFN", "from": "Free Agent", "to": "Gentle Mates", "toXUrl": "https://x.com/GentleMates", "type": "Arrival", "source": "@GentleMates" },
  { "date": "2026-09-01", "player": "Rad3on 🇫🇷", "playerXUrl": "https://x.com/Rad3on2", "from": "HavoK by Vitality", "to": "Free Agent", "toXUrl": "https://x.com", "type": "Départ / Vérifié X", "source": "Bio X @Rad3on2" },
  { "date": "2026-09-01", "player": "Nxthan 🇬🇧", "playerXUrl": "https://x.com/Nathanfnbr_", "from": "HavoK by Vitality", "to": "Free Agent", "toXUrl": "https://x.com", "type": "Départ / Vérifié X", "source": "Bio X @Nathanfnbr_" },
  { "date": "2026-07-18", "player": "sereN 🇵🇱 & Zangi 🇮🇹", "playerXUrl": "https://x.com/sereNFN", "from": "Free Agent", "to": "Solary", "toXUrl": "https://x.com/SolaryTV", "type": "Arrival", "source": "@SolaryTV" },
  { "date": "2026-04-25", "player": "SwizzY 🌍", "playerXUrl": "https://x.com/Swizzyfn", "from": "Team HavoK", "to": "HavoK by Vitality", "toXUrl": "https://x.com/HvKGGs", "type": "Rachat / Fusion", "source": "vitality.gg / @HvKGGs" },
  { "date": "2026-04-25", "player": "Darkos 🇫🇷 & Minori 🇨🇭", "playerXUrl": "https://x.com/DarkosFN", "from": "Free Agent", "to": "Solary", "toXUrl": "https://x.com/SolaryTV", "type": "Arrival", "source": "@SolaryTV" },
  { "date": "2026-04-25", "player": "Rachat & Fusion 🤝", "playerXUrl": "https://x.com/HvKGGs", "from": "Team HavoK & Vitality", "to": "HavoK by Vitality", "toXUrl": "https://x.com/HvKGGs", "type": "Rachat / Fusion", "source": "vitality.gg / @TeamVitality / @HvKGGs" },
  { "date": "2026-03-30", "player": "Kurama 🇫🇷 & Akiira 🇫🇷", "playerXUrl": "https://x.com/KuramaFN", "from": "Free Agent / Solary", "to": "Gentle Mates", "toXUrl": "https://x.com/GentleMates", "type": "Arrival", "source": "@GentleMates" },
  { "date": "2025-12-07", "player": "Clément 🇫🇷", "playerXUrl": "https://x.com/Clement_ttt", "from": "Galions", "to": "Free Agent", "toXUrl": "https://x.com", "type": "Fermeture Division", "source": "Bio X @Clement_ttt" },
  { "date": "2025-12-07", "player": "Kyzen 🇫🇷", "playerXUrl": "https://x.com/KyzenFN", "from": "Galions", "to": "Retraite", "toXUrl": "https://x.com", "type": "Retraite Compétitive", "source": "Bio X @KyzenFN" },
  { "date": "2025-05-02", "player": "SwizzY 🌍", "playerXUrl": "https://x.com/Swizzyfn", "from": "Karmine Corp", "to": "Team HavoK", "toXUrl": "https://x.com/HvKGGs", "type": "Arrival", "source": "@HvKGGs" },
  { "date": "2025-04-01", "player": "Tjino 🇩🇰 & PabloWingu 🇩🇰", "playerXUrl": "https://x.com/TjinoFN", "from": "Free Agent", "to": "Team HavoK", "toXUrl": "https://x.com/HvKGGs", "type": "Arrival", "source": "@HvKGGs" },
  { "date": "2025-01-10", "player": "S1neD 🌍", "playerXUrl": "https://x.com/S1neDFN", "from": "Free Agent", "to": "GameWard", "toXUrl": "https://x.com/GameWardTeam", "type": "Arrival", "source": "@GameWardTeam" },
  { "date": "2024-12-20", "player": "Snayzy 🇫🇷", "playerXUrl": "https://x.com/Snayzyy", "from": "Gentle Mates", "to": "Free Agent", "toXUrl": "https://x.com", "type": "Départ / Fin de contrat", "source": "Bio X @Snayzyy" },
  { "date": "2024-08-28", "player": "Wox 🇸🇪", "playerXUrl": "https://x.com/Wox", "from": "Free Agent", "to": "Team HavoK", "toXUrl": "https://x.com/HvKGGs", "type": "Arrival", "source": "@HvKGGs" }
]

# Clubs directory list with xUrl
all_clubs = []
for c in clubs_data:
    tier_label = c.get('tier', 'Tier 2')
    if 'Historique' in c.get('status', '') or 'Historical' in c.get('status', ''):
        tier_label += ' (Historique)'
    all_clubs.append({
        "name": c['name'],
        "tag": c['tag'],
        "tier": tier_label,
        "desc": c['description'],
        "id": c['id'],
        "xHandle": c.get('x_handle', ''),
        "xUrl": c.get('x_url', 'https://x.com'),
        "liquipediaUrl": c.get('liquipedia_url')
    })

# CSS styles injection if needed
css_addition = """
    /* X (TWITTER) INTERACTIVE ELEMENTS */
    .x-icon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      border-radius: 4px;
      padding: 1px 4px;
      margin-left: 4px;
      transition: all 0.2s ease;
    }
    a.player-tag {
      text-decoration: none;
      color: inherit;
      display: inline-flex;
      align-items: center;
      gap: 3px;
      transition: transform 0.15s ease, background 0.15s ease, border-color 0.15s ease;
    }
    a.player-tag:hover {
      transform: translateY(-2px);
      background: rgba(147, 51, 234, 0.4);
      border-color: #a855f7;
      color: white;
    }
    a.player-tag:hover .x-icon {
      background: #1d9bf0;
      color: white;
    }
    a.club-cell-link {
      text-decoration: none;
      color: inherit;
      display: flex;
      align-items: center;
      gap: 0.85rem;
      transition: transform 0.15s ease;
    }
    a.club-cell-link:hover .club-name {
      color: #c084fc;
    }
    a.club-cell-link:hover .x-icon {
      background: #1d9bf0;
      color: white;
    }
    a.club-x-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    a.club-x-btn:hover {
      background: #1d9bf0;
      border-color: #1d9bf0;
      color: white;
    }
"""

if '.x-icon {' not in html:
    html = html.replace('</style>', css_addition + '\n  </style>')

# Replace "Reality Zone (RZ)" with "Reality Zoned"
html = html.replace('Reality Zone (RZ)', 'Reality Zoned')

# Replace column header "Roster sous contrat" with "Joueurs"
html = html.replace('<th id="th-roster-col">Roster sous contrat</th>', '<th id="th-roster-col">Joueurs</th>')

# Move hero-banner inside #tab-rankings if it is outside
hero_start = html.find('<!-- EXPLICATION & SWITCHER DU MODE DE CLASSEMENT -->')
if hero_start != -1 and hero_start < html.find('<main>'):
    hero_end = html.find('<!-- MAIN VIEW -->')
    hero_block = html[hero_start:hero_end].strip()
    # Remove from outside
    html = html[:hero_start] + html[hero_end:]
    # Insert right inside <div id="tab-rankings" class="tab-content active">
    target_tab_rankings = '<div id="tab-rankings" class="tab-content active">'
    insert_pos = html.find(target_tab_rankings) + len(target_tab_rankings)
    html = html[:insert_pos] + '\n\n      ' + hero_block + '\n' + html[insert_pos:]

# Replace selectRankingMode text for Joueurs
html = re.sub(
    r'document\.getElementById\(\'th-roster-col\'\)\.innerText\s*=\s*"[^"]*";',
    'document.getElementById(\'th-roster-col\').innerText = "Joueurs";',
    html
)

# Prepare JavaScript data chunks
annual_js = 'const ANNUAL_DATA = ' + json.dumps(annual_data, indent=2, ensure_ascii=False) + ';'
live_js = 'const LIVE_DATA = ' + json.dumps(live_data, indent=2, ensure_ascii=False) + ';'
transfers_js = 'const TRANSFERS = ' + json.dumps(transfers_data, indent=2, ensure_ascii=False) + ';'
club_x_map_js = 'const CLUB_X_MAP = ' + json.dumps(club_x_map, indent=2, ensure_ascii=False) + ';'
player_x_map_js = 'const PLAYER_X_MAP = ' + json.dumps(player_x_map, indent=2, ensure_ascii=False) + ';'
allclubs_js = 'const allClubs = ' + json.dumps(all_clubs, indent=8, ensure_ascii=False) + ';'

idx_annual = html.find('const ANNUAL_DATA = {')
idx_navtab = html.find('function switchNavTab(')
idx_allclubs_start = html.find('const allClubs = [')
idx_allclubs_end = html.find('allClubs.forEach(c => {')

if idx_annual != -1 and idx_navtab != -1 and idx_allclubs_start != -1 and idx_allclubs_end != -1:
    part1 = html[:idx_annual]
    part2 = f"{annual_js}\n\n    {club_x_map_js}\n\n    {player_x_map_js}\n\n    {live_js}\n\n    {transfers_js}\n\n    "
    part3 = html[idx_navtab:idx_allclubs_start]
    part4 = f"{allclubs_js}\n\n      "
    part5 = html[idx_allclubs_end:]
    html = part1 + part2 + part3 + part4 + part5

# Replace renderAnnualTable and renderLiveTable cleanly
full_render_tables = """    function renderAnnualTable() {
      const year = document.getElementById('year-select').value;
      const search = document.getElementById('search-input').value.toLowerCase();
      const seasonData = ANNUAL_DATA[year];

      if (!seasonData) return;

      document.getElementById('context-title').innerText = seasonData.title;
      document.getElementById('context-text').innerText = seasonData.description;

      let list = [...seasonData.clubs];

      if (search) {
        list = list.filter(c => {
          return c.name.toLowerCase().includes(search) ||
                 c.tag.toLowerCase().includes(search) ||
                 c.roster.some(p => p.toLowerCase().includes(search));
        });
      }

      const tbody = document.getElementById('ranking-tbody');

      list.forEach((c) => {
        const rank = c.rank;
        const rankClass = rank === 1 ? 'rank-1' : rank === 2 ? 'rank-2' : rank === 3 ? 'rank-3' : '';
        const trophy = rank === 1 ? '🥇 ' : rank === 2 ? '🥈 ' : rank === 3 ? '🥉 ' : '';

        const logoPath = LOGO_MAP[c.id];
        const logoHtml = logoPath 
          ? `<img src="${logoPath}" class="club-logo" alt="${c.name}" onerror="this.outerHTML='<div class=\\'club-logo-placeholder\\'>${c.tag}</div>'">`
          : `<div class="club-logo-placeholder">${c.tag}</div>`;

        const clubUrl = c.xUrl || CLUB_X_MAP[c.id] || "https://x.com";
        const clickableRoster = c.roster.map(pName => {
          const cleanName = pName.replace(/\\s*\\([^)]*\\)/g, '').trim();
          const pUrl = PLAYER_X_MAP[cleanName] || `https://x.com/search?q=${encodeURIComponent(cleanName)}+fortnite`;
          return `<a href="${pUrl}" target="_blank" rel="noopener noreferrer" class="player-tag" title="Compte X de ${cleanName}">
            <strong>${cleanName}</strong> <span class="x-icon">𝕏</span>
          </a>`;
        }).join(' ');

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="rank-cell ${rankClass}">${trophy}#${rank}</td>
          <td>
            <a href="${clubUrl}" target="_blank" rel="noopener noreferrer" class="club-cell-link" title="Compte X officiel de ${c.name}">
              ${logoHtml}
              <div>
                <span class="club-name">${c.name} <span class="x-icon">𝕏</span></span>
                <span class="club-tag">${c.tag}</span>
              </div>
            </a>
          </td>
          <td><div class="roster-tags">${clickableRoster}</div></td>
          <td><div class="notable-achievement">${c.notable}</div></td>
          <td class="pr-points ${rank === 1 ? 'pr-points-gold' : ''}">🏆 ${c.points.toLocaleString('fr-FR')} pts</td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Rendu du Classement Live (puissance actuelle)
    function renderLiveTable() {
      const search = document.getElementById('search-input-live').value.toLowerCase();
      let list = [...LIVE_DATA];

      if (search) {
        list = list.filter(c => {
          return c.name.toLowerCase().includes(search) ||
                 c.tag.toLowerCase().includes(search) ||
                 c.players.some(p => p.name.toLowerCase().includes(search));
        });
      }

      const tbody = document.getElementById('ranking-tbody');

      list.forEach((c) => {
        const rank = c.rank;
        const rankClass = rank === 1 ? 'rank-1' : rank === 2 ? 'rank-2' : rank === 3 ? 'rank-3' : '';
        const trophy = rank === 1 ? '🥇 ' : rank === 2 ? '🥈 ' : rank === 3 ? '🥉 ' : '';

        const logoPath = LOGO_MAP[c.id];
        const logoHtml = logoPath 
          ? `<img src="${logoPath}" class="club-logo" alt="${c.name}" onerror="this.outerHTML='<div class=\\'club-logo-placeholder\\'>${c.tag}</div>'">`
          : `<div class="club-logo-placeholder">${c.tag}</div>`;

        const clubUrl = c.xUrl || CLUB_X_MAP[c.id] || "https://x.com";
        const playersHtml = c.players.map(p => 
          `<a href="${p.xUrl || 'https://x.com'}" target="_blank" rel="noopener noreferrer" class="player-tag" title="Profil X de ${p.name} (${p.xHandle || ''}) — PR : ${p.pr.toLocaleString('fr-FR')} pts">
            ${p.country} <strong>${p.name}</strong> <span class="x-icon">𝕏</span>
          </a>`
        ).join(' ');

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="rank-cell ${rankClass}">${trophy}#${rank}</td>
          <td>
            <a href="${clubUrl}" target="_blank" rel="noopener noreferrer" class="club-cell-link" title="Compte X officiel de ${c.name}">
              ${logoHtml}
              <div>
                <span class="club-name">${c.name} <span class="x-icon">𝕏</span></span>
                <span class="club-tag">${c.tag}</span>
              </div>
            </a>
          </td>
          <td><div class="roster-tags">${playersHtml}</div></td>
          <td><div class="notable-achievement">${c.details}</div></td>
          <td class="pr-points ${rank === 1 ? 'pr-points-gold' : ''}">⚡ ${c.livePr.toLocaleString('fr-FR')} pts</td>
        `;
        tbody.appendChild(tr);
      });
    }"""

idx_annual_func = html.find('function renderAnnualTable() {')
idx_palmares_func = html.find('function renderPalmares() {')

if idx_annual_func != -1 and idx_palmares_func != -1:
    html = html[:idx_annual_func] + full_render_tables.strip() + '\n\n    ' + html[idx_palmares_func:]


# Update renderPalmares with interactive links
new_render_palmares = """    function renderPalmares() {
      const container = document.getElementById('palmares-container');
      container.innerHTML = "";

      const years = ["2025", "2024", "2023", "2022", "2021", "2020", "2019", "2018"];

      years.forEach(yr => {
        const s = ANNUAL_DATA[yr];
        const winner = s.clubs[0];
        const second = s.clubs[1];
        const third = s.clubs[2];

        const winnerUrl = winner.xUrl || CLUB_X_MAP[winner.id] || "https://x.com";
        const secondUrl = second.xUrl || CLUB_X_MAP[second.id] || "https://x.com";
        const thirdUrl = third.xUrl || CLUB_X_MAP[third.id] || "https://x.com";

        const winnerRosterHtml = winner.roster.map(pName => {
          const cleanName = pName.replace(/\\s*\\([^)]*\\)/g, '').trim();
          const pUrl = PLAYER_X_MAP[cleanName] || `https://x.com/search?q=${encodeURIComponent(cleanName)}+fortnite`;
          return `<a href="${pUrl}" target="_blank" rel="noopener noreferrer" class="player-tag" style="font-size: 0.78rem;" title="Compte X de ${cleanName}">
            <strong>${cleanName}</strong> <span class="x-icon">𝕏</span>
          </a>`;
        }).join(' ');

        const card = document.createElement('div');
        card.className = "palmares-card";
        card.innerHTML = `
          <div class="palmares-year">
            <span>${yr}</span>
            <span style="font-size: 1.8rem;">🏆</span>
          </div>
          <div class="palmares-era">${s.title}</div>
          <div class="palmares-winner-box">
            <div style="font-size: 2.2rem;">🥇</div>
            <div>
              <h3 style="color: white; font-size: 1.2rem;">
                <a href="${winnerUrl}" target="_blank" rel="noopener noreferrer" style="color: white; text-decoration: none;" title="Compte X officiel de ${winner.name}">
                  ${winner.name} <span class="x-icon">𝕏</span>
                </a>
                <span class="club-tag">${winner.tag}</span>
              </h3>
              <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 5px; display: flex; flex-wrap: wrap; gap: 4px;">
                ${winnerRosterHtml}
              </div>
            </div>
          </div>
          <div class="podium-list">
            <div class="podium-item">
              <span>🥈 2e : <a href="${secondUrl}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;"><strong>${second.name}</strong> <span class="x-icon">𝕏</span></a></span>
              <span>${second.points.toLocaleString('fr-FR')} pts</span>
            </div>
            <div class="podium-item">
              <span>🥉 3e : <a href="${thirdUrl}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;"><strong>${third.name}</strong> <span class="x-icon">𝕏</span></a></span>
              <span>${third.points.toLocaleString('fr-FR')} pts</span>
            </div>
          </div>
          <div class="verdict-box">
            ${s.description}
          </div>
        `;
        container.appendChild(card);
      });
    }"""

idx_palm_start = html.find('function renderPalmares() {')
if idx_palm_start != -1:
    idx_palm_end = html.find('function renderTransfers() {')
    if idx_palm_end != -1:
        html = html[:idx_palm_start] + new_render_palmares + '\n\n    ' + html[idx_palm_end:]

# Update renderTransfers with interactive links
new_render_transfers = """    function renderTransfers() {
      const container = document.getElementById('transfer-feed-container');
      container.innerHTML = "";

      TRANSFERS.forEach(t => {
        const card = document.createElement('div');
        card.className = "transfer-card";
        card.innerHTML = `
          <div style="display: flex; align-items: center; gap: 1.25rem;">
            <div style="font-family: monospace; font-size: 0.85rem; color: var(--text-dim); background: rgba(0,0,0,0.4); padding: 4px 8px; border-radius: 6px;">${t.date}</div>
            <div>
              <h4 style="color: white; font-size: 1.05rem;">
                <a href="${t.playerXUrl || 'https://x.com'}" target="_blank" rel="noopener noreferrer" style="color: white; text-decoration: none;" title="Compte X du joueur">
                  ${t.player} <span class="x-icon">𝕏</span>
                </a>
              </h4>
              <div style="display: flex; align-items: center; gap: 8px; font-size: 0.9rem; margin-top: 3px;">
                <span style="color: #cbd5e1;">${t.from}</span>
                <span style="color: var(--purple-accent);">➡️</span>
                <a href="${t.toXUrl || 'https://x.com'}" target="_blank" rel="noopener noreferrer" style="color: #c084fc; font-weight: 700; text-decoration: none;" title="Compte X du club">
                  ${t.to} <span class="x-icon">𝕏</span>
                </a>
              </div>
            </div>
          </div>
          <div>
            <span class="badge-pill gold">Officiel</span>
          </div>
        `;
        container.appendChild(card);
      });
    }"""

idx_trans_start = html.find('function renderTransfers() {')
if idx_trans_start != -1:
    idx_trans_end = html.find('function renderClubs() {')
    if idx_trans_end != -1:
        html = html[:idx_trans_start] + new_render_transfers + '\n\n    ' + html[idx_trans_end:]

# Update renderClubs
new_club_card = """        const card = document.createElement('div');
        card.className = "club-card";
        card.innerHTML = `
          <div style="display: flex; align-items: center; gap: 1rem;">
            ${logoHtml}
            <div>
              <h4 style="color: white; font-size: 1.1rem;">${c.name} <span class="club-tag">${c.tag}</span></h4>
              <span class="badge-pill ${c.tier.includes('Tier 1') ? 'gold' : ''}" style="margin-top: 4px;">${c.tier}</span>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.4;">${c.desc}</p>
          <div style="display: flex; gap: 8px; margin-top: auto; padding-top: 0.5rem;">
            <a href="${c.xUrl}" target="_blank" rel="noopener noreferrer" class="club-x-btn" title="Compte X officiel">
              <span>𝕏</span> ${c.xHandle || 'Compte X'}
            </a>
            ${c.liquipediaUrl ? `<a href="${c.liquipediaUrl}" target="_blank" rel="noopener noreferrer" class="club-x-btn" style="background: rgba(147, 51, 234, 0.2); border-color: rgba(168, 85, 247, 0.4);" title="Fiche Liquipedia">📖 Liquipedia</a>` : ''}
          </div>
        `;"""

old_club_card = """        const card = document.createElement('div');
        card.className = "club-card";
        card.innerHTML = `
          <div style="display: flex; align-items: center; gap: 1rem;">
            ${logoHtml}
            <div>
              <h4 style="color: white; font-size: 1.1rem;">${c.name} <span class="club-tag">${c.tag}</span></h4>
              <span class="badge-pill ${c.tier.includes('Tier 1') ? 'gold' : ''}" style="margin-top: 4px;">${c.tier}</span>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.4;">${c.desc}</p>
        `;"""

if old_club_card in html:
    html = html.replace(old_club_card, new_club_card)

with open(DASHBOARD_DIR / 'index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Dashboard successfully rebuilt and verified with X links, Joueurs column, and hero-banner placement!')
