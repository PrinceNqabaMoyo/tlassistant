import React, { useEffect, useState } from 'react';
import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../shared/EvaluatedWorkspaceModeShell';
import { UserFriendlyError } from '../../ui/UserFriendlyError';
const h = React.createElement;
import Grade10AccountingIndigenousScaffold from '../grade10/accounting/indigenous-bookkeeping/Grade10AccountingIndigenousScaffold';
import Grade10AccountingIndigenousPractice from '../grade10/accounting/indigenous-bookkeeping/Grade10AccountingIndigenousPractice';
import Grade10AccountingEthicsScaffold from '../grade10/accounting/ethics/Grade10AccountingEthicsScaffold';
import Grade10AccountingEthicsPractice from '../grade10/accounting/ethics/Grade10AccountingEthicsPractice';
import Grade10AccountingGAAPScaffold from '../grade10/accounting/gaap/Grade10AccountingGAAPScaffold';
import Grade10AccountingGAAPPractice from '../grade10/accounting/gaap/Grade10AccountingGAAPPractice';
import Grade10AccountingInternalControlScaffold from '../grade10/accounting/internal-control/Grade10AccountingInternalControlScaffold';
import Grade10AccountingInternalControlPractice from '../grade10/accounting/internal-control/Grade10AccountingInternalControlPractice';
import Grade10AccountingSoleTraderScaffold from '../grade10/accounting/sole-trader/Grade10AccountingSoleTraderScaffold';
import Grade10AccountingSoleTraderPractice from '../grade10/accounting/sole-trader/Grade10AccountingSoleTraderPractice';
import Grade10AccountingSalariesWagesScaffold from '../grade10/accounting/salaries-wages/Grade10AccountingSalariesWagesScaffold';
import Grade10AccountingSalariesWagesPractice from '../grade10/accounting/salaries-wages/Grade10AccountingSalariesWagesPractice';
import Grade10AccountingFinalAccountsScaffold from '../grade10/accounting/final-accounts/Grade10AccountingFinalAccountsScaffold';
import Grade10AccountingFinalAccountsPractice from '../grade10/accounting/final-accounts/Grade10AccountingFinalAccountsPractice';
import Grade10AccountingVATScaffold from '../grade10/accounting/vat/Grade10AccountingVATScaffold';
import Grade10AccountingVATPractice from '../grade10/accounting/vat/Grade10AccountingVATPractice';
import { useGrade10IndigenousBookkeepingController, Grade10IndigenousBookkeepingVisualAids } from '../grade10/accounting/indigenous-bookkeeping';
import { useGrade10EthicsController, Grade10EthicsVisualAids } from '../grade10/accounting/ethics';
import { useGrade10AccountingGAAPController, Grade10AccountingGAAPVisualAids } from '../grade10/accounting/gaap';
import { useGrade10InternalControlController, Grade10InternalControlVisualAids } from '../grade10/accounting/internal-control';
import { useGrade10SoleTraderController, Grade10SoleTraderVisualAids } from '../grade10/accounting/sole-trader';
import { useGrade10SalariesWagesController, Grade10SalariesWagesVisualAids } from '../grade10/accounting/salaries-wages';
import { useGrade10FinalAccountsController, Grade10FinalAccountsVisualAids } from '../grade10/accounting/final-accounts';
import { useGrade10VATController, Grade10VATVisualAids } from '../grade10/accounting/vat';

const Grade10AccountingGAAPRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10AccountingGAAPController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10AcctGAAPVisualAids = () => h(Grade10AccountingGAAPVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const commonShellProps = {
        availableModes: [workspaceMode.split('_').pop()],
        subskills: controller.scaffoldSteps,
        difficulty: workspaceMode.endsWith('_scaffold') ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: workspaceMode.endsWith('_scaffold') ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'gaap') : 'mixed',
        setSubskill: (nextKey) => {
            if (workspaceMode.endsWith('_scaffold')) {
                const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
            }
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (workspaceMode.endsWith('_scaffold')) {
                controller.fetchScaffoldQuestion({
                    subskill: config.subskill,
                    difficulty: config.difficulty,
                });
            } else {
                controller.fetchPractice({
                    difficulty: config.difficulty,
                });
            }
        },
    };

    // Hooks must be called unconditionally (Rules of Hooks)
    const [gaapIdx, setGaapIdx] = useState(0);
    const handleGaapNext = () => {
        const total = (controller.practiceQuestions || []).length;
        if (gaapIdx + 1 < total) setGaapIdx(gaapIdx + 1);
    };

    if (workspaceMode === 'grade10_accounting_gaap_scaffold' || workspaceMode === 'grade10_accounting_gaap_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({
                subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'intro',
                difficulty: controller.scaffoldDifficulty,
            }),
            renderVisualAids: renderGrade10AcctGAAPVisualAids,
            questionSlot: sq ? h('div', { className: 'space-y-1' }, h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, sq.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            question: sq,
            userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingGAAPScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'),
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10AcctGAAPVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctGAAPVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctGAAPScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10AcctGAAPScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctGAAPScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10AcctGAAPScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctGAAPScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctGAAPScaffoldLoading: controller.scaffoldLoading,
            g10AcctGAAPScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctGAAPScaffoldQuestion: controller.scaffoldQuestion,
            g10AcctGAAPScaffoldAnswer: controller.scaffoldAnswer,
            setG10AcctGAAPScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctGAAPScaffoldFeedback: controller.scaffoldFeedback,
            setG10AcctGAAPScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctGAAPScaffoldShowHint: controller.scaffoldShowHint,
            setG10AcctGAAPScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctGAAPVisualAids,
            hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_gaap_practice') {
        const pqs = controller.practiceQuestions || [];
        const curQ = pqs[gaapIdx];

        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: handleGaapNext,
            renderVisualAids: renderGrade10AcctGAAPVisualAids,
            questionSlot: curQ ? h('div', { className: 'space-y-1' }, h('div', { className: 'text-sm text-slate-500' }, `Question ${gaapIdx + 1} of ${pqs.length}`), h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, curQ.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            ...commonShellProps,
        }, h(Grade10AccountingGAAPPractice, {
            onBack: ctx.onBack,
            g10AcctGAAPVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctGAAPVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctGAAPPracticeDifficulty: controller.practiceDifficulty,
            setG10AcctGAAPPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctGAAPPractice: controller.fetchPractice,
            g10AcctGAAPPracticeLoading: controller.practiceLoading,
            g10AcctGAAPPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctGAAPPracticeQuestions: controller.practiceQuestions,
            g10AcctGAAPPracticeAnswers: controller.practiceAnswers,
            setG10AcctGAAPPracticeAnswers: controller.setPracticeAnswers,
            g10AcctGAAPPracticeFeedback: controller.practiceFeedback,
            setG10AcctGAAPPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctGAAPVisualAids,
            currentIndex: gaapIdx,
            hideConfig: true,
        }));
    }

    return null;
};

