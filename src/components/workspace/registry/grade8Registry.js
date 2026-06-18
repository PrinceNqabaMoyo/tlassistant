import React from 'react';
import Grade8WholeNumbersScaffold from '../grade8/mathematics/whole-numbers/Grade8WholeNumbersScaffold';
import Grade8WholeNumbersPractice from '../grade8/mathematics/whole-numbers/Grade8WholeNumbersPractice';
import Grade8IntegersScaffold from '../grade8/mathematics/integers/Grade8IntegersScaffold';
import Grade8IntegersPractice from '../grade8/mathematics/integers/Grade8IntegersPractice';
import Grade8ExponentsScaffold from '../grade8/mathematics/exponents/Grade8ExponentsScaffold';
import Grade8ExponentsPractice from '../grade8/mathematics/exponents/Grade8ExponentsPractice';
import Grade8FunctionsScaffold from '../grade8/mathematics/functions/Grade8FunctionsScaffold';
import Grade8FunctionsPractice from '../grade8/mathematics/functions/Grade8FunctionsPractice';
import Grade8AlgebraicExpressionsScaffold from '../grade8/mathematics/algebraic-expressions/Grade8AlgebraicExpressionsScaffold';
import Grade8AlgebraicExpressionsPractice from '../grade8/mathematics/algebraic-expressions/Grade8AlgebraicExpressionsPractice';
import Grade8AlgebraicEquationsScaffold from '../grade8/mathematics/algebraic-equations/Grade8AlgebraicEquationsScaffold';
import Grade8AlgebraicEquationsPractice from '../grade8/mathematics/algebraic-equations/Grade8AlgebraicEquationsPractice';
import Grade8PatternsScaffold from '../grade8/mathematics/patterns/Grade8PatternsScaffold';
import Grade8PatternsPractice from '../grade8/mathematics/patterns/Grade8PatternsPractice';

import { useGrade8WholeNumbersController, WholeNumbersVisualAids as Grade8WholeNumbersVisualAids } from '../grade8/mathematics/whole-numbers';
import { useGrade8IntegersController, IntegersVisualAids } from '../grade8/mathematics/integers';
import { useGrade8ExponentsController, ExponentsVisualAids as Grade8ExponentsVisualAids } from '../grade8/mathematics/exponents';
import { useGrade8PatternsController, PatternsVisualAids } from '../grade8/mathematics/patterns';
import { useGrade8FunctionsController, FunctionsVisualAids } from '../grade8/mathematics/functions';
import { useGrade8AlgebraicExpressionsController, AlgebraicExpressionsVisualAids } from '../grade8/mathematics/algebraic-expressions';
import { useGrade8AlgebraicEquationsController, AlgebraicEquationsVisualAids } from '../grade8/mathematics/algebraic-equations';

const h = React.createElement;

const Grade8WholeNumbersRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8WholeNumbersController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8WholeNumbersVisualAids = () => h(Grade8WholeNumbersVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade8_whole_scaffold') {
        return h(Grade8WholeNumbersScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8WholeVisualAidsOpen: controller.visualAidsOpen,
            setG8WholeVisualAidsOpen: controller.setVisualAidsOpen,
            g8WholeScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8WholeScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8WholeScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8WholeScaffoldStepIndex: controller.setScaffoldStepIndex,
            setG8WholeScaffoldFeedback: controller.setScaffoldFeedback,
            setG8WholeScaffoldShowHint: controller.setScaffoldShowHint,
            setG8WholeScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            setG8WholeScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            setG8WholeScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            fetchGrade8WholeNumbersScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8WholeScaffoldLoading: controller.scaffoldLoading,
            g8WholeScaffoldError: controller.scaffoldError,
            g8WholeScaffoldQuestion: controller.scaffoldQuestion,
            g8WholeScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            g8WholeScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            g8WholeScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            g8WholeScaffoldShowHint: controller.scaffoldShowHint,
            g8WholeScaffoldAnswer: controller.scaffoldAnswer,
            setG8WholeScaffoldAnswer: controller.setScaffoldAnswer,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            g8WholeScaffoldFeedback: controller.scaffoldFeedback,
            renderGrade8WholeNumbersVisualAids,
        });
    }

    if (workspaceMode === 'grade8_whole_practice') {
        return h(Grade8WholeNumbersPractice, {
            onBack: ctx.onBack,
            g8WholeVisualAidsOpen: controller.visualAidsOpen,
            setG8WholeVisualAidsOpen: controller.setVisualAidsOpen,
            g8WholePracticeDifficulty: controller.practiceDifficulty,
            setG8WholePracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8WholeNumbersPractice: controller.fetchPractice,
            g8WholePracticeLoading: controller.practiceLoading,
            g8WholePracticeError: controller.practiceError,
            g8WholePracticeQuestions: controller.practiceQuestions,
            g8WholePracticeAnswers: controller.practiceAnswers,
            setG8WholePracticeAnswers: controller.setPracticeAnswers,
            g8WholePracticeFeedback: controller.practiceFeedback,
            setG8WholePracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            renderGrade8WholeNumbersVisualAids,
        });
    }

    return null;
};

