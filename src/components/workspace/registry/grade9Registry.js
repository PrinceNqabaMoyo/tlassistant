import React from 'react';
import Grade9WholeNumbersScaffold from '../grade9/mathematics/whole-numbers/Grade9WholeNumbersScaffold';
import Grade9WholeNumbersPractice from '../grade9/mathematics/whole-numbers/Grade9WholeNumbersPractice';
import Grade9IntegersScaffold from '../grade9/mathematics/integers/Grade9IntegersScaffold';
import Grade9IntegersPractice from '../grade9/mathematics/integers/Grade9IntegersPractice';
import Grade9FractionsScaffold from '../grade9/mathematics/fractions/Grade9FractionsScaffold';
import Grade9FractionsPractice from '../grade9/mathematics/fractions/Grade9FractionsPractice';
import Grade9DecimalNotationScaffold from '../grade9/mathematics/decimal-notation/Grade9DecimalNotationScaffold';
import Grade9DecimalNotationPractice from '../grade9/mathematics/decimal-notation/Grade9DecimalNotationPractice';
import Grade9ExponentsScaffold from '../grade9/mathematics/exponents/Grade9ExponentsScaffold';
import Grade9ExponentsPractice from '../grade9/mathematics/exponents/Grade9ExponentsPractice';
import Grade9PatternsScaffold from '../grade9/mathematics/patterns/Grade9PatternsScaffold';
import Grade9PatternsPractice from '../grade9/mathematics/patterns/Grade9PatternsPractice';
import Grade9FunctionsRelationshipsScaffold from '../grade9/mathematics/functions-relationships/Grade9FunctionsRelationshipsScaffold';
import Grade9FunctionsRelationshipsPractice from '../grade9/mathematics/functions-relationships/Grade9FunctionsRelationshipsPractice';
import Grade9AlgebraicExpressionsScaffold from '../grade9/mathematics/algebraic-expressions-1/Grade9AlgebraicExpressionsScaffold';
import Grade9AlgebraicExpressionsPractice from '../grade9/mathematics/algebraic-expressions-1/Grade9AlgebraicExpressionsPractice';
import Grade9AlgebraicEquationsScaffold from '../grade9/mathematics/algebraic-equations-1/Grade9AlgebraicEquationsScaffold';
import Grade9AlgebraicEquationsPractice from '../grade9/mathematics/algebraic-equations-1/Grade9AlgebraicEquationsPractice';

import { useGrade9WholeNumbersController, WholeNumbersVisualAids as Grade9WholeNumbersVisualAids } from '../grade9/mathematics/whole-numbers';
import { useGrade9IntegersController, IntegersVisualAids as Grade9IntegersVisualAids } from '../grade9/mathematics/integers';
import { useGrade9FractionsController, FractionsVisualAids as Grade9FractionsVisualAids } from '../grade9/mathematics/fractions';
import { useGrade9DecimalNotationController, DecimalNotationVisualAids as Grade9DecimalNotationVisualAids } from '../grade9/mathematics/decimal-notation';
import { useGrade9ExponentsController, ExponentsVisualAids as Grade9ExponentsVisualAids } from '../grade9/mathematics/exponents';
import { useGrade9PatternsController, PatternsVisualAids as Grade9PatternsVisualAids } from '../grade9/mathematics/patterns';
import { useGrade9FunctionsRelationshipsController, FunctionsRelationshipsVisualAids as Grade9FunctionsRelationshipsVisualAids } from '../grade9/mathematics/functions-relationships';
import { useGrade9AlgebraicExpressions1Controller, AlgebraicExpressions1VisualAids } from '../grade9/mathematics/algebraic-expressions-1';
import { useGrade9AlgebraicEquations1Controller, AlgebraicEquations1VisualAids } from '../grade9/mathematics/algebraic-equations-1';

const h = React.createElement;

