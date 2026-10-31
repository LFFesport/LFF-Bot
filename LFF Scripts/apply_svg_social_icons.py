import re

def main():
    with open('LFF Dashboard/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update CSS for social-pill, social-pill:hover, social-pills-group, x-icon
    old_css_target = """    .social-pills-group {
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
    }"""

    new_css_replacement = """    .social-pills-group {
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
      width: 19px;
      height: 19px;
      border-radius: 4px;
      padding: 0;
      text-decoration: none;
      transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
      vertical-align: middle;
      flex-shrink: 0;
      box-sizing: border-box;
      border: 1px solid transparent;
    }

    .social-pill svg {
      transition: transform 0.15s ease;
      display: block;
    }

    .social-pill:hover svg {
      transform: scale(1.15);
    }

    .x-pill {
      background: rgba(255, 255, 255, 0.1);
      color: #f1f5f9;
      border-color: rgba(255, 255, 255, 0.08);
    }
    .x-pill:hover {
      background: #000000;
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.35);
      box-shadow: 0 0 8px rgba(255, 255, 255, 0.25);
    }

    .twitch-pill {
      background: rgba(145, 70, 255, 0.2);
      color: #c084fc;
      border-color: rgba(145, 70, 255, 0.15);
    }
    .twitch-pill:hover {
      background: #9146FF;
      color: #ffffff;
      border-color: #a855f7;
      box-shadow: 0 0 8px rgba(145, 70, 255, 0.45);
    }

    .youtube-pill {
      background: rgba(239, 68, 68, 0.2);
      color: #fca5a5;
      border-color: rgba(239, 68, 68, 0.15);
    }
    .youtube-pill:hover {
      background: #ff0000;
      color: #ffffff;
      border-color: #ef4444;
      box-shadow: 0 0 8px rgba(239, 68, 68, 0.45);
    }

    .tiktok-pill {
      background: rgba(0, 242, 234, 0.18);
      color: #38bdf8;
      border-color: rgba(0, 242, 234, 0.15);
    }
    .tiktok-pill:hover {
      background: #010101;
      color: #00f2fe;
      border-color: #ff0050;
      box-shadow: 0 0 8px rgba(0, 242, 254, 0.45);
    }

    .insta-pill {
      background: rgba(236, 72, 153, 0.2);
      color: #f472b6;
      border-color: rgba(236, 72, 153, 0.15);
    }
    .insta-pill:hover {
      background: linear-gradient(45deg, #f58529, #dd2a7b, #8134af);
      color: #ffffff;
      border-color: #ec4899;
      box-shadow: 0 0 8px rgba(221, 42, 123, 0.45);
    }

    .discord-pill {
      background: rgba(88, 101, 242, 0.2);
      color: #a5b4fc;
      border-color: rgba(88, 101, 242, 0.15);
    }
    .discord-pill:hover {
      background: #5865F2;
      color: #ffffff;
      border-color: #818cf8;
      box-shadow: 0 0 8px rgba(88, 101, 242, 0.45);
    }"""

    if old_css_target in html:
        html = html.replace(old_css_target, new_css_replacement)
        print('[+] Replaced CSS rules for social pills')
    else:
        print('[!] Warning: old_css_target not found')

    # 2. Add SOCIAL_ICONS definition in JS
    icons_def = """    // Vector logos officiels pour les réseaux sociaux (SVG conformes aux chartes de marque)
    const SOCIAL_ICONS = {
      x: `<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor" aria-hidden="true" style="display:block;"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>`,
      twitch: `<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor" aria-hidden="true" style="display:block;"><path d="M11.571 4.714h1.715v5.143H11.57zm4.715 0H18v5.143h-1.714zM6 0L1.714 4.286v15.428h5.143V24l4.286-4.286h3.428L22.286 12V0zm14.571 11.143l-3.428 3.428h-3.429l-3 3v-3H6.857V1.714h13.714Z"/></svg>`,
      youtube: `<svg viewBox="0 0 24 24" width="12" height="11" fill="currentColor" aria-hidden="true" style="display:block;"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>`,
      tiktok: `<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor" aria-hidden="true" style="display:block;"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.89 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.35 0 .69.06 1 .18V9.45a6.34 6.34 0 0 0-1-.08 6.34 6.34 0 1 0 6.34 6.34V8.5a8.27 8.27 0 0 0 4.76 1.48V6.69z"/></svg>`,
      instagram: `<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor" aria-hidden="true" style="display:block;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>`,
      discord: `<svg viewBox="0 0 24 24" width="12" height="11" fill="currentColor" aria-hidden="true" style="display:block;"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>`
    };
"""

    if "function buildPlayerTagHtml" in html and "const SOCIAL_ICONS" not in html:
        html = html.replace("    function buildPlayerTagHtml", icons_def + "\n    function buildPlayerTagHtml")
        print('[+] Added SOCIAL_ICONS definition before buildPlayerTagHtml')

    # 3. Update buildPlayerTagHtml socials rendering
    old_player_socials = """      let socialsHtml = '';
      if (socials.x) socialsHtml += `<a href="${socials.x}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" title="Profil X de ${rawName}">𝕏</a>`;
      if (socials.twitch) socialsHtml += `<a href="${socials.twitch}" target="_blank" rel="noopener noreferrer" class="social-pill twitch-pill" title="Twitch de ${rawName}">🟣</a>`;
      if (socials.youtube) socialsHtml += `<a href="${socials.youtube}" target="_blank" rel="noopener noreferrer" class="social-pill youtube-pill" title="YouTube de ${rawName}">🔴</a>`;
      if (socials.tiktok) socialsHtml += `<a href="${socials.tiktok}" target="_blank" rel="noopener noreferrer" class="social-pill tiktok-pill" title="TikTok de ${rawName}">🎵</a>`;
      if (socials.instagram) socialsHtml += `<a href="${socials.instagram}" target="_blank" rel="noopener noreferrer" class="social-pill insta-pill" title="Instagram de ${rawName}">📸</a>`;"""

    new_player_socials = """      let socialsHtml = '';
      if (socials.x) socialsHtml += `<a href="${socials.x}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" title="Profil X de ${rawName}">${SOCIAL_ICONS.x}</a>`;
      if (socials.twitch) socialsHtml += `<a href="${socials.twitch}" target="_blank" rel="noopener noreferrer" class="social-pill twitch-pill" title="Twitch de ${rawName}">${SOCIAL_ICONS.twitch}</a>`;
      if (socials.youtube) socialsHtml += `<a href="${socials.youtube}" target="_blank" rel="noopener noreferrer" class="social-pill youtube-pill" title="YouTube de ${rawName}">${SOCIAL_ICONS.youtube}</a>`;
      if (socials.tiktok) socialsHtml += `<a href="${socials.tiktok}" target="_blank" rel="noopener noreferrer" class="social-pill tiktok-pill" title="TikTok de ${rawName}">${SOCIAL_ICONS.tiktok}</a>`;
      if (socials.instagram) socialsHtml += `<a href="${socials.instagram}" target="_blank" rel="noopener noreferrer" class="social-pill insta-pill" title="Instagram de ${rawName}">${SOCIAL_ICONS.instagram}</a>`;
      if (socials.discord) socialsHtml += `<a href="${socials.discord}" target="_blank" rel="noopener noreferrer" class="social-pill discord-pill" title="Discord de ${rawName}">${SOCIAL_ICONS.discord}</a>`;"""

    if old_player_socials in html:
        html = html.replace(old_player_socials, new_player_socials)
        print('[+] Updated buildPlayerTagHtml socials rendering with vector SVG icons')
    else:
        print('[!] Warning: old_player_socials not found')

    # 4. Update buildClubSocialsHtml
    old_club_socials = """    function buildClubSocialsHtml(c) {
      const s = c.socials || {};
      let html = '';
      if (s.x || c.x_url || c.xUrl) html += `<a href="${s.x || c.x_url || c.xUrl}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" title="X officiel de ${c.name}">𝕏</a>`;
      if (s.twitch) html += `<a href="${s.twitch}" target="_blank" rel="noopener noreferrer" class="social-pill twitch-pill" title="Twitch officiel de ${c.name}">🟣</a>`;
      if (s.youtube) html += `<a href="${s.youtube}" target="_blank" rel="noopener noreferrer" class="social-pill youtube-pill" title="YouTube officiel de ${c.name}">🔴</a>`;
      if (s.tiktok) html += `<a href="${s.tiktok}" target="_blank" rel="noopener noreferrer" class="social-pill tiktok-pill" title="TikTok officiel de ${c.name}">🎵</a>`;
      if (s.instagram) html += `<a href="${s.instagram}" target="_blank" rel="noopener noreferrer" class="social-pill insta-pill" title="Instagram officiel de ${c.name}">📸</a>`;
      if (s.discord) html += `<a href="${s.discord}" target="_blank" rel="noopener noreferrer" class="social-pill discord-pill" title="Discord officiel de ${c.name}">💬</a>`;
      return html ? `<div class="club-social-pills">${html}</div>` : '';
    }"""

    new_club_socials = """    function buildClubSocialsHtml(c) {
      const s = c.socials || {};
      let html = '';
      if (s.x || c.x_url || c.xUrl) html += `<a href="${s.x || c.x_url || c.xUrl}" target="_blank" rel="noopener noreferrer" class="social-pill x-pill" title="X officiel de ${c.name}">${SOCIAL_ICONS.x}</a>`;
      if (s.twitch) html += `<a href="${s.twitch}" target="_blank" rel="noopener noreferrer" class="social-pill twitch-pill" title="Twitch officiel de ${c.name}">${SOCIAL_ICONS.twitch}</a>`;
      if (s.youtube) html += `<a href="${s.youtube}" target="_blank" rel="noopener noreferrer" class="social-pill youtube-pill" title="YouTube officiel de ${c.name}">${SOCIAL_ICONS.youtube}</a>`;
      if (s.tiktok) html += `<a href="${s.tiktok}" target="_blank" rel="noopener noreferrer" class="social-pill tiktok-pill" title="TikTok officiel de ${c.name}">${SOCIAL_ICONS.tiktok}</a>`;
      if (s.instagram) html += `<a href="${s.instagram}" target="_blank" rel="noopener noreferrer" class="social-pill insta-pill" title="Instagram officiel de ${c.name}">${SOCIAL_ICONS.instagram}</a>`;
      if (s.discord) html += `<a href="${s.discord}" target="_blank" rel="noopener noreferrer" class="social-pill discord-pill" title="Discord officiel de ${c.name}">${SOCIAL_ICONS.discord}</a>`;
      return html ? `<div class="club-social-pills">${html}</div>` : '';
    }"""

    if old_club_socials in html:
        html = html.replace(old_club_socials, new_club_socials)
        print('[+] Updated buildClubSocialsHtml with vector SVG icons')
    else:
        print('[!] Warning: old_club_socials not found')

    # 5. Update renderPalmares winner and podium X icons
    html = html.replace('${winner.name} <span class="x-icon">𝕏</span>', '${winner.name} <span class="x-icon">${SOCIAL_ICONS.x}</span>')
    html = html.replace('<strong>${second.name}</strong> <span class="x-icon">𝕏</span>', '<strong>${second.name}</strong> <span class="x-icon">${SOCIAL_ICONS.x}</span>')
    html = html.replace('<strong>${third.name}</strong> <span class="x-icon">𝕏</span>', '<strong>${third.name}</strong> <span class="x-icon">${SOCIAL_ICONS.x}</span>')

    # 6. Update renderTransfers player and club X icons
    html = html.replace('title="Compte X de ${t.player}">𝕏</a>', 'title="Compte X de ${t.player}">${SOCIAL_ICONS.x}</a>')
    html = html.replace('${t.to} <span class="x-icon">𝕏</span>', '${t.to} <span class="x-icon">${SOCIAL_ICONS.x}</span>')

    # 7. Update header button at lines 864 & 1025
    x_badge_svg = """<svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor" aria-hidden="true" style="display:inline-block; vertical-align:middle; margin-right:4px;"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>"""
    html = html.replace('𝕏 @LFFesport', f'{x_badge_svg}@LFFesport')
    html = html.replace('𝕏 Compte Officiel @LFFesport', f'{x_badge_svg}Compte Officiel @LFFesport')

    with open('LFF Dashboard/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('[+] Saved updated LFF Dashboard/index.html')

if __name__ == '__main__':
    main()
