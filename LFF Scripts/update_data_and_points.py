import json

FT_EXACT_POINTS = {
    "havok-by-vitality": 741548,
    "team-havok": 741548,
    "gentle-mates": 503388,
    "solary": 361168,
    "lyost-esport": 351106,
    "mga-esport": 230804,
    "gameward": 176065,
    "k13-esport": 173080,
    "team-orchid": 171417,
    "1p-esport": 135029,
    "r4c-esport": 103789,
    "wooka-esport": 100725,
    "vulcan-esport": 96183,
    "orphee-esport": 95564,
    "trkf-esport": 78684,
    "pandore-esport": 75158,
    "now-esport": 65772,
    "poyo-esports": 63765,
    "lynox-esport": 63421,
    "eoz-esport": 63050,
    "ekinox-esports": 62332,
    "wip-esports": 42782,
    "haikoo": 37089,
    "g3nz-esport": 31695,
    "bk-rog": 17515,
    "novix-esport": 15132,
    "australe-esport": 13494,
    "valiant": 11033,
    "reality-zone": 9500,
    "reality-zoned": 9500,
    "team-fake": 8200,
    "team-bsk": 7100,
    "aten-esport": 5400,
    "jupitar-esport": 4800,
    "odious-esport": 4200,
    "paps-esport": 3900,
    "pandaria-esport": 3400,
    "fly-again": 2900,
    "zerance": 2500,
    "galions": 1800,
    "karmine-corp": 1200
}

