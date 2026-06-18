import React from 'react';
import Grade12AccountingScaffold from '../grade12/accounting/Grade12AccountingScaffold';
import Grade12PatternsSequencesSeriesScaffold from '../grade12/mathematics/patterns-sequences-series/Grade12PatternsSequencesSeriesScaffold';
import Grade12PatternsSequencesSeriesPractice from '../grade12/mathematics/patterns-sequences-series/Grade12PatternsSequencesSeriesPractice';
import Grade12FunctionsScaffold from '../grade12/mathematics/functions/Grade12FunctionsScaffold';
import Grade12FunctionsPractice from '../grade12/mathematics/functions/Grade12FunctionsPractice';
import Grade12FinanceScaffold from '../grade12/mathematics/finance/Grade12FinanceScaffold';
import Grade12FinancePractice from '../grade12/mathematics/finance/Grade12FinancePractice';
import Grade12TrigonometryScaffold from '../grade12/mathematics/trigonometry/Grade12TrigonometryScaffold';
import Grade12TrigonometryPractice from '../grade12/mathematics/trigonometry/Grade12TrigonometryPractice';

import { useGrade12AccountingController, Grade12AccountingVisualAids } from '../grade12/accounting';
import { useGrade12PatternsSequencesSeriesController, Grade12PatternsSequencesSeriesVisualAids } from '../grade12/mathematics/patterns-sequences-series';
import { useGrade12FunctionsController, Grade12FunctionsVisualAids } from '../grade12/mathematics/functions';
import { useGrade12FinanceController, Grade12FinanceVisualAids } from '../grade12/mathematics/finance';
import { useGrade12TrigonometryController, Grade12TrigonometryVisualAids } from '../grade12/mathematics/trigonometry';

import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../shared/EvaluatedWorkspaceModeShell';

const h = React.createElement;

