import React from 'react';
import WorkspaceModeShell from '../WorkspaceModeShell';
import MathText from './MathText';
import MathAnswerArea from './MathAnswerArea';
import { createMathController } from './useMathController';

const h = React.createElement;

const renderMathPrompt = (question, prefix = '') => {
    if (!question) return null;
    return (
        <div className="space-y-3">
            {prefix ? <div className="text-sm text-slate-500">{prefix}</div> : null}
            {question.marks ? (
                <span className="inline-flex px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-semibold uppercase tracking-wide">
                    {question.marks} {question.marks === 1 ? 'mark' : 'marks'}
                </span>
            ) : null}
            <div className="text-lg text-slate-800 leading-relaxed">
                {question.prompt_latex
                    ? <MathText latex={question.prompt_latex} display />
                    : <span className="whitespace-pre-wrap">{question.prompt}</span>}
            </div>
        </div>
    );
};

/**
 * Builds scaffold + practice registry entries for a single Grade 10 Mathematics
 * topic. Mirrors ``createGrade10BSTopicRegistry`` but renders the maths surface
 * (KaTeX prompt + keypad + Working Pad) and marks via the SymPy backend.
 */
export const createMathTopicRegistry = ({ topicKey, modePrefix }) => {
    const scaffoldMode = `${modePrefix}_scaffold`;
    const practiceMode = `${modePrefix}_practice`;
    const useController = createMathController({ topicKey, scaffoldMode });

    const Route = ({ workspaceMode, ctx }) => {
        const c = useController({ workspaceMode, buildApiUrl: ctx.buildApiUrl });
        const isScaffold = workspaceMode === scaffoldMode;

        const answerArea = c.question
            ? h(MathAnswerArea, {
                question: c.question,
                topic: topicKey,
                onCheck: c.check,
                result: c.result,
                busy: c.marking,
            })
            : h('p', { className: 'text-sm text-slate-500' }, 'Generate a question to begin.');

        const shellProps = {
            workspaceMode,
            setWorkspaceMode: ctx.setWorkspaceMode,
            onBack: ctx.onBack,
            selectedSubject: ctx.selectedSubject,
            selectedGrade: ctx.selectedGrade,
            topic: ctx.topic,
            subscriptionTier: ctx.subscriptionTier,
            availableModes: ['scaffold', 'practice'],
            isGenerating: c.loading,
            generationError: c.error,
        };

        if (isScaffold) {
            const subskills = c.sections;
            const currentKey = subskills?.[c.scaffoldStepIndex]?.key || 'concepts';
            return h(WorkspaceModeShell, {
                ...shellProps,
                subskills,
                subskill: currentKey,
                setSubskill: (key) => {
                    const idx = subskills.findIndex((s) => s.key === key);
                    if (idx >= 0) c.setScaffoldStepIndex(idx);
                },
                difficulty: c.scaffoldDifficulty,
                setDifficulty: c.setScaffoldDifficulty,
                onGenerate: ({ difficulty, subskill }) => c.fetchScaffoldQuestion({ subskill, difficulty }),
                onNext: () => c.fetchScaffoldQuestion({ subskill: currentKey, difficulty: c.scaffoldDifficulty }),
                questionSlot: renderMathPrompt(c.question),
            }, answerArea);
        }

        // Practice
        const total = c.practiceQuestions.length;
        const prefix = total > 0 ? `Question ${c.practiceIndex + 1} of ${total}` : '';
        const nav = total > 0
            ? h('div', { className: 'flex justify-between pt-2' }, [
                h('button', {
                    key: 'prev',
                    onClick: () => c.gotoPractice(c.practiceIndex - 1),
                    disabled: c.practiceIndex === 0,
                    className: 'px-4 py-2 rounded-lg border border-slate-200 text-sm text-slate-700 disabled:opacity-40',
                }, 'Previous'),
                h('button', {
                    key: 'next',
                    onClick: () => c.gotoPractice(c.practiceIndex + 1),
                    disabled: c.practiceIndex >= total - 1,
                    className: 'px-4 py-2 rounded-lg border border-slate-200 text-sm text-slate-700 disabled:opacity-40',
                }, 'Next'),
            ])
            : null;

        return h(WorkspaceModeShell, {
            ...shellProps,
            disableSubskillControl: true,
            subskill: 'mixed',
            difficulty: c.practiceDifficulty,
            setDifficulty: c.setPracticeDifficulty,
            onGenerate: ({ difficulty }) => c.fetchPractice({ difficulty }),
            questionSlot: renderMathPrompt(c.question, prefix),
        }, h('div', { className: 'space-y-4' }, [
            h('div', { key: 'area' }, answerArea),
            nav,
        ]));
    };

    return {
        [scaffoldMode]: { render: (ctx) => h(Route, { workspaceMode: scaffoldMode, ctx }) },
        [practiceMode]: { render: (ctx) => h(Route, { workspaceMode: practiceMode, ctx }) },
    };
};