const Grade9AlgebraicEquations1Route = ({ workspaceMode, ctx }) => {
    const controller = useGrade9AlgebraicEquations1Controller({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9AlgEqVisualAids = () => h(AlgebraicEquations1VisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_algebraic_equations_1_scaffold') {
        return h(Grade9AlgebraicEquationsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9AlgEqVisualAidsOpen: controller.visualAidsOpen,
            setG9AlgEqVisualAidsOpen: controller.setVisualAidsOpen,
            g9AlgEqScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9AlgEqScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9AlgEqScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9AlgEqScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade9AlgEqScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9AlgEqScaffoldLoading: controller.scaffoldLoading,
            g9AlgEqScaffoldError: controller.scaffoldError,
            g9AlgEqScaffoldQuestion: controller.scaffoldQuestion,
            g9AlgEqScaffoldShowHint: controller.scaffoldShowHint,
            setG9AlgEqScaffoldShowHint: controller.setScaffoldShowHint,
            g9AlgEqScaffoldAnswer: controller.scaffoldAnswer,
            setG9AlgEqScaffoldAnswer: controller.setScaffoldAnswer,
            g9AlgEqScaffoldFeedback: controller.scaffoldFeedback,
            setG9AlgEqScaffoldFeedback: controller.setScaffoldFeedback,
            g9AlgEqScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9AlgEqScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g9AlgEqScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9AlgEqScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g9AlgEqScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9AlgEqScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9AlgEqVisualAids,
        });
    }

    if (workspaceMode === 'grade9_algebraic_equations_1_practice') {
        return h(Grade9AlgebraicEquationsPractice, {
            onBack: ctx.onBack,
            g9AlgEqVisualAidsOpen: controller.visualAidsOpen,
            setG9AlgEqVisualAidsOpen: controller.setVisualAidsOpen,
            g9AlgEqPracticeDifficulty: controller.practiceDifficulty,
            setG9AlgEqPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9AlgEqPractice: controller.fetchPractice,
            g9AlgEqPracticeLoading: controller.practiceLoading,
            g9AlgEqPracticeError: controller.practiceError,
            g9AlgEqPracticeQuestions: controller.practiceQuestions,
            g9AlgEqPracticeAnswers: controller.practiceAnswers,
            setG9AlgEqPracticeAnswers: controller.setPracticeAnswers,
            g9AlgEqPracticeFeedback: controller.practiceFeedback,
            setG9AlgEqPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9AlgEqVisualAids,
        });
    }

    return null;
};

const Grade9AlgebraicExpressions1Route = ({ workspaceMode, ctx }) => {
    const controller = useGrade9AlgebraicExpressions1Controller({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9AlgExpVisualAids = () => h(AlgebraicExpressions1VisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_algebraic_expressions_1_scaffold') {
        return h(Grade9AlgebraicExpressionsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9AlgExpVisualAidsOpen: controller.visualAidsOpen,
            setG9AlgExpVisualAidsOpen: controller.setVisualAidsOpen,
            g9AlgExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9AlgExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9AlgExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9AlgExpScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade9AlgExpScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9AlgExpScaffoldLoading: controller.scaffoldLoading,
            g9AlgExpScaffoldError: controller.scaffoldError,
            g9AlgExpScaffoldQuestion: controller.scaffoldQuestion,
            g9AlgExpScaffoldShowHint: controller.scaffoldShowHint,
            setG9AlgExpScaffoldShowHint: controller.setG9AlgExpScaffoldShowHint,
            g9AlgExpScaffoldAnswer: controller.scaffoldAnswer,
            setG9AlgExpScaffoldAnswer: controller.setScaffoldAnswer,
            g9AlgExpScaffoldFeedback: controller.scaffoldFeedback,
            setG9AlgExpScaffoldFeedback: controller.setScaffoldFeedback,
            g9AlgExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9AlgExpScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g9AlgExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9AlgExpScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g9AlgExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9AlgExpScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9AlgExpVisualAids,
        });
    }

    if (workspaceMode === 'grade9_algebraic_expressions_1_practice') {
        return h(Grade9AlgebraicExpressionsPractice, {
            onBack: ctx.onBack,
            g9AlgExpVisualAidsOpen: controller.visualAidsOpen,
            setG9AlgExpVisualAidsOpen: controller.setVisualAidsOpen,
            g9AlgExpPracticeDifficulty: controller.practiceDifficulty,
            setG9AlgExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9AlgExpPractice: controller.fetchPractice,
            g9AlgExpPracticeLoading: controller.practiceLoading,
            g9AlgExpPracticeError: controller.practiceError,
            g9AlgExpPracticeQuestions: controller.practiceQuestions,
            g9AlgExpPracticeAnswers: controller.practiceAnswers,
            setG9AlgExpPracticeAnswers: controller.setPracticeAnswers,
            g9AlgExpPracticeFeedback: controller.practiceFeedback,
            setG9AlgExpPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9AlgExpVisualAids,
        });
    }

    return null;
};

const Grade9PatternsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9PatternsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9PatternsVisualAids = () => h(Grade9PatternsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_patterns_scaffold') {
        return h(Grade9PatternsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9PatVisualAidsOpen: controller.visualAidsOpen,
            setG9PatVisualAidsOpen: controller.setVisualAidsOpen,
            g9PatScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9PatScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9PatScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9PatScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade9PatternsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9PatScaffoldLoading: controller.scaffoldLoading,
            g9PatScaffoldError: controller.scaffoldError,
            g9PatScaffoldQuestion: controller.scaffoldQuestion,
            g9PatScaffoldShowHint: controller.scaffoldShowHint,
            setG9PatScaffoldShowHint: controller.setG9PatScaffoldShowHint,
            g9PatScaffoldAnswer: controller.scaffoldAnswer,
            setG9PatScaffoldAnswer: controller.setG9PatScaffoldAnswer,
            g9PatScaffoldFeedback: controller.scaffoldFeedback,
            setG9PatScaffoldFeedback: controller.setG9PatScaffoldFeedback,
            g9PatScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9PatScaffoldCheckpointIndex: controller.setG9PatScaffoldCheckpointIndex,
            g9PatScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9PatScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g9PatScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9PatScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            renderGrade9PatternsVisualAids,
        });
    }

    if (workspaceMode === 'grade9_patterns_practice') {
        return h(Grade9PatternsPractice, {
            onBack: ctx.onBack,
            g9PatVisualAidsOpen: controller.visualAidsOpen,
            setG9PatVisualAidsOpen: controller.setVisualAidsOpen,
            g9PatPracticeDifficulty: controller.practiceDifficulty,
            setG9PatPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9PatternsPractice: controller.fetchPractice,
            g9PatPracticeLoading: controller.practiceLoading,
            g9PatPracticeError: controller.practiceError,
            g9PatPracticeQuestions: controller.practiceQuestions,
            g9PatPracticeAnswers: controller.practiceAnswers,
            setG9PatPracticeAnswers: controller.setPracticeAnswers,
            g9PatPracticeFeedback: controller.practiceFeedback,
            setG9PatPracticeFeedback: controller.setPracticeFeedback,
            renderGrade9PatternsVisualAids,
        });
    }

    return null;
};

