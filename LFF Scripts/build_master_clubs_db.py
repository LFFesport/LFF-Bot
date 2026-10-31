import json

with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
    clubs = json.load(f)

with open('LFF Scripts/club_socials.json', 'r', encoding='utf-8') as f:
    cs = json.load(f)

master_clubs = {}

for c in clubs:
    cid = c['id']
    tracker_url = f"https://fortnitetracker.com/esports/organization/{cid}"
    
    # Merge socials
    socials = {}
    if cid in cs:
        for net, val in cs[cid].items():
            if val:
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
    
    if c.get('socials'):
        for k, v in c['socials'].items():
            if k not in socials and v:
                socials[k] = v
                
    if c.get('x_url') and 'x' not in socials:
        socials['x'] = c['x_url']
    elif c.get('xUrl') and 'x' not in socials:
        socials['x'] = c['xUrl']
        
    # Crucial user correction for Zerance:
    if cid == 'zerance':
        socials['x'] = "https://x.com/ZerancePartout"
        
    master_clubs[cid] = {
        'id': cid,
        'name': c['name'],
        'tag': c['tag'],
        'tracker_url': tracker_url,
        'socials': socials,
        'desc': c.get('desc', '')
    }

print(f"Master clubs count: {len(master_clubs)}")
print("Zerance socials:", master_clubs['zerance']['socials'])

with open('LFF Scripts/master_clubs.json', 'w', encoding='utf-8') as f:
    json.dump(master_clubs, f, indent=2, ensure_ascii=False)
