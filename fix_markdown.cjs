const fs = require('fs');

function findJsx(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = dir + '/' + file;
    if (fs.statSync(fullPath).isDirectory()) {
      findJsx(fullPath, fileList);
    } else if (fullPath.endsWith('.jsx')) {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

const allJsx = findJsx('src/components/workspace/grade10/business-studies');
allJsx.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  if (content.includes('react-markdown')) {
    content = content.replace(/import ReactMarkdown from 'react-markdown';\r?\n/, '');
    content = content.replace(/<ReactMarkdown>({[^}]+})<\/ReactMarkdown>/g, '<div className=\"whitespace-pre-wrap\">$1</div>');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(file, content);
    console.log('Fixed markdown in', file);
  }
});
