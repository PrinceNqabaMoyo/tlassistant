import { useMemo, useState } from 'react';
import { useDynamicScaffoldSteps } from '../../shared/useDynamicScaffoldSteps';

const topicKey = 'grade11_bs_influences_on_business_environments';
const endpointPath = '/api/business-studies/grade11/generate';
const REQUIRED_SCAFFOLD_SUCCESSES = 2;
const REQUIRED_DISTINCT_EVIDENCE = 2;
const REQUIRED_DISTINCT_FAMILIES = {
    concepts: 2,
    application: 2,
    discussion: 1,
};

const createInitialStepProgress = () => ({
    successCount: 0,
    questionIds: [],
    familyIds: [],
    evidenceKeys: [],
});

const createInitialMasteryProgress = () => ({
    concepts: createInitialStepProgress(),
    application: createInitialStepProgress(),
    discussion: createInitialStepProgress(),
});

const getQuestionFamilyId = (question) => (
    question?.question_family_id
    || question?.scenario_family_id
    || question?.concept_id
    || question?.id
    || 'unknown-family'
);

const getQuestionEvidenceKey = (question) => `${getQuestionFamilyId(question)}::${question?.retry_variant || 'core'}`;

const isMasteredFeedback = (feedback) => Boolean(feedback?.is_mastered ?? feedback?.is_correct);

const isStepMastered = (stepKey, progress) => {
    const successCount = progress?.successCount || 0;
    const familyCount = progress?.familyIds?.length || 0;
    const evidenceCount = progress?.evidenceKeys?.length || 0;

    if (successCount < REQUIRED_SCAFFOLD_SUCCESSES || evidenceCount < REQUIRED_DISTINCT_EVIDENCE) {
        return false;
    }

    if (stepKey === 'discussion') {
        return true;
    }

    return familyCount >= (REQUIRED_DISTINCT_FAMILIES[stepKey] || 1);
};

const hasCompletedAllSteps = (progress) => (
    isStepMastered('concepts', progress?.concepts)
    && isStepMastered('application', progress?.application)
    && isStepMastered('discussion', progress?.discussion)
);

