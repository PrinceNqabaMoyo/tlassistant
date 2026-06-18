const fs = require('fs');

const files = [
    'src/components/workspace/grade10/accounting/indigenous-bookkeeping/Grade10AccountingIndigenousScaffold.jsx',
    'src/components/workspace/grade10/accounting/ethics/Grade10AccountingEthicsScaffold.jsx',
    'src/components/workspace/grade10/accounting/gaap/Grade10AccountingGAAPScaffold.jsx',
    'src/components/workspace/grade10/accounting/internal-control/Grade10AccountingInternalControlScaffold.jsx',
    'src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderScaffold.jsx'
];

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    // The target: const isHelpable = journalType === 'crj' && helpText.length > 0;
    // We want to replace it with: const isHelpable = !isMarkingEnv && helpText.length > 0;

    // It appears twice per file (one for headerRows, one for base headers)
    const regex = /const isHelpable = journalType === 'crj' && helpText\.length > 0;/g;
    content = content.replace(regex, "const isHelpable = !isMarkingEnv && helpText.length > 0;");

    fs.writeFileSync(file, content, 'utf8');
    console.log('Processed', file);
});
