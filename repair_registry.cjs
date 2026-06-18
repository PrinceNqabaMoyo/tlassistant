const fs = require('fs');
const filePath = 'src/components/workspace/registry/grade10AccountingRegistry.js';
let content = fs.readFileSync(filePath, 'utf8');

// Fix double commas
content = content.replace(/\},,/g, '},');

// Fix double React import
content = content.replace(
    /import React, \{ useEffect, useState \} from 'react';\r?\nimport React, \{ useEffect, useState \} from 'react';/,
    "import React, { useEffect, useState } from 'react';"
);

fs.writeFileSync(filePath, content);
console.log('Fixed syntax errors in grade10AccountingRegistry.js');
