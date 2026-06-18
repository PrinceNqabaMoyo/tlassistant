import { useEffect, useMemo, useState } from 'react';

export const useGrade8PatternsController = ({ workspaceMode, buildApiUrl }) => {
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
    const [visualAidsTab, setVisualAidsTab] = useState('rules');

    const scaffoldSteps = useMemo(
        () => [
            { key: 'next_terms_arithmetic', title: 'Arithmetic sequences', prompt: 'Find next terms using constant difference.' },
            { key: 'next_terms_geometric', title: 'Geometric sequences', prompt: 'Find next terms using constant ratio.' },
            { key: 'growing_difference', title: 'Growing differences', prompt: 'Identify changing differences and predict next term.' },
            { key: 'linear_nth_term', title: 'Linear nth term', prompt: 'Find an explicit nth-term rule and compute a term.' },
            { key: 'square_numbers', title: 'Square numbers', prompt: 'Use n² patterns and recognise sequences.' },
            { key: 'triangular_numbers', title: 'Triangular numbers', prompt: 'Use n(n+1)/2 patterns and sequences.' },
            { key: 'cube_numbers', title: 'Cube numbers', prompt: 'Use n³ patterns and sequences.' },
            { key: 't_shape_numbers', title: 'T-shape patterns', prompt: 'Find the rule for a growing T-shape match/tile pattern.' },
            { key: 'tile_n_shape', title: 'Tile n patterns', prompt: 'Find the rule for a general “n-shape” tile pattern.' },
        ],
        []
    );

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade8/patterns/generate');

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: subskill || 'mixed',
                    difficulty: difficulty || 'easy',
                    question_type: 'scaffold',
                    count: 1,
                }),
            });

            if (!res.ok) throw new Error(`Grade 8 Patterns scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Grade 8 patterns scaffold generation failed');
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
                setScaffoldError(`Failed to fetch (${buildApiUrl('/api/math/grade8/patterns/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
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
            const endpoint = buildApiUrl('/api/math/grade8/patterns/generate');

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
            if (!typedRes.ok) throw new Error(`Grade 8 Patterns (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Grade 8 Patterns (typed) generation failed');

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
            if (!mcqRes.ok) throw new Error(`Grade 8 Patterns (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Grade 8 Patterns (mcq) generation failed');

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
                setPracticeError(`Failed to fetch (${buildApiUrl('/api/math/grade8/patterns/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade8_patterns_scaffold') return;
        const stepKey = (scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0])?.key;

        const tabByStepKey = {
            square_numbers: 'tables',
            triangular_numbers: 'rules',
            cube_numbers: 'tables',
        };

        setVisualAidsTab(tabByStepKey[stepKey] || 'rules');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade8_patterns_scaffold') return;
        const step = scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0];
        fetchScaffoldQuestion({ subskill: step.key, difficulty: scaffoldDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade8_patterns_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inMode = workspaceMode === 'grade8_patterns_scaffold' || workspaceMode === 'grade8_patterns_practice';
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
    };
};