const Grade10AccountingEthicsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10EthicsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10AcctEthicsVisualAids = () => h(Grade10EthicsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const commonShellProps = {
        availableModes: [workspaceMode.split('_').pop()],
        subskills: controller.scaffoldSteps,
        difficulty: workspaceMode.endsWith('_scaffold') ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: workspaceMode.endsWith('_scaffold') ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'ethics') : 'mixed',
        setSubskill: (nextKey) => {
            if (workspaceMode.endsWith('_scaffold')) {
                const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
            }
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (workspaceMode.endsWith('_scaffold')) {
                controller.fetchScaffoldQuestion({
                    subskill: config.subskill,
                    difficulty: config.difficulty,
                });
            } else {
                controller.fetchPractice({
                    difficulty: config.difficulty,
                });
            }
        },
    };

    // Hooks must be called unconditionally (Rules of Hooks)
    const [ethicsIdx, setEthicsIdx] = useState(0);
    const handleEthicsNext = () => {
        const total = (controller.practiceQuestions || []).length;
        if (ethicsIdx + 1 < total) setEthicsIdx(ethicsIdx + 1);
    };

    if (workspaceMode === 'grade10_accounting_ethics_scaffold' || workspaceMode === 'grade10_accounting_ethics_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({
                subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'code_of_ethics',
                difficulty: controller.scaffoldDifficulty,
            }),
            renderVisualAids: renderGrade10AcctEthicsVisualAids,
            questionSlot: sq ? h('div', { className: 'space-y-1' }, h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, sq.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            question: sq,
            userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingEthicsScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'),
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10AcctEthicsVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctEthicsVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctEthicsScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10AcctEthicsScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctEthicsScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10AcctEthicsScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctEthicsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctEthicsScaffoldLoading: controller.scaffoldLoading,
            g10AcctEthicsScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctEthicsScaffoldQuestion: controller.scaffoldQuestion,
            g10AcctEthicsScaffoldAnswer: controller.scaffoldAnswer,
            setG10AcctEthicsScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctEthicsScaffoldFeedback: controller.scaffoldFeedback,
            setG10AcctEthicsScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctEthicsScaffoldShowHint: controller.scaffoldShowHint,
            setG10AcctEthicsScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctEthicsVisualAids,
            hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_ethics_practice') {
        const pqs = controller.practiceQuestions || [];
        const curQ = pqs[ethicsIdx];

        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: handleEthicsNext,
            renderVisualAids: renderGrade10AcctEthicsVisualAids,
            questionSlot: curQ ? h('div', { className: 'space-y-1' }, h('div', { className: 'text-sm text-slate-500' }, `Question ${ethicsIdx + 1} of ${pqs.length}`), h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, curQ.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            ...commonShellProps,
        }, h(Grade10AccountingEthicsPractice, {
            onBack: ctx.onBack,
            g10AcctEthicsVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctEthicsVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctEthicsPracticeDifficulty: controller.practiceDifficulty,
            setG10AcctEthicsPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctEthicsPractice: controller.fetchPractice,
            g10AcctEthicsPracticeLoading: controller.practiceLoading,
            g10AcctEthicsPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctEthicsPracticeQuestions: controller.practiceQuestions,
            g10AcctEthicsPracticeAnswers: controller.practiceAnswers,
            setG10AcctEthicsPracticeAnswers: controller.setPracticeAnswers,
            g10AcctEthicsPracticeFeedback: controller.practiceFeedback,
            setG10AcctEthicsPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctEthicsVisualAids,
            currentIndex: ethicsIdx,
            hideConfig: true,
        }));
    }

    return null;
};

const Grade10AccountingIndigenousRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10IndigenousBookkeepingController({ workspaceMode, buildApiUrl: ctx.buildApiUrl, currentUser: ctx.currentUser });

    const renderGrade10AcctIndVisualAids = () => h(Grade10IndigenousBookkeepingVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const isScaffoldLikeMode = workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking');

    const commonShellProps = {
        availableModes: [workspaceMode.split('_').pop()],
        subskills: isScaffoldLikeMode ? controller.scaffoldSteps : controller.subskills,
        difficulty: isScaffoldLikeMode ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: isScaffoldLikeMode ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: isScaffoldLikeMode ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'informal_vs_formal') : (controller.practiceSubskill || 'mixed'),
        setSubskill: (nextKey) => {
            if (isScaffoldLikeMode) {
                const idx = controller.scaffoldSteps.findIndex((s) => String(s?.key) === String(nextKey));
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
                return;
            }
            controller.setPracticeSubskill(nextKey || 'mixed');
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({
                    subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'informal_vs_formal',
                    difficulty: config.difficulty,
                });
            } else {
                controller.fetchPractice({
                    subskill: config.subskill,
                    difficulty: config.difficulty,
                });
            }
        },
    };

    if (workspaceMode === 'grade10_accounting_indigenous_scaffold' || workspaceMode === 'grade10_accounting_indigenous_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({
                subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'informal_vs_formal',
                difficulty: controller.scaffoldDifficulty,
            }),
            renderVisualAids: renderGrade10AcctIndVisualAids,
            questionSlot: sq ? h('div', { className: 'space-y-1' }, h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, sq.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            question: sq,
            userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingIndigenousScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'),
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10AcctIndVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctIndVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctIndScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10AcctIndScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctIndScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10AcctIndScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctIndScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctIndScaffoldLoading: controller.scaffoldLoading,
            g10AcctIndScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctIndScaffoldQuestion: controller.scaffoldQuestion,
            g10AcctIndScaffoldAnswer: controller.scaffoldAnswer,
            setG10AcctIndScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctIndScaffoldFeedback: controller.scaffoldFeedback,
            setG10AcctIndScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctIndScaffoldShowHint: controller.scaffoldShowHint,
            setG10AcctIndScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctIndVisualAids,
            hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_indigenous_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            renderVisualAids: renderGrade10AcctIndVisualAids,
            questionSlot: null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            ...commonShellProps,
        }, h(Grade10AccountingIndigenousPractice, {
            onBack: ctx.onBack,
            g10AcctIndVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctIndVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctIndPracticeDifficulty: controller.practiceDifficulty,
            setG10AcctIndPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctIndPractice: controller.fetchPractice,
            g10AcctIndPracticeLoading: controller.practiceLoading,
            g10AcctIndPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctIndPracticeQuestions: controller.practiceQuestions,
            g10AcctIndPracticeAnswers: controller.practiceAnswers,
            setG10AcctIndPracticeAnswers: controller.setPracticeAnswers,
            g10AcctIndPracticeFeedback: controller.practiceFeedback,
            setG10AcctIndPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctIndVisualAids,
            hideConfig: true,
        }));
    }

    return null;
};