const Grade9FunctionsRelationshipsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9FunctionsRelationshipsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9FunctionsVisualAids = () => h(Grade9FunctionsRelationshipsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_functions_relationships_1_scaffold') {
        return h(Grade9FunctionsRelationshipsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9FuncVisualAidsOpen: controller.visualAidsOpen,
            setG9FuncVisualAidsOpen: controller.setVisualAidsOpen,
            g9FuncScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9FuncScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9FuncScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9FuncScaffoldStepIndex: controller.setG9FuncScaffoldStepIndex,
            fetchGrade9FunctionsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9FuncScaffoldLoading: controller.scaffoldLoading,
            g9FuncScaffoldError: controller.scaffoldError,
            g9FuncScaffoldQuestion: controller.scaffoldQuestion,
            g9FuncScaffoldShowHint: controller.scaffoldShowHint,
            setG9FuncScaffoldShowHint: controller.setG9FuncScaffoldShowHint,
            g9FuncScaffoldAnswer: controller.scaffoldAnswer,
            setG9FuncScaffoldAnswer: controller.setG9FuncScaffoldAnswer,
            g9FuncScaffoldFeedback: controller.scaffoldFeedback,
            setG9FuncScaffoldFeedback: controller.setG9FuncScaffoldFeedback,
            g9FuncScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9FuncScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g9FuncScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9FuncScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g9FuncScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9FuncScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9FunctionsVisualAids,
        });
    }

    if (workspaceMode === 'grade9_functions_relationships_1_practice') {
        return h(Grade9FunctionsRelationshipsPractice, {
            onBack: ctx.onBack,
            g9FuncVisualAidsOpen: controller.visualAidsOpen,
            setG9FuncVisualAidsOpen: controller.setVisualAidsOpen,
            g9FuncPracticeDifficulty: controller.practiceDifficulty,
            setG9FuncPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9FunctionsPractice: controller.fetchPractice,
            g9FuncPracticeLoading: controller.practiceLoading,
            g9FuncPracticeError: controller.practiceError,
            g9FuncPracticeQuestions: controller.practiceQuestions,
            g9FuncPracticeAnswers: controller.practiceAnswers,
            setG9FuncPracticeAnswers: controller.setPracticeAnswers,
            g9FuncPracticeFeedback: controller.practiceFeedback,
            setG9FuncPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9FunctionsVisualAids,
        });
    }

    return null;
};

