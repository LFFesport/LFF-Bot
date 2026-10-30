#!/usr/bin/env python3
"""
Ligue Française de Fortnite (LFF) - X (Twitter) Auto-Poster
Module d'automatisation des publications sur le compte officiel @LFFesport.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Fix console encoding on Windows
if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = (BASE_DIR / "LFF Data") if (BASE_DIR / "LFF Data").exists() else (BASE_DIR / "data")
ENV_PATH = (BASE_DIR / ".env") if (BASE_DIR / ".env").exists() else (Path(__file__).resolve().parent / ".env")

def load_env():
    """Charge les clés depuis le fichier .env"""
    env_vars = {}
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip()
    return env_vars

def save_env_keys(api_key, api_secret, access_token, access_token_secret):
    """Enregistre les clés X dans le fichier .env"""
    lines = []
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            lines = [l for l in f.readlines() if not any(l.startswith(k) for k in [
                "X_API_KEY=", "X_API_SECRET=", "X_ACCESS_TOKEN=", "X_ACCESS_TOKEN_SECRET="
            ])]

    lines.append(f"X_API_KEY={api_key}\n")
    lines.append(f"X_API_SECRET={api_secret}\n")
    lines.append(f"X_ACCESS_TOKEN={access_token}\n")
    lines.append(f"X_ACCESS_TOKEN_SECRET={access_token_secret}\n")

    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("✅ Clés d'API X enregistrées dans .env !")

def get_twitter_clients():
    """Initialise les clients Tweepy (v1 pour média, v2 pour publication)"""
    env = load_env()
    api_key = env.get("X_API_KEY")
    api_secret = env.get("X_API_SECRET")
    access_token = env.get("X_ACCESS_TOKEN")
    access_token_secret = env.get("X_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_token_secret]):
        return None, None

    try:
        import tweepy
        # Client v2 pour publier
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        # Auth v1.1 pour l'upload d'images
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        api_v1 = tweepy.API(auth)
        return client, api_v1
    except Exception as e:
        print(f"[!] Erreur d'initialisation Tweepy : {e}")
        return None, None

def publish_tweet(text, image_path=None, preview_only=False):
    """Publie un tweet avec ou sans image, ou en mode aperçu si les clés manquent."""
    print("=" * 70)
    print(" 📢 APERÇU DU TWEET À PUBLIER SUR @LFFesport")
    print("=" * 70)
    print(text)
    print("-" * 70)
    print(f"Longueur du texte : {len(text)} / 280 caractères")
    if image_path:
        print(f"Média joint       : {image_path}")
    print("=" * 70)

    if preview_only:
        print("ℹ️ Mode prévisualisation actif (aucun envoi sur le réseau).")
        return

    client, api_v1 = get_twitter_clients()
    if not client:
        print("\n⚠️ Clés de compte X manquantes dans le fichier .env.")
        print("Pour activer la publication réelle, renseignez vos 4 clés X gratuites :")
        print("  1. X_API_KEY (Consumer Key)")
        print("  2. X_API_SECRET (Consumer Secret)")
        print("  3. X_ACCESS_TOKEN")
        print("  4. X_ACCESS_TOKEN_SECRET")
        print("\nVous pouvez les configurer avec :")
        print("  python scripts/lff_twitter_bot.py --setup-keys")
        return

    try:
        media_ids = []
        if image_path and os.path.exists(image_path) and api_v1:
            print(f"📤 Téléversement de l'affiche ({image_path})...")
            media = api_v1.media_upload(filename=image_path)
            media_ids.append(media.media_id)
            print(f"✅ Média téléversé avec succès (ID: {media.media_id})")

        print("🚀 Envoi du tweet sur @LFFesport...")
        if media_ids:
            response = client.create_tweet(text=text, media_ids=media_ids)
        else:
            response = client.create_tweet(text=text)

        tweet_id = response.data.get("id")
        tweet_url = f"https://x.com/LFFesport/status/{tweet_id}"
        print(f"\n🎉 Tweet publié avec succès !")
        print(f"🔗 Lien : {tweet_url}")
    except Exception as e:
        print(f"\n[!] Échec de publication : {e}")

def create_ranking_tweet(season=2025, attach_poster=True):
    """Génère le texte calibré sous 280 caractères et le visuel du classement Power Ranking"""
    text = (
        f"🏆 CLASSEMENT LFF POWER RANKING\n\n"
        f"Top clubs après les derniers tournois :\n"
        f"🥇 #1 @GentleMates : 84.5k\n"
        f"🥈 #2 @SolaryTV : 76.2k\n"
        f"🥉 #3 @RealityZoneFR : 34.1k\n"
        f"4️⃣ @TeamFake_esport : 28.4k\n"
        f"5️⃣ @AtenEsport : 22.1k\n"
        f"6️⃣ @TeamBSK_ : 20.5k\n\n"
        f"#LFF #Fortnite"
    )

    image_path = None
    if attach_poster:
        poster_candidate = BASE_DIR / "LFF Photos" / "Affiche Officielle LFF 2026.jpg"
        if poster_candidate.exists():
            image_path = str(poster_candidate)

    return text, image_path

def create_mercato_tweet(player, to_club, from_club="Free Agent"):
    """Génère une alerte transfert officielle calibrée sous 280 caractères"""
    text = (
        f"🚨 #MERCATO LFF | OFFICIALISATION\n\n"
        f"Le joueur {player} s'engage officiellement avec {to_club} "
        f"(ex-{from_club}) !\n\n"
        f"Ses futurs points FNCS et Cash Cups seront crédités au club dans la LFF. 🇫🇷🌍\n\n"
        f"Bienvenue dans la ligue !\n"
        f"#LFF #Fortnite"
    )
    return text

def save_local_draft(title, text, image_path=None):
    """Enregistre un brouillon dans data/drafts.json et génère le lien Web Intent"""
    import urllib.parse
    drafts_file = DATA_DIR / "drafts.json"
    drafts_data = []
    if drafts_file.exists():
        with open(drafts_file, "r", encoding="utf-8") as f:
            try:
                drafts_data = json.load(f)
            except Exception:
                drafts_data = []

    encoded_text = urllib.parse.quote(text)
    intent_url = f"https://x.com/intent/tweet?text={encoded_text}"

    draft_entry = {
        "id": f"draft_{int(datetime.now().timestamp())}",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": title,
        "text": text,
        "image_path": image_path,
        "intent_url": intent_url,
        "status": "Draft"
    }

    drafts_data.insert(0, draft_entry)
    with open(drafts_file, "w", encoding="utf-8") as f:
        json.dump(drafts_data, f, indent=2, ensure_ascii=False)

    return draft_entry

def open_draft_in_browser(intent_url):
    """Ouvre le tweet pré-rempli directement dans Google Chrome"""
    import subprocess
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        subprocess.Popen([chrome_path, intent_url])
        print("🌐 Google Chrome a ouvert votre brouillon pré-rempli sur X !")
    except Exception as e:
        print(f"[!] Impossible d'ouvrir Chrome automatiquement : {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python lff_twitter_bot.py [commande]")
        print("  --draft-ranking     : Préparer et ouvrir le brouillon du classement sur X")
        print("  --preview-ranking   : Prévisualiser le tweet du classement")
        print("  --post-ranking      : Publier le classement Power Ranking sur @LFFesport")
        print("  --mercato <joueur> <club_arrivee> [club_depart] : Annoncer un transfert")
        print("  --custom <texte> [--image <chemin>]            : Publier un tweet personnalisé")
        print("  --setup-keys        : Configurer vos 4 clés d'API X en ligne de commande")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "--draft-ranking":
        text, img = create_ranking_tweet(attach_poster=True)
        draft = save_local_draft("Classement LFF Power Ranking 2025", text, img)
        print("=" * 70)
        print(" 📝 BROUILLON ENREGISTRÉ DANS LE PROJET (data/drafts.json)")
        print("=" * 70)
        print(text)
        print("-" * 70)
        print(f"🖼️ Affiche associée : {img}")
        print(f"🔗 Lien Web Intent direct : {draft['intent_url']}")
        print("=" * 70)
        open_draft_in_browser(draft['intent_url'])

    elif cmd == "--post-ranking":
        text, img = create_ranking_tweet(attach_poster=True)
        publish_tweet(text, image_path=img, preview_only=False)

    elif cmd == "--mercato" and len(sys.argv) >= 4:
        player = sys.argv[2]
        to_club = sys.argv[3]
        from_club = sys.argv[4] if len(sys.argv) >= 5 else "Free Agent"
        text = create_mercato_tweet(player, to_club, from_club)
        publish_tweet(text, preview_only=False)

    elif cmd == "--custom" and len(sys.argv) >= 3:
        text = sys.argv[2]
        img = None
        if "--image" in sys.argv:
            idx = sys.argv.index("--image")
            if idx + 1 < len(sys.argv):
                img = sys.argv[idx + 1]
        publish_tweet(text, image_path=img, preview_only=False)

    elif cmd == "--setup-keys":
        print("--- CONFIGURATION DES CLÉS X (TWITTER) POUR @LFFesport ---")
        k = input("X_API_KEY (Consumer Key) : ").strip()
        s = input("X_API_SECRET (Consumer Secret) : ").strip()
        t = input("X_ACCESS_TOKEN : ").strip()
        ts = input("X_ACCESS_TOKEN_SECRET : ").strip()
        if all([k, s, t, ts]):
            save_env_keys(k, s, t, ts)
        else:
            print("[!] Saisie incomplète.")
    else:
        print("[!] Commande non reconnue.")

if __name__ == "__main__":
    main()
