import json
import re
from pathlib import Path

BASE_DIR = Path("C:/Users/marti/Documents/MARTIN/LFF")
DASH_FILE = BASE_DIR / "LFF Dashboard/index.html"
CLUBS_FILE = BASE_DIR / "LFF Data/clubs.json"
ANNUAL_FILE = BASE_DIR / "LFF Data/annual_rankings.json"
ROSTERS_FILE = BASE_DIR / "LFF Data/rosters.json"

def main():
    with open(DASH_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    with open(CLUBS_FILE, "r", encoding="utf-8") as f:
        clubs = json.load(f)

    with open(ANNUAL_FILE, "r", encoding="utf-8") as f:
        annual = json.load(f)

    with open(ROSTERS_FILE, "r", encoding="utf-8") as f:
        rosters = json.load(f)

    clubs_dict = {c['id']: c for c in clubs}

    # 1. Build clean LIVE_DATA (active players ONLY, no former players)
    live_clubs = []
    for c_ann in annual.get('2026', {}).get('clubs', []):
        cid = c_ann['id']
        c_meta = clubs_dict.get(cid, {})
        all_players = rosters.get('active_rosters', {}).get(cid, [])
        # Strict filter: ONLY active players
        active_players = [p for p in all_players if not p.get('is_former')]
        live_pr = sum(p.get('pr', 0) for p in active_players)

        live_club = {
            "id": cid,
            "name": c_meta.get('name', c_ann.get('name')),
            "tag": c_meta.get('tag', c_ann.get('tag')),
            "logo": c_meta.get('logo_path', f"LFF Logos/{cid}.png"),
            "tracker_url": c_meta.get('tracker_url', f"https://fortnitetracker.com/esports/organization/{cid}"),
            "socials": c_meta.get('socials', {}),
            "livePr": live_pr,
            "earnings": c_meta.get('earnings_usd', 0),
            "players": active_players,
            "details": f"Roster actif sous contrat ({len(active_players)} joueur{'s' if len(active_players) > 1 else ''})",
            "trend": "0"
        }
        live_clubs.append(live_club)

    # Sort LIVE_DATA by livePr descending
    live_clubs.sort(key=lambda x: x['livePr'], reverse=True)
    for i, c in enumerate(live_clubs):
        c['rank'] = i + 1

    live_json = json.dumps(live_clubs, ensure_ascii=False, indent=2)

    # Replace LIVE_DATA in index.html
    live_start = html.find('const LIVE_DATA = [')
    live_end = html.find('];', live_start)
    if live_start != -1 and live_end != -1:
        html = html[:live_start] + f"const LIVE_DATA = {live_json}" + html[live_end:]
        print("[+] Successfully replaced LIVE_DATA with active-only rosters and recomputed live PR")
    else:
        print("[!] Warning: LIVE_DATA block not found")

    # 2. Update ANNUAL_DATA in index.html with exact FT points and clean tiers
    annual_start = html.find('const ANNUAL_DATA = {')
    annual_end = html.find('};\n\n    const LOGO_MAP', annual_start)
    if annual_start != -1 and annual_end != -1:
        annual_json = json.dumps(annual, ensure_ascii=False, indent=2)
        html = html[:annual_start] + f"const ANNUAL_DATA = {annual_json}" + html[annual_end:]
        print("[+] Successfully replaced ANNUAL_DATA with exact FT points in 2026")
    else:
        print("[!] Warning: ANNUAL_DATA block not found")

    # 3. Rename navigation buttons
    html = html.replace("switchNavTab('tab-rankings')\">📊 Classements LFF</button>", "switchNavTab('tab-rankings')\">📊 Classement</button>")
    html = html.replace("switchNavTab('tab-palmares')\">🏆 Palmarès Historique</button>", "switchNavTab('tab-palmares')\">🏆 Palmarès</button>")
    html = html.replace("switchNavTab('tab-mercato')\">🔄 Mercato & Transferts</button>", "switchNavTab('tab-mercato')\">🔄 Transferts</button>")
    html = html.replace("switchNavTab('tab-clubs')\">🛡️ Tous les Clubs</button>", "switchNavTab('tab-clubs')\">🛡️ Clubs</button>")
    html = html.replace("switchNavTab('tab-reglement')\">⚖️ Règlement & PR</button>", "switchNavTab('tab-reglement')\">⚖️ Règlement</button>")
    print("[+] Renamed all navigation buttons")

    # 4. In tab-clubs: remove (ÉLITE & CHALLENGER) and update title
    html = html.replace("<h3>🛡️ ANNUAIRE DES CLUBS FRANÇAIS (ÉLITE & CHALLENGER)</h3>", "<h3>🛡️ CLUBS FRANÇAIS</h3>")
    html = html.replace("L'ensemble des structures esportives françaises engagées sur Fortnite, de l'Élite aux Challengers.", "L'ensemble des structures esportives françaises engagées sur Fortnite.")
    print("[+] Updated Clubs section title and removed Élite & Challenger mentions")

    # 5. In renderClubs(): Remove Tracker button, Liquipedia button, and tier badge
    old_render_clubs_card = """          <div style="display: flex; align-items: center; gap: 1rem;">
            ${logoHtml}
            <div>
              <h4 style="color: white; font-size: 1.1rem;">
                <a href="${trackerUrl}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" title="Page Fortnite Tracker de ${c.name}">
                  ${c.name}
                </a>
                <span class="club-tag">${c.tag}</span>
              </h4>
              <span class="badge-pill ${c.tier && c.tier.includes('Tier 1') ? 'gold' : ''}" style="margin-top: 4px;">${c.tier}</span>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.4;">${c.desc}</p>
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; margin-top: auto; padding-top: 0.5rem;">
            <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;">
              <a href="${trackerUrl}" target="_blank" rel="noopener noreferrer" class="club-x-btn" style="background: rgba(59, 130, 246, 0.2); border-color: rgba(96, 165, 250, 0.4);" title="Page Fortnite Tracker de ${c.name}">
                🎯 Tracker
              </a>
              ${c.liquipediaUrl ? `<a href="${c.liquipediaUrl}" target="_blank" rel="noopener noreferrer" class="club-x-btn" style="background: rgba(147, 51, 234, 0.2); border-color: rgba(168, 85, 247, 0.4);" title="Fiche Liquipedia">📖 Liquipedia</a>` : ''}
            </div>
            ${buildClubSocialsHtml(clubObj)}
          </div>"""

    new_render_clubs_card = """          <div style="display: flex; align-items: center; gap: 1rem;">
            ${logoHtml}
            <div>
              <h4 style="color: white; font-size: 1.1rem;">
                <a href="${trackerUrl}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" title="Page Fortnite Tracker de ${c.name}">
                  ${c.name}
                </a>
                <span class="club-tag">${c.tag}</span>
              </h4>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.4;">${c.desc}</p>
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: flex-end; gap: 6px; margin-top: auto; padding-top: 0.5rem;">
            ${buildClubSocialsHtml(clubObj)}
          </div>"""

    if old_render_clubs_card in html:
        html = html.replace(old_render_clubs_card, new_render_clubs_card)
        print("[+] Updated renderClubs card: removed Tracker and Liquipedia buttons, removed Tier badge")
    else:
        print("[!] Warning: old_render_clubs_card not found exactly")

    # 6. Update renderLiveTable() and renderAnnualTable() roster legend adaptation
    old_legend = """      <div class="roster-legend-box" style="margin-top: 1rem; font-size: 0.82rem; color: #94a3b8; display: flex; gap: 1.5rem; align-items: center; justify-content: flex-end; padding: 0.5rem 1rem; background: rgba(0,0,0,0.25); border-radius: 8px;">
        <span style="display: inline-flex; align-items: center; gap: 6px;">
          <span class="player-tag active-player" style="font-size: 0.72rem; padding: 2px 6px;">Joueur</span>
          <span>Joueur actif sous contrat</span>
        </span>
        <span style="display: inline-flex; align-items: center; gap: 6px;">
          <span class="player-tag former-player" style="font-size: 0.72rem; padding: 2px 6px;">Joueur*</span>
          <span>Ancien joueur ayant rapporté des points (Classement Annuel)</span>
        </span>
      </div>"""

    new_legend = """      <div id="roster-legend" class="roster-legend-box" style="margin-top: 1rem; font-size: 0.82rem; color: #94a3b8; display: flex; gap: 1.5rem; align-items: center; justify-content: flex-end; padding: 0.5rem 1rem; background: rgba(0,0,0,0.25); border-radius: 8px;">
        <span style="display: inline-flex; align-items: center; gap: 6px;">
          <span class="player-tag active-player" style="font-size: 0.72rem; padding: 2px 6px;">Joueur</span>
          <span>Joueur actif sous contrat</span>
        </span>
        <span style="display: inline-flex; align-items: center; gap: 6px;">
          <span class="player-tag former-player" style="font-size: 0.72rem; padding: 2px 6px;">Joueur*</span>
          <span>Ancien joueur ayant rapporté des points (Classement Annuel uniquement)</span>
        </span>
      </div>"""

    if old_legend in html:
        html = html.replace(old_legend, new_legend)
        print("[+] Updated roster legend box")

    # In renderLiveTable(): ensure only active players are rendered
    old_live_render_players = """        let playersHtml = '';
        if (Array.isArray(c.players)) {
          playersHtml = c.players.map(buildPlayerTagHtml).join(' ');
        } else if (typeof c.players === 'string') {
          playersHtml = c.players.split(',').map(buildPlayerTagHtml).join(' ');
        }"""

    new_live_render_players = """        let activePlayers = Array.isArray(c.players) 
          ? c.players.filter(p => !p.is_former && !(typeof p === 'string' && p.includes('*')))
          : [];
        let playersHtml = activePlayers.map(buildPlayerTagHtml).join(' ');"""

    if old_live_render_players in html:
        html = html.replace(old_live_render_players, new_live_render_players)
        print("[+] Updated renderLiveTable to strictly render active players only")

    # 7. Rewrite tab-reglement with complete, crystal-clear explanation
    reglement_start = html.find('<div id="tab-reglement" class="tab-content">')
    reglement_end = html.find('</div>\n\n  </main>', reglement_start)

    new_reglement_content = """<div id="tab-reglement" class="tab-content">
      <div class="ranking-table-card" style="padding: 2.5rem; line-height: 1.75;">
        <h2 style="font-family: 'Teko', sans-serif; font-size: 2.4rem; color: var(--purple-accent); margin-bottom: 0.5rem; text-transform: uppercase;">
          RÈGLEMENT OFFICIEL & COMPTABILISATION DES POINTS DE LA LFF
        </h2>
        <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 2rem;">
          Le cadre réglementaire officiel régissant l'attribution des points, le fonctionnement des classements et l'intégrité de la Ligue Française de Fortnite.
        </p>

        <!-- SECTION 1 : FONCTIONNEMENT DES DEUX CLASSEMENTS -->
        <div style="background: rgba(147, 51, 234, 0.08); border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem;">
          <h3 style="color: white; font-size: 1.3rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 8px;">
            <span>⚖️</span> 1. Deux Classements Complémentaires : Annuel vs Live
          </h3>
          <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 1.25rem;">
            La LFF propose deux lectures distinctes et rigoureuses des performances esportives des clubs français :
          </p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
            <div style="background: rgba(0, 0, 0, 0.35); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 1.25rem;">
              <h4 style="color: #f59e0b; font-size: 1.1rem; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 6px;">
                <span>🏆</span> Classement Annuel (Championship)
              </h4>
              <p style="color: #e2e8f0; font-size: 0.9rem; margin-bottom: 0.75rem;">
                <strong>Objet :</strong> Couronner le <em>Club Champion de France de Fortnite</em> à l'issue de chaque année civile (1er janvier au 31 décembre).
              </p>
              <ul style="color: #cbd5e1; font-size: 0.88rem; padding-left: 1.2rem; display: flex; flex-direction: column; gap: 6px;">
                <li><strong>Comptabilisation des points :</strong> Cumul officiel des points de Power Ranking (PR) de l'organisation sur Fortnite Tracker Europe acquis lors des tournois officiels (FNCS, Majors, Cash Cups, Victory Cups).</li>
                <li><strong>Effectif retenu :</strong> Les <strong>4 meilleurs contributeurs PR</strong> de l'organisation au cours de la saison.</li>
                <li><strong>Anciens joueurs (<span style="color: #f59e0b;">*</span>) :</strong> En vertu de la règle de conservation des points acquis, un joueur qui a quitté le club en cours d'année conserve l'intégralité des points marqués pour le club pendant son contrat. Il est identifié par un astérisque (<code>*</code>) et un badge en pointillés.</li>
              </ul>
            </div>

            <div style="background: rgba(0, 0, 0, 0.35); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 8px; padding: 1.25rem;">
              <h4 style="color: #38bdf8; font-size: 1.1rem; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 6px;">
                <span>⚡</span> Classement Live (Power Index)
              </h4>
              <p style="color: #e2e8f0; font-size: 0.9rem; margin-bottom: 0.75rem;">
                <strong>Objet :</strong> Mesurer la <em>force de frappe instantanée</em> de chaque club en temps réel aujourd'hui.
              </p>
              <ul style="color: #cbd5e1; font-size: 0.88rem; padding-left: 1.2rem; display: flex; flex-direction: column; gap: 6px;">
                <li><strong>Comptabilisation des points :</strong> Somme directe du Power Ranking actuel des <strong>joueurs actifs sous contrat uniquement</strong>.</li>
                <li><strong>Roster 100% Actif :</strong> Seuls les joueurs portant les couleurs du club à l'instant T sont affichés.</li>
                <li><strong>Zéro ancien joueur :</strong> Dès qu'un joueur quitte la structure (LFT, Free Agent, transfert), il disparaît instantanément du Classement Live du club. Aucun astérisque n'apparaît dans ce classement.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- SECTION 2 : RÈGLE NO BUYING PR -->
        <h3 style="color: white; margin-top: 1.5rem; margin-bottom: 0.5rem;">2. Règle d'or « No Buying PR » (Anti-Mercenariat)</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem;">
          À l'image du règlement officiel de Fandom Esports et du championnat des constructeurs en Formule 1, un club n'engrange de points de Power Ranking que lors des compétitions disputées par ses joueurs <strong>pendant leur période contractuelle effective</strong>.
          Si une structure recrute un joueur disposant déjà de 50 000 points PR, le club ne bénéficie pas de ce total passé. Le joueur commence à marquer pour le club à partir de sa date officielle de signature.
        </p>

        <!-- SECTION 3 : CONSERVATION DES POINTS ACQUIS -->
        <h3 style="color: white; margin-top: 1.5rem; margin-bottom: 0.5rem;">3. Conservation des Points Acquis par les Anciens Joueurs</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem;">
          Si un joueur quitte une structure en cours d'année, l'ensemble des points qu'il a rapportés pendant sa période sous contrat reste définitivement crédité au club pour le classement annuel de la saison en cours. Ce principe fondamental empêche toute perte rétroactive et récompense l'investissement sportif de la structure.
        </p>

        <!-- SECTION 4 : RÈGLE DES TOP 4 JOUEURS -->
        <h3 style="color: white; margin-top: 1.5rem; margin-bottom: 0.5rem;">4. Règle des Top 4 Joueurs par Organisation</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem;">
          Pour assurer une équité stricte entre les structures et éviter qu'un club ne recrute un nombre démesuré de joueurs pour gonfler artificiellement son total, seuls les points des <strong>4 joueurs les plus performants</strong> au sein de l'organisation sont comptabilisés dans le total annuel officiel de Fortnite Tracker.
        </p>

        <!-- SECTION 5 : ÉLIGIBILITÉ INTERNATIONALE -->
        <h3 style="color: white; margin-top: 1.5rem; margin-bottom: 0.5rem;">5. Éligibilité 100% Ouverte à l'International</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem;">
          Les joueurs sous contrat avec un club français <strong>n'ont aucune obligation d'être de nationalité française</strong>. Les athlètes internationaux (ex: SwizzY, Pixie, Vanyak3kk, Malibuca, Merstach, Veno) marquent 100% de leurs points pour leur club français, avec les mêmes barèmes qu'un joueur tricolore.
        </p>

        <!-- SECTION 6 : PROTOCOLE D'INTÉGRITÉ ANTI-ERREUR -->
        <h3 style="color: white; margin-top: 1.5rem; margin-bottom: 0.5rem;">6. Protocole de Veille & d'Intégrité Anti-Erreur Multi-Plateformes</h3>
        <p style="color: #cbd5e1; font-size: 0.95rem; margin-bottom: 0.75rem;">
          Pour éliminer toute hallucination ou attribution erronée, l'affectation de chaque joueur et le calcul du classement s'appuient sur un croisement systématique de 4 sources complémentaires (primaires et secondaires) :
        </p>
        <ul style="color: #cbd5e1; font-size: 0.92rem; padding-left: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
          <li>
            <strong>1. Comptes & Biographies X (Twitter) des Joueurs et des Clubs (Sources Primaires) :</strong> Tout joueur actif doit expressément mentionner le club (<span style="color: #c084fc;">@Club</span>) dans sa biographie officielle (ex: @Seekkfn mentionnant @HvKGGs). Tout joueur avec mention <em>« was pro »</em>, <em>« LFT »</em> ou <em>« Free Agent »</em> est immédiatement retiré de l'effectif actif (ex: Snayzy, Clément, Kyzen, Rad3on, Nxthan).
          </li>
          <li>
            <strong>2. Décideurs / Staff des Clubs & Médias d'Actualité Esport :</strong> Suivi prioritaire des déclarations et confirmations directes des dirigeants et managers de sections, notamment <a href="https://x.com/Revenja_" target="_blank" style="color: #38bdf8; text-decoration: none;"><strong>@Revenja_</strong></a> (<strong>Head of Fortnite de Solary</strong>) dont les annonces de recrues et prolongations font autorité absolue, complété par la veille continue de <a href="https://x.com/FortniteFraActu" target="_blank" style="color: #38bdf8; text-decoration: none;">@FortniteFraActu</a>.
          </li>
          <li>
            <strong>3. Wikis Collaboratifs & Références Historiques (Liquipedia & Fandom Esports) :</strong> Consultation conjointe de <a href="https://liquipedia.net/fortnite/Category:French_Teams" target="_blank" style="color: #c084fc; text-decoration: none;">Liquipedia Fortnite</a> et de la <a href="https://fortnite-esports.fandom.com/wiki/Power_Rankings_-_Teams/PC/Europe" target="_blank" style="color: #c084fc; text-decoration: none;">Fortnite Esports Wiki Fandom (Team PR Europe)</a>. <em>Vigilance intégrité :</em> ces bases communautaires accusant parfois des retards d'actualisation ou des imprécisions de roster, elles sont systématiquement arbitrées par les sources primaires (bios X et annonces officielles).
          </li>
          <li>
            <strong>4. Fortnite Tracker Power Ranking (PR) :</strong> Synchronisation des points officiels de tournois (FNCS, Cash Cups, Victory Cups) selon la période contractuelle exacte, corrigée des éventuelles mauvaises attributions de Tracker via la règle d'or <em>« No Buying PR »</em>.
          </li>
        </ul>
      </div>
    </div>"""

    if reglement_start != -1 and reglement_end != -1:
        html = html[:reglement_start] + new_reglement_content + html[reglement_end + len('</div>\n\n  </main>'):]
        print("[+] Replaced tab-reglement with complete explanation of points and rankings")
    else:
        print("[!] Warning: tab-reglement block not found")

    # 8. Remove all remaining mentions of "Tier" across index.html
    html = re.sub(r'\s*"tier":\s*"[^"]*",?', '', html)
    html = html.replace('Révélation Tier 2 de l\'année', 'Révélation de l\'année')
    html = html.replace('Podiums Tier 2', 'Podiums Nationaux')
    html = html.replace('Solide leader du Tier 2', 'Régularité au sommet')
    html = re.sub(r'Tier 2 Régional \(([^)]+)\)', r'Circuit Régional (\1)', html)
    html = re.sub(r'<span class="badge-pill [^"]*">\s*Tier\s*\d\s*</span>', '', html)

    # 9. In allClubs embedded in index.html (renderClubs), remove "tier" key
    html = re.sub(r'"tier":\s*"[^"]*",\s*', '', html)

    with open(DASH_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("[+] Successfully updated LFF Dashboard/index.html")

if __name__ == '__main__':
    main()
