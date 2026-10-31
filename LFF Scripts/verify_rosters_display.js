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
      value: id === 'year-select' ? '2026' : '',
      style: {},
      children: [],
      appendChild: function(child) {
        this.children.push(child);
        const tag = child.tagName ? child.tagName.toLowerCase() : 'div';
        this.innerHTML += `<${tag}>${child.innerHTML || ''}</${tag}>`;
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

// Test Annual Table
context.renderAnnualTable();
const annualHtml = getEl('ranking-tbody').innerHTML;
console.log('=== ANNUAL TABLE CHECKS ===');
console.log('HavoK SwizzY in Annual:', annualHtml.includes('SwizzY'));
console.log('HavoK IDrop in Annual:', annualHtml.includes('IDrop'));
console.log('Gentle Mates Akiira in Annual:', annualHtml.includes('Akiira'));
console.log('Gentle Mates MariusCOW* in Annual:', annualHtml.includes('MariusCOW*'));
console.log('Solary Ghonzo in Annual:', annualHtml.includes('Ghonzo'));
console.log('Solary SkyJump* in Annual:', annualHtml.includes('SkyJump*'));
console.log('Solary XZEEVIT in Annual:', annualHtml.includes('XZEEVIT'));
console.log('GameWard Snaylyx in Annual:', annualHtml.includes('Snaylyx'));
console.log('GameWard Nociff* in Annual:', annualHtml.includes('Nociff*'));

// Test Live Table
context.renderLiveTable();
const liveHtml = getEl('ranking-tbody').innerHTML;
console.log('\n=== LIVE TABLE CHECKS ===');
console.log('HavoK SwizzY in Live:', liveHtml.includes('SwizzY'));
console.log('HavoK IDrop in Live:', liveHtml.includes('IDrop'));
console.log('Gentle Mates Akiira in Live:', liveHtml.includes('Akiira'));
console.log('Gentle Mates Snayzy in Live:', liveHtml.includes('Snayzy'));
console.log('Gentle Mates NO MariusCOW in Live:', !liveHtml.includes('MariusCOW'));
console.log('Solary NO SkyJump in Live:', !liveHtml.includes('SkyJump'));
console.log('Solary Darkos in Live:', liveHtml.includes('Darkos'));
console.log('Solary Zangi in Live:', liveHtml.includes('Zangi'));
console.log('GameWard NO Nociff in Live:', !liveHtml.includes('Nociff'));
console.log('GameWard Baxo in Live:', liveHtml.includes('Baxo'));
console.log('Zero asterisks in Live:', !liveHtml.includes('*'));
