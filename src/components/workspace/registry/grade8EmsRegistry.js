import React from 'react';
import { useGrade8EmsController } from '../grade8/ems/controller';
import Grade8EmsScaffold from '../grade8/ems/Grade8EmsScaffold';
import Grade8EmsPractice from '../grade8/ems/Grade8EmsPractice';
import EmsAssessment from '../grade7/ems/EmsAssessment'; // Reuse the Grade 7 assessment component

const h = React.createElement;

const TOPIC_CONFIGS = {
    'grade8_ems_gov_and_society': {
        topic: 'grade8_ems_gov_and_society',
        title: 'Grade 8 EMS • Term 1 • Government and Society',
        steps: [
            { key: 'concepts', title: 'Concepts' },
            { key: 'discussion', title: 'Discussion' }
        ]
    },
    'grade8_ems_accounting_basics': {
        topic: 'grade8_ems_accounting_basics',
        title: 'Grade 8 EMS • Term 1 • Accounting Basics',
        steps: [
            { key: 'concepts', title: 'Concepts' },
            { key: 'accounting_equation', title: 'Accounting Equation' }
        ]
    },
    'grade8_ems_markets_and_production': {
        topic: 'grade8_ems_markets_and_production',
        title: 'Grade 8 EMS • Term 2 • Markets and Production',
        steps: [
            { key: 'concepts', title: 'Concepts' },
            { key: 'discussion', title: 'Discussion' }
        ]
    },
    'grade8_ems_crj': {
        topic: 'grade8_ems_crj',
        title: 'Grade 8 EMS • Term 2 • Cash Receipts Journal',
        steps: [
            { key: 'crj', title: 'CRJ' }
        ]
    },
    'grade8_ems_cpj_and_crj': {
        topic: 'grade8_ems_cpj_and_crj',
        title: 'Grade 8 EMS • Term 3 • Cash Payments Journal',
        steps: [
            { key: 'cpj', title: 'CPJ' }
        ]
    },
    'grade8_ems_ownership': {
        topic: 'grade8_ems_ownership',
        title: 'Grade 8 EMS • Term 3 • Forms of Ownership',
        steps: [
            { key: 'concepts', title: 'Concepts' },
            { key: 'discussion', title: 'Discussion' }
        ]
    }
};

const Grade8EmsRoute = ({ workspaceMode, ctx }) => {
    const isScaffold = workspaceMode.endsWith('_scaffold');
    const isPractice = workspaceMode.endsWith('_practice');
    const isAssessment = workspaceMode.endsWith('_assessment');
    const baseMode = workspaceMode.replace('_scaffold', '').replace('_practice', '').replace('_assessment', '');
    
    const config = TOPIC_CONFIGS[baseMode];
    if (!config && !isAssessment) return null;

    const controller = useGrade8EmsController({ 
        workspaceMode, 
        buildApiUrl: ctx.buildApiUrl, 
        config: config || {} 
    });

    if (isScaffold) {
        return h(Grade8EmsScaffold, {
            onBack: ctx.onBack,
            scaffoldSteps: controller.scaffoldSteps,
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
            renderVisualAids: () => null,
            isMarkingEnv: false,
            topicTitle: config.title
        });
    }

    if (isPractice) {
        return h(Grade8EmsPractice, {
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
            buildApiUrl: ctx.buildApiUrl,
            grade: 8
        });
    }

    return null;
};

export const grade8EmsRegistry = {};

Object.keys(TOPIC_CONFIGS).forEach(baseMode => {
    grade8EmsRegistry[`${baseMode}_scaffold`] = { render: (ctx) => h(Grade8EmsRoute, { workspaceMode: `${baseMode}_scaffold`, ctx }) };
    grade8EmsRegistry[`${baseMode}_practice`] = { render: (ctx) => h(Grade8EmsRoute, { workspaceMode: `${baseMode}_practice`, ctx }) };
});
grade8EmsRegistry['grade8_ems_assessment'] = { render: (ctx) => h(Grade8EmsRoute, { workspaceMode: 'grade8_ems_assessment', ctx }) };
