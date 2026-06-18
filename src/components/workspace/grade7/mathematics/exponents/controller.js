import { useEffect, useMemo, useState } from 'react';

export const useGrade7ExponentsController = ({ workspaceMode, buildApiUrl }) => {
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState({});
    const [practiceFeedback, setPracticeFeedback] = useState({});
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
    const [visualAidsTab, setVisualAidsTab] = useState('powers');
    const [vizBase, setVizBase] = useState(3);
    const [vizExponent, setVizExponent] = useState(4);
    const [vizRoot, setVizRoot] = useState(144);

    const scaffoldSteps = useMemo(() => (
        [
            { key: 'squares_cubes_quickfacts', title: 'Squares & cubes', prompt: 'Quick facts for squares and cubes.' },
            { key: 'expanded_to_exponential', title: 'Expanded → exponential', prompt: 'Write repeated multiplication using exponents.' },
            { key: 'exponential_to_expanded_or_value', title: 'Exponential → expanded/value', prompt: 'Expand or calculate a power.' },
            { key: 'identify_base_exponent_language', title: 'Base & exponent language', prompt: 'Use words like base, exponent, squared, cubed, power.' },
            { key: 'prime_factors_to_exponential', title: 'Prime factors → exponential', prompt: 'Write prime factorization using exponent notation.' },
            { key: 'express_as_power_2_3_5_10', title: 'Express as power (2/3/5/10)', prompt: 'Express a number as a power of 2, 3, 5, or 10.' },
            { key: 'roots_square_cube', title: 'Square & cube roots', prompt: 'Find √ and ∛ for perfect squares/cubes.' },
            { key: 'compare_exponential_root_forms', title: 'Compare forms', prompt: 'Compare powers/roots using <, >, =.' },
            { key: 'order_expressions', title: 'Ordering', prompt: 'Order expressions ascending/descending.' },
            { key: 'order_of_operations_with_powers_and_roots', title: 'Order of operations', prompt: 'Calculate expressions with powers/roots using correct order.' },
            { key: 'write_expression_in_words', title: 'Write in words', prompt: 'Write a numerical expression in words.' },
            { key: 'mixed_calculations_worksheet', title: 'Worksheet mix', prompt: 'Mixed calculations using exponents and roots.' },
            { key: 'patterns_last_digit_powers_of_2', title: 'Last digit patterns', prompt: 'Find the last digit of powers of 2 without full calculation.' },
        ]
    ), []);

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade7/exponents/generate');

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill,
                    difficulty,
                    question_type: 'scaffold',
                    count: 1,
                }),
            });
            if (!res.ok) throw new Error(`Exponents scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Exponents scaffold generation failed');
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
                setScaffoldError(`Failed to fetch (${buildApiUrl('/api/math/grade7/exponents/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
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
            const endpoint = buildApiUrl('/api/math/grade7/exponents/generate');

            const typedRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'mixed_calculations_worksheet',
                    difficulty,
                    question_type: 'typed',
                    count: 4,
                }),
            });
            if (!typedRes.ok) throw new Error(`Exponents (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Exponents (typed) generation failed');

            const mcqRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'compare_exponential_root_forms',
                    difficulty,
                    question_type: 'mcq',
                    count: 3,
                }),
            });
            if (!mcqRes.ok) throw new Error(`Exponents (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Exponents (mcq) generation failed');

            const combined = [...(typedData.questions || []), ...(mcqData.questions || [])];
            for (let i = combined.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [combined[i], combined[j]] = [combined[j], combined[i]];
            }

            setPracticeQuestions(combined);
            setPracticeAnswers({});
            setPracticeFeedback({});
        } catch (err) {
            const msg = err?.message || String(err);
            if (String(msg).toLowerCase().includes('failed to fetch')) {
                setPracticeError(`Failed to fetch (${buildApiUrl('/api/math/grade7/exponents/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade7_exponents_scaffold') return;
        const stepKey = (scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0])?.key;

        const tabByStepKey = {
            squares_cubes_quickfacts: 'tables',
            expanded_to_exponential: 'powers',
            exponential_to_expanded_or_value: 'powers',
            identify_base_exponent_language: 'powers',
            prime_factors_to_exponential: 'powers',
            express_as_power_2_3_5_10: 'powers',
            roots_square_cube: 'roots',
            compare_exponential_root_forms: 'powers',
            order_expressions: 'powers',
            order_of_operations_with_powers_and_roots: 'bodmas',
            write_expression_in_words: 'powers',
            mixed_calculations_worksheet: 'bodmas',
            patterns_last_digit_powers_of_2: 'powers',
        };

        setVisualAidsTab(tabByStepKey[stepKey] || 'powers');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade7_exponents_scaffold') return;
        const step = scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0];
        fetchScaffoldQuestion({ subskill: step.key, difficulty: scaffoldDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade7_exponents_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inExponentsMode = workspaceMode === 'grade7_exponents_scaffold' || workspaceMode === 'grade7_exponents_practice';
        if (!inExponentsMode) return;
        if (!visualAidsOpen) return;

        const handleKeyDown = (e) => {
            if (e.key === 'Escape') {
                setVisualAidsOpen(false);
            }
        };

        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
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
        vizBase,
        setVizBase,
        vizExponent,
        setVizExponent,
        vizRoot,
        setVizRoot,
    };
};
