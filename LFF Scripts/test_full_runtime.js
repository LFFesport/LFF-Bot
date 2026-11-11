const fs = require('fs');

const htmlPath = fs.existsSync('LFF Dashboard/LFF Plateforme.html') 
  ? 'LFF Dashboard/LFF Plateforme.html' 
  : 'LFF Dashboard/index.html';
const html = fs.readFileSync(htmlPath, 'utf8');
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
      }
    };
  }
  return elements[id];
}

const document = {
  getElementById: getEl,
  createElement: function(tag) {
    return {
      tagName: tag,
      className: '',
      style: {},
      innerHTML: '',
      appendChild: function(child) {
        this.innerHTML += child.innerHTML || '';
      }
    };
  },
  querySelectorAll: function() { return []; }
};

const window = {
  addEventListener: function() {}
};

// Exécution du code dashboard
const sandbox = {
  document,
  window,
  console: { log: () => {} },
  encodeURIComponent,
  parseInt,
  parseFloat,
  Array,
  Object,
  String,
  Number
};

const vm = require('vm');
const context = vm.createContext(sandbox);

try {
  vm.runInContext(code, context);
  
  // Test 1: renderAnnualTable
  context.renderAnnualTable();
  const rankTbody = getEl('ranking-tbody');
  if (!rankTbody.innerHTML || rankTbody.innerHTML.includes('undefined')) {
    throw new Error('renderAnnualTable returned empty or undefined values!');
  }
  console.log('renderAnnualTable OK! Rows length:', rankTbody.innerHTML.length);

  // Test 2: renderLiveTable
  context.renderLiveTable();
  const liveTbody = getEl('ranking-tbody');
  if (!liveTbody.innerHTML || liveTbody.innerHTML.includes('undefined')) {
    throw new Error('renderLiveTable returned empty or undefined values!');
  }
  console.log('renderLiveTable OK! Rows length:', liveTbody.innerHTML.length);

  // Test 3: renderPalmares
  context.renderPalmares();
  const palmares = getEl('palmares-container');
  if (!palmares.innerHTML || palmares.innerHTML.includes('undefined')) {
    throw new Error('renderPalmares returned empty or undefined values!');
  }
  console.log('renderPalmares OK! Length:', palmares.innerHTML.length);

  // Test 4: renderTransfers
  context.renderTransfers();
  const transfers = getEl('transfer-feed-container');
  if (!transfers.innerHTML || transfers.innerHTML.includes('undefined')) {
    throw new Error('renderTransfers returned empty or undefined values!');
  }
  console.log('renderTransfers OK! Length:', transfers.innerHTML.length);

  // Test 5: renderClubs
  context.renderClubs();
  const clubs = getEl('clubs-grid-container');
  if (!clubs.innerHTML || clubs.innerHTML.includes('undefined')) {
    throw new Error('renderClubs returned empty or undefined values!');
  }
  console.log('renderClubs OK! Length:', clubs.innerHTML.length);

  console.log('ALL TESTS PASSED WITH 0 ERRORS AND 0 UNDEFINED VALUES!');
} catch (err) {
  console.error('RUNTIME ERROR IN DASHBOARD:', err);
  process.exit(1);
}
