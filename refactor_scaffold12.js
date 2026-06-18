const fs = require('fs');

const file = 'src/components/workspace/grade12/accounting/Grade12AccountingScaffold.jsx';
let content = fs.readFileSync(file, 'utf8');

// 1. Add isMarkingEnv to props if not there yet
if (!content.includes('isMarkingEnv = false,')) {
    content = content.replace(/onBack,/, 'onBack,\n    isMarkingEnv = false,');
}

// 2. Set marking mode from props
content = content.replace(/marking\.setMarkingMode\('practice'\);/g, "marking.setMarkingMode(isMarkingEnv ? 'marking' : 'practice');");

// 3. Remove inline toggle completely
let toggleRegex = /\{question && \(\s*<div className="flex items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200">\s*<span className="text-sm font-semibold text-slate-700">Mode:<\/span>[\s\S]*?<\/div>\s*\)\}/g;
content = content.replace(toggleRegex, '{/* Inline Toggle Removed for 2-Mode Architecture */}');

fs.writeFileSync(file, content, 'utf8');
console.log('Processed', file);
