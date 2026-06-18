import React from 'react';
import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../shared/EvaluatedWorkspaceModeShell';
import { useGrade10BusinessStudiesMarking } from '../grade10/business-studies/useGrade10BusinessStudiesMarking';
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

import { Grade10BSMicroEnvironmentScaffold } from '../grade10/business-studies/term-1/micro-environment/Grade10BSMicroEnvironmentScaffold';
import { Grade10BSMicroEnvironmentPractice } from '../grade10/business-studies/term-1/micro-environment/Grade10BSMicroEnvironmentPractice';
import { useGrade10BSMicroEnvironmentController, Grade10BSMicroEnvironmentVisualAids } from '../grade10/business-studies/term-1/micro-environment';

import { Grade10BSBusinessFunctionsScaffold } from '../grade10/business-studies/term-1/business-functions/Grade10BSBusinessFunctionsScaffold';
import { Grade10BSBusinessFunctionsPractice } from '../grade10/business-studies/term-1/business-functions/Grade10BSBusinessFunctionsPractice';
import { useGrade10BSBusinessFunctionsController, Grade10BSBusinessFunctionsVisualAids } from '../grade10/business-studies/term-1/business-functions';

import { Grade10BSMarketEnvironmentScaffold } from '../grade10/business-studies/term-1/market-environment/Grade10BSMarketEnvironmentScaffold';
import { Grade10BSMarketEnvironmentPractice } from '../grade10/business-studies/term-1/market-environment/Grade10BSMarketEnvironmentPractice';
import { useGrade10BSMarketEnvironmentController, Grade10BSMarketEnvironmentVisualAids } from '../grade10/business-studies/term-1/market-environment';

import { Grade10BSMacroEnvironmentScaffold } from '../grade10/business-studies/term-1/macro-environment/Grade10BSMacroEnvironmentScaffold';
import { Grade10BSMacroEnvironmentPractice } from '../grade10/business-studies/term-1/macro-environment/Grade10BSMacroEnvironmentPractice';
import { useGrade10BSMacroEnvironmentController, Grade10BSMacroEnvironmentVisualAids } from '../grade10/business-studies/term-1/macro-environment';

import { Grade10BSInterrelationshipScaffold } from '../grade10/business-studies/term-1/interrelationship/Grade10BSInterrelationshipScaffold';
import { Grade10BSInterrelationshipPractice } from '../grade10/business-studies/term-1/interrelationship/Grade10BSInterrelationshipPractice';
import { useGrade10BSInterrelationshipController, Grade10BSInterrelationshipVisualAids } from '../grade10/business-studies/term-1/interrelationship';

import { Grade10BSBusinessSectorsScaffold } from '../grade10/business-studies/term-1/business-sectors/Grade10BSBusinessSectorsScaffold';
import { Grade10BSBusinessSectorsPractice } from '../grade10/business-studies/term-1/business-sectors/Grade10BSBusinessSectorsPractice';
import { useGrade10BSBusinessSectorsController, Grade10BSBusinessSectorsVisualAids } from '../grade10/business-studies/term-1/business-sectors';

import { Grade10BSSocioEconomicIssuesScaffold } from '../grade10/business-studies/term-2/socio-economic-issues/Grade10BSSocioEconomicIssuesScaffold';
import { Grade10BSSocioEconomicIssuesPractice } from '../grade10/business-studies/term-2/socio-economic-issues/Grade10BSSocioEconomicIssuesPractice';
import { useGrade10BSSocioEconomicIssuesController, Grade10BSSocioEconomicIssuesVisualAids } from '../grade10/business-studies/term-2/socio-economic-issues';

import { Grade10BSSocialResponsibilityScaffold } from '../grade10/business-studies/term-2/social-responsibility/Grade10BSSocialResponsibilityScaffold';
import { Grade10BSSocialResponsibilityPractice } from '../grade10/business-studies/term-2/social-responsibility/Grade10BSSocialResponsibilityPractice';
import { useGrade10BSSocialResponsibilityController, Grade10BSSocialResponsibilityVisualAids } from '../grade10/business-studies/term-2/social-responsibility';

import { Grade10BSEntrepreneurialQualitiesScaffold } from '../grade10/business-studies/term-2/entrepreneurial-qualities/Grade10BSEntrepreneurialQualitiesScaffold';
import { Grade10BSEntrepreneurialQualitiesPractice } from '../grade10/business-studies/term-2/entrepreneurial-qualities/Grade10BSEntrepreneurialQualitiesPractice';
import { useGrade10BSEntrepreneurialQualitiesController, Grade10BSEntrepreneurialQualitiesVisualAids } from '../grade10/business-studies/term-2/entrepreneurial-qualities';

import { Grade10BSFormsOfOwnershipScaffold } from '../grade10/business-studies/term-2/forms-of-ownership/Grade10BSFormsOfOwnershipScaffold';
import { Grade10BSFormsOfOwnershipPractice } from '../grade10/business-studies/term-2/forms-of-ownership/Grade10BSFormsOfOwnershipPractice';
import { useGrade10BSFormsOfOwnershipController, Grade10BSFormsOfOwnershipVisualAids } from '../grade10/business-studies/term-2/forms-of-ownership';

