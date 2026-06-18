import { useEffect, useMemo, useState } from 'react';

export const useGrade10AlgebraicExpressionsController = ({ workspaceMode, buildApiUrl }) => {
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
            { key: 'classify_real_numbers', title: 'Real number system', prompt: 'Classify numbers as rational/irrational.' },
            { key: 'rounding_off', title: 'Rounding off', prompt: 'Round decimals to a given number of decimal places.' },
            { key: 'estimate_surds_between_integers', title: 'Estimating surds', prompt: 'Use perfect squares/cubes to bound a surd.' },
            { key: 'expand_products', title: 'Expanding products', prompt: 'Expand products of monomials/binomials and simplify.' },
            { key: 'factor_common_or_difference_of_squares', title: 'Common factor / difference of squares', prompt: 'Factorise using a common factor or A² − B².' },
            { key: 'factorise_by_grouping', title: 'Grouping', prompt: 'Factorise by grouping terms in pairs.' },
            { key: 'factorise_trinomial', title: 'Trinomial', prompt: 'Factorise a quadratic trinomial.' },
        ],
        []
    );

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade10/algebraic-expressions/generate');

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: subskill || 'algebraic_expressions',
                    difficulty: difficulty || 'easy',
                    question_type: 'scaffold',
                    count: 1,
                }),
            });

            if (!res.ok) throw new Error(`Grade 10 Algebraic Expressions scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Grade 10 Algebraic Expressions scaffold generation failed');
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
                setScaffoldError(`Failed to fetch (${buildApiUrl('/api/math/grade10/algebraic-expressions/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
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
            const endpoint = buildApiUrl('/api/math/grade10/algebraic-expressions/generate');

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
            if (!typedRes.ok) throw new Error(`Grade 10 Algebraic Expressions (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Grade 10 Algebraic Expressions (typed) generation failed');

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
            if (!mcqRes.ok) throw new Error(`Grade 10 Algebraic Expressions (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Grade 10 Algebraic Expressions (mcq) generation failed');

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
                setPracticeError(`Failed to fetch (${buildApiUrl('/api/math/grade10/algebraic-expressions/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        const inAlgExpMode = workspaceMode === 'grade10_algebraic_expressions_scaffold' || workspaceMode === 'grade10_algebraic_expressions_practice';
        if (!inAlgExpMode) return;
        if (!visualAidsOpen) return;
        if (!visualAidsTab) setVisualAidsTab('basics');
    }, [workspaceMode, visualAidsOpen]);

    useEffect(() => {
        if (workspaceMode !== 'grade10_algebraic_expressions_practice') return;
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
