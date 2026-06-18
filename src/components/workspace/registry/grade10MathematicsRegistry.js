import React, { useEffect, useState } from 'react';
import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../shared/EvaluatedWorkspaceModeShell';
const h = React.createElement;
import Grade10AlgebraicExpressionsScaffold from '../grade10/mathematics/algebraic-expressions/Grade10AlgebraicExpressionsScaffold';
import Grade10AlgebraicExpressionsPractice from '../grade10/mathematics/algebraic-expressions/Grade10AlgebraicExpressionsPractice';
import Grade10ExponentsScaffold from '../grade10/mathematics/exponents/Grade10ExponentsScaffold';
import Grade10ExponentsPractice from '../grade10/mathematics/exponents/Grade10ExponentsPractice';
import Grade10PatternsSequencesScaffold from '../grade10/mathematics/patterns-sequences/Grade10PatternsSequencesScaffold';
import Grade10PatternsSequencesPractice from '../grade10/mathematics/patterns-sequences/Grade10PatternsSequencesPractice';
import Grade10EquationsInequalitiesScaffold from '../grade10/mathematics/equations-inequalities/Grade10EquationsInequalitiesScaffold';
import Grade10EquationsInequalitiesPractice from '../grade10/mathematics/equations-inequalities/Grade10EquationsInequalitiesPractice';
import Grade10Trigonometry1Scaffold from '../grade10/mathematics/trigonometry-1/Grade10Trigonometry1Scaffold';
import Grade10Trigonometry1Practice from '../grade10/mathematics/trigonometry-1/Grade10Trigonometry1Practice';
import { useGrade10AlgebraicExpressionsController, AlgebraicExpressionsVisualAids as Grade10AlgebraicExpressionsVisualAids } from '../grade10/mathematics/algebraic-expressions';
import { useGrade10ExponentsController, ExponentsVisualAids as Grade10ExponentsVisualAids } from '../grade10/mathematics/exponents';
import { useGrade10PatternsSequencesController, PatternsSequencesVisualAids as Grade10PatternsSequencesVisualAids } from '../grade10/mathematics/patterns-sequences';
import { useGrade10EquationsInequalitiesController, EquationsInequalitiesVisualAids as Grade10EquationsInequalitiesVisualAids } from '../grade10/mathematics/equations-inequalities';
import { useGrade10Trigonometry1Controller, Trigonometry1VisualAids as Grade10Trigonometry1VisualAids } from '../grade10/mathematics/trigonometry-1';

const Grade10AlgebraicExpressionsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10AlgebraicExpressionsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10AlgExpVisualAids = () => h(Grade10AlgebraicExpressionsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade10_algebraic_expressions_scaffold') {
        return h(Grade10AlgebraicExpressionsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10AlgExpVisualAidsOpen: controller.visualAidsOpen,
            setG10AlgExpVisualAidsOpen: controller.setVisualAidsOpen,
            g10AlgExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10AlgExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10AlgExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10AlgExpScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10AlgExpScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10AlgExpScaffoldLoading: controller.scaffoldLoading,
            g10AlgExpScaffoldError: controller.scaffoldError,
            g10AlgExpScaffoldQuestion: controller.scaffoldQuestion,
            g10AlgExpScaffoldShowHint: controller.scaffoldShowHint,
            setG10AlgExpScaffoldShowHint: controller.setScaffoldShowHint,
            g10AlgExpScaffoldAnswer: controller.scaffoldAnswer,
            setG10AlgExpScaffoldAnswer: controller.setScaffoldAnswer,
            g10AlgExpScaffoldFeedback: controller.scaffoldFeedback,
            setG10AlgExpScaffoldFeedback: controller.setScaffoldFeedback,
            g10AlgExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG10AlgExpScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g10AlgExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG10AlgExpScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g10AlgExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG10AlgExpScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade10AlgExpVisualAids,
        });
    }

    if (workspaceMode === 'grade10_algebraic_expressions_practice') {
        return h(Grade10AlgebraicExpressionsPractice, {
            onBack: ctx.onBack,
            g10AlgExpVisualAidsOpen: controller.visualAidsOpen,
            setG10AlgExpVisualAidsOpen: controller.setVisualAidsOpen,
            g10AlgExpPracticeDifficulty: controller.practiceDifficulty,
            setG10AlgExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10AlgExpPractice: controller.fetchPractice,
            g10AlgExpPracticeLoading: controller.practiceLoading,
            g10AlgExpPracticeError: controller.practiceError,
            g10AlgExpPracticeQuestions: controller.practiceQuestions,
            g10AlgExpPracticeAnswers: controller.practiceAnswers,
            setG10AlgExpPracticeAnswers: controller.setPracticeAnswers,
            g10AlgExpPracticeFeedback: controller.practiceFeedback,
            setG10AlgExpPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade10AlgExpVisualAids,
        });
    }

    return null;
};