import { Grade10BSConceptOfQualityScaffold } from '../grade10/business-studies/term-2/concept-of-quality/Grade10BSConceptOfQualityScaffold';
import { Grade10BSConceptOfQualityPractice } from '../grade10/business-studies/term-2/concept-of-quality/Grade10BSConceptOfQualityPractice';
import { useGrade10BSConceptOfQualityController, Grade10BSConceptOfQualityVisualAids } from '../grade10/business-studies/term-2/concept-of-quality';


const Grade10BSMicroEnvironmentRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSMicroEnvironmentController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSMicroEnvironmentVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_micro_environment_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_micro_environment_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSMicroEnvironmentScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_micro_environment_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSMicroEnvironmentPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSBusinessFunctionsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSBusinessFunctionsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSBusinessFunctionsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_business_functions_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_business_functions_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSBusinessFunctionsScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_business_functions_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSBusinessFunctionsPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSMarketEnvironmentRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSMarketEnvironmentController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSMarketEnvironmentVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_market_environment_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_market_environment_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSMarketEnvironmentScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_market_environment_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSMarketEnvironmentPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSMacroEnvironmentRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSMacroEnvironmentController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSMacroEnvironmentVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_macro_environment_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_macro_environment_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSMacroEnvironmentScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_macro_environment_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSMacroEnvironmentPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSInterrelationshipRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSInterrelationshipController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSInterrelationshipVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_interrelationship_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_interrelationship_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSInterrelationshipScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_interrelationship_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSInterrelationshipPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSBusinessSectorsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSBusinessSectorsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSBusinessSectorsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_business_sectors_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_business_sectors_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSBusinessSectorsScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_business_sectors_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSBusinessSectorsPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSSocioEconomicIssuesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSSocioEconomicIssuesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSSocioEconomicIssuesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_socio_economic_issues_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_socio_economic_issues_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSSocioEconomicIssuesScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_socio_economic_issues_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSSocioEconomicIssuesPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSSocialResponsibilityRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSSocialResponsibilityController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSSocialResponsibilityVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_social_responsibility_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_social_responsibility_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSSocialResponsibilityScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_social_responsibility_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSSocialResponsibilityPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSEntrepreneurialQualitiesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSEntrepreneurialQualitiesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSEntrepreneurialQualitiesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_entrepreneurial_qualities_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_entrepreneurial_qualities_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSEntrepreneurialQualitiesScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_entrepreneurial_qualities_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSEntrepreneurialQualitiesPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSFormsOfOwnershipRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSFormsOfOwnershipController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSFormsOfOwnershipVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_forms_of_ownership_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_forms_of_ownership_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSFormsOfOwnershipScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            questionSlotEnabled: true,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_forms_of_ownership_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSFormsOfOwnershipPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};

const Grade10BSConceptOfQualityRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BSConceptOfQualityController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });
    const [practiceQuestionIndex, setPracticeQuestionIndex] = React.useState(0);

    const renderVisualAids = () => h(Grade10BSConceptOfQualityVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    React.useEffect(() => {
        setPracticeQuestionIndex(0);
    }, [controller.practiceQuestions]);

    const currentPracticeQuestion = controller.practiceQuestions?.[practiceQuestionIndex] || null;

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_concept_of_quality_scaffold';

    const commonShellProps = {
        availableModes: ['scaffold', 'practice'],
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
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_bs_concept_of_quality_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderBSQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BSConceptOfQualityScaffold, {
            onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            scaffoldDifficulty: controller.scaffoldDifficulty, setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex, setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading, scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion, scaffoldAnswer: controller.scaffoldAnswer, setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback, setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint, setScaffoldShowHint: controller.setScaffoldShowHint,
            markScaffoldAnswer: async (q, ans) => {
                const resultsObj = await marking.markQuestions([q], { [q.id]: ans });
                if (resultsObj && resultsObj[q.id]) {
                    controller.setScaffoldFeedback(resultsObj[q.id]);
                }
            }
        }));
    }

    if (workspaceMode === 'grade10_bs_concept_of_quality_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: practiceQuestionIndex >= 0
                ? renderBSQuestionSlot(currentPracticeQuestion, controller.practiceQuestions?.length > 0 ? `Question ${practiceQuestionIndex + 1} of ${controller.practiceQuestions.length}` : '')
                : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BSConceptOfQualityPractice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
            currentQuestionIndex: practiceQuestionIndex,
            setCurrentQuestionIndex: setPracticeQuestionIndex,
            questionSlotEnabled: true,
            markingStatus: marking.status,
            markPracticeTest: async () => {
                const resultsObj = await marking.markQuestions(controller.practiceQuestions, controller.practiceAnswers);
                if (resultsObj) {
                    controller.setPracticeFeedback({ results: resultsObj, total_score: marking.scoreState.totalScore, max_score: marking.scoreState.maxScore });
                }
            }
        }));
    }
    return null;
};


