import { useEffect, useMemo, useState } from 'react';

export const useGrade7WholeNumbersController = ({ workspaceMode, buildApiUrl }) => {
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
    const [visualAidsTab, setVisualAidsTab] = useState('place_value');
    const [multiplesBase, setMultiplesBase] = useState(3);
    const [multiplesMax, setMultiplesMax] = useState(100);
    const [placeValueInput, setPlaceValueInput] = useState('');
    const [roundingNumber, setRoundingNumber] = useState('');
    const [roundingBase, setRoundingBase] = useState(10);

    const scaffoldSteps = useMemo(() => (
        [
            { key: 'place_value', title: 'Place value', prompt: 'Identify the value of a digit.' },
            { key: 'expanded_notation', title: 'Expanded notation', prompt: 'Break a number into place-value parts.' },
            { key: 'build_number_from_expanded', title: 'Build the number', prompt: 'Combine parts into one number.' },
            { key: 'compare', title: 'Compare', prompt: 'Compare two whole numbers using <, >, =.' },
            { key: 'ordering', title: 'Ordering', prompt: 'Order a list of numbers.' },
            { key: 'rounding', title: 'Rounding', prompt: 'Round to a given place value.' },
            { key: 'multiples', title: 'Multiples', prompt: 'Identify multiples and common multiples.' },
            { key: 'words_to_number', title: 'Words to number', prompt: 'Convert words to a numeral.' },
            { key: 'doubling_halving', title: 'Doubling strategy', prompt: 'Use doubling (×2, ×4, ×8, ×16) to multiply.' },
        ]
    ), []);

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade7/whole-numbers/generate');

            const scaffoldV2Subskills = new Set([
                'rounding',
                'expanded_notation',
                'build_number_from_expanded',
                'compare',
                'place_value',
                'multiples',
                'words_to_number',
                'ordering',
                'doubling_halving',
            ]);

            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill,
                    difficulty,
                    question_type: scaffoldV2Subskills.has(subskill) ? 'scaffold' : 'typed',
                    count: 1,
                }),
            });
            if (!res.ok) throw new Error(`Scaffold question request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Scaffold question generation failed');
            const q = data?.questions?.[0] || null;
            setScaffoldQuestion(q);
            setScaffoldAnswer('');
            setScaffoldFeedback(null);
            setScaffoldShowHint(false);
            setScaffoldCheckpointIndex(0);
            setScaffoldCheckpointAnswers({});
            setScaffoldCheckpointFeedback({});
        } catch (err) {
            setScaffoldError(err?.message || String(err));
        } finally {
            setScaffoldLoading(false);
        }
    };

    const fetchPractice = async ({ difficulty }) => {
        setPracticeLoading(true);
        setPracticeError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade7/whole-numbers/generate');

            const typedRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'whole_numbers',
                    difficulty,
                    question_type: 'typed',
                    count: 4,
                }),
            });
            if (!typedRes.ok) throw new Error(`Whole Numbers (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Whole Numbers (typed) generation failed');

            const mcqRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'whole_numbers',
                    difficulty,
                    question_type: 'mcq',
                    count: 3,
                }),
            });
            if (!mcqRes.ok) throw new Error(`Whole Numbers (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Whole Numbers (mcq) generation failed');

            const combined = [...(typedData.questions || []), ...(mcqData.questions || [])];
            for (let i = combined.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [combined[i], combined[j]] = [combined[j], combined[i]];
            }

            setPracticeQuestions(combined);
            setPracticeAnswers({});
            setPracticeFeedback({});
        } catch (err) {
            setPracticeError(err?.message || String(err));
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade7_whole_scaffold') return;
        const stepKey = (scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0])?.key;

        const tabByStepKey = {
            place_value: 'place_value',
            expanded_notation: 'place_value',
            build_number_from_expanded: 'place_value',
            compare: 'place_value',
            rounding: 'rounding',
            multiples: 'multiples',
            words_to_number: 'place_value',
            ordering: 'place_value',
            doubling_halving: 'multiples',
        };

        setVisualAidsTab(tabByStepKey[stepKey] || 'place_value');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade7_whole_scaffold') return;
        const step = scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0];
        fetchScaffoldQuestion({ subskill: step.key, difficulty: scaffoldDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade7_whole_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inWholeNumbersMode = workspaceMode === 'grade7_whole_scaffold' || workspaceMode === 'grade7_whole_practice';
        if (!inWholeNumbersMode) return;
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
        multiplesBase,
        setMultiplesBase,
        multiplesMax,
        setMultiplesMax,
        placeValueInput,
        setPlaceValueInput,
        roundingNumber,
        setRoundingNumber,
        roundingBase,
        setRoundingBase,
    };
};
