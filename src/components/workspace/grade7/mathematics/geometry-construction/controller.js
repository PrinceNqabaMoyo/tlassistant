import { useEffect, useMemo, useState } from 'react';

export const useGrade7GeoConstructController = ({ workspaceMode, buildApiUrl }) => {
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
    const [visualAidsTab, setVisualAidsTab] = useState('angles');

    const scaffoldSteps = useMemo(() => (
        [
            { key: 'degree_unit_familiar_angles_table', title: 'Degrees: common angles', prompt: 'Recall common angles like 90°, 180°, 360° and fractions of these.' },
            { key: 'clock_degree_movement', title: 'Clock hand degrees', prompt: 'Use 360° in a full turn to find clock hand movement.' },
            { key: 'classify_angles_by_degree', title: 'Classify angles', prompt: 'Classify angles as acute/right/obtuse/straight/reflex.' },
            { key: 'protractor_reading_choose_scale', title: 'Protractor scale', prompt: 'Choose the correct protractor scale (start at 0° on the reference arm).' },
            { key: 'reflex_angle_strategy', title: 'Reflex angles', prompt: 'Use 360° − smaller angle to find a reflex angle.' },
            { key: 'construct_angle_to_given_line_steps', title: 'Construct angle steps', prompt: 'Fill in missing words for protractor construction steps.' },
            { key: 'parallel_perpendicular_language_symbols', title: 'Symbols', prompt: 'Use ⊥ for perpendicular and // for parallel.' },
            { key: 'circle_radius_concepts', title: 'Circle radius', prompt: 'Know what radius means and where it is in a circle.' },
            { key: 'compass_set_radius_steps', title: 'Compass: set radius', prompt: 'Set a compass radius correctly to draw circles.' },
            { key: 'construct_equilateral_triangle_from_segment', title: 'Equilateral triangle construction', prompt: 'Understand why the two-circle method makes an equilateral triangle.' },
            { key: 'construct_parallelogram_from_two_segments', title: 'Parallelogram construction', prompt: 'Recognise why a circle method can create a parallelogram.' },
        ]
    ), []);

    const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        try {
            const endpoint = buildApiUrl('/api/math/grade7/geometry-construction/generate');

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
            if (!res.ok) throw new Error(`Geometry Construction scaffold request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Geometry Construction scaffold generation failed');
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
                setScaffoldError(`Failed to fetch (${buildApiUrl('/api/math/grade7/geometry-construction/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
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
            const endpoint = buildApiUrl('/api/math/grade7/geometry-construction/generate');

            const typedRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'geometry_construction',
                    difficulty,
                    question_type: 'typed',
                    count: 4,
                }),
            });
            if (!typedRes.ok) throw new Error(`Geometry Construction (typed) request failed: HTTP ${typedRes.status}`);
            const typedData = await typedRes.json();
            if (!typedData?.success) throw new Error(typedData?.error || 'Geometry Construction (typed) generation failed');

            const mcqRes = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    subskill: 'geometry_construction',
                    difficulty,
                    question_type: 'mcq',
                    count: 3,
                }),
            });
            if (!mcqRes.ok) throw new Error(`Geometry Construction (mcq) request failed: HTTP ${mcqRes.status}`);
            const mcqData = await mcqRes.json();
            if (!mcqData?.success) throw new Error(mcqData?.error || 'Geometry Construction (mcq) generation failed');

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
                setPracticeError(`Failed to fetch (${buildApiUrl('/api/math/grade7/geometry-construction/generate')}). Check that the backend is running and VITE_API_BASE_URL / runtime-config.js points to it.`);
            } else {
                setPracticeError(msg);
            }
        } finally {
            setPracticeLoading(false);
        }
    };

    useEffect(() => {
        if (workspaceMode !== 'grade7_geo_construct_scaffold') return;
        const stepKey = (scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0])?.key;

        const tabByStepKey = {
            degree_unit_familiar_angles_table: 'degrees',
            clock_degree_movement: 'degrees',
            classify_angles_by_degree: 'angles',
            protractor_reading_choose_scale: 'protractor',
            reflex_angle_strategy: 'protractor',
            construct_angle_to_given_line_steps: 'protractor',
            parallel_perpendicular_language_symbols: 'lines',
            circle_radius_concepts: 'compass',
            compass_set_radius_steps: 'compass',
            construct_equilateral_triangle_from_segment: 'compass',
            construct_parallelogram_from_two_segments: 'compass',
        };

        setVisualAidsTab(tabByStepKey[stepKey] || 'angles');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade7_geo_construct_scaffold') return;
        const step = scaffoldSteps[scaffoldStepIndex] || scaffoldSteps[0];
        fetchScaffoldQuestion({ subskill: step.key, difficulty: scaffoldDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode, scaffoldStepIndex]);

    useEffect(() => {
        if (workspaceMode !== 'grade7_geo_construct_practice') return;
        fetchPractice({ difficulty: practiceDifficulty });
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [workspaceMode]);

    useEffect(() => {
        const inGeoMode = workspaceMode === 'grade7_geo_construct_scaffold' || workspaceMode === 'grade7_geo_construct_practice';
        if (!inGeoMode) return;
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
