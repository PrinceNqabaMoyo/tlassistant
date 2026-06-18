const fs = require('fs');
const path = require('path');

const curriculumPath = path.join(__dirname, 'src', 'components', 'curriculum', 'CurriculumHelper.jsx');
let code = fs.readFileSync(curriculumPath, 'utf8');

if (!code.includes('isGrade10BSConceptOfQuality')) {
    code = code.replace(
        'const isGrade10BSFormsOfOwnership = (name) => {',
        `const isGrade10BSConceptOfQuality = (name) => {
        const n = String(name || '').toLowerCase();
        return n.includes('concept') && n.includes('quality');
    };

    const isGrade10BSFormsOfOwnership = (name) => {`
    );

    code = code.replace(
        "if (isGrade10BSFormsOfOwnership(topicName)) return 'grade10_bs_forms_of_ownership_scaffold';",
        "if (isGrade10BSFormsOfOwnership(topicName)) return 'grade10_bs_forms_of_ownership_scaffold';\n            if (isGrade10BSConceptOfQuality(topicName)) return 'grade10_bs_concept_of_quality_scaffold';"
    );

    code = code.replace(
        "if (isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(topicName)) return 'Forms of ownership';",
        "if (isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(topicName)) return 'Forms of ownership';\n        if (isGrade10BusinessStudies && isGrade10BSConceptOfQuality(topicName)) return 'The concept of quality';"
    );

    const uiCard = `                    {isGrade10BusinessStudies && isGrade10BSConceptOfQuality(selectedTopic.name) && (
                        <div className="mb-6 bg-indigo-50 border border-indigo-200 rounded-lg p-4">
                            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                                <div>
                                    <h4 className="font-semibold text-indigo-900">Topic 11: Concept of Quality</h4>
                                    <p className="text-sm text-indigo-800">Term 2. Quality control vs quality assurance, SABS, ISO, and total quality management (TQM).</p>
                                </div>
                                <div className="flex flex-col sm:flex-row gap-2">
                                    <button
                                        onClick={() => navigateToWorkspaceWithMode('grade10_bs_concept_of_quality_scaffold', 'Concept of Quality • Scaffold')}
                                        className="px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700"
                                    >
                                        Start Scaffold
                                    </button>
                                    <button
                                        onClick={() => navigateToWorkspaceWithMode('grade10_bs_concept_of_quality_practice', 'Concept of Quality • Practice')}
                                        className="px-4 py-2 bg-white text-indigo-700 border border-indigo-300 rounded-lg font-semibold hover:bg-indigo-50"
                                    >
                                        Start Practice
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}`;

    code = code.replace(
        '{isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(selectedTopic.name) && (',
        uiCard + '\n\n                    {isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(selectedTopic.name) && ('
    );

    fs.writeFileSync(curriculumPath, code);
    console.log('Successfully patched CurriculumHelper.jsx');
} else {
    console.log('Already patched CurriculumHelper.jsx');
}
