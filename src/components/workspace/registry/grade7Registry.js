import React from 'react';
import Grade7WholeNumbersScaffold from '../grade7/mathematics/whole-numbers/Grade7WholeNumbersScaffold';
import Grade7WholeNumbersPractice from '../grade7/mathematics/whole-numbers/Grade7WholeNumbersPractice';
import Grade7ExponentsScaffold from '../grade7/mathematics/exponents/Grade7ExponentsScaffold';
import Grade7ExponentsPractice from '../grade7/mathematics/exponents/Grade7ExponentsPractice';
import Grade7GeoConstructScaffold from '../grade7/mathematics/geometry-construction/Grade7GeoConstructScaffold';
import Grade7GeoConstructPractice from '../grade7/mathematics/geometry-construction/Grade7GeoConstructPractice';
import Grade7Geo2DScaffold from '../grade7/mathematics/geometry-2d/Grade7Geo2DScaffold';
import Grade7Geo2DPractice from '../grade7/mathematics/geometry-2d/Grade7Geo2DPractice';
import Grade7StraightLinesScaffold from '../grade7/mathematics/geometry-straight-lines/Grade7StraightLinesScaffold';
import Grade7StraightLinesPractice from '../grade7/mathematics/geometry-straight-lines/Grade7StraightLinesPractice';

import { useGrade7WholeNumbersController, WholeNumbersVisualAids } from '../grade7/mathematics/whole-numbers';
import { useGrade7ExponentsController, ExponentsVisualAids } from '../grade7/mathematics/exponents';
import { useGrade7GeoConstructController, GeoConstructVisualAids } from '../grade7/mathematics/geometry-construction';
import { useGrade7Geo2DController, Geo2DVisualAids } from '../grade7/mathematics/geometry-2d';
import { useGrade7StraightLinesController, StraightLinesVisualAids } from '../grade7/mathematics/geometry-straight-lines';

const h = React.createElement;

const Grade7WholeNumbersRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade7WholeNumbersController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderWholeNumbersVisualAids = () => h(WholeNumbersVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
        multiplesBase: controller.multiplesBase,
        setMultiplesBase: controller.setMultiplesBase,
        multiplesMax: controller.multiplesMax,
        setMultiplesMax: controller.setMultiplesMax,
        placeValueInput: controller.placeValueInput,
        setPlaceValueInput: controller.setPlaceValueInput,
        roundingNumber: controller.roundingNumber,
        setRoundingNumber: controller.setRoundingNumber,
        roundingBase: controller.roundingBase,
        setRoundingBase: controller.setRoundingBase,
    });

    if (workspaceMode === 'grade7_whole_scaffold') {
        return h(Grade7WholeNumbersScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            g7WholeVisualAidsOpen: controller.visualAidsOpen,
            setG7WholeVisualAidsOpen: controller.setVisualAidsOpen,
            g7WholeScaffoldDifficulty: controller.scaffoldDifficulty,
            setG7WholeScaffoldDifficulty: controller.setScaffoldDifficulty,
            g7WholeScaffoldStepIndex: controller.scaffoldStepIndex,
            setG7WholeScaffoldStepIndex: controller.setScaffoldStepIndex,
            setG7WholeScaffoldFeedback: controller.setScaffoldFeedback,
            setG7WholeScaffoldShowHint: controller.setScaffoldShowHint,
            setG7WholeScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            setG7WholeScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            setG7WholeScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            fetchGrade7WholeNumbersScaffoldQuestion: controller.fetchScaffoldQuestion,
            g7WholeScaffoldLoading: controller.scaffoldLoading,
            g7WholeScaffoldError: controller.scaffoldError,
            g7WholeScaffoldQuestion: controller.scaffoldQuestion,
            g7WholeScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            g7WholeScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            g7WholeScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            g7WholeScaffoldShowHint: controller.scaffoldShowHint,
            g7WholeScaffoldAnswer: controller.scaffoldAnswer,
            setG7WholeScaffoldAnswer: controller.setScaffoldAnswer,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            g7WholeScaffoldFeedback: controller.scaffoldFeedback,
            renderWholeNumbersVisualAids,
        });
    }

    if (workspaceMode === 'grade7_whole_practice') {
        return h(Grade7WholeNumbersPractice, {
            onBack: ctx.onBack,
            g7WholeVisualAidsOpen: controller.visualAidsOpen,
            setG7WholeVisualAidsOpen: controller.setVisualAidsOpen,
            g7WholePracticeDifficulty: controller.practiceDifficulty,
            setG7WholePracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade7WholeNumbersPractice: controller.fetchPractice,
            g7WholePracticeLoading: controller.practiceLoading,
            g7WholePracticeError: controller.practiceError,
            g7WholePracticeQuestions: controller.practiceQuestions,
            g7WholePracticeAnswers: controller.practiceAnswers,
            setG7WholePracticeAnswers: controller.setPracticeAnswers,
            g7WholePracticeFeedback: controller.practiceFeedback,
            setG7WholePracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            renderWholeNumbersVisualAids,
        });
    }

    return null;
};