const Grade12AccountingRoute = ({ workspaceMode, ctx, subskills, defaultSubskill }) => {
    const controller = useGrade12AccountingController({ workspaceMode, buildApiUrl: ctx.buildApiUrl, subskills, defaultSubskill });

    // State for Practice Navigation
    const [practiceIndex, setPracticeIndex] = React.useState(0);

    // Reset index when mode or subskill changes
    React.useEffect(() => {
        setPracticeIndex(0);
    }, [workspaceMode, controller.practiceSubskill]);

    // Derived current question for practice
    const currentPracticeQuestion = controller.practiceQuestions?.[practiceIndex];

    const renderGrade12AccountingVisualAids = () => h(Grade12AccountingVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const commonShellProps = {
        availableModes: ['scaffold', 'practice', 'marking'],
        subskills: controller.subskills,
        difficulty: workspaceMode.endsWith('_scaffold') ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: workspaceMode.endsWith('_scaffold') ? controller.scaffoldSubskill : controller.practiceSubskill,
        setSubskill: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldSubskill : controller.setPracticeSubskill,
        onGenerate: (config) => {
            if (workspaceMode.endsWith('_scaffold')) {
                controller.fetchScaffoldQuestion({
                    difficulty: config.difficulty,
                    subskill: config.subskill,
                    seed: controller.scaffoldSeed
                });
            } else {
                setPracticeIndex(0);
                controller.fetchPractice({
                    difficulty: config.difficulty,
                    subskill: config.subskill,
                    seed: controller.practiceSeed
                });
            }
        }
    };

    if (workspaceMode.includes('grade12_accounting_') && (workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking'))) {
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            question: controller.scaffoldQuestion,
            userAnswersCells: controller.scaffoldAnswer?.cells || {},
            questionSlot: h('div', { className: "prose prose-sm max-w-none text-gray-900" }, [
                h('h3', { key: 'title', className: "text-lg font-semibold mb-2" }, controller.scaffoldQuestion?.title || 'Question'),
                h('div', { key: 'prompt', className: "whitespace-pre-wrap" }, controller.scaffoldQuestion?.prompt)
            ]),
            onNext: () => {
                controller.fetchScaffoldQuestion({
                    difficulty: controller.scaffoldDifficulty,
                    subskill: controller.scaffoldSubskill,
                    seed: Math.floor(Math.random() * 2147483647)
                });
            },
            renderVisualAids: renderGrade12AccountingVisualAids,
            ...commonShellProps,
        }, h(Grade12AccountingScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'),
            onBack: ctx.onBack,
            subskills: controller.subskills,
            g12AcctVisualAidsOpen: controller.visualAidsOpen,
            setG12AcctVisualAidsOpen: controller.setVisualAidsOpen,
            g12AcctScaffoldDifficulty: controller.scaffoldDifficulty,
            setG12AcctScaffoldDifficulty: controller.setScaffoldDifficulty,
            g12AcctScaffoldSubskill: controller.scaffoldSubskill,
            setG12AcctScaffoldSubskill: controller.setScaffoldSubskill,
            g12AcctScaffoldSeed: controller.scaffoldSeed,
            setG12AcctScaffoldSeed: controller.setScaffoldSeed,
            fetchGrade12AccountingScaffoldQuestion: controller.fetchScaffoldQuestion,
            g12AcctScaffoldLoading: controller.scaffoldLoading,
            g12AcctScaffoldError: controller.scaffoldError,
            g12AcctScaffoldQuestion: controller.scaffoldQuestion,
            g12AcctScaffoldAnswer: controller.scaffoldAnswer,
            setG12AcctScaffoldAnswer: controller.setScaffoldAnswer,
            g12AcctScaffoldFeedback: controller.scaffoldFeedback,
            setG12AcctScaffoldFeedback: controller.setScaffoldFeedback,
            g12AcctScaffoldShowHint: controller.scaffoldShowHint,
            setG12AcctShowHint: controller.setScaffoldShowHint,
            renderGrade12AccountingVisualAids,
            hideConfig: true,
        }));
    }

    if (workspaceMode.includes('grade12_accounting_') && workspaceMode.endsWith('_practice')) {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            ...commonShellProps,
            // Visual Aids disabled for practice as per user request (or consistent with Grade 10/11 practice?)
            // User request: "no visual aid for practice"
            renderVisualAids: null,
            questionSlot: h('div', { className: "prose prose-sm max-w-none text-gray-900" }, [
                h('h3', { className: "text-lg font-semibold mb-2" }, `Question ${practiceIndex + 1}`),
                h('div', { className: "whitespace-pre-wrap" }, currentPracticeQuestion?.prompt || 'Loading...')
            ]),
            onNext: () => {
                if (controller.practiceQuestions && practiceIndex < controller.practiceQuestions.length - 1) {
                    setPracticeIndex(prev => prev + 1);
                }
            },
            onPrevious: () => {
                if (practiceIndex > 0) {
                    setPracticeIndex(prev => prev - 1);
                }
            },
            canGoNext: controller.practiceQuestions && practiceIndex < controller.practiceQuestions.length - 1,
            canGoPrevious: practiceIndex > 0,
        }, h(Grade12AccountingPractice, {
            onBack: ctx.onBack,
            subskills: controller.subskills,
            g12AcctVisualAidsOpen: controller.visualAidsOpen,
            setG12AcctVisualAidsOpen: controller.setVisualAidsOpen,
            g12AcctPracticeDifficulty: controller.practiceDifficulty,
            setG12AcctPracticeDifficulty: controller.setPracticeDifficulty,
            g12AcctPracticeSubskill: controller.practiceSubskill,
            setG12AcctPracticeSubskill: controller.setPracticeSubskill,
            g12AcctPracticeSeed: controller.practiceSeed,
            setG12AcctPracticeSeed: controller.setPracticeSeed,
            fetchGrade12AccountingPractice: (params) => {
                setPracticeIndex(0);
                controller.fetchPractice(params);
            },
            g12AcctPracticeLoading: controller.practiceLoading,
            g12AcctPracticeError: controller.practiceError,
            g12AcctPracticeQuestions: controller.practiceQuestions,
            g12AcctPracticeAnswers: controller.practiceAnswers,
            setG12AcctPracticeAnswers: controller.setPracticeAnswers,
            g12AcctPracticeFeedback: controller.practiceFeedback,
            setG12AcctPracticeFeedback: controller.setPracticeFeedback,
            renderGrade12AccountingVisualAids,
            hideConfig: true,
            currentIndex: practiceIndex,
        }));
    }

    return null;
};