const Grade10AccountingInternalControlRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10InternalControlController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10AcctICVisualAids = () => h(Grade10InternalControlVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const commonShellProps = {
        availableModes: ['scaffold', 'practice', 'marking'],
        subskills: controller.scaffoldSteps,
        difficulty: workspaceMode.endsWith('_scaffold') ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: workspaceMode.endsWith('_scaffold') ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'definition') : 'mixed',
        setSubskill: (nextKey) => {
            if (workspaceMode.endsWith('_scaffold')) {
                const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
            }
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (workspaceMode.endsWith('_scaffold')) {
                controller.fetchScaffoldQuestion({
                    subskill: config.subskill,
                    difficulty: config.difficulty,
                });
            } else {
                controller.fetchPractice({
                    difficulty: config.difficulty,
                });
            }
        },
    };

    // Hooks must be called unconditionally (Rules of Hooks)
    const [icIdx, setIcIdx] = useState(0);
    const handleICNext = () => {
        const total = (controller.practiceQuestions || []).length;
        if (icIdx + 1 < total) setIcIdx(icIdx + 1);
    };

    if (workspaceMode === 'grade10_accounting_internal_control_scaffold' || workspaceMode === 'grade10_accounting_internal_control_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({
                subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'definition',
                difficulty: controller.scaffoldDifficulty,
            }),
            renderVisualAids: renderGrade10AcctICVisualAids,
            questionSlot: sq ? h('div', { className: 'space-y-1' }, h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, sq.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            question: sq,
            userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingInternalControlScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'),
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10AcctICVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctICVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctICScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10AcctICScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctICScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10AcctICScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctICScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctICScaffoldLoading: controller.scaffoldLoading,
            g10AcctICScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctICScaffoldQuestion: controller.scaffoldQuestion,
            g10AcctICScaffoldAnswer: controller.scaffoldAnswer,
            setG10AcctICScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctICScaffoldFeedback: controller.scaffoldFeedback,
            setG10AcctICScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctICScaffoldShowHint: controller.scaffoldShowHint,
            setG10AcctICScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctICVisualAids,
            hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_internal_control_practice') {
        const pqs = controller.practiceQuestions || [];
        const curQ = pqs[icIdx];

        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: handleICNext,
            renderVisualAids: renderGrade10AcctICVisualAids,
            questionSlot: curQ ? h('div', { className: 'space-y-1' }, h('div', { className: 'text-sm text-slate-500' }, `Question ${icIdx + 1} of ${pqs.length}`), h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, curQ.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            ...commonShellProps,
        }, h(Grade10AccountingInternalControlPractice, {
            onBack: ctx.onBack,
            g10AcctICVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctICVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctICPracticeDifficulty: controller.practiceDifficulty,
            setG10AcctICPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctICPractice: controller.fetchPractice,
            g10AcctICPracticeLoading: controller.practiceLoading,
            g10AcctICPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctICPracticeQuestions: controller.practiceQuestions,
            g10AcctICPracticeAnswers: controller.practiceAnswers,
            setG10AcctICPracticeAnswers: controller.setPracticeAnswers,
            g10AcctICPracticeFeedback: controller.practiceFeedback,
            setG10AcctICPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctICVisualAids,
            currentIndex: icIdx,
            hideConfig: true,
        }));
    }

    return null;
};