const Grade7ExponentsRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade7ExponentsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderExponentsVisualAids = () => h(ExponentsVisualAids, {
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

    if (workspaceMode === 'grade7_exponents_scaffold') {
        return h(Grade7ExponentsScaffold, {
            onBack: ctx.onBack,
            exponentsSteps: controller.scaffoldSteps,
            g7ExpVisualAidsOpen: controller.visualAidsOpen,
            setG7ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g7ExpScaffoldDifficulty: controller.scaffoldDifficulty,
            setG7ExpScaffoldDifficulty: controller.setScaffoldDifficulty,
            g7ExpScaffoldStepIndex: controller.scaffoldStepIndex,
            setG7ExpScaffoldStepIndex: controller.setScaffoldStepIndex,
            setG7ExpScaffoldFeedback: controller.setScaffoldFeedback,
            setG7ExpScaffoldShowHint: controller.setScaffoldShowHint,
            setG7ExpScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            setG7ExpScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            setG7ExpScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            fetchGrade7ExponentsScaffoldQuestion: controller.fetchScaffoldQuestion,
            g7ExpScaffoldLoading: controller.scaffoldLoading,
            g7ExpScaffoldError: controller.scaffoldError,
            g7ExpScaffoldQuestion: controller.scaffoldQuestion,
            g7ExpScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            g7ExpScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            g7ExpScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            g7ExpScaffoldShowHint: controller.scaffoldShowHint,
            g7ExpScaffoldAnswer: controller.scaffoldAnswer,
            setG7ExpScaffoldAnswer: controller.setScaffoldAnswer,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            formatExponentCarets: ctx.formatExponentCarets,
            g7ExpScaffoldFeedback: controller.scaffoldFeedback,
            renderExponentsVisualAids,
        });
    }

    if (workspaceMode === 'grade7_exponents_practice') {
        return h(Grade7ExponentsPractice, {
            onBack: ctx.onBack,
            g7ExpVisualAidsOpen: controller.visualAidsOpen,
            setG7ExpVisualAidsOpen: controller.setVisualAidsOpen,
            g7ExpPracticeDifficulty: controller.practiceDifficulty,
            setG7ExpPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade7ExponentsPractice: controller.fetchPractice,
            g7ExpPracticeLoading: controller.practiceLoading,
            g7ExpPracticeError: controller.practiceError,
            g7ExpPracticeQuestions: controller.practiceQuestions,
            g7ExpPracticeAnswers: controller.practiceAnswers,
            setG7ExpPracticeAnswers: controller.setPracticeAnswers,
            g7ExpPracticeFeedback: controller.practiceFeedback,
            setG7ExpPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            formatExponentCarets: ctx.formatExponentCarets,
            renderExponentsVisualAids,
        });
    }

    return null;
};

const Grade7GeoConstructRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade7GeoConstructController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGeoConstructVisualAids = () => h(GeoConstructVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade7_geo_construct_scaffold') {
        return h(Grade7GeoConstructScaffold, {
            onBack: ctx.onBack,
            geoConstructSteps: controller.scaffoldSteps,
            g7GeoConstructVisualAidsOpen: controller.visualAidsOpen,
            setG7GeoConstructVisualAidsOpen: controller.setVisualAidsOpen,
            g7GeoConstructScaffoldDifficulty: controller.scaffoldDifficulty,
            setG7GeoConstructScaffoldDifficulty: controller.setScaffoldDifficulty,
            g7GeoConstructScaffoldStepIndex: controller.scaffoldStepIndex,
            setG7GeoConstructScaffoldStepIndex: controller.setScaffoldStepIndex,
            setG7GeoConstructScaffoldFeedback: controller.setScaffoldFeedback,
            setG7GeoConstructScaffoldShowHint: controller.setScaffoldShowHint,
            setG7GeoConstructScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            setG7GeoConstructScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            setG7GeoConstructScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            fetchGrade7GeometryConstructionScaffoldQuestion: controller.fetchScaffoldQuestion,
            g7GeoConstructScaffoldLoading: controller.scaffoldLoading,
            g7GeoConstructScaffoldError: controller.scaffoldError,
            g7GeoConstructScaffoldQuestion: controller.scaffoldQuestion,
            g7GeoConstructScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            g7GeoConstructScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            g7GeoConstructScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            g7GeoConstructScaffoldShowHint: controller.scaffoldShowHint,
            g7GeoConstructScaffoldAnswer: controller.scaffoldAnswer,
            setG7GeoConstructScaffoldAnswer: controller.setScaffoldAnswer,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            g7GeoConstructScaffoldFeedback: controller.scaffoldFeedback,
            renderGeoConstructVisualAids,
            renderGeoConstructionVisualAids: renderGeoConstructVisualAids,
        });
    }

    if (workspaceMode === 'grade7_geo_construct_practice') {
        return h(Grade7GeoConstructPractice, {
            onBack: ctx.onBack,
            g7GeoConstructVisualAidsOpen: controller.visualAidsOpen,
            setG7GeoConstructVisualAidsOpen: controller.setVisualAidsOpen,
            g7GeoConstructPracticeDifficulty: controller.practiceDifficulty,
            setG7GeoConstructPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade7GeometryConstructionPractice: controller.fetchPractice,
            g7GeoConstructPracticeLoading: controller.practiceLoading,
            g7GeoConstructPracticeError: controller.practiceError,
            g7GeoConstructPracticeQuestions: controller.practiceQuestions,
            g7GeoConstructPracticeAnswers: controller.practiceAnswers,
            setG7GeoConstructPracticeAnswers: controller.setPracticeAnswers,
            g7GeoConstructPracticeFeedback: controller.practiceFeedback,
            setG7GeoConstructPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGeoConstructVisualAids,
            renderGeoConstructionVisualAids: renderGeoConstructVisualAids,
        });
    }

    return null;
};

