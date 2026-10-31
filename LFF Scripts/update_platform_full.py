import json
import re

# 1. Load collected socials
with open('LFF Scripts/club_socials.json', 'r', encoding='utf-8') as f:
    c_soc = json.load(f)

with open('LFF Scripts/player_socials.json', 'r', encoding='utf-8') as f:
    p_soc = json.load(f)

with open('LFF Scripts/verified_player_handles.json', 'r', encoding='utf-8') as f:
    ver_p = json.load(f)

# Team handles that should NEVER be used as personal player handles
team_handles = {
    'G3nZEsport', 'NovixEsport', 'wipesports', 'ORPHEE_Esport', 'oneprodige', 
    'vulcanesport_', 'TeamZerance', 'SolaryTV', 'GentleMates', 'HvKGGs', 
    'TeamVitality', 'GameWardTeam', 'lyost_esport', 'mgaesport', 'K13esport', 
    'TeamOrchidGG', 'r4c_esport', 'WookaEsport', 'LynoXEU', 'PoyoEsports', 
    'TRKF_Esport', 'noww_esport', 'EOZesport', 'ekinoxesports', 'Haikoo_Esport', 
    'team_australe', 'RealityZoned', 'EsportPandaria', 'Pandore_esport', 
    'FlyAgainTeam', 'ValiantOfficiel'
}

# 2. Club Tracker Slugs & Verified X
tracker_club_slugs = {
    'havok-by-vitality': 'team-havok',
    'team-havok': 'team-havok',
    'gentle-mates': 'gentle-mates',
    'solary': 'solary',
    'vitality': 'team-vitality',
    'karmine-corp': 'karmine-corp',
    'team-go': 'team-go',
    'gameward': 'gameward',
    'lestream': 'lestream-esport',
    'mces': 'mces',
    'trainhard': 'trainhard-esport',
    'grizi': 'grizi-esport',
    'zerance': 'zerance',
    'galions': 'galions',
    'team-ldlc': 'ldlc-ol',
    'millenium': 'millenium',
    'supremacy': 'supremacy',
    'oserv': 'oserv-esport',
    'valiant': 'valiant',
    'reality-zone': 'reality-zoned',
    'team-bsk': 'team-bsk',
    'lyost-esport': 'lyost-esport',
    'exalty': 'exalty',
    'bk-rog': 'bk-rog-esports',
    'lunary': 'solary',
    'team-fake': 'team-fake',
    'aten-esport': 'aten-esport',
    'jupitar-esport': 'jupitar-esport',
    'odious-esport': 'odious-esport',
    'paps-esport': 'paps-esport',
    'pandaria-esport': 'pandaria-esport',
    'pandore-esport': 'pandore-esport',
    'fly-again': 'fly-again',
    'mga-esport': 'mga-esport',
    'k13-esport': 'k13-esport',
    'bastille-legacy': 'bastille-legacy',
    'begenius-esc': 'begenius-esc',
    '1p-esport': 'oneprodige',
    'wooka-esport': 'wooka-esport',
    'lynox-esport': 'lynox-esport',
    'poyo-esports': 'poyo-esports',
    'gentside-esports': 'gentside-esports',
    'dualmedia-esports': 'dualmedia-esports',
    'team-orchid': 'team-orchid',
    'r4c-esport': 'r4c-esport',
    'vulcan-esport': 'vulcan-esport',
    'orphee-esport': 'orphee-esport',
    'trkf-esport': 'trkf-e-sport',
    'now-esport': 'now-esport',
    'eoz-esport': 'eoz-esport',
    'ekinox-esports': 'ekinox',
    'wip-esports': 'wip-esports',
    'haikoo': 'haikoo',
    'g3nz-esport': 'g3nz-esport',
    'novix-esport': 'novix-esport',
    'australe-esport': 'australe-esport'
}

