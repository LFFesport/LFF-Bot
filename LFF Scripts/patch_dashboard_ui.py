import re

with open('LFF Dashboard/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. New CSS styles
new_css = """
    /* SOCIAL PILLS & TRACKER LINKS */
    .social-pills-group {
      display: inline-flex;
      align-items: center;
      gap: 3px;
      margin-left: 5px;
      vertical-align: middle;
    }

    .social-pill {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.68rem;
      font-weight: 700;
      border-radius: 4px;
      padding: 1px 4px;
      text-decoration: none;
      line-height: 1.1;
      transition: all 0.15s ease;
      vertical-align: middle;
    }

    .x-pill {
      background: rgba(255, 255, 255, 0.12);
      color: #e2e8f0;
    }
    .x-pill:hover {
      background: #000;
      color: #38bdf8;
      transform: scale(1.15);
    }

    .twitch-pill {
      background: rgba(145, 70, 255, 0.22);
      color: #c084fc;
    }
    .twitch-pill:hover {
      background: #9146FF;
      color: #ffffff;
      transform: scale(1.15);
    }

    .youtube-pill {
      background: rgba(239, 68, 68, 0.22);
      color: #fca5a5;
    }
    .youtube-pill:hover {
      background: #ef4444;
      color: #ffffff;
      transform: scale(1.15);
    }

    .tiktok-pill {
      background: rgba(0, 242, 234, 0.2);
      color: #38bdf8;
    }
    .tiktok-pill:hover {
      background: #010101;
      color: #00f2fe;
      border: 1px solid #ff0050;
      transform: scale(1.15);
    }

    .insta-pill {
      background: rgba(236, 72, 153, 0.22);
      color: #f472b6;
    }
    .insta-pill:hover {
      background: #ec4899;
      color: #ffffff;
      transform: scale(1.15);
    }

    .discord-pill {
      background: rgba(99, 102, 241, 0.22);
      color: #a5b4fc;
    }
    .discord-pill:hover {
      background: #6366f1;
      color: #ffffff;
      transform: scale(1.15);
    }

    .player-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.80rem;
      transition: all 0.15s ease;
      white-space: nowrap;
    }

    .player-tag.active-player {
      background: rgba(147, 51, 234, 0.15);
      border: 1px solid rgba(168, 85, 247, 0.4);
      color: #f1f5f9;
    }
    .player-tag.active-player:hover {
      background: rgba(147, 51, 234, 0.35);
      border-color: #c084fc;
    }

    .player-tag.former-player {
      background: rgba(255, 255, 255, 0.04);
      border: 1px dashed rgba(255, 255, 255, 0.25);
      color: #94a3b8;
      opacity: 0.88;
    }
    .player-tag.former-player:hover {
      opacity: 1;
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.45);
      color: #f1f5f9;
    }

    .player-tracker-link {
      text-decoration: none;
      color: inherit;
      transition: color 0.15s ease;
    }
    .player-tracker-link:hover {
      color: #38bdf8;
      text-decoration: underline;
    }

    .club-cell-link {
      text-decoration: none;
      color: inherit;
      display: flex;
      align-items: center;
      gap: 0.85rem;
      transition: transform 0.15s ease;
    }
    .club-cell-link:hover .club-name {
      color: #38bdf8;
    }

    .club-social-pills {
      display: flex;
      gap: 4px;
      margin-top: 4px;
      flex-wrap: wrap;
    }

    .roster-legend-box {
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
      padding: 10px 18px;
      margin-top: 14px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-light);
      border-radius: 8px;
      font-size: 0.82rem;
      color: #94a3b8;
    }
    .legend-title {
      font-weight: 700;
      color: #cbd5e1;
    }
    .status-indicator.active-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      margin-right: 4px;
    }
    .status-indicator.former-dot {
      display: inline-block;
      font-weight: 800;
      color: #f59e0b;
      margin-right: 4px;
    }
"""

if "/* SOCIAL PILLS & TRACKER LINKS */" not in html:
    html = html.replace("</style>", new_css + "\n  </style>")

# 2. Add legend box after </table>
legend_html = """        <div class="roster-legend-box">
          <span class="legend-title">Légende Effectif Tracker :</span>
          <span class="legend-item"><span class="status-indicator active-dot"></span> <strong>Actif</strong> : Joueur sous contrat actif</span>
          <span class="legend-item"><span class="status-indicator former-dot">*</span> <strong>* Ancien</strong> : Joueur ayant rapporté des points PR au club mais ne faisant plus partie de l'équipe</span>
        </div>"""

if '<div class="roster-legend-box">' not in html:
    html = html.replace("</table>\n      </div>", "</table>\n      </div>\n" + legend_html)

# 3. New renderAnnualTable & renderLiveTable implementations
new_render_functions = """    // Construction HTML d'un tag joueur avec lien Tracker et pastilles de réseaux sociaux personnels
    function buildPlayerTagHtml(p) {
      if (!p) return '';
      
      let rawName = '';
      let isFormer = false;
      let country = '🌍';
      let trackerUrl = '';
      let socials = {};
      let pr = 0;

      if (typeof p === 'string') {
        rawName = p.replace(/\\*/g, '').trim();
        isFormer = p.includes('*');
        trackerUrl = `https://fortnitetracker.com/profile/all/${encodeURIComponent(rawName)}`;
        const pData = (ROSTERS_DATA.active_rosters && ROSTERS_DATA.active_rosters['gentle-mates'] ? Object.values(ROSTERS_DATA.active_rosters).flat().find(x => x && x.name === rawName) : null);
        if (pData) {
          country = pData.country || '🌍';
          socials = pData.socials || {};
          pr = pData.pr || 0;
          if (pData.tracker_url) trackerUrl = pData.tracker_url;
        } else if (PLAYER_X_MAP[rawName]) {
          socials = { x: PLAYER_X_MAP[rawName] };
        }
      } else {
        rawName = p.name || p.ign || '';
        isFormer = !!p.is_former;
        country = p.country || '🌍';
        trackerUrl = p.tracker_url || `https://fortnitetracker.com/profile/all/${encodeURIComponent(rawName)}`;
        socials = p.socials || {};
        pr = p.pr || 0;
        if (!socials.x && p.x_url) socials.x = p.x_url;
      }

      if (rawName.toLowerCase() === 'pixie') {
        trackerUrl = "https://fortnitetracker.com/fortnite/profile/epic/havok%20%D1%80ixie%20b%C3%A4%C3%A4%C7%83/epic-events/overview";
      }

      let socialsHtml = '';
      if (socials.x) socialsHtml += `<a href="${socials.x}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" title="Profil X de ${rawName}">𝕏</a>`;
      if (socials.twitch) socialsHtml += `<a href="${socials.twitch}" target="_blank" rel="noopener noreferrer" class="social-pill twitch-pill" title="Twitch de ${rawName}">🟣</a>`;
      if (socials.youtube) socialsHtml += `<a href="${socials.youtube}" target="_blank" rel="noopener noreferrer" class="social-pill youtube-pill" title="YouTube de ${rawName}">🔴</a>`;
      if (socials.tiktok) socialsHtml += `<a href="${socials.tiktok}" target="_blank" rel="noopener noreferrer" class="social-pill tiktok-pill" title="TikTok de ${rawName}">🎵</a>`;
      if (socials.instagram) socialsHtml += `<a href="${socials.instagram}" target="_blank" rel="noopener noreferrer" class="social-pill insta-pill" title="Instagram de ${rawName}">📸</a>`;

      const prTitle = pr ? ` - PR : ${pr.toLocaleString('fr-FR')} pts` : '';
      const tagClass = isFormer ? 'player-tag former-player' : 'player-tag active-player';
      const tooltip = isFormer 
        ? `Ancien joueur ayant rapporté des points au club${prTitle}` 
        : `Joueur actif sous contrat${prTitle}`;

      return `
        <span class="${tagClass}" title="${tooltip}">
          <span class="player-country">${country}</span>
          <a href="${trackerUrl}" target="_blank" rel="noopener noreferrer" class="player-tracker-link" title="Statistiques Fortnite Tracker de ${rawName}">
            <strong>${rawName}${isFormer ? '*' : ''}</strong>
          </a>
          ${socialsHtml ? `<span class="social-pills-group">${socialsHtml}</span>` : ''}
        </span>
      `;
    }

    // Construction des pastilles de réseaux sociaux du club
    function buildClubSocialsHtml(c) {
      const s = c.socials || {};
      let html = '';
      if (s.x || c.x_url || c.xUrl) html += `<a href="${s.x || c.x_url || c.xUrl}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" title="X officiel de ${c.name}">𝕏</a>`;
      if (s.twitch) html += `<a href="${s.twitch}" target="_blank" rel="noopener noreferrer" class="social-pill twitch-pill" title="Twitch officiel de ${c.name}">🟣</a>`;
      if (s.youtube) html += `<a href="${s.youtube}" target="_blank" rel="noopener noreferrer" class="social-pill youtube-pill" title="YouTube officiel de ${c.name}">🔴</a>`;
      if (s.tiktok) html += `<a href="${s.tiktok}" target="_blank" rel="noopener noreferrer" class="social-pill tiktok-pill" title="TikTok officiel de ${c.name}">🎵</a>`;
      if (s.instagram) html += `<a href="${s.instagram}" target="_blank" rel="noopener noreferrer" class="social-pill insta-pill" title="Instagram officiel de ${c.name}">📸</a>`;
      if (s.discord) html += `<a href="${s.discord}" target="_blank" rel="noopener noreferrer" class="social-pill discord-pill" title="Discord officiel de ${c.name}">💬</a>`;
      return html ? `<div class="club-social-pills">${html}</div>` : '';
    }

    // Rendu du Classement Annuel (historique par année)
    function renderAnnualTable() {
      const year = document.getElementById('year-select').value;
      const search = document.getElementById('search-input').value.toLowerCase();
      const seasonData = ANNUAL_DATA[year];

      if (!seasonData) return;

      document.getElementById('context-title').innerText = seasonData.title;
      document.getElementById('context-text').innerText = seasonData.description;

      let list = [...seasonData.clubs];

      if (search) {
        list = list.filter(c => {
          const matchName = c.name && c.name.toLowerCase().includes(search);
          const matchTag = c.tag && c.tag.toLowerCase().includes(search);
          let matchPlayer = false;
          if (Array.isArray(c.players)) {
            matchPlayer = c.players.some(p => (typeof p === 'string' ? p : (p.name || '')).toLowerCase().includes(search));
          } else if (typeof c.notable === 'string') {
            matchPlayer = c.notable.toLowerCase().includes(search);
          } else if (Array.isArray(c.roster)) {
            matchPlayer = c.roster.some(p => (p || '').toLowerCase().includes(search));
          }
          return matchName || matchTag || matchPlayer;
        });
      }

      const tbody = document.getElementById('ranking-tbody');
      tbody.innerHTML = '';

      list.forEach((c) => {
        const rank = c.rank;
        const rankClass = rank === 1 ? 'rank-1' : rank === 2 ? 'rank-2' : rank === 3 ? 'rank-3' : '';
        const trophy = rank === 1 ? '🥇 ' : rank === 2 ? '🥈 ' : rank === 3 ? '🥉 ' : '';

        const logoPath = LOGO_MAP[c.id];
        const logoHtml = logoPath 
          ? `<img src="${logoPath}" class="club-logo" alt="${c.name}" onerror="this.outerHTML='<div class=\\'club-logo-placeholder\\'>${c.tag}</div>'">`
          : `<div class="club-logo-placeholder">${c.tag}</div>`;

        const trackerUrl = c.tracker_url || `https://fortnitetracker.com/esports/organization/${c.id}`;
        const clubSocialsHtml = buildClubSocialsHtml(c);

        let playersHtml = '';
        if (Array.isArray(c.players) && c.players.length > 0) {
          playersHtml = c.players.map(buildPlayerTagHtml).join(' ');
        } else if (Array.isArray(c.roster)) {
          playersHtml = c.roster.map(buildPlayerTagHtml).join(' ');
        } else if (typeof c.notable === 'string') {
          playersHtml = c.notable.split(',').map(buildPlayerTagHtml).join(' ');
        }

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="rank-cell ${rankClass}">${trophy}#${rank}</td>
          <td>
            <a href="${trackerUrl}" target="_blank" rel="noopener noreferrer" class="club-cell-link" title="Page Fortnite Tracker de ${c.name}">
              ${logoHtml}
              <div>
                <span class="club-name">${c.name}</span>
                <span class="club-tag">${c.tag}</span>
              </div>
            </a>
            ${clubSocialsHtml}
          </td>
          <td><div class="roster-tags">${playersHtml}</div></td>
          <td><div class="notable-achievement">${c.details || c.notable || c.key_achievement || ""}</div></td>
          <td class="pr-points ${rank === 1 ? 'pr-points-gold' : ''}">🏆 ${c.points.toLocaleString('fr-FR')} pts</td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Rendu du Classement Live (puissance actuelle)
    function renderLiveTable() {
      const search = document.getElementById('search-input-live').value.toLowerCase();
      let list = [...LIVE_DATA];

      if (search) {
        list = list.filter(c => {
          const matchName = c.name && c.name.toLowerCase().includes(search);
          const matchTag = c.tag && c.tag.toLowerCase().includes(search);
          let matchPlayer = false;
          if (Array.isArray(c.players)) {
            matchPlayer = c.players.some(p => (typeof p === 'string' ? p : (p.name || '')).toLowerCase().includes(search));
          } else if (typeof c.players === 'string') {
            matchPlayer = c.players.toLowerCase().includes(search);
          }
          return matchName || matchTag || matchPlayer;
        });
      }

      const tbody = document.getElementById('ranking-tbody');
      tbody.innerHTML = '';

      list.forEach((c) => {
        const rank = c.rank;
        const rankClass = rank === 1 ? 'rank-1' : rank === 2 ? 'rank-2' : rank === 3 ? 'rank-3' : '';
        const trophy = rank === 1 ? '🥇 ' : rank === 2 ? '🥈 ' : rank === 3 ? '🥉 ' : '';

        const logoPath = LOGO_MAP[c.id];
        const logoHtml = logoPath 
          ? `<img src="${logoPath}" class="club-logo" alt="${c.name}" onerror="this.outerHTML='<div class=\\'club-logo-placeholder\\'>${c.tag}</div>'">`
          : `<div class="club-logo-placeholder">${c.tag}</div>`;

        const trackerUrl = c.tracker_url || `https://fortnitetracker.com/esports/organization/${c.id}`;
        const clubSocialsHtml = buildClubSocialsHtml(c);

        let playersHtml = '';
        if (Array.isArray(c.players)) {
          playersHtml = c.players.map(buildPlayerTagHtml).join(' ');
        } else if (typeof c.players === 'string') {
          playersHtml = c.players.split(',').map(buildPlayerTagHtml).join(' ');
        }

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td class="rank-cell ${rankClass}">${trophy}#${rank}</td>
          <td>
            <a href="${trackerUrl}" target="_blank" rel="noopener noreferrer" class="club-cell-link" title="Page Fortnite Tracker de ${c.name}">
              ${logoHtml}
              <div>
                <span class="club-name">${c.name}</span>
                <span class="club-tag">${c.tag}</span>
              </div>
            </a>
            ${clubSocialsHtml}
          </td>
          <td><div class="roster-tags">${playersHtml}</div></td>
          <td><div class="notable-achievement">${c.details || c.trend || ""}</div></td>
          <td class="pr-points ${rank === 1 ? 'pr-points-gold' : ''}">⚡ ${c.livePr.toLocaleString('fr-FR')} pts</td>
        `;
        tbody.appendChild(tr);
      });
    }"""

# Replace renderAnnualTable and renderLiveTable in index.html
fn_start = html.find("function renderAnnualTable()")
fn_end = html.find("function renderPalmares()")

if fn_start != -1 and fn_end != -1:
    html = html[:fn_start] + new_render_functions + "\n\n    " + html[fn_end:]
    print("Replaced renderAnnualTable & renderLiveTable successfully.")
else:
    print("Error: Could not locate function boundaries.")

with open('LFF Dashboard/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully.")
