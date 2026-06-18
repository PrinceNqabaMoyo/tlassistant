import { useEffect, useMemo, useState } from 'react';

export const useGrade10SoleTraderController = ({ workspaceMode, buildApiUrl }) => {
    const journalScaffoldPattern = ['activity', 'exam', 'activity', 'exam', 'single'];
    const rotatingJournalSubskills = new Set(['crj', 'cpj', 'dj', 'daj', 'cj', 'caj', 'pcj', 'gj']);
    const controlAccountsPracticeKeys = new Set(['control_accounts', 'control_accounts_reconciliation', 'reconciliation_analysis']);
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');
    const [practiceSubskill, setPracticeSubskill] = useState('concepts');
    const [practiceSeed, setPracticeSeed] = useState(''); // Debug seed for deterministic generation

    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');
    const [scaffoldSubskill, setScaffoldSubskill] = useState('concepts');
    const [scaffoldSeed, setScaffoldSeed] = useState(''); // Debug seed for deterministic generation
    const [journalScaffoldMixIndex, setJournalScaffoldMixIndex] = useState({ crj: 0, cpj: 0, dj: 0, daj: 0, cj: 0, caj: 0, pcj: 0, gj: 0 });

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('overview');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'concepts', title: 'Accounting concepts & principles' },
            { key: 'equation', title: 'Analysis of transactions using the accounting equation' },
            { key: 'journals', title: 'Journals (CRJ/CPJ)' },
            { key: 'gj', title: 'General Journal (GJ)' },
            { key: 'general_ledger', title: 'General Ledger (posting)' },
            { key: 'debtors_ledger', title: 'Debtors Ledger (posting)' },
            { key: 'creditors_ledger', title: 'Creditors Ledger (posting)' },
            { key: 'trading_stock_account', title: 'Trading stock account' },
            { key: 'control_accounts', title: 'Control accounts' },
            { key: 'control_accounts_reconciliation', title: 'Control accounts reconciliation' },
            { key: 'reconciliation_analysis', title: 'Reconciliation analysis' },
            { key: 'trial_balance', title: 'Trial Balance' },
            { key: 'full_accounting_cycle_bookkeeping', title: 'Project: Accounting cycle bookkeeping' },
        ],
        []
    );

    const subskills = useMemo(
        () => [
            { key: 'concepts', title: 'Accounting concepts & principles' },
            { key: 'equation', title: 'Analysis of transactions using the accounting equation' },
            { key: 'crj', title: 'Cash Receipts Journal (CRJ)' },
            { key: 'cpj', title: 'Cash Payments Journal (CPJ)' },
            { key: 'dj', title: 'Debtors Journal (DJ)' },
            { key: 'daj', title: 'Debtors Allowances Journal (DAJ)' },
            { key: 'cj', title: 'Creditors Journal (CJ)' },
            { key: 'caj', title: 'Creditors Allowances Journal (CAJ)' },
            { key: 'pcj', title: 'Petty Cash Journal (PCJ)' },
            { key: 'gj', title: 'General Journal (GJ)' },
            { key: 'general_ledger', title: 'General Ledger (posting)' },
            { key: 'debtors_ledger', title: 'Debtors Ledger (posting)' },
            { key: 'creditors_ledger', title: 'Creditors Ledger (posting)' },
            { key: 'trading_stock_account', title: 'Trading stock account' },
            { key: 'control_accounts', title: 'Control accounts' },
            { key: 'control_accounts_reconciliation', title: 'Control accounts reconciliation' },
            { key: 'reconciliation_analysis', title: 'Reconciliation analysis' },
            { key: 'trial_balance', title: 'Trial Balance' },
            { key: 'full_accounting_cycle_bookkeeping', title: 'Project: Accounting cycle bookkeeping' },
            { key: 'journals', title: 'Journals (any)' },
            { key: 'mixed', title: 'Mixed (all)' },
        ],
        []
    );

    const endpointPath = '/api/accounting/grade10/sole-trader/generate';

    const fetchScaffoldQuestion = async ({ subskill, difficulty, seed, question_type }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const subskillKey = String(subskill || 'mixed').trim().toLowerCase();
            const explicitQuestionType = String(question_type || 'mixed').trim().toLowerCase();
            const useJournalRotation = rotatingJournalSubskills.has(subskillKey) && explicitQuestionType === 'mixed';
            const resolvedQuestionType = useJournalRotation
                ? journalScaffoldPattern[(journalScaffoldMixIndex[subskillKey] || 0) % journalScaffoldPattern.length]
                : (question_type || 'mixed');
            const body = {
                mode: 'scaffold',
                subskill: subskill || 'mixed',
                difficulty: difficulty || 'easy',
                question_type: resolvedQuestionType,
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

            if (!res.ok) throw new Error(`Grade 10 Accounting Sole Trader scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');

            const q = data?.questions?.[0] || null;
            setScaffoldQuestion(q);
            setScaffoldAnswer(null);
            setScaffoldFeedback(null);
            setScaffoldShowHint(false);
            if (useJournalRotation) {
                setJournalScaffoldMixIndex((prev) => ({
                    ...prev,
                    [subskillKey]: (prev[subskillKey] || 0) + 1,
                }));
            }
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

    const fetchPractice = async ({ difficulty, subskill, seed, question_type }) => {
        setPracticeLoading(true);
        setPracticeError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const parsedSeed = (seed && String(seed).trim()) ? parseInt(seed, 10) : null;
            const practiceCount = Number.isInteger(parsedSeed)
                ? 6 + (Math.abs(parsedSeed) % 5)
                : 8;
            const body = {
                mode: 'practice',
                subskill: subskill || 'mixed',
                difficulty: difficulty || 'easy',
                question_type: question_type || 'mixed',
                count: practiceCount,
            };
            if (Number.isInteger(parsedSeed)) {
                body.seed = parsedSeed;
            }
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body),
            });

            if (!res.ok) throw new Error(`Grade 10 Accounting Sole Trader practice request failed: HTTP ${res.status}`);
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
        if (workspaceMode !== 'grade8_ems_sole_trader_practice') return;
        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill, seed: practiceSeed });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        if (controlAccountsPracticeKeys.has(practiceSubskill) && practiceDifficulty === 'easy') {
            setPracticeDifficulty('hard');
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [practiceSubskill]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade8_ems_sole_trader_scaffold' || workspaceMode === 'grade8_ems_sole_trader_practice';
        if (!inMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('overview');
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
        practiceSeed,
        setPracticeSeed,
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


// Alias to match the name expected by grade8EmsRegistry (module was a copy-paste stub).
export const useGrade8EmsController = useGrade10SoleTraderController;