const Grade7Geo2DRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade7Geo2DController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderGeo2DVisualAids = () => h(Geo2DVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade7_geo2d_scaffold') {
        return h(Grade7Geo2DScaffold, {
            onBack: ctx.onBack,
            geo2DSteps: controller.scaffoldSteps,
            g7Geo2DVisualAidsOpen: controller.visualAidsOpen,
            setG7Geo2DVisualAidsOpen: controller.setVisualAidsOpen,
            g7Geo2DScaffoldDifficulty: controller.scaffoldDifficulty,
            setG7Geo2DScaffoldDifficulty: controller.setScaffoldDifficulty,
            g7Geo2DScaffoldStepIndex: controller.scaffoldStepIndex,
            setG7Geo2DScaffoldStepIndex: controller.setScaffoldStepIndex,
            setG7Geo2DScaffoldFeedback: controller.setScaffoldFeedback,
            setG7Geo2DScaffoldShowHint: controller.setScaffoldShowHint,
            setG7Geo2DScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            setG7Geo2DScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            setG7Geo2DScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            fetchGrade7Geo2DScaffoldQuestion: controller.fetchScaffoldQuestion,
            g7Geo2DScaffoldLoading: controller.scaffoldLoading,
            g7Geo2DScaffoldError: controller.scaffoldError,
            g7Geo2DScaffoldQuestion: controller.scaffoldQuestion,
            formatExponentCarets: ctx.formatExponentCarets,
            g7Geo2DScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            g7Geo2DScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            g7Geo2DScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            g7Geo2DScaffoldShowHint: controller.scaffoldShowHint,
            g7Geo2DScaffoldAnswer: controller.scaffoldAnswer,
            setG7Geo2DScaffoldAnswer: controller.setScaffoldAnswer,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            g7Geo2DScaffoldFeedback: controller.scaffoldFeedback,
            renderGeo2DVisualAids,
        });
    }

    if (workspaceMode === 'grade7_geo2d_practice') {
        return h(Grade7Geo2DPractice, {
            onBack: ctx.onBack,
            g7Geo2DVisualAidsOpen: controller.visualAidsOpen,
            setG7Geo2DVisualAidsOpen: controller.setVisualAidsOpen,
            g7Geo2DPracticeDifficulty: controller.practiceDifficulty,
            setG7Geo2DPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade7Geo2DPractice: controller.fetchPractice,
            g7Geo2DPracticeLoading: controller.practiceLoading,
            g7Geo2DPracticeError: controller.practiceError,
            g7Geo2DPracticeQuestions: controller.practiceQuestions,
            g7Geo2DPracticeAnswers: controller.practiceAnswers,
            setG7Geo2DPracticeAnswers: controller.setPracticeAnswers,
            g7Geo2DPracticeFeedback: controller.practiceFeedback,
            setG7Geo2DPracticeFeedback: controller.setPracticeFeedback,
            formatExponentCarets: ctx.formatExponentCarets,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderGeo2DVisualAids,
        });
    }

    return null;
};

