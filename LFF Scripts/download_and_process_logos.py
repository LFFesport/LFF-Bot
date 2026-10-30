import urllib.request
import io
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

OUTPUT_DIR = os.path.abspath("LFF Logos")
os.makedirs(OUTPUT_DIR, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Referer": "https://fortnite-esports.fandom.com/"
}

def remove_background(img_data, tolerance=35):
    img = Image.open(io.BytesIO(img_data)).convert("RGBA")
    w, h = img.size
    
    # Check corners
    corners = [
        img.getpixel((0, 0)),
        img.getpixel((w - 1, 0)),
        img.getpixel((0, h - 1)),
        img.getpixel((w - 1, h - 1))
    ]
    
    # If already transparent, return as is
    if any(c[3] < 100 for c in corners):
        return img
        
    bg_r = sum(c[0] for c in corners) // 4
    bg_g = sum(c[1] for c in corners) // 4
    bg_b = sum(c[2] for c in corners) // 4
    
    pixels = img.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
            if dist < tolerance:
                pixels[x, y] = (r, g, b, 0)
            elif dist < tolerance * 1.4:
                alpha = int(255 * (dist - tolerance) / (tolerance * 0.4))
                pixels[x, y] = (r, g, b, alpha)
                
    return img

logo_sources = [
    # Fandom direct official transparent PNG/WebP
    ("Logo Vitality (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/6/63/Team_Vitalitylogo_std.png"),
    ("Logo Gentle Mates (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/e/e3/Gentle_Mateslogo_std.png"),
    ("Logo Karmine Corp (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/e/ed/Karmine_Corplogo_std.png"),
    ("Logo Solary (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/6/60/Solarylogo_std.png"),
    ("Logo LeStream (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/c/c4/LeStream_Esportlogo_std.png"),
    ("Logo TrainHard (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/0/0c/TrainHard_eSportslogo_std.png"),
    ("Logo Grizi (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/7/7f/Grizi_Esportlogo_std.png"),
    ("Logo Galions (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/3/3b/Galionslogo_std.png"),
    ("Logo GO (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/3/3f/GamersOriginlogo_std.png"),
    ("Logo Supremacy (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/3/3e/Supremacylogo_std.png"),
    ("Logo Oserv (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/e/e1/Oserv_Esportlogo_std.png"),
    ("Logo Valiant (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/1/17/Valiantlogo_std.png"),
    ("Logo Lyost (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/d/d9/Lyost_Esportlogo_std.png"),
    ("Logo Exalty (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/b/b8/Exaltylogo_std.png"),
    ("Logo BK ROG (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/3/34/BK_ROG_Esportslogo_std.png"),
    ("Logo MCES (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/7/7f/Team_MCESlogo_std.png"),
    ("Logo Millenium (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/0/09/Milleniumlogo_std.png"),
    ("Logo Zerance (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/8/81/Zerancelogo_std.png"),
    ("Logo Fly Again (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/7/74/Fly_Againlogo_std.png"),
    ("Logo X6 (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/d/d1/X6_E-sportlogo_std.png"),
    ("Logo MGA (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/a/a1/MGA_eSportlogo_std.png"),
    ("Logo K13 (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/7/74/K13_Esportlogo_std.png"),
    ("Logo Pandaria (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/3/39/Pandaria_Esportlogo_std.png"),
    ("Logo Pandore (fond vide).png", "https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/f/f7/Pandore_Esportlogo_std.png"),
    
    # Twitter / Unavatar sources with transparent conversion
    ("Logo GameWard (fond vide).png", "https://unavatar.io/twitter/GameWardTeam"),
    ("Logo LDLC (fond vide).png", "https://unavatar.io/twitter/LDLC_OL"),
    ("Logo HavoK (fond vide).png", "https://unavatar.io/twitter/HvKGGs"),
    ("Logo HavoK by Vitality (fond vide).png", "https://unavatar.io/twitter/HvKGGs")
]

for filename, url in logo_sources:
    out_path = os.path.join(OUTPUT_DIR, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            processed_img = remove_background(data)
            processed_img.save(out_path, "PNG")
            print(f"[OK] {filename} saved successfully ({processed_img.size})")
    except Exception as e:
        print(f"[ERR] {filename} from {url} failed: {e}")

# Duplicate Solary for Lunary if needed
solary_path = os.path.join(OUTPUT_DIR, "Logo Solary (fond vide).png")
lunary_path = os.path.join(OUTPUT_DIR, "Logo Lunary (fond vide).png")
if os.path.exists(solary_path) and not os.path.exists(lunary_path):
    img = Image.open(solary_path)
    img.save(lunary_path, "PNG")
    print("[OK] Logo Lunary (fond vide).png created from Solary base")

print("\nDone downloading and generating logos!")