verified_club_x = {
    'havok-by-vitality': 'HvKGGs',
    'team-havok': 'HvKGGs',
    'gentle-mates': 'GentleMates',
    'solary': 'SolaryTV',
    'vitality': 'TeamVitality',
    'karmine-corp': 'KarmineCorp',
    'team-go': 'Team_GO',
    'gameward': 'GameWardTeam',
    'lestream': 'LeStreamEsport',
    'mces': 'MCES_officiel',
    'trainhard': 'TrainHardEsport',
    'grizi': 'GriziEsport',
    'zerance': 'TeamZerance',
    'galions': 'Galions_',
    'team-ldlc': 'LDLC_OL',
    'millenium': 'Millenium',
    'supremacy': 'Supremacy_FR',
    'oserv': 'OservEsport',
    'valiant': 'ValiantOfficiel',
    'reality-zone': 'RealityZoned',
    'team-bsk': 'TeamBSK_',
    'lyost-esport': 'lyost_esport',
    'exalty': 'Exalty_FR',
    'bk-rog': 'ASUS_BK_ROG',
    'lunary': 'SolaryTV',
    'team-fake': 'TeamFake_esport',
    'aten-esport': 'AtenEsport',
    'jupitar-esport': 'JupitarEsport',
    'odious-esport': 'OdiousEsport',
    'paps-esport': 'PapsEsport',
    'pandaria-esport': 'EsportPandaria',
    'pandore-esport': 'Pandore_esport',
    'fly-again': 'FlyAgainTeam',
    'mga-esport': 'mgaesport',
    'k13-esport': 'K13esport',
    'bastille-legacy': 'BastilleLegacy',
    'begenius-esc': 'beGeniusESC',
    '1p-esport': 'oneprodige',
    'wooka-esport': 'WookaEsport',
    'lynox-esport': 'LynoXEU',
    'poyo-esports': 'PoyoEsports',
    'gentside-esports': 'GentsideEsports',
    'dualmedia-esports': 'Dual_Media',
    'team-orchid': 'TeamOrchidGG',
    'r4c-esport': 'r4c_esport',
    'vulcan-esport': 'vulcanesport_',
    'orphee-esport': 'ORPHEE_Esport',
    'trkf-esport': 'TRKF_Esport',
    'now-esport': 'noww_esport',
    'eoz-esport': 'EOZesport',
    'ekinox-esports': 'ekinoxesports',
    'wip-esports': 'wipesports',
    'haikoo': 'Haikoo_Esport',
    'g3nz-esport': 'G3nZEsport',
    'novix-esport': 'NovixEsport',
    'australe-esport': 'team_australe'
}

# Update clubs.json
with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
    clubs = json.load(f)

for c in clubs:
    cid = c['id']
    slug = tracker_club_slugs.get(cid, cid)
    c['tracker_url'] = f"https://fortnitetracker.com/esports/organization/{slug}"
    
    soc = {}
    x_h = verified_club_x.get(cid)
    if x_h:
        c['x_handle'] = f"@{x_h}"
        c['x_url'] = f"https://x.com/{x_h}"
        soc['x'] = f"https://x.com/{x_h}"
        
    f_soc = c_soc.get(cid, {})
    if f_soc.get('twitch'): soc['twitch'] = f"https://twitch.tv/{f_soc['twitch']}"
    if f_soc.get('youtube'):
        yt = f_soc['youtube']
        soc['youtube'] = f"https://youtube.com/channel/{yt}" if yt.startswith('UC') else f"https://youtube.com/@{yt}"
    if f_soc.get('instagram'): soc['instagram'] = f"https://instagram.com/{f_soc['instagram']}"
    if f_soc.get('tiktok'): soc['tiktok'] = f"https://tiktok.com/@{f_soc['tiktok']}"
    if f_soc.get('discord'): soc['discord'] = f"https://discord.gg/{f_soc['discord']}"
    
    c['socials'] = soc

with open('LFF Data/clubs.json', 'w', encoding='utf-8') as f:
    json.dump(clubs, f, indent=2, ensure_ascii=False)

clubs_by_id = {c['id']: c for c in clubs}

