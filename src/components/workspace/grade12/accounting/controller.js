import { useEffect, useMemo, useState } from 'react';

export const useGrade12AccountingController = ({ workspaceMode, buildApiUrl, subskills: customSubskills, defaultSubskill }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');
    const [practiceSubskill, setPracticeSubskill] = useState(defaultSubskill || 'mixed');
    const [practiceSeed, setPracticeSeed] = useState('');

    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');
    const [scaffoldSubskill, setScaffoldSubskill] = useState(defaultSubskill || 'mixed');
    const [scaffoldSeed, setScaffoldSeed] = useState('');

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('overview');

    const subskills = useMemo(
        () => {
            if (customSubskills) return customSubskills;
            return [
                { key: 'mixed', title: 'Mixed (all)' },
                { key: 'concepts', title: 'Concepts (Companies)' },
                { key: 'audits-governance-shareholding', title: 'Audits, Corporate Governance & Shareholding' },
                { key: 'company-general-ledger', title: 'Bookkeeping of companies (General Ledger)' },
                { key: 'financial-statements-notes', title: 'Financial statements & notes (Income Statement)' },
                { key: 'cash-flow', title: 'Cash Flow Statement' },
                { key: 'analysis-interpretation', title: 'Analysis & interpretation of financial statements' },
            ];
        },
        [customSubskills]
    );

    const endpointPath = '/api/accounting/grade12/accounting/generate';

    const fetchScaffoldQuestion = async ({ difficulty, subskill, seed }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const body = {
                mode: 'scaffold',
                subskill: subskill || 'mixed',
                difficulty: difficulty || 'easy',
                question_type: 'mixed',
                count: 1,
            };
            if (seed && String(seed).trim()) {
                body.seed = parseInt(seed, 10);
            }

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body),
            });

            if (!res.ok) throw new Error(`Grade 12 Accounting scaffold request failed: HTTP ${res.status}`);
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

    const fetchPractice = async ({ difficulty, subskill, seed }) => {
        setPracticeLoading(true);
        setPracticeError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const body = {
                mode: 'practice',
                subskill: subskill || 'mixed',
                difficulty: difficulty || 'easy',
                question_type: 'mixed',
                count: 6,
            };
            if (seed && String(seed).trim()) {
                body.seed = parseInt(seed, 10);
            }

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body),
            });

            if (!res.ok) throw new Error(`Grade 12 Accounting practice request failed: HTTP ${res.status}`);
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
        if (workspaceMode !== 'grade12_accounting_practice') return;
        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill, seed: practiceSeed });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade12_accounting_scaffold' || workspaceMode === 'grade12_accounting_practice';
        if (!inMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('overview');
    }, [workspaceMode, visualAidsOpen]);

    return {
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
        practiceSeed,
        setPracticeSeed,
        fetchPractice,

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
        scaffoldSubskill,
        setScaffoldSubskill,
        scaffoldSeed,
        setScaffoldSeed,
        fetchScaffoldQuestion,

        visualAidsOpen,
        setVisualAidsOpen,
        visualAidsTab,
        setVisualAidsTab,
    };
};