const Grade7StraightLinesRoute = ({ workspaceMode, ctx }) => {
    const controller = useGrade7StraightLinesController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });

    const renderStraightLinesVisualAids = () => h(StraightLinesVisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    if (workspaceMode === 'grade7_straight_lines_scaffold') {
        return h(Grade7StraightLinesScaffold, {
            onBack: ctx.onBack,
            straightLinesSteps: controller.scaffoldSteps,
            g7StraightVisualAidsOpen: controller.visualAidsOpen,
            setG7StraightVisualAidsOpen: controller.setVisualAidsOpen,
            g7StraightScaffoldDifficulty: controller.scaffoldDifficulty,
            setG7StraightScaffoldDifficulty: controller.setScaffoldDifficulty,
            g7StraightScaffoldStepIndex: controller.scaffoldStepIndex,
            setG7StraightScaffoldStepIndex: controller.setScaffoldStepIndex,
            setG7StraightScaffoldFeedback: controller.setScaffoldFeedback,
            setG7StraightScaffoldShowHint: controller.setScaffoldShowHint,
            setG7StraightScaffoldCheckpointIndex: controller.setScaffoldCheckpointIndex,
            setG7StraightScaffoldCheckpointAnswers: controller.setScaffoldCheckpointAnswers,
            setG7StraightScaffoldCheckpointFeedback: controller.setScaffoldCheckpointFeedback,
            fetchGrade7StraightLinesScaffoldQuestion: controller.fetchScaffoldQuestion,
            g7StraightScaffoldLoading: controller.scaffoldLoading,
            g7StraightScaffoldError: controller.scaffoldError,
            g7StraightScaffoldQuestion: controller.scaffoldQuestion,
            g7StraightScaffoldCheckpointIndex: controller.scaffoldCheckpointIndex,
            g7StraightScaffoldCheckpointAnswers: controller.scaffoldCheckpointAnswers,
            g7StraightScaffoldCheckpointFeedback: controller.scaffoldCheckpointFeedback,
            g7StraightScaffoldShowHint: controller.scaffoldShowHint,
            g7StraightScaffoldAnswer: controller.scaffoldAnswer,
            setG7StraightScaffoldAnswer: controller.setScaffoldAnswer,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            g7StraightScaffoldFeedback: controller.scaffoldFeedback,
            renderStraightLinesVisualAids,
        });
    }

    if (workspaceMode === 'grade7_straight_lines_practice') {
        return h(Grade7StraightLinesPractice, {
            onBack: ctx.onBack,
            g7StraightVisualAidsOpen: controller.visualAidsOpen,
            setG7StraightVisualAidsOpen: controller.setVisualAidsOpen,
            g7StraightPracticeDifficulty: controller.practiceDifficulty,
            setG7StraightPracticeDifficulty: controller.setPracticeDifficulty,
            fetchGrade7StraightLinesPractice: controller.fetchPractice,
            g7StraightPracticeLoading: controller.practiceLoading,
            g7StraightPracticeError: controller.practiceError,
            g7StraightPracticeQuestions: controller.practiceQuestions,
            g7StraightPracticeAnswers: controller.practiceAnswers,
            setG7StraightPracticeAnswers: controller.setPracticeAnswers,
            g7StraightPracticeFeedback: controller.practiceFeedback,
            setG7StraightPracticeFeedback: controller.setPracticeFeedback,
            normalizeWholeNumberAnswer: ctx.normalizeWholeNumberAnswer,
            normalizeTextAnswer: ctx.normalizeTextAnswer,
            renderStraightLinesVisualAids,
        });
    }

    return null;
};

