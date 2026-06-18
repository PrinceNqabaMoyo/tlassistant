import { useEffect, useMemo, useState } from 'react';

export const useGrade9AlgebraicEquations1Controller = ({ workspaceMode, buildApiUrl }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState([]);
    const [practiceFeedback, setPracticeFeedback] = useState([]);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('easy');

    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState('');
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('easy');

    const [scaffoldCheckpointIndex, setScaffoldCheckpointIndex] = useState(0);
    const [scaffoldCheckpointAnswers, setScaffoldCheckpointAnswers] = useState({});
    const [scaffoldCheckpointFeedback, setScaffoldCheckpointFeedback] = useState({});

    const [visualAidsOpen, setVisualAidsOpen] = useState(true);
    const [visualAidsTab, setVisualAidsTab] = useState('basics');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'inspection_table', title: 'Inspection (try values)', prompt: 'Try values to make an equation true.' },
            { key: 'solve_one_step', title: 'Solve one-step', prompt: 'Solve equations like x + b = c or ax = c.' },
            { key: 'solve_two_step', title: 'Solve two-step', prompt: 'Solve equations like ax + b = c.' },
            { key: 'solve_brackets', title: 'Solve with brackets', prompt: 'Solve equations like k(ax + b) = c.' },
            { key: 'word_problem_linear', title: 'Word problem', prompt: 'Set up and solve a linear equation from a situation.' },
            { key: 'exponent_equation_same_base', title: 'Exponent equation', prompt: 'Solve equations like a^(x + b) = a^k.' },
            { key: 'power_equation_variable_base', title: 'Variable in base', prompt: 'Solve equations like x^n = k for simple powers.' },
        ],
        []
    );

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade9/algebraic-equations/generate');

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: subskill || 'algebraic_equations',
                    difficulty: difficulty || 'easy',
                    question_type: 'scaffold',
                    count: 1,
                }),
            });
            if (!res.ok) throw new Error(`Grade 9 Algebraic Equations scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Grade 9 Algebraic Equations scaffold generation failed');
            const q = data?.questions?.[0] || null;

            setScaffoldQuestion(q);
            setScaffoldAnswer('');
            setScaffoldFeedback(null);
            setScaffoldShowHint(false);
            setScaffoldCheckpointIndex(0);
            setScaffoldCheckpointAnswers({});
            setScaffoldCheckpointFeedback({});
        } catch (err) {
            const msg = err?.message || String(err);
            if (String(msg).toLowerCase().includes('failed to fetch')) {
                setScaffoldError(`Failed to fetch (${buildApiUrl('/api/math/grade9/algebraic-equations/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
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
            const endpoint = buildApiUrl('/api/math/grade9/algebraic-equations/generate');

            const typedRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'mixed',
                    difficulty,
                    question_type: 'typed',
                    count: 4,
                }),
            });
            if (!typedRes.ok) throw new Error(`Grade 9 Algebraic Equations (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Grade 9 Algebraic Equations (typed) generation failed');

            const mcqRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'mixed',
                    difficulty,
                    question_type: 'mcq',
                    count: 3,
                }),
            });
            if (!mcqRes.ok) throw new Error(`Grade 9 Algebraic Equations (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Grade 9 Algebraic Equations (mcq) generation failed');

            const combined = [...(typedData.questions || []), ...(mcqData.questions || [])];
            for (let i = combined.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [combined[i], combined[j]] = [combined[j], combined[i]];
            }

            setPracticeQuestions(combined);
            setPracticeAnswers([]);
            setPracticeFeedback([]);
        } catch (err) {
            const msg = err?.message || String(err);
            if (String(msg).toLowerCase().includes('failed to fetch')) {
                setPracticeError(`Failed to fetch (${buildApiUrl('/api/math/grade9/algebraic-equations/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        const inMode = workspaceMode === 'grade9_algebraic_equations_1_scaffold' || workspaceMode === 'grade9_algebraic_equations_1_practice';
        if (!inMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('basics');
    }, [workspaceMode, visualAidsOpen]);

    useEffect(() => {
        if (workspaceMode !== 'grade9_algebraic_equations_1_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

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
        scaffoldCheckpointIndex,
        setScaffoldCheckpointIndex,
        scaffoldCheckpointAnswers,
        setScaffoldCheckpointAnswers,
        scaffoldCheckpointFeedback,
        setScaffoldCheckpointFeedback,
        fetchScaffoldQuestion,
        visualAidsOpen,
        setVisualAidsOpen,
        visualAidsTab,
        setVisualAidsTab,
    };
};
