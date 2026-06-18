import { useEffect, useMemo, useState } from 'react';

export const useGrade10EthicsController = ({ workspaceMode, buildApiUrl }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');

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
            { key: 'ethics', title: 'Ethics' },
        ],
        []
    );

    const endpointPath = '/api/accounting/grade10/ethics/generate';

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: subskill || 'mixed',
                    difficulty: difficulty || 'easy',
                    question_type: 'mixed',
                    count: 1,
                }),
            });

            if (!res.ok) throw new Error(`Grade 10 Accounting Ethics scaffold request failed: HTTP ${res.status}`);
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

    const fetchPractice = async ({ difficulty }) => {
        setPracticeLoading(true);
        setPracticeError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'mixed',
                    difficulty: difficulty || 'easy',
                    question_type: 'mixed',
                    count: 8,
                }),
            });

            if (!res.ok) throw new Error(`Grade 10 Accounting Ethics practice request failed: HTTP ${res.status}`);
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
        if (workspaceMode !== 'grade10_accounting_ethics_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade10_accounting_ethics_scaffold' || workspaceMode === 'grade10_accounting_ethics_practice';
        if (!inMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('concepts');
    }, [workspaceMode, visualAidsOpen]);

    return {
        scaffoldSteps,

        practiceQuestions,
        practiceAnswers,
        setPracticeAnswers,
        practiceFeedback,
        setPracticeFeedback,
        practiceLoading,
        practiceError,
        practiceDifficulty,
        setPracticeDifficulty,
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