const Grade10ExponentsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10ExponentsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10ExpVisualAids = () => h(Grade10ExponentsVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade10_exponents_scaffold') {
        return h(Grade10ExponentsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10ExpVisualAidsOpen: controller.visualAidsOpen,
            setG10ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g10ExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10ExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10ExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10ExpScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10ExpScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10ExpScaffoldLoading: controller.scaffoldLoading,
            g10ExpScaffoldError: controller.scaffoldError,
            g10ExpScaffoldQuestion: controller.scaffoldQuestion,
            g10ExpScaffoldShowHint: controller.scaffoldShowHint,
            setG10ExpScaffoldShowHint: controller.setScaffoldShowHint,
            g10ExpScaffoldAnswer: controller.scaffoldAnswer,
            setG10ExpScaffoldAnswer: controller.setScaffoldAnswer,
            g10ExpScaffoldFeedback: controller.scaffoldFeedback,
            setG10ExpScaffoldFeedback: controller.setScaffoldFeedback,
            g10ExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG10ExpScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g10ExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG10ExpScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g10ExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG10ExpScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade10ExpVisualAids,
        });
    }

    if (workspaceMode === 'grade10_exponents_practice') {
        return h(Grade10ExponentsPractice, {
            onBack: ctx.onBack,
            g10ExpVisualAidsOpen: controller.visualAidsOpen,
            setG10ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g10ExpPracticeDifficulty: controller.practiceDifficulty,
            setG10ExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10ExpPractice: controller.fetchPractice,
            g10ExpPracticeLoading: controller.practiceLoading,
            g10ExpPracticeError: controller.practiceError,
            g10ExpPracticeQuestions: controller.practiceQuestions,
            g10ExpPracticeAnswers: controller.practiceAnswers,
            setG10ExpPracticeAnswers: controller.setPracticeAnswers,
            g10ExpPracticeFeedback: controller.practiceFeedback,
            setG10ExpPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGrade10ExpVisualAids,
        });
    }

    return null;
};

const Grade10PatternsSequencesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10PatternsSequencesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10PatSeqVisualAids = () => h(Grade10PatternsSequencesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade10_patterns_sequences_scaffold') {
        return h(Grade10PatternsSequencesScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10PatSeqVisualAidsOpen: controller.visualAidsOpen,
            setG10PatSeqVisualAidsOpen: controller.setVisualAidsOpen,
            g10PatSeqScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10PatSeqScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10PatSeqScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10PatSeqScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10PatternsSequencesScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10PatSeqScaffoldLoading: controller.scaffoldLoading,
            g10PatSeqScaffoldError: controller.scaffoldError,
            g10PatSeqScaffoldQuestion: controller.scaffoldQuestion,
            g10PatSeqScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG10PatSeqScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g10PatSeqScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG10PatSeqScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g10PatSeqScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG10PatSeqScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            g10PatSeqScaffoldAnswer: controller.scaffoldAnswer,
            setG10PatSeqScaffoldAnswer: controller.setG10PatSeqScaffoldAnswer,
            g10PatSeqScaffoldFeedback: controller.scaffoldFeedback,
            setG10PatSeqScaffoldFeedback: controller.setScaffoldFeedback,
            g10PatSeqScaffoldShowHint: controller.scaffoldShowHint,
            setG10PatSeqScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10PatternsSequencesVisualAids: renderGrade10PatSeqVisualAids,
        });
    }

    if (workspaceMode === 'grade10_patterns_sequences_practice') {
        return h(Grade10PatternsSequencesPractice, {
            onBack: ctx.onBack,
            g10PatSeqVisualAidsOpen: controller.visualAidsOpen,
            setG10PatSeqVisualAidsOpen: controller.setVisualAidsOpen,
            g10PatSeqPracticeDifficulty: controller.practiceDifficulty,
            setG10PatSeqPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10PatternsSequencesPractice: controller.fetchPractice,
            g10PatSeqPracticeLoading: controller.practiceLoading,
            g10PatSeqPracticeError: controller.practiceError,
            g10PatSeqPracticeQuestions: controller.practiceQuestions,
            g10PatSeqPracticeAnswers: controller.practiceAnswers,
            setG10PatSeqPracticeAnswers: controller.setPracticeAnswers,
            g10PatSeqPracticeFeedback: controller.practiceFeedback,
            setG10PatSeqPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10PatternsSequencesVisualAids: renderGrade10PatSeqVisualAids,
        });
    }

    return null;
};

