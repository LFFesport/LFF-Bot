const fs = require('fs');

const html = fs.readFileSync('LFF Dashboard/index.html', 'utf8');

console.log('1. COURSE AU TITRE ANNUEL (2018 - AUJOURD\'HUI):', html.includes("COURSE AU TITRE ANNUEL (2018 - AUJOURD'HUI)"));
console.log('2. 2026 (En cours):', html.includes("2026 (En cours)"));
console.log('3. Zero em dashes:', !html.includes("—"));
console.log('4. Zero Tier mentions in nav or tabs:', !html.includes("Tier 1") && !html.includes("Tier 2") && !html.includes("Tier 3"));
console.log('5. Renamed tabs present:');
console.log('   - Classement:', html.includes("📊 Classement"));
console.log('   - Palmarès:', html.includes("🏆 Palmarès"));
console.log('   - Transferts:', html.includes("🔄 Transferts"));
console.log('   - Clubs:', html.includes("🛡️ Clubs"));
console.log('   - Règlement:', html.includes("⚖️ Règlement"));
console.log('6. Clubs page has no Tracker/Liquipedia buttons:', !html.includes('btn-tracker') && !html.includes('btn-wiki'));
console.log('7. Reglement section 4 updated:', html.includes("4. Affichage Exhaustif de Tous les Joueurs (Sans Restriction à 4)"));
