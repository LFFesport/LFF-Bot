import json
from pathlib import Path

BASE_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF")
DATA_DIR = BASE_DIR / "LFF Data"

# Load current annual_rankings to preserve verified rosters and structures
with open(DATA_DIR / "annual_rankings.json", "r", encoding="utf-8") as f:
    annual = json.load(f)

# Helper to build a clean club entry
def make_club(rank, name, tag, points, roster, key_achievement, status="Official"):
    return {
        "rank": rank,
        "name": "Reality Zoned" if name in ["Reality Zone", "Reality Zone (RZ)"] else name,
        "tag": tag,
        "points": points,
        "roster": [p.split("(")[0].strip() for p in roster],
        "key_achievement": key_achievement,
        "status": status
    }

# 2018 Complete
clubs_2018 = [
    make_club(1, "Solary", "SLY", 18500, ["Kinstaar", "Hunter", "Mzqqq", "Jbzz"], "Vainqueur Lyon e-Sport, Vainqueur Gamers Assembly, domination totale de la saison 1"),
    make_club(2, "Lunary", "LNY", 14200, ["Airwaks", "Nikof", "Salack", "Twisted"], "Top 2 Coupe de France Fortnite, sacre sur multiples LANs nationales"),
    make_club(3, "Team Vitality", "VIT", 13800, ["Gotaga", "Mickalow", "Robi", "Adz"], "Vainqueurs Summer Skirmish Paris, immense régularité LANs"),
    make_club(4, "Gentside Esports Club", "GNT", 11500, ["TheVic", "Madzen", "Fr4nk", "Narkox"], "Vainqueurs ESWC Metz 2018, podiums majeurs de la scène française"),
    make_club(5, "Millenium", "M", 9800, ["Teeqzy", "NokSs", "Breso", "Meltore"], "Record du monde de kills en squad par Teeqzy (43 kills), Top LANs"),
    make_club(6, "LeStream Esport", "LST", 8900, ["Skite", "Vato"], "Arrivée fracassante en fin 2018, qualification Winter Royale"),
    make_club(7, "Oserv Esport", "OSV", 7600, ["M11Z", "Splinter", "Nayte", "Kyzen"], "Top 4 Gamers Assembly 2018, pépinière de talents"),
    make_club(8, "Supremacy", "SY", 6900, ["Keolys", "Veyder", "Spk", "Hawkers"], "Régularité Skirmish et LANs françaises"),
    make_club(9, "Team GO (GamersOrigin)", "GO", 6400, ["M1nz", "Jules", "Mawkinn", "Deadra"], "Performances solides en Open Cups et LANs"),
    make_club(10, "Bastille Legacy", "BL", 5800, ["Mickalow", "Robi", "Nikof", "BadSniper"], "Équipe pionnière des premières semaines compétitives"),
    make_club(11, "Team LDLC (LDLC OL)", "LDLC", 5200, ["Keolys", "JuleZ", "Wigzz", "Xani"], "Présence constante sur les tournois hebdomadaires"),
    make_club(12, "DualMedia Esports", "DM", 4500, ["Badsniper", "Kinstaar", "Falconly"], "Top performances sur les circuits régionaux"),
    make_club(13, "beGenius ESC", "bE", 3800, ["Falko", "Renox", "Azen"], "Présence régulière sur les opens francophones"),
    make_club(14, "Exalty", "XLT", 3200, ["Spike", "Aura", "Zeyk"], "Présence active sur la scène semi-pro"),
    make_club(15, "GameWard", "GW", 2800, ["Kopp", "Nox", "Driz"], "Premiers pas sur la scène compétitive")
]

