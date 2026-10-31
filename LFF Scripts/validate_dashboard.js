const fs = require('fs');
const html = fs.readFileSync('LFF Dashboard/index.html', 'utf8');
const scriptMatches = html.match(/<script>([\s\S]*?)<\/script>/g);
console.log('Found scripts:', scriptMatches ? scriptMatches.length : 0);
if (scriptMatches) {
  scriptMatches.forEach((s, idx) => {
    const code = s.replace(/<script>/, '').replace(/<\/script>/, '');
    try {
      new Function(code);
      console.log('Script ' + (idx + 1) + ' syntax: OK');
    } catch (e) {
      console.error('Script ' + (idx + 1) + ' Error:', e);
      process.exit(1);
    }
  });
}