const Grade10AccountingSoleTraderRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10SoleTraderController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const isSuperAdmin = !!ctx.currentUser?.isSuperAdmin;

    const renderGrade10AcctSoleTraderVisualAids = () => h(Grade10SoleTraderVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
        currentSubskill: workspaceMode === 'grade10_accounting_sole_trader_practice'
            ? controller.practiceSubskill
            : controller.scaffoldSubskill,
    });

    const renderReadOnlyPromptTable = (journal, key, fallbackHeading = '') => {
        if (!journal) return null;
        const headers = Array.isArray(journal?.headers) ? journal.headers : [];
        const rows = Array.isArray(journal?.rows) ? journal.rows : [];
        const headerRows = Array.isArray(journal?.header_rows) ? journal.header_rows.filter((row) => Array.isArray(row) && row.length > 0) : [];
        const tableHeading = String(journal?.heading || fallbackHeading || '').trim();
        return h('div', { key, className: 'space-y-2' }, [
            tableHeading
                ? h('div', { key: `${key}-heading`, className: 'text-sm font-semibold text-slate-700' }, tableHeading)
                : null,
            h('div', { key: `${key}-wrap`, className: 'overflow-x-auto', style: { WebkitOverflowScrolling: 'touch' } },
                h('table', {
                    style: {
                        width: '100%',
                        minWidth: `${Math.max(headers.length * 112, 720)}px`,
                        borderCollapse: 'collapse',
                        tableLayout: 'fixed',
                    },
                }, [
                    h('thead', { key: 'thead' },
                        headerRows.length > 0
                            ? headerRows.map((row, rowIndex) => h('tr', { key: `hr-${rowIndex}` },
                                row.map((cell, cellIndex) => h('th', {
                                    key: `hh-${rowIndex}-${cellIndex}`,
                                    colSpan: Number.isFinite(Number(cell?.colSpan)) ? Number(cell.colSpan) : 1,
                                    rowSpan: Number.isFinite(Number(cell?.rowSpan)) ? Number(cell.rowSpan) : 1,
                                    style: {
                                        border: '1px solid #000',
                                        padding: '6px',
                                        background: '#e5e7eb',
                                        fontWeight: 600,
                                        textAlign: 'center',
                                        fontSize: '0.75rem',
                                        minWidth: '7rem',
                                        verticalAlign: 'middle',
                                    },
                                }, cell?.label || '')))
                            )
                            : h('tr', {}, headers.map((header, headerIndex) => h('th', {
                                key: `h-${headerIndex}`,
                                style: {
                                    border: '1px solid #000',
                                    padding: '6px',
                                    background: '#e5e7eb',
                                    fontWeight: 600,
                                    textAlign: 'center',
                                    fontSize: '0.75rem',
                                    minWidth: '7rem',
                                    verticalAlign: 'middle',
                                },
                            }, header)))
                    ),
                    h('tbody', { key: 'tbody' }, rows.map((row, rowIndex) => h('tr', { key: `r-${rowIndex}` },
                        (Array.isArray(row) ? row : []).map((cell, cellIndex) => h('td', {
                            key: `c-${rowIndex}-${cellIndex}`,
                            style: {
                                border: '1px solid #000',
                                padding: '6px',
                                verticalAlign: 'top',
                                minWidth: '7rem',
                                whiteSpace: 'pre-wrap',
                                overflowWrap: 'anywhere',
                                wordBreak: 'break-word',
                                textAlign: cellIndex === 4 || cellIndex === 9 ? 'right' : 'left',
                                fontFamily: cellIndex === 4 || cellIndex === 9 ? 'ui-monospace, monospace' : 'inherit',
                            },
                        }, cell?.value || ''))
                    )))
                ])
            )
        ].filter(Boolean));
    };

    const splitPromptSections = (promptText) => {
        const lines = String(promptText || '').split('\n');
        const infoIndex = lines.findIndex((line) => String(line || '').trim().toLowerCase() === 'information:');
        const additionalIndex = lines.findIndex((line) => String(line || '').trim().toLowerCase() === 'additional information:');
        const requiredIndex = lines.findIndex((line) => String(line || '').trim().toLowerCase() === 'required:');
        if (infoIndex < 0) {
            return {
                introText: String(promptText || '').trim(),
                additionalText: '',
                requiredText: '',
            };
        }
        const introText = lines.slice(0, infoIndex).join('\n').trim();
        const additionalStart = additionalIndex >= 0 ? additionalIndex + 1 : -1;
        const additionalEnd = requiredIndex >= 0 ? requiredIndex : lines.length;
        const additionalText = additionalStart >= 0 ? lines.slice(additionalStart, additionalEnd).join('\n').trim() : '';
        const requiredText = requiredIndex >= 0 ? lines.slice(requiredIndex + 1).join('\n').trim() : '';
        return { introText, additionalText, requiredText };
    };

    const renderSoleTraderQuestionSlot = (currentQuestion) => {
        if (!currentQuestion) return null;
        const promptText = String(currentQuestion?.prompt || '').trim();
        const promptJournals = Array.isArray(currentQuestion?.prompt_journals)
            ? currentQuestion.prompt_journals
            : (currentQuestion?.prompt_journal ? [currentQuestion.prompt_journal] : []);
        const referenceJournal = currentQuestion?.reference_journal;
        const headers = Array.isArray(referenceJournal?.headers) ? referenceJournal.headers : [];
        const rows = Array.isArray(referenceJournal?.rows) ? referenceJournal.rows : [];
        const { introText, additionalText, requiredText } = promptJournals.length > 0 ? splitPromptSections(promptText) : { introText: promptText, additionalText: '', requiredText: '' };
        return h('div', { className: 'space-y-4' }, [
            introText
                ? h('div', {
                    key: 'prompt',
                    className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed whitespace-pre-wrap',
                }, introText)
                : null,
            ...promptJournals.map((journal, promptIndex) => renderReadOnlyPromptTable(journal, `prompt-journal-${promptIndex}`)),
            additionalText
                ? h('div', { key: 'additional-info', className: 'space-y-1' }, [
                    h('div', { key: 'additional-label', className: 'text-sm font-semibold text-slate-700' }, 'Additional information:'),
                    h('div', { key: 'additional-text', className: 'text-sm text-slate-700 whitespace-pre-wrap' }, additionalText),
                ])
                : null,
            requiredText
                ? h('div', { key: 'required', className: 'space-y-1' }, [
                    h('div', { key: 'required-label', className: 'text-sm font-semibold text-slate-700' }, 'Required:'),
                    h('div', { key: 'required-text', className: 'text-sm text-slate-800 whitespace-pre-wrap' }, requiredText),
                ])
                : null,
            referenceJournal
                ? h('div', { key: 'reference', className: 'space-y-2' }, [
                    h('div', { key: 'reference-heading', className: 'text-sm font-semibold text-slate-700' }, referenceJournal?.heading || 'Reference Trial Balance'),
                    h('div', { key: 'reference-wrap', className: 'overflow-x-auto', style: { WebkitOverflowScrolling: 'touch' } },
                        h('table', {
                            style: {
                                width: '100%',
                                minWidth: `${Math.max(headers.length * 112, 720)}px`,
                                borderCollapse: 'collapse',
                                tableLayout: 'fixed',
                            },
                        }, [
                            h('thead', { key: 'thead' },
                                h('tr', {}, headers.map((header, headerIndex) => h('th', {
                                    key: `h-${headerIndex}`,
                                    style: {
                                        border: '1px solid #000',
                                        padding: '6px',
                                        background: '#e5e7eb',
                                        fontWeight: 600,
                                        textAlign: 'center',
                                        fontSize: '0.75rem',
                                        minWidth: '7rem',
                                        verticalAlign: 'middle',
                                    },
                                }, header)))
                            ),
                            h('tbody', { key: 'tbody' }, rows.map((row, rowIndex) => h('tr', { key: `r-${rowIndex}` },
                                (Array.isArray(row) ? row : []).map((cell, cellIndex) => h('td', {
                                    key: `c-${rowIndex}-${cellIndex}`,
                                    style: {
                                        border: '1px solid #000',
                                        padding: '6px',
                                        verticalAlign: 'top',
                                        minWidth: '7rem',
                                        whiteSpace: 'pre-wrap',
                                        overflowWrap: 'anywhere',
                                        wordBreak: 'break-word',
                                        textAlign: cellIndex >= 2 ? 'right' : 'left',
                                        fontFamily: cellIndex >= 2 ? 'ui-monospace, monospace' : 'inherit',
                                    },
                                }, cell?.value || '')))
                            ))
                        ])
                    )
                ])
                : null,
        ].filter(Boolean));
    };

    const orderedSubskills = Array.isArray(controller.subskills)
        ? [
            ...controller.subskills.filter((subskill) => subskill.key !== 'mixed'),
            ...controller.subskills.filter((subskill) => subskill.key === 'mixed'),
        ]
        : [];

    const commonShellProps = {
        availableModes: isSuperAdmin ? ['scaffold', 'practice', 'marking'] : ['scaffold', 'practice'],
        subskills: orderedSubskills,
        difficulty: workspaceMode.endsWith('_scaffold') ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: workspaceMode.endsWith('_scaffold') ? controller.scaffoldSubskill : controller.practiceSubskill,
        setSubskill: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldSubskill : controller.setPracticeSubskill,
        showDifficultyControl: isSuperAdmin,
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (workspaceMode.endsWith('_scaffold')) {
                controller.fetchScaffoldQuestion({
                    difficulty: config.difficulty,
                    subskill: config.subskill,
                    seed: controller.scaffoldSeed
                });
            } else {
                controller.fetchPractice({
                    difficulty: config.difficulty,
                    subskill: config.subskill,
                    seed: controller.practiceSeed
                });
            }
        }
    };

    if (workspaceMode === 'grade10_accounting_sole_trader_scaffold' || workspaceMode === 'grade10_accounting_sole_trader_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({
                subskill: controller.scaffoldSubskill,
                difficulty: controller.scaffoldDifficulty,
                seed: Date.now()
            }),
            renderVisualAids: renderGrade10AcctSoleTraderVisualAids,
            questionSlot: renderSoleTraderQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            question: sq,
            userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingSoleTraderScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'),
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            subskills: controller.subskills,
            g10AcctSTVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctSTVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctSTScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10AcctSTScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctSTSubskill: controller.scaffoldSubskill,
            setG10AcctSTSubskill: controller.setScaffoldSubskill,
            g10AcctSTScaffoldSeed: controller.scaffoldSeed,
            setG10AcctSTScaffoldSeed: controller.setScaffoldSeed,
            g10AcctSTScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10AcctSTScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctSTScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctSTScaffoldLoading: controller.scaffoldLoading,
            g10AcctSTScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctSTScaffoldQuestion: controller.scaffoldQuestion,
            g10AcctSTScaffoldAnswer: controller.scaffoldAnswer,
            setG10AcctSTScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctSTScaffoldFeedback: controller.scaffoldFeedback,
            setG10AcctSTScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctSTScaffoldShowHint: controller.scaffoldShowHint,
            setG10AcctSTScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctSTVisualAids: renderGrade10AcctSoleTraderVisualAids,
            hideConfig: true,
            isSuperAdmin,
        }));
    }

    if (workspaceMode === 'grade10_accounting_sole_trader_practice') {
        const pqs = controller.practiceQuestions || [];

        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            renderVisualAids: renderGrade10AcctSoleTraderVisualAids,
            questionSlot: pqs.length > 0 ? h('div', { className: 'space-y-1' }, h('div', { className: 'text-sm text-slate-500' }, `Practice set ready: ${pqs.length} questions`), h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed whitespace-pre-wrap' }, 'Answer the full set, then check everything at the end.')) : null,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            ...commonShellProps,
        }, h(Grade10AccountingSoleTraderPractice, {
            onBack: ctx.onBack,
            g10AcctSTVisualAidsOpen: controller.visualAidsOpen,
            setG10AcctSTVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctSTPracticeDifficulty: controller.practiceDifficulty,
            setG10AcctSTPracticeDifficulty: controller.setPracticeDifficulty,
            g10AcctSTPracticeSubskill: controller.practiceSubskill,
            setG10AcctSTPracticeSubskill: controller.setPracticeSubskill,
            g10AcctSTPracticeSeed: controller.practiceSeed,
            setG10AcctSTPracticeSeed: controller.setPracticeSeed,
            subskills: controller.subskills,
            fetchGrade10AcctSTPractice: controller.fetchPractice,
            g10AcctSTPracticeLoading: controller.practiceLoading,
            g10AcctSTPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctSTPracticeQuestions: controller.practiceQuestions,
            g10AcctSTPracticeAnswers: controller.practiceAnswers,
            setG10AcctSTPracticeAnswers: controller.setPracticeAnswers,
            g10AcctSTPracticeFeedback: controller.practiceFeedback,
            setG10AcctSTPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctSTVisualAids: renderGrade10AcctSoleTraderVisualAids,
            hideConfig: true,
            isSuperAdmin,
        }));
    }

    return null;
};