const Grade12FinanceRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade12FinanceController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade12FinanceVisualAids = () => h(Grade12FinanceVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade12_finance_scaffold') {
        return h(Grade12FinanceScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g12FinanceVisualAidsOpen: controller.visualAidsOpen,
            setG12FinanceVisualAidsOpen: controller.setVisualAidsOpen,
            g12FinanceScaffoldDifficulty: controller.scaffoldDifficulty,
            setG12FinanceScaffoldDifficulty: controller.setScaffoldDifficulty,
            g12FinanceScaffoldStepIndex: controller.scaffoldStepIndex,
            setG12FinanceScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade12FinanceScaffoldQuestion: controller.fetchScaffoldQuestion,
            g12FinanceScaffoldLoading: controller.scaffoldLoading,
            g12FinanceScaffoldError: controller.scaffoldError,
            g12FinanceScaffoldQuestion: controller.scaffoldQuestion,
            g12FinanceScaffoldAnswer: controller.scaffoldAnswer,
            setG12FinanceScaffoldAnswer: controller.setScaffoldAnswer,
            g12FinanceScaffoldFeedback: controller.scaffoldFeedback,
            setG12FinanceScaffoldFeedback: controller.setScaffoldFeedback,
            g12FinanceScaffoldShowHint: controller.scaffoldShowHint,
            setG12FinanceScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade12FinanceVisualAids,
        });
    }

    if (workspaceMode === 'grade12_finance_practice') {
        return h(Grade12FinancePractice, {
            onBack: ctx.onBack,
            g12FinanceVisualAidsOpen: controller.visualAidsOpen,
            setG12FinanceVisualAidsOpen: controller.setVisualAidsOpen,
            g12FinancePracticeDifficulty: controller.practiceDifficulty,
            setG12FinancePracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade12FinancePractice: controller.fetchPractice,
            g12FinancePracticeLoading: controller.practiceLoading,
            g12FinancePracticeError: controller.practiceError,
            g12FinancePracticeQuestions: controller.practiceQuestions,
            g12FinancePracticeAnswers: controller.practiceAnswers,
            setG12FinancePracticeAnswers: controller.setPracticeAnswers,
            g12FinancePracticeFeedback: controller.practiceFeedback,
            setG12FinancePracticeFeedback: controller.setPracticeFeedback,
            renderGrade12FinanceVisualAids,
        });
    }

    return null;
};

