const fs = require('fs');
const content = fs.readFileSync('src/App.jsx', 'utf-8');
const lines = content.split('\n');
const matches = [];
for (let i=0; i<lines.length; i++) {
  if (lines[i].includes('/api/')) {
    matches.push((i+1) + ": " + lines[i].trim());
  }
}
console.log(matches.join('\n'));