const Grade10AccountingSalariesWagesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10SalariesWagesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderVisualAids = () => h(Grade10SalariesWagesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const renderReadOnlyPromptTable = (journal, key, fallbackHeading = '') => {
        if (!journal) return null;
        const headers = Array.isArray(journal?.headers) ? journal.headers : [];
        const rows = Array.isArray(journal?.rows) ? journal.rows : [];
        const headerRows = Array.isArray(journal?.header_rows) ? journal.header_rows.filter((row) => Array.isArray(row) && row.length > 0) : [];
        const tableHeading = String(journal?.heading || fallbackHeading || '').trim();
        return h('div', { key, className: 'space-y-2' }, [
            tableHeading
                ? h('div', { key: `${key}-heading`, className: 'text-sm font-semibold text-slate-700' }, tableHeading)
                : null,
            h('div', { key: `${key}-wrap`, className: 'overflow-x-auto', style: { WebkitOverflowScrolling: 'touch' } },
                h('table', {
                    style: {
                        width: '100%',
                        minWidth: `${Math.max(headers.length * 112, 720)}px`,
                        borderCollapse: 'collapse',
                        tableLayout: 'fixed',
                    },
                }, [
                    h('thead', { key: 'thead' },
                        headerRows.length > 0
                            ? headerRows.map((row, rowIndex) => h('tr', { key: `hr-${rowIndex}` },
                                row.map((cell, cellIndex) => h('th', {
                                    key: `hh-${rowIndex}-${cellIndex}`,
                                    colSpan: Number.isFinite(Number(cell?.colSpan)) ? Number(cell.colSpan) : 1,
                                    rowSpan: Number.isFinite(Number(cell?.rowSpan)) ? Number(cell.rowSpan) : 1,
                                    style: {
                                        border: '1px solid #000',
                                        padding: '6px',
                                        background: '#e5e7eb',
                                        fontWeight: 600,
                                        textAlign: 'center',
                                        fontSize: '0.75rem',
                                        minWidth: '7rem',
                                        verticalAlign: 'middle',
                                    },
                                }, cell?.label || '')))
                            )
                            : h('tr', {}, headers.map((header, headerIndex) => h('th', {
                                key: `h-${headerIndex}`,
                                style: {
                                    border: '1px solid #000',
                                    padding: '6px',
                                    background: '#e5e7eb',
                                    fontWeight: 600,
                                    textAlign: 'center',
                                    fontSize: '0.75rem',
                                    minWidth: '7rem',
                                    verticalAlign: 'middle',
                                },
                            }, header)))
                    ),
                    h('tbody', { key: 'tbody' }, rows.map((row, rowIndex) => h('tr', { key: `r-${rowIndex}` },
                        (Array.isArray(row) ? row : []).map((cell, cellIndex) => h('td', {
                            key: `c-${rowIndex}-${cellIndex}`,
                            style: {
                                border: '1px solid #000',
                                padding: '6px',
                                verticalAlign: 'top',
                                minWidth: '7rem',
                                whiteSpace: 'pre-wrap',
                                overflowWrap: 'anywhere',
                                wordBreak: 'break-word',
                                textAlign: cellIndex >= Math.max(2, headers.length - 2) ? 'right' : 'left',
                                fontFamily: cellIndex >= Math.max(2, headers.length - 2) ? 'ui-monospace, monospace' : 'inherit',
                            },
                        }, cell?.value || ''))
                    )))
                ])
            )
        ].filter(Boolean));
    };

    const renderSWQuestionSlot = (currentQuestion, prefixText = '') => {
        if (!currentQuestion) return null;
        const promptText = String(currentQuestion?.prompt || '').trim();
        const promptJournals = Array.isArray(currentQuestion?.prompt_journals)
            ? currentQuestion.prompt_journals
            : (currentQuestion?.prompt_journal ? [currentQuestion.prompt_journal] : []);
        return h('div', { className: 'space-y-3' }, [
            prefixText
                ? h('div', { key: 'prefix', className: 'text-sm text-slate-500' }, prefixText)
                : null,
            promptText
                ? h('h2', { key: 'prompt', className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed whitespace-pre-wrap' }, promptText)
                : null,
            ...promptJournals.map((journal, promptIndex) => renderReadOnlyPromptTable(journal, `swj-prompt-journal-${promptIndex}`)),
        ].filter(Boolean));
    };

    const commonShellProps = {
        availableModes: ['scaffold', 'practice', 'marking'],
        subskills: controller.scaffoldSteps,
        difficulty: workspaceMode.endsWith('_scaffold') ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: workspaceMode.endsWith('_scaffold') ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: workspaceMode.endsWith('_scaffold')
            ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'salary_scales')
            : (controller.practiceSubskill || 'salary_scales'),
        setSubskill: (nextKey) => {
            if (workspaceMode.endsWith('_scaffold')) {
                const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
            } else {
                controller.setPracticeSubskill(nextKey || 'salary_scales');
            }
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (workspaceMode.endsWith('_scaffold')) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'salary_scales', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ difficulty: config.difficulty, subskill: config.subskill });
            }
        },
    };

    if (workspaceMode === 'grade10_accounting_salaries_wages_scaffold' || workspaceMode === 'grade10_accounting_salaries_wages_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'salary_scales', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderSWQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingSalariesWagesScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'), onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            g10AcctSWVisualAidsOpen: controller.visualAidsOpen, setG10AcctSWVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctSWScaffoldDifficulty: controller.scaffoldDifficulty, setG10AcctSWScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctSWScaffoldStepIndex: controller.scaffoldStepIndex, setG10AcctSWScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctSWScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctSWScaffoldLoading: controller.scaffoldLoading, g10AcctSWScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctSWScaffoldQuestion: controller.scaffoldQuestion, g10AcctSWScaffoldAnswer: controller.scaffoldAnswer, setG10AcctSWScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctSWScaffoldFeedback: controller.scaffoldFeedback, setG10AcctSWScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctSWScaffoldShowHint: controller.scaffoldShowHint, setG10AcctSWScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctSWVisualAids: renderVisualAids, hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_salaries_wages_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10AccountingSalariesWagesPractice, {
            onBack: ctx.onBack, g10AcctSWVisualAidsOpen: controller.visualAidsOpen, setG10AcctSWVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctSWPracticeDifficulty: controller.practiceDifficulty, setG10AcctSWPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctSWPractice: controller.fetchPractice, g10AcctSWPracticeLoading: controller.practiceLoading, g10AcctSWPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctSWPracticeQuestions: controller.practiceQuestions, g10AcctSWPracticeAnswers: controller.practiceAnswers, setG10AcctSWPracticeAnswers: controller.setPracticeAnswers,
            g10AcctSWPracticeFeedback: controller.practiceFeedback, setG10AcctSWPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctSWVisualAids: renderVisualAids, hideConfig: true,
        }));
    }
    return null;
};

