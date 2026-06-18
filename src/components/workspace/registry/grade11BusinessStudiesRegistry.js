import React from 'react';
import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import { useGrade11BusinessStudiesMarking } from '../grade11/business-studies/useGrade11BusinessStudiesMarking';
import { Grade11BSInfluencesScaffold } from '../grade11/business-studies/term-1/influences-on-business-environments/Grade11BSInfluencesScaffold';
import { Grade11BSInfluencesPractice } from '../grade11/business-studies/term-1/influences-on-business-environments/Grade11BSInfluencesPractice';
import { useGrade11BSInfluencesController, Grade11BSInfluencesVisualAids } from '../grade11/business-studies/term-1/influences-on-business-environments';
import { Grade11BSChallengesScaffold } from '../grade11/business-studies/term-1/challenges-of-the-business-environments/Grade11BSChallengesScaffold';
import { Grade11BSChallengesPractice } from '../grade11/business-studies/term-1/challenges-of-the-business-environments/Grade11BSChallengesPractice';
import { useGrade11BSChallengesController, Grade11BSChallengesVisualAids } from '../grade11/business-studies/term-1/challenges-of-the-business-environments';

const h = React.createElement;

const renderQuestionSlot = (question, prefixText = '') => {
    if (!question) return null;

    return h('div', { className: 'space-y-3' }, [
        prefixText
            ? h('div', { key: 'prefix', className: 'text-sm text-slate-500' }, prefixText)
            : null,
        question?.marks
            ? h('div', { key: 'marks', className: 'inline-flex px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-semibold uppercase tracking-wide' }, `${question.marks} marks`)
            : null,
        h('h2', {
            key: 'prompt',
            className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed whitespace-pre-wrap',
        }, question?.prompt || ''),
    ].filter(Boolean));
};

