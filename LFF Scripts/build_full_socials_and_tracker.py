import json
import re

# 1. Load collected socials
with open('LFF Scripts/club_socials.json', 'r', encoding='utf-8') as f:
    c_soc = json.load(f)

with open('LFF Scripts/player_socials.json', 'r', encoding='utf-8') as f:
    p_soc = json.load(f)

with open('LFF Scripts/verified_player_handles.json', 'r', encoding='utf-8') as f:
    verified_player_x = json.load(f)

# Official verified club Twitter handles
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

# Club Fortnite Tracker slugs
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

# 2. Update clubs.json
with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
    clubs = json.load(f)

for c in clubs:
    cid = c['id']
    # Tracker URL
    slug = tracker_club_slugs.get(cid, cid)
    c['tracker_url'] = f"https://fortnitetracker.com/esports/organization/{slug}"
    
    # Official socials
    soc = {}
    # X
    x_handle = verified_club_x.get(cid)
    if x_handle:
        c['x_handle'] = f"@{x_handle}"
        c['x_url'] = f"https://x.com/{x_handle}"
        soc['x'] = f"https://x.com/{x_handle}"
    
    # Fandom socials
    f_soc = c_soc.get(cid, {})
    if f_soc.get('twitch'): soc['twitch'] = f"https://twitch.tv/{f_soc['twitch']}"
    if f_soc.get('youtube'):
        yt_val = f_soc['youtube']
        soc['youtube'] = f"https://youtube.com/channel/{yt_val}" if yt_val.startswith('UC') else f"https://youtube.com/@{yt_val}"
    if f_soc.get('instagram'): soc['instagram'] = f"https://instagram.com/{f_soc['instagram']}"
    if f_soc.get('tiktok'): soc['tiktok'] = f"https://tiktok.com/@{f_soc['tiktok']}"
    if f_soc.get('discord'): soc['discord'] = f"https://discord.gg/{f_soc['discord']}"
    
    c['socials'] = soc

with open('LFF Data/clubs.json', 'w', encoding='utf-8') as f:
    json.dump(clubs, f, indent=2, ensure_ascii=False)

print(f"Updated clubs.json with tracker_url and multi-network socials for {len(clubs)} clubs.")