const Grade10EquationsInequalitiesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade10EquationsInequalitiesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10EqIneqVisualAids = () => h(Grade10EquationsInequalitiesVisualAids);

    if (workspaceMode === 'grade10_equations_inequalities_scaffold') {
        return h(Grade10EquationsInequalitiesScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10EqIneqVisualAidsOpen: controller.visualAidsOpen,
            setG10EqIneqVisualAidsOpen: controller.setVisualAidsOpen,
            g10EqIneqScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10EqIneqScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10EqIneqScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10EqIneqScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10EqIneqScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10EqIneqScaffoldLoading: controller.scaffoldLoading,
            g10EqIneqScaffoldError: controller.scaffoldError,
            g10EqIneqScaffoldQuestion: controller.scaffoldQuestion,
            g10EqIneqScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG10EqIneqScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g10EqIneqScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG10EqIneqScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g10EqIneqScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG10EqIneqScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            g10EqIneqScaffoldAnswer: controller.scaffoldAnswer,
            setG10EqIneqScaffoldAnswer: controller.setG10EqIneqScaffoldAnswer,
            g10EqIneqScaffoldFeedback: controller.scaffoldFeedback,
            setG10EqIneqScaffoldFeedback: controller.setScaffoldFeedback,
            g10EqIneqScaffoldShowHint: controller.scaffoldShowHint,
            setG10EqIneqScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10EqIneqVisualAids,
        });
    }

    if (workspaceMode === 'grade10_equations_inequalities_practice') {
        return h(Grade10EquationsInequalitiesPractice, {
            onBack: ctx.onBack,
            g10EqIneqVisualAidsOpen: controller.visualAidsOpen,
            setG10EqIneqVisualAidsOpen: controller.setVisualAidsOpen,
            g10EqIneqPracticeDifficulty: controller.practiceDifficulty,
            setG10EqIneqPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10EqIneqPractice: controller.fetchPractice,
            g10EqIneqPracticeLoading: controller.practiceLoading,
            g10EqIneqPracticeError: controller.practiceError,
            g10EqIneqPracticeQuestions: controller.practiceQuestions,
            g10EqIneqPracticeAnswers: controller.practiceAnswers,
            setG10EqIneqPracticeAnswers: controller.setPracticeAnswers,
            g10EqIneqPracticeFeedback: controller.practiceFeedback,
            setG10EqIneqPracticeFeedback: controller.setPracticeFeedback,
            renderGrade10EqIneqVisualAids,
        });
    }

    return null;
};

