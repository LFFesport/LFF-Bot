import sys
import io
import json
import re
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

def search_fandom(term):
    url = f'https://fortnite-esports.fandom.com/api.php?action=query&list=search&srsearch={urllib.parse.quote(term)}&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [hit['title'] for hit in data.get('query', {}).get('search', [])]
    except Exception as e:
        return []

def get_page_links(title):
    url = f'https://fortnite-esports.fandom.com/api.php?action=parse&page={urllib.parse.quote(title)}&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            text = data.get('parse', {}).get('text', {}).get('*', '')
            links = re.findall(r'https?://(?:www\.)?(?:twitter|x)\.com/([A-Za-z0-9_]+)', text)
            handles = [h for h in links if h.lower() not in ('intent', 'share', 'widgets', 'home', 'search')]
            return handles
    except Exception as e:
        return []

with open('LFF Data/rosters.json', 'r', encoding='utf-8') as f:
    rosters = json.load(f)

all_players = set()
for club_id, p_list in rosters.get('active_rosters', {}).items():
    for p in p_list:
        if isinstance(p, dict) and p.get('ign'):
            all_players.add(p['ign'])

for t in rosters.get('transfers_log', []):
    if isinstance(t, dict) and t.get('player'):
        all_players.add(t['player'])

print(f"Total unique players to check: {len(all_players)}")

# Known verified handles
verified_handles = {
    # Gentle Mates
    'Vanyak3kk': 'Vanyak3kk',
    'Akiira': 'AkiiraFN',
    'MariusCOW': 'MariusCOW',
    'Kurama': 'FtnKurama',
    # Solary
    'Ghonzo': 'ghonzofn',
    'Minori': 'minorifn_',
    'SkyJump': 'skyjumpftn',
    'Kinstaar': 'Kinstaar92i',
    'Hunter': 'Hunter_FN',
    'Airwaks': 'Airwaks',
    'Nikof': 'Nikof',
    'DRG': 'DRG_FN',
    'Floki': 'Flokito_',
    'Decyptos': 'Decyptos',
    'Clement': 'Clement_fn',
    'Charyy': 'charyyfn',
    # HavoK
    'SwizzY': 'SwizzY281',
    'PabloWingu': 'PabloWingu',
    'Tjino': 'tjino9',
    'Pixie': 'pixiefnbr',
    'Wox': 'WoxSHTER',
    'Seekk': 'Seekkfn',
    'Keziix': 'Keziix7',
    'Snayzy': 'Snayzy',
    # GameWard
    'Tylio': 'Tylio77',
    'S1neD': 'S1neDfnn',
    'Kombek': 'kombekfn',
    'Nociff': 'nocifFN',
    # Lyost
    'Momsy': 'MomsyFN',
    'Werex': 'werexfnbr',
    'Twek': 'twekje',
    'Borsuk': 'borsukfn',
    # MGA
    'Syaaz': 'Syaazzfn',
    'Truslo': 'Trusiofnbr',
    'FiTo': 'FiTofnbr',
    'iFrOzi': 'iFr0zi_',
    # K13
    'Firen': 'Firenfn1',
    'Asa': 'Asafnr',
    'Seyyto': 'SeyytoFN',
    # Orchid
    'Izzi': 'izziFNBR',
    # 1P
    'Lericx': 'LericxFN',
    'Alvinlr': 'AlvinIr2',
    # R4C
    'Kenrop': 'KenropFN',
    'Maloyache': 'maloyache32',
    'Foczka': 'foczka_fn',
    # Wooka
    'Szarik': 'szarik17',
    'Matez': 'mateziak_',
    'Kizers': 'Kizers_',
    'Ferdy': 'Ferdy_ftn',
    # Vulcan
    'Tarpz': 'Tarpz7',
    'Vexi': 'vexi7k',
    # TrainHard / MCES / Vitality
    'Robabz': 'Robabz_',
    'BlastR': 'BlastR_FN',
    'Alpha': 'AlphaFN',
    'Yags': 'YagsFN',
    'Andilex': 'Andilex',
    'Xsweeze': 'xsweeze',
    'Jahq': 'Jahq_',
    'PodaSai': 'Podasai_',
    'TaySon': 'tayson2k',
    'Stompy': 'stompyv',
    'Klausen': 'KlausenFN',
    'BadSniper': 'BadSniperr',
    'Oslo': 'OsloFN',
    'Maxalambo': 'Maxalambo',
    'Trulex': 'TrulexFN',
    'Skyze': 'SkyzeFN',
}

results = dict(verified_handles)

for p in sorted(all_players):
    if not p or p in results:
        continue
    titles = search_fandom(p)
    found_handle = None
    for t in titles[:3]:
        handles = get_page_links(t)
        for h in handles:
            if p.lower() in h.lower() or h.lower() in p.lower():
                found_handle = h
                break
        if found_handle:
            break
    if found_handle:
        results[p] = found_handle
        print(f"FOUND [Fandom] {p:15} -> @{found_handle}")
    else:
        print(f"NOT FOUND: {p}")

with open('LFF Scripts/verified_player_handles.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\nDone! Saved {len(results)} player handles to verified_player_handles.json")
