import { useEffect, useMemo, useState } from 'react';

const normalizeVatSubskill = (subskill) => {
    const key = String(subskill || 'mixed').trim().toLowerCase();
    const mapping = {
        vat_concepts: 'concepts',
        vat_calculations: 'calculations',
        vat_classification: 'classification',
        vat_ethics: 'ethics',
    };
    return mapping[key] || key || 'mixed';
};

export const useGrade10VATController = ({ workspaceMode, buildApiUrl }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');
    const [practiceSubskill, setPracticeSubskill] = useState('mixed');
    const [practiceSeed, setPracticeSeed] = useState('');

    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');
    const [scaffoldSubskill, setScaffoldSubskill] = useState('concepts');
    const [scaffoldSeed, setScaffoldSeed] = useState('');

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('overview');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'concepts', title: 'VAT concepts (rate, registration, terminology)' },
            { key: 'calculations', title: 'VAT calculations (inclusive/exclusive)' },
            { key: 'classification', title: 'Classification of supplies (taxable/exempt/zero-rated)' },
            { key: 'ethics', title: 'Tax evasion vs avoidance & ethics' },
        ],
        []
    );

    const subskills = useMemo(
        () => [
            { key: 'mixed', title: 'Mixed (all)' },
            { key: 'concepts', title: 'VAT concepts' },
            { key: 'calculations', title: 'VAT calculations' },
            { key: 'classification', title: 'Supply classification' },
            { key: 'ethics', title: 'Tax ethics' },
        ],
        []
    );

    const endpointPath = '/api/accounting/grade10/accounting/generate';

    const fetchScaffoldQuestion = async ({ subskill, difficulty, seed }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const resolvedSubskill = normalizeVatSubskill(subskill || scaffoldSubskill || 'concepts');
            const body = { mode: 'scaffold', topic: 'vat', subskill: resolvedSubskill, difficulty: difficulty || 'easy', question_type: 'mixed', count: 1 };
            if (seed && String(seed).trim()) body.seed = parseInt(seed, 10);
            const res = await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
            if (!res.ok) throw new Error(`Grade 10 VAT scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');
            setScaffoldQuestion(data?.questions?.[0] || null);
            setScaffoldAnswer(null);
            setScaffoldFeedback(null);
            setScaffoldShowHint(false);
        } catch (err) {
            const msg = err?.message || String(err);
            setScaffoldError(String(msg).toLowerCase().includes('failed to fetch') ? `Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running.` : msg);
        } finally { setScaffoldLoading(false); }
    };

    const fetchPractice = async ({ difficulty, subskill, seed }) => {
        setPracticeLoading(true);
        setPracticeError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const resolvedSubskill = normalizeVatSubskill(subskill || practiceSubskill || 'mixed');
            const body = { mode: 'practice', topic: 'vat', subskill: resolvedSubskill, difficulty: difficulty || 'easy', question_type: 'mixed', count: 8 };
            if (seed && String(seed).trim()) body.seed = parseInt(seed, 10);
            const res = await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
            if (!res.ok) throw new Error(`Grade 10 VAT practice request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');
            setPracticeQuestions(Array.isArray(data?.questions) ? data.questions : []);
            setPracticeAnswers([]);
            setPracticeFeedback([]);
        } catch (err) {
            const msg = err?.message || String(err);
            setPracticeError(String(msg).toLowerCase().includes('failed to fetch') ? `Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running.` : msg);
        } finally { setPracticeLoading(false); }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade10_accounting_vat_practice') return;
        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill, seed: practiceSeed });
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade10_accounting_vat_scaffold' || workspaceMode === 'grade10_accounting_vat_practice';
        if (!inMode || !visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('overview');
    }, [workspaceMode, visualAidsOpen]);

    return {
        scaffoldSteps, subskills,
        practiceQuestions, practiceAnswers, setPracticeAnswers, practiceFeedback, setPracticeFeedback,
        practiceLoading, practiceError, practiceDifficulty, setPracticeDifficulty,
        practiceSubskill, setPracticeSubskill, practiceSeed, setPracticeSeed, fetchPractice,
        scaffoldStepIndex, setScaffoldStepIndex, scaffoldQuestion, scaffoldAnswer, setScaffoldAnswer,
        scaffoldFeedback, setScaffoldFeedback, scaffoldShowHint, setScaffoldShowHint,
        scaffoldLoading, scaffoldError, scaffoldDifficulty, setScaffoldDifficulty,
        scaffoldSubskill, setScaffoldSubskill, scaffoldSeed, setScaffoldSeed, fetchScaffoldQuestion,
        visualAidsOpen, setVisualAidsOpen, visualAidsTab, setVisualAidsTab,
    };
};
