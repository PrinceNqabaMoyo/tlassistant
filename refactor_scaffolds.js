const fs = require('fs');

const files = [
    'src/components/workspace/grade10/accounting/indigenous-bookkeeping/Grade10AccountingIndigenousScaffold.jsx',
    'src/components/workspace/grade10/accounting/ethics/Grade10AccountingEthicsScaffold.jsx',
    'src/components/workspace/grade10/accounting/gaap/Grade10AccountingGAAPScaffold.jsx',
    'src/components/workspace/grade10/accounting/internal-control/Grade10AccountingInternalControlScaffold.jsx',
    'src/components/workspace/grade10/accounting/sole-trader/Grade10AccountingSoleTraderScaffold.jsx',
    'src/components/workspace/grade11/accounting/Grade11AccountingScaffold.jsx'
];

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    // 1. Add isMarkingEnv to props if not there yet
    if (!content.includes('isMarkingEnv = false,')) {
        content = content.replace(/onBack,/, 'onBack,\n    isMarkingEnv = false,');
    }

    // 2. Set marking mode from props
    // We update all marking.setMarkingMode('practice') inside useEffect to use the prop
    content = content.replace(/marking\.setMarkingMode\('practice'\);/g, "marking.setMarkingMode(isMarkingEnv ? 'marking' : 'practice');");

    // 3. Remove inline toggle completely
    // The exact div string in Grade10AccountingSoleTraderScaffold:
    /*
                {question && (
                    <div className="flex items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200">
                        <span className="text-sm font-semibold text-slate-700">Mode:</span>
                        <button
                            onClick={marking.toggleMarkingMode}
                            disabled={marking.isSubmitting}
                            className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2 ${!marking.isPracticeMode ? 'bg-indigo-600' : 'bg-slate-200'}`}
                        >
                            <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${!marking.isPracticeMode ? 'translate-x-6' : 'translate-x-1'}`} />
                        </button>
                        <span className="text-sm text-slate-600">
                            {marking.isPracticeMode ? 'Practice' : 'Marking'}
                        </span>
                    </div>
                )}
    */
    // We can use a regex that matches from `{question && (\s*<div.*>Mode:<\/span>` to `<\/div>\s*\)\}`
    let toggleRegex = /\{question && \(\s*<div className="flex items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200">\s*<span className="text-sm font-semibold text-slate-700">Mode:<\/span>[\s\S]*?<\/div>\s*\)\}/g;
    content = content.replace(toggleRegex, '{/* Inline Toggle Removed for 2-Mode Architecture */}');

    // Make sure we also update the effect dependencies if needed, but [isMarkingEnv] can just be ignored as a missing dependency warning if it's fine.

    fs.writeFileSync(file, content, 'utf8');
    console.log('Processed', file);
});