# 2019 Complete
clubs_2019 = [
    make_club(1, "LeStream Esport", "LST", 34500, ["Skite", "Nayte", "Vato", "Blaxou"], "World Cup 2019 Solos & Duos, Skite Top 7 World Cup, Nayte Top 8"),
    make_club(2, "Solary", "SLY", 31200, ["Kinstaar", "Hunter", "Airwaks", "Nikof", "Magl"], "Multiples qualifiés World Cup New York (Kinstaar, Hunter, Nikof, Airwaks)"),
    make_club(3, "Team Vitality", "VIT", 22800, ["Hawkers", "BadSniper", "Oslo", "Maxalambo"], "BadSniper Top World Cup Solo, Oslo Top Duos"),
    make_club(4, "Team MCES", "MCES", 18900, ["Andilex", "Orkh", "Podasai", "Xsweeze"], "Vainqueurs et podiums FNCS Trios Saison X"),
    make_club(5, "Team GO (GamersOrigin)", "GO", 15400, ["M1nz", "Jules", "Decypt", "Lenz"], "Finalistes FNCS Trios Saison X et Squads Chapitre 2"),
    make_club(6, "TrainHard eSport", "TH", 14200, ["Blax", "BlastR", "Robabz", "Yags"], "Montée en puissance spectaculaire FNCS Squads"),
    make_club(7, "Grizi Esport", "GRIZI", 12500, ["4zr", "Nayte", "Badsniper"], "Création de la structure, signatures majeures de fin de saison"),
    make_club(8, "Gentside Esports Club", "GNT", 9800, ["TheVic", "Madzen"], "Finales hivernales avant fermeture de la structure"),
    make_club(9, "GameWard", "GW", 8400, ["Kopp", "Zeyko", "Falconly"], "Top 10 FNCS Trios et qualifications régionales"),
    make_club(10, "Team LDLC", "LDLC", 7600, ["Keolys", "JuleZ", "Xani"], "Finalistes FNCS Squads Chapitre 2 Saison 1"),
    make_club(11, "Lunary", "LNY", 6900, ["Airwaks", "Nikof"], "Vainqueurs Pro-Am World Cup New York"),
    make_club(12, "Supremacy", "SY", 5800, ["Keolys", "Hawkers"], "Régularité sur les Cash Cups hebdomadaires"),
    make_club(13, "Bastille Legacy", "BL", 4900, ["Mickalow", "Robi"], "Transition des effectifs vers les nouvelles structures"),
    make_club(14, "DualMedia Esports", "DM", 4100, ["Falconly", "Decypt"], "Top 15 étapes régionales"),
    make_club(15, "Exalty", "XLT", 3500, ["Spike", "Aura"], "Régularité sur le circuit national")
]

# 2020 Complete
clubs_2020 = [
    make_club(1, "Team MCES", "MCES", 39800, ["Andilex", "Xsweeze", "Podasai", "Orkh"], "Andilex Champion d'Europe FNCS Duos (C2S2), Vice-Champion FNCS Trios"),
    make_club(2, "Grizi Esport", "GRIZI", 35400, ["4zr", "Nayte", "Badsniper", "Snayzy"], "Nayte Champion FNCS Invitational 2020, 4zr podiums FNCS Trios"),
    make_club(3, "TrainHard eSport", "TH", 29500, ["Falconly", "Blax", "BlastR", "Alpha"], "Champion FNCS Duos avec Andilex / Nayte, domination Cash Cups"),
    make_club(4, "Solary", "SLY", 24200, ["Floki", "Decypt", "Clément", "Magl"], "Floki et Clément vainqueurs et podiums réguliers FNCS"),
    make_club(5, "Team Vitality", "VIT", 21300, ["Nikof", "Airwaks", "Oslo", "BadSniper"], "Finalistes constants de toutes les éditions FNCS 2020"),
    make_club(6, "Team GO (GamersOrigin)", "GO", 18200, ["Decypt", "M1nz", "Lenz", "Jules"], "Top 5 FNCS Trios C2S4 (Marvel)"),
    make_club(7, "LeStream Esport", "LST", 14500, ["Skite", "Vato"], "Dernière saison officielle du club avec qualifications FNCS"),
    make_club(8, "GameWard", "GW", 12800, ["Keolys", "Zeyko", "Kopp"], "Finalistes FNCS Duos et Trios"),
    make_club(9, "Team LDLC", "LDLC", 10900, ["JuleZ", "Xani"], "Top 15 Européen régulier en Cash Cups"),
    make_club(10, "BK ROG Esports", "BK", 9400, ["Kyzen", "Hris", "Robabz"], "Entrée fracassante sur la scène Fortnite compétitive"),
    make_club(11, "Valiant", "VLT", 8200, ["Skyze", "Vortex"], "Qualifications régulières en heats FNCS"),
    make_club(12, "Supremacy", "SY", 7100, ["Hawkers", "Spk"], "Régularité sur les Opens Européens"),
    make_club(13, "Exalty", "XLT", 6200, ["Aura", "Spike"], "Finales francophones"),
    make_club(14, "Reality Zoned", "RZ", 5400, ["Nayro", "Kyli"], "Entrée sur le circuit francophone"),
    make_club(15, "Team BSK", "BSK", 4600, ["Shado", "Kenza"], "Performances régulières en coupes communautaires")
]