const Grade9ExponentsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9ExponentsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9ExponentsVisualAids = () => h(Grade9ExponentsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_exponents_scaffold') {
        return h(Grade9ExponentsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9ExpVisualAidsOpen: controller.visualAidsOpen,
            setG9ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g9ExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9ExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9ExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9ExpScaffoldStepIndex: controller.setG9ExpScaffoldStepIndex,
            fetchGrade9ExponentsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9ExpScaffoldLoading: controller.scaffoldLoading,
            g9ExpScaffoldError: controller.scaffoldError,
            g9ExpScaffoldQuestion: controller.scaffoldQuestion,
            g9ExpScaffoldShowHint: controller.scaffoldShowHint,
            setG9ExpScaffoldShowHint: controller.setG9ExpScaffoldShowHint,
            g9ExpScaffoldAnswer: controller.scaffoldAnswer,
            setG9ExpScaffoldAnswer: controller.setG9ExpScaffoldAnswer,
            g9ExpScaffoldFeedback: controller.scaffoldFeedback,
            setG9ExpScaffoldFeedback: controller.setG9ExpScaffoldFeedback,
            g9ExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9ExpScaffoldCheckpointIndex: controller.setG9ExpScaffoldCheckpointIndex,
            g9ExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9ExpScaffoldCheckpointAnswers: controller.setG9ExpScaffoldCheckpointAnswers,
            g9ExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9ExpScaffoldCheckpointFeedback: controller.setG9ExpScaffoldCheckpointFeedback,
            renderGrade9ExponentsVisualAids,
        });
    }

    if (workspaceMode === 'grade9_exponents_practice') {
        return h(Grade9ExponentsPractice, {
            onBack: ctx.onBack,
            g9ExpVisualAidsOpen: controller.visualAidsOpen,
            setG9ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g9ExpPracticeDifficulty: controller.practiceDifficulty,
            setG9ExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9ExponentsPractice: controller.fetchPractice,
            g9ExpPracticeLoading: controller.practiceLoading,
            g9ExpPracticeError: controller.practiceError,
            g9ExpPracticeQuestions: controller.practiceQuestions,
            g9ExpPracticeAnswers: controller.practiceAnswers,
            setG9ExpPracticeAnswers: controller.setPracticeAnswers,
            g9ExpPracticeFeedback: controller.practiceFeedback,
            setG9ExpPracticeFeedback: controller.setPracticeFeedback,
            renderGrade9ExponentsVisualAids,
        });
    }

    return null;
};