# Verified comprehensive socials for clubs
ENRICHED_CLUB_SOCIALS = {
    "havok-by-vitality": {
        "x": "https://x.com/HvKGGs",
        "twitch": "https://twitch.tv/teamhavok",
        "instagram": "https://instagram.com/teamhavokgg",
        "tiktok": "https://tiktok.com/@teamhavok",
        "discord": "https://discord.gg/havok"
    },
    "team-havok": {
        "x": "https://x.com/HvKGGs",
        "twitch": "https://twitch.tv/teamhavok",
        "instagram": "https://instagram.com/teamhavokgg",
        "tiktok": "https://tiktok.com/@teamhavok",
        "discord": "https://discord.gg/havok"
    },
    "gentle-mates": {
        "x": "https://x.com/GentleMates",
        "twitch": "https://twitch.tv/gotaga",
        "youtube": "https://youtube.com/@teamgentlemates",
        "instagram": "https://instagram.com/gentlemates",
        "tiktok": "https://tiktok.com/@gentlemates",
        "discord": "https://discord.gg/gentle-mates"
    },
    "karmine-corp": {
        "x": "https://x.com/KarmineCorp",
        "twitch": "https://twitch.tv/karminecorp",
        "youtube": "https://youtube.com/@Karmine_Corp",
        "instagram": "https://instagram.com/karminecorp",
        "tiktok": "https://tiktok.com/@karmine_corp",
        "discord": "https://discord.gg/karminecorp"
    },
    "solary": {
        "x": "https://x.com/SolaryTV",
        "twitch": "https://twitch.tv/solaryfortnite",
        "youtube": "https://youtube.com/channel/UCTmx6aOnNK9O7qoF9_SoR5g",
        "instagram": "https://instagram.com/solarytv",
        "tiktok": "https://tiktok.com/@solary_fortnite",
        "discord": "https://discord.gg/solary"
    },
    "vitality": {
        "x": "https://x.com/TeamVitality",
        "twitch": "https://twitch.tv/vitality",
        "youtube": "https://youtube.com/channel/UCgjhed4ZWlmC25hS4Sgs7gw",
        "instagram": "https://instagram.com/teamvitality",
        "tiktok": "https://tiktok.com/@teamvitality",
        "discord": "https://discord.gg/vitality"
    },
    "gameward": {
        "x": "https://x.com/GameWardTeam",
        "twitch": "https://twitch.tv/gamewardteam",
        "youtube": "https://youtube.com/@GameWard",
        "instagram": "https://instagram.com/gamewardteam",
        "tiktok": "https://tiktok.com/@gamewardteam",
        "discord": "https://discord.gg/gameward"
    },
    "team-go": {
        "x": "https://x.com/Team_GO",
        "twitch": "https://twitch.tv/teamgogg",
        "youtube": "https://youtube.com/@teamgogg",
        "instagram": "https://instagram.com/teamgogg",
        "tiktok": "https://tiktok.com/@teamgogg"
    },
    "lestream": {
        "x": "https://x.com/LeStreamEsport",
        "twitch": "https://twitch.tv/lestream",
        "youtube": "https://youtube.com/@LeStream"
    },
    "mces": {
        "x": "https://x.com/MCES_officiel",
        "twitch": "https://twitch.tv/mces_officiel",
        "youtube": "https://youtube.com/@MCESofficiel",
        "instagram": "https://instagram.com/mces_officiel",
        "tiktok": "https://tiktok.com/@mces_officiel"
    },
    "trainhard": {
        "x": "https://x.com/TrainHardEsport",
        "twitch": "https://twitch.tv/trainhardwebtv",
        "instagram": "https://instagram.com/trainhardesport"
    },
    "grizi": {
        "x": "https://x.com/GriziEsport",
        "youtube": "https://youtube.com/@griziesport",
        "instagram": "https://instagram.com/griziesport",
        "tiktok": "https://tiktok.com/@griziesport"
    },
    "zerance": {
        "x": "https://x.com/TeamZerance",
        "twitch": "https://twitch.tv/teamzerance",
        "youtube": "https://youtube.com/@zerance",
        "instagram": "https://instagram.com/teamzerance",
        "tiktok": "https://tiktok.com/@teamzerance",
        "discord": "https://discord.gg/zerance"
    },
    "galions": {
        "x": "https://x.com/Galions_",
        "youtube": "https://youtube.com/@galions_team",
        "instagram": "https://instagram.com/galions_team",
        "tiktok": "https://tiktok.com/@galions_team",
        "discord": "https://discord.gg/yVDXNfp"
    },
    "team-ldlc": {
        "x": "https://x.com/LDLC_OL",
        "twitch": "https://twitch.tv/teamldlcol",
        "youtube": "https://youtube.com/@TeamLDLC",
        "instagram": "https://instagram.com/teamldlcol"
    },
    "millenium": {
        "x": "https://x.com/Millenium",
        "youtube": "https://youtube.com/@MilleniumVOD",
        "instagram": "https://instagram.com/millenium.team"
    },
    "supremacy": {
        "x": "https://x.com/Supremacy_FR",
        "youtube": "https://youtube.com/channel/UCisb_trxnFN_ylhpgGfbyqQ",
        "instagram": "https://instagram.com/supremacy_fr"
    },
    "oserv": {
        "x": "https://x.com/OservEsport",
        "twitch": "https://twitch.tv/oservtv",
        "youtube": "https://youtube.com/channel/UCHbWqCwlFzBh-ikyZ33aCtA"
    },
    "valiant": {
        "x": "https://x.com/ValiantOfficiel",
        "twitch": "https://twitch.tv/valiantofficiel",
        "youtube": "https://youtube.com/channel/UCfAj4rFVhgGCNWNTw0lVeZg",
        "instagram": "https://instagram.com/valiantofficiel",
        "tiktok": "https://tiktok.com/@vaillantofficiel",
        "discord": "https://discord.gg/valiant"
    },
    "reality-zone": {
        "x": "https://x.com/RealityZoned",
        "twitch": "https://twitch.tv/realityzoned",
        "youtube": "https://youtube.com/channel/UCSade4H7IspAjPAq5ejcrHQ",
        "instagram": "https://instagram.com/realityzoned",
        "tiktok": "https://tiktok.com/@realityzoned",
        "discord": "https://discord.gg/gQhyrW6VXg"
    },
    "lyost-esport": {
        "x": "https://x.com/lyost_esport",
        "twitch": "https://twitch.tv/lyostesport",
        "instagram": "https://instagram.com/lyost.esport",
        "tiktok": "https://tiktok.com/@lyost_esport",
        "discord": "https://discord.gg/rGRfA3yR9c"
    },
    "exalty": {
        "x": "https://x.com/Exalty_FR",
        "twitch": "https://twitch.tv/Exaltytv1",
        "youtube": "https://youtube.com/@Exalty",
        "instagram": "https://instagram.com/exalty_fr",
        "discord": "https://discord.gg/mUrf4QN"
    },
    "bk-rog": {
        "x": "https://x.com/ASUS_BK_ROG",
        "youtube": "https://youtube.com/channel/UCtPk46t9ycQtlFw4KDwd2Fw",
        "instagram": "https://instagram.com/bk_rog_esports",
        "tiktok": "https://tiktok.com/@bkrogesports",
        "discord": "https://discord.gg/bkrogesports"
    },
    "lunary": {
        "x": "https://x.com/SolaryTV",
        "twitch": "https://twitch.tv/solaryfortnite",
        "youtube": "https://youtube.com/channel/UCTmx6aOnNK9O7qoF9_SoR5g",
        "instagram": "https://instagram.com/solarytv"
    },
    "1p-esport": {
        "x": "https://x.com/oneprodige",
        "twitch": "https://twitch.tv/oneprodige",
        "instagram": "https://instagram.com/oneprodige",
        "tiktok": "https://tiktok.com/@oneprodige",
        "discord": "https://discord.gg/oneprodige"
    },
    "mga-esport": {
        "x": "https://x.com/mgaesport",
        "twitch": "https://twitch.tv/mgaesport",
        "youtube": "https://youtube.com/@mGaeSport",
        "instagram": "https://instagram.com/mgaesport",
        "tiktok": "https://tiktok.com/@mgaesport",
        "discord": "https://discord.gg/mgaesport"
    },
    "k13-esport": {
        "x": "https://x.com/K13esport",
        "twitch": "https://twitch.tv/K13Esport",
        "instagram": "https://instagram.com/k13esport1",
        "tiktok": "https://tiktok.com/@k13esport",
        "discord": "https://discord.gg/k13esport"
    },
    "team-orchid": {
        "x": "https://x.com/TeamOrchidGG",
        "twitch": "https://twitch.tv/teamorchidgg",
        "youtube": "https://youtube.com/@TeamOrchidGG",
        "instagram": "https://instagram.com/teamorchidgg",
        "tiktok": "https://tiktok.com/@team_orchid",
        "discord": "https://discord.gg/orchid"
    },
    "wooka-esport": {
        "x": "https://x.com/WookaEsport",
        "twitch": "https://twitch.tv/wooka_esport",
        "youtube": "https://youtube.com/@wookaesport5056",
        "instagram": "https://instagram.com/wookaesports",
        "tiktok": "https://tiktok.com/@wooka_esport",
        "discord": "https://discord.gg/wookaesport"
    },
    "lynox-esport": {
        "x": "https://x.com/LynoXEU",
        "twitch": "https://twitch.tv/lynoxeu",
        "youtube": "https://youtube.com/@LynoxEU",
        "tiktok": "https://tiktok.com/@lynox_esport",
        "discord": "https://discord.gg/lynoxeu"
    },
    "poyo-esports": {
        "x": "https://x.com/PoyoEsports",
        "twitch": "https://twitch.tv/poyocup",
        "youtube": "https://youtube.com/@poyocup",
        "instagram": "https://instagram.com/poyoesports",
        "tiktok": "https://tiktok.com/@poyo.esports",
        "discord": "https://discord.gg/fWYbQuWDMv"
    },
    "r4c-esport": {
        "x": "https://x.com/r4c_esport",
        "tiktok": "https://tiktok.com/@r4c_esport",
        "discord": "https://discord.gg/r4cesport"
    },
    "vulcan-esport": {
        "x": "https://x.com/vulcanesport_",
        "tiktok": "https://tiktok.com/@vulcanesport_",
        "discord": "https://discord.gg/vulcanesport"
    },
    "orphee-esport": {
        "x": "https://x.com/ORPHEE_Esport",
        "twitch": "https://twitch.tv/orpheecore",
        "tiktok": "https://tiktok.com/@orphee_core",
        "discord": "https://discord.gg/orphee"
    },
    "trkf-esport": {
        "x": "https://x.com/TRKF_Esport",
        "twitch": "https://twitch.tv/trkf_esport",
        "instagram": "https://instagram.com/trkf_esport",
        "tiktok": "https://tiktok.com/@trkf_esport",
        "discord": "https://discord.gg/trkf"
    },
    "pandore-esport": {
        "x": "https://x.com/Pandore_esport",
        "tiktok": "https://tiktok.com/@pandore_esport",
        "discord": "https://discord.gg/pandore"
    },
    "now-esport": {
        "x": "https://x.com/noww_esport",
        "twitch": "https://twitch.tv/noww_esport",
        "youtube": "https://youtube.com/@RVLESP",
        "instagram": "https://instagram.com/noww_esport",
        "tiktok": "https://tiktok.com/@noww_esport",
        "discord": "https://discord.gg/mMMCNBGKh2"
    },
    "eoz-esport": {
        "x": "https://x.com/EOZesport",
        "twitch": "https://twitch.tv/eozesport",
        "tiktok": "https://tiktok.com/@eozesport",
        "discord": "https://discord.gg/eozesport"
    },
    "ekinox-esports": {
        "x": "https://x.com/ekinoxesports",
        "twitch": "https://twitch.tv/ekinoxesports",
        "instagram": "https://instagram.com/ekinoxesports",
        "tiktok": "https://tiktok.com/@ekinoxesports",
        "discord": "https://discord.gg/ekinox"
    },
    "wip-esports": {
        "x": "https://x.com/wipesports",
        "instagram": "https://instagram.com/wip_esports",
        "tiktok": "https://tiktok.com/@wipesports",
        "discord": "https://discord.gg/wipesports"
    },
    "haikoo": {
        "x": "https://x.com/Haikoo_Esport",
        "tiktok": "https://tiktok.com/@haikoo_esport",
        "discord": "https://discord.gg/haikoo"
    },
    "g3nz-esport": {
        "x": "https://x.com/G3nZEsport",
        "tiktok": "https://tiktok.com/@g3nzesport",
        "discord": "https://discord.gg/g3nzesport"
    },
    "novix-esport": {
        "x": "https://x.com/NovixEsport",
        "tiktok": "https://tiktok.com/@novixesport",
        "discord": "https://discord.gg/novixesport"
    },
    "australe-esport": {
        "x": "https://x.com/team_australe",
        "twitch": "https://twitch.tv/teamaustrale",
        "instagram": "https://instagram.com/team.australe",
        "discord": "https://discord.gg/australe"
    },
    "team-fake": {
        "x": "https://x.com/TeamFake_esport",
        "tiktok": "https://tiktok.com/@teamfake",
        "discord": "https://discord.gg/teamfake"
    },
    "team-bsk": {
        "x": "https://x.com/TeamBSK_",
        "tiktok": "https://tiktok.com/@teambsk",
        "discord": "https://discord.gg/teambsk"
    },
    "aten-esport": {
        "x": "https://x.com/AtenEsport",
        "tiktok": "https://tiktok.com/@atenesport",
        "discord": "https://discord.gg/atenesport"
    },
    "jupitar-esport": {
        "x": "https://x.com/JupitarEsport",
        "tiktok": "https://tiktok.com/@jupitaresport",
        "discord": "https://discord.gg/jupitaresport"
    },
    "odious-esport": {
        "x": "https://x.com/OdiousEsport",
        "twitch": "https://twitch.tv/tvodious",
        "tiktok": "https://tiktok.com/@odious.esport",
        "discord": "https://discord.gg/odious"
    },
    "paps-esport": {
        "x": "https://x.com/PapsEsport",
        "twitch": "https://twitch.tv/lepapyofficiel",
        "tiktok": "https://tiktok.com/@papy.officiel"
    },
    "pandaria-esport": {
        "x": "https://x.com/EsportPandaria",
        "twitch": "https://twitch.tv/pandariaesportfr",
        "youtube": "https://youtube.com/channel/UC8BwLlUbJ13lidx718QnCFw",
        "instagram": "https://instagram.com/pandariaesportfr",
        "tiktok": "https://tiktok.com/@pandariaesport",
        "discord": "https://discord.gg/mg8CrWHFxn"
    },
    "fly-again": {
        "x": "https://x.com/FlyAgainTeam",
        "twitch": "https://twitch.tv/flyagainofficialteam",
        "youtube": "https://youtube.com/channel/UCJSaFlPaSgkpCUW53PWhLrA",
        "instagram": "https://instagram.com/flyagain.team",
        "discord": "https://discord.gg/A82YbYrb"
    }
}

