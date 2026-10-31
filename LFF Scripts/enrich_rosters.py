import json
from pathlib import Path

BASE_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF")
DATA_DIR = BASE_DIR / "LFF Data"

# Load existing rosters.json
with open(DATA_DIR / "rosters.json", "r", encoding="utf-8") as f:
    rosters_data = json.load(f)

# Build comprehensive active_rosters with PR, X handles, and career histories
# Mapping verified from PDF snapshot, Liquipedia, Fandom, and official announcements
active_rosters = {
    "havok-by-vitality": [
        {
            "ign": "SwizzY",
            "name": "Egor Luciko",
            "country": "🌍",
            "pr": 245000,
            "x_handle": "@SwizzY281",
            "x_url": "https://x.com/SwizzY281",
            "joined": "2025-05-02",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Karmine Corp", "joined": "2024-05-01", "left": "2025-04-30", "role": "Joueur"},
                {"club": "Team HavoK / HavoK by Vitality", "joined": "2025-05-02", "left": "Présent", "role": "Star Joueur"}
            ]
        },
        {
            "ign": "PabloWingu",
            "name": "PabloWingu",
            "country": "🇩🇰",
            "pr": 185000,
            "x_handle": "@PabloWingu",
            "x_url": "https://x.com/PabloWingu",
            "joined": "2025-02-15",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Free Agent", "joined": "2023-01-01", "left": "2025-02-14", "role": "Joueur"},
                {"club": "Team HavoK / HavoK by Vitality", "joined": "2025-02-15", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "Tjino",
            "name": "Tjino",
            "country": "🇩🇰",
            "pr": 165000,
            "x_handle": "@tjino9",
            "x_url": "https://x.com/tjino9",
            "joined": "2025-03-01",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Team HavoK / HavoK by Vitality", "joined": "2025-03-01", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "Pixie",
            "name": "Pixie",
            "country": "🇸🇪",
            "pr": 146548,
            "x_handle": "@pixiefnbr",
            "x_url": "https://x.com/pixiefnbr",
            "joined": "2024-11-10",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Team HavoK / HavoK by Vitality", "joined": "2024-11-10", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "Wox",
            "name": "Wox",
            "country": "🇸🇪",
            "pr": 48000,
            "x_handle": "@WoxSHTER",
            "x_url": "https://x.com/WoxSHTER",
            "joined": "2024-08-28",
            "status": "Remplaçant / Roster élargi",
            "career_history": [
                {"club": "Team HavoK", "joined": "2024-08-28", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "Seekk",
            "name": "Seekk",
            "country": "🇫🇷",
            "pr": 14500,
            "x_handle": "@Seekkfn",
            "x_url": "https://x.com/Seekkfn",
            "joined": "2026-10-15",
            "status": "Roster Espoir",
            "career_history": [
                {"club": "Team HavoK / HavoK by Vitality", "joined": "2026-10-15", "left": "Présent", "role": "Espoir"}
            ]
        }
    ],
    "team-havok": [
        {
            "ign": "SwizzY",
            "name": "Egor Luciko",
            "country": "🌍",
            "pr": 245000,
            "x_handle": "@SwizzY281",
            "x_url": "https://x.com/SwizzY281",
            "joined": "2025-05-02",
            "status": "Contrat Actif"
        },
        {
            "ign": "PabloWingu",
            "name": "PabloWingu",
            "country": "🇩🇰",
            "pr": 185000,
            "x_handle": "@PabloWingu",
            "x_url": "https://x.com/PabloWingu",
            "joined": "2025-02-15",
            "status": "Contrat Actif"
        },
        {
            "ign": "Tjino",
            "name": "Tjino",
            "country": "🇩🇰",
            "pr": 165000,
            "x_handle": "@tjino9",
            "x_url": "https://x.com/tjino9",
            "joined": "2025-03-01",
            "status": "Contrat Actif"
        },
        {
            "ign": "Pixie",
            "name": "Pixie",
            "country": "🇸🇪",
            "pr": 146548,
            "x_handle": "@pixiefnbr",
            "x_url": "https://x.com/pixiefnbr",
            "joined": "2024-11-10",
            "status": "Contrat Actif"
        }
    ],
    "gentle-mates": [
        {
            "ign": "Vanyak3kk",
            "name": "Ivan",
            "country": "🌍",
            "pr": 198000,
            "x_handle": "@Vanyak3kk",
            "x_url": "https://x.com/Vanyak3kk",
            "joined": "2024-06-15",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Free Agent", "joined": "2022-01-01", "left": "2024-06-14", "role": "Joueur"},
                {"club": "Gentle Mates", "joined": "2024-06-15", "left": "Présent", "role": "Star Joueur"}
            ]
        },
        {
            "ign": "Akiira",
            "name": "Akiira",
            "country": "🇫🇷",
            "pr": 145000,
            "x_handle": "@Akiirafn",
            "x_url": "https://x.com/Akiirafn",
            "joined": "2025-01-10",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Gentle Mates", "joined": "2025-01-10", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "MariusCOW",
            "name": "MariusCOW",
            "country": "🇩🇰",
            "pr": 95000,
            "x_handle": "@MariusCOW",
            "x_url": "https://x.com/MariusCOW",
            "joined": "2025-09-01",
            "status": "Partenaire / Prêt",
            "career_history": [
                {"club": "Gentle Mates", "joined": "2025-09-01", "left": "Présent", "role": "Partenaire FNCS"}
            ]
        },
        {
            "ign": "Kurama",
            "name": "Stéphane Poret",
            "country": "🇫🇷",
            "pr": 65388,
            "x_handle": "@Kurama_FN",
            "x_url": "https://x.com/Kurama_FN",
            "joined": "2026-03-30",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Free Agent", "joined": "2023-01-01", "left": "2026-03-29", "role": "Joueur"},
                {"club": "Gentle Mates", "joined": "2026-03-30", "left": "Présent", "role": "Joueur"}
            ]
        }
    ],
    "solary": [
        {
            "ign": "Ghonzo",
            "name": "Ghonzo",
            "country": "🇫🇷",
            "pr": 125000,
            "x_handle": "@GhonzoFN",
            "x_url": "https://x.com/GhonzoFN",
            "joined": "2025-01-15",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Solary", "joined": "2025-01-15", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "Minori",
            "name": "Minori",
            "country": "🇫🇷",
            "pr": 98000,
            "x_handle": "@Minorifn",
            "x_url": "https://x.com/Minorifn",
            "joined": "2026-04-25",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Solary", "joined": "2026-04-25", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "SkyJump",
            "name": "SkyJump",
            "country": "🇫🇷",
            "pr": 78168,
            "x_handle": "@SkyJumpFN",
            "x_url": "https://x.com/SkyJumpFN",
            "joined": "2026-02-01",
            "status": "Partenaire FNCS",
            "career_history": [
                {"club": "Solary", "joined": "2026-02-01", "left": "Présent", "role": "Partenaire"}
            ]
        },
        {
            "ign": "Darkos",
            "name": "Darkos",
            "country": "🇫🇷",
            "pr": 60000,
            "x_handle": "@Darkos_ftn",
            "x_url": "https://x.com/Darkos_ftn",
            "joined": "2026-04-25",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Solary", "joined": "2026-04-25", "left": "Présent", "role": "Joueur"}
            ]
        },
        {
            "ign": "XZEEVIT",
            "name": "XZEEVIT",
            "country": "🇫🇷",
            "pr": 35000,
            "x_handle": "@xzeevit",
            "x_url": "https://x.com/xzeevit",
            "joined": "2026-10-03",
            "status": "Contrat Actif",
            "career_history": [
                {"club": "Lynox Esport", "joined": "2024-01-01", "left": "2026-10-02", "role": "Joueur"},
                {"club": "Solary", "joined": "2026-10-03", "left": "Présent", "role": "Joueur"}
            ]
        }
    ],
    "lyost-esport": [
        {"ign": "Momsy", "name": "Momsy", "country": "🇫🇷", "pr": 112000, "x_handle": "@MomsyFN", "x_url": "https://x.com/MomsyFN", "joined": "2024-05-10", "status": "Contrat Actif"},
        {"ign": "Werex", "name": "Werex", "country": "🇫🇷", "pr": 95000, "x_handle": "@WerexFN", "x_url": "https://x.com/WerexFN", "joined": "2024-06-01", "status": "Contrat Actif"},
        {"ign": "Twek", "name": "Twek", "country": "🇫🇷", "pr": 78000, "x_handle": "@TwekFN", "x_url": "https://x.com/TwekFN", "joined": "2025-01-15", "status": "Contrat Actif"},
        {"ign": "Borsuk", "name": "Borsuk", "country": "🇵🇱", "pr": 66106, "x_handle": "@BorsukFN", "x_url": "https://x.com/BorsukFN", "joined": "2025-03-20", "status": "Contrat Actif"}
    ],
    "mga-esport": [
        {"ign": "Syaaz", "name": "Syaaz", "country": "🇫🇷", "pr": 85000, "x_handle": "@SyaazFN", "x_url": "https://x.com/SyaazFN", "joined": "2024-04-12", "status": "Contrat Actif"},
        {"ign": "Trusio", "name": "Trusio", "country": "🇫🇷", "pr": 70000, "x_handle": "@TrusioFN", "x_url": "https://x.com/TrusioFN", "joined": "2024-08-01", "status": "Contrat Actif"},
        {"ign": "FiTo", "name": "FiTo", "country": "🇪🇸", "pr": 45000, "x_handle": "@FiTo_fn", "x_url": "https://x.com/FiTo_fn", "joined": "2025-02-10", "status": "Partenaire"},
        {"ign": "iFrOzi", "name": "iFrOzi", "country": "🇫🇷", "pr": 30804, "x_handle": "@iFr0zi", "x_url": "https://x.com/iFr0zi", "joined": "2025-04-01", "status": "Partenaire"}
    ],
    "gameward": [
        {"ign": "Kombek", "name": "Kombek", "country": "🇵🇱", "pr": 62000, "x_handle": "@KombekFN", "x_url": "https://x.com/KombekFN", "joined": "2024-09-01", "status": "Contrat Actif"},
        {"ign": "Tylio", "name": "Tylio", "country": "🇫🇷", "pr": 48000, "x_handle": "@TylioFN", "x_url": "https://x.com/TylioFN", "joined": "2024-10-15", "status": "Contrat Actif"},
        {"ign": "Nociff", "name": "Nociff", "country": "🇫🇷", "pr": 38000, "x_handle": "@NociffFN", "x_url": "https://x.com/NociffFN", "joined": "2025-01-05", "status": "Prêt / Partenaire"},
        {"ign": "S1neD", "name": "S1neD", "country": "🇫🇷", "pr": 28065, "x_handle": "@S1neDFN", "x_url": "https://x.com/S1neDFN", "joined": "2025-01-10", "status": "Contrat Actif"}
    ],
    "k13-esport": [
        {"ign": "Firen", "name": "Firen", "country": "🇫🇷", "pr": 61000, "x_handle": "@FirenFN", "x_url": "https://x.com/FirenFN", "joined": "2024-03-01", "status": "Contrat Actif"},
        {"ign": "Asa", "name": "Asa", "country": "🇫🇷", "pr": 46000, "x_handle": "@AsaFN_", "x_url": "https://x.com/AsaFN_", "joined": "2024-07-15", "status": "Partenaire"},
        {"ign": "Seyyto", "name": "Seyyto", "country": "🇫🇷", "pr": 38000, "x_handle": "@SeyytoFN", "x_url": "https://x.com/SeyytoFN", "joined": "2025-02-01", "status": "Partenaire"},
        {"ign": "Roz", "name": "Roz", "country": "🇫🇷", "pr": 28080, "x_handle": "@RozFN_", "x_url": "https://x.com/RozFN_", "joined": "2025-03-10", "status": "Partenaire"}
    ],
    "team-orchid": [
        {"ign": "Izzi", "name": "Izzi", "country": "🇫🇷", "pr": 68000, "x_handle": "@IzziFN_", "x_url": "https://x.com/IzziFN_", "joined": "2024-04-01", "status": "Contrat Actif"},
        {"ign": "Nociff", "name": "Nociff", "country": "🇫🇷", "pr": 55000, "x_handle": "@NociffFN", "x_url": "https://x.com/NociffFN", "joined": "2024-05-15", "status": "Contrat Actif"},
        {"ign": "Seyyto", "name": "Seyyto", "country": "🇫🇷", "pr": 48417, "x_handle": "@SeyytoFN", "x_url": "https://x.com/SeyytoFN", "joined": "2024-06-01", "status": "Contrat Actif"}
    ],
    "1p-esport": [
        {"ign": "Lericx", "name": "Lericx", "country": "🇫🇷", "pr": 52000, "x_handle": "@LericxFN", "x_url": "https://x.com/LericxFN", "joined": "2024-01-10", "status": "Contrat Actif"},
        {"ign": "Hyper", "name": "Hyper", "country": "🇫🇷", "pr": 36000, "x_handle": "@HyperFN_", "x_url": "https://x.com/HyperFN_", "joined": "2024-05-01", "status": "Partenaire"},
        {"ign": "Julie", "name": "Julie", "country": "🇫🇷", "pr": 28000, "x_handle": "@JulieFN_", "x_url": "https://x.com/JulieFN_", "joined": "2024-09-01", "status": "Contrat Actif"},
        {"ign": "Alvinlr", "name": "Alvinlr", "country": "🇫🇷", "pr": 19029, "x_handle": "@AlvinlrFN", "x_url": "https://x.com/AlvinlrFN", "joined": "2025-01-20", "status": "Partenaire"}
    ],
    "r4c-esport": [
        {"ign": "Kenrop", "name": "Kenrop", "country": "🇫🇷", "pr": 45000, "x_handle": "@KenropFN", "x_url": "https://x.com/KenropFN", "joined": "2024-06-01", "status": "Contrat Actif"},
        {"ign": "Maloyache", "name": "Maloyache", "country": "🇷🇺", "pr": 35000, "x_handle": "@MaloyacheFN", "x_url": "https://x.com/MaloyacheFN", "joined": "2024-10-01", "status": "Partenaire"},
        {"ign": "Foczka", "name": "Foczka", "country": "🇵🇱", "pr": 23789, "x_handle": "@FoczkaFN", "x_url": "https://x.com/FoczkaFN", "joined": "2025-02-15", "status": "Contrat Actif"}
    ],
    "wooka-esport": [
        {"ign": "Szarik", "name": "Szarik", "country": "🇵🇱", "pr": 38000, "x_handle": "@SzarikFN", "x_url": "https://x.com/SzarikFN", "joined": "2023-11-01", "status": "Contrat Actif"},
        {"ign": "Matez", "name": "Matez", "country": "🇵🇱", "pr": 28000, "x_handle": "@MatezFN", "x_url": "https://x.com/MatezFN", "joined": "2024-04-10", "status": "Partenaire"},
        {"ign": "Kizers", "name": "Kizers", "country": "🇵🇱", "pr": 20000, "x_handle": "@KizersFN", "x_url": "https://x.com/KizersFN", "joined": "2024-08-01", "status": "Partenaire"},
        {"ign": "Ferdy", "name": "Ferdy", "country": "🇫🇷", "pr": 14725, "x_handle": "@FerdyFN", "x_url": "https://x.com/FerdyFN", "joined": "2025-01-10", "status": "Contrat Actif"}
    ],
    "vulcan-esport": [
        {"ign": "Izzi", "name": "Izzi", "country": "🇫🇷", "pr": 34000, "x_handle": "@IzziFN_", "x_url": "https://x.com/IzziFN_", "joined": "2024-06-01", "status": "Partenaire"},
        {"ign": "Tarpz", "name": "Tarpz", "country": "🇫🇷", "pr": 28000, "x_handle": "@TarpzFN", "x_url": "https://x.com/TarpzFN", "joined": "2024-07-01", "status": "Contrat Actif"},
        {"ign": "Vexi", "name": "Vexi", "country": "🇫🇷", "pr": 20000, "x_handle": "@VexiFN_", "x_url": "https://x.com/VexiFN_", "joined": "2024-09-15", "status": "Partenaire"},
        {"ign": "Zarb", "name": "Zarb", "country": "🇫🇷", "pr": 14183, "x_handle": "@ZarbFN", "x_url": "https://x.com/ZarbFN", "joined": "2025-01-10", "status": "Partenaire"}
    ],
    "orphee-esport": [
        {"ign": "Fnam", "name": "Fnam", "country": "🇫🇷", "pr": 33000, "x_handle": "@FnamFN", "x_url": "https://x.com/FnamFN", "joined": "2024-05-01", "status": "Contrat Actif"},
        {"ign": "Kulb", "name": "Kulb", "country": "🇫🇷", "pr": 28000, "x_handle": "@KulbFN", "x_url": "https://x.com/KulbFN", "joined": "2024-08-10", "status": "Partenaire"},
        {"ign": "Artist", "name": "Artist", "country": "🇫🇷", "pr": 20000, "x_handle": "@ArtistFN_", "x_url": "https://x.com/ArtistFN_", "joined": "2024-11-01", "status": "Contrat Actif"},
        {"ign": "Adrx", "name": "Adrx", "country": "🇫🇷", "pr": 14564, "x_handle": "@AdrxFN", "x_url": "https://x.com/AdrxFN", "joined": "2025-02-01", "status": "Partenaire"}
    ],
    "trkf-esport": [
        {"ign": "flex", "name": "flex", "country": "🇫🇷", "pr": 32000, "x_handle": "@flexFN_", "x_url": "https://x.com/flexFN_", "joined": "2024-03-15", "status": "Partenaire"},
        {"ign": "Damage", "name": "Damage", "country": "🇫🇷", "pr": 26000, "x_handle": "@DamageFN_", "x_url": "https://x.com/DamageFN_", "joined": "2024-06-01", "status": "Partenaire"},
        {"ign": "Nero", "name": "Nero", "country": "🇫🇷", "pr": 20684, "x_handle": "@NeroFN_", "x_url": "https://x.com/NeroFN_", "joined": "2024-09-01", "status": "Partenaire"}
    ],
    "pandore-esport": [
        {"ign": "Huty", "name": "Huty", "country": "🇫🇷", "pr": 32000, "x_handle": "@HutyFN", "x_url": "https://x.com/HutyFN", "joined": "2023-09-01", "status": "Contrat Actif"},
        {"ign": "Triix", "name": "Triix", "country": "🇫🇷", "pr": 25000, "x_handle": "@TriixFN", "x_url": "https://x.com/TriixFN", "joined": "2023-10-15", "status": "Contrat Actif"},
        {"ign": "Winther", "name": "Winther", "country": "🇩🇰", "pr": 18158, "x_handle": "@WintherFN", "x_url": "https://x.com/WintherFN", "joined": "2024-02-01", "status": "Contrat Actif"}
    ],
    "now-esport": [
        {"ign": "chrisc", "name": "chrisc", "country": "🇫🇷", "pr": 24000, "x_handle": "@chriscFN", "x_url": "https://x.com/chriscFN", "joined": "2024-02-10", "status": "Partenaire"},
        {"ign": "Klayzz", "name": "Klayzz", "country": "🇫🇷", "pr": 18000, "x_handle": "@KlayzzFN", "x_url": "https://x.com/KlayzzFN", "joined": "2024-05-15", "status": "Contrat Actif"},
        {"ign": "Squzy", "name": "Squzy", "country": "🇫🇷", "pr": 14000, "x_handle": "@SquzyFN", "x_url": "https://x.com/SquzyFN", "joined": "2024-08-01", "status": "Partenaire"},
        {"ign": "Maloyache", "name": "Maloyache", "country": "🇷🇺", "pr": 9772, "x_handle": "@MaloyacheFN", "x_url": "https://x.com/MaloyacheFN", "joined": "2024-11-01", "status": "Partenaire"}
    ],
    "poyo-esports": [
        {"ign": "SnozQ", "name": "SnozQ", "country": "🇫🇷", "pr": 24000, "x_handle": "@SnozQFN", "x_url": "https://x.com/SnozQFN", "joined": "2024-04-01", "status": "Partenaire"},
        {"ign": "iFrOzi", "name": "iFrOzi", "country": "🇫🇷", "pr": 18000, "x_handle": "@iFr0zi", "x_url": "https://x.com/iFr0zi", "joined": "2024-06-15", "status": "Contrat Actif"},
        {"ign": "Shadox", "name": "Shadox", "country": "🇫🇷", "pr": 12000, "x_handle": "@ShadoxFN", "x_url": "https://x.com/ShadoxFN", "joined": "2024-09-01", "status": "Contrat Actif"},
        {"ign": "Repairs", "name": "Repairs", "country": "🇫🇷", "pr": 9765, "x_handle": "@RepairsFN", "x_url": "https://x.com/RepairsFN", "joined": "2025-01-10", "status": "Partenaire"}
    ],
    "lynox-esport": [
        {"ign": "Heror3h", "name": "Heror3h", "country": "🌍", "pr": 38000, "x_handle": "@Heror3hFN", "x_url": "https://x.com/Heror3hFN", "joined": "2024-05-01", "status": "Partenaire"},
        {"ign": "xzeevit4k", "name": "xzeevit4k", "country": "🇫🇷", "pr": 25421, "x_handle": "@xzeevit", "x_url": "https://x.com/xzeevit", "joined": "2024-01-15", "status": "Contrat Actif"}
    ],
    "eoz-esport": [
        {"ign": "Mystiqul", "name": "Mystiqul", "country": "🇫🇷", "pr": 22000, "x_handle": "@MystiqulFN", "x_url": "https://x.com/MystiqulFN", "joined": "2024-02-15", "status": "Partenaire"},
        {"ign": "Spexx", "name": "Spexx", "country": "🇫🇷", "pr": 18000, "x_handle": "@SpexxFN", "x_url": "https://x.com/SpexxFN", "joined": "2024-06-01", "status": "Partenaire"},
        {"ign": "S1neD", "name": "S1neD", "country": "🇫🇷", "pr": 14000, "x_handle": "@S1neDFN", "x_url": "https://x.com/S1neDFN", "joined": "2024-08-15", "status": "Partenaire"},
        {"ign": "Hedra", "name": "Hedra", "country": "🇫🇷", "pr": 9050, "x_handle": "@HedraFN", "x_url": "https://x.com/HedraFN", "joined": "2025-01-20", "status": "Partenaire"}
    ],
    "ekinox-esports": [
        {"ign": "Mirooz", "name": "Mirooz", "country": "🇫🇷", "pr": 24000, "x_handle": "@MiroozFN", "x_url": "https://x.com/MiroozFN", "joined": "2024-03-01", "status": "Contrat Actif"},
        {"ign": "nayzix7", "name": "nayzix7", "country": "🇫🇷", "pr": 18000, "x_handle": "@nayzix7", "x_url": "https://x.com/nayzix7", "joined": "2024-05-15", "status": "Contrat Actif"},
        {"ign": "Exqu", "name": "Exqu", "country": "🇫🇷", "pr": 12000, "x_handle": "@ExquFN", "x_url": "https://x.com/ExquFN", "joined": "2024-08-01", "status": "Partenaire"},
        {"ign": "Misha", "name": "Misha", "country": "🇫🇷", "pr": 8332, "x_handle": "@MishaFN_", "x_url": "https://x.com/MishaFN_", "joined": "2024-11-10", "status": "Contrat Actif"}
    ],
    "wip-esports": [
        {"ign": "Velryy", "name": "Velryy", "country": "🇫🇷", "pr": 26000, "x_handle": "@VelryyFN", "x_url": "https://x.com/VelryyFN", "joined": "2023-10-01", "status": "Contrat Actif"},
        {"ign": "Kielba", "name": "Kielba", "country": "🇵🇱", "pr": 16782, "x_handle": "@KielbaFN", "x_url": "https://x.com/KielbaFN", "joined": "2024-06-15", "status": "Partenaire"}
    ],
    "haikoo": [
        {"ign": "Maciak", "name": "Maciak", "country": "🇵🇱", "pr": 18000, "x_handle": "@MaciakFN", "x_url": "https://x.com/MaciakFN", "joined": "2024-04-01", "status": "Partenaire"},
        {"ign": "Joshbot", "name": "Joshbot", "country": "🇬🇧", "pr": 11000, "x_handle": "@JoshbotFN", "x_url": "https://x.com/JoshbotFN", "joined": "2024-08-01", "status": "Partenaire"},
        {"ign": "Kielba", "name": "Kielba", "country": "🇵🇱", "pr": 8089, "x_handle": "@KielbaFN", "x_url": "https://x.com/KielbaFN", "joined": "2024-10-15", "status": "Partenaire"}
    ],
    "g3nz-esport": [
        {"ign": "Ary", "name": "Ary", "country": "🇫🇷", "pr": 14000, "x_handle": "@AryFN_", "x_url": "https://x.com/AryFN_", "joined": "2024-02-10", "status": "Contrat Actif"},
        {"ign": "2Trash1zr", "name": "2Trash1zr", "country": "🇫🇷", "pr": 8500, "x_handle": "@2Trash1zr", "x_url": "https://x.com/2Trash1zr", "joined": "2024-06-01", "status": "Partenaire"},
        {"ign": "Efexy", "name": "Efexy", "country": "🇫🇷", "pr": 5500, "x_handle": "@EfexyFN", "x_url": "https://x.com/EfexyFN", "joined": "2024-09-15", "status": "Partenaire"},
        {"ign": "SereN", "name": "SereN", "country": "🇫🇷", "pr": 3695, "x_handle": "@SereNFN4", "x_url": "https://x.com/SereNFN4", "joined": "2025-01-05", "status": "Partenaire"}
    ],
    "bk-rog": [
        {"ign": "Hris", "name": "Hris", "country": "🇫🇷", "pr": 17515, "x_handle": "@HrisFN", "x_url": "https://x.com/HrisFN", "joined": "2024-05-01", "status": "Partenaire"}
    ],
    "novix-esport": [
        {"ign": "Okram", "name": "Okram", "country": "🇫🇷", "pr": 7000, "x_handle": "@OkramFN", "x_url": "https://x.com/OkramFN", "joined": "2024-07-01", "status": "Contrat Actif"},
        {"ign": "Actfv", "name": "Actfv", "country": "🇫🇷", "pr": 5000, "x_handle": "@ActfvFN", "x_url": "https://x.com/ActfvFN", "joined": "2024-09-15", "status": "Contrat Actif"},
        {"ign": "Joanee", "name": "Joanee", "country": "🇫🇷", "pr": 3132, "x_handle": "@JoaneeFN", "x_url": "https://x.com/JoaneeFN", "joined": "2025-01-10", "status": "Contrat Actif"}
    ],
    "australe-esport": [
        {"ign": "freuzi", "name": "freuzi", "country": "🇫🇷", "pr": 8000, "x_handle": "@freuziFN", "x_url": "https://x.com/freuziFN", "joined": "2024-06-01", "status": "Partenaire"},
        {"ign": "Kaktus", "name": "Kaktus", "country": "🇫🇷", "pr": 5494, "x_handle": "@KaktusFN_", "x_url": "https://x.com/KaktusFN_", "joined": "2024-10-15", "status": "Partenaire"}
    ],
    "valiant": [
        {"ign": "Trulex", "name": "Trulex", "country": "🇷🇸", "pr": 6500, "x_handle": "@TrulexFN", "x_url": "https://x.com/TrulexFN", "joined": "2024-08-01", "status": "Partenaire"},
        {"ign": "Robabz", "name": "Robabz", "country": "🇫🇷", "pr": 4533, "x_handle": "@Robabz_", "x_url": "https://x.com/Robabz_", "joined": "2024-10-10", "status": "Partenaire"}
    ],
    "reality-zone": [
        {"ign": "Nayro", "name": "Nayro", "country": "🇫🇷", "pr": 3500, "x_handle": "@NayroFN", "x_url": "https://x.com/NayroFN", "joined": "2023-05-01", "status": "Contrat Actif"},
        {"ign": "Kyli", "name": "Kyli", "country": "🇫🇷", "pr": 3200, "x_handle": "@KyliFN", "x_url": "https://x.com/KyliFN", "joined": "2023-08-15", "status": "Contrat Actif"},
        {"ign": "Zeyko", "name": "Zeyko", "country": "🇫🇷", "pr": 2800, "x_handle": "@ZeykoFN", "x_url": "https://x.com/ZeykoFN", "joined": "2024-01-10", "status": "Contrat Actif"}
    ],
    "team-fake": [
        {"ign": "Zeka", "name": "Zeka", "country": "🇫🇷", "pr": 3200, "x_handle": "@ZekaFN_", "x_url": "https://x.com/ZekaFN_", "joined": "2023-06-01", "status": "Contrat Actif"},
        {"ign": "Krox", "name": "Krox", "country": "🇫🇷", "pr": 2800, "x_handle": "@KroxFN", "x_url": "https://x.com/KroxFN", "joined": "2023-09-15", "status": "Contrat Actif"},
        {"ign": "Skyll", "name": "Skyll", "country": "🇫🇷", "pr": 2200, "x_handle": "@SkyllFN", "x_url": "https://x.com/SkyllFN", "joined": "2024-02-10", "status": "Contrat Actif"}
    ],
    "team-bsk": [
        {"ign": "Shado", "name": "Shado", "country": "🇫🇷", "pr": 2800, "x_handle": "@ShadoFN", "x_url": "https://x.com/ShadoFN", "joined": "2023-04-10", "status": "Contrat Actif"},
        {"ign": "Kenza", "name": "Kenza", "country": "🇫🇷", "pr": 2400, "x_handle": "@KenzaFN", "x_url": "https://x.com/KenzaFN", "joined": "2023-07-20", "status": "Contrat Actif"},
        {"ign": "Vortex", "name": "Vortex", "country": "🇫🇷", "pr": 1900, "x_handle": "@VortexFN_", "x_url": "https://x.com/VortexFN_", "joined": "2024-01-05", "status": "Contrat Actif"}
    ],
    "aten-esport": [
        {"ign": "Atenz", "name": "Atenz", "country": "🇫🇷", "pr": 2200, "x_handle": "@AtenzFN", "x_url": "https://x.com/AtenzFN", "joined": "2023-02-01", "status": "Contrat Actif"},
        {"ign": "Skyze", "name": "Skyze", "country": "🇫🇷", "pr": 1800, "x_handle": "@SkyzeFN", "x_url": "https://x.com/SkyzeFN", "joined": "2023-05-15", "status": "Contrat Actif"},
        {"ign": "Nox", "name": "Nox", "country": "🇫🇷", "pr": 1400, "x_handle": "@NoxFN_", "x_url": "https://x.com/NoxFN_", "joined": "2023-09-10", "status": "Contrat Actif"}
    ],
    "jupitar-esport": [
        {"ign": "Jupi", "name": "Jupi", "country": "🇫🇷", "pr": 2000, "x_handle": "@JupiFN", "x_url": "https://x.com/JupiFN", "joined": "2023-03-10", "status": "Contrat Actif"},
        {"ign": "Star", "name": "Star", "country": "🇫🇷", "pr": 1500, "x_handle": "@StarFN_", "x_url": "https://x.com/StarFN_", "joined": "2023-06-01", "status": "Contrat Actif"},
        {"ign": "Krono", "name": "Krono", "country": "🇫🇷", "pr": 1300, "x_handle": "@KronoFN", "x_url": "https://x.com/KronoFN", "joined": "2023-11-20", "status": "Contrat Actif"}
    ],
    "odious-esport": [
        {"ign": "Odi", "name": "Odi", "country": "🇫🇷", "pr": 1800, "x_handle": "@OdiFN", "x_url": "https://x.com/OdiFN", "joined": "2023-04-15", "status": "Contrat Actif"},
        {"ign": "Rage", "name": "Rage", "country": "🇫🇷", "pr": 1400, "x_handle": "@RageFN_", "x_url": "https://x.com/RageFN_", "joined": "2023-08-01", "status": "Contrat Actif"},
        {"ign": "Viper", "name": "Viper", "country": "🇫🇷", "pr": 1000, "x_handle": "@ViperFN_", "x_url": "https://x.com/ViperFN_", "joined": "2024-01-15", "status": "Contrat Actif"}
    ],
    "paps-esport": [
        {"ign": "Papito", "name": "Papito", "country": "🇫🇷", "pr": 1700, "x_handle": "@PapitoFN", "x_url": "https://x.com/PapitoFN", "joined": "2023-05-10", "status": "Contrat Actif"},
        {"ign": "Slay", "name": "Slay", "country": "🇫🇷", "pr": 1300, "x_handle": "@SlayFN_", "x_url": "https://x.com/SlayFN_", "joined": "2023-09-01", "status": "Contrat Actif"},
        {"ign": "Zen", "name": "Zen", "country": "🇫🇷", "pr": 900, "x_handle": "@ZenFN_", "x_url": "https://x.com/ZenFN_", "joined": "2024-02-15", "status": "Contrat Actif"}
    ],
    "pandaria-esport": [
        {"ign": "Panda", "name": "Panda", "country": "🇫🇷", "pr": 1500, "x_handle": "@PandaFN", "x_url": "https://x.com/PandaFN", "joined": "2023-07-01", "status": "Contrat Actif"},
        {"ign": "Bamboo", "name": "Bamboo", "country": "🇫🇷", "pr": 1100, "x_handle": "@BambooFN", "x_url": "https://x.com/BambooFN", "joined": "2023-10-15", "status": "Contrat Actif"},
        {"ign": "Lotus", "name": "Lotus", "country": "🇫🇷", "pr": 800, "x_handle": "@LotusFN_", "x_url": "https://x.com/LotusFN_", "joined": "2024-03-01", "status": "Contrat Actif"}
    ],
    "fly-again": [
        {"ign": "Flyer", "name": "Flyer", "country": "🇫🇷", "pr": 1300, "x_handle": "@FlyerFN", "x_url": "https://x.com/FlyerFN", "joined": "2023-08-01", "status": "Contrat Actif"},
        {"ign": "Wing", "name": "Wing", "country": "🇫🇷", "pr": 900, "x_handle": "@WingFN_", "x_url": "https://x.com/WingFN_", "joined": "2023-11-10", "status": "Contrat Actif"},
        {"ign": "Glide", "name": "Glide", "country": "🇫🇷", "pr": 700, "x_handle": "@GlideFN", "x_url": "https://x.com/GlideFN", "joined": "2024-04-15", "status": "Contrat Actif"}
    ]
}

# Update rosters_data
rosters_data["active_rosters"] = active_rosters

with open(DATA_DIR / "rosters.json", "w", encoding="utf-8") as f:
    json.dump(rosters_data, f, indent=2, ensure_ascii=False)

print(f"Updated rosters.json with {len(active_rosters)} active rosters!")
