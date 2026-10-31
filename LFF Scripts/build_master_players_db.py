import json
import urllib.parse

# Baseline non-french countries
FOREIGN_COUNTRIES = {
    'Kinstaar': 'ch', '4zr': 'ch', 'Minori': 'ch',
    'Pixie': 'se', 'Tjino': 'se',
    'PabloWingu': 'dk', 'Wox': 'dk', 'Umplify': 'dk',
    'SwizzY': 'ru', 'Malibuca': 'ru', 'maloyache': 'ru', 'dandepuzo': 'ru',
    'Merstach': 'lv',
    'Veno': 'gb', 'Joshbot': 'gb',
    'Vanyak3kk': 'ua',
    'MariusCOW': 'no', 'Ghonzo': 'no',
    'SereN': 'pl', 'Borsuk': 'pl', 'Foczka': 'pl', 'Szarik': 'pl',
    'Matez': 'pl', 'Kizers': 'pl', 'Kielba': 'pl', 'Maciak': 'pl', 'Okram': 'pl',
    'Zangi': 'it',
    'xzeevit': 'co', 'xzeevit4k': 'co', 'XZEEVIT': 'co',
    'Velryy': 'cz',
    'Hris': 'bg',
    'Vico': 'at', 'Vic0': 'at',
    'TaySon': 'si',
    'Trulex': 'rs',
    'Deyy': 'us',
    'Matsoe': 'nl'
}

SPECIAL_TRACKER_URLS = {
    'TheVic': 'https://fortnitetracker.com/fortnite/profile/epic/thevic%20%E3%83%8D/epic-events/overview?region=EU&platform=kbm',
    'Pixie': 'https://fortnitetracker.com/fortnite/profile/epic/havok%20%D1%80ixie%20b%C3%A4%C3%A4%C7%83/epic-events/overview'
}