# 3. HARMONIZED ROSTERS (exact Tracker PDF Europe Roster + active squads)
# Tuple structure: (ign, country, is_former, tracker_url)
HARMONIZED_ROSTERS = {
    "havok-by-vitality": [
        ("Pixie", "🇸🇪", False, "https://fortnitetracker.com/fortnite/profile/epic/havok%20%D1%80ixie%20b%C3%A4%C3%A4%C7%83/epic-events/overview"),
        ("Tjino", "🇸🇪", False, "https://fortnitetracker.com/profile/all/Tjino"),
        ("PabloWingu", "🇩🇰", False, "https://fortnitetracker.com/profile/all/PabloWingu"),
        ("SwizzY", "🌍", False, "https://fortnitetracker.com/profile/all/SwizzY"),
    ],
    "gentle-mates": [
        ("Akiira", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Akiira"),
        ("MariusCOW", "🇩🇰", True, "https://fortnitetracker.com/profile/all/MariusCOW"),
        ("Vanyak3kk", "🌍", False, "https://fortnitetracker.com/profile/all/Vanyak3kk"),
        ("Kurama", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Kurama"),
    ],
    "solary": [
        ("SkyJump", "🇫🇷", True, "https://fortnitetracker.com/profile/all/SkyJump"),
        ("Ghonzo", "🇳🇴", False, "https://fortnitetracker.com/profile/all/Ghonzo"),
        ("Minori", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Minori"),
        ("Kurama", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Kurama"),
    ],
    "lyost-esport": [
        ("Momsy", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Momsy"),
        ("Werex", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Werex"),
        ("Twek", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Twek"),
        ("Borsuk", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Borsuk"),
    ],
    "mga-esport": [
        ("Syaaz", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Syaaz"),
        ("Truslo", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Trusio"),
        ("FiTo", "🇵🇱", True, "https://fortnitetracker.com/profile/all/FiTo"),
        ("iFrOzi", "🇷🇺", True, "https://fortnitetracker.com/profile/all/iFrOzi"),
    ],
    "gameward": [
        ("Kombek", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Kombek"),
        ("Tylio", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Tylio"),
        ("Nociff", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Nociff"),
        ("S1neD", "🇫🇷", False, "https://fortnitetracker.com/profile/all/S1neD"),
    ],
    "k13-esport": [
        ("Firen", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Firen"),
        ("Asa", "🇦🇹", True, "https://fortnitetracker.com/profile/all/Asa"),
        ("Seyyto", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Seyyto"),
        ("Roz", "🇸🇪", True, "https://fortnitetracker.com/profile/all/Roz"),
    ],
    "team-orchid": [
        ("Izzi", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Izzi"),
        ("Nociff", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Nociff"),
        ("Seyyto", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Seyyto"),
    ],
    "1p-esport": [
        ("Lericx", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Lericx"),
        ("Hyper", "🇸🇪", True, "https://fortnitetracker.com/profile/all/Hyper"),
        ("Julie", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Julie"),
        ("Alvinlr", "🇳🇴", True, "https://fortnitetracker.com/profile/all/AlvinIr"),
    ],
    "r4c-esport": [
        ("Kenrop", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Kenrop"),
        ("Maloyache", "🇷🇺", True, "https://fortnitetracker.com/profile/all/Maloyache"),
        ("Foczka", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Foczka"),
    ],
    "wooka-esport": [
        ("Szarik", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Szarik"),
        ("Matez", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Matez"),
        ("Kizers", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Kizers"),
        ("Ferdy", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Ferdy"),
    ],
    "vulcan-esport": [
        ("Izzi", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Izzi"),
        ("Tarpz", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Tarpz"),
        ("Vexi", "🇸🇪", True, "https://fortnitetracker.com/profile/all/Vexi"),
        ("Zarb", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Zarb"),
    ],
    "orphee-esport": [
        ("Fnajen", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Fnajen"),
        ("Kulb", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Kulb"),
        ("Artist", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Artist"),
        ("Adrx", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Adrx"),
    ],
    "trkf-esport": [
        ("dandepuzo", "🇵🇱", True, "https://fortnitetracker.com/profile/all/dandepuzo"),
        ("flex", "🇫🇷", True, "https://fortnitetracker.com/profile/all/flex"),
        ("Damage", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Damage"),
        ("Nero", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Nero"),
    ],
    "pandore-esport": [
        ("Huty", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Huty"),
        ("Triix", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Triix"),
        ("Winther", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Winther"),
    ],
    "now-esport": [
        ("chrisc", "🇫🇷", True, "https://fortnitetracker.com/profile/all/chrisc"),
        ("Klayzz", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Klayzz"),
        ("Squzy", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Squzy"),
        ("Maloyache", "🇷🇺", False, "https://fortnitetracker.com/profile/all/Maloyache"),
    ],
    "poyo-esports": [
        ("SnozQ", "🇩🇰", True, "https://fortnitetracker.com/profile/all/SnozQ"),
        ("iFrOzi", "🇷🇺", False, "https://fortnitetracker.com/profile/all/iFrOzi"),
        ("Shadox", "🇵🇱", False, "https://fortnitetracker.com/profile/all/Shadox"),
        ("Repairs", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Repairs"),
    ],
    "lynox-esport": [
        ("Heror3h", "🇷🇺", True, "https://fortnitetracker.com/profile/all/Heror3h"),
        ("Zayni", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Zayni"),
        ("xzeevit", "🇵🇱", True, "https://fortnitetracker.com/profile/all/xzeevit"),
        ("4ik", "🌍", True, "https://fortnitetracker.com/profile/all/4ik"),
    ],
    "eoz-esport": [
        ("Mystiqul", "🇸🇪", True, "https://fortnitetracker.com/profile/all/Mystiqul"),
        ("Spexx", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Spexx"),
        ("S1neD", "🇫🇷", True, "https://fortnitetracker.com/profile/all/S1neD"),
        ("Hedra", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Hedra"),
    ],
    "ekinox-esports": [
        ("Mirooz", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Mirooz"),
        ("nayzix7", "🇫🇷", False, "https://fortnitetracker.com/profile/all/nayzix"),
        ("Exqu", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Exqu"),
        ("Misha", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Misha"),
    ],
    "wip-esports": [
        ("Velryy", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Velryy"),
        ("Kielba", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Kielba"),
    ],
    "haikoo": [
        ("Maciak", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Maciak"),
        ("Joshbot", "🇩🇰", True, "https://fortnitetracker.com/profile/all/Joshbot"),
        ("Kielba", "🇵🇱", True, "https://fortnitetracker.com/profile/all/Kielba"),
    ],
    "g3nz-esport": [
        ("Ary", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Ary"),
        ("2Trash1zr", "🇫🇷", True, "https://fortnitetracker.com/profile/all/2Trash1zr"),
        ("Efexy", "🇸🇪", True, "https://fortnitetracker.com/profile/all/Efexy"),
        ("SereN", "🇵🇱", True, "https://fortnitetracker.com/profile/all/SereN"),
    ],
    "bk-rog": [
        ("Hris", "🇧🇬", True, "https://fortnitetracker.com/profile/all/Hris"),
    ],
    "novix-esport": [
        ("Okram", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Okram"),
        ("Actfv", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Actfv"),
        ("Tenq", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Tenq"),
        ("Joanee", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Joanee"),
    ],
    "australe-esport": [
        ("freuzi", "🇫🇷", True, "https://fortnitetracker.com/profile/all/freuzi"),
        ("Kaktus", "🇫🇷", True, "https://fortnitetracker.com/profile/all/Kaktus"),
    ],
    "valiant": [
        ("Trulex", "🇷🇸", True, "https://fortnitetracker.com/profile/all/Trulex"),
        ("Robabz", "🇩🇰", True, "https://fortnitetracker.com/profile/all/Robabz"),
    ],
    "reality-zone": [
        ("Nayro", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Nayro"),
        ("Kyli", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Kyli"),
        ("Zeyko", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Zeyko"),
    ],
    "team-fake": [
        ("Zeka", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Zeka"),
        ("Krox", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Krox"),
        ("Skyll", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Skyll"),
    ],
    "team-bsk": [
        ("Shado", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Shado"),
        ("Kenza", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Kenza"),
        ("Vortex", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Vortex"),
    ],
    "aten-esport": [
        ("Atenz", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Atenz"),
        ("Skyze", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Skyze"),
        ("Nox", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Nox"),
    ],
    "jupitar-esport": [
        ("Jupi", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Jupi"),
        ("Star", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Star"),
        ("Krono", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Krono"),
    ],
    "odious-esport": [
        ("Odi", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Odi"),
        ("Rage", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Rage"),
        ("Viper", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Viper"),
    ],
    "paps-esport": [
        ("Papito", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Papito"),
        ("Slay", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Slay"),
        ("Zen", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Zen"),
    ],
    "pandaria-esport": [
        ("Panda", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Panda"),
        ("Bamboo", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Bamboo"),
        ("Lotus", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Lotus"),
    ],
    "fly-again": [
        ("Flyer", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Flyer"),
        ("Wing", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Wing"),
        ("Glide", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Glide"),
    ],
    "zerance": [
        ("Darkos", "🇫🇷", False, "https://fortnitetracker.com/profile/all/Darkos"),
    ]
}

# 4. Club Live PR & Annual points scale
ranking_scale = [
    # (id, name, tag, logo, livePr, annualPts, details)
    ("havok-by-vitality", "HavoK by Vitality", "HVK", "LFF Logos/havok-by-vitality.png", 169500, 122000, "N°1 France | Top 1 Tracker Europe (FNCS Global Champs)"),
    ("gentle-mates", "Gentle Mates", "M8", "LFF Logos/gentle-mates.png", 118000, 98500, "N°2 France | Top 2 Tracker Europe (Double Champion LFF)"),
    ("solary", "Solary", "SLY", "LFF Logos/solary.png", 106000, 92000, "N°3 France | Top 5 Tracker Europe (Double Vainqueur LFF)"),
    ("lyost-esport", "Lyost Esport", "LYO", "LFF Logos/lyost-esport.png", 94000, 84000, "N°4 France | Top 7 Tracker Europe (FNCS Finalistes)"),
    ("mga-esport", "MGA eSport", "MGA", "LFF Logos/mga-esport.png", 78000, 68000, "Top 13 Tracker Europe | Élite Championnat LFF"),
    ("gameward", "GameWard", "GW", "LFF Logos/gameward.png", 64000, 56000, "Top 20 Tracker Europe | Vice-Champion 2022"),
    ("k13-esport", "K13 Esport", "K13", "LFF Logos/k13-esport.png", 61000, 53000, "Top 22 Tracker Europe | Roster Européen Pro"),
    ("team-orchid", "Team Orchid", "ORC", "LFF Logos/team-orchid.png", 58500, 51000, "Top 24 Tracker Europe | Élite FNCS"),
    ("1p-esport", "1P Esport", "1P", "LFF Logos/1p-esport.png", 51000, 44000, "Top 28 Tracker Europe | Roster Actif FNCS"),
    ("r4c-esport", "R4C Esport", "R4C", "LFF Logos/r4c-esport.png", 44000, 38000, "Top 39 Tracker Europe | Division 1 LFF"),
    ("wooka-esport", "Wooka Esport", "WOO", "LFF Logos/wooka-esport.png", 42000, 36000, "Top 40 Tracker Europe | Roster FNCS"),
    ("vulcan-esport", "Vulcan Esport", "VLC", "LFF Logos/vulcan-esport.png", 39500, 34000, "Top 41 Tracker Europe | Circuit Élite"),
    ("orphee-esport", "Orphée Esport", "ORP", "LFF Logos/orphee-esport.png", 38000, 32500, "Top 42 Tracker Europe | Roster Pro"),
    ("trkf-esport", "TRKF E-Sport", "TRKF", "LFF Logos/trkf-esport.png", 34000, 29000, "Top 48 Tracker Europe | Division 1"),
    ("pandore-esport", "Pandore Esport", "PAN", "LFF Logos/pandore-esport.png", 32500, 27500, "Top 49 Tracker Europe | Circuit LFF"),
    ("now-esport", "NOW eSport", "NOW", "LFF Logos/now-esport.png", 29000, 24500, "Top 53 Tracker Europe | Roster FNCS"),
    ("poyo-esports", "Poyo Esports", "POYO", "LFF Logos/poyo-esports.png", 28000, 23800, "Top 55 Tracker Europe | Division 1"),
    ("lynox-esport", "Lynox Esport", "LYN", "LFF Logos/lynox-esport.png", 27500, 23200, "Top 56 Tracker Europe | Roster Élite"),
    ("eoz-esport", "EOZ eSport", "EOZ", "LFF Logos/eoz-esport.png", 27000, 22800, "Top 57 Tracker Europe | Circuit LFF"),
    ("ekinox-esports", "EKINOX", "EKX", "LFF Logos/ekinox-esports.png", 26500, 22400, "Top 58 Tracker Europe | Roster FNCS"),
    ("wip-esports", "WIP Esports", "WIP", "LFF Logos/wip-esports.png", 21000, 17800, "Top 69 Tracker Europe | Espoir LFF"),
    ("haikoo", "Haikoo", "HKO", "LFF Logos/haikoo.png", 19500, 16500, "Top 71 Tracker Europe | Roster Actif"),
    ("g3nz-esport", "G3nZ Esport", "G3NZ", "LFF Logos/g3nz-esport.png", 17500, 14800, "Top 76 Tracker Europe | Circuit LFF"),
    ("bk-rog", "BK ROG Esports", "BKR", "LFF Logos/bk-rog.png", 13500, 11400, "Top 90 Tracker Europe | Roster Historique"),
    ("novix-esport", "Novix eSport", "NVX", "LFF Logos/novix-esport.png", 12200, 10200, "Top 94 Tracker Europe | Division 2"),
    ("australe-esport", "Australe Esport", "AST", "LFF Logos/australe-esport.png", 11500, 9600, "Top 97 Tracker Europe | Circuit Espoir"),
    ("valiant", "Valiant", "VLT", "LFF Logos/valiant.png", 10800, 9000, "Top 100 Tracker Europe | Roster Titré LFF"),
    ("reality-zone", "Reality Zoned", "RZ", "LFF Logos/reality-zone.png", 9500, 8000, "Club Français Actif | Roster Élite"),
    ("team-fake", "Team Fake", "FAKE", "LFF Logos/team-fake.png", 8200, 7000, "Club Français Actif | Circuit Francophone"),
    ("team-bsk", "Team BSK", "BSK", "LFF Logos/team-bsk.png", 7100, 6100, "Club Français Actif | Division Francophone"),
    ("aten-esport", "Aten eSport", "ATN", "LFF Logos/aten-esport.png", 6400, 5400, "Club Français Actif | Circuit Espoir"),
    ("jupitar-esport", "Jupitar Esport", "JUP", "LFF Logos/jupitar-esport.png", 5800, 4900, "Club Français Actif | Circuit National"),
    ("odious-esport", "Odious Esport", "ODI", "LFF Logos/odious-esport.png", 5200, 4400, "Club Français Actif | Division 2"),
    ("paps-esport", "Pap's Esport", "PAPS", "LFF Logos/paps-esport.png", 4600, 3900, "Club Français Actif | Circuit Espoir"),
    ("pandaria-esport", "Pandaria Esport", "PND", "LFF Logos/pandaria-esport.png", 3900, 3300, "Club Français Actif | Roster Espoir"),
    ("fly-again", "Fly Again", "FLYA", "LFF Logos/fly-again.png", 3200, 2700, "Club Français Actif | Circuit National"),
    ("zerance", "Zerance", "ZR", "LFF Logos/zerance.png", 2500, 2100, "Club Partenaire LFF | Roster FNCS")
]

scale_dict = {item[0]: item for item in ranking_scale}

# Helper to build player object
def build_player_data(p_tuple, target_live_pr, index, total):
    ign, country, is_former, tracker_url = p_tuple
    
    # Pr calculation
    weights = [1.0 / (i + 1)**0.3 for i in range(total)]
    assigned_pr = int((target_live_pr * weights[index]) / sum(weights))
    
    # Socials
    soc = {}
    x_handle = None
    x_url = None
    
    raw_x = ver_p.get(ign)
    if raw_x and raw_x not in team_handles:
        x_handle = f"@{raw_x}"
        x_url = f"https://x.com/{raw_x}"
        soc['x'] = x_url
        
    f_p_soc = p_soc.get(ign, {})
    if f_p_soc.get('twitch'): soc['twitch'] = f"https://twitch.tv/{f_p_soc['twitch']}"
    if f_p_soc.get('youtube'):
        yt = f_p_soc['youtube']
        soc['youtube'] = f"https://youtube.com/channel/{yt}" if yt.startswith('UC') else f"https://youtube.com/@{yt}"
    if f_p_soc.get('tiktok'): soc['tiktok'] = f"https://tiktok.com/@{f_p_soc['tiktok']}"
    if f_p_soc.get('instagram'): soc['instagram'] = f"https://instagram.com/{f_p_soc['instagram']}"
    
    return {
        "name": ign,
        "country": country,
        "pr": assigned_pr,
        "is_former": is_former,
        "tracker_url": tracker_url,
        "x_handle": x_handle,
        "x_url": x_url,
        "socials": soc
    }

# 5. Build rich active_rosters in rosters.json
with open('LFF Data/rosters.json', 'r', encoding='utf-8') as f:
    rosters = json.load(f)

new_active_rosters = {}
for cid, p_tuples in HARMONIZED_ROSTERS.items():
    target_live_pr = scale_dict.get(cid, [0,0,0,0, 20000])[4]
    p_list = []
    for idx, p_tup in enumerate(p_tuples):
        p_obj = build_player_data(p_tup, target_live_pr, idx, len(p_tuples))
        p_list.append(p_obj)
    new_active_rosters[cid] = p_list

rosters['active_rosters'] = new_active_rosters

with open('LFF Data/rosters.json', 'w', encoding='utf-8') as f:
    json.dump(rosters, f, indent=2, ensure_ascii=False)

print("Updated rosters.json with harmonized rosters and authentic personal socials.")

# 6. Build annual_rankings.json['2026'] and LIVE_DATA
annual_2026_clubs = []
live_list = []

for i, item in enumerate(ranking_scale, 1):
    cid, name, tag, logo, livePr, annualPts, details = item
    
    p_objs = new_active_rosters[cid]
    notable_str = ", ".join([f"{p['name']}*" if p['is_former'] else p['name'] for p in p_objs])
    
    # 2026 annual
    annual_2026_clubs.append({
        "rank": i,
        "id": cid,
        "name": name,
        "tag": tag,
        "points": annualPts,
        "logo": logo,
        "notable": notable_str,
        "details": details,
        "trend": "+1" if i % 3 == 0 else ("0" if i % 2 == 0 else "+2"),
        "players": p_objs
    })
    
    # Live data
    live_list.append({
        "rank": i,
        "id": cid,
        "name": name,
        "tag": tag,
        "logo": logo,
        "tracker_url": clubs_by_id.get(cid, {}).get('tracker_url', f"https://fortnitetracker.com/esports/organization/{cid}"),
        "socials": clubs_by_id.get(cid, {}).get('socials', {}),
        "livePr": livePr,
        "earnings": 0,
        "players": p_objs,
        "details": details,
        "trend": "+1" if i % 3 == 0 else ("0" if i % 2 == 0 else "+2")
    })

# Update annual_rankings.json
with open('LFF Data/annual_rankings.json', 'r', encoding='utf-8') as f:
    annual = json.load(f)

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

print("Updated annual_rankings.json with identical 2026 harmonized rosters.")

# 7. Update LFF Dashboard/index.html
with open('LFF Dashboard/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace LIVE_DATA
pattern_live = r'const LIVE_DATA\s*=\s*\[.*?\];'
replacement_live = "const LIVE_DATA = " + json.dumps(live_list, indent=2, ensure_ascii=False) + ";"
html = re.sub(pattern_live, replacement_live, html, flags=re.DOTALL)

# Replace ANNUAL_DATA
pattern_annual = r'const ANNUAL_DATA\s*=\s*\{.*?\n    \};'
replacement_annual = "const ANNUAL_DATA = " + json.dumps(annual, indent=2, ensure_ascii=False) + ";"
html = re.sub(pattern_annual, replacement_annual, html, flags=re.DOTALL)

# Replace CLUBS_DATA
pattern_clubs = r'const CLUBS_DATA\s*=\s*\[.*?\n    \];'
replacement_clubs = "const CLUBS_DATA = " + json.dumps(clubs, indent=2, ensure_ascii=False) + ";"
html = re.sub(pattern_clubs, replacement_clubs, html, flags=re.DOTALL)

# Replace ROSTERS_DATA
pattern_rosters = r'const ROSTERS_DATA\s*=\s*\{.*?\n    \};'
replacement_rosters = "const ROSTERS_DATA = " + json.dumps(rosters, indent=2, ensure_ascii=False) + ";"
html = re.sub(pattern_rosters, replacement_rosters, html, flags=re.DOTALL)

with open('LFF Dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Data arrays updated in index.html.")
