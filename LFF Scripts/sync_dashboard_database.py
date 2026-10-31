import json
import re
from pathlib import Path

BASE_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF")
DATA_DIR = BASE_DIR / "LFF Data"
DASH_DIR = BASE_DIR / "LFF Dashboard"

# Load files
with open(DATA_DIR / "clubs.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

with open(DATA_DIR / "rosters.json", "r", encoding="utf-8") as f:
    rosters_data = json.load(f)

with open(DATA_DIR / "annual_rankings.json", "r", encoding="utf-8") as f:
    annual = json.load(f)

with open(DASH_DIR / "index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Subtitle
html = html.replace(
    '<div class="mode-subtitle">Course au Titre Annuel (2018 - 2025)</div>',
    '<div class="mode-subtitle">COURSE AU TITRE ANNUEL (2018 - AUJOURD\'HUI)</div>'
)

# 2. Clean year-select: remove champions/sacre from options
old_select = """            <select class="filter-select" id="year-select" onchange="renderRankingView()">
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

new_select = """            <select class="filter-select" id="year-select" onchange="renderRankingView()">
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

if old_select in html:
    html = html.replace(old_select, new_select)
else:
    # Regex replace option tags inside year-select
    html = re.sub(
        r'<option value="(\d{4})"[^>]*>📅 \d{4}[^<]*</option>',
        r'<option value="\1">📅 \1</option>',
        html
    )
    # Ensure 2026 is selected
    html = html.replace('<option value="2026">📅 2026</option>', '<option value="2026" selected>📅 2026</option>')

# 3. Build CLUB_X_MAP
club_x_map = {}
for c in clubs:
    cid = c["id"]
    if c.get("x_url"):
        club_x_map[cid] = c["x_url"]
    elif c.get("x_handle"):
        clean = c["x_handle"].replace("@", "")
        club_x_map[cid] = f"https://x.com/{clean}"

# 4. Build PLAYER_X_MAP
player_x_map = {}
# From active_rosters
for cid, plist in rosters_data.get("active_rosters", {}).items():
    for p in plist:
        ign = p["ign"]
        if p.get("x_url"):
            player_x_map[ign] = p["x_url"]
        elif p.get("x_handle"):
            clean = p["x_handle"].replace("@", "")
            player_x_map[ign] = f"https://x.com/{clean}"

# Known historical players X handles
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

# 5. Build LIVE_DATA
club_by_id = {c["id"]: c for c in clubs}
active_rosters = rosters_data.get("active_rosters", {})

live_clubs_list = []
# Clubs in order of FT rank
ft_order = [
    ("havok-by-vitality", 1, "+1", "Tier 1"),
    ("gentle-mates", 2, "-1", "Tier 1"),
    ("solary", 3, "=", "Tier 1"),
    ("lyost-esport", 4, "+3", "Tier 2"),
    ("mga-esport", 5, "+8", "Tier 2"),
    ("gameward", 6, "+2", "Tier 1"),
    ("k13-esport", 7, "+15", "Tier 2"),
    ("team-orchid", 8, "+16", "Tier 2"),
    ("1p-esport", 9, "+7", "Tier 2"),
    ("r4c-esport", 10, "+29", "Tier 2"),
    ("wooka-esport", 11, "+29", "Tier 2"),
    ("vulcan-esport", 12, "+29", "Tier 2"),
    ("orphee-esport", 13, "+29", "Tier 2"),
    ("trkf-esport", 14, "+34", "Tier 2"),
    ("pandore-esport", 15, "+34", "Tier 2"),
    ("now-esport", 16, "+37", "Tier 2"),
    ("poyo-esports", 17, "+38", "Tier 2"),
    ("lynox-esport", 18, "+38", "Tier 2"),
    ("eoz-esport", 19, "+38", "Tier 2"),
    ("ekinox-esports", 20, "+38", "Tier 2"),
    ("wip-esports", 21, "+48", "Tier 2"),
    ("haikoo", 22, "+49", "Tier 2"),
    ("g3nz-esport", 23, "+53", "Tier 2"),
    ("bk-rog", 24, "+66", "Tier 2"),
    ("novix-esport", 25, "+69", "Tier 2"),
    ("australe-esport", 26, "+71", "Tier 2"),
    ("valiant", 27, "-17", "Tier 2"),
    ("reality-zone", 28, "-20", "Tier 2"),
    ("team-fake", 29, "-19", "Tier 2"),
    ("team-bsk", 30, "-18", "Tier 2"),
    ("aten-esport", 31, "-19", "Tier 2"),
    ("jupitar-esport", 32, "-19", "Tier 2"),
    ("odious-esport", 33, "-19", "Tier 2"),
    ("paps-esport", 34, "-19", "Tier 2"),
    ("pandaria-esport", 35, "-19", "Tier 2"),
    ("fly-again", 36, "-19", "Tier 2"),
    ("zerance", 37, "-32", "Tier 1")
]

for cid, rank, trend, tier in ft_order:
    c = club_by_id.get(cid, {})
    cname = "Reality Zoned" if cid == "reality-zone" else c.get("name", cid)
    pts = c.get("points_lff", 1000)
    x_url = c.get("x_url", f"https://x.com/{cid}")
    x_handle = c.get("x_handle", f"@{cid}")
    
    # build player objects
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
        "xUrl": x_url,
        "xHandle": x_handle,
        "players": p_objs
    })

