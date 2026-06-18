import { useEffect, useMemo, useState } from 'react';

export const useGrade10SalariesWagesController = ({ workspaceMode, buildApiUrl }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');
    const [practiceSubskill, setPracticeSubskill] = useState('salary_scales');
    const [practiceSeed, setPracticeSeed] = useState('');

    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');
    const [scaffoldSubskill, setScaffoldSubskill] = useState('salary_scales');
    const [scaffoldSeed, setScaffoldSeed] = useState('');

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('overview');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'salary_scales', title: 'Salary scales (notch/annual/monthly)' },
            { key: 'wages_calc', title: 'Gross wage calculation (ordinary + overtime)' },
            { key: 'deductions', title: 'Deductions (PAYE, pension, medical, UIF)' },
            { key: 'employer_contributions', title: 'Employer contributions (SDL, UIF, medical, pension)' },
            { key: 'salary_journal', title: 'Complete the Salary Journal' },
            { key: 'wage_journal', title: 'Complete the Wage Journal' },
            { key: 'general_ledger', title: 'Post to General Ledger' },
            { key: 'glossary', title: 'Glossary, abbreviations and concepts' },
            { key: 'ethics', title: 'Ethics and internal control' },
        ],
        []
    );

    const subskills = useMemo(
        () => [
            { key: 'salary_scales', title: 'Salary scales' },
            { key: 'wages_calc', title: 'Wage calculations' },
            { key: 'deductions', title: 'Deductions' },
            { key: 'employer_contributions', title: 'Employer contributions' },
            { key: 'salary_journal', title: 'Salary Journal' },
            { key: 'wage_journal', title: 'Wage Journal' },
            { key: 'general_ledger', title: 'General Ledger posting' },
            { key: 'glossary', title: 'Glossary and concepts' },
            { key: 'ethics', title: 'Ethics and internal control' },
        ],
        []
    );

    const endpointPath = '/api/accounting/grade10/accounting/generate';

    const fetchScaffoldQuestion = async ({ subskill, difficulty, seed }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl(endpointPath);
            const body = {
                mode: 'scaffold',
                topic: 'salaries-wages',
                subskill: subskill || scaffoldSubskill || 'salary_scales',
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

            if (!res.ok) throw new Error(`Grade 10 Salaries & Wages scaffold request failed: HTTP ${res.status}`);
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
                setScaffoldError(`Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running.`);
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
                topic: 'salaries-wages',
                subskill: subskill || practiceSubskill || 'salary_scales',
                difficulty: difficulty || 'easy',
                question_type: 'mixed',
                count: 8,
            };
            if (seed && String(seed).trim()) {
                body.seed = parseInt(seed, 10);
            }
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body),
            });

            if (!res.ok) throw new Error(`Grade 10 Salaries & Wages practice request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');

            const qs = Array.isArray(data?.questions) ? data.questions : [];
            setPracticeQuestions(qs);
            setPracticeAnswers([]);
            setPracticeFeedback([]);
        } catch (err) {
            const msg = err?.message || String(err);
            if (String(msg).toLowerCase().includes('failed to fetch')) {
                setPracticeError(`Failed to fetch (${buildApiUrl(endpointPath)}). Check backend is running.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade10_accounting_salaries_wages_practice') return;
        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill, seed: practiceSeed });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const nextSubskill = scaffoldSteps[scaffoldStepIndex]?.key || 'salary_scales';
        if (scaffoldSubskill !== nextSubskill) {
            setScaffoldSubskill(nextSubskill);
        }
        setScaffoldQuestion(null);
        setScaffoldAnswer(null);
        setScaffoldFeedback(null);
        setScaffoldShowHint(false);
    }, [scaffoldStepIndex, scaffoldSteps, scaffoldSubskill]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade10_accounting_salaries_wages_scaffold' || workspaceMode === 'grade10_accounting_salaries_wages_practice';
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
