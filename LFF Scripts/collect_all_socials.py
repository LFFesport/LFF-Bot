import urllib.request
import urllib.parse
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_fandom_socials(title):
    url = f'https://fortnite-esports.fandom.com/api.php?action=parse&page={urllib.parse.quote(title)}&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            text = data.get('parse', {}).get('text', {}).get('*', '')
            socials = {}
            
            # X / Twitter
            tw = re.findall(r'https?://(?:www\.)?(?:twitter|x)\.com/([A-Za-z0-9_]+)', text)
            clean_tw = [t for t in tw if t.lower() not in ('intent', 'share', 'widgets', 'home', 'search')]
            if clean_tw:
                socials['x'] = clean_tw[0]
                
            # Twitch
            twch = re.findall(r'https?://(?:www\.)?twitch\.tv/([A-Za-z0-9_]+)', text)
            clean_twch = [t for t in twch if t.lower() not in ('team', 'p')]
            if clean_twch:
                socials['twitch'] = clean_twch[0]
                
            # YouTube
            yt = re.findall(r'https?://(?:www\.)?youtube\.com/(?:c/|channel/|user/|@)?([A-Za-z0-9_.-]+)', text)
            clean_yt = [y for y in yt if y.lower() not in ('embed', 'watch', 'results', 'feed')]
            if clean_yt:
                socials['youtube'] = clean_yt[0]
                
            # Instagram
            ig = re.findall(r'https?://(?:www\.)?instagram\.com/([A-Za-z0-9_.-]+)', text)
            clean_ig = [i for i in ig if i.lower() not in ('p', 'reel', 'stories')]
            if clean_ig:
                socials['instagram'] = clean_ig[0]
                
            # TikTok
            tk = re.findall(r'https?://(?:www\.)?tiktok\.com/@([A-Za-z0-9_.-]+)', text)
            if tk:
                socials['tiktok'] = tk[0]
                
            # Discord
            disc = re.findall(r'https?://(?:www\.)?discord\.(?:gg|com/invite)/([A-Za-z0-9_.-]+)', text)
            if disc:
                socials['discord'] = disc[0]
                
            return socials
    except Exception:
        return {}

# 1. Load clubs and players
with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
    clubs = json.load(f)

with open('LFF Scripts/verified_player_handles.json', 'r', encoding='utf-8') as f:
    verified_players = json.load(f)

# Collect club socials
club_socials = {}
for c in clubs:
    cid = c['id']
    fandom_title = c['name'].replace(' ', '_')
    soc = get_fandom_socials(fandom_title)
    if soc:
        club_socials[cid] = soc
        print(f"Club {cid:20} -> {soc}")

# Collect player socials
player_socials = {}
for p_name in sorted(verified_players.keys()):
    soc = get_fandom_socials(p_name)
    if soc:
        player_socials[p_name] = soc
        print(f"Player {p_name:18} -> {soc}")

with open('LFF Scripts/club_socials.json', 'w', encoding='utf-8') as f:
    json.dump(club_socials, f, indent=2, ensure_ascii=False)

with open('LFF Scripts/player_socials.json', 'w', encoding='utf-8') as f:
    json.dump(player_socials, f, indent=2, ensure_ascii=False)

print(f"\nDone! Saved {len(club_socials)} club socials and {len(player_socials)} player socials.")
