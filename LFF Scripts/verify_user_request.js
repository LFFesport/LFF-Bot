const fs = require('fs');
const html = fs.readFileSync('LFF Dashboard/index.html', 'utf-8');

console.log("=== VÉRIFICATION GLOBALE LFF ===");

// 1. Course au titre
const titleCheck = html.includes("COURSE AU TITRE (2018 - AUJOURD'HUI)");
console.log(`1. Titre 'COURSE AU TITRE (2018 - AUJOURD'HUI)': ${titleCheck ? '✅ OK' : '❌ FAIL'}`);

// 2. Option 2026
const option2026Check = html.includes("2026 (En cours)") || html.includes("2026 (en cours)");
console.log(`2. Option 2026 (En cours): ${option2026Check ? '✅ OK' : '❌ FAIL'}`);

// 3. Em dashes
const emDashCount = (html.match(/—/g) || []).length;
console.log(`3. Tirets cadratins (—): ${emDashCount === 0 ? '✅ 0 trouvé' : `❌ ${emDashCount} trouvés`}`);

// 4. Drapeaux graphiques
const flagFunctionCheck = html.includes("getPlayerFlagHtml") && html.includes('flags/${iso}.png');
const flagDir = fs.readdirSync('LFF Dashboard/flags');
console.log(`4. Drapeaux graphiques (${flagDir.length} fichiers PNG locaux): ${flagFunctionCheck && flagDir.length >= 22 ? '✅ OK' : '❌ FAIL'}`);

// 5. Points non-ronds
const roundTotals = (html.match(/🏆\s*\d+[05]00\s*pts/g) || []).length;
console.log(`5. Points ronds suspects (ex: 18500, 50000): ${roundTotals === 0 ? '✅ 0 (tous non-ronds)' : `⚠️ ${roundTotals} trouvés`}`);

// 6. X de Zerance
const zeranceCheck = html.includes("https://x.com/ZerancePartout");
const badZeranceCheck = html.includes("https://x.com/Zerance_Club") || html.includes("https://x.com/TeamZerance");
console.log(`6. Zerance X officiel: ${zeranceCheck && !badZeranceCheck ? '✅ https://x.com/ZerancePartout (aucun ancien lien)' : '❌ FAIL'}`);

// 7. TheVic
const thevicCheck = html.includes("TheVic") && html.includes("thevic%20%E3%83%8D");
const thevicSocials = html.includes("https://x.com/TheVic_c") && html.includes("https://youtube.com/@TheVicc");
console.log(`7. TheVic intégration Tracker & réseaux: ${thevicCheck && thevicSocials ? '✅ OK' : '❌ FAIL'}`);

// 8. Clubs page tri et recherche
const clubsSortCheck = html.includes("club-sort-select") && html.includes("club-search-input");
console.log(`8. Clubs page tri & recherche: ${clubsSortCheck ? '✅ OK' : '❌ FAIL'}`);

// 9. Règlement 1 pt LFF = 1 pt Tracker
const reglementCheck = /1\s*point\s*lff\s*=\s*1\s*point/i.test(html);
console.log(`9. Règlement explication points: ${reglementCheck ? '✅ OK' : '❌ FAIL'}`);

// 10. Universal Tracker links on clubs and players
const clubTrackerCheck = html.includes("https://fortnitetracker.com/esports/organization/");
const playerTrackerCheck = html.includes("player-tracker-link") && html.includes("https://fortnitetracker.com/profile/all/");
console.log(`10. Liens universels Tracker (clubs & joueurs): ${clubTrackerCheck && playerTrackerCheck ? '✅ OK' : '❌ FAIL'}`);

// 11. Multi-network social pills
const socialsPillsCheck = html.includes("social-pills-group") && html.includes("club-social-pills");
console.log(`11. Pastilles multi-réseaux SVG (clubs & joueurs): ${socialsPillsCheck ? '✅ OK' : '❌ FAIL'}`);
