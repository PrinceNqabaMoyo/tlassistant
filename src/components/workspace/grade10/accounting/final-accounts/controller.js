import { useEffect, useMemo, useState } from 'react';

export const useGrade10FinalAccountsController = ({ workspaceMode, buildApiUrl }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');
    const [practiceSubskill, setPracticeSubskill] = useState('closing_transfers');
    const [practiceSeed, setPracticeSeed] = useState('');
    const [practiceRotationOrdinals, setPracticeRotationOrdinals] = useState({});

    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');
    const [scaffoldSubskill, setScaffoldSubskill] = useState('closing_transfers');
    const [scaffoldSeed, setScaffoldSeed] = useState('');
    const [scaffoldRotationOrdinals, setScaffoldRotationOrdinals] = useState({});

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('overview');

    const getRotationOrdinal = (rotationMap, subskillKey) => {
        const value = rotationMap?.[subskillKey];
        return Number.isFinite(value) && value >= 0 ? value : 0;
    };

    const advanceRotationOrdinal = (setter, subskillKey, increment) => {
        const normalizedIncrement = Math.max(0, Number(increment) || 0);
        if (!subskillKey || normalizedIncrement < 1) return;
        setter((prev) => {
            const current = getRotationOrdinal(prev, subskillKey);
            return {
                ...prev,
                [subskillKey]: current + normalizedIncrement,
            };
        });
    };

    const scaffoldSteps = useMemo(
        () => [
            { key: 'closing_transfers', title: 'Closing transfers & year-end process' },
            { key: 'depreciation', title: 'Depreciation (straight-line & diminishing balance)' },
            { key: 'asset_register', title: 'Asset registers' },
            { key: 'ledger_posting', title: 'Ledger posting of depreciation' },
            { key: 'interest_adjustments', title: 'Interest adjustments' },
            { key: 'consumable_stores_on_hand', title: 'Consumable stores on hand' },
            { key: 'adjustments', title: 'Year-end adjustments' },
            { key: 'adjustment_journal', title: 'General Journal adjustments' },
            { key: 'error_corrections_and_reclassification', title: 'Error corrections & reclassification' },
            { key: 'adjustment_analysis', title: 'Adjustment analysis tables' },
            { key: 'accrued_income_and_reversals', title: 'Accrued income & reversals' },
            { key: 'accrued_expenses_and_reversals', title: 'Accrued expenses & reversals' },
            { key: 'prepaid_expenses_and_reversals', title: 'Prepaid expenses & reversals' },
            { key: 'income_received_in_advance_and_reversals', title: 'Income received in advance & reversals' },
            { key: 'reversals', title: 'Mixed reversals ledger practice' },
            { key: 'income_statement', title: 'Trading & Profit and Loss accounts' },
            { key: 'final_accounts_trading_account', title: 'Trading Account' },
            { key: 'final_accounts_profit_and_loss', title: 'Profit and Loss Account' },
            { key: 'final_accounts_table', title: 'Final accounts fill-in tables' },
            { key: 'integrated_final_accounts', title: 'Integrated multipart final accounts' },
            { key: 'post_adjustment_trial_balance', title: 'Post-adjustment Trial Balance' },
            { key: 'trial_balance', title: 'Trial balances & reversals' },
            { key: 'post_closing_trial_balance', title: 'Post-closing Trial Balance fill-in' },
        ],
        []
    );

    const subskills = scaffoldSteps;

    const endpointPath = '/api/accounting/grade10/accounting/generate';

    const fetchScaffoldQuestion = async ({ subskill, difficulty, seed }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const resolvedSubskill = subskill || scaffoldSubskill || scaffoldSteps[scaffoldStepIndex]?.key || 'closing_transfers';
            const body = {
                mode: 'scaffold',
                topic: 'final-accounts',
                subskill: resolvedSubskill,
                difficulty: difficulty || 'easy',
                question_type: 'mixed',
                count: 1,
                rotation_ordinal: getRotationOrdinal(scaffoldRotationOrdinals, resolvedSubskill),
            };
            if (seed && String(seed).trim()) body.seed = parseInt(seed, 10);
            const res = await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
            if (!res.ok) throw new Error(`Grade 10 Final Accounts scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');
            const nextQuestions = Array.isArray(data?.questions) ? data.questions : [];
            setScaffoldQuestion(nextQuestions[0] || null);
            setScaffoldAnswer(null);
            setScaffoldFeedback(null);
            setScaffoldShowHint(false);
            advanceRotationOrdinal(setScaffoldRotationOrdinals, resolvedSubskill, nextQuestions.length);
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
            const resolvedSubskill = subskill || practiceSubskill || scaffoldSteps[0]?.key || 'closing_transfers';
            const body = {
                mode: 'practice',
                topic: 'final-accounts',
                subskill: resolvedSubskill,
                difficulty: difficulty || 'easy',
                question_type: 'mixed',
                count: 8,
                rotation_ordinal: getRotationOrdinal(practiceRotationOrdinals, resolvedSubskill),
            };
            if (seed && String(seed).trim()) body.seed = parseInt(seed, 10);
            const res = await fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
            if (!res.ok) throw new Error(`Grade 10 Final Accounts practice request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');
            const nextQuestions = Array.isArray(data?.questions) ? data.questions : [];
            setPracticeQuestions(nextQuestions);
            setPracticeAnswers([]);
            setPracticeFeedback([]);
            advanceRotationOrdinal(setPracticeRotationOrdinals, resolvedSubskill, nextQuestions.length);
        } catch (err) {
            const msg = err?.message || String(err);
            setPracticeError(String(msg).toLowerCase().includes('failed to fetch') ? `Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running.` : msg);
        } finally { setPracticeLoading(false); }
    };

    useEffect(() => {
        const nextSubskill = scaffoldSteps[scaffoldStepIndex]?.key || 'closing_transfers';
        setScaffoldSubskill(nextSubskill);
        setScaffoldQuestion(null);
        setScaffoldAnswer(null);
        setScaffoldFeedback(null);
        setScaffoldShowHint(false);
    }, [scaffoldStepIndex, scaffoldSteps]);

    useEffect(() => {
        if (workspaceMode !== 'grade10_accounting_final_accounts_practice') return;
        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill, seed: practiceSeed });
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade10_accounting_final_accounts_scaffold' || workspaceMode === 'grade10_accounting_final_accounts_practice';
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