const Grade10AccountingFinalAccountsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10FinalAccountsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const isScaffoldLikeMode = workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking');

    const renderVisualAids = () => h(Grade10FinalAccountsVisualAids, {
        visualAidsTab: controller.visualAidsTab, setVisualAidsTab: controller.setVisualAidsTab, setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const renderReadOnlyPromptTable = (table, key, fallbackHeading = '') => {
        if (!table) return null;
        const headers = Array.isArray(table?.headers) ? table.headers : [];
        const rows = Array.isArray(table?.rows) ? table.rows : [];
        const headerRows = Array.isArray(table?.header_rows) ? table.header_rows.filter((row) => Array.isArray(row) && row.length > 0) : [];
        const tableHeading = String(table?.heading || fallbackHeading || '').trim();
        return h('div', { key, className: 'space-y-2' }, [
            tableHeading
                ? h('div', { key: `${key}-heading`, className: 'text-sm font-semibold text-slate-700' }, tableHeading)
                : null,
            h('div', { key: `${key}-wrap`, className: 'overflow-x-auto', style: { WebkitOverflowScrolling: 'touch' } },
                h('table', {
                    style: {
                        width: '100%',
                        minWidth: `${Math.max(headers.length * 112, 720)}px`,
                        borderCollapse: 'collapse',
                        tableLayout: 'fixed',
                    },
                }, [
                    h('thead', { key: 'thead' },
                        headerRows.length > 0
                            ? headerRows.map((row, rowIndex) => h('tr', { key: `hr-${rowIndex}` },
                                row.map((cell, cellIndex) => h('th', {
                                    key: `hh-${rowIndex}-${cellIndex}`,
                                    colSpan: Number.isFinite(Number(cell?.colSpan)) ? Number(cell.colSpan) : 1,
                                    rowSpan: Number.isFinite(Number(cell?.rowSpan)) ? Number(cell.rowSpan) : 1,
                                    style: {
                                        border: '1px solid #000',
                                        padding: '6px',
                                        background: '#e5e7eb',
                                        fontWeight: 600,
                                        textAlign: 'center',
                                        fontSize: '0.75rem',
                                        minWidth: '7rem',
                                        verticalAlign: 'middle',
                                    },
                                }, cell?.label || '')))
                            )
                            : h('tr', {}, headers.map((header, headerIndex) => h('th', {
                                key: `h-${headerIndex}`,
                                style: {
                                    border: '1px solid #000',
                                    padding: '6px',
                                    background: '#e5e7eb',
                                    fontWeight: 600,
                                    textAlign: 'center',
                                    fontSize: '0.75rem',
                                    minWidth: '7rem',
                                    verticalAlign: 'middle',
                                },
                            }, header)))
                    ),
                    h('tbody', { key: 'tbody' }, rows.map((row, rowIndex) => h('tr', { key: `r-${rowIndex}` },
                        (Array.isArray(row) ? row : []).map((cell, cellIndex) => {
                            const headerLabel = String(headers[cellIndex] || '').toLowerCase();
                            const isNumeric = /(amount|debit|credit|balance|profit|loss|capital|drawings|sales|stock|cost|income|expense)/.test(headerLabel);
                            return h('td', {
                                key: `c-${rowIndex}-${cellIndex}`,
                                style: {
                                    border: '1px solid #000',
                                    padding: '6px',
                                    verticalAlign: 'top',
                                    minWidth: '7rem',
                                    whiteSpace: 'pre-wrap',
                                    overflowWrap: 'anywhere',
                                    wordBreak: 'break-word',
                                    textAlign: isNumeric ? 'right' : 'center',
                                    fontFamily: isNumeric ? 'ui-monospace, monospace' : 'inherit',
                                    color: /(period|month)/.test(headerLabel) ? '#6b7280' : 'inherit',
                                },
                            }, cell?.value || '');
                        })
                    )))
                ])
            )
        ].filter(Boolean));
    };

    const renderFAQuestionSlot = (currentQuestion, prefixText = '') => {
        if (!currentQuestion) return null;
        const promptText = String(currentQuestion?.prompt || '').trim();
        const promptTables = Array.isArray(currentQuestion?.prompt_tables)
            ? currentQuestion.prompt_tables
            : (currentQuestion?.prompt_table ? [currentQuestion.prompt_table] : Array.isArray(currentQuestion?.prompt_journals)
                ? currentQuestion.prompt_journals
                : (currentQuestion?.prompt_journal ? [currentQuestion.prompt_journal] : []));
        return h('div', { className: 'space-y-3' }, [
            prefixText
                ? h('div', { key: 'prefix', className: 'text-sm text-slate-500' }, prefixText)
                : null,
            promptText
                ? h('h2', { key: 'prompt', className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed whitespace-pre-wrap' }, promptText)
                : null,
            ...promptTables.map((table, promptIndex) => renderReadOnlyPromptTable(table, `fa-prompt-table-${promptIndex}`)),
        ].filter(Boolean));
    };

    const commonShellProps = {
        availableModes: ['scaffold', 'practice', 'marking'],
        subskills: isScaffoldLikeMode ? controller.scaffoldSteps : controller.subskills,
        difficulty: isScaffoldLikeMode ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: isScaffoldLikeMode ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: isScaffoldLikeMode ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'closing_transfers') : (controller.practiceSubskill || 'closing_transfers'),
        setSubskill: (nextKey) => {
            if (isScaffoldLikeMode) {
                const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
                return;
            }
            controller.setPracticeSubskill(nextKey || 'closing_transfers');
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'closing_transfers', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ subskill: config.subskill, difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_accounting_final_accounts_scaffold' || workspaceMode === 'grade10_accounting_final_accounts_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'closing_transfers', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: renderFAQuestionSlot(sq),
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingFinalAccountsScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'), onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            g10AcctFAVisualAidsOpen: controller.visualAidsOpen, setG10AcctFAVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctFAScaffoldDifficulty: controller.scaffoldDifficulty, setG10AcctFAScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctFAScaffoldStepIndex: controller.scaffoldStepIndex, setG10AcctFAScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctFAScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctFAScaffoldLoading: controller.scaffoldLoading, g10AcctFAScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctFAScaffoldQuestion: controller.scaffoldQuestion, g10AcctFAScaffoldAnswer: controller.scaffoldAnswer, setG10AcctFAScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctFAScaffoldFeedback: controller.scaffoldFeedback, setG10AcctFAScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctFAScaffoldShowHint: controller.scaffoldShowHint, setG10AcctFAScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctFAVisualAids: renderVisualAids, hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_final_accounts_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10AccountingFinalAccountsPractice, {
            onBack: ctx.onBack, g10AcctFAVisualAidsOpen: controller.visualAidsOpen, setG10AcctFAVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctFAPracticeDifficulty: controller.practiceDifficulty, setG10AcctFAPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctFAPractice: controller.fetchPractice, g10AcctFAPracticeLoading: controller.practiceLoading, g10AcctFAPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctFAPracticeQuestions: controller.practiceQuestions, g10AcctFAPracticeAnswers: controller.practiceAnswers, setG10AcctFAPracticeAnswers: controller.setPracticeAnswers,
            g10AcctFAPracticeFeedback: controller.practiceFeedback, setG10AcctFAPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctFAVisualAids: renderVisualAids, hideConfig: true,
        }));
    }
    return null;
};