const Grade10Trigonometry1Route = ({ workspaceMode, ctx }) => {
    const controller = useGrade10Trigonometry1Controller({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGrade10Trig1VisualAids = () => h(Grade10Trigonometry1VisualAids);

    if (workspaceMode === 'grade10_trigonometry_1_scaffold') {
        return h(Grade10Trigonometry1Scaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g10Trig1VisualAidsOpen: controller.visualAidsOpen,
            setG10Trig1VisualAidsOpen: controller.setVisualAidsOpen,
            g10Trig1ScaffoldDifficulty: controller.scaffoldDifficulty,
            setG10Trig1ScaffoldDifficulty: controller.setScaffoldDifficulty,
            g10Trig1ScaffoldStepIndex: controller.scaffoldStepIndex,
            setG10Trig1ScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchGrade10Trig1ScaffoldQuestion: controller.fetchScaffoldQuestion,
            g10Trig1ScaffoldLoading: controller.scaffoldLoading,
            g10Trig1ScaffoldError: controller.scaffoldError,
            g10Trig1ScaffoldQuestion: controller.scaffoldQuestion,
            g10Trig1ScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            setG10Trig1ScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            g10Trig1ScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            setG10Trig1ScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            g10Trig1ScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            setG10Trig1ScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            g10Trig1ScaffoldAnswer: controller.scaffoldAnswer,
            setG10Trig1ScaffoldAnswer: controller.setG10Trig1ScaffoldAnswer,
            g10Trig1ScaffoldFeedback: controller.scaffoldFeedback,
            setG10Trig1ScaffoldFeedback: controller.setScaffoldFeedback,
            g10Trig1ScaffoldShowHint: controller.scaffoldShowHint,
            setG10Trig1ScaffoldShowHint: controller.setScaffoldShowHint,
            renderGrade10Trig1VisualAids,
        });
    }

    if (workspaceMode === 'grade10_trigonometry_1_practice') {
        return h(Grade10Trigonometry1Practice, {
            onBack: ctx.onBack,
            g10Trig1VisualAidsOpen: controller.visualAidsOpen,
            setG10Trig1VisualAidsOpen: controller.setVisualAidsOpen,
            g10Trig1PracticeDifficulty: controller.practiceDifficulty,
            setG10Trig1PracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade10Trig1Practice: controller.fetchPractice,
            g10Trig1PracticeLoading: controller.practiceLoading,
            g10Trig1PracticeError: controller.practiceError,
            g10Trig1PracticeQuestions: controller.practiceQuestions,
            g10Trig1PracticeAnswers: controller.practiceAnswers,
            setG10Trig1PracticeAnswers: controller.setPracticeAnswers,
            g10Trig1PracticeFeedback: controller.practiceFeedback,
            setG10Trig1PracticeFeedback: controller.setPracticeFeedback,
            renderGrade10Trig1VisualAids,
        });
    }

    return null;
};


export const grade10MathematicsRegistry = {
    grade10_algebraic_expressions_scaffold: {
        render: (ctx) => h(Grade10AlgebraicExpressionsRoute, { workspaceMode: 'grade10_algebraic_expressions_scaffold', ctx }),
    },
    grade10_algebraic_expressions_practice: {
        render: (ctx) => h(Grade10AlgebraicExpressionsRoute, { workspaceMode: 'grade10_algebraic_expressions_practice', ctx }),
    },
    grade10_exponents_scaffold: {
        render: (ctx) => h(Grade10ExponentsRoute, { workspaceMode: 'grade10_exponents_scaffold', ctx }),
    },
    grade10_exponents_practice: {
        render: (ctx) => h(Grade10ExponentsRoute, { workspaceMode: 'grade10_exponents_practice', ctx }),
    },
    grade10_patterns_sequences_scaffold: {
        render: (ctx) => h(Grade10PatternsSequencesRoute, { workspaceMode: 'grade10_patterns_sequences_scaffold', ctx }),
    },
    grade10_patterns_sequences_practice: {
        render: (ctx) => h(Grade10PatternsSequencesRoute, { workspaceMode: 'grade10_patterns_sequences_practice', ctx }),
    },
    grade10_equations_inequalities_scaffold: {
        render: (ctx) => h(Grade10EquationsInequalitiesRoute, { workspaceMode: 'grade10_equations_inequalities_scaffold', ctx }),
    },
    grade10_equations_inequalities_practice: {
        render: (ctx) => h(Grade10EquationsInequalitiesRoute, { workspaceMode: 'grade10_equations_inequalities_practice', ctx }),
    },
    grade10_trigonometry_1_scaffold: {
        render: (ctx) => h(Grade10Trigonometry1Route, { workspaceMode: 'grade10_trigonometry_1_scaffold', ctx }),
    },
    grade10_trigonometry_1_practice: {
        render: (ctx) => h(Grade10Trigonometry1Route, { workspaceMode: 'grade10_trigonometry_1_practice', ctx }),
    },
};