const Grade8ExponentsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8ExponentsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8ExponentsVisualAids = () => h(Grade8ExponentsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
        vizBase: controller.vizBase,
        setVizBase: controller.setVizBase,
        vizExponent: controller.vizExponent,
        setVizExponent: controller.setVizExponent,
        vizRoot: controller.vizRoot,
        setVizRoot: controller.setVizRoot,
        formatExponentCarets: ctx.formatExponentCarets,
    });

    if (workspaceMode === 'grade8_exponents_scaffold') {
        return h(Grade8ExponentsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8ExpVisualAidsOpen: controller.visualAidsOpen,
            setG8ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g8ExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8ExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8ExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8ExpScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade8ExponentsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8ExpScaffoldLoading: controller.scaffoldLoading,
            g8ExpScaffoldError: controller.scaffoldError,
            g8ExpScaffoldQuestion: controller.scaffoldQuestion,
            g8ExpScaffoldShowHint: controller.scaffoldShowHint,
            setG8ExpScaffoldShowHint: controller.setScaffoldShowHint,
            g8ExpScaffoldAnswer: controller.scaffoldAnswer,
            setG8ExpScaffoldAnswer: controller.setScaffoldAnswer,
            g8ExpScaffoldFeedback: controller.scaffoldFeedback,
            setG8ExpScaffoldFeedback: controller.setScaffoldFeedback,
            g8ExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG8ExpScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g8ExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG8ExpScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g8ExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG8ExpScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            formatExponentCarets: ctx.formatExponentCarets,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8ExponentsVisualAids,
        });
    }

    if (workspaceMode === 'grade8_exponents_practice') {
        return h(Grade8ExponentsPractice, {
            onBack: ctx.onBack,
            g8ExpVisualAidsOpen: controller.visualAidsOpen,
            setG8ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g8ExpPracticeDifficulty: controller.practiceDifficulty,
            setG8ExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8ExponentsPractice: controller.fetchPractice,
            g8ExpPracticeLoading: controller.practiceLoading,
            g8ExpPracticeError: controller.practiceError,
            g8ExpPracticeQuestions: controller.practiceQuestions,
            g8ExpPracticeAnswers: controller.practiceAnswers,
            setG8ExpPracticeAnswers: controller.setPracticeAnswers,
            g8ExpPracticeFeedback: controller.practiceFeedback,
            setG8ExpPracticeFeedback: controller.setPracticeFeedback,
            formatExponentCarets: ctx.formatExponentCarets,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8ExponentsVisualAids,
        });
    }

    return null;
};

const Grade8IntegersRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8IntegersController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8IntegersVisualAids = () => h(IntegersVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade8_integers_scaffold') {
        return h(Grade8IntegersScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8IntVisualAidsOpen: controller.visualAidsOpen,
            setG8IntVisualAidsOpen: controller.setVisualAidsOpen,
            g8IntScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8IntScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8IntScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8IntScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade8IntegersScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8IntScaffoldLoading: controller.scaffoldLoading,
            g8IntScaffoldError: controller.scaffoldError,
            g8IntScaffoldQuestion: controller.scaffoldQuestion,
            g8IntScaffoldShowHint: controller.scaffoldShowHint,
            setG8IntScaffoldShowHint: controller.setScaffoldShowHint,
            g8IntScaffoldAnswer: controller.scaffoldAnswer,
            setG8IntScaffoldAnswer: controller.setScaffoldAnswer,
            g8IntScaffoldFeedback: controller.scaffoldFeedback,
            setG8IntScaffoldFeedback: controller.setScaffoldFeedback,
            g8IntScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG8IntScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g8IntScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG8IntScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g8IntScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG8IntScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            renderGrade8IntegersVisualAids,
        });
    }

    if (workspaceMode === 'grade8_integers_practice') {
        return h(Grade8IntegersPractice, {
            onBack: ctx.onBack,
            g8IntVisualAidsOpen: controller.visualAidsOpen,
            setG8IntVisualAidsOpen: controller.setVisualAidsOpen,
            g8IntPracticeDifficulty: controller.practiceDifficulty,
            setG8IntPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8IntegersPractice: controller.fetchPractice,
            g8IntPracticeLoading: controller.practiceLoading,
            g8IntPracticeError: controller.practiceError,
            g8IntPracticeQuestions: controller.practiceQuestions,
            g8IntPracticeAnswers: controller.practiceAnswers,
            setG8IntPracticeAnswers: controller.setPracticeAnswers,
            g8IntPracticeFeedback: controller.practiceFeedback,
            setG8IntPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            renderGrade8IntegersVisualAids,
        });
    }

    return null;
};