const Grade9DecimalNotationRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9DecimalNotationController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9DecimalNotationVisualAids = () => h(Grade9DecimalNotationVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_decimal_notation_scaffold') {
        return h(Grade9DecimalNotationScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9DecVisualAidsOpen: controller.visualAidsOpen,
            setG9DecVisualAidsOpen: controller.setVisualAidsOpen,
            g9DecScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9DecScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9DecScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9DecScaffoldStepIndex: controller.setG9DecScaffoldStepIndex,
            fetchGrade9DecimalNotationScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9DecScaffoldLoading: controller.scaffoldLoading,
            g9DecScaffoldError: controller.scaffoldError,
            g9DecScaffoldQuestion: controller.scaffoldQuestion,
            g9DecScaffoldShowHint: controller.scaffoldShowHint,
            setG9DecScaffoldShowHint: controller.setG9DecScaffoldShowHint,
            g9DecScaffoldAnswer: controller.scaffoldAnswer,
            setG9DecScaffoldAnswer: controller.setG9DecScaffoldAnswer,
            g9DecScaffoldFeedback: controller.scaffoldFeedback,
            setG9DecScaffoldFeedback: controller.setG9DecScaffoldFeedback,
            g9DecScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9DecScaffoldCheckpointIndex: controller.setG9DecScaffoldCheckpointIndex,
            g9DecScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9DecScaffoldCheckpointAnswers: controller.setG9DecScaffoldCheckpointAnswers,
            g9DecScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9DecScaffoldCheckpointFeedback: controller.setG9DecScaffoldCheckpointFeedback,
            renderGrade9DecimalNotationVisualAids,
        });
    }

    if (workspaceMode === 'grade9_decimal_notation_practice') {
        return h(Grade9DecimalNotationPractice, {
            onBack: ctx.onBack,
            g9DecVisualAidsOpen: controller.visualAidsOpen,
            setG9DecVisualAidsOpen: controller.setVisualAidsOpen,
            g9DecPracticeDifficulty: controller.practiceDifficulty,
            setG9DecPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9DecimalNotationPractice: controller.fetchPractice,
            g9DecPracticeLoading: controller.practiceLoading,
            g9DecPracticeError: controller.practiceError,
            g9DecPracticeQuestions: controller.practiceQuestions,
            g9DecPracticeAnswers: controller.practiceAnswers,
            setG9DecPracticeAnswers: controller.setPracticeAnswers,
            g9DecPracticeFeedback: controller.practiceFeedback,
            setG9DecPracticeFeedback: controller.setPracticeFeedback,
            renderGrade9DecimalNotationVisualAids,
        });
    }

    return null;
};

const Grade9FractionsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9FractionsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9FractionsVisualAids = () => h(Grade9FractionsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_fractions_scaffold') {
        return h(Grade9FractionsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9FracVisualAidsOpen: controller.visualAidsOpen,
            setG9FracVisualAidsOpen: controller.setVisualAidsOpen,
            g9FracScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9FracScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9FracScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9FracScaffoldStepIndex: controller.setG9FracScaffoldStepIndex,
            fetchGrade9FractionsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9FracScaffoldLoading: controller.scaffoldLoading,
            g9FracScaffoldError: controller.scaffoldError,
            g9FracScaffoldQuestion: controller.scaffoldQuestion,
            g9FracScaffoldShowHint: controller.scaffoldShowHint,
            setG9FracScaffoldShowHint: controller.setG9FracScaffoldShowHint,
            g9FracScaffoldAnswer: controller.scaffoldAnswer,
            setG9FracScaffoldAnswer: controller.setG9FracScaffoldAnswer,
            g9FracScaffoldFeedback: controller.scaffoldFeedback,
            setG9FracScaffoldFeedback: controller.setG9FracScaffoldFeedback,
            g9FracScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9FracScaffoldCheckpointIndex: controller.setG9FracScaffoldCheckpointIndex,
            g9FracScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9FracScaffoldCheckpointAnswers: controller.setG9FracScaffoldCheckpointAnswers,
            g9FracScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9FracScaffoldCheckpointFeedback: controller.setG9FracScaffoldCheckpointFeedback,
            renderGrade9FractionsVisualAids,
        });
    }

    if (workspaceMode === 'grade9_fractions_practice') {
        return h(Grade9FractionsPractice, {
            onBack: ctx.onBack,
            g9FracVisualAidsOpen: controller.visualAidsOpen,
            setG9FracVisualAidsOpen: controller.setVisualAidsOpen,
            g9FracPracticeDifficulty: controller.practiceDifficulty,
            setG9FracPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9FractionsPractice: controller.fetchPractice,
            g9FracPracticeLoading: controller.practiceLoading,
            g9FracPracticeError: controller.practiceError,
            g9FracPracticeQuestions: controller.practiceQuestions,
            g9FracPracticeAnswers: controller.practiceAnswers,
            setG9FracPracticeAnswers: controller.setPracticeAnswers,
            g9FracPracticeFeedback: controller.practiceFeedback,
            setG9FracPracticeFeedback: controller.setPracticeFeedback,
            renderGrade9FractionsVisualAids,
        });
    }

    return null;
};

