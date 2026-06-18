const fs = require('fs');

const content = fs.readFileSync('src/components/workspace/registry/grade10Registry - Copy.js', 'utf8');
const lines = content.split('\n');

const importsMath = [];
const routesMath = [];
const exportsMath = [];

let currentRoute = [];
let currentSubject = '';
let currentExport = [];

let inRegistryObject = false;

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (line.startsWith('export const grade10Registry = {') || line.startsWith('export const grade10Registry={')) {
        inRegistryObject = true;
        continue;
    }

    if (inRegistryObject) {
        if (line === '};') {
            inRegistryObject = false;
            if (currentExport.length > 0) {
                const block = currentExport.join('\n');
                if (!block.includes('grade10_accounting_') && !block.includes('grade10_bookkeeping_') && !block.includes('grade10_general_ledger') && !block.includes('grade10_trial_balance') && !block.includes('grade10_financial_statements') && !block.includes('grade10_salary_journals') && !block.includes('grade10_wages_journals') && !block.includes('grade10_bs_')) exportsMath.push(block + (block.trim().endsWith(',') ? '' : ','));
                currentExport = [];
            }
            continue;
        }

        if (line.trim().startsWith('grade10_')) {
            if (currentExport.length > 0) {
                const block = currentExport.join('\n');
                if (!block.includes('grade10_accounting_') && !block.includes('grade10_bookkeeping_') && !block.includes('grade10_general_ledger') && !block.includes('grade10_trial_balance') && !block.includes('grade10_financial_statements') && !block.includes('grade10_salary_journals') && !block.includes('grade10_wages_journals') && !block.includes('grade10_bs_')) exportsMath.push(block + (block.trim().endsWith(',') ? '' : ','));
                currentExport = [];
            }
        }
        
        currentExport.push(line);
        continue;
    }

    if (line.startsWith('import React')) continue;
    if (line.startsWith('import ')) {
        if (line.includes('/mathematics/')) {
            importsMath.push(line);
        }
        continue;
    }

    if (line.startsWith('const Grade10')) {
        if (currentRoute.length > 0) {
            if (currentSubject === 'math') routesMath.push(currentRoute.join('\n'));
            currentRoute = [];
        }

        if (line.includes('Grade10BS')) currentSubject = 'bs';
        else if (line.includes('Accounting') || line.includes('Bookkeeping') || line.includes('Ethics') || line.includes('InternalControl') || line.includes('SoleTrader') || line.includes('SalariesWages') || line.includes('FinalAccounts') || line.includes('VAT') || line.includes('Reconciliation') || line.includes('Budgets') || line.includes('CostAccounting') || line.includes('AssetDisposal')) currentSubject = 'acct';
        else currentSubject = 'math';

        currentRoute.push(line);
    } else if (currentRoute.length > 0) {
        currentRoute.push(line);
    }
}

if (currentRoute.length > 0) {
    if (currentSubject === 'math') routesMath.push(currentRoute.join('\n'));
}

const generateFile = (importsSubject, routesSubject, exportsSubject, name) => {
    return `import React, { useEffect, useState } from 'react';
import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../shared/EvaluatedWorkspaceModeShell';
const h = React.createElement;
${importsSubject.join('\n')}

${routesSubject.join('\n')}

export const ${name} = {
${exportsSubject.join('\n')}
};
`;
};

fs.writeFileSync('src/components/workspace/registry/grade10MathematicsRegistry.js', generateFile(importsMath, routesMath, exportsMath, 'grade10MathematicsRegistry'));
console.log('Successfully recovered grade10MathematicsRegistry.js');
