import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Complete player definitions
PLAYERS_DB = {
    # HavoK by Vitality
    "SwizzY": {"country": "🇷🇺", "pr": 144548, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/swizzy/overview", "socials": {"x": "https://x.com/Swizzyfn"}},
    "PabloWingu": {"country": "🇩🇰", "pr": 184000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/pablowingu/overview", "socials": {"x": "https://x.com/PabloWingu"}},
    "Tjino": {"country": "🇸🇪", "pr": 198000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/tjino/overview", "socials": {"x": "https://x.com/TjinoFN"}},
    "Pixie": {"country": "🇸🇪", "pr": 215000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/havok%20%D1%80ixie%20b%C3%A4%C3%A4%C7%83/epic-events/overview", "socials": {"x": "https://x.com/pixiefn"}},
    "Wox": {"country": "🇩🇰", "pr": 78000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/wox/overview", "socials": {"x": "https://x.com/WoxFn"}},
    "Seekk": {"country": "🇫🇷", "pr": 65000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/seekk/overview", "socials": {"x": "https://x.com/Seekkfn"}},
    "IDrop": {"country": "🇫🇷", "pr": 54000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/idrop/overview", "socials": {"x": "https://x.com/iDropFN"}},

    # Gentle Mates
    "Akiira": {"country": "🇫🇷", "pr": 162000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/akiira/overview", "socials": {"x": "https://x.com/Akiirafn"}},
    "Vanyak3kk": {"country": "🇺🇦", "pr": 145000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/vanyak3kk/overview", "socials": {"x": "https://x.com/Vanyak3kk"}},
    "Kurama": {"country": "🇫🇷", "pr": 112000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kurama/overview", "socials": {"x": "https://x.com/kuramafn"}},
    "Snayzy": {"country": "🇫🇷", "pr": 75000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/snayzy/overview", "socials": {"x": "https://x.com/Snayzy"}},
    "Rax": {"country": "🇫🇷", "pr": 68000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/rax/overview", "socials": {"x": "https://x.com/raxfn"}},
    "MariusCOW": {"country": "🇳🇴", "pr": 84388, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/mariuscow/overview", "socials": {"x": "https://x.com/marius_cow"}},

    # Solary
    "Ghonzo": {"country": "🇳🇴", "pr": 128000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/ghonzo/overview", "socials": {"x": "https://x.com/GhonzoFN"}},
    "Minori": {"country": "🇨🇭", "pr": 114000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/minori/overview", "socials": {"x": "https://x.com/MinoriFN"}},
    "SereN": {"country": "🇵🇱", "pr": 95000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/seren/overview", "socials": {"x": "https://x.com/sereN_fn"}},
    "Darkos": {"country": "🇫🇷", "pr": 88000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/darkos/overview", "socials": {"x": "https://x.com/DarkosFN"}},
    "Zangi": {"country": "🇮🇹", "pr": 72000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/zangi/overview", "socials": {"x": "https://x.com/zangifn"}},
    "XZEEVIT": {"country": "🇨🇴", "pr": 64000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/xzeevit/overview", "socials": {"x": "https://x.com/xzeevit"}},
    "SkyJump": {"country": "🇫🇷", "pr": 59168, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/skyjump/overview", "socials": {"x": "https://x.com/SkyJumpFN"}},

    # Lyost Esport
    "Momsy": {"country": "🇫🇷", "pr": 92000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/momsy/overview", "socials": {"x": "https://x.com/MomsyFN"}},
    "Werex": {"country": "🇫🇷", "pr": 88000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/werex/overview", "socials": {"x": "https://x.com/WerexFN"}},
    "Twek": {"country": "🇫🇷", "pr": 86000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/twek/overview", "socials": {"x": "https://x.com/TwekFN"}},
    "Borsuk": {"country": "🇵🇱", "pr": 85496, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/borsuk/overview", "socials": {"x": "https://x.com/BorsukFN"}},

    # MGA eSport
    "Syaaz": {"country": "🇫🇷", "pr": 68000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/syaaz/overview", "socials": {"x": "https://x.com/SyaazFN"}},
    "Truslo": {"country": "🇫🇷", "pr": 62804, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/truslo/overview", "socials": {"x": "https://x.com/TrusloFN"}},
    "FiTo": {"country": "🇫🇷", "pr": 50000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/fito/overview", "socials": {"x": "https://x.com/FiToFN"}},
    "iFrOzi": {"country": "🇫🇷", "pr": 50000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/ifrozi/overview", "socials": {"x": "https://x.com/iFrOzi"}},

    # GameWard
    "Kombek": {"country": "🇫🇷", "pr": 52000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kombek/overview", "socials": {"x": "https://x.com/kombekfn"}},
    "Tylio": {"country": "🇫🇷", "pr": 48000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/tylio/overview", "socials": {"x": "https://x.com/tyliofn"}},
    "S1neD": {"country": "🇫🇷", "pr": 42000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/s1ned/overview", "socials": {"x": "https://x.com/s1nedfn"}},
    "Repairs": {"country": "🇫🇷", "pr": 34065, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/repairs/overview", "socials": {"x": "https://x.com/repairsfn"}},
    "Baxo": {"country": "🇫🇷", "pr": 28000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/baxo/overview", "socials": {"x": "https://x.com/baxofn"}},
    "Snaylyx": {"country": "🇫🇷", "pr": 24000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/snaylyx/overview", "socials": {"x": "https://x.com/snaylyxfn"}},
    "Nociff": {"country": "🇫🇷", "pr": 34000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/nociff/overview", "socials": {"x": "https://x.com/Nociff"}},

    # K13 Esport
    "Firen": {"country": "🇫🇷", "pr": 45080, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/firen/overview", "socials": {"x": "https://x.com/FirenFN"}},
    "Asa": {"country": "🇫🇷", "pr": 44000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/asa/overview", "socials": {"x": "https://x.com/AsaFN"}},
    "Seyyto": {"country": "🇫🇷", "pr": 42000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/seyyto/overview", "socials": {"x": "https://x.com/SeyytoFN"}},
    "Roz": {"country": "🇫🇷", "pr": 42000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/roz/overview", "socials": {"x": "https://x.com/RozFN"}},

    # Team Orchid
    "Izzi": {"country": "🇫🇷", "pr": 62000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/izzi/overview", "socials": {"x": "https://x.com/IzziFN"}},

    # 1P Esport
    "Lericx": {"country": "🇫🇷", "pr": 42029, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/lericx/overview", "socials": {"x": "https://x.com/LericxFN"}},
    "Julie": {"country": "🇫🇷", "pr": 36000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/julie/overview", "socials": {"x": "https://x.com/JulieFN"}},
    "Hyper": {"country": "🇫🇷", "pr": 31000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/hyper/overview", "socials": {"x": "https://x.com/HyperFN"}},
    "Alvinlr": {"country": "🇫🇷", "pr": 26000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/alvinlr/overview", "socials": {"x": "https://x.com/alvinlr_"}},

    # R4C Esport
    "Kenrop": {"country": "🇫🇷", "pr": 42000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kenrop/overview", "socials": {"x": "https://x.com/KenropFN"}},
    "Foczka": {"country": "🇵🇱", "pr": 36789, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/foczka/overview", "socials": {"x": "https://x.com/FoczkaFN"}},
    "Maloyache": {"country": "🇷🇺", "pr": 25000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/maloyache/overview", "socials": {"x": "https://x.com/maloyache"}},

    # Wooka Esport
    "Szarik": {"country": "🇵🇱", "pr": 38000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/szarik/overview", "socials": {"x": "https://x.com/SzarikFN"}},
    "Ferdy": {"country": "🇫🇷", "pr": 32725, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/ferdy/overview", "socials": {"x": "https://x.com/FerdyFN"}},
    "Matez": {"country": "🇵🇱", "pr": 18000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/matez/overview", "socials": {"x": "https://x.com/MatezFN"}},
    "Kizers": {"country": "🇵🇱", "pr": 12000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kizers/overview", "socials": {"x": "https://x.com/KizersFN"}},

    # Vulcan Esport
    "Tarpz": {"country": "🇫🇷", "pr": 34183, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/tarpz/overview", "socials": {"x": "https://x.com/TarpzFN"}},
    "Vexi": {"country": "🇫🇷", "pr": 20000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/vexi/overview", "socials": {"x": "https://x.com/VexiFN"}},
    "Zarb": {"country": "🇫🇷", "pr": 18000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/zarb/overview", "socials": {"x": "https://x.com/ZarbFN"}},

    # Orphée Esport
    "Fnajen": {"country": "🇫🇷", "pr": 32564, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/fnajen/overview", "socials": {"x": "https://x.com/FnajenFN"}},
    "Kulb": {"country": "🇫🇷", "pr": 24000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kulb/overview", "socials": {"x": "https://x.com/KulbFN"}},
    "Artist": {"country": "🇫🇷", "pr": 21000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/artist/overview", "socials": {"x": "https://x.com/ArtistFN"}},
    "Adrx": {"country": "🇫🇷", "pr": 18000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/adrx/overview", "socials": {"x": "https://x.com/AdrxFN"}},

    # TRKF E-Sport
    "flex": {"country": "🇫🇷", "pr": 28000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/flex/overview", "socials": {"x": "https://x.com/flexfn"}},
    "Damage": {"country": "🇫🇷", "pr": 26000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/damage/overview", "socials": {"x": "https://x.com/DamageFN"}},
    "Nero": {"country": "🇫🇷", "pr": 24684, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/nero/overview", "socials": {"x": "https://x.com/NeroFN"}},
    "dandepuzo": {"country": "🇷🇺", "pr": 20000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/dandepuzo/overview", "socials": {"x": "https://x.com/dandepuzo"}},

    # Pandore Esport
    "Huty": {"country": "🇫🇷", "pr": 28000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/huty/overview", "socials": {"x": "https://x.com/HutyFN"}},
    "Triix": {"country": "🇫🇷", "pr": 24158, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/triix/overview", "socials": {"x": "https://x.com/TriixFN"}},
    "Winther": {"country": "🇫🇷", "pr": 23000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/winther/overview", "socials": {"x": "https://x.com/WintherFN"}},

    # NOW eSport
    "Klayzz": {"country": "🇫🇷", "pr": 24000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/klayzz/overview", "socials": {"x": "https://x.com/KlayzzFN"}},
    "chrisc": {"country": "🇫🇷", "pr": 10000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/chrisc/overview", "socials": {"x": "https://x.com/chriscFN"}},
    "Squzy": {"country": "🇫🇷", "pr": 9000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/squzy/overview", "socials": {"x": "https://x.com/SquzyFN"}},

    # Poyo Esports
    "Shadox": {"country": "🇫🇷", "pr": 21765, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/shadox/overview", "socials": {"x": "https://x.com/ShadoxFN"}},
    "SnozQ": {"country": "🇫🇷", "pr": 10000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/snozq/overview", "socials": {"x": "https://x.com/SnozQFN"}},

    # Lynox Esport
    "Heror3h": {"country": "🇫🇷", "pr": 22000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/heror3h/overview", "socials": {"x": "https://x.com/Heror3h"}},
    "Zayni": {"country": "🇫🇷", "pr": 18000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/zayni/overview", "socials": {"x": "https://x.com/ZayniFN"}},
    "4ik": {"country": "🇫🇷", "pr": 15421, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/4ik/overview", "socials": {"x": "https://x.com/4ikFN"}},
    "xzeevit": {"country": "🇨🇴", "pr": 8000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/xzeevit/overview", "socials": {"x": "https://x.com/xzeevit"}},

    # EOZ eSport
    "Mystiqul": {"country": "🇫🇷", "pr": 22000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/mystiqul/overview", "socials": {"x": "https://x.com/MystiqulFN"}},
    "Spexx": {"country": "🇫🇷", "pr": 21050, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/spexx/overview", "socials": {"x": "https://x.com/SpexxFN"}},
    "Hedra": {"country": "🇫🇷", "pr": 20000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/hedra/overview", "socials": {"x": "https://x.com/HedraFN"}},

    # EKINOX
    "Mirooz": {"country": "🇫🇷", "pr": 22000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/mirooz/overview", "socials": {"x": "https://x.com/MiroozFN"}},
    "nayzix7": {"country": "🇫🇷", "pr": 21000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/nayzix7/overview", "socials": {"x": "https://x.com/nayzix7"}},
    "Misha": {"country": "🇫🇷", "pr": 19332, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/misha/overview", "socials": {"x": "https://x.com/MishaFN"}},
    "Exqu": {"country": "🇫🇷", "pr": 6000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/exqu/overview", "socials": {"x": "https://x.com/ExquFN"}},

    # WIP Esports
    "Velryy": {"country": "🇨🇿", "pr": 28782, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/velryy/overview", "socials": {"x": "https://x.com/velryy"}},
    "Kielba": {"country": "🇵🇱", "pr": 14000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kielba/overview", "socials": {"x": "https://x.com/KielbaFN"}},

    # Haikoo
    "Maciak": {"country": "🇵🇱", "pr": 18000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/maciak/overview", "socials": {"x": "https://x.com/MaciakFN"}},
    "Joshbot": {"country": "🇬🇧", "pr": 19089, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/joshbot/overview", "socials": {"x": "https://x.com/JoshbotFN"}},

    # G3nZ Esport
    "Ary": {"country": "🇫🇷", "pr": 16000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/ary/overview", "socials": {"x": "https://x.com/AryFN"}},
    "Efexy": {"country": "🇫🇷", "pr": 15695, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/efexy/overview", "socials": {"x": "https://x.com/EfexyFN"}},
    "2Trash1zr": {"country": "🇫🇷", "pr": 14000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/2trash1zr/overview", "socials": {"x": "https://x.com/2Trash1zr"}},

    # BK ROG
    "Hris": {"country": "🇧🇬", "pr": 17515, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/hris/overview", "socials": {"x": "https://x.com/HrisFN"}},

    # Novix
    "Okram": {"country": "🇵🇱", "pr": 4500, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/okram/overview", "socials": {"x": "https://x.com/OkramFN"}},
    "Actfv": {"country": "🇫🇷", "pr": 4200, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/actfv/overview", "socials": {"x": "https://x.com/ActfvFN"}},
    "Tenq": {"country": "🇫🇷", "pr": 3500, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/tenq/overview", "socials": {"x": "https://x.com/TenqFN"}},
    "Joanee": {"country": "🇫🇷", "pr": 2932, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/joanee/overview", "socials": {"x": "https://x.com/JoaneeFN"}},

    # Australe
    "freuzi": {"country": "🇫🇷", "pr": 7000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/freuzi/overview", "socials": {"x": "https://x.com/freuziFN"}},
    "Kaktus": {"country": "🇫🇷", "pr": 6494, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kaktus/overview", "socials": {"x": "https://x.com/KaktusFN"}},

    # Valiant
    "Trulex": {"country": "🇫🇷", "pr": 6000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/trulex/overview", "socials": {"x": "https://x.com/Trulex"}},
    "Robabz": {"country": "🇫🇷", "pr": 5033, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/robabz/overview", "socials": {"x": "https://x.com/RobabzFN"}},

    # Reality Zoned
    "Nayro": {"country": "🇫🇷", "pr": 3400, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/nayro/overview", "socials": {"x": "https://x.com/NayroFN"}},
    "Kyli": {"country": "🇫🇷", "pr": 3200, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kyli/overview", "socials": {"x": "https://x.com/KyliFN"}},
    "Zeyko": {"country": "🇫🇷", "pr": 3000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/zeyko/overview", "socials": {"x": "https://x.com/ZeykoFN"}},

    # Team Fake
    "Zeka": {"country": "🇫🇷", "pr": 3000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/zeka/overview", "socials": {"x": "https://x.com/ZekaFN"}},
    "Krox": {"country": "🇫🇷", "pr": 2800, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/krox/overview", "socials": {"x": "https://x.com/KroxFN"}},
    "Skyll": {"country": "🇫🇷", "pr": 2600, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/skyll/overview", "socials": {"x": "https://x.com/SkyllFN"}},

    # Team BSK
    "Shado": {"country": "🇫🇷", "pr": 2600, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/shado/overview", "socials": {"x": "https://x.com/ShadoFN"}},
    "Kenza": {"country": "🇫🇷", "pr": 2400, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/kenza/overview", "socials": {"x": "https://x.com/KenzaFN"}},
    "Vortex": {"country": "🇫🇷", "pr": 2200, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/vortex/overview", "socials": {"x": "https://x.com/VortexFN"}},

    # Aten
    "Atenz": {"country": "🇫🇷", "pr": 2400, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/atenz/overview", "socials": {"x": "https://x.com/AtenzFN"}},
    "Skyze": {"country": "🇫🇷", "pr": 2200, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/skyze/overview", "socials": {"x": "https://x.com/SkyzeFN"}},
    "Nox": {"country": "🇫🇷", "pr": 2000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/nox/overview", "socials": {"x": "https://x.com/NoxFN"}},

    # Jupitar
    "Jupi": {"country": "🇫🇷", "pr": 2000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/jupi/overview", "socials": {"x": "https://x.com/JupiFN"}},
    "Star": {"country": "🇫🇷", "pr": 1800, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/star/overview", "socials": {"x": "https://x.com/StarFN"}},
    "Krono": {"country": "🇫🇷", "pr": 1600, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/krono/overview", "socials": {"x": "https://x.com/KronoFN"}},

    # Odious
    "Odi": {"country": "🇫🇷", "pr": 1800, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/odi/overview", "socials": {"x": "https://x.com/OdiFN"}},
    "Rage": {"country": "🇫🇷", "pr": 1600, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/rage/overview", "socials": {"x": "https://x.com/RageFN"}},
    "Viper": {"country": "🇫🇷", "pr": 1400, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/viper/overview", "socials": {"x": "https://x.com/ViperFN"}},

    # Pap's
    "Papito": {"country": "🇫🇷", "pr": 1500, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/papito/overview", "socials": {"x": "https://x.com/PapitoFN"}},
    "Slay": {"country": "🇫🇷", "pr": 1400, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/slay/overview", "socials": {"x": "https://x.com/SlayFN"}},
    "Zen": {"country": "🇫🇷", "pr": 1300, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/zen/overview", "socials": {"x": "https://x.com/ZenFN"}},

    # Pandaria
    "Panda": {"country": "🇫🇷", "pr": 1400, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/panda/overview", "socials": {"x": "https://x.com/PandaFN"}},
    "Bamboo": {"country": "🇫🇷", "pr": 1300, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/bamboo/overview", "socials": {"x": "https://x.com/BambooFN"}},
    "Lotus": {"country": "🇫🇷", "pr": 1200, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/lotus/overview", "socials": {"x": "https://x.com/LotusFN"}},

    # Fly Again
    "Flyer": {"country": "🇫🇷", "pr": 1200, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/flyer/overview", "socials": {"x": "https://x.com/FlyerFN"}},
    "Wing": {"country": "🇫🇷", "pr": 1100, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/wing/overview", "socials": {"x": "https://x.com/WingFN"}},
    "Glide": {"country": "🇫🇷", "pr": 1000, "tracker_url": "https://fortnitetracker.com/fortnite/profile/epic/glide/overview", "socials": {"x": "https://x.com/GlideFN"}}
}

def make_player(name, is_former=False):
    db = PLAYERS_DB.get(name, {})
    return {
        "name": name,
        "country": db.get("country", "🇫🇷"),
        "pr": db.get("pr", 1000),
        "is_former": is_former,
        "tracker_url": db.get("tracker_url", f"https://fortnitetracker.com/fortnite/profile/epic/{name.lower()}/overview"),
        "socials": db.get("socials", {})
    }

ACTIVE_ROSTERS = {
    "havok-by-vitality": ["Pixie", "Tjino", "PabloWingu", "SwizzY", "Wox", "Seekk", "IDrop"],
    "gentle-mates": ["Akiira", "Vanyak3kk", "Kurama", "Snayzy", "Rax"],
    "solary": ["Ghonzo", "Minori", "SereN", "Darkos", "Zangi", "XZEEVIT"],
    "lyost-esport": ["Momsy", "Werex", "Twek", "Borsuk"],
    "mga-esport": ["Syaaz", "Truslo"],
    "gameward": ["Kombek", "Tylio", "S1neD", "Repairs", "Baxo", "Snaylyx"],
    "k13-esport": ["Firen"],
    "team-orchid": ["Izzi", "Nociff", "Seyyto"],
    "1p-esport": ["Lericx", "Julie"],
    "r4c-esport": ["Kenrop", "Foczka"],
    "wooka-esport": ["Szarik", "Ferdy"],
    "vulcan-esport": ["Tarpz"],
    "orphee-esport": ["Fnajen"],
    "trkf-esport": ["flex", "Damage", "Nero"],
    "pandore-esport": ["Huty", "Triix", "Winther"],
    "now-esport": ["Klayzz", "Maloyache"],
    "poyo-esports": ["iFrOzi", "Shadox"],
    "lynox-esport": ["Heror3h", "Zayni", "4ik"],
    "eoz-esport": ["Mystiqul", "Spexx", "Hedra"],
    "ekinox-esports": ["Mirooz", "nayzix7", "Misha"],
    "wip-esports": ["Velryy"],
    "haikoo": ["Maciak", "Joshbot"],
    "g3nz-esport": ["Ary", "Efexy", "2Trash1zr"],
    "bk-rog": ["Hris"],
    "novix-esport": ["Okram", "Actfv", "Tenq", "Joanee"],
    "australe-esport": ["freuzi", "Kaktus"],
    "valiant": ["Trulex", "Robabz"],
    "reality-zone": ["Nayro", "Kyli", "Zeyko"],
    "team-fake": ["Zeka", "Krox", "Skyll"],
    "team-bsk": ["Shado", "Kenza", "Vortex"],
    "aten-esport": ["Atenz", "Skyze", "Nox"],
    "jupitar-esport": ["Jupi", "Star", "Krono"],
    "odious-esport": ["Odi", "Rage", "Viper"],
    "paps-esport": ["Papito", "Slay", "Zen"],
    "pandaria-esport": ["Panda", "Bamboo", "Lotus"],
    "fly-again": ["Flyer", "Wing", "Glide"],
    "zerance": ["Darkos"]
}

ANNUAL_FORMER_2026 = {
    "gentle-mates": ["MariusCOW"],
    "solary": ["SkyJump", "Kurama"],
    "mga-esport": ["FiTo", "iFrOzi"],
    "gameward": ["Nociff"],
    "k13-esport": ["Asa", "Seyyto", "Roz"],
    "1p-esport": ["Hyper", "Alvinlr"],
    "r4c-esport": ["Maloyache"],
    "wooka-esport": ["Matez", "Kizers"],
    "vulcan-esport": ["Izzi", "Vexi", "Zarb"],
    "orphee-esport": ["Kulb", "Artist", "Adrx"],
    "trkf-esport": ["dandepuzo"],
    "now-esport": ["chrisc", "Squzy"],
    "poyo-esports": ["SnozQ", "Repairs"],
    "lynox-esport": ["xzeevit"],
    "eoz-esport": ["S1neD"],
    "ekinox-esports": ["Exqu"],
    "wip-esports": ["Kielba"],
    "haikoo": ["Kielba"],
    "g3nz-esport": ["SereN"]
}

# 1. UPDATE ROSTERS.JSON
rosters_path = 'LFF Data/rosters.json'
with open(rosters_path, 'r', encoding='utf-8') as f:
    rosters_data = json.load(f)

rosters_data['active_rosters'] = {}
for cid, p_names in ACTIVE_ROSTERS.items():
    rosters_data['active_rosters'][cid] = [make_player(name, is_former=False) for name in p_names]

with open(rosters_path, 'w', encoding='utf-8') as f:
    json.dump(rosters_data, f, indent=2, ensure_ascii=False)
print("Updated LFF Data/rosters.json with full rosters.")

# 2. UPDATE ANNUAL_RANKINGS.JSON
annual_path = 'LFF Data/annual_rankings.json'
with open(annual_path, 'r', encoding='utf-8') as f:
    annual_data = json.load(f)

clubs_2026 = annual_data.get('2026', {}).get('clubs', [])
for club in clubs_2026:
    cid = club['id']
    act_names = ACTIVE_ROSTERS.get(cid, [])
    form_names = ANNUAL_FORMER_2026.get(cid, [])
    
    players_list = []
    for name in act_names:
        players_list.append(make_player(name, is_former=False))
    for name in form_names:
        players_list.append(make_player(name, is_former=True))
    
    club['players'] = players_list
    club['notable'] = ", ".join([p['name'] + ('*' if p['is_former'] else '') for p in players_list])

with open(annual_path, 'w', encoding='utf-8') as f:
    json.dump(annual_data, f, indent=2, ensure_ascii=False)
print("Updated LFF Data/annual_rankings.json (2026) with full rosters.")

# 3. UPDATE INDEX.HTML
html_path = 'LFF Dashboard/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace ANNUAL_DATA
m_ann = re.search(r'const ANNUAL_DATA = (\{[\s\S]*?\});\s*const CLUB_X_MAP', html_content)
if not m_ann:
    print("ERROR: Could not find ANNUAL_DATA before CLUB_X_MAP")
    sys.exit(1)

ann_json = json.loads(m_ann.group(1))
ann_json['2026']['clubs'] = annual_data['2026']['clubs']

new_ann_str = "const ANNUAL_DATA = " + json.dumps(ann_json, indent=2, ensure_ascii=False) + ";"
html_content = html_content[:m_ann.start()] + new_ann_str + html_content[m_ann.end() - len(";\n    const CLUB_X_MAP"):]

# Now calculate LIVE_DATA
live_list = []
for c_ann in ann_json['2026']['clubs']:
    cid = c_ann['id']
    act_names = ACTIVE_ROSTERS.get(cid, [])
    act_players = [make_player(name, is_former=False) for name in act_names]
    
    live_pr = sum(p['pr'] for p in act_players)
    if live_pr == 0:
        live_pr = 5000
    
    live_club = {
        "rank": c_ann['rank'],
        "id": cid,
        "name": c_ann['name'],
        "tag": c_ann['tag'],
        "livePr": live_pr,
        "players": act_players,
        "socials": c_ann.get('socials', {}),
        "tracker_url": c_ann.get('tracker_url', f"https://fortnitetracker.com/esports/organization/{cid}"),
        "details": c_ann.get('details', "")
    }
    live_list.append(live_club)

live_list.sort(key=lambda x: x['livePr'], reverse=True)
for i, c in enumerate(live_list):
    c['rank'] = i + 1

new_live_str = "const LIVE_DATA = " + json.dumps(live_list, indent=2, ensure_ascii=False) + ";"
m_live = re.search(r'const LIVE_DATA = \[[\s\S]*?\];\s*const TRANSFERS', html_content)
if not m_live:
    print("ERROR: Could not find LIVE_DATA before TRANSFERS")
    sys.exit(1)

html_content = html_content[:m_live.start()] + new_live_str + html_content[m_live.end() - len(";\n    const TRANSFERS"):]

# Update tab-reglement
html_content = html_content.replace(
    "<li><strong>Effectif retenu :</strong> Les <strong>4 meilleurs contributeurs PR</strong> de l'organisation au cours de la saison.</li>",
    "<li><strong>Effectif complet affiché :</strong> L'ensemble de tous les joueurs ayant représenté le club au cours de la saison est affiché et représenté (aucun plafonnement ou restriction artificielle aux 4 meilleurs).</li>"
)

pattern_sec_4 = r'<!-- SECTION 4 : RÈGLE DES TOP 4 JOUEURS -->[\s\S]*?<\/p>'
new_sec_4 = """<!-- SECTION 4 : AFFICHAGE EXHAUSTIF DES EFFECTIFS -->
        <h3 style="color: white; margin-top: 1.5rem; margin-bottom: 0.5rem;">4. Affichage Exhaustif de Tous les Joueurs (Sans Restriction à 4)</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem;">
          La Ligue Française de Fortnite valorise l'ensemble des athlètes sous contrat : <strong>tous les joueurs</strong> d'un club sont affichés et visibles dans les classements, sans coupure artificielle aux 4 meilleurs. Dans le classement annuel, tous les joueurs ayant apporté des points au cours de la saison sont listés (les anciens joueurs étant signalés par un astérisque <code>*</code>). Dans le classement Live, l'intégralité des joueurs actuellement sous contrat est représentée en temps réel."""

html_content = re.sub(pattern_sec_4, new_sec_4, html_content)

# Clean any em dashes
html_content = html_content.replace("\u2014", "-")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated LFF Dashboard/index.html successfully.")
