const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'src/components/workspace/registry/grade10Registry - Copy.js');
const content = fs.readFileSync(filePath, 'utf8');

const lines = content.split('\n');

const importsMath = [];
const importsAcct = [];
const importsBS = [];
const importsShared = [];

const routesMath = [];
const routesAcct = [];
const routesBS = [];

const exportsMath = [];
const exportsAcct = [];
const exportsBS = [];

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
                if (block.includes('grade10_bs_')) exportsBS.push(block + (block.trim().endsWith(',') ? '' : ','));
                else if (block.includes('grade10_accounting_') || block.includes('grade10_bookkeeping_') || block.includes('grade10_general_ledger') || block.includes('grade10_trial_balance') || block.includes('grade10_financial_statements') || block.includes('grade10_salary_journals') || block.includes('grade10_wages_journals')) exportsAcct.push(block + (block.trim().endsWith(',') ? '' : ','));
                else exportsMath.push(block + (block.trim().endsWith(',') ? '' : ','));
                currentExport = [];
            }
            continue;
        }

        if (line.trim().startsWith('grade10_')) {
            if (currentExport.length > 0) {
                const block = currentExport.join('\n');
                if (block.includes('grade10_bs_')) exportsBS.push(block + (block.trim().endsWith(',') ? '' : ','));
                else if (block.includes('grade10_accounting_') || block.includes('grade10_bookkeeping_') || block.includes('grade10_general_ledger') || block.includes('grade10_trial_balance') || block.includes('grade10_financial_statements') || block.includes('grade10_salary_journals') || block.includes('grade10_wages_journals')) exportsAcct.push(block + (block.trim().endsWith(',') ? '' : ','));
                else exportsMath.push(block + (block.trim().endsWith(',') ? '' : ','));
                currentExport = [];
            }
        }
        
        currentExport.push(line);
        continue;
    }

    if (line.startsWith('import React')) continue;
    if (line.startsWith('import ')) {
        if (line.includes('/business-studies/')) {
            importsBS.push(line);
        } else if (line.includes('/accounting/')) {
            importsAcct.push(line);
        } else if (line.includes('/mathematics/')) {
            importsMath.push(line);
        } else {
            importsShared.push(line);
        }
        continue;
    }

    if (line.startsWith('const Grade10')) {
        if (currentRoute.length > 0) {
            if (currentSubject === 'bs') routesBS.push(currentRoute.join('\n'));
            else if (currentSubject === 'acct') routesAcct.push(currentRoute.join('\n'));
            else if (currentSubject === 'math') routesMath.push(currentRoute.join('\n'));
            currentRoute = [];
        }

        if (line.includes('Grade10BS')) currentSubject = 'bs';
        else if (line.includes('Accounting') || line.includes('Bookkeeping') || line.includes('Ethics') || line.includes('InternalControl') || line.includes('SoleTrader') || line.includes('SalariesWages') || line.includes('FinalAccounts') || line.includes('VAT') || line.includes('Reconciliation') || line.includes('Budgets') || line.includes('CostAccounting') || line.includes('AssetDisposal')) currentSubject = 'acct';
        else currentSubject = 'math';

        currentRoute.push(line);
    } else if (currentRoute.length > 0) {
        currentRoute.push(line);
    } else if (line.startsWith('const h = React.createElement;')) {
        importsShared.push(line);
    }
}

if (currentRoute.length > 0) {
    if (currentSubject === 'bs') routesBS.push(currentRoute.join('\n'));
    else if (currentSubject === 'acct') routesAcct.push(currentRoute.join('\n'));
    else if (currentSubject === 'math') routesMath.push(currentRoute.join('\n'));
}

const generateFile = (importsSubject, routesSubject, exportsSubject, name) => {
    return `import React, { useEffect, useState } from 'react';
${importsShared.join('\n')}
${importsSubject.join('\n')}

${routesSubject.join('\n')}

export const ${name} = {
${exportsSubject.join('\n')}
};
`;
};

fs.writeFileSync(path.join(__dirname, 'src/components/workspace/registry/grade10MathematicsRegistry.js'), generateFile(importsMath, routesMath, exportsMath, 'grade10MathematicsRegistry'));
fs.writeFileSync(path.join(__dirname, 'src/components/workspace/registry/grade10AccountingRegistry.js'), generateFile(importsAcct, routesAcct, exportsAcct, 'grade10AccountingRegistry'));
fs.writeFileSync(path.join(__dirname, 'src/components/workspace/registry/grade10BusinessStudiesRegistry.js'), generateFile(importsBS, routesBS, exportsBS, 'grade10BusinessStudiesRegistry'));

const mainRegistry = `import { grade10MathematicsRegistry } from './grade10MathematicsRegistry';
import { grade10AccountingRegistry } from './grade10AccountingRegistry';
import { grade10BusinessStudiesRegistry } from './grade10BusinessStudiesRegistry';

export const grade10Registry = {
    ...grade10MathematicsRegistry,
    ...grade10AccountingRegistry,
    ...grade10BusinessStudiesRegistry,
};
`;

fs.writeFileSync(path.join(__dirname, 'src/components/workspace/registry/grade10Registry.js'), mainRegistry);

console.log('Successfully refactored grade10Registry.js');