# Known manual socials for historical legends
KNOWN_LEGENDS_SOCIALS = {
    'TheVic': {
        'x': 'https://x.com/TheVic_c',
        'youtube': 'https://youtube.com/@TheVicc',
        'twitch': 'https://twitch.tv/thevic'
    },
    'Gotaga': {
        'x': 'https://x.com/Gotaga',
        'twitch': 'https://twitch.tv/gotaga',
        'youtube': 'https://youtube.com/@GotagaTV',
        'instagram': 'https://instagram.com/gotaga'
    },
    'Mickalow': {
        'x': 'https://x.com/Mickalow_',
        'twitch': 'https://twitch.tv/mickalow',
        'youtube': 'https://youtube.com/@Mickalow'
    },
    'Robi': {
        'x': 'https://x.com/Robi_fn',
        'twitch': 'https://twitch.tv/robi'
    },
    'Adz': {
        'x': 'https://x.com/Adz_tv',
        'twitch': 'https://twitch.tv/adz_tv'
    },
    'Teeqzy': {
        'x': 'https://x.com/Teeqzy_',
        'twitch': 'https://twitch.tv/teeqzy',
        'youtube': 'https://youtube.com/@TeeqzyTV'
    },
    'NokSs': {
        'x': 'https://x.com/NokSstv',
        'twitch': 'https://twitch.tv/noksstv'
    },
    'Breso': {
        'x': 'https://x.com/Breso_fn'
    },
    'Skite': {
        'x': 'https://x.com/Skite',
        'twitch': 'https://twitch.tv/skite',
        'youtube': 'https://youtube.com/@SkiteTV'
    },
    'Vato': {
        'x': 'https://x.com/Vato_fn',
        'twitch': 'https://twitch.tv/vato'
    },
    'Nayte': {
        'x': 'https://x.com/naytefn',
        'twitch': 'https://twitch.tv/nayte',
        'youtube': 'https://youtube.com/@naytefn'
    },
    '4zr': {
        'x': 'https://x.com/4zr_fn',
        'twitch': 'https://twitch.tv/4zrr',
        'youtube': 'https://youtube.com/@4zr'
    },
    'Kinstaar': {
        'x': 'https://x.com/Kinstaar92i',
        'twitch': 'https://twitch.tv/kinstaar',
        'youtube': 'https://youtube.com/@Kinstaar'
    },
    'Airwaks': {
        'x': 'https://x.com/Airwaks',
        'twitch': 'https://twitch.tv/airwaks',
        'youtube': 'https://youtube.com/@Airwaks',
        'instagram': 'https://instagram.com/airwaks.tn'
    },
    'Nikof': {
        'x': 'https://x.com/Nikof_',
        'twitch': 'https://twitch.tv/nikof',
        'youtube': 'https://youtube.com/@Nikof'
    },
    'Hunter': {
        'x': 'https://x.com/Hunter_FN',
        'twitch': 'https://twitch.tv/hunter'
    },
    'Jbzz': {
        'x': 'https://x.com/Jbzzd',
        'twitch': 'https://twitch.tv/jbzz'
    },
    'Mzqqq': {
        'x': 'https://x.com/Mzqqq_'
    },
    'BadSniper': {
        'x': 'https://x.com/BadSniper_',
        'twitch': 'https://twitch.tv/badsniper'
    },
    'Badsniper': {
        'x': 'https://x.com/BadSniper_',
        'twitch': 'https://twitch.tv/badsniper'
    },
    'Falconly': {
        'x': 'https://x.com/Falconly_',
        'twitch': 'https://twitch.tv/falconly'
    },
    'Keolys': {
        'x': 'https://x.com/Keolys_',
        'twitch': 'https://twitch.tv/keolys'
    },
    'Kyzen': {
        'x': 'https://x.com/Kyzen_fn',
        'twitch': 'https://twitch.tv/kyzen'
    },
    'Hawkers': {
        'x': 'https://x.com/Hawkers_fn'
    },
    'Decypt': {
        'x': 'https://x.com/Decypt_'
    },
    'Blax': {
        'x': 'https://x.com/Blax_fn',
        'twitch': 'https://twitch.tv/blax'
    },
    'Blaxou': {
        'x': 'https://x.com/Blax_fn',
        'twitch': 'https://twitch.tv/blax'
    },
    'BlastR': {
        'x': 'https://x.com/BlastR_',
        'twitch': 'https://twitch.tv/blastr'
    },
    'Floki': {
        'x': 'https://x.com/Floki_fn',
        'twitch': 'https://twitch.tv/floki'
    },
    'Clément': {
        'x': 'https://x.com/Clement_fn',
        'twitch': 'https://twitch.tv/clement'
    },
    'Magl': {
        'x': 'https://x.com/Magl_fn'
    },
    'Chubs': {
        'x': 'https://x.com/Chubs_fn'
    },
    'Podasai': {
        'x': 'https://x.com/Podasai_'
    },
    'Orkh': {
        'x': 'https://x.com/Orkh_fn'
    },
    'Xsweeze': {
        'x': 'https://x.com/Xsweeze_'
    },
    'Snayzy': {
        'x': 'https://x.com/Snayzy_',
        'twitch': 'https://twitch.tv/snayzy',
        'youtube': 'https://youtube.com/@Snayzy'
    },
    'Andilex': {
        'x': 'https://x.com/AndilexFN',
        'twitch': 'https://twitch.tv/andilextv',
        'instagram': 'https://instagram.com/andilex_yt'
    },
    'Alpha': {
        'x': 'https://x.com/AlphaaGG'
    },
    'Malibuca': {
        'x': 'https://x.com/Malibuca',
        'twitch': 'https://twitch.tv/malibuca'
    },
    'Merstach': {
        'x': 'https://x.com/Merstach',
        'twitch': 'https://twitch.tv/merstach'
    },
    'Veno': {
        'x': 'https://x.com/VenoFN',
        'twitch': 'https://twitch.tv/veno'
    },
    'IDrop': {
        'x': 'https://x.com/IDropFN',
        'twitch': 'https://twitch.tv/idrop'
    },
    'Seekk': {
        'x': 'https://x.com/SeekkFN',
        'twitch': 'https://twitch.tv/seekk'
    },
    'Rax': {
        'x': 'https://x.com/Rax_fn'
    },
    'Zangi': {
        'x': 'https://x.com/zangifn',
        'twitch': 'https://twitch.tv/zangi'
    },
    'xzeevit': {
        'x': 'https://x.com/xzeevit4k',
        'twitch': 'https://twitch.tv/xzeevit'
    },
    'xzeevit4k': {
        'x': 'https://x.com/xzeevit4k',
        'twitch': 'https://twitch.tv/xzeevit'
    },
    'XZEEVIT': {
        'x': 'https://x.com/xzeevit4k',
        'twitch': 'https://twitch.tv/xzeevit'
    },
    'Deyy': {
        'x': 'https://x.com/DeyyFN',
        'twitch': 'https://twitch.tv/deyy'
    },
    'Trulex': {
        'x': 'https://x.com/Trulex',
        'twitch': 'https://twitch.tv/trulex'
    },
    'Vico': {
        'x': 'https://x.com/Vic0_fn',
        'twitch': 'https://twitch.tv/vico'
    },
    'Vic0': {
        'x': 'https://x.com/Vic0_fn',
        'twitch': 'https://twitch.tv/vico'
    }
}

