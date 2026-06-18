import { useEffect, useMemo, useState } from 'react';

export const useGrade10InternalControlController = ({ workspaceMode, buildApiUrl }) => {
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
    const [visualAidsTab, setVisualAidsTab] = useState('overview');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'definition', title: 'Definition' },
            { key: 'processes', title: 'Control process' },
            { key: 'stock', title: 'Stock control' },
            { key: 'debtors', title: 'Debtors control' },
            { key: 'creditors', title: 'Creditors control' },
            { key: 'fixed_assets', title: 'Fixed assets' },
            { key: 'consumables', title: 'Consumable goods' },
            { key: 'cash', title: 'Cash control (CRJ/CPJ/PCJ)' },
            { key: 'activity_1', title: 'Activity (scenario)' },
        ],
        []
    );

    const endpointPath = '/api/accounting/grade10/internal-control/generate';

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

            if (!res.ok) throw new Error(`Grade 10 Accounting Internal Control scaffold request failed: HTTP ${res.status}`);
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
            
            // 8-question timed flow:
            // 2 definitions/processes, 5 topic questions (stock, debtors, creditors, fixed assets, consumables, cash), 1 activity
            const definitionsReq = fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ subskill: 'processes', difficulty: difficulty || 'easy', count: 2 }),
            }).then(r => r.json());

            const mixedReq = fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ subskill: 'mixed', difficulty: difficulty || 'easy', count: 5 }),
            }).then(r => r.json());

            const activityReq = fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ subskill: 'activity_1', difficulty: difficulty || 'easy', count: 1 }),
            }).then(r => r.json());

            const [defRes, mixedRes, actRes] = await Promise.all([definitionsReq, mixedReq, activityReq]);

            if (!defRes?.success) throw new Error(defRes?.error || 'Generation failed');
            if (!mixedRes?.success) throw new Error(mixedRes?.error || 'Generation failed');
            if (!actRes?.success) throw new Error(actRes?.error || 'Generation failed');

            const allQs = [
                ...(defRes.questions || []),
                ...(mixedRes.questions || []),
                ...(actRes.questions || []),
            ];

            // In case we don't get exactly 8, we just use what we get. Usually it will be 2 + 5 + 1 = 8.
            setPracticeQuestions(allQs);
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
        if (workspaceMode !== 'grade10_accounting_internal_control_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade10_accounting_internal_control_scaffold' || workspaceMode === 'grade10_accounting_internal_control_practice';
        if (!inMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('overview');
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
