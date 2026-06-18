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
    const m = c.match(/\b([a-zA-Z0-9_]+)\s*,\s*\1\b/);
    if (m) console.log(f, m[0]);
});