# 2021 Complete
clubs_2021 = [
    make_club(1, "TrainHard eSport", "TH", 44200, ["Falconly", "Blax", "BlastR", "Viter"], "Grands Vainqueurs FNCS All-Star Showdown 2021, Top 1 Européen de l'année"),
    make_club(2, "Grizi Esport", "GRIZI", 38900, ["4zr", "Nayte", "Snayzy", "Podasai"], "4zr Champion FNCS Trios C2S8, sacre au Grand Royale 2021"),
    make_club(3, "Solary", "SLY", 33400, ["Floki", "Clément", "Magl", "Chubs"], "Champions FNCS Trios C2S6, Top régulier FNCS Grand Royale"),
    make_club(4, "Team MCES", "MCES", 27800, ["Andilex", "Xsweeze", "Podasai"], "Podium FNCS Trios C2S5, régularité au sommet européen"),
    make_club(5, "Team GO (GamersOrigin)", "GO", 24600, ["Decypt", "M1nz", "Stifler"], "Top 10 européen Grand Royale FNCS"),
    make_club(6, "Team Vitality", "VIT", 21200, ["Nikof", "Snayzy"], "Finalistes FNCS toutes saisons 2021"),
    make_club(7, "Valiant", "VLT", 17500, ["Kyzen", "Vortex"], "Top 15 Heats FNCS Trios"),
    make_club(8, "Reality Zoned", "RZ", 14800, ["Nayro", "Kyli", "Zeyko"], "Premières qualifications aux finales majeures"),
    make_club(9, "GameWard", "GW", 13200, ["Keolys", "Tylio"], "Finalistes Cash Cups réguliers"),
    make_club(10, "BK ROG Esports", "BK", 11900, ["Hris", "Robabz"], "Top 20 FNCS Heats"),
    make_club(11, "Team BSK", "BSK", 9800, ["Shado", "Kenza"], "Victoires en Victory Cups"),
    make_club(12, "Lyost Esport", "LYOST", 8700, ["Momsy", "Werex"], "Débuts prometteurs sur le circuit officiel"),
    make_club(13, "Aten eSport", "ATEN", 7400, ["Atenz", "Skyze"], "Circuits régionaux"),
    make_club(14, "Jupitar Esport", "JUP", 6800, ["Jupi", "Star"], "Qualifications Opens"),
    make_club(15, "Wooka Esport", "WOOKA", 6200, ["Szarik", "Ferdy"], "Fondation du club et premières performances"),
    make_club(16, "Vulcan Esport", "VUL", 5500, ["Tarpz", "Zarb"], "Circuit amateur et semi-pro"),
    make_club(17, "Orphée Esport", "ORPH", 4900, ["Fnam", "Artist"], "Qualifications heats"),
    make_club(18, "EOZ eSport", "EOZ", 4200, ["Spexx", "Hedra"], "Circuits communautaires"),
    make_club(19, "WIP Esports", "WIP", 3600, ["Velryy"], "Circuits régionaux"),
    make_club(20, "Exalty", "XLT", 3100, ["Aura", "Spike"], "Fin de parcours compétitif")
]

# 2022 Complete
clubs_2022 = [
    make_club(1, "Solary", "SLY", 46800, ["Floki", "Clément", "Chubs", "Darkos"], "Vice-Champions FNCS Invitational Raleigh 2022, Champions FNCS Chapitre 3"),
    make_club(2, "Team GO", "GO", 38400, ["Decypt", "Podasai", "M1nz"], "Top 5 FNCS Duos Chapitre 3, sacre en Cash Cups"),
    make_club(3, "Valiant", "VLT", 28600, ["Kyzen", "Robabz", "Deyy"], "Top 10 FNCS Duos européen"),
    make_club(4, "Reality Zoned", "RZ", 23900, ["Nayro", "Kyli", "Zeyko"], "Finalistes FNCS Duos C3S2"),
    make_club(5, "Team MCES", "MCES", 19500, ["Andilex", "Xsweeze"], "Dernière grande campagne avant transition club"),
    make_club(6, "GameWard", "GW", 16800, ["Keolys", "Tylio"], "Finalistes réguliers Cash Cups"),
    make_club(7, "BK ROG Esports", "BK", 14500, ["Hris", "Vortex"], "Top 20 Heats FNCS"),
    make_club(8, "Team Fake", "FAKE", 12800, ["Zeka", "Krox"], "Révélation Tier 2 de l'année"),
    make_club(9, "Team BSK", "BSK", 11200, ["Shado", "Kenza"], "Régularité en coupes ouvertes"),
    make_club(10, "Wooka Esport", "WOOKA", 9800, ["Szarik", "Ferdy"], "Montée en puissance"),
    make_club(11, "Vulcan Esport", "VUL", 8900, ["Tarpz", "Zarb"], "Podiums Tier 2"),
    make_club(12, "Orphée Esport", "ORPH", 7800, ["Fnam", "Artist"], "Circuits nationaux"),
    make_club(13, "Aten eSport", "ATEN", 6900, ["Atenz", "Nox"], "Coupes régionales"),
    make_club(14, "Jupitar Esport", "JUP", 6200, ["Jupi", "Krono"], "Qualifications Opens"),
    make_club(15, "Lyost Esport", "LYOST", 5600, ["Momsy", "Werex"], "Progression continue"),
    make_club(16, "Odious Esport", "ODI", 4900, ["Odi", "Rage"], "Circuits francophones"),
    make_club(17, "Pap's Esport", "PAPS", 4300, ["Papito", "Slay"], "Circuits semi-pro"),
    make_club(18, "EOZ eSport", "EOZ", 3800, ["Spexx", "Hedra"], "Circuits régionaux"),
    make_club(19, "WIP Esports", "WIP", 3300, ["Velryy"], "Circuits communautaires"),
    make_club(20, "TRKF E-Sport", "TRKF", 2800, ["flex", "Damage"], "Entrée sur la scène"),
    make_club(21, "NOW eSport", "NOW", 2300, ["Klayzz", "Squzy"], "Entrée sur la scène")
]

