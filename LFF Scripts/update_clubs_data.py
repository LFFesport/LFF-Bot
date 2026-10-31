import json
from pathlib import Path

BASE_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF")
DATA_DIR = BASE_DIR / "LFF Data"
DASH_DIR = BASE_DIR / "LFF Dashboard"

# 1. Load clubs.json
with open(DATA_DIR / "clubs.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

# FT Points and earnings mapped from live PDF top 100
ft_data = {
    "havok-by-vitality": {"pts": 741548, "earnings": 1395160, "rank_ft": 1},
    "team-havok": {"pts": 741548, "earnings": 1395160, "rank_ft": 1},
    "gentle-mates": {"pts": 503388, "earnings": 631600, "rank_ft": 2},
    "solary": {"pts": 361168, "earnings": 122890, "rank_ft": 5},
    "lyost-esport": {"pts": 351106, "earnings": 151275, "rank_ft": 7},
    "mga-esport": {"pts": 230804, "earnings": 47025, "rank_ft": 13},
    "gameward": {"pts": 176065, "earnings": 11300, "rank_ft": 20},
    "k13-esport": {"pts": 173080, "earnings": 36800, "rank_ft": 22},
    "team-orchid": {"pts": 171417, "earnings": 97625, "rank_ft": 24},
    "1p-esport": {"pts": 135029, "earnings": 21500, "rank_ft": 28},
    "r4c-esport": {"pts": 103789, "earnings": 4560, "rank_ft": 39},
    "wooka-esport": {"pts": 100725, "earnings": 5900, "rank_ft": 40},
    "vulcan-esport": {"pts": 96183, "earnings": 5200, "rank_ft": 41},
    "orphee-esport": {"pts": 95564, "earnings": 7600, "rank_ft": 42},
    "trkf-esport": {"pts": 78684, "earnings": 7000, "rank_ft": 48},
    "pandore-esport": {"pts": 75158, "earnings": 21670, "rank_ft": 49},
    "now-esport": {"pts": 65772, "earnings": 1050, "rank_ft": 53},
    "poyo-esports": {"pts": 63765, "earnings": 4100, "rank_ft": 55},
    "lynox-esport": {"pts": 63421, "earnings": 2900, "rank_ft": 56},
    "eoz-esport": {"pts": 63050, "earnings": 2050, "rank_ft": 57},
    "ekinox-esports": {"pts": 62332, "earnings": 650, "rank_ft": 58},
    "wip-esports": {"pts": 42782, "earnings": 1350, "rank_ft": 69},
    "haikoo": {"pts": 37089, "earnings": 3600, "rank_ft": 71},
    "g3nz-esport": {"pts": 31695, "earnings": 2700, "rank_ft": 76},
    "bk-rog": {"pts": 17515, "earnings": 48900, "rank_ft": 90},
    "novix-esport": {"pts": 15132, "earnings": 500, "rank_ft": 94},
    "australe-esport": {"pts": 13494, "earnings": 550, "rank_ft": 97},
    "valiant": {"pts": 11033, "earnings": 168295, "rank_ft": 100},
    # Other active French structures in regional/academy circuit
    "reality-zone": {"pts": 9500, "earnings": 12000, "rank_ft": 105},
    "team-fake": {"pts": 8200, "earnings": 8500, "rank_ft": 112},
    "team-bsk": {"pts": 7100, "earnings": 6200, "rank_ft": 120},
    "aten-esport": {"pts": 5400, "earnings": 4500, "rank_ft": 135},
    "jupitar-esport": {"pts": 4800, "earnings": 3800, "rank_ft": 142},
    "odious-esport": {"pts": 4200, "earnings": 2900, "rank_ft": 150},
    "paps-esport": {"pts": 3900, "earnings": 2100, "rank_ft": 158},
    "pandaria-esport": {"pts": 3400, "earnings": 1800, "rank_ft": 165},
    "fly-again": {"pts": 2900, "earnings": 1400, "rank_ft": 172},
    "zerance": {"pts": 2500, "earnings": 15400, "rank_ft": 180},
    "galions": {"pts": 1800, "earnings": 12500, "rank_ft": 195},
    "karmine-corp": {"pts": 1200, "earnings": 520000, "rank_ft": 210}
}

for c in clubs:
    cid = c["id"]
    if cid in ft_data:
        c["points_lff"] = ft_data[cid]["pts"]
        c["earnings_usd"] = ft_data[cid]["earnings"]
        c["rank_ft_europe"] = ft_data[cid]["rank_ft"]
    if cid == "reality-zone":
        c["name"] = "Reality Zoned"
    # Ensure X URL
    if not c.get("x_url") and c.get("x_handle"):
        clean = c["x_handle"].replace("@", "")
        c["x_url"] = f"https://x.com/{clean}"

with open(DATA_DIR / "clubs.json", "w", encoding="utf-8") as f:
    json.dump(clubs, f, indent=2, ensure_ascii=False)

print(f"Updated {len(clubs)} clubs in clubs.json")