const Grade11BSInfluencesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade11BSInfluencesController({ buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade11BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const isScaffoldMode = workspaceMode === 'grade11_bs_influences_on_business_environments_scaffold';
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    React.useEffect(() => {
        marking.resetMarking();
    }, [workspaceMode]);

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const renderVisualAids = () => h(Grade11BSInfluencesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const commonShellProps = {
        subscriptionTier: ctx.subscriptionTier,
        workspaceMode,
        setWorkspaceMode: ctx.setWorkspaceMode,
        onBack: ctx.onBack,
        renderVisualAids,
        selectedSubject: ctx.selectedSubject,
        selectedGrade: ctx.selectedGrade,
        topic: ctx.topic,
        availableModes: ['scaffold', 'practice'],
        questionSlot: null,
        disableSubskillControl: isScaffoldMode,
        subskills: isScaffoldMode ? controller.scaffoldSteps : controller.practiceSubskills,
        difficulty: isScaffoldMode ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: isScaffoldMode ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: isScaffoldMode
            ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts')
            : controller.practiceSubskill,
        setSubskill: (nextKey) => {
            if (isScaffoldMode) {
                const nextIndex = controller.scaffoldSteps.findIndex((step) => step.key === nextKey);
                if (nextIndex >= 0) {
                    controller.setScaffoldStepIndex(nextIndex);
                }
                return;
            }
            controller.setPracticeSubskill(nextKey);
        },
        onGenerate: (config) => {
            if (!isScaffoldMode) {
                marking.resetMarking();
                controller.fetchPractice({
                    difficulty: config.difficulty,
                    subskill: config.subskill,
                });
            }
        },
    };

    if (isScaffoldMode) {
        return h(WorkspaceModeShell, {
            ...commonShellProps,
            questionSlot: renderQuestionSlot(controller.scaffoldQuestion),
        }, h(Grade11BSInfluencesScaffold, {
            scaffoldSteps: controller.scaffoldSteps,
            scaffoldStepIndex: controller.scaffoldStepIndex,
            setScaffoldStepIndex: controller.setScaffoldStepIndex,
            scaffoldQuestion: controller.scaffoldQuestion,
            scaffoldAnswer: controller.scaffoldAnswer,
            setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback,
            setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldHintLevel: controller.scaffoldHintLevel,
            setScaffoldHintLevel: controller.setScaffoldHintLevel,
            scaffoldShowMemo: controller.scaffoldShowMemo,
            setScaffoldShowMemo: controller.setScaffoldShowMemo,
            scaffoldLoading: controller.scaffoldLoading,
            scaffoldError: controller.scaffoldError,
            scaffoldDifficulty: controller.scaffoldDifficulty,
            scaffoldMasteryProgress: controller.scaffoldMasteryProgress,
            scaffoldTopicCompleted: controller.scaffoldTopicCompleted,
            scaffoldMasteryRequirements: controller.scaffoldMasteryRequirements,
            isScaffoldStepMastered: controller.isScaffoldStepMastered,
            hasCompletedAllScaffoldSteps: controller.hasCompletedAllScaffoldSteps,
            resetScaffoldSession: controller.resetScaffoldSession,
            completeScaffoldTopic: controller.completeScaffoldTopic,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (question, answer) => {
                const payload = await marking.markQuestions([question], { [question.id]: answer });
                if (payload?.results && payload.results[question.id]) {
                    controller.applyScaffoldResult(question, payload.results[question.id]);
                }
            },
        }));
    }

    if (workspaceMode === 'grade11_bs_influences_on_business_environments_practice') {
        return h(WorkspaceModeShell, {
            ...commonShellProps,
            questionSlot: practiceQuestionIndex >= 0
                ? renderQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
        }, h(Grade11BSInfluencesPractice, {
            practiceQuestions: controller.practiceQuestions,
            practiceAnswers: controller.practiceAnswers,
            setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback,
            practiceLoading: controller.practiceLoading,
            practiceError: controller.practiceError,
            practiceDifficulty: controller.practiceDifficulty,
            practiceSubskill: controller.practiceSubskill,
            fetchPractice: controller.fetchPractice,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            markingStatus: marking.status,
            resetMarking: marking.resetMarking,
            markPracticeTest: async () => {
                const payload = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (payload?.results) {
                    controller.setPracticeFeedback({
                        results: payload.results,
                        total_score: payload.total_score,
                        max_score: payload.max_score,
                    });
                }
            },
        }));
    }

    return null;
};

const Grade11BSChallengesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade11BSChallengesController({ buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade11BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const isScaffoldMode = workspaceMode === 'grade11_bs_challenges_of_the_business_environments_scaffold';
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    React.useEffect(() => {
        marking.resetMarking();
    }, [workspaceMode]);

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const renderVisualAids = () => h(Grade11BSChallengesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const commonShellProps = {
        subscriptionTier: ctx.subscriptionTier,
        workspaceMode,
        setWorkspaceMode: ctx.setWorkspaceMode,
        onBack: ctx.onBack,
        renderVisualAids,
        selectedSubject: ctx.selectedSubject,
        selectedGrade: ctx.selectedGrade,
        topic: ctx.topic,
        availableModes: ['scaffold', 'practice'],
        questionSlot: null,
        disableSubskillControl: isScaffoldMode,
        subskills: isScaffoldMode ? controller.scaffoldSteps : controller.practiceSubskills,
        difficulty: isScaffoldMode ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: isScaffoldMode ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: isScaffoldMode
            ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts')
            : controller.practiceSubskill,
        setSubskill: (nextKey) => {
            if (isScaffoldMode) {
                const nextIndex = controller.scaffoldSteps.findIndex((step) => step.key === nextKey);
                if (nextIndex >= 0) {
                    controller.setScaffoldStepIndex(nextIndex);
                }
                return;
            }
            controller.setPracticeSubskill(nextKey);
        },
        onGenerate: (config) => {
            if (!isScaffoldMode) {
                marking.resetMarking();
                controller.fetchPractice({
                    difficulty: config.difficulty,
                    subskill: config.subskill,
                });
            }
        },
    };

    if (isScaffoldMode) {
        return h(WorkspaceModeShell, {
            ...commonShellProps,
            questionSlot: renderQuestionSlot(controller.scaffoldQuestion),
        }, h(Grade11BSChallengesScaffold, {
            scaffoldSteps: controller.scaffoldSteps,
            scaffoldStepIndex: controller.scaffoldStepIndex,
            setScaffoldStepIndex: controller.setScaffoldStepIndex,
            scaffoldQuestion: controller.scaffoldQuestion,
            scaffoldAnswer: controller.scaffoldAnswer,
            setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback,
            setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldHintLevel: controller.scaffoldHintLevel,
            setScaffoldHintLevel: controller.setScaffoldHintLevel,
            scaffoldShowMemo: controller.scaffoldShowMemo,
            setScaffoldShowMemo: controller.setScaffoldShowMemo,
            scaffoldLoading: controller.scaffoldLoading,
            scaffoldError: controller.scaffoldError,
            scaffoldDifficulty: controller.scaffoldDifficulty,
            scaffoldMasteryProgress: controller.scaffoldMasteryProgress,
            scaffoldTopicCompleted: controller.scaffoldTopicCompleted,
            scaffoldMasteryRequirements: controller.scaffoldMasteryRequirements,
            isScaffoldStepMastered: controller.isScaffoldStepMastered,
            hasCompletedAllScaffoldSteps: controller.hasCompletedAllScaffoldSteps,
            resetScaffoldSession: controller.resetScaffoldSession,
            completeScaffoldTopic: controller.completeScaffoldTopic,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (question, answer) => {
                const payload = await marking.markQuestions([question], { [question.id]: answer });
                if (payload?.results && payload.results[question.id]) {
                    controller.applyScaffoldResult(question, payload.results[question.id]);
                }
            },
        }));
    }

    if (workspaceMode === 'grade11_bs_challenges_of_the_business_environments_practice') {
        return h(WorkspaceModeShell, {
            ...commonShellProps,
            questionSlot: practiceQuestionIndex >= 0
                ? renderQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
        }, h(Grade11BSChallengesPractice, {
            practiceQuestions: controller.practiceQuestions,
            practiceAnswers: controller.practiceAnswers,
            setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback,
            practiceLoading: controller.practiceLoading,
            practiceError: controller.practiceError,
            practiceDifficulty: controller.practiceDifficulty,
            practiceSubskill: controller.practiceSubskill,
            fetchPractice: controller.fetchPractice,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            markingStatus: marking.status,
            resetMarking: marking.resetMarking,
            markPracticeTest: async () => {
                const payload = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (payload?.results) {
                    controller.setPracticeFeedback({
                        results: payload.results,
                        total_score: payload.total_score,
                        max_score: payload.max_score,
                    });
                }
            },
        }));
    }

    return null;
};

export const grade11BusinessStudiesRegistry = {
    grade11_bs_influences_on_business_environments_scaffold: {
        render: (ctx) => h(Grade11BSInfluencesRoute, {
            workspaceMode: 'grade11_bs_influences_on_business_environments_scaffold',
            ctx,
        }),
    },
    grade11_bs_influences_on_business_environments_practice: {
        render: (ctx) => h(Grade11BSInfluencesRoute, {
            workspaceMode: 'grade11_bs_influences_on_business_environments_practice',
            ctx,
        }),
    },
    grade11_bs_challenges_of_the_business_environments_scaffold: {
        render: (ctx) => h(Grade11BSChallengesRoute, {
            workspaceMode: 'grade11_bs_challenges_of_the_business_environments_scaffold',
            ctx,
        }),
    },
    grade11_bs_challenges_of_the_business_environments_practice: {
        render: (ctx) => h(Grade11BSChallengesRoute, {
            workspaceMode: 'grade11_bs_challenges_of_the_business_environments_practice',
            ctx,
        }),
    },
};