const Grade9IntegersRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9IntegersController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9IntegersVisualAids = () => h(Grade9IntegersVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_integers_scaffold') {
        return h(Grade9IntegersScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9IntVisualAidsOpen: controller.visualAidsOpen,
            setG9IntVisualAidsOpen: controller.setVisualAidsOpen,
            g9IntScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9IntScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9IntScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9IntScaffoldStepIndex: controller.setG9IntScaffoldStepIndex,
            fetchGrade9IntegersScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9IntScaffoldLoading: controller.scaffoldLoading,
            g9IntScaffoldError: controller.scaffoldError,
            g9IntScaffoldQuestion: controller.scaffoldQuestion,
            g9IntScaffoldShowHint: controller.scaffoldShowHint,
            setG9IntScaffoldShowHint: controller.setG9IntScaffoldShowHint,
            g9IntScaffoldAnswer: controller.scaffoldAnswer,
            setG9IntScaffoldAnswer: controller.setG9IntScaffoldAnswer,
            g9IntScaffoldFeedback: controller.scaffoldFeedback,
            setG9IntScaffoldFeedback: controller.setG9IntScaffoldFeedback,
            g9IntScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9IntScaffoldCheckpointIndex: controller.setG9IntScaffoldCheckpointIndex,
            g9IntScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9IntScaffoldCheckpointAnswers: controller.setG9IntScaffoldCheckpointAnswers,
            g9IntScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9IntScaffoldCheckpointFeedback: controller.setG9IntScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9IntegersVisualAids,
        });
    }

    if (workspaceMode === 'grade9_integers_practice') {
        return h(Grade9IntegersPractice, {
            onBack: ctx.onBack,
            g9IntVisualAidsOpen: controller.visualAidsOpen,
            setG9IntVisualAidsOpen: controller.setVisualAidsOpen,
            g9IntPracticeDifficulty: controller.practiceDifficulty,
            setG9IntPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9IntegersPractice: controller.fetchPractice,
            g9IntPracticeLoading: controller.practiceLoading,
            g9IntPracticeError: controller.practiceError,
            g9IntPracticeQuestions: controller.practiceQuestions,
            g9IntPracticeAnswers: controller.practiceAnswers,
            setG9IntPracticeAnswers: controller.setPracticeAnswers,
            g9IntPracticeFeedback: controller.practiceFeedback,
            setG9IntPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9IntegersVisualAids,
        });
    }

    return null;
};

const Grade9WholeNumbersRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade9WholeNumbersController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade9WholeNumbersVisualAids = () => h(Grade9WholeNumbersVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade9_whole_scaffold') {
        return h(Grade9WholeNumbersScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g9WholeVisualAidsOpen: controller.visualAidsOpen,
            setG9WholeVisualAidsOpen: controller.setVisualAidsOpen,
            g9WholeScaffoldDifficulty: controller.scaffoldDifficulty,
            setG9WholeScaffoldDifficulty: controller.setScaffoldDifficulty,
            g9WholeScaffoldStepIndex: controller.scaffoldStepIndex,
            setG9WholeScaffoldStepIndex: controller.setG9WholeScaffoldStepIndex,
            fetchGrade9WholeNumbersScaffoldQuestion: controller.fetchScaffoldQuestion,
            g9WholeScaffoldLoading: controller.scaffoldLoading,
            g9WholeScaffoldError: controller.scaffoldError,
            g9WholeScaffoldQuestion: controller.scaffoldQuestion,
            g9WholeScaffoldShowHint: controller.scaffoldShowHint,
            setG9WholeScaffoldShowHint: controller.setG9WholeScaffoldShowHint,
            g9WholeScaffoldAnswer: controller.scaffoldAnswer,
            setG9WholeScaffoldAnswer: controller.setG9WholeScaffoldAnswer,
            g9WholeScaffoldFeedback: controller.scaffoldFeedback,
            setG9WholeScaffoldFeedback: controller.setG9WholeScaffoldFeedback,
            g9WholeScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG9WholeScaffoldCheckpointIndex: controller.setG9WholeScaffoldCheckpointIndex,
            g9WholeScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG9WholeScaffoldCheckpointAnswers: controller.setG9WholeScaffoldCheckpointAnswers,
            g9WholeScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG9WholeScaffoldCheckpointFeedback: controller.setG9WholeScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9WholeNumbersVisualAids,
        });
    }

    if (workspaceMode === 'grade9_whole_practice') {
        return h(Grade9WholeNumbersPractice, {
            onBack: ctx.onBack,
            g9WholeVisualAidsOpen: controller.visualAidsOpen,
            setG9WholeVisualAidsOpen: controller.setVisualAidsOpen,
            g9WholePracticeDifficulty: controller.practiceDifficulty,
            setG9WholePracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade9WholeNumbersPractice: controller.fetchPractice,
            g9WholePracticeLoading: controller.practiceLoading,
            g9WholePracticeError: controller.practiceError,
            g9WholePracticeQuestions: controller.practiceQuestions,
            g9WholePracticeAnswers: controller.practiceAnswers,
            setG9WholePracticeAnswers: controller.setPracticeAnswers,
            g9WholePracticeFeedback: controller.practiceFeedback,
            setG9WholePracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade9WholeNumbersVisualAids,
        });
    }

    return null;
};