export const useGrade11BSInfluencesController = ({ buildApiUrl }) => {
    const [scaffoldQuestion, setScaffoldQuestion] = useState(null);
    const [scaffoldAnswer, setScaffoldAnswer] = useState('');
    const [scaffoldFeedback, setScaffoldFeedback] = useState(null);
    const [scaffoldLoading, setScaffoldLoading] = useState(false);
    const [scaffoldError, setScaffoldError] = useState(null);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('medium');
    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldHintLevel, setScaffoldHintLevel] = useState(0);
    const [scaffoldShowMemo, setScaffoldShowMemo] = useState(false);
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceAnswers, setPracticeAnswers] = useState({});
    const [practiceFeedback, setPracticeFeedback] = useState(null);
    const [practiceLoading, setPracticeLoading] = useState(false);
    const [practiceError, setPracticeError] = useState(null);
    const [practiceDifficulty, setPracticeDifficulty] = useState('medium');
    const [practiceSubskill, setPracticeSubskill] = useState('mixed');
    const [visualAidsTab, setVisualAidsTab] = useState('overview');
    const [visualAidsOpen, setVisualAidsOpen] = useState(false);
    const [scaffoldMasteryProgress, setScaffoldMasteryProgress] = useState(createInitialMasteryProgress);
    const [scaffoldTopicCompleted, setScaffoldTopicCompleted] = useState(false);

    const scaffoldMode = 'grade11_bs_influences_on_business_environments_scaffold';
    const { steps: scaffoldSteps, loading: stepsLoading } = useDynamicScaffoldSteps({
        topicKey,
        buildApiUrl,
        enabled: true,
        sectionsEndpoint: '/api/business-studies/grade11/sections',
    });

    const practiceSubskills = useMemo(() => ([
        { key: 'mixed', title: 'Mixed Practice' },
        ...scaffoldSteps,
    ]), [scaffoldSteps]);

    const resetScaffoldSessionState = () => {
        setScaffoldAnswer('');
        setScaffoldFeedback(null);
        setScaffoldHintLevel(0);
        setScaffoldShowMemo(false);
        setScaffoldError(null);
        setScaffoldQuestion(null);
        setScaffoldMasteryProgress(createInitialMasteryProgress());
        setScaffoldTopicCompleted(false);
    };

    const getStepKey = (stepKey) => stepKey || scaffoldSteps[scaffoldStepIndex]?.key || 'concepts';

    const completeScaffoldTopic = () => {
        setScaffoldTopicCompleted(true);
        setScaffoldQuestion(null);
        setScaffoldAnswer('');
        setScaffoldFeedback(null);
        setScaffoldHintLevel(0);
        setScaffoldShowMemo(false);
    };

    const postGenerate = async ({ subskill, difficulty, count, config }) => {
        const endpoint = typeof buildApiUrl === 'function'
            ? buildApiUrl(endpointPath)
            : buildApiUrl(endpointPath);
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                topic: topicKey,
                subskill,
                difficulty,
                count,
                config: config || {},
            }),
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `HTTP error ${response.status}`);
        }

        const data = await response.json();
        return data.questions || [];
    };

    const fetchScaffoldQuestion = async ({ subskill, difficulty, config, avoidQuestionFamilyIds, avoidEvidenceKeys } = {}) => {
        setScaffoldLoading(true);
        setScaffoldError(null);
        setScaffoldFeedback(null);
        setScaffoldAnswer('');
        setScaffoldHintLevel(0);
        setScaffoldShowMemo(false);

        try {
            const effectiveSubskill = getStepKey(subskill);
            const disallowedFamilyIds = new Set(avoidQuestionFamilyIds || []);
            const disallowedEvidenceKeys = new Set(avoidEvidenceKeys || []);
            const maxAttempts = config
                ? 1
                : (disallowedFamilyIds.size > 0 || disallowedEvidenceKeys.size > 0 ? 6 : 1);
            let nextQuestion = null;

            for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
                const questions = await postGenerate({
                    subskill: effectiveSubskill,
                    difficulty: difficulty || scaffoldDifficulty,
                    count: 1,
                    config,
                });
                const candidate = questions[0] || null;

                if (!candidate) {
                    nextQuestion = null;
                    break;
                }

                nextQuestion = candidate;

                if (config) {
                    break;
                }

                const familyId = getQuestionFamilyId(candidate);
                const evidenceKey = getQuestionEvidenceKey(candidate);
                const isDuplicateFamily = disallowedFamilyIds.has(familyId);
                const isDuplicateEvidence = disallowedEvidenceKeys.has(evidenceKey);

                if (!isDuplicateFamily && !isDuplicateEvidence) {
                    break;
                }
            }

            setScaffoldQuestion(nextQuestion);
        } catch (err) {
            console.error('Failed to fetch Grade 11 Business Studies scaffold question:', err);
            setScaffoldError(err.message || 'Failed to generate scaffold question.');
            setScaffoldQuestion(null);
        } finally {
            setScaffoldLoading(false);
        }
    };

    const applyScaffoldResult = (question, feedback) => {
        setScaffoldFeedback(feedback);

        if (!question || !isMasteredFeedback(feedback)) {
            return;
        }

        const stepKey = question?.subskill || getStepKey();
        const questionId = question?.id;
        const familyId = getQuestionFamilyId(question);
        const evidenceKey = getQuestionEvidenceKey(question);

        setScaffoldMasteryProgress((current) => {
            const currentStepProgress = current[stepKey] || createInitialStepProgress();

            if (questionId && currentStepProgress.questionIds.includes(questionId)) {
                return current;
            }

            return {
                ...current,
                [stepKey]: {
                    successCount: currentStepProgress.successCount + 1,
                    questionIds: questionId
                        ? [...currentStepProgress.questionIds, questionId]
                        : currentStepProgress.questionIds,
                    familyIds: currentStepProgress.familyIds.includes(familyId)
                        ? currentStepProgress.familyIds
                        : [...currentStepProgress.familyIds, familyId],
                    evidenceKeys: currentStepProgress.evidenceKeys.includes(evidenceKey)
                        ? currentStepProgress.evidenceKeys
                        : [...currentStepProgress.evidenceKeys, evidenceKey],
                },
            };
        });
    };

    const resetScaffoldSession = async () => {
        resetScaffoldSessionState();
        setScaffoldStepIndex(0);
    };

    const fetchPractice = async ({ difficulty, subskill, config }) => {
        const effectiveSubskill = subskill || practiceSubskill || 'mixed';
        setPracticeLoading(true);
        setPracticeError(null);
        setPracticeFeedback(null);
        setPracticeAnswers({});

        try {
            let questions = [];
            if (effectiveSubskill === 'mixed') {
                const [concepts, application, discussion] = await Promise.all([
                    postGenerate({ subskill: 'concepts', difficulty: difficulty || practiceDifficulty, count: 3, config }),
                    postGenerate({ subskill: 'application', difficulty: difficulty || practiceDifficulty, count: 3, config }),
                    postGenerate({ subskill: 'discussion', difficulty: difficulty || practiceDifficulty, count: 2, config }),
                ]);
                questions = [...concepts, ...application, ...discussion];
            } else {
                questions = await postGenerate({
                    subskill: effectiveSubskill,
                    difficulty: difficulty || practiceDifficulty,
                    count: 8,
                    config,
                });
            }
            setPracticeQuestions(questions);
        } catch (err) {
            console.error('Failed to fetch Grade 11 Business Studies practice questions:', err);
            setPracticeError(err.message || 'Failed to generate practice questions.');
            setPracticeQuestions([]);
        } finally {
            setPracticeLoading(false);
        }
    };

    return {
        scaffoldSteps,
        stepsLoading,
        practiceSubskills,
        scaffoldQuestion,
        setScaffoldQuestion,
        scaffoldAnswer,
        setScaffoldAnswer,
        scaffoldFeedback,
        setScaffoldFeedback,
        scaffoldLoading,
        scaffoldError,
        scaffoldDifficulty,
        setScaffoldDifficulty,
        scaffoldStepIndex,
        setScaffoldStepIndex,
        scaffoldHintLevel,
        setScaffoldHintLevel,
        scaffoldShowMemo,
        setScaffoldShowMemo,
        scaffoldMasteryProgress,
        scaffoldTopicCompleted,
        scaffoldMasteryRequirements: {
            requiredSuccessCount: REQUIRED_SCAFFOLD_SUCCESSES,
            requiredDistinctEvidence: REQUIRED_DISTINCT_EVIDENCE,
            requiredDistinctFamilies: REQUIRED_DISTINCT_FAMILIES,
        },
        isScaffoldStepMastered: (stepKey) => isStepMastered(stepKey, scaffoldMasteryProgress[stepKey]),
        hasCompletedAllScaffoldSteps: hasCompletedAllSteps(scaffoldMasteryProgress),
        resetScaffoldSessionState,
        resetScaffoldSession,
        completeScaffoldTopic,
        applyScaffoldResult,
        fetchScaffoldQuestion,
        practiceQuestions,
        setPracticeQuestions,
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
        fetchPractice,
        visualAidsTab,
        setVisualAidsTab,
        visualAidsOpen,
        setVisualAidsOpen,
    };
};
