import json
import re
import subprocess
from pathlib import Path

BASE_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF")
DATA_DIR = BASE_DIR / "LFF Data"
DASH_DIR = BASE_DIR / "LFF Dashboard"

# 1. Load clubs.json to have authoritative club metadata
with open(DATA_DIR / "clubs.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

club_by_id = {c["id"]: c for c in clubs}
name_to_id = {c["name"]: c["id"] for c in clubs}
name_to_id.update({
    "Reality Zoned": "reality-zone",
    "Reality Zone": "reality-zone",
    "Reality Zone (RZ)": "reality-zone",
    "HavoK by Vitality": "havok-by-vitality",
    "Team HavoK": "team-havok",
    "Team GO (GamersOrigin)": "team-go",
    "Team GO": "team-go",
    "Team LDLC (LDLC OL)": "team-ldlc",
    "Team LDLC": "team-ldlc",
    "1P (OneProdige)": "1p-esport",
    "1P Esport": "1p-esport",
    "BK ROG Esports": "bk-rog",
    "Gentside Esports Club": "gentside-esports",
    "DualMedia Esports": "dualmedia-esports",
    "beGenius ESC": "begenius-esc",
    "Orphée Esport": "orphee-esport",
    "MGA eSport": "mga-esport",
    "MGA Esport": "mga-esport",
    "EKINOX": "ekinox-esports"
})

# 2. Load rosters.json
with open(DATA_DIR / "rosters.json", "r", encoding="utf-8") as f:
    rosters_data = json.load(f)

# Build CLUB_X_MAP
club_x_map = {}
for c in clubs:
    cid = c["id"]
    if c.get("x_url"):
        club_x_map[cid] = c["x_url"]
    elif c.get("x_handle"):
        clean = c["x_handle"].replace("@", "")
        club_x_map[cid] = f"https://x.com/{clean}"

# Build PLAYER_X_MAP
player_x_map = {}
for cid, plist in rosters_data.get("active_rosters", {}).items():
    for p in plist:
        ign = p["ign"]
        if p.get("x_url"):
            player_x_map[ign] = p["x_url"]
        elif p.get("x_handle"):
            clean = p["x_handle"].replace("@", "")
            player_x_map[ign] = f"https://x.com/{clean}"

historical_players_x = {
    "Kinstaar": "https://x.com/Kinstaar92",
    "Hunter": "https://x.com/Hunter__FN",
    "Airwaks": "https://x.com/Airwaks",
    "Nikof": "https://x.com/Nikof",
    "Gotaga": "https://x.com/Gotaga",
    "Mickalow": "https://x.com/Mickalow",
    "Robi": "https://x.com/Robi_ow",
    "TheVic": "https://x.com/TheVic_FN",
    "Madzen": "https://x.com/Madzen_FN",
    "Teeqzy": "https://x.com/Teeqzy_",
    "Skite": "https://x.com/Skite",
    "Nayte": "https://x.com/nayteFN",
    "4zr": "https://x.com/4zr",
    "BadSniper": "https://x.com/BadSniper",
    "Andilex": "https://x.com/Andilex",
    "Xsweeze": "https://x.com/xsweeze",
    "PodaSai": "https://x.com/PodaSai",
    "Falconly": "https://x.com/Falconly",
    "Blax": "https://x.com/Blaxou",
    "BlastR": "https://x.com/BlastR_FN",
    "Floki": "https://x.com/Flokito_",
    "Clément": "https://x.com/Clement_ttt",
    "Decypt": "https://x.com/Decypt_",
    "Snayzy": "https://x.com/Snayzyy",
    "Veno": "https://x.com/VenoFN",
    "Malibuca": "https://x.com/Malibuca",
    "Merstach": "https://x.com/Merstach",
    "Vanyak3kk": "https://x.com/Vanyak3kk",
    "SwizzY": "https://x.com/SwizzY281",
    "Pixie": "https://x.com/pixiefnbr",
    "PabloWingu": "https://x.com/PabloWingu",
    "Tjino": "https://x.com/tjino9",
    "Wox": "https://x.com/WoxSHTER",
    "Seekk": "https://x.com/Seekkfn",
    "Akiira": "https://x.com/Akiirafn",
    "MariusCOW": "https://x.com/MariusCOW",
    "Kurama": "https://x.com/Kurama_FN",
    "Ghonzo": "https://x.com/GhonzoFN",
    "Minori": "https://x.com/Minorifn",
    "SkyJump": "https://x.com/SkyJumpFN",
    "Darkos": "https://x.com/Darkos_ftn",
    "XZEEVIT": "https://x.com/xzeevit",
    "xzeevit4k": "https://x.com/xzeevit",
    "Momsy": "https://x.com/MomsyFN",
    "Werex": "https://x.com/WerexFN",
    "Twek": "https://x.com/TwekFN",
    "Borsuk": "https://x.com/BorsukFN",
    "Syaaz": "https://x.com/SyaazFN",
    "Trusio": "https://x.com/TrusioFN",
    "FiTo": "https://x.com/FiTo_fn",
    "iFrOzi": "https://x.com/iFr0zi",
    "Kombek": "https://x.com/KombekFN",
    "Tylio": "https://x.com/TylioFN",
    "Nociff": "https://x.com/NociffFN",
    "S1neD": "https://x.com/S1neDFN",
    "Firen": "https://x.com/FirenFN",
    "Asa": "https://x.com/AsaFN_",
    "Seyyto": "https://x.com/SeyytoFN",
    "Roz": "https://x.com/RozFN_",
    "Izzi": "https://x.com/IzziFN_",
    "Lericx": "https://x.com/LericxFN",
    "Hyper": "https://x.com/HyperFN_",
    "Julie": "https://x.com/JulieFN_",
    "Alvinlr": "https://x.com/AlvinlrFN",
    "Kenrop": "https://x.com/KenropFN",
    "Maloyache": "https://x.com/MaloyacheFN",
    "Foczka": "https://x.com/FoczkaFN",
    "Szarik": "https://x.com/SzarikFN",
    "Matez": "https://x.com/MatezFN",
    "Kizers": "https://x.com/KizersFN",
    "Ferdy": "https://x.com/FerdyFN",
    "Tarpz": "https://x.com/TarpzFN",
    "Vexi": "https://x.com/VexiFN_",
    "Zarb": "https://x.com/ZarbFN",
    "Fnam": "https://x.com/FnamFN",
    "Kulb": "https://x.com/KulbFN",
    "Artist": "https://x.com/ArtistFN_",
    "Adrx": "https://x.com/AdrxFN",
    "flex": "https://x.com/flexFN_",
    "Damage": "https://x.com/DamageFN_",
    "Nero": "https://x.com/NeroFN_",
    "Huty": "https://x.com/HutyFN",
    "Triix": "https://x.com/TriixFN",
    "Winther": "https://x.com/WintherFN",
    "chrisc": "https://x.com/chriscFN",
    "Klayzz": "https://x.com/KlayzzFN",
    "Squzy": "https://x.com/SquzyFN",
    "SnozQ": "https://x.com/SnozQFN",
    "Shadox": "https://x.com/ShadoxFN",
    "Repairs": "https://x.com/RepairsFN",
    "Heror3h": "https://x.com/Heror3hFN",
    "Mystiqul": "https://x.com/MystiqulFN",
    "Spexx": "https://x.com/SpexxFN",
    "Hedra": "https://x.com/HedraFN",
    "Mirooz": "https://x.com/MiroozFN",
    "nayzix7": "https://x.com/nayzix7",
    "Exqu": "https://x.com/ExquFN",
    "Misha": "https://x.com/MishaFN_",
    "Velryy": "https://x.com/VelryyFN",
    "Kielba": "https://x.com/KielbaFN",
    "Maciak": "https://x.com/MaciakFN",
    "Joshbot": "https://x.com/JoshbotFN",
    "Ary": "https://x.com/AryFN_",
    "2Trash1zr": "https://x.com/2Trash1zr",
    "Efexy": "https://x.com/EfexyFN",
    "SereN": "https://x.com/SereNFN4",
    "Hris": "https://x.com/HrisFN",
    "Okram": "https://x.com/OkramFN",
    "Actfv": "https://x.com/ActfvFN",
    "Joanee": "https://x.com/JoaneeFN",
    "freuzi": "https://x.com/freuziFN",
    "Kaktus": "https://x.com/KaktusFN_",
    "Trulex": "https://x.com/TrulexFN",
    "Robabz": "https://x.com/Robabz_",
    "Kyzen": "https://x.com/KyzenFN",
    "Keolys": "https://x.com/Keolys",
    "Hawkers": "https://x.com/HawkersFN",
    "Oslo": "https://x.com/OsloFN",
    "Chubs": "https://x.com/ChubsFN",
    "Skydeun": "https://x.com/Skydeun",
    "Vatira": "https://x.com/Vatira5"
}

for k, v in historical_players_x.items():
    if k not in player_x_map:
        player_x_map[k] = v

# 3. Load & Fix annual_rankings.json
with open(DATA_DIR / "annual_rankings.json", "r", encoding="utf-8") as f:
    annual = json.load(f)

for yr, ydata in annual.items():
    for c in ydata.get("clubs", []):
        cname = "Reality Zoned" if c["name"] in ["Reality Zone", "Reality Zone (RZ)"] else c["name"]
        c["name"] = cname
        cid = name_to_id.get(cname) or name_to_id.get(c.get("name")) or cname.lower().replace(" ", "-")
        c["id"] = cid
        c["tier"] = club_by_id.get(cid, {}).get("tier", "Tier 2")
        # Ensure both notable and key_achievement exist
        achievement = c.get("notable") or c.get("key_achievement") or "Performances compétitives officielles"
        c["notable"] = achievement
        c["key_achievement"] = achievement
        c["xUrl"] = club_x_map.get(cid, f"https://x.com/{cid}")
        # clean roster
        c["roster"] = [p.split("(")[0].strip() for p in c.get("roster", [])]

with open(DATA_DIR / "annual_rankings.json", "w", encoding="utf-8") as f:
    json.dump(annual, f, indent=2, ensure_ascii=False)

# 4. Build LIVE_DATA with 'details', 'id', 'livePr', 'rank', 'players'
ft_order = [
    ("havok-by-vitality", 1, "+1", "Tier 1", "Rank 1 Fortnite Tracker Europe (741 548 pts, 1 395 160 $)"),
    ("gentle-mates", 2, "-1", "Tier 1", "Rank 2 Fortnite Tracker Europe (503 388 pts, 631 600 $)"),
    ("solary", 3, "=", "Tier 1", "Rank 5 Fortnite Tracker Europe (361 168 pts, 122 890 $)"),
    ("lyost-esport", 4, "+3", "Tier 2", "Rank 7 Fortnite Tracker Europe (351 106 pts, 151 275 $)"),
    ("mga-esport", 5, "+8", "Tier 2", "Rank 13 Fortnite Tracker Europe (230 804 pts, 47 025 $)"),
    ("gameward", 6, "+2", "Tier 1", "Rank 20 Fortnite Tracker Europe (176 065 pts, 11 300 $)"),
    ("k13-esport", 7, "+15", "Tier 2", "Rank 22 Fortnite Tracker Europe (173 080 pts, 36 800 $)"),
    ("team-orchid", 8, "+16", "Tier 2", "Rank 24 Fortnite Tracker Europe (171 417 pts, 97 625 $)"),
    ("1p-esport", 9, "+7", "Tier 2", "Rank 28 Fortnite Tracker Europe (135 029 pts, 21 500 $)"),
    ("r4c-esport", 10, "+29", "Tier 2", "Rank 39 Fortnite Tracker Europe (103 789 pts, 4 560 $)"),
    ("wooka-esport", 11, "+29", "Tier 2", "Rank 40 Fortnite Tracker Europe (100 725 pts, 5 900 $)"),
    ("vulcan-esport", 12, "+29", "Tier 2", "Rank 41 Fortnite Tracker Europe (96 183 pts, 5 200 $)"),
    ("orphee-esport", 13, "+29", "Tier 2", "Rank 42 Fortnite Tracker Europe (95 564 pts, 7 600 $)"),
    ("trkf-esport", 14, "+34", "Tier 2", "Rank 48 Fortnite Tracker Europe (78 684 pts, 7 000 $)"),
    ("pandore-esport", 15, "+34", "Tier 2", "Rank 49 Fortnite Tracker Europe (75 158 pts, 21 670 $)"),
    ("now-esport", 16, "+37", "Tier 2", "Rank 53 Fortnite Tracker Europe (65 772 pts, 1 050 $)"),
    ("poyo-esports", 17, "+38", "Tier 2", "Rank 55 Fortnite Tracker Europe (63 765 pts, 4 100 $)"),
    ("lynox-esport", 18, "+38", "Tier 2", "Rank 56 Fortnite Tracker Europe (63 421 pts, 2 900 $)"),
    ("eoz-esport", 19, "+38", "Tier 2", "Rank 57 Fortnite Tracker Europe (63 050 pts, 2 050 $)"),
    ("ekinox-esports", 20, "+38", "Tier 2", "Rank 58 Fortnite Tracker Europe (62 332 pts, 650 $)"),
    ("wip-esports", 21, "+48", "Tier 2", "Rank 69 Fortnite Tracker Europe (42 782 pts, 1 350 $)"),
    ("haikoo", 22, "+49", "Tier 2", "Rank 71 Fortnite Tracker Europe (37 089 pts, 3 600 $)"),
    ("g3nz-esport", 23, "+53", "Tier 2", "Rank 76 Fortnite Tracker Europe (31 695 pts, 2 700 $)"),
    ("bk-rog", 24, "+66", "Tier 2", "Rank 90 Fortnite Tracker Europe (17 515 pts, 48 900 $)"),
    ("novix-esport", 25, "+69", "Tier 2", "Rank 94 Fortnite Tracker Europe (15 132 pts, 500 $)"),
    ("australe-esport", 26, "+71", "Tier 2", "Rank 97 Fortnite Tracker Europe (13 494 pts, 550 $)"),
    ("valiant", 27, "-17", "Tier 2", "Rank 100 Fortnite Tracker Europe (11 033 pts, 168 295 $)"),
    ("reality-zone", 28, "-20", "Tier 2", "Circuit Tier 2 Régional LFF (9 500 pts)"),
    ("team-fake", 29, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (8 200 pts)"),
    ("team-bsk", 30, "-18", "Tier 2", "Circuit Tier 2 Régional LFF (7 100 pts)"),
    ("aten-esport", 31, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (5 400 pts)"),
    ("jupitar-esport", 32, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (4 800 pts)"),
    ("odious-esport", 33, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (4 200 pts)"),
    ("paps-esport", 34, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (3 900 pts)"),
    ("pandaria-esport", 35, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (3 400 pts)"),
    ("fly-again", 36, "-19", "Tier 2", "Circuit Tier 2 Régional LFF (2 900 pts)"),
    ("zerance", 37, "-32", "Tier 1", "Circuit Majeur / Repositionnement LFF (2 500 pts)")
]

live_clubs_list = []
active_rosters = rosters_data.get("active_rosters", {})

for cid, rank, trend, tier, details in ft_order:
    c = club_by_id.get(cid, {})
    cname = "Reality Zoned" if cid == "reality-zone" else c.get("name", cid)
    pts = c.get("points_lff", 1000)
    x_url = club_x_map.get(cid, f"https://x.com/{cid}")
    x_handle = c.get("x_handle", f"@{cid}")
    
    plist = active_rosters.get(cid, [])
    p_objs = []
    for p in plist:
        p_name = p.get("ign")
        p_pr = p.get("pr", 1000)
        p_c = p.get("country", "🇫🇷")
        p_handle = p.get("x_handle", f"@{p_name}")
        p_u = p.get("x_url", player_x_map.get(p_name, f"https://x.com/{p_name}"))
        p_objs.append({
            "name": p_name,
            "pr": p_pr,
            "country": p_c,
            "xHandle": p_handle,
            "xUrl": p_u
        })
    
    live_clubs_list.append({
        "rank": rank,
        "id": cid,
        "name": cname,
        "tag": c.get("tag", "LFF"),
        "tier": tier,
        "livePr": pts,
        "trend": trend,
        "details": details,
        "xUrl": x_url,
        "xHandle": x_handle,
        "players": p_objs
    })

# 5. Build TRANSFERS formatted for renderTransfers()
clean_transfers = []
for t in rosters_data.get("transfers_log", []):
    pname = t.get("player_ign") or t.get("player_name", "Joueur")
    # clean name
    pname = re.sub(r'\s*\([^)]*\)', '', pname).strip()
    cid = t.get("club_id", "")
    to_club_obj = club_by_id.get(cid, {})
    to_club_name = to_club_obj.get("name", cid.replace("-", " ").title())
    if cid == "reality-zone": to_club_name = "Reality Zoned"
    
    from_club = t.get("previous_club", "Free Agent")
    if from_club in ["reality-zone", "reality-zone (rz)"]: from_club = "Reality Zoned"
    
    clean_transfers.append({
        "date": t.get("date", ""),
        "player": pname,
        "playerXUrl": player_x_map.get(pname, f"https://x.com/search?q={pname}+fortnite"),
        "from": from_club,
        "to": to_club_name,
        "toXUrl": club_x_map.get(cid, f"https://x.com/{cid}"),
        "type": t.get("type", "Transfert"),
        "status": t.get("status", "Confirmé")
    })

# 6. Build allClubs for renderClubs() with 'id' so LOGO_MAP[c.id] works!
all_clubs_cards = []
for c in clubs:
    cid = c["id"]
    cname = "Reality Zoned" if cid == "reality-zone" else c.get("name")
    all_clubs_cards.append({
        "id": cid,
        "name": cname,
        "tag": c.get("tag", "LFF"),
        "tier": c.get("tier", "Tier 2"),
        "desc": c.get("description", ""),
        "xUrl": club_x_map.get(cid, f"https://x.com/{cid}"),
        "xHandle": c.get("x_handle", f"@{cid}"),
        "liquipediaUrl": c.get("liquipedia_url")
    })

# 7. Start from the pristine 12c16e2 index.html to avoid any corruptions
html = subprocess.check_output(
    ['git', 'show', '12c16e2:LFF Dashboard/index.html'],
    text=True,
    encoding='utf-8'
)

# Replace Subtitle
html = html.replace(
    '<div class="mode-subtitle">Course au Titre Annuel (2018 - 2025)</div>',
    '<div class="mode-subtitle">COURSE AU TITRE ANNUEL (2018 - AUJOURD\'HUI)</div>'
)

# Replace year-select options
old_year_options = """            <select class="filter-select" id="year-select" onchange="renderRankingView()">
              <option value="2026" selected>📅 2026 (En cours)</option>
              <option value="2025">📅 2025 (Gentle Mates)</option>
              <option value="2024">📅 2024 (Karmine Corp)</option>
              <option value="2023">📅 2023 (Gentle Mates)</option>
              <option value="2022">📅 2022 (Solary)</option>
              <option value="2021">📅 2021 (TrainHard eSport)</option>
              <option value="2020">📅 2020 (Team MCES)</option>
              <option value="2019">📅 2019 (LeStream Esport)</option>
              <option value="2018">📅 2018 (Solary)</option>
            </select>"""

new_year_options = """            <select class="filter-select" id="year-select" onchange="renderRankingView()">
              <option value="2026" selected>📅 2026</option>
              <option value="2025">📅 2025</option>
              <option value="2024">📅 2024</option>
              <option value="2023">📅 2023</option>
              <option value="2022">📅 2022</option>
              <option value="2021">📅 2021</option>
              <option value="2020">📅 2020</option>
              <option value="2019">📅 2019</option>
              <option value="2018">📅 2018</option>
            </select>"""

if old_year_options in html:
    html = html.replace(old_year_options, new_year_options)

# Robust switchNavTab implementation
robust_switch_nav = """    function switchNavTab(tabId, ev) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));
      const targetTab = document.getElementById(tabId);
      if (targetTab) targetTab.classList.add('active');

      const btn = (ev && ev.currentTarget) ||
                  (typeof window !== 'undefined' && window.event && (window.event.currentTarget || window.event.target)) ||
                  document.querySelector(`button[onclick*="${tabId}"]`);
      if (btn) {
        const navBtn = btn.closest ? btn.closest('.nav-tab-btn') : btn;
        if (navBtn && navBtn.classList) navBtn.classList.add('active');
      }
    }"""

old_switch_nav = """    function switchNavTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      event.target.classList.add('active');
    }"""

if old_switch_nav in html:
    html = html.replace(old_switch_nav, robust_switch_nav)

# Robust renderAnnualTable: handle both c.notable and c.key_achievement
html = html.replace(
    '<td><div class="notable-achievement">${c.notable}</div></td>',
    '<td><div class="notable-achievement">${c.notable || c.key_achievement || ""}</div></td>'
)

# Robust renderLiveTable: handle both c.details and c.trend
html = html.replace(
    '<td><div class="notable-achievement">${c.details}</div></td>',
    '<td><div class="notable-achievement">${c.details || c.trend || ""}</div></td>'
)

# Splice constants safely
# 1. ANNUAL_DATA
idx_annual_start = html.find('const ANNUAL_DATA =')
idx_annual_end = html.find('const CLUB_X_MAP =')
assert idx_annual_start != -1 and idx_annual_end != -1, "ANNUAL_DATA markers not found"
annual_str = json.dumps(annual, indent=2, ensure_ascii=False)
html = html[:idx_annual_start] + f"const ANNUAL_DATA = {annual_str};\n\n    " + html[idx_annual_end:]

# 2. CLUB_X_MAP
idx_cx_start = html.find('const CLUB_X_MAP =')
idx_cx_end = html.find('const PLAYER_X_MAP =')
assert idx_cx_start != -1 and idx_cx_end != -1, "CLUB_X_MAP markers not found"
cx_str = json.dumps(club_x_map, indent=2, ensure_ascii=False)
html = html[:idx_cx_start] + f"const CLUB_X_MAP = {cx_str};\n\n    " + html[idx_cx_end:]

# 3. PLAYER_X_MAP
idx_px_start = html.find('const PLAYER_X_MAP =')
idx_px_end = html.find('const LIVE_DATA =')
assert idx_px_start != -1 and idx_px_end != -1, "PLAYER_X_MAP markers not found"
px_str = json.dumps(player_x_map, indent=2, ensure_ascii=False)
html = html[:idx_px_start] + f"const PLAYER_X_MAP = {px_str};\n\n    " + html[idx_px_end:]

# 4. LIVE_DATA
idx_live_start = html.find('const LIVE_DATA =')
idx_live_end = html.find('const TRANSFERS =')
assert idx_live_start != -1 and idx_live_end != -1, "LIVE_DATA markers not found"
live_str = json.dumps(live_clubs_list, indent=2, ensure_ascii=False)
html = html[:idx_live_start] + f"const LIVE_DATA = {live_str};\n\n    " + html[idx_live_end:]

# 5. TRANSFERS
idx_tr_start = html.find('const TRANSFERS =')
idx_tr_end = html.find('function switchNavTab(')
assert idx_tr_start != -1 and idx_tr_end != -1, "TRANSFERS markers not found"
tr_str = json.dumps(clean_transfers, indent=2, ensure_ascii=False)
html = html[:idx_tr_start] + f"const TRANSFERS = {tr_str};\n\n    " + html[idx_tr_end:]

# 6. allClubs in renderClubs()
idx_ac_start = html.find('const allClubs = [')
idx_ac_end = html.find('allClubs.forEach(c => {')
assert idx_ac_start != -1 and idx_ac_end != -1, "allClubs markers not found"
all_clubs_str = json.dumps(all_clubs_cards, indent=8, ensure_ascii=False)
html = html[:idx_ac_start] + f"const allClubs = {all_clubs_str};\n\n      " + html[idx_ac_end:]

# Remove any em dashes
html = html.replace('\u2014', '-')

# Write updated index.html
with open(DASH_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html fully updated and repaired!")