export const grade10BusinessStudiesRegistry = {
    grade10_bs_micro_environment_scaffold: {
        render: (ctx) => h(Grade10BSMicroEnvironmentRoute, { workspaceMode: 'grade10_bs_micro_environment_scaffold', ctx }),
    },
    grade10_bs_micro_environment_practice: {
        render: (ctx) => h(Grade10BSMicroEnvironmentRoute, { workspaceMode: 'grade10_bs_micro_environment_practice', ctx }),
    },
    grade10_bs_business_functions_scaffold: {
        render: (ctx) => h(Grade10BSBusinessFunctionsRoute, { workspaceMode: 'grade10_bs_business_functions_scaffold', ctx }),
    },
    grade10_bs_business_functions_practice: {
        render: (ctx) => h(Grade10BSBusinessFunctionsRoute, { workspaceMode: 'grade10_bs_business_functions_practice', ctx }),
    },
    grade10_bs_market_environment_scaffold: {
        render: (ctx) => h(Grade10BSMarketEnvironmentRoute, { workspaceMode: 'grade10_bs_market_environment_scaffold', ctx }),
    },
    grade10_bs_market_environment_practice: {
        render: (ctx) => h(Grade10BSMarketEnvironmentRoute, { workspaceMode: 'grade10_bs_market_environment_practice', ctx }),
    },
    grade10_bs_macro_environment_scaffold: {
        render: (ctx) => h(Grade10BSMacroEnvironmentRoute, { workspaceMode: 'grade10_bs_macro_environment_scaffold', ctx }),
    },
    grade10_bs_macro_environment_practice: {
        render: (ctx) => h(Grade10BSMacroEnvironmentRoute, { workspaceMode: 'grade10_bs_macro_environment_practice', ctx }),
    },
    grade10_bs_interrelationship_scaffold: {
        render: (ctx) => h(Grade10BSInterrelationshipRoute, { workspaceMode: 'grade10_bs_interrelationship_scaffold', ctx }),
    },
    grade10_bs_interrelationship_practice: {
        render: (ctx) => h(Grade10BSInterrelationshipRoute, { workspaceMode: 'grade10_bs_interrelationship_practice', ctx }),
    },
    grade10_bs_business_sectors_scaffold: {
        render: (ctx) => h(Grade10BSBusinessSectorsRoute, { workspaceMode: 'grade10_bs_business_sectors_scaffold', ctx }),
    },
    grade10_bs_business_sectors_practice: {
        render: (ctx) => h(Grade10BSBusinessSectorsRoute, { workspaceMode: 'grade10_bs_business_sectors_practice', ctx }),
    },
    grade10_bs_socio_economic_issues_scaffold: {
        render: (ctx) => h(Grade10BSSocioEconomicIssuesRoute, { workspaceMode: 'grade10_bs_socio_economic_issues_scaffold', ctx }),
    },
    grade10_bs_socio_economic_issues_practice: {
        render: (ctx) => h(Grade10BSSocioEconomicIssuesRoute, { workspaceMode: 'grade10_bs_socio_economic_issues_practice', ctx }),
    },
    grade10_bs_social_responsibility_scaffold: {
        render: (ctx) => h(Grade10BSSocialResponsibilityRoute, { workspaceMode: 'grade10_bs_social_responsibility_scaffold', ctx }),
    },
    grade10_bs_social_responsibility_practice: {
        render: (ctx) => h(Grade10BSSocialResponsibilityRoute, { workspaceMode: 'grade10_bs_social_responsibility_practice', ctx }),
    },
    grade10_bs_entrepreneurial_qualities_scaffold: {
        render: (ctx) => h(Grade10BSEntrepreneurialQualitiesRoute, { workspaceMode: 'grade10_bs_entrepreneurial_qualities_scaffold', ctx }),
    },
    grade10_bs_entrepreneurial_qualities_practice: {
        render: (ctx) => h(Grade10BSEntrepreneurialQualitiesRoute, { workspaceMode: 'grade10_bs_entrepreneurial_qualities_practice', ctx }),
    },
    grade10_bs_forms_of_ownership_scaffold: {
        render: (ctx) => h(Grade10BSFormsOfOwnershipRoute, { workspaceMode: 'grade10_bs_forms_of_ownership_scaffold', ctx }),
    },
    grade10_bs_forms_of_ownership_practice: {
        render: (ctx) => h(Grade10BSFormsOfOwnershipRoute, { workspaceMode: 'grade10_bs_forms_of_ownership_practice', ctx }),
    },
    grade10_bs_concept_of_quality_scaffold: {
        render: (ctx) => h(Grade10BSConceptOfQualityRoute, { workspaceMode: 'grade10_bs_concept_of_quality_scaffold', ctx }),
    },
    grade10_bs_concept_of_quality_practice: {
        render: (ctx) => h(Grade10BSConceptOfQualityRoute, { workspaceMode: 'grade10_bs_concept_of_quality_practice', ctx }),
    },
};
