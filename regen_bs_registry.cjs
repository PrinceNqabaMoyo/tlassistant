const fs = require('fs');
const path = require('path');

const term1Topics = [
    { dir: 'micro-environment', name: 'MicroEnvironment', key: 'micro_environment' },
    { dir: 'business-functions', name: 'BusinessFunctions', key: 'business_functions' },
    { dir: 'market-environment', name: 'MarketEnvironment', key: 'market_environment' },
    { dir: 'macro-environment', name: 'MacroEnvironment', key: 'macro_environment' },
    { dir: 'interrelationship', name: 'Interrelationship', key: 'interrelationship' },
    { dir: 'business-sectors', name: 'BusinessSectors', key: 'business_sectors' }
];

const term2Topics = [
    { dir: 'socio-economic-issues', name: 'SocioEconomicIssues', key: 'socio_economic_issues' },
    { dir: 'social-responsibility', name: 'SocialResponsibility', key: 'social_responsibility' },
    { dir: 'entrepreneurial-qualities', name: 'EntrepreneurialQualities', key: 'entrepreneurial_qualities' },
    { dir: 'forms-of-ownership', name: 'FormsOfOwnership', key: 'forms_of_ownership' },
    { dir: 'concept-of-quality', name: 'ConceptOfQuality', key: 'concept_of_quality' }
];

const allTopics = [...term1Topics.map(t => ({...t, term: 1})), ...term2Topics.map(t => ({...t, term: 2}))];

let imports = `import React from 'react';
import WorkspaceModeShell from '../shared/WorkspaceModeShell';
import EvaluatedWorkspaceModeShell from '../shared/EvaluatedWorkspaceModeShell';
import { useGrade10BusinessStudiesMarking } from '../grade10/business-studies/useGrade10BusinessStudiesMarking';
const h = React.createElement;

`;

let routes = '';
let exportsList = '';

allTopics.forEach(topic => {
    imports += `import { Grade10BS${topic.name}Scaffold } from '../grade10/business-studies/term-${topic.term}/${topic.dir}/Grade10BS${topic.name}Scaffold';\n`;
    imports += `import { Grade10BS${topic.name}Practice } from '../grade10/business-studies/term-${topic.term}/${topic.dir}/Grade10BS${topic.name}Practice';\n`;
    imports += `import { useGrade10BS${topic.name}Controller, Grade10BS${topic.name}VisualAids } from '../grade10/business-studies/term-${topic.term}/${topic.dir}';\n\n`;

    routes += `const Grade10BS${topic.name}Route = ({ workspaceMode, ctx }) => {
    const controller = useGrade10BS${topic.name}Controller({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
    const marking = useGrade10BusinessStudiesMarking({ buildApiUrl: ctx.buildApiUrl });

    const renderVisualAids = () => h(Grade10BS${topic.name}VisualAids, {
        visualAidsTab: controller.visualAidsTab,
        setVisualAidsTab: controller.setVisualAidsTab,
        setVisualAidsOpen: controller.setVisualAidsOpen,
    });

    const isScaffoldLikeMode = workspaceMode === 'grade10_bs_${topic.key}_scaffold';

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

    if (workspaceMode === 'grade10_bs_${topic.key}_scaffold') {
        const sq = controller.scaffoldQuestion;
        return h(EvaluatedWorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack,
            onNext: () => controller.fetchScaffoldQuestion({ subskill: controller.scaffoldSteps?.[controller.scaffoldStepIndex]?.key || 'concepts', difficulty: controller.scaffoldDifficulty }),
            renderVisualAids, questionSlot: sq ? h('div', { className: 'space-y-1' }, h('h2', { className: 'text-base sm:text-lg font-semibold text-slate-800 leading-relaxed' }, 'Concept Check')) : null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, question: sq, userAnswersCells: {},
            ...commonShellProps,
        }, h(Grade10BS${topic.name}Scaffold, {
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

    if (workspaceMode === 'grade10_bs_${topic.key}_practice') {
        return h(WorkspaceModeShell, {
            subscriptionTier: ctx.subscriptionTier,
            workspaceMode, setWorkspaceMode: ctx.setWorkspaceMode, onBack: ctx.onBack, renderVisualAids,
            questionSlot: null,
            selectedSubject: ctx.selectedSubject, selectedGrade: ctx.selectedGrade, topic: ctx.topic, ...commonShellProps,
        }, h(Grade10BS${topic.name}Practice, {
            practiceDifficulty: controller.practiceDifficulty, setPracticeDifficulty: controller.setPracticeDifficulty,
            fetchPractice: controller.fetchPractice, practiceLoading: controller.practiceLoading, practiceError: controller.practiceError,
            practiceQuestions: controller.practiceQuestions, practiceAnswers: controller.practiceAnswers, setPracticeAnswers: controller.setPracticeAnswers,
            practiceFeedback: controller.practiceFeedback, setPracticeFeedback: controller.setPracticeFeedback,
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

`;

    exportsList += `    grade10_bs_${topic.key}_scaffold: {
        render: (ctx) => h(Grade10BS${topic.name}Route, { workspaceMode: 'grade10_bs_${topic.key}_scaffold', ctx }),
    },
    grade10_bs_${topic.key}_practice: {
        render: (ctx) => h(Grade10BS${topic.name}Route, { workspaceMode: 'grade10_bs_${topic.key}_practice', ctx }),
    },\n`;
});

const finalContent = `${imports}
${routes}
export const grade10BusinessStudiesRegistry = {
${exportsList}};
`;

fs.writeFileSync(path.join(__dirname, 'src/components/workspace/registry/grade10BusinessStudiesRegistry.js'), finalContent);
console.log('Successfully regenerated grade10BusinessStudiesRegistry.js');