const Grade8PatternsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8PatternsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8PatternsVisualAids = () => h(PatternsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade8_patterns_scaffold') {
        return h(Grade8PatternsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8PatVisualAidsOpen: controller.visualAidsOpen,
            setG8PatVisualAidsOpen: controller.setVisualAidsOpen,
            g8PatScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8PatScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8PatScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8PatScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade8PatternsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8PatScaffoldLoading: controller.scaffoldLoading,
            g8PatScaffoldError: controller.scaffoldError,
            g8PatScaffoldQuestion: controller.scaffoldQuestion,
            g8PatScaffoldShowHint: controller.scaffoldShowHint,
            setG8PatScaffoldShowHint: controller.setScaffoldShowHint,
            g8PatScaffoldAnswer: controller.scaffoldAnswer,
            setG8PatScaffoldAnswer: controller.setScaffoldAnswer,
            g8PatScaffoldFeedback: controller.scaffoldFeedback,
            setG8PatScaffoldFeedback: controller.setScaffoldFeedback,
            g8PatScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG8PatScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g8PatScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG8PatScaffoldCheckpointAnswers: controller.setPracticeAnswers,
            g8PatScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG8PatScaffoldCheckpointFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8PatternsVisualAids,
        });
    }

    if (workspaceMode === 'grade8_patterns_practice') {
        return h(Grade8PatternsPractice, {
            onBack: ctx.onBack,
            g8PatVisualAidsOpen: controller.visualAidsOpen,
            setG8PatVisualAidsOpen: controller.setVisualAidsOpen,
            g8PatPracticeDifficulty: controller.practiceDifficulty,
            setG8PatPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8PatternsPractice: controller.fetchPractice,
            g8PatPracticeLoading: controller.practiceLoading,
            g8PatPracticeError: controller.practiceError,
            g8PatPracticeQuestions: controller.practiceQuestions,
            g8PatPracticeAnswers: controller.practiceAnswers,
            setG8PatPracticeAnswers: controller.setPracticeAnswers,
            g8PatPracticeFeedback: controller.practiceFeedback,
            setG8PatPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8PatternsVisualAids,
        });
    }

    return null;
};

const Grade8FunctionsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8FunctionsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8FunctionsVisualAids = () => h(FunctionsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade8_functions_1_scaffold') {
        return h(Grade8FunctionsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8FuncVisualAidsOpen: controller.visualAidsOpen,
            setG8FuncVisualAidsOpen: controller.setVisualAidsOpen,
            g8FuncScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8FuncScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8FuncScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8FuncScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade8FunctionsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8FuncScaffoldLoading: controller.scaffoldLoading,
            g8FuncScaffoldError: controller.scaffoldError,
            g8FuncScaffoldQuestion: controller.scaffoldQuestion,
            g8FuncScaffoldShowHint: controller.scaffoldShowHint,
            setG8FuncScaffoldShowHint: controller.setG8FuncScaffoldShowHint,
            g8FuncScaffoldAnswer: controller.scaffoldAnswer,
            setG8FuncScaffoldAnswer: controller.setScaffoldAnswer,
            g8FuncScaffoldFeedback: controller.scaffoldFeedback,
            setG8FuncScaffoldFeedback: controller.setScaffoldFeedback,
            g8FuncScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG8FuncScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g8FuncScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG8FuncScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g8FuncScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG8FuncScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8FunctionsVisualAids,
        });
    }

    if (workspaceMode === 'grade8_functions_1_practice') {
        return h(Grade8FunctionsPractice, {
            onBack: ctx.onBack,
            g8FuncVisualAidsOpen: controller.visualAidsOpen,
            setG8FuncVisualAidsOpen: controller.setVisualAidsOpen,
            g8FuncPracticeDifficulty: controller.practiceDifficulty,
            setG8FuncPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8FunctionsPractice: controller.fetchPractice,
            g8FuncPracticeLoading: controller.practiceLoading,
            g8FuncPracticeError: controller.practiceError,
            g8FuncPracticeQuestions: controller.practiceQuestions,
            g8FuncPracticeAnswers: controller.practiceAnswers,
            setG8FuncPracticeAnswers: controller.setPracticeAnswers,
            g8FuncPracticeFeedback: controller.practiceFeedback,
            setG8FuncPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8FunctionsVisualAids,
        });
    }

    return null;
};

