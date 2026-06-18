const fs = require('fs');
const path = require('path');

// 1. Rename index.js to index.jsx
const terms = ['term-1', 'term-2'];
const bsDir = 'src/components/workspace/grade10/business-studies';
terms.forEach(term => {
    const termDir = path.join(bsDir, term);
    if (!fs.existsSync(termDir)) return;
    const topics = fs.readdirSync(termDir);
    topics.forEach(topic => {
        const indexJs = path.join(termDir, topic, 'index.js');
        const indexJsx = path.join(termDir, topic, 'index.jsx');
        if (fs.existsSync(indexJs)) {
            fs.renameSync(indexJs, indexJsx);
            console.log('Renamed', indexJs, 'to', indexJsx);
        }
    });
});

// 2. Create the missing ui components
const uiDir = path.join('src', 'components', 'workspace', 'grade10', 'ui');
if (!fs.existsSync(uiDir)) fs.mkdirSync(uiDir, { recursive: true });

const cardContent = `import React from 'react';
export const Card = ({ children, className = '' }) => (
    <div className={\`bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden \${className}\`}>
        {children}
    </div>
);
export const CardContent = ({ children, className = '' }) => (
    <div className={\`p-6 \${className}\`}>
        {children}
    </div>
);
`;
fs.writeFileSync(path.join(uiDir, 'card.jsx'), cardContent);

const buttonContent = `import React from 'react';
export const Button = ({ children, onClick, disabled, className = '', variant = 'primary' }) => {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={\`px-4 py-2 rounded-xl font-semibold transition-colors flex items-center justify-center \${disabled ? 'opacity-50 cursor-not-allowed' : ''} \${className}\`}
        >
            {children}
        </button>
    );
};
`;
fs.writeFileSync(path.join(uiDir, 'button.jsx'), buttonContent);
console.log('Created card.jsx and button.jsx in grade10/ui');
