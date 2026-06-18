import { useEffect, useMemo, useState } from 'react';

const normalizeIndigenousSubskill = (subskill) => {
    const key = String(subskill || 'mixed').trim().toLowerCase();
    const mapping = {
        concepts: 'informal_vs_formal',
        concept: 'informal_vs_formal',
        activity_1: 'business_planning',
        activity1: 'business_planning',
        activity_2: 'informal_vs_formal',
        activity2: 'informal_vs_formal',
        compare_systems: 'informal_vs_formal',
    };
    return mapping[key] || key || 'informal_vs_formal';
};

export const useGrade10IndigenousBookkeepingController = ({ workspaceMode, buildApiUrl, currentUser }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');
    const [practiceSubskill, setPracticeSubskill] = useState('informal_vs_formal');

    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('concepts');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'informal_vs_formal', title: 'Informal vs Formal Bookkeeping' },
            { key: 'resource_management', title: 'Resource Management in Informal Businesses' },
            { key: 'business_planning', title: 'Planning an Informal Business' },
            { key: 'pricing_and_markup', title: 'Cost Price, Selling Price and Mark-up' },
            { key: 'labour_income_expenses', title: 'Labour, Income and Expenses' },
        ],
        []
    );

    const subskills = useMemo(
        () => [
            ...scaffoldSteps,
        ],
        [scaffoldSteps]
    );

    const endpointPath = '/api/accounting/grade10/indigenous-bookkeeping/generate';

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const resolvedSubskill = normalizeIndigenousSubskill(subskill || scaffoldSteps?.[scaffoldStepIndex]?.key || 'informal_vs_formal');
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: resolvedSubskill,
                    difficulty: difficulty || 'easy',
                    question_type: 'mixed',
                    count: 1,
                    user_id: currentUser?.uid || null,
                }),
            });

            if (!res.ok) throw new Error(`Grade 10 Accounting Indigenous Bookkeeping scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');

            const q = data?.questions?.[0] || null;
            setScaffoldQuestion(q);
            setScaffoldAnswer(null);
            setScaffoldFeedback(null);
            setScaffoldShowHint(false);
        } catch (err) {
            const msg = err?.message || String(err);
            if (String(msg).toLowerCase().includes('failed to fetch')) {
                setScaffoldError(`Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setScaffoldError(msg);
            }
        } finally {
            setScaffoldLoading(false);
        }
    };

    const fetchPractice = async ({ difficulty, subskill }) => {
        setPracticeLoading(true);
        setPracticeError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const resolvedSubskill = normalizeIndigenousSubskill(subskill || practiceSubskill || 'informal_vs_formal');
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: resolvedSubskill,
                    difficulty: difficulty || 'easy',
                    question_type: 'mixed',
                    count: 8,
                    user_id: currentUser?.uid || null,
                }),
            });

            if (!res.ok) throw new Error(`Grade 10 Accounting Indigenous Bookkeeping practice request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');

            const qs = Array.isArray(data?.questions) ? data.questions : [];
            setPracticeQuestions(qs);
            setPracticeAnswers([]);
            setPracticeFeedback([]);
        } catch (err) {
            const msg = err?.message || String(err);
            if (String(msg).toLowerCase().includes('failed to fetch')) {
                setPracticeError(`Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade10_accounting_indigenous_practice') return;
        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        if (workspaceMode !== 'grade10_accounting_indigenous_scaffold' && workspaceMode !== 'grade10_accounting_indigenous_marking') return;
        const step = scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0];
        fetchScaffoldQuestion({ subskill: step.key, difficulty: scaffoldDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade10_accounting_indigenous_scaffold' || workspaceMode === 'grade10_accounting_indigenous_practice';
        if (!inMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('concepts');
    }, [workspaceMode, visualAidsOpen]);

    return {
        scaffoldSteps,
        subskills,

        practiceQuestions,
        practiceAnswers,
        setPracticeAnswers,
        practiceFeedback,
        setPracticeFeedback,
        practiceLoading,
        practiceError,
        practiceDifficulty,
        setPracticeDifficulty,
        practiceSubskill,
        setPracticeSubskill,
        fetchPractice,

        scaffoldStepIndex,
        setScaffoldStepIndex,
        scaffoldQuestion,
        scaffoldAnswer,
        setScaffoldAnswer,
        scaffoldFeedback,
        setScaffoldFeedback,
        scaffoldShowHint,
        setScaffoldShowHint,
        scaffoldLoading,
        scaffoldError,
        scaffoldDifficulty,
        setScaffoldDifficulty,
        fetchScaffoldQuestion,

        visualAidsOpen,
        setVisualAidsOpen,
        visualAidsTab,
        setVisualAidsTab,
    };
};