const Grade8AlgebraicExpressionsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8AlgebraicExpressionsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8AlgExpVisualAids = () => h(AlgebraicExpressionsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade8_algebraic_expressions_1_scaffold') {
        return h(Grade8AlgebraicExpressionsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8AlgExpVisualAidsOpen: controller.visualAidsOpen,
            setG8AlgExpVisualAidsOpen: controller.setVisualAidsOpen,
            g8AlgExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8AlgExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8AlgExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8AlgExpScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade8AlgExpScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8AlgExpScaffoldLoading: controller.scaffoldLoading,
            g8AlgExpScaffoldError: controller.scaffoldError,
            g8AlgExpScaffoldQuestion: controller.scaffoldQuestion,
            g8AlgExpScaffoldShowHint: controller.scaffoldShowHint,
            setG8AlgExpScaffoldShowHint: controller.setG8AlgExpScaffoldShowHint,
            g8AlgExpScaffoldAnswer: controller.scaffoldAnswer,
            setG8AlgExpScaffoldAnswer: controller.setScaffoldAnswer,
            g8AlgExpScaffoldFeedback: controller.scaffoldFeedback,
            setG8AlgExpScaffoldFeedback: controller.setScaffoldFeedback,
            g8AlgExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG8AlgExpScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g8AlgExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG8AlgExpScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g8AlgExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG8AlgExpScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8AlgExpVisualAids,
        });
    }

    if (workspaceMode === 'grade8_algebraic_expressions_1_practice') {
        return h(Grade8AlgebraicExpressionsPractice, {
            onBack: ctx.onBack,
            g8AlgExpVisualAidsOpen: controller.visualAidsOpen,
            setG8AlgExpVisualAidsOpen: controller.setVisualAidsOpen,
            g8AlgExpPracticeDifficulty: controller.practiceDifficulty,
            setG8AlgExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8AlgExpPractice: controller.fetchPractice,
            g8AlgExpPracticeLoading: controller.practiceLoading,
            g8AlgExpPracticeError: controller.practiceError,
            g8AlgExpPracticeQuestions: controller.practiceQuestions,
            g8AlgExpPracticeAnswers: controller.practiceAnswers,
            setG8AlgExpPracticeAnswers: controller.setPracticeAnswers,
            g8AlgExpPracticeFeedback: controller.practiceFeedback,
            setG8AlgExpPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8AlgExpVisualAids,
        });
    }

    return null;
};

