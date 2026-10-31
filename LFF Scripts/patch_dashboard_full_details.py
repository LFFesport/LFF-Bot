import json
import re

def main():
    with open('LFF Dashboard/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('LFF Data/clubs.json', 'r', encoding='utf-8') as f:
        clubs = json.load(f)

    clubs_meta = {}
    for c in clubs:
        clubs_meta[c['id']] = {
            'tracker_url': c.get('tracker_url'),
            'socials': c.get('socials', {})
        }

    meta_json = json.dumps(clubs_meta, ensure_ascii=False, indent=2)

    # 1. Update renderPalmares winnerRosterHtml
    old_winner_roster = """        const winnerRosterHtml = winner.roster.map(pName => {
          const cleanName = pName.replace(/\\s*\\([^)]*\\)/g, '').trim();
          const pUrl = PLAYER_X_MAP[cleanName] || `https://x.com/search?q=${encodeURIComponent(cleanName)}+fortnite`;
          return `<a href="${pUrl}" target="_blank" rel="noopener noreferrer" class="player-tag" style="font-size: 0.78rem;" title="Compte X de ${cleanName}">
            <strong>${cleanName}</strong> <span class="x-icon">𝕏</span>
          </a>`;
        }).join(' ');"""

    new_winner_roster = """        const winnerRosterHtml = winner.roster.map(buildPlayerTagHtml).join(' ');"""

    if old_winner_roster in html:
        html = html.replace(old_winner_roster, new_winner_roster)
        print('Updated winnerRosterHtml in renderPalmares')
    else:
        print('Warning: old_winner_roster not found exactly')

    # 2. Update renderTransfers player link
    old_transfer_player = """              <h4 style="color: white; font-size: 1.05rem;">
                <a href="${t.playerXUrl || 'https://x.com'}" target="_blank" rel="noopener noreferrer" style="color: white; text-decoration: none;" title="Compte X du joueur">
                  ${t.player} <span class="x-icon">𝕏</span>
                </a>
              </h4>"""

    new_transfer_player = """              <h4 style="color: white; font-size: 1.05rem;">
                <a href="https://fortnitetracker.com/profile/all/${encodeURIComponent(t.player)}" target="_blank" rel="noopener noreferrer" class="player-tracker-link" style="color: white; text-decoration: none;" title="Statistiques Fortnite Tracker de ${t.player}">
                  <strong>${t.player}</strong>
                </a>
                ${t.playerXUrl ? `<a href="${t.playerXUrl}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" style="display: inline-flex; vertical-align: middle; margin-left: 4px;" title="Compte X de ${t.player}">𝕏</a>` : ''}
              </h4>"""

    if old_transfer_player in html:
        html = html.replace(old_transfer_player, new_transfer_player)
        print('Updated transfer player in renderTransfers')
    else:
        print('Warning: old_transfer_player not found exactly')

    # 3. Update renderClubs
    old_render_clubs_loop = """      allClubs.forEach(c => {
        const logoPath = LOGO_MAP[c.id];
        const logoHtml = logoPath 
          ? `<img src="${logoPath}" class="club-logo" alt="${c.name}">`
          : `<div class="club-logo-placeholder">${c.tag}</div>`;

        const card = document.createElement('div');
        card.className = "club-card";
        card.innerHTML = `
          <div style="display: flex; align-items: center; gap: 1rem;">
            ${logoHtml}
            <div>
              <h4 style="color: white; font-size: 1.1rem;">${c.name} <span class="club-tag">${c.tag}</span></h4>
              <span class="badge-pill ${c.tier.includes('Tier 1') ? 'gold' : ''}" style="margin-top: 4px;">${c.tier}</span>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.4;">${c.desc}</p>
          <div style="display: flex; gap: 8px; margin-top: auto; padding-top: 0.5rem;">
            <a href="${c.xUrl}" target="_blank" rel="noopener noreferrer" class="club-x-btn" title="Compte X officiel">
              <span>𝕏</span> ${c.xHandle || 'Compte X'}
            </a>
            ${c.liquipediaUrl ? `<a href="${c.liquipediaUrl}" target="_blank" rel="noopener noreferrer" class="club-x-btn" style="background: rgba(147, 51, 234, 0.2); border-color: rgba(168, 85, 247, 0.4);" title="Fiche Liquipedia">📖 Liquipedia</a>` : ''}
          </div>
        `;
        container.appendChild(card);
      });"""

    new_render_clubs_loop = f"""      const CLUBS_META = {meta_json};

      allClubs.forEach(c => {{
        const logoPath = LOGO_MAP[c.id];
        const logoHtml = logoPath 
          ? `<img src="${{logoPath}}" class="club-logo" alt="${{c.name}}">`
          : `<div class="club-logo-placeholder">${{c.tag}}</div>`;

        const meta = CLUBS_META[c.id] || {{}};
        const trackerUrl = c.tracker_url || meta.tracker_url || `https://fortnitetracker.com/esports/organization/${{c.id}}`;
        const socials = c.socials || meta.socials || (c.xUrl ? {{ x: c.xUrl }} : {{}});
        const clubObj = {{ ...c, tracker_url: trackerUrl, socials: socials }};

        const card = document.createElement('div');
        card.className = "club-card";
        card.innerHTML = `
          <div style="display: flex; align-items: center; gap: 1rem;">
            ${{logoHtml}}
            <div>
              <h4 style="color: white; font-size: 1.1rem;">
                <a href="${{trackerUrl}}" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" title="Page Fortnite Tracker de ${{c.name}}">
                  ${{c.name}}
                </a>
                <span class="club-tag">${{c.tag}}</span>
              </h4>
              <span class="badge-pill ${{c.tier && c.tier.includes('Tier 1') ? 'gold' : ''}}" style="margin-top: 4px;">${{c.tier}}</span>
            </div>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-dim); line-height: 1.4;">${{c.desc}}</p>
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; margin-top: auto; padding-top: 0.5rem;">
            <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;">
              <a href="${{trackerUrl}}" target="_blank" rel="noopener noreferrer" class="club-x-btn" style="background: rgba(59, 130, 246, 0.2); border-color: rgba(96, 165, 250, 0.4);" title="Page Fortnite Tracker de ${{c.name}}">
                🎯 Tracker
              </a>
              ${{c.liquipediaUrl ? `<a href="${{c.liquipediaUrl}}" target="_blank" rel="noopener noreferrer" class="club-x-btn" style="background: rgba(147, 51, 234, 0.2); border-color: rgba(168, 85, 247, 0.4);" title="Fiche Liquipedia">📖 Liquipedia</a>` : ''}}
            </div>
            ${{buildClubSocialsHtml(clubObj)}}
          </div>
        `;
        container.appendChild(card);
      }});"""

    if old_render_clubs_loop in html:
        html = html.replace(old_render_clubs_loop, new_render_clubs_loop)
        print('Updated renderClubs loop')
    else:
        print('Warning: old_render_clubs_loop not found exactly')

    with open('LFF Dashboard/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Dashboard index.html written successfully!')

if __name__ == '__main__':
    main()
