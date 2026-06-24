import React from 'react';
import WorkspaceModeShell from '../../../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../../../shared/EvaluatedWorkspaceModeShell';
import { useGrade12BusinessStudiesMarking } from '../useGrade12BusinessStudiesMarking';
import { BSGenericScaffold } from '../../../grade10/business-studies/shared/BSGenericScaffold';
import { BSGenericPractice } from '../../../grade10/business-studies/shared/BSGenericPractice';
import { BSGenericVisualAids } from '../../../grade10/business-studies/shared/BSGenericVisualAids';
import { createGrade12BSController } from './createGrade12BSController';

const h = React.createElement;

const renderBSQuestionSlot = (question, prefixText = '') => {
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

/**
 * Assembles the scaffold + practice registry entries for a single Grade 12
 * Business Studies topic from a small config object, keeping each new topic to a
 * few lines of declarative config. Mirrors the Grade 11 shared layer but uses
 * the Grade 12 marking hook (keyword-based mastery) and endpoints.
 */
export const createGrade12BSTopicRegistry = (config) => {
    const {
        topicKey,
        modePrefix,
        topicTitle,
        scaffoldSteps,
        visualAidsTitle,
        visualAidsTabs = [],
    } = config;

    const scaffoldMode = `${modePrefix}_scaffold`;
    const practiceMode = `${modePrefix}_practice`;

    const useController = createGrade12BSController({ topicKey, modePrefix, scaffoldSteps });

    const Route = ({ workspaceMode, ctx }) => {
        const controller = useController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
        const marking = useGrade12BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
        const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

        const renderVisualAids = () => h(BSGenericVisualAids, {
            title: visualAidsTitle || topicTitle,
            tabs: visualAidsTabs,
            visualAidsTab: controller.visualAidsTab,
            setVisualAidsTab: controller.setVisualAidsTab,
            setVisualAidsOpen: controller.setVisualAidsOpen,
        });

        React.useEffect(() => {
            setPracticeQuestionIndex(0);
        }, [controller.practiceQuestions]);

        const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;
        const isScaffoldLikeMode = workspaceMode === scaffoldMode;

        const commonShellProps = {
            availableModes: ['scaffold', 'practice'],
            disableSubskillControl: isScaffoldLikeMode,
            subskills: isScaffoldLikeMode ? controller.scaffoldSteps : null,
            difficulty: isScaffoldLikeMode ? controller.scaffoldDifficulty : controller.practiceDifficulty,
            setDifficulty: isScaffoldLikeMode ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
            subskill: isScaffoldLikeMode ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts') : 'mixed',
            setSubskill: (nextKey) => {
                if (isScaffoldLikeMode) {
                    const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                    if (idx >= 0) controller.setScaffoldStepIndex(idx);
                }
            },
            onGenerate: (cfg) => {
                if (isScaffoldLikeMode) {
                    controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: cfg.difficulty });
                } else {
                    marking.resetMarking();
                    controller.fetchPractice({ difficulty: cfg.difficulty });
                }
            },
        };

        if (workspaceMode === scaffoldMode) {
            const sq = controller.scaffoldQuestion;
            return h(EvaluatedWorkspaceModeShell, {
                subscriptionTier: ctx.subscriptionTier,
                workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
                onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
                renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
                selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
                ...commonShellProps,
            }, h(BSGenericScaffold, {
                topicTitle,
                scaffoldSteps: controller.scaffoldSteps,
                scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
                fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
                scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
                scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
                scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
                scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
                questionSlotEnabled: true,
                markScaffoldAnswer: async (q, ans) => {
                    const payload = await marking.markQuestions([q], { [q.id]: ans });
                    if (payload?.results && payload.results[q.id]) {
                        controller.setScaffoldFeedback(payload.results[q.id]);
                    }
                },
            }));
        }

        if (workspaceMode === practiceMode) {
            return h(WorkspaceModeShell, {
                subscriptionTier: ctx.subscriptionTier,
                workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
                questionSlot: practiceQuestionIndex >= 0
                    ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                    : null,
                selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
            }, h(BSGenericPractice, {
                topicTitle,
                practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
                fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
                practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
                practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
                currentQuestionIndex: practiceQuestionIndex,
                setCurrentQuestionIndex: setPracticeQuestionIndex,
                questionSlotEnabled: true,
                markingStatus: marking.status,
                markPracticeTest: async () => {
                    const payload = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                    if (payload?.results) {
                        controller.setPracticeFeedback({ results: payload.results, total_score: payload.total_score, max_score: payload.max_score });
                    }
                },
            }));
        }

        return null;
    };

    return {
        [scaffoldMode]: {
            render: (ctx) => h(Route, { workspaceMode: scaffoldMode, ctx }),
        },
        [practiceMode]: {
            render: (ctx) => h(Route, { workspaceMode: practiceMode, ctx }),
        },
    };
};