def update_clubs():
    with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
        clubs = json.load(f)

    for c in clubs:
        cid = c['id']
        # Remove tier
        if 'tier' in c:
            del c['tier']
        # Update points
        if cid in FT_EXACT_POINTS:
            c['points_lff'] = FT_EXACT_POINTS[cid]
        # Update socials
        if cid in ENRICHED_CLUB_SOCIALS:
            c['socials'] = ENRICHED_CLUB_SOCIALS[cid]
        elif 'socials' not in c:
            c['socials'] = {}

    with open('LFF Data/clubs.json', 'w', encoding='utf-8') as f:
        json.dump(clubs, f, indent=2, ensure_ascii=False)
    print("Updated LFF Data/clubs.json")

def update_annual_rankings():
    with open('LFF Data/annual_rankings.json', 'r', encoding='utf-8') as f:
        annual = json.load(f)

    # Clean tier from all years
    for yr, data in annual.items():
        if isinstance(data, dict) and 'clubs' in data:
            for c in data['clubs']:
                if 'tier' in c:
                    del c['tier']

    # Update 2026 points with FT exact points and sort
    s2026 = annual.get('2026', {})
    if 'clubs' in s2026:
        for c in s2026['clubs']:
            cid = c.get('id')
            if cid in FT_EXACT_POINTS:
                c['points'] = FT_EXACT_POINTS[cid]
            if cid in ENRICHED_CLUB_SOCIALS:
                c['socials'] = ENRICHED_CLUB_SOCIALS[cid]
        
        # Sort by points descending
        s2026['clubs'].sort(key=lambda x: x.get('points', 0), reverse=True)
        # Update rank numbers
        for i, c in enumerate(s2026['clubs']):
            c['rank'] = i + 1

    with open('LFF Data/annual_rankings.json', 'w', encoding='utf-8') as f:
        json.dump(annual, f, indent=2, ensure_ascii=False)
    print("Updated LFF Data/annual_rankings.json")

def update_rosters():
    with open('LFF Data/rosters.json', 'r', encoding='utf-8') as f:
        rosters = json.load(f)

    for cid, players in rosters.get('active_rosters', {}).items():
        for p in players:
            if isinstance(p, dict) and 'tier' in p:
                del p['tier']

    with open('LFF Data/rosters.json', 'w', encoding='utf-8') as f:
        json.dump(rosters, f, indent=2, ensure_ascii=False)
    print("Updated LFF Data/rosters.json")

if __name__ == '__main__':
    update_clubs()
    update_annual_rankings()
    update_rosters()