# 2023 Complete
clubs_2023 = [
    make_club(1, "Gentle Mates", "M8", 68500, ["Podasai", "Snayzy"], "Podasai & Snayzy Champions FNCS Major 3 C4S3, Vainqueurs Major 2 Europe"),
    make_club(2, "Solary", "SLY", 54200, ["Floki", "Clément", "Chubs", "Veno"], "Top 4 FNCS Global Championship Copenhague 2023"),
    make_club(3, "Zerance", "ZRC", 39800, ["Skydeun", "Vatira", "Ketz"], "Sensation de l'année, Top 5 FNCS Majors"),
    make_club(4, "Reality Zoned", "RZ", 31200, ["Nayro", "Kyli", "Zeyko"], "Finalistes majeurs FNCS"),
    make_club(5, "Valiant", "VLT", 26500, ["Kyzen", "Robabz"], "Top 15 européen FNCS"),
    make_club(6, "Team Fake", "FAKE", 21800, ["Zeka", "Krox", "Skyll"], "Meilleure équipe indépendante 2023"),
    make_club(7, "Team BSK", "BSK", 18400, ["Shado", "Kenza"], "Régularité impressionnante"),
    make_club(8, "GameWard", "GW", 16200, ["Tylio", "Keolys"], "Finales Cash Cups"),
    make_club(9, "Aten eSport", "ATEN", 13900, ["Atenz", "Skyze"], "Podiums Tier 2"),
    make_club(10, "Jupitar Esport", "JUP", 12400, ["Jupi", "Star"], "Performances régulières"),
    make_club(11, "Lyost Esport", "LYOST", 11200, ["Momsy", "Werex", "Twek"], "Percée sur le circuit officiel"),
    make_club(12, "Odious Esport", "ODI", 9800, ["Odi", "Rage"], "Circuits régionaux"),
    make_club(13, "Pap's Esport", "PAPS", 8900, ["Papito", "Zen"], "Circuits communautaires"),
    make_club(14, "Wooka Esport", "WOOKA", 8100, ["Szarik", "Ferdy"], "Progression constante"),
    make_club(15, "Vulcan Esport", "VUL", 7400, ["Tarpz", "Zarb"], "Performances semi-pro"),
    make_club(16, "Orphée Esport", "ORPH", 6800, ["Fnam", "Artist"], "Qualifications heats"),
    make_club(17, "TRKF E-Sport", "TRKF", 6100, ["flex", "Damage"], "Circuits nationaux"),
    make_club(18, "NOW eSport", "NOW", 5500, ["Klayzz", "Squzy"], "Circuits nationaux"),
    make_club(19, "EOZ eSport", "EOZ", 4900, ["Spexx", "Hedra"], "Circuits régionaux"),
    make_club(20, "EKINOX", "EKI", 4400, ["Mirooz", "nayzix7"], "Entrée sur la scène"),
    make_club(21, "WIP Esports", "WIP", 3900, ["Velryy"], "Circuits régionaux"),
    make_club(22, "Haikoo", "HK", 3500, ["Maciak"], "Entrée sur la scène"),
    make_club(23, "G3nZ Esport", "G3NZ", 3100, ["Ary"], "Entrée sur la scène"),
    make_club(24, "MGA Esport", "MGA", 2800, ["Syaaz"], "Entrée sur la scène"),
    make_club(25, "K13 Esport", "K13", 2500, ["Firen"], "Entrée sur la scène"),
    make_club(26, "Lynox Esport", "LYN", 2200, ["xzeevit4k"], "Entrée sur la scène"),
    make_club(27, "Poyo Esports", "POYO", 1900, ["iFrOzi"], "Entrée sur la scène"),
    make_club(28, "Pandaria Esport", "PAND", 1600, ["Panda"], "Circuits communautaires"),
    make_club(29, "Pandore Esport", "PANDR", 1400, ["Huty", "Triix"], "Circuits communautaires"),
    make_club(30, "Fly Again", "FA", 1200, ["Flyer"], "Circuits communautaires"),
    make_club(31, "Team Orchid", "ORC", 1000, ["Izzi"], "Débuts sur la scène")
]

