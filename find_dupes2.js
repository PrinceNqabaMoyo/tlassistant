const fs = require('fs');
const path = require('path');

const walkSync = (dir, filelist = []) => {
    fs.readdirSync(dir).forEach(file => {
        const dirFile = path.join(dir, file);
        if (fs.statSync(dirFile).isDirectory()) {
            filelist = walkSync(dirFile, filelist);
        } else if (file.endsWith('.jsx') || file.endsWith('.js')) {
            filelist.push(dirFile);
        }
    });
    return filelist;
};

const files = walkSync('src/components/workspace/grade10/accounting');
files.forEach(f => {
    const c = fs.readFileSync(f, 'utf8');

    // Check component params
    const match = c.match(/const [a-zA-Z0-9_]+ = \(\{([\s\S]*?)\}\) =>/);
    if (match) {
        const paramsStr = match[1];
        const params = paramsStr.split(',').map(p => p.trim().split('=')[0].trim()).filter(Boolean);
        const set = new Set();
        params.forEach(p => {
            if (set.has(p)) {
                console.log('DUPLICATE PARAM IN:', f, '->', p);
            }
            set.add(p);
        });
    }

    // Check for standard function duplicate params like (row, row) or (cell, cIdx, cell)
    const arrowFuncs = [...c.matchAll(/\(([^)]+)\)\s*=>/g)];
    arrowFuncs.forEach(m => {
        const argsStr = m[1];
        const args = argsStr.split(',').map(a => a.trim().split('=')[0].trim()).filter(a => a && a !== '...' && !a.includes('{') && !a.includes('['));
        const set = new Set();
        args.forEach(a => {
            if (set.has(a)) {
                console.log('DUPLICATE ARROW PARAM IN:', f, '->', a, 'in', argsStr);
            }
            set.add(a);
        });
    });
});
