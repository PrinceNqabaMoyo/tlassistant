const fs = require('fs');
const path = require('path');

const curriculumPath = path.join(__dirname, 'src', 'components', 'curriculum', 'CurriculumHelper.jsx');
let code = fs.readFileSync(curriculumPath, 'utf8');

if (!code.includes('isGrade10BSConceptOfQuality = (name)')) {
    code = code.replace(
        'const isGrade10BSFormsOfOwnership = (name) => {',
        `const isGrade10BSConceptOfQuality = (name) => {
        const n = String(name || '').toLowerCase();
        return n.includes('concept') && n.includes('quality');
    };

    const isGrade10BSFormsOfOwnership = (name) => {`
    );
    fs.writeFileSync(curriculumPath, code);
    console.log('Successfully added definition for isGrade10BSConceptOfQuality');
} else {
    console.log('Definition already present');
}