const Grade12PatternsSequencesSeriesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade12PatternsSequencesSeriesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade12PssVisualAids = () => h(Grade12PatternsSequencesSeriesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade12_patterns_sequences_series_scaffold') {
        return h(Grade12PatternsSequencesSeriesScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g12PssVisualAidsOpen: controller.visualAidsOpen,
            setG12PssVisualAidsOpen: controller.setVisualAidsOpen,
            g12PssScaffoldDifficulty: controller.scaffoldDifficulty,
            setG12PssScaffoldDifficulty: controller.setScaffoldDifficulty,
            g12PssScaffoldStepIndex: controller.scaffoldStepIndex,
            setG12PssScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade12PatternsSequencesSeriesScaffoldQuestion: controller.fetchScaffoldQuestion,
            g12PssScaffoldLoading: controller.scaffoldLoading,
            g12PssScaffoldError: controller.scaffoldError,
            g12PssScaffoldQuestion: controller.scaffoldQuestion,
            g12PssScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG12PssScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g12PssScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG12PssScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g12PssScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG12PssScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            g12PssScaffoldAnswer: controller.scaffoldAnswer,
            setG12PssScaffoldAnswer: controller.setScaffoldAnswer,
            g12PssScaffoldFeedback: controller.scaffoldFeedback,
            setG12PssScaffoldFeedback: controller.setScaffoldFeedback,
            g12PssScaffoldShowHint: controller.scaffoldShowHint,
            setG12PssScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade12PatternsSequencesSeriesVisualAids: renderGrade12PssVisualAids,
        });
    }

    if (workspaceMode === 'grade12_patterns_sequences_series_practice') {
        return h(Grade12PatternsSequencesSeriesPractice, {
            onBack: ctx.onBack,
            g12PssVisualAidsOpen: controller.visualAidsOpen,
            setG12PssVisualAidsOpen: controller.setVisualAidsOpen,
            g12PssPracticeDifficulty: controller.practiceDifficulty,
            setG12PssPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade12PatternsSequencesSeriesPractice: controller.fetchPractice,
            g12PssPracticeLoading: controller.practiceLoading,
            g12PssPracticeError: controller.practiceError,
            g12PssPracticeQuestions: controller.practiceQuestions,
            g12PssPracticeAnswers: controller.practiceAnswers,
            setG12PssPracticeAnswers: controller.setPracticeAnswers,
            g12PssPracticeFeedback: controller.practiceFeedback,
            setG12PssPracticeFeedback: controller.setPracticeFeedback,
            renderGrade12PatternsSequencesSeriesVisualAids: renderGrade12PssVisualAids,
        });
    }

    return null;
};

const Grade12FunctionsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade12FunctionsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade12FunctionsVisualAids = () => h(Grade12FunctionsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade12_functions_scaffold') {
        return h(Grade12FunctionsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g12FunctionsVisualAidsOpen: controller.visualAidsOpen,
            setG12FunctionsVisualAidsOpen: controller.setVisualAidsOpen,
            g12FunctionsScaffoldDifficulty: controller.scaffoldDifficulty,
            setG12FunctionsScaffoldDifficulty: controller.setScaffoldDifficulty,
            g12FunctionsScaffoldStepIndex: controller.scaffoldStepIndex,
            setG12FunctionsScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade12FunctionsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g12FunctionsScaffoldLoading: controller.scaffoldLoading,
            g12FunctionsScaffoldError: controller.scaffoldError,
            g12FunctionsScaffoldQuestion: controller.scaffoldQuestion,
            g12FunctionsScaffoldAnswer: controller.scaffoldAnswer,
            setG12FunctionsScaffoldAnswer: controller.setG12FunctionsScaffoldAnswer,
            g12FunctionsScaffoldFeedback: controller.scaffoldFeedback,
            setG12FunctionsScaffoldFeedback: controller.setG12FunctionsScaffoldFeedback,
            g12FunctionsScaffoldShowHint: controller.scaffoldShowHint,
            setG12FunctionsScaffoldShowHint: controller.setG12FunctionsScaffoldShowHint,
            renderGrade12FunctionsVisualAids,
        });
    }

    if (workspaceMode === 'grade12_functions_practice') {
        return h(Grade12FunctionsPractice, {
            onBack: ctx.onBack,
            g12FunctionsVisualAidsOpen: controller.visualAidsOpen,
            setG12FunctionsVisualAidsOpen: controller.setVisualAidsOpen,
            g12FunctionsPracticeDifficulty: controller.practiceDifficulty,
            setG12FunctionsPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade12FunctionsPractice: controller.fetchPractice,
            g12FunctionsPracticeLoading: controller.practiceLoading,
            g12FunctionsPracticeError: controller.practiceError,
            g12FunctionsPracticeQuestions: controller.practiceQuestions,
            g12FunctionsPracticeAnswers: controller.practiceAnswers,
            setG12FunctionsPracticeAnswers: controller.setPracticeAnswers,
            g12FunctionsPracticeFeedback: controller.practiceFeedback,
            setG12FunctionsPracticeFeedback: controller.setPracticeFeedback,
            renderGrade12FunctionsVisualAids,
        });
    }

    return null;
};