const Grade8AlgebraicEquationsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade8AlgebraicEquationsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade8AlgEqVisualAids = () => h(AlgebraicEquationsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade8_algebraic_equations_1_scaffold') {
        return h(Grade8AlgebraicEquationsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g8AlgEqVisualAidsOpen: controller.visualAidsOpen,
            setG8AlgEqVisualAidsOpen: controller.setVisualAidsOpen,
            g8AlgEqScaffoldDifficulty: controller.scaffoldDifficulty,
            setG8AlgEqScaffoldDifficulty: controller.setScaffoldDifficulty,
            g8AlgEqScaffoldStepIndex: controller.scaffoldStepIndex,
            setG8AlgEqScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade8AlgEqScaffoldQuestion: controller.fetchScaffoldQuestion,
            g8AlgEqScaffoldLoading: controller.scaffoldLoading,
            g8AlgEqScaffoldError: controller.scaffoldError,
            g8AlgEqScaffoldQuestion: controller.scaffoldQuestion,
            g8AlgEqScaffoldShowHint: controller.scaffoldShowHint,
            setG8AlgEqScaffoldShowHint: controller.setG8AlgEqScaffoldShowHint,
            g8AlgEqScaffoldAnswer: controller.scaffoldAnswer,
            setG8AlgEqScaffoldAnswer: controller.setScaffoldAnswer,
            g8AlgEqScaffoldFeedback: controller.scaffoldFeedback,
            setG8AlgEqScaffoldFeedback: controller.setScaffoldFeedback,
            g8AlgEqScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG8AlgEqScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g8AlgEqScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG8AlgEqScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g8AlgEqScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG8AlgEqScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8AlgEqVisualAids,
        });
    }

    if (workspaceMode === 'grade8_algebraic_equations_1_practice') {
        return h(Grade8AlgebraicEquationsPractice, {
            onBack: ctx.onBack,
            g8AlgEqVisualAidsOpen: controller.visualAidsOpen,
            setG8AlgEqVisualAidsOpen: controller.setVisualAidsOpen,
            g8AlgEqPracticeDifficulty: controller.practiceDifficulty,
            setG8AlgEqPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade8AlgEqPractice: controller.fetchPractice,
            g8AlgEqPracticeLoading: controller.practiceLoading,
            g8AlgEqPracticeError: controller.practiceError,
            g8AlgEqPracticeQuestions: controller.practiceQuestions,
            g8AlgEqPracticeAnswers: controller.practiceAnswers,
            setG8AlgEqPracticeAnswers: controller.setPracticeAnswers,
            g8AlgEqPracticeFeedback: controller.practiceFeedback,
            setG8AlgEqPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade8AlgEqVisualAids,
        });
    }

    return null;
};

export const grade8Registry = {
    grade8_whole_scaffold: {
        render: (ctx) => h(Grade8WholeNumbersRoute, { workspaceMode: 'grade8_whole_scaffold', ctx }),
    },
    grade8_whole_practice: {
        render: (ctx) => h(Grade8WholeNumbersRoute, { workspaceMode: 'grade8_whole_practice', ctx }),
    },
    grade8_integers_scaffold: {
        render: (ctx) => h(Grade8IntegersRoute, { workspaceMode: 'grade8_integers_scaffold', ctx }),
    },
    grade8_integers_practice: {
        render: (ctx) => h(Grade8IntegersRoute, { workspaceMode: 'grade8_integers_practice', ctx }),
    },
    grade8_exponents_scaffold: {
        render: (ctx) => h(Grade8ExponentsRoute, { workspaceMode: 'grade8_exponents_scaffold', ctx }),
    },
    grade8_exponents_practice: {
        render: (ctx) => h(Grade8ExponentsRoute, { workspaceMode: 'grade8_exponents_practice', ctx }),
    },
    grade8_algebraic_equations_1_scaffold: {
        render: (ctx) => h(Grade8AlgebraicEquationsRoute, { workspaceMode: 'grade8_algebraic_equations_1_scaffold', ctx }),
    },
    grade8_algebraic_equations_1_practice: {
        render: (ctx) => h(Grade8AlgebraicEquationsRoute, { workspaceMode: 'grade8_algebraic_equations_1_practice', ctx }),
    },
    grade8_algebraic_expressions_1_scaffold: {
        render: (ctx) => h(Grade8AlgebraicExpressionsRoute, { workspaceMode: 'grade8_algebraic_expressions_1_scaffold', ctx }),
    },
    grade8_algebraic_expressions_1_practice: {
        render: (ctx) => h(Grade8AlgebraicExpressionsRoute, { workspaceMode: 'grade8_algebraic_expressions_1_practice', ctx }),
    },
    grade8_functions_1_scaffold: {
        render: (ctx) => h(Grade8FunctionsRoute, { workspaceMode: 'grade8_functions_1_scaffold', ctx }),
    },
    grade8_functions_1_practice: {
        render: (ctx) => h(Grade8FunctionsRoute, { workspaceMode: 'grade8_functions_1_practice', ctx }),
    },
    grade8_patterns_scaffold: {
        render: (ctx) => h(Grade8PatternsRoute, { workspaceMode: 'grade8_patterns_scaffold', ctx }),
    },
    grade8_patterns_practice: {
        render: (ctx) => h(Grade8PatternsRoute, { workspaceMode: 'grade8_patterns_practice', ctx }),
    },
};
