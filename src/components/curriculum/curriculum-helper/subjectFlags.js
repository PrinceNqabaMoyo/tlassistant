export const buildSubjectFlags = ({ selectedGrade, selectedSubject }) => {
    const subjectNameLower = selectedSubject?.name?.toLowerCase?.() || '';
    const gradeString = String(selectedGrade);
    const gradeNumber = parseInt(selectedGrade, 10);

    return {
        subjectNameLower,
        gradeString,
        gradeNumber,
        isGrade7Math:
            gradeString === '7' &&
            (subjectNameLower === 'mathematics' || subjectNameLower === 'math'),
        isGrade8Math:
            gradeString === '8' &&
            (subjectNameLower === 'mathematics' || subjectNameLower === 'math'),
        isGrade9Math:
            gradeString === '9' &&
            (subjectNameLower === 'mathematics' || subjectNameLower === 'math'),
        isGrade10Math:
            gradeString === '10' &&
            (subjectNameLower === 'mathematics' || subjectNameLower === 'math'),
        isGrade10Accounting:
            gradeString === '10' && subjectNameLower.includes('accounting'),
        isGrade10BusinessStudies:
            gradeString === '10' &&
            (subjectNameLower.includes('business studies') || subjectNameLower.includes('business')),
        isGrade11BusinessStudies:
            gradeString === '11' &&
            (subjectNameLower.includes('business studies') || subjectNameLower.includes('business')),
        isGrade11Accounting:
            gradeString === '11' && subjectNameLower.includes('accounting'),
        isGrade12Accounting:
            gradeString === '12' && subjectNameLower.includes('accounting'),
        isGrade11Math:
            gradeNumber === 11 &&
            (subjectNameLower.includes('mathematics') || subjectNameLower.includes('math')),
        isGrade12Math:
            gradeNumber === 12 &&
            (subjectNameLower.includes('mathematics') || subjectNameLower.includes('math')),
    };
};

export const buildAvailableTopics = ({ selectedGrade, selectedSubject }) => {
    const availableTopicsRaw = selectedSubject?.topicsByGrade?.[selectedGrade]?.topics || [];
    let availableTopics = (Array.isArray(availableTopicsRaw) ? availableTopicsRaw : [])
        .map((topic) => (typeof topic === 'string' ? topic : topic?.name))
        .filter(Boolean);

    const subjectNameLower = selectedSubject?.name?.toLowerCase?.() || '';

    const isGrade11AccountingCheck = String(selectedGrade) === '11' && subjectNameLower.includes('accounting');
    if (isGrade11AccountingCheck) {
        const numberedTopics = [
            '1. Ethics and Internal Control',
            '2. Bank Reconciliation',
            '3. Fixed Tangible Assets',
            '4. Partnerships: Analysis of Financial Statements',
            '5. Analysis and Interpretation of financial statements',
            '6. Non profit Organisations or Clubs'
        ];

        const coveredKeywords = [
            'ethics', 'internal control', 'reconciliation', 'fixed', 'tangible', 'assets', 'partnership',
            'analysis', 'interpretation', 'intepretation', 'club', 'non-profit', 'nonprofit'
        ];

        const otherTopics = availableTopics.filter((topicName) => {
            const lower = topicName.toLowerCase();
            return !coveredKeywords.some((keyword) => lower.includes(keyword));
        });

        availableTopics = [...numberedTopics, ...otherTopics];
    }

    const isGrade12AccountingCheck = String(selectedGrade) === '12' && subjectNameLower.includes('accounting');
    if (isGrade12AccountingCheck) {
        availableTopics = [
            '1. Accounting of companies: Concepts',
            '2. Bookkeeping and Unique ledger accounts of Companies',
            '3. Preparation of financial statements of companies',
            '4. Analysis and Interpretation of Financial Statements',
            '5. Audits, Corporate governance and shareholding',
            '6. Fixed / Tangible Assets',
            '7. Inventories',
            '8. Reconciliations',
            '9. Value Added Tax'
        ];
    }

    return availableTopics;
};

export const hasStructuredTopicOrdering = (flags) => (
    flags.isGrade7Math
    || flags.isGrade8Math
    || flags.isGrade9Math
    || flags.isGrade10Math
    || flags.isGrade11Math
    || flags.isGrade12Math
    || flags.isGrade10Accounting
    || flags.isGrade10BusinessStudies
    || flags.isGrade11BusinessStudies
    || flags.isGrade11Accounting
    || flags.isGrade12Accounting
);