const Grade10AccountingVATRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10VATController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderVisualAids = () => h(Grade10VATVisualAids, {
        visualAidsTab: controller.visualAidsTab, setVisualAidsTab: controller.setVisualAidsTab, setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const isScaffoldLikeMode = workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking');

    const commonShellProps = {
        availableModes: ['scaffold', 'practice', 'marking'],
        subskills: isScaffoldLikeMode ? controller.scaffoldSteps : controller.subskills,
        difficulty: isScaffoldLikeMode ? controller.scaffoldDifficulty : controller.practiceDifficulty,
        setDifficulty: isScaffoldLikeMode ? controller.setScaffoldDifficulty : controller.setPracticeDifficulty,
        subskill: isScaffoldLikeMode ? (controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts') : (controller.practiceSubskill || 'mixed'),
        setSubskill: (nextKey) => {
            if (isScaffoldLikeMode) {
                const idx = controller.scaffoldSteps.findIndex(s => s.key === nextKey);
                if (idx >= 0) controller.setScaffoldStepIndex(idx);
                return;
            }
            controller.setPracticeSubskill(nextKey || 'mixed');
        },
        isSuperAdmin: !!ctx.currentUser?.isSuperAdmin,
        isGenerating: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldLoading : controller.practiceLoading,
        generationError: workspaceMode.endsWith('_scaffold') || workspaceMode.endsWith('_marking') ? controller.scaffoldError : controller.practiceError,
        onGenerate: (config) => {
            if (isScaffoldLikeMode) {
                controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: config.difficulty });
            } else {
                controller.fetchPractice({ subskill: config.subskill, difficulty: config.difficulty });
            }
        },
    };

    if (workspaceMode === 'grade10_accounting_vat_scaffold' || workspaceMode === 'grade10_accounting_vat_marking') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: sq ? h('div', { className: 'space-y-1' }, h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, sq.prompt || '')) : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: controller.scaffoldAnswer?.cells || {},
            ...commonShellProps,
        }, h(Grade10AccountingVATScaffold, {
            isMarkingEnv: workspaceMode.endsWith('_marking'), onBack: ctx.onBack, scaffoldSteps: controller.scaffoldSteps,
            g10AcctVATVisualAidsOpen: controller.visualAidsOpen, setG10AcctVATVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctVATScaffoldDifficulty: controller.scaffoldDifficulty, setG10AcctVATScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AcctVATScaffoldStepIndex: controller.scaffoldStepIndex, setG10AcctVATScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AcctVATScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AcctVATScaffoldLoading: controller.scaffoldLoading, g10AcctVATScaffoldError: controller.scaffoldError ? h(UserFriendlyError, { error: controller.scaffoldError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctVATScaffoldQuestion: controller.scaffoldQuestion, g10AcctVATScaffoldAnswer: controller.scaffoldAnswer, setG10AcctVATScaffoldAnswer: controller.setScaffoldAnswer,
            g10AcctVATScaffoldFeedback: controller.scaffoldFeedback, setG10AcctVATScaffoldFeedback: controller.setScaffoldFeedback,
            g10AcctVATScaffoldShowHint: controller.scaffoldShowHint, setG10AcctVATScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10AcctVATVisualAids: renderVisualAids, hideConfig: true,
        }));
    }

    if (workspaceMode === 'grade10_accounting_vat_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10AccountingVATPractice, {
            onBack: ctx.onBack, g10AcctVATVisualAidsOpen: controller.visualAidsOpen, setG10AcctVATVisualAidsOpen: controller.setVisualAidsOpen,
            g10AcctVATPracticeDifficulty: controller.practiceDifficulty, setG10AcctVATPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AcctVATPractice: controller.fetchPractice, g10AcctVATPracticeLoading: controller.practiceLoading, g10AcctVATPracticeError: controller.practiceError ? h(UserFriendlyError, { error: controller.practiceError, isSuperAdmin: !!ctx.currentUser?.isSuperAdmin }) : null,
            g10AcctVATPracticeQuestions: controller.practiceQuestions, g10AcctVATPracticeAnswers: controller.practiceAnswers, setG10AcctVATPracticeAnswers: controller.setPracticeAnswers,
            g10AcctVATPracticeFeedback: controller.practiceFeedback, setG10AcctVATPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10AcctVATVisualAids: renderVisualAids, hideConfig: true,
        }));
    }
    return null;
};


