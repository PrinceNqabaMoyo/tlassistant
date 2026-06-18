import {
    Target,
    BookOpen,
    Calculator,
    Brain,
    BrainCircuit,
    FileText,
    FlaskConical,
    Briefcase,
    Building,
    FunctionSquare,
    Atom,
    Beaker,
    Landmark,
    AreaChart,
    BarChart,
    FileJson,
    Users,
    DraftingCompass,
    Sigma,
    Percent,
    Rocket,
} from 'lucide-react';

export const topicColors = [
    'bg-blue-500',
    'bg-green-500',
    'bg-yellow-500',
    'bg-purple-500',
    'bg-pink-500',
    'bg-indigo-500',
    'bg-red-500',
    'bg-gray-500',
];

export const getTopicIcon = (topicName, subjectName) => {
    const topic = String(topicName || '').toLowerCase();
    const subject = String(subjectName || '').toLowerCase();

    if (subject.includes('accounting') || subject.includes('business') || subject.includes('economic')) {
        if (topic.includes('financ') || topic.includes('budget')) return AreaChart;
        if (topic.includes('control') || topic.includes('manage')) return Users;
        if (topic.includes('gaap') || topic.includes('principles')) return Landmark;
        if (topic.includes('bookkeeping') || topic.includes('sole trader')) return Building;
        return BarChart;
    }

    if (subject.includes('math')) {
        if (topic.includes('algebra') || topic.includes('functions')) return FunctionSquare;
        if (topic.includes('geometry') || topic.includes('shape')) return DraftingCompass;
        if (topic.includes('trigonometry')) return Sigma;
        if (topic.includes('exponents') || topic.includes('number')) return Calculator;
        if (topic.includes('probability') || topic.includes('stats')) return Percent;
        return Calculator;
    }

    if (subject.includes('physical science')) {
        if (topic.includes('electric') || topic.includes('magnet')) return Rocket;
        if (topic.includes('wave') || topic.includes('optic')) return Target;
        if (topic.includes('matter') || topic.includes('atom') || topic.includes('bond')) return Atom;
        if (topic.includes('reaction') || topic.includes('chemical')) return FlaskConical;
        return Beaker;
    }

    if (topic.includes('data') || topic.includes('report')) return FileJson;
    if (topic.includes('brain') || topic.includes('thinking')) return Brain;

    return BookOpen;
};

export const getAvailableRepositories = (selectedSubject, selectedGrade, handlers) => {
    const repositories = [];
    const subjectName = String(selectedSubject?.name || '').toLowerCase();
    const grade = parseInt(selectedGrade, 10);

    if (['mathematics', 'mathematical literacy', 'technical mathematics'].includes(subjectName)) {
        repositories.push({
            key: 'math',
            name: 'Math Components',
            icon: Calculator,
            onClick: handlers.openMathComponentsRepository
        });
    }

    if (subjectName === 'physical science' && grade >= 10 && grade <= 12) {
        repositories.push({
            key: 'chemistry',
            name: 'Chemistry Components',
            icon: FileText,
            onClick: handlers.openChemistryComponentsRepository
        });
        repositories.push({
            key: 'physics',
            name: 'Physics Components',
            icon: Target,
            onClick: handlers.openPhysicsComponentsRepository
        });
    }

    repositories.push({
        key: 'cross-disciplinary',
        name: 'Cross-Disciplinary',
        icon: BrainCircuit,
        onClick: handlers.openCrossDisciplinaryComponentsRepository
    });

    return repositories;
};

export const abbreviateSubjectName = (name) => {
    const abbreviations = {
        Mathematics: 'Math',
        'Mathematical Literacy': 'Math Lit',
        'Technical Mathematics': 'Tech Math',
        'Physical Sciences': 'Physics',
        'Life Sciences': 'Biology',
        Accounting: 'Accounting',
        'Business Studies': 'Business',
        'Economic and Management Sciences': 'EMS'
    };
    return abbreviations[name] || name;
};

export const formatGrade = (grade) => `Grade ${grade}`;
