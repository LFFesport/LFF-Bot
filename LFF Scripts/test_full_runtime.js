const fs = require('fs');

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

try {
  const vm = require('vm');
  vm.createContext(context);
  vm.runInContext(code, context);

  // Test renderAnnualTable
  context.currentMode = 'annual';
  context.renderAnnualTable();
  console.log('renderAnnualTable OK! Rows length:', context.document.getElementById('ranking-tbody').innerHTML.length);

  // Clear tbody and test renderLiveTable
  context.document.getElementById('ranking-tbody').innerHTML = '';
  context.currentMode = 'live';
  context.renderLiveTable();
  console.log('renderLiveTable OK! Rows length:', context.document.getElementById('ranking-tbody').innerHTML.length);

  // Test renderPalmares
  context.renderPalmares();
  console.log('renderPalmares OK! Length:', context.document.getElementById('palmares-container').innerHTML.length);

  // Test renderTransfers
  context.renderTransfers();
  console.log('renderTransfers OK! Length:', context.document.getElementById('transfer-feed-container').innerHTML.length);

  // Test renderClubs
  context.renderClubs();
  console.log('renderClubs OK! Length:', context.document.getElementById('clubs-grid-container').innerHTML.length);

  // Check for undefined values in generated content
  let hasUndefined = false;
  for (const [id, el] of Object.entries(elements)) {
    if (el.innerHTML.includes('undefined')) {
      console.warn(`WARNING: Element #${id} contains 'undefined' in its innerHTML!`);
      hasUndefined = true;
    }
  }

  if (!hasUndefined) {
    console.log('ALL TESTS PASSED WITH 0 ERRORS AND 0 UNDEFINED VALUES!');
  }
} catch (e) {
  console.error('VM Execution Error:', e);
  process.exit(1);
}