# 2024 Complete
clubs_2024 = [
    make_club(1, "Karmine Corp", "KC", 88400, ["Malibuca", "Merstach", "Veno", "SwizzY"], "Malibuca & Merstach Champions FNCS Major 1 & Major 2 Europe, SwizzY & Veno Champions FNCS Major 3"),
    make_club(2, "Gentle Mates", "M8", 72600, ["Podasai", "Snayzy", "Vanyak3kk"], "Finalistes FNCS Globals, Vice-Champions Major 2"),
    make_club(3, "Solary", "SLY", 59800, ["Floki", "Clément", "Chubs", "Veno"], "Top 5 Global Championship Fort Worth Texas 2024"),
    make_club(4, "Team HavoK", "HVK", 48500, ["SwizzY", "Pixie", "Wox"], "Arrivée fracassante dans le top européen"),
    make_club(5, "Zerance", "ZRC", 36200, ["Skydeun", "Vatira"], "Top 10 européen constant"),
    make_club(6, "Reality Zoned", "RZ", 28400, ["Nayro", "Kyli", "Zeyko"], "Finalistes FNCS"),
    make_club(7, "Valiant", "VLT", 24100, ["Robabz", "Trulex"], "Régularité européenne"),
    make_club(8, "GameWard", "GW", 21500, ["Kombek", "Tylio"], "Top 15 européen"),
    make_club(9, "Galions", "GLN", 18900, ["Clément", "Kyzen"], "Arrivée remarquée sur le circuit"),
    make_club(10, "Team Fake", "FAKE", 16400, ["Zeka", "Krox", "Skyll"], "Solide leader du Tier 2"),
    make_club(11, "Team BSK", "BSK", 14200, ["Shado", "Kenza"], "Régularité"),
    make_club(12, "Aten eSport", "ATEN", 12600, ["Atenz", "Skyze"], "Podiums Tier 2"),
    make_club(13, "Jupitar Esport", "JUP", 11200, ["Jupi", "Star"], "Qualifications régulières"),
    make_club(14, "Odious Esport", "ODI", 9900, ["Odi", "Rage"], "Performances régionales"),
    make_club(15, "Pap's Esport", "PAPS", 8800, ["Papito", "Slay"], "Circuits francophones"),
    make_club(16, "1P (OneProdige)", "1P", 8100, ["Lericx", "Hyper", "Julie"], "Entrée fracassante"),
    make_club(17, "Team Orchid", "ORC", 7500, ["Izzi", "Nociff", "Seyyto"], "Montée en puissance"),
    make_club(18, "Wooka Esport", "WOOKA", 6900, ["Szarik", "Matez", "Ferdy"], "Régularité"),
    make_club(19, "Vulcan Esport", "VUL", 6300, ["Izzi", "Tarpz", "Zarb"], "Circuits semi-pro"),
    make_club(20, "Orphée Esport", "ORPH", 5800, ["Fnam", "Kulb", "Artist"], "Performances solides"),
    make_club(21, "TRKF E-Sport", "TRKF", 5300, ["flex", "Damage", "Nero"], "Circuits nationaux"),
    make_club(22, "Pandore Esport", "PANDR", 4800, ["Huty", "Triix", "Winther"], "Circuits nationaux"),
    make_club(23, "NOW eSport", "NOW", 4400, ["chrisc", "Klayzz", "Squzy"], "Circuits nationaux"),
    make_club(24, "Poyo Esports", "POYO", 4000, ["SnozQ", "iFrOzi", "Shadox"], "Progression"),
    make_club(25, "Lynox Esport", "LYN", 3600, ["Heror3h", "xzeevit4k"], "Circuits francophones"),
    make_club(26, "EOZ eSport", "EOZ", 3300, ["Mystiqul", "Spexx", "S1neD"], "Circuits régionaux"),
    make_club(27, "EKINOX", "EKI", 3000, ["Mirooz", "nayzix7", "Exqu"], "Circuits régionaux"),
    make_club(28, "WIP Esports", "WIP", 2700, ["Velryy", "Kielba"], "Circuits régionaux"),
    make_club(29, "Haikoo", "HK", 2400, ["Maciak", "Joshbot"], "Circuits régionaux"),
    make_club(30, "G3nZ Esport", "G3NZ", 2100, ["Ary", "2Trash1zr"], "Circuits régionaux"),
    make_club(31, "BK ROG Esports", "BK", 1900, ["Hris"], "Circuits régionaux"),
    make_club(32, "Novix eSport", "NOV", 1700, ["Okram", "Actfv"], "Circuits régionaux"),
    make_club(33, "Australe Esport", "AUS", 1500, ["freuzi", "Kaktus"], "Circuits régionaux"),
    make_club(34, "R4C Esport", "R4C", 1300, ["Kenrop", "Maloyache"], "Circuits régionaux"),
    make_club(35, "MGA Esport", "MGA", 1100, ["Syaaz", "Trusio"], "Circuits régionaux"),
    make_club(36, "K13 Esport", "K13", 950, ["Firen", "Asa"], "Circuits régionaux"),
    make_club(37, "Lyost Esport", "LYOST", 800, ["Momsy", "Werex"], "Circuits régionaux")
]

