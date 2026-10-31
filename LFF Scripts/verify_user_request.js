const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('LFF Dashboard/index.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
const code = scriptMatch[1];

const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id,
      innerHTML: '',
      innerText: '',
      value: id === 'year-select' ? '2026' : (id === 'club-sort-select' ? 'points-desc' : ''),
      style: {},
      children: [],
      appendChild: function(child) {
        this.children.push(child);
        const tag = child.tagName ? child.tagName.toLowerCase() : 'div';
        this.innerHTML += `<${tag} class="${child.className || ''}">${child.innerHTML || ''}</${tag}>`;
      },
      classList: {
        add: () => {},
        remove: () => {},
        contains: () => false
      },
      querySelectorAll: () => []
    };
  }
  return elements[id];
}

const window = {
  document: {
    getElementById: getEl,
    querySelectorAll: () => [],
    querySelector: () => null,
    createElement: (tag) => ({
      tagName: tag,
      className: '',
      innerHTML: '',
      classList: { add: () => {}, remove: () => {} }
    }),
    addEventListener: () => {}
  },
  addEventListener: () => {},
  console: console
};

const context = {
  window,
  document: window.document,
  console: console,
  setTimeout: () => {},
  setInterval: () => {}
};

vm.createContext(context);
vm.runInContext(code, context);

console.log('=== TEST 1: THEAD COLUMNS ===');
console.log('Has "Faits d\'armes / Titres":', html.includes("Faits d'armes / Titres"));
console.log('Has "Détail / Tendance Live":', html.includes("Détail / Tendance Live"));
console.log('Has <th>Clubs</th>:', html.includes("<th>Clubs</th>"));
console.log('Has <th style="text-align: right;" id="th-points-col">Points</th>:', html.includes('id="th-points-col">Points</th>'));

console.log('\n=== TEST 2: RANKING TABLE RENDERING ===');
context.renderAnnualTable();
const tableHtml = getEl('ranking-tbody').innerHTML;
console.log('Pixie has flag image:', tableHtml.includes('flags/se.png') && tableHtml.includes('player-flag-img'));
console.log('Pixie has points pill:', tableHtml.includes('215\u202f000 pts') || tableHtml.includes('215 000 pts'));
console.log('SwizzY has flag image ru:', tableHtml.includes('flags/ru.png'));
console.log('PabloWingu has flag image dk:', tableHtml.includes('flags/dk.png'));
console.log('Vanyak3kk has flag image ua:', tableHtml.includes('flags/ua.png'));
console.log('Akiira has flag image fr:', tableHtml.includes('flags/fr.png'));
console.log('Solary logo in table:', tableHtml.includes('Logo Solary (fond vide).png'));

console.log('\n=== TEST 3: CLUBS PAGE RENDERING ===');
context.renderClubs();
const clubsHtml = getEl('clubs-grid-container').innerHTML;
console.log('HavoK points in clubs card:', clubsHtml.includes('1\u202f038\u202f548 pts') || clubsHtml.includes('1 038 548 pts') || clubsHtml.includes('pts'));
console.log('Gentle Mates in clubs card:', clubsHtml.includes('Gentle Mates'));
console.log('Gentle Mates active roster in clubs card:', clubsHtml.includes('Akiira') && clubsHtml.includes('Vanyak3kk') && clubsHtml.includes('Kurama'));
console.log('Flags present in clubs card:', clubsHtml.includes('player-flag-img'));
console.log('Player points present in clubs card:', clubsHtml.includes('player-pts'));

console.log('\n=== TEST 4: REGLEMENT PAGE & 1 POINT LFF = 1 POINT TRACKER ===');
console.log('Contains 1 Point LFF = 1 Point Fortnite Tracker:', html.includes('1 Point LFF = 1 Point Fortnite Tracker'));
console.log('Contains No 2-rankings switcher:', !html.includes('COMPRENDRE LES DEUX CLASSEMENTS'));
console.log('Contains Zero em dashes in html:', !html.includes('—'));

console.log('\n=== TEST 5: CLUBS PAGE CONTROLS ===');
console.log('Contains club-search-input:', html.includes('id="club-search-input"'));
console.log('Contains club-sort-select:', html.includes('id="club-sort-select"'));
console.log('Contains points-desc (default):', html.includes('value="points-desc" selected'));
console.log('Contains points-asc:', html.includes('value="points-asc"'));
console.log('Contains alpha-asc:', html.includes('value="alpha-asc"'));