const Grade12TrigonometryRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade12TrigonometryController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade12TrigVisualAids = () => h(Grade12TrigonometryVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade12_trigonometry_scaffold') {
        return h(Grade12TrigonometryScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g12TrigVisualAidsOpen: controller.visualAidsOpen,
            setG12TrigVisualAidsOpen: controller.setVisualAidsOpen,
            g12TrigScaffoldDifficulty: controller.scaffoldDifficulty,
            setG12TrigScaffoldDifficulty: controller.setScaffoldDifficulty,
            g12TrigScaffoldStepIndex: controller.scaffoldStepIndex,
            setG12TrigScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade12TrigScaffoldQuestion: controller.fetchScaffoldQuestion,
            g12TrigScaffoldLoading: controller.scaffoldLoading,
            g12TrigScaffoldError: controller.scaffoldError,
            g12TrigScaffoldQuestion: controller.scaffoldQuestion,
            g12TrigScaffoldAnswer: controller.scaffoldAnswer,
            setG12TrigScaffoldAnswer: controller.setG12TrigScaffoldAnswer,
            g12TrigScaffoldFeedback: controller.scaffoldFeedback,
            setG12TrigScaffoldFeedback: controller.setG12TrigScaffoldFeedback,
            g12TrigScaffoldShowHint: controller.scaffoldShowHint,
            setG12TrigScaffoldShowHint: controller.setG12TrigScaffoldShowHint,
            renderGrade12TrigVisualAids: renderGrade12TrigVisualAids,
        });
    }

    if (workspaceMode === 'grade12_trigonometry_practice') {
        return h(Grade12TrigonometryPractice, {
            onBack: ctx.onBack,
            g12TrigVisualAidsOpen: controller.visualAidsOpen,
            setG12TrigVisualAidsOpen: controller.setVisualAidsOpen,
            g12TrigPracticeDifficulty: controller.practiceDifficulty,
            setG12TrigPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade12TrigPractice: controller.fetchPractice,
            g12TrigPracticeLoading: controller.practiceLoading,
            g12TrigPracticeError: controller.practiceError,
            g12TrigPracticeQuestions: controller.practiceQuestions,
            g12TrigPracticeAnswers: controller.practiceAnswers,
            setG12TrigPracticeAnswers: controller.setPracticeAnswers,
            g12TrigPracticeFeedback: controller.practiceFeedback,
            setG12TrigPracticeFeedback: controller.setPracticeFeedback,
            renderGrade12TrigVisualAids: renderGrade12TrigVisualAids,
        });
    }

    return null;
};

