import json

with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
    clubs = json.load(f)

print(f"Total clubs: {len(clubs)}")
for c in clubs:
    print(f"{c['id']}: {c['name']} | Tier: {c.get('tier')} | X: {c.get('x_handle')} | Pts: {c.get('points_lff')}")
