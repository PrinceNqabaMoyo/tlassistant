import { useEffect, useState } from 'react';
import { useDynamicScaffoldSteps } from './useDynamicScaffoldSteps';

const DEFAULT_SCAFFOLD_STEPS = [
    { key: 'concepts', title: 'Concepts (MCQ)' },
    { key: 'discussion', title: 'Semantic/Essay (Discussion)' },
];

/**
 * Factory that builds a controller hook for a Grade 10 Business Studies topic.
 * Each topic only differs by its backend topic key, workspace mode prefix and
 * (optionally) its scaffold steps, so the heavy lifting is shared here.
 *
 * Phase 1 update: scaffold steps are now fetched dynamically from the
 * curriculum `.md` file via `/sections` endpoint.
 */
export const createGrade10BSController = ({
    topicKey,
    modePrefix,
    endpointPath = '/api/business-studies/grade10/generate',
    scaffoldSteps: initialScaffoldSteps = null,
}) => {
    const scaffoldMode = `${modePrefix}_scaffold`;
    const practiceMode = `${modePrefix}_practice`;

    return ({ workspaceMode, buildApiUrl }) => {
        const [practiceQuestions, setPracticeQuestions] = useState([]);
        const [practiceAnswers, setPracticeAnswers] = useState({});
        const [practiceFeedback, setPracticeFeedback] = useState(null);
        const [practiceLoading, setPracticeLoading] = useState(false);
        const [practiceError, setPracticeError] = useState(null);
        const [practiceDifficulty, setPracticeDifficulty] = useState('medium');

        const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
        const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
        const [scaffoldAnswer, setScaffoldAnswer] = useState(null);
        const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
        const [scaffoldShowHint, setScaffoldShowHint] = useState(false);
        const [scaffoldLoading, setScaffoldLoading] = useState(false);
        const [scaffoldError, setScaffoldError] = useState(null);
        const [scaffoldDifficulty, setScaffoldDifficulty] = useState('medium');

        const [visualAidsOpen, setVisualAidsOpen] = useState(true);
        const [visualAidsTab, setVisualAidsTab] = useState('overview');

        // Dynamic scaffold steps from curriculum .md files
        const { steps, loading: stepsLoading } = useDynamicScaffoldSteps({
            topicKey,
            buildApiUrl,
            enabled: workspaceMode === scaffoldMode,
        });

        const fetchScaffoldQuestion = async ({ subskill, difficulty }) => {
            setScaffoldLoading(true);
            setScaffoldError(null);
            try {
                const endpoint = buildApiUrl(endpointPath);
                const res = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        topic: topicKey,
                        subskill: subskill || 'concepts',
                        difficulty: difficulty || scaffoldDifficulty || 'medium',
                        count: 1,
                    }),
                });

                if (!res.ok) throw new Error(`Grade 10 Business Studies scaffold request failed: HTTP ${res.status}`);
                const data = await res.json();
                if (!data?.questions) throw new Error(data?.error || 'Generation failed');

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

        const fetchPractice = async ({ difficulty }) => {
            setPracticeLoading(true);
            setPracticeError(null);
            try {
                const endpoint = buildApiUrl(endpointPath);

                const conceptsReq = fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ topic: topicKey, subskill: 'concepts', difficulty: difficulty || 'medium', count: 5 }),
                }).then(r => r.json());

                const discussionReq = fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ topic: topicKey, subskill: 'discussion', difficulty: difficulty || 'medium', count: 3 }),
                }).then(r => r.json());

                const [conceptsRes, discussionRes] = await Promise.all([conceptsReq, discussionReq]);

                if (conceptsRes?.error) throw new Error(conceptsRes.error);
                if (discussionRes?.error) throw new Error(discussionRes.error);

                const allQs = [
                    ...(conceptsRes.questions || []),
                    ...(discussionRes.questions || []),
                ];

                setPracticeQuestions(allQs);
                setPracticeAnswers({});
                setPracticeFeedback(null);
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
            if (workspaceMode !== practiceMode) return;
            fetchPractice({ difficulty: practiceDifficulty });
            // eslint-disable-next-line react-hooks/exhaustive-deps
        }, [workspaceMode]);

        useEffect(() => {
            const inMode = workspaceMode === scaffoldMode || workspaceMode === practiceMode;
            if (!inMode) return;
            if (!visualAidsOpen) return;
            if (!visualAidsTab) setVisualAidsTab('overview');
        }, [workspaceMode, visualAidsOpen]);

        return {
            scaffoldSteps: steps,
            stepsLoading,
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
            fetchScaffoldQuestion,
            visualAidsOpen,
            setVisualAidsOpen,
            visualAidsTab,
            setVisualAidsTab,
        };
    };
};