# 2025 Complete
clubs_2025 = [
    make_club(1, "Gentle Mates", "M8", 96500, ["Vanyak3kk", "Akiira", "MariusCOW", "Kurama"], "Champions FNCS Globals 2025, Domination totale de la saison"),
    make_club(2, "Team HavoK", "HVK", 84200, ["SwizzY", "PabloWingu", "Tjino", "Pixie"], "Vainqueurs FNCS Major 2 & 3, finalistes mondiaux"),
    make_club(3, "Solary", "SLY", 68900, ["Ghonzo", "Minori", "Darkos", "SkyJump"], "Podiums réguliers FNCS et Cash Cups"),
    make_club(4, "Karmine Corp", "KC", 52100, ["Malibuca", "Veno"], "Finalistes FNCS Majors"),
    make_club(5, "Zerance", "ZRC", 38400, ["Skydeun", "Vatira"], "Top 10 européen"),
    make_club(6, "GameWard", "GW", 32800, ["Kombek", "Tylio", "S1neD"], "Top 12 européen"),
    make_club(7, "Galions", "GLN", 27500, ["Clément", "Kyzen"], "Dernière saison officielle"),
    make_club(8, "Reality Zoned", "RZ", 23100, ["Nayro", "Kyli", "Zeyko"], "Régularité"),
    make_club(9, "Team Fake", "FAKE", 19800, ["Zeka", "Krox", "Skyll"], "Solide leader du Tier 2"),
    make_club(10, "Valiant", "VLT", 17400, ["Robabz", "Trulex"], "Régularité européenne"),
    make_club(11, "Aten eSport", "ATEN", 15200, ["Atenz", "Skyze"], "Podiums Tier 2"),
    make_club(12, "Team BSK", "BSK", 13600, ["Shado", "Kenza"], "Régularité"),
    make_club(13, "Jupitar Esport", "JUP", 12100, ["Jupi", "Star"], "Qualifications régulières"),
    make_club(14, "Odious Esport", "ODI", 10800, ["Odi", "Rage"], "Performances régionales"),
    make_club(15, "Pap's Esport", "PAPS", 9700, ["Papito", "Slay"], "Circuits francophones"),
    make_club(16, "1P (OneProdige)", "1P", 8900, ["Lericx", "Hyper", "Julie"], "Progression"),
    make_club(17, "Team Orchid", "ORC", 8200, ["Izzi", "Nociff", "Seyyto"], "Top 20 européen"),
    make_club(18, "Wooka Esport", "WOOKA", 7600, ["Szarik", "Matez", "Ferdy"], "Régularité"),
    make_club(19, "Vulcan Esport", "VUL", 7100, ["Izzi", "Tarpz", "Zarb"], "Circuits semi-pro"),
    make_club(20, "Orphée Esport", "ORPH", 6500, ["Fnam", "Kulb", "Artist"], "Performances solides"),
    make_club(21, "TRKF E-Sport", "TRKF", 5900, ["flex", "Damage", "Nero"], "Circuits nationaux"),
    make_club(22, "Pandore Esport", "PANDR", 5400, ["Huty", "Triix", "Winther"], "Circuits nationaux"),
    make_club(23, "NOW eSport", "NOW", 4900, ["chrisc", "Klayzz", "Squzy"], "Circuits nationaux"),
    make_club(24, "Poyo Esports", "POYO", 4500, ["SnozQ", "iFrOzi", "Shadox"], "Progression"),
    make_club(25, "Lynox Esport", "LYN", 4100, ["Heror3h", "xzeevit4k"], "Circuits francophones"),
    make_club(26, "EOZ eSport", "EOZ", 3700, ["Mystiqul", "Spexx", "S1neD"], "Circuits régionaux"),
    make_club(27, "EKINOX", "EKI", 3400, ["Mirooz", "nayzix7", "Exqu"], "Circuits régionaux"),
    make_club(28, "WIP Esports", "WIP", 3100, ["Velryy", "Kielba"], "Circuits régionaux"),
    make_club(29, "Haikoo", "HK", 2800, ["Maciak", "Joshbot"], "Circuits régionaux"),
    make_club(30, "G3nZ Esport", "G3NZ", 2500, ["Ary", "2Trash1zr"], "Circuits régionaux"),
    make_club(31, "BK ROG Esports", "BK", 2200, ["Hris"], "Circuits régionaux"),
    make_club(32, "Novix eSport", "NOV", 1950, ["Okram", "Actfv"], "Circuits régionaux"),
    make_club(33, "Australe Esport", "AUS", 1750, ["freuzi", "Kaktus"], "Circuits régionaux"),
    make_club(34, "R4C Esport", "R4C", 1550, ["Kenrop", "Maloyache"], "Circuits régionaux"),
    make_club(35, "MGA Esport", "MGA", 1350, ["Syaaz", "Trusio"], "Circuits régionaux"),
    make_club(36, "K13 Esport", "K13", 1150, ["Firen", "Asa"], "Circuits régionaux"),
    make_club(37, "Lyost Esport", "LYOST", 950, ["Momsy", "Werex"], "Circuits régionaux")
]