export const grade12Registry = {
    grade12_trigonometry_scaffold: {
        render: (ctx) => h(Grade12TrigonometryRoute, { workspaceMode: 'grade12_trigonometry_scaffold', ctx }),
    },
    grade12_trigonometry_practice: {
        render: (ctx) => h(Grade12TrigonometryRoute, { workspaceMode: 'grade12_trigonometry_practice', ctx }),
    },
    grade12_finance_scaffold: {
        render: (ctx) => h(Grade12FinanceRoute, { workspaceMode: 'grade12_finance_scaffold', ctx }),
    },
    grade12_finance_practice: {
        render: (ctx) => h(Grade12FinanceRoute, { workspaceMode: 'grade12_finance_practice', ctx }),
    },
    grade12_functions_scaffold: {
        render: (ctx) => h(Grade12FunctionsRoute, { workspaceMode: 'grade12_functions_scaffold', ctx }),
    },
    grade12_functions_practice: {
        render: (ctx) => h(Grade12FunctionsRoute, { workspaceMode: 'grade12_functions_practice', ctx }),
    },
    grade12_patterns_sequences_series_scaffold: {
        render: (ctx) => h(Grade12PatternsSequencesSeriesRoute, { workspaceMode: 'grade12_patterns_sequences_series_scaffold', ctx }),
    },
    grade12_patterns_sequences_series_practice: {
        render: (ctx) => h(Grade12PatternsSequencesSeriesRoute, { workspaceMode: 'grade12_patterns_sequences_series_practice', ctx }),
    },
    // --- GRADE 12 ACCOUNTING ROUTES (Split) ---
    // 1. Concepts
    grade12_accounting_concepts_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_concepts_scaffold',
            ctx,
            subskills: [
                { key: 'concepts', title: 'Concepts (Companies)' }
            ],
            defaultSubskill: 'concepts'
        }),
    },
    grade12_accounting_concepts_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_concepts_practice',
            ctx,
            subskills: [
                { key: 'concepts', title: 'Concepts (Companies)' }
            ],
            defaultSubskill: 'concepts'
        }),
    },

    // 2. Bookkeeping (General Ledger)
    grade12_accounting_bookkeeping_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_bookkeeping_scaffold',
            ctx,
            subskills: [
                { key: 'company-general-ledger', title: 'Bookkeeping of companies (General Ledger)' }
            ],
            defaultSubskill: 'company-general-ledger'
        }),
    },
    grade12_accounting_bookkeeping_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_bookkeeping_practice',
            ctx,
            subskills: [
                { key: 'company-general-ledger', title: 'Bookkeeping of companies (General Ledger)' }
            ],
            defaultSubskill: 'company-general-ledger'
        }),
    },

    // 3. Financial Statements & Notes (Includes Cash Flow)
    grade12_accounting_finance_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_finance_scaffold',
            ctx,
            subskills: [
                { key: 'financial-statements-notes', title: 'Financial statements & notes' },
                { key: 'cash-flow', title: 'Cash Flow Statement' }
            ],
            defaultSubskill: 'financial-statements-notes'
        }),
    },
    grade12_accounting_finance_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_finance_practice',
            ctx,
            subskills: [
                { key: 'financial-statements-notes', title: 'Financial statements & notes' },
                { key: 'cash-flow', title: 'Cash Flow Statement' }
            ],
            defaultSubskill: 'financial-statements-notes'
        }),
    },

    // 4. Analysis & Interpretation
    grade12_accounting_analysis_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_analysis_scaffold',
            ctx,
            subskills: [
                { key: 'analysis-interpretation', title: 'Analysis & interpretation of financial statements' }
            ],
            defaultSubskill: 'analysis-interpretation'
        }),
    },
    grade12_accounting_analysis_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_analysis_practice',
            ctx,
            subskills: [
                { key: 'analysis-interpretation', title: 'Analysis & interpretation of financial statements' }
            ],
            defaultSubskill: 'analysis-interpretation'
        }),
    },

    // 5. Audits, Corporate Governance & Shareholding
    grade12_accounting_audits_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_audits_scaffold',
            ctx,
            subskills: [
                { key: 'audits-governance-shareholding', title: 'Audits, Corporate Governance & Shareholding' }
            ],
            defaultSubskill: 'audits-governance-shareholding'
        }),
    },
    grade12_accounting_audits_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_audits_practice',
            ctx,
            subskills: [
                { key: 'audits-governance-shareholding', title: 'Audits, Corporate Governance & Shareholding' }
            ],
            defaultSubskill: 'audits-governance-shareholding'
        }),
    },

    // --- GRADE 12 ACCOUNTING TERM 2 ---

    // 6. Fixed / Tangible Assets (Term 2)
    grade12_accounting_fixed_assets_t2_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_fixed_assets_t2_scaffold',
            ctx,
            subskills: [
                { key: 'fixed-assets-t2', title: 'Fixed / Tangible Assets' }
            ],
            defaultSubskill: 'fixed-assets-t2'
        }),
    },
    grade12_accounting_fixed_assets_t2_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_fixed_assets_t2_practice',
            ctx,
            subskills: [
                { key: 'fixed-assets-t2', title: 'Fixed / Tangible Assets' }
            ],
            defaultSubskill: 'fixed-assets-t2'
        }),
    },
    grade12_accounting_fixed_assets_t2_marking: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_fixed_assets_t2_marking',
            ctx,
            subskills: [
                { key: 'fixed-assets-t2', title: 'Fixed / Tangible Assets' }
            ],
            defaultSubskill: 'fixed-assets-t2'
        }),
    },

    // 7. Inventory Systems (Term 2)
    grade12_accounting_inventory_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_inventory_scaffold',
            ctx,
            subskills: [
                { key: 'inventory-systems', title: 'Inventory Systems' }
            ],
            defaultSubskill: 'inventory-systems'
        }),
    },
    grade12_accounting_inventory_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_inventory_practice',
            ctx,
            subskills: [
                { key: 'inventory-systems', title: 'Inventory Systems' }
            ],
            defaultSubskill: 'inventory-systems'
        }),
    },
    grade12_accounting_inventory_marking: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_inventory_marking',
            ctx,
            subskills: [
                { key: 'inventory-systems', title: 'Inventory Systems' }
            ],
            defaultSubskill: 'inventory-systems'
        }),
    },

    // 8. Reconciliation (Term 2)
    grade12_accounting_reconciliation_t2_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_reconciliation_t2_scaffold',
            ctx,
            subskills: [
                { key: 'reconciliation-t2', title: 'Reconciliations' }
            ],
            defaultSubskill: 'reconciliation-t2'
        }),
    },
    grade12_accounting_reconciliation_t2_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_reconciliation_t2_practice',
            ctx,
            subskills: [
                { key: 'reconciliation-t2', title: 'Reconciliations' }
            ],
            defaultSubskill: 'reconciliation-t2'
        }),
    },
    grade12_accounting_reconciliation_t2_marking: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_reconciliation_t2_marking',
            ctx,
            subskills: [
                { key: 'reconciliation-t2', title: 'Reconciliations' }
            ],
            defaultSubskill: 'reconciliation-t2'
        }),
    },

    // 9. Value Added Tax (Term 2)
    grade12_accounting_vat_t2_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_vat_t2_scaffold',
            ctx,
            subskills: [
                { key: 'vat-t2', title: 'Value Added Tax (VAT)' }
            ],
            defaultSubskill: 'vat-t2'
        }),
    },
    grade12_accounting_vat_t2_practice: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_vat_t2_practice',
            ctx,
            subskills: [
                { key: 'vat-t2', title: 'Value Added Tax (VAT)' }
            ],
            defaultSubskill: 'vat-t2'
        }),
    },
    grade12_accounting_vat_t2_marking: {
        render: (ctx) => h(Grade12AccountingRoute, {
            workspaceMode: 'grade12_accounting_vat_t2_marking',
            ctx,
            subskills: [
                { key: 'vat-t2', title: 'Value Added Tax (VAT)' }
            ],
            defaultSubskill: 'vat-t2'
        }),
    },

    // Fallback/Legacy
    grade12_accounting_scaffold: {
        render: (ctx) => h(Grade12AccountingRoute, { workspaceMode: 'grade12_accounting_scaffold', ctx }),
    },
    grade12_accounting_practice: {
        render: (ctx) => h(Grade12AccountingRoute, { workspaceMode: 'grade12_accounting_practice', ctx }),
    },
};