export const grade10AccountingRegistry = {
    grade10_accounting_indigenous_scaffold: {
        render: (ctx) => h(Grade10AccountingIndigenousRoute, { workspaceMode: 'grade10_accounting_indigenous_scaffold', ctx }),
    },
    grade10_accounting_indigenous_practice: {
        render: (ctx) => h(Grade10AccountingIndigenousRoute, { workspaceMode: 'grade10_accounting_indigenous_practice', ctx }),
    },
    grade10_accounting_ethics_scaffold: {
        render: (ctx) => h(Grade10AccountingEthicsRoute, { workspaceMode: 'grade10_accounting_ethics_scaffold', ctx }),
    },
    grade10_accounting_ethics_practice: {
        render: (ctx) => h(Grade10AccountingEthicsRoute, { workspaceMode: 'grade10_accounting_ethics_practice', ctx }),
    },
    grade10_accounting_gaap_scaffold: {
        render: (ctx) => h(Grade10AccountingGAAPRoute, { workspaceMode: 'grade10_accounting_gaap_scaffold', ctx }),
    },
    grade10_accounting_gaap_practice: {
        render: (ctx) => h(Grade10AccountingGAAPRoute, { workspaceMode: 'grade10_accounting_gaap_practice', ctx }),
    },
    grade10_accounting_internal_control_scaffold: {
        render: (ctx) => h(Grade10AccountingInternalControlRoute, { workspaceMode: 'grade10_accounting_internal_control_scaffold', ctx }),
    },
    grade10_accounting_internal_control_practice: {
        render: (ctx) => h(Grade10AccountingInternalControlRoute, { workspaceMode: 'grade10_accounting_internal_control_practice', ctx }),
    },
    grade10_accounting_sole_trader_scaffold: {
        render: (ctx) => h(Grade10AccountingSoleTraderRoute, { workspaceMode: 'grade10_accounting_sole_trader_scaffold', ctx }),
    },
    grade10_accounting_sole_trader_practice: {
        render: (ctx) => h(Grade10AccountingSoleTraderRoute, { workspaceMode: 'grade10_accounting_sole_trader_practice', ctx }),
    },
    grade10_accounting_salaries_wages_scaffold: {
        render: (ctx) => h(Grade10AccountingSalariesWagesRoute, { workspaceMode: 'grade10_accounting_salaries_wages_scaffold', ctx }),
    },
    grade10_accounting_salaries_wages_practice: {
        render: (ctx) => h(Grade10AccountingSalariesWagesRoute, { workspaceMode: 'grade10_accounting_salaries_wages_practice', ctx }),
    },
    grade10_accounting_salaries_wages_marking: {
        render: (ctx) => h(Grade10AccountingSalariesWagesRoute, { workspaceMode: 'grade10_accounting_salaries_wages_marking', ctx }),
    },
    grade10_accounting_final_accounts_scaffold: {
        render: (ctx) => h(Grade10AccountingFinalAccountsRoute, { workspaceMode: 'grade10_accounting_final_accounts_scaffold', ctx }),
    },
    grade10_accounting_final_accounts_practice: {
        render: (ctx) => h(Grade10AccountingFinalAccountsRoute, { workspaceMode: 'grade10_accounting_final_accounts_practice', ctx }),
    },
    grade10_accounting_final_accounts_marking: {
        render: (ctx) => h(Grade10AccountingFinalAccountsRoute, { workspaceMode: 'grade10_accounting_final_accounts_marking', ctx }),
    },
    grade10_accounting_vat_scaffold: {
        render: (ctx) => h(Grade10AccountingVATRoute, { workspaceMode: 'grade10_accounting_vat_scaffold', ctx }),
    },
    grade10_accounting_vat_practice: {
        render: (ctx) => h(Grade10AccountingVATRoute, { workspaceMode: 'grade10_accounting_vat_practice', ctx }),
    },
};