with open('LFF Scripts/all_players_catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

with open('LFF Scripts/player_socials.json', 'r', encoding='utf-8') as f:
    ps = json.load(f)

with open('LFF Scripts/verified_player_handles.json', 'r', encoding='utf-8') as f:
    vph = json.load(f)

master_players = {}

for name in sorted(catalog.keys()):
    country = FOREIGN_COUNTRIES.get(name, 'fr')
    
    # Tracker URL
    if name in SPECIAL_TRACKER_URLS:
        tracker_url = SPECIAL_TRACKER_URLS[name]
    else:
        tracker_url = f"https://fortnitetracker.com/profile/all/{urllib.parse.quote(name)}"
    
    # Socials
    socials = {}
    
    # 1. From KNOWN_LEGENDS_SOCIALS
    if name in KNOWN_LEGENDS_SOCIALS:
        socials.update(KNOWN_LEGENDS_SOCIALS[name])
    
    # 2. From player_socials.json
    if name in ps:
        for net, val in ps[name].items():
            if net not in socials and val:
                if net == 'x':
                    val = val if val.startswith('http') else f"https://x.com/{val}"
                elif net == 'twitch':
                    val = val if val.startswith('http') else f"https://twitch.tv/{val}"
                elif net == 'youtube':
                    val = val if val.startswith('http') else (f"https://youtube.com/@{val}" if not val.startswith('UC') else f"https://youtube.com/channel/{val}")
                elif net == 'instagram':
                    val = val if val.startswith('http') else f"https://instagram.com/{val}"
                elif net == 'tiktok':
                    val = val if val.startswith('http') else f"https://tiktok.com/@{val}"
                elif net == 'discord':
                    val = val if val.startswith('http') else f"https://discord.gg/{val}"
                socials[net] = val
                
    # 3. From verified_player_handles.json (for X)
    if 'x' not in socials and name in vph and vph[name]:
        val = vph[name]
        socials['x'] = val if val.startswith('http') else f"https://x.com/{val}"
    
    master_players[name] = {
        'name': name,
        'country': country,
        'tracker_url': tracker_url,
        'socials': socials
    }

print(f"Built master players database with {len(master_players)} players.")
with_x = sum(1 for p in master_players.values() if p['socials'].get('x'))
with_multi = sum(1 for p in master_players.values() if len(p['socials']) > 1)
print(f"Players with verified X: {with_x}/{len(master_players)}")
print(f"Players with multiple verified socials: {with_multi}/{len(master_players)}")

with open('LFF Scripts/master_players.json', 'w', encoding='utf-8') as f:
    json.dump(master_players, f, indent=2, ensure_ascii=False)
print("Saved to LFF Scripts/master_players.json")