# 6. Replace constants in index.html
# Replace ANNUAL_DATA
idx_annual_start = html.find('const ANNUAL_DATA =')
if idx_annual_start != -1:
    idx_annual_end = html.find('const CLUB_X_MAP =')
    if idx_annual_end != -1:
        annual_json_str = json.dumps(annual, indent=2, ensure_ascii=False)
        html = html[:idx_annual_start] + f"const ANNUAL_DATA = {annual_json_str};\n\n    " + html[idx_annual_end:]

# Replace CLUB_X_MAP
idx_cx_start = html.find('const CLUB_X_MAP =')
if idx_cx_start != -1:
    idx_cx_end = html.find('const PLAYER_X_MAP =')
    if idx_cx_end != -1:
        cx_json_str = json.dumps(club_x_map, indent=2, ensure_ascii=False)
        html = html[:idx_cx_start] + f"const CLUB_X_MAP = {cx_json_str};\n\n    " + html[idx_cx_end:]

# Replace PLAYER_X_MAP
idx_px_start = html.find('const PLAYER_X_MAP =')
if idx_px_start != -1:
    idx_px_end = html.find('const LIVE_DATA =')
    if idx_px_end != -1:
        px_json_str = json.dumps(player_x_map, indent=2, ensure_ascii=False)
        html = html[:idx_px_start] + f"const PLAYER_X_MAP = {px_json_str};\n\n    " + html[idx_px_end:]

# Replace LIVE_DATA
idx_live_start = html.find('const LIVE_DATA =')
if idx_live_start != -1:
    idx_live_end = html.find('const TRANSFERS =')
    if idx_live_end != -1:
        live_json_str = json.dumps(live_clubs_list, indent=2, ensure_ascii=False)
        html = html[:idx_live_start] + f"const LIVE_DATA = {live_json_str};\n\n    " + html[idx_live_end:]

# Replace TRANSFERS
idx_tr_start = html.find('const TRANSFERS =')
if idx_tr_start != -1:
    idx_tr_end = html.find('let currentMode =')
    if idx_tr_end != -1:
        tr_json_str = json.dumps(rosters_data.get("transfers_log", []), indent=2, ensure_ascii=False)
        html = html[:idx_tr_start] + f"const TRANSFERS = {tr_json_str};\n\n    " + html[idx_tr_end:]

# Replace allClubs in renderClubs()
all_clubs_cards = []
for c in clubs:
    cid = c["id"]
    cname = "Reality Zoned" if cid == "reality-zone" else c.get("name")
    all_clubs_cards.append({
        "name": cname,
        "tag": c.get("tag", "LFF"),
        "tier": c.get("tier", "Tier 2"),
        "desc": c.get("description", ""),
        "xUrl": c.get("x_url", f"https://x.com/{cid}"),
        "xHandle": c.get("x_handle", f"@{cid}"),
        "liquipediaUrl": c.get("liquipedia_url")
    })

all_clubs_json_str = json.dumps(all_clubs_cards, indent=8, ensure_ascii=False)
idx_ac_start = html.find('const allClubs = [')
if idx_ac_start != -1:
    idx_ac_end = html.find('allClubs.forEach(c => {')
    if idx_ac_end != -1:
        html = html[:idx_ac_start] + f"const allClubs = {all_clubs_json_str};\n\n      " + html[idx_ac_end:]

# Eradicate any em dashes
html = html.replace("\u2014", "-")

with open(DASH_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Synchronized all database constants, live data, annual data, X maps, and subtitle into index.html!")