export const grade7Registry = {
    grade7_whole_scaffold: {
        render: (ctx) => h(Grade7WholeNumbersRoute, { workspaceMode: 'grade7_whole_scaffold', ctx }),
    },
    grade7_whole_practice: {
        render: (ctx) => h(Grade7WholeNumbersRoute, { workspaceMode: 'grade7_whole_practice', ctx }),
    },
    grade7_exponents_scaffold: {
        render: (ctx) => h(Grade7ExponentsRoute, { workspaceMode: 'grade7_exponents_scaffold', ctx }),
    },
    grade7_exponents_practice: {
        render: (ctx) => h(Grade7ExponentsRoute, { workspaceMode: 'grade7_exponents_practice', ctx }),
    },
    grade7_geo_construct_scaffold: {
        render: (ctx) => h(Grade7GeoConstructRoute, { workspaceMode: 'grade7_geo_construct_scaffold', ctx }),
    },
    grade7_geo_construct_practice: {
        render: (ctx) => h(Grade7GeoConstructRoute, { workspaceMode: 'grade7_geo_construct_practice', ctx }),
    },
    grade7_geo2d_scaffold: {
        render: (ctx) => h(Grade7Geo2DRoute, { workspaceMode: 'grade7_geo2d_scaffold', ctx }),
    },
    grade7_geo2d_practice: {
        render: (ctx) => h(Grade7Geo2DRoute, { workspaceMode: 'grade7_geo2d_practice', ctx }),
    },
    grade7_straight_lines_scaffold: {
        render: (ctx) => h(Grade7StraightLinesRoute, { workspaceMode: 'grade7_straight_lines_scaffold', ctx }),
    },
    grade7_straight_lines_practice: {
        render: (ctx) => h(Grade7StraightLinesRoute, { workspaceMode: 'grade7_straight_lines_practice', ctx }),
    },
};