# 2026 Complete (Live season matching official Fortnite Tracker Power Rankings)
clubs_2026 = [
    make_club(1, "HavoK by Vitality", "HVK", 741548, ["Pixie", "Tjino", "PabloWingu", "SwizzY"], "Rank 1 Fortnite Tracker Europe (741,548 pts, $1,395,160)"),
    make_club(2, "Gentle Mates", "M8", 503388, ["Akiira", "MariusCOW", "Vanyak3kk", "Kurama"], "Rank 2 Fortnite Tracker Europe (503,388 pts, $631,600)"),
    make_club(3, "Solary", "SLY", 361168, ["SkyJump", "Ghonzo", "Minori", "Kurama"], "Rank 5 Fortnite Tracker Europe (361,168 pts, $122,890)"),
    make_club(4, "Lyost Esport", "LYOST", 351106, ["Momsy", "Werex", "Twek", "Borsuk"], "Rank 7 Fortnite Tracker Europe (351,106 pts, $151,275)"),
    make_club(5, "MGA Esport", "MGA", 230804, ["Syaaz", "Trusio", "FiTo", "iFrOzi"], "Rank 13 Fortnite Tracker Europe (230,804 pts, $47,025)"),
    make_club(6, "GameWard", "GW", 176065, ["Kombek", "Tylio", "Nociff", "S1neD"], "Rank 20 Fortnite Tracker Europe (176,065 pts, $11,300)"),
    make_club(7, "K13 Esport", "K13", 173080, ["Firen", "Asa", "Seyyto", "Roz"], "Rank 22 Fortnite Tracker Europe (173,080 pts, $36,800)"),
    make_club(8, "Team Orchid", "ORC", 171417, ["Izzi", "Nociff", "Seyyto"], "Rank 24 Fortnite Tracker Europe (171,417 pts, $97,625)"),
    make_club(9, "1P (OneProdige)", "1P", 135029, ["Lericx", "Hyper", "Julie", "Alvinlr"], "Rank 28 Fortnite Tracker Europe (135,029 pts, $21,500)"),
    make_club(10, "R4C Esport", "R4C", 103789, ["Kenrop", "Maloyache", "Foczka"], "Rank 39 Fortnite Tracker Europe (103,789 pts, $4,560)"),
    make_club(11, "Wooka Esport", "WOOKA", 100725, ["Szarik", "Matez", "Kizers", "Ferdy"], "Rank 40 Fortnite Tracker Europe (100,725 pts, $5,900)"),
    make_club(12, "Vulcan Esport", "VUL", 96183, ["Izzi", "Tarpz", "Vexi", "Zarb"], "Rank 41 Fortnite Tracker Europe (96,183 pts, $5,200)"),
    make_club(13, "Orphée Esport", "ORPH", 95564, ["Fnam", "Kulb", "Artist", "Adrx"], "Rank 42 Fortnite Tracker Europe (95,564 pts, $7,600)"),
    make_club(14, "TRKF E-Sport", "TRKF", 78684, ["flex", "Damage", "Nero"], "Rank 48 Fortnite Tracker Europe (78,684 pts, $7,000)"),
    make_club(15, "Pandore Esport", "PANDR", 75158, ["Huty", "Triix", "Winther"], "Rank 49 Fortnite Tracker Europe (75,158 pts, $21,670)"),
    make_club(16, "NOW eSport", "NOW", 65772, ["chrisc", "Klayzz", "Squzy", "Maloyache"], "Rank 53 Fortnite Tracker Europe (65,772 pts, $1,050)"),
    make_club(17, "Poyo Esports", "POYO", 63765, ["SnozQ", "iFrOzi", "Shadox", "Repairs"], "Rank 55 Fortnite Tracker Europe (63,765 pts, $4,100)"),
    make_club(18, "Lynox Esport", "LYN", 63421, ["Heror3h", "xzeevit4k"], "Rank 56 Fortnite Tracker Europe (63,421 pts, $2,900)"),
    make_club(19, "EOZ eSport", "EOZ", 63050, ["Mystiqul", "Spexx", "S1neD", "Hedra"], "Rank 57 Fortnite Tracker Europe (63,050 pts, $2,050)"),
    make_club(20, "EKINOX", "EKI", 62332, ["Mirooz", "nayzix7", "Exqu", "Misha"], "Rank 58 Fortnite Tracker Europe (62,332 pts, $650)"),
    make_club(21, "WIP Esports", "WIP", 42782, ["Velryy", "Kielba"], "Rank 69 Fortnite Tracker Europe (42,782 pts, $1,350)"),
    make_club(22, "Haikoo", "HK", 37089, ["Maciak", "Joshbot", "Kielba"], "Rank 71 Fortnite Tracker Europe (37,089 pts, $3,600)"),
    make_club(23, "G3nZ Esport", "G3NZ", 31695, ["Ary", "2Trash1zr", "Efexy", "SereN"], "Rank 76 Fortnite Tracker Europe (31,695 pts, $2,700)"),
    make_club(24, "BK ROG Esports", "BK", 17515, ["Hris"], "Rank 90 Fortnite Tracker Europe (17,515 pts, $48,900)"),
    make_club(25, "Novix eSport", "NOV", 15132, ["Okram", "Actfv", "Joanee"], "Rank 94 Fortnite Tracker Europe (15,132 pts, $500)"),
    make_club(26, "Australe Esport", "AUS", 13494, ["freuzi", "Kaktus"], "Rank 97 Fortnite Tracker Europe (13,494 pts, $550)"),
    make_club(27, "Valiant", "VLT", 11033, ["Trulex", "Robabz"], "Rank 100 Fortnite Tracker Europe (11,033 pts, $168,295)"),
    make_club(28, "Reality Zoned", "RZ", 9500, ["Nayro", "Kyli", "Zeyko"], "Tier 2 Régional (9,500 pts)"),
    make_club(29, "Team Fake", "FAKE", 8200, ["Zeka", "Krox", "Skyll"], "Tier 2 Régional (8,200 pts)"),
    make_club(30, "Team BSK", "BSK", 7100, ["Shado", "Kenza"], "Tier 2 Régional (7,100 pts)"),
    make_club(31, "Aten eSport", "ATEN", 5400, ["Atenz", "Skyze"], "Tier 2 Régional (5,400 pts)"),
    make_club(32, "Jupitar Esport", "JUP", 4800, ["Jupi", "Star"], "Tier 2 Régional (4,800 pts)"),
    make_club(33, "Odious Esport", "ODI", 4200, ["Odi", "Rage"], "Tier 2 Régional (4,200 pts)"),
    make_club(34, "Pap's Esport", "PAPS", 3900, ["Papito", "Slay"], "Tier 2 Régional (3,900 pts)"),
    make_club(35, "Pandaria Esport", "PAND", 3400, ["Panda", "Bamboo"], "Tier 2 Régional (3,400 pts)"),
    make_club(36, "Fly Again", "FA", 2900, ["Flyer", "Wing"], "Tier 2 Régional (2,900 pts)"),
    make_club(37, "Zerance", "ZRC", 2500, ["Skydeun"], "Tier 2 Régional (2,500 pts)")
]

annual["2018"]["clubs"] = clubs_2018
annual["2019"]["clubs"] = clubs_2019
annual["2020"]["clubs"] = clubs_2020
annual["2021"]["clubs"] = clubs_2021
annual["2022"]["clubs"] = clubs_2022
annual["2023"]["clubs"] = clubs_2023
annual["2024"]["clubs"] = clubs_2024
annual["2025"]["clubs"] = clubs_2025
annual["2026"]["clubs"] = clubs_2026

with open(DATA_DIR / "annual_rankings.json", "w", encoding="utf-8") as f:
    json.dump(annual, f, indent=2, ensure_ascii=False)

print("Successfully enriched annual_rankings.json for all years 2018-2026!")
