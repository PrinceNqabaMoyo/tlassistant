import React from 'react';
import { useGrade7EmsController } from '../grade7/ems/controller';
import EmsScaffold from '../grade7/ems/EmsScaffold';
import EmsPractice from '../grade7/ems/EmsPractice';
import EmsAssessment from '../grade7/ems/EmsAssessment';

const h = React.createElement;

const TOPIC_CONFIGS = {
    'grade7_ems_money_needs': {
        topic: 'grade7_ems_money_and_needs',
        title: 'Grade 7 EMS • Term 1 • Money and Needs',
    },
    'grade7_ems_needs_and_wants': {
        topic: 'grade7_ems_needs_and_wants',
        title: 'Grade 7 EMS • Term 1 • Needs and Wants',
    },
    'grade7_ems_goods_and_services': {
        topic: 'grade7_ems_goods_and_services',
        title: 'Grade 7 EMS • Term 1 • Goods and Services',
    },
    'grade7_ems_businesses': {
        topic: 'grade7_ems_businesses',
        title: 'Grade 7 EMS • Term 1 • Businesses',
    },
    'grade7_ems_accounting_concepts': {
        topic: 'grade7_ems_accounting_concepts',
        title: 'Grade 7 EMS • Term 2 • Accounting Concepts',
    },
    'grade7_ems_income_expenses': {
        topic: 'grade7_ems_income_and_expenses',
        title: 'Grade 7 EMS • Term 2 • Income and Expenses',
    },
    'grade7_ems_budgets': {
        topic: 'grade7_ems_budgets',
        title: 'Grade 7 EMS • Term 2 • Budgets',
    },
    'grade7_ems_entrepreneurship': {
        topic: 'grade7_ems_entrepreneurship',
        title: 'Grade 7 EMS • Term 3 • Entrepreneurship',
    },
    'grade7_ems_the_entrepreneur': {
        topic: 'grade7_ems_the_entrepreneur',
        title: 'Grade 7 EMS • Term 3 • The Entrepreneur',
    },
    'grade7_ems_starting_a_business': {
        topic: 'grade7_ems_starting_a_business',
        title: 'Grade 7 EMS • Term 3 • Starting a Business',
    },
    'grade7_ems_entrepreneurs_day': {
        topic: 'grade7_ems_entrepreneurs_day',
        title: 'Grade 7 EMS • Term 3 • Entrepreneurs Day',
    },
    'grade7_ems_inequality_and_poverty': {
        topic: 'grade7_ems_inequality_and_poverty',
        title: 'Grade 7 EMS • Term 3 • Inequality and Poverty',
    },
};

const Grade7EmsRoute = ({ workspaceMode, ctx }) => {
    // Mode is usually something like 'grade7_ems_money_needs_scaffold'
    const isScaffold = workspaceMode.endsWith('_scaffold');
    const isPractice = workspaceMode.endsWith('_practice');
    const isAssessment = workspaceMode.endsWith('_assessment');
    const baseMode = workspaceMode.replace('_scaffold', '').replace('_practice', '').replace('_assessment', '');
    
    const config = TOPIC_CONFIGS[baseMode];
    if (!config) return null;

    const controller = useGrade7EmsController({ workspaceMode, buildApiUrl: ctx.buildApiUrl, config });

    if (isScaffold) {
        return h(EmsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
            stepsLoading: controller.stepsLoading,
            visualAidsOpen: controller.visualAidsOpen,
            setVisualAidsOpen: controller.setVisualAidsOpen,
            scaffoldDifficulty: controller.scaffoldDifficulty,
            setScaffoldDifficulty: controller.setScaffoldDifficulty,
            scaffoldStepIndex: controller.scaffoldStepIndex,
            setScaffoldStepIndex: controller.setScaffoldStepIndex,
            fetchScaffoldQuestion: controller.fetchScaffoldQuestion,
            scaffoldLoading: controller.scaffoldLoading,
            scaffoldError: controller.scaffoldError,
            scaffoldQuestion: controller.scaffoldQuestion,
            scaffoldAnswer: controller.scaffoldAnswer,
            setScaffoldAnswer: controller.setScaffoldAnswer,
            scaffoldFeedback: controller.scaffoldFeedback,
            setScaffoldFeedback: controller.setScaffoldFeedback,
            scaffoldShowHint: controller.scaffoldShowHint,
            setScaffoldShowHint: controller.setScaffoldShowHint,
            renderVisualAids: () => null, // We can add visual aids later if needed
            isMarkingEnv: false,
            topicTitle: config.title
        });
    }

    if (isPractice) {
        return h(EmsPractice, {
            onBack: ctx.onBack,
            visualAidsOpen: controller.visualAidsOpen,
            setVisualAidsOpen: controller.setVisualAidsOpen,
            practiceDifficulty: controller.practiceDifficulty,
            setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice,
            practiceLoading: controller.practiceLoading,
            practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions,
            practiceAnswers: controller.practiceAnswers,
            setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback,
            setPracticeFeedback: controller.setPracticeFeedback,
            renderVisualAids: () => null,
            isMarkingEnv: false,
            topicTitle: config.title
        });
    }

    if (isAssessment) {
        return h(EmsAssessment, {
            onBack: ctx.onBack,
            buildApiUrl: ctx.buildApiUrl
        });
    }

    return null;
};

export const grade7EmsRegistry = {};

Object.keys(TOPIC_CONFIGS).forEach(baseMode => {
    grade7EmsRegistry[`${baseMode}_scaffold`] = { render: (ctx) => h(Grade7EmsRoute, { workspaceMode: `${baseMode}_scaffold`, ctx }) };
    grade7EmsRegistry[`${baseMode}_practice`] = { render: (ctx) => h(Grade7EmsRoute, { workspaceMode: `${baseMode}_practice`, ctx }) };
});
grade7EmsRegistry['grade7_ems_assessment'] = { render: (ctx) => h(Grade7EmsRoute, { workspaceMode: 'grade7_ems_assessment', ctx }) };
