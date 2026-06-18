import { useEffect, useMemo, useState } from 'react';

export const useGrade8ExponentsController = ({ workspaceMode, buildApiUrl }) => {
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

    const scaffoldSteps = useMemo(
        () => [
            { key: 'write_exponential_form', title: 'Expanded → exponential', prompt: 'Write repeated multiplication using exponents.' },
            { key: 'calculate_power', title: 'Calculate a power', prompt: 'Calculate a power without a calculator.' },
            { key: 'square_or_cube_root', title: 'Roots', prompt: 'Find √ and ∛ for perfect squares/cubes.' },
            { key: 'negative_base_parentheses', title: 'Negative bases', prompt: 'Distinguish -2^2 vs (-2)^2.' },
            { key: 'product_of_powers', title: 'Product of powers', prompt: 'Same base: add exponents.' },
            { key: 'quotient_of_powers', title: 'Quotient of powers', prompt: 'Same base: subtract exponents.' },
            { key: 'power_of_a_power', title: 'Power of a power', prompt: 'Multiply exponents.' },
            { key: 'power_of_a_product', title: 'Power of a product', prompt: '(ab)^n = a^n b^n.' },
            { key: 'zero_exponent', title: 'Zero exponent', prompt: 'Use a^0 = 1.' },
        ],
        []
    );

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade8/exponents/generate');

            const scaffoldCapable = new Set(['product_of_powers', 'power_of_a_power']);

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill,
                    difficulty,
                    question_type: scaffoldCapable.has(subskill) ? 'scaffold' : 'typed',
                    count: 1,
                }),
            });

            if (!res.ok) throw new Error(`Grade 8 exponents scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Grade 8 exponents scaffold generation failed');
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
                setScaffoldError(`Failed to fetch (${buildApiUrl('/api/math/grade8/exponents/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
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
            const endpoint = buildApiUrl('/api/math/grade8/exponents/generate');

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
            if (!typedRes.ok) throw new Error(`Grade 8 Exponents (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Grade 8 Exponents (typed) generation failed');

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
            if (!mcqRes.ok) throw new Error(`Grade 8 Exponents (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Grade 8 Exponents (mcq) generation failed');

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
                setPracticeError(`Failed to fetch (${buildApiUrl('/api/math/grade8/exponents/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade8_exponents_scaffold') return;
        const stepKey = (scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0])?.key;

        const tabByStepKey = {
            square_or_cube_root: 'roots',
        };

        setVisualAidsTab(tabByStepKey[stepKey] || 'powers');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade8_exponents_scaffold') return;
        const step = scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0];
        fetchScaffoldQuestion({ subskill: step.key, difficulty: scaffoldDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade8_exponents_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade8_exponents_scaffold' || workspaceMode === 'grade8_exponents_practice';
        if (!inMode) return;
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