export const grade9Registry = {
    grade9_algebraic_equations_1_scaffold: {
        render: (ctx) => h(Grade9AlgebraicEquations1Route, { workspaceMode: 'grade9_algebraic_equations_1_scaffold', ctx }),
    },
    grade9_algebraic_equations_1_practice: {
        render: (ctx) => h(Grade9AlgebraicEquations1Route, { workspaceMode: 'grade9_algebraic_equations_1_practice', ctx }),
    },
    grade9_algebraic_expressions_1_scaffold: {
        render: (ctx) => h(Grade9AlgebraicExpressions1Route, { workspaceMode: 'grade9_algebraic_expressions_1_scaffold', ctx }),
    },
    grade9_algebraic_expressions_1_practice: {
        render: (ctx) => h(Grade9AlgebraicExpressions1Route, { workspaceMode: 'grade9_algebraic_expressions_1_practice', ctx }),
    },
    grade9_functions_relationships_1_scaffold: {
        render: (ctx) => h(Grade9FunctionsRelationshipsRoute, { workspaceMode: 'grade9_functions_relationships_1_scaffold', ctx }),
    },
    grade9_functions_relationships_1_practice: {
        render: (ctx) => h(Grade9FunctionsRelationshipsRoute, { workspaceMode: 'grade9_functions_relationships_1_practice', ctx }),
    },
    grade9_patterns_scaffold: {
        render: (ctx) => h(Grade9PatternsRoute, { workspaceMode: 'grade9_patterns_scaffold', ctx }),
    },
    grade9_patterns_practice: {
        render: (ctx) => h(Grade9PatternsRoute, { workspaceMode: 'grade9_patterns_practice', ctx }),
    },
    grade9_exponents_scaffold: {
        render: (ctx) => h(Grade9ExponentsRoute, { workspaceMode: 'grade9_exponents_scaffold', ctx }),
    },
    grade9_exponents_practice: {
        render: (ctx) => h(Grade9ExponentsRoute, { workspaceMode: 'grade9_exponents_practice', ctx }),
    },
    grade9_decimal_notation_scaffold: {
        render: (ctx) => h(Grade9DecimalNotationRoute, { workspaceMode: 'grade9_decimal_notation_scaffold', ctx }),
    },
    grade9_decimal_notation_practice: {
        render: (ctx) => h(Grade9DecimalNotationRoute, { workspaceMode: 'grade9_decimal_notation_practice', ctx }),
    },
    grade9_fractions_scaffold: {
        render: (ctx) => h(Grade9FractionsRoute, { workspaceMode: 'grade9_fractions_scaffold', ctx }),
    },
    grade9_fractions_practice: {
        render: (ctx) => h(Grade9FractionsRoute, { workspaceMode: 'grade9_fractions_practice', ctx }),
    },
    grade9_integers_scaffold: {
        render: (ctx) => h(Grade9IntegersRoute, { workspaceMode: 'grade9_integers_scaffold', ctx }),
    },
    grade9_integers_practice: {
        render: (ctx) => h(Grade9IntegersRoute, { workspaceMode: 'grade9_integers_practice', ctx }),
    },
    grade9_whole_scaffold: {
        render: (ctx) => h(Grade9WholeNumbersRoute, { workspaceMode: 'grade9_whole_scaffold', ctx }),
    },
    grade9_whole_practice: {
        render: (ctx) => h(Grade9WholeNumbersRoute, { workspaceMode: 'grade9_whole_practice', ctx }),
    },
};
