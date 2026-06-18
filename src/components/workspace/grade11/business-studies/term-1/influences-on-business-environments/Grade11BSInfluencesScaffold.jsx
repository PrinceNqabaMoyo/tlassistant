import React, { useEffect } from 'react';
import { Card, CardContent } from '../../../../grade10/ui/card';
import { Button } from '../../../../grade10/ui/button';
import {
    AlertCircle,
    ArrowRight,
    BookOpen,
    CheckCircle2,
    LightbulbIcon,
    Loader2,
    XCircle,
} from 'lucide-react';

const MemoCard = ({ question }) => {
    const correctOption = question?.question_type === 'mcq' && Array.isArray(question?.options)
        ? question.options[Number(question.correct_index)]
        : null;

    return (
        <div className="rounded-2xl border border-indigo-200 bg-indigo-50 p-5 space-y-4">
            <div>
                <p className="text-sm font-semibold text-indigo-900">Memo comparison</p>
                <p className="text-sm text-indigo-800">Use this memo to compare the structure and content of your answer.</p>
            </div>

            {correctOption && (
                <div className="space-y-1">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Correct answer</p>
                    <p className="text-sm text-slate-700">{correctOption}</p>
                </div>
            )}

            {Array.isArray(question?.guidelines) && question.guidelines.length > 0 && (
                <div className="space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Guidelines</p>
                    <ul className="space-y-2 text-sm text-slate-700">
                        {question.guidelines.map((item, index) => (
                            <li key={`${question.id}-guide-${index}`} className="rounded-xl bg-white/80 px-3 py-2 border border-indigo-100">
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            )}

            {Array.isArray(question?.marking_points) && question.marking_points.length > 0 && (
                <div className="space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Marking points</p>
                    <ul className="space-y-2 text-sm text-slate-700">
                        {question.marking_points.map((item, index) => (
                            <li key={`${question.id}-mark-${index}`} className="rounded-xl bg-white/80 px-3 py-2 border border-indigo-100">
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            )}

            {Array.isArray(question?.answer_part_hints) && question.answer_part_hints.length > 0 && (
                <div className="space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Answer structure</p>
                    <ul className="space-y-2 text-sm text-slate-700">
                        {question.answer_part_hints.map((item, index) => (
                            <li key={`${question.id}-part-${index}`} className="rounded-xl bg-white/80 px-3 py-2 border border-indigo-100">
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            )}

            {question?.sample_answer && (
                <div className="space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Sample answer</p>
                    <div className="rounded-xl bg-white/80 px-4 py-3 border border-indigo-100 text-sm text-slate-700 whitespace-pre-wrap">
                        {question.sample_answer}
                    </div>
                </div>
            )}

            {question?.teaching_note && (
                <div className="rounded-xl border border-indigo-100 bg-white/80 px-4 py-3 text-sm text-slate-700">
                    {question.teaching_note}
                </div>
            )}
        </div>
    );
};


const getNextRetryVariant = (question) => {
    const currentVariant = question?.retry_variant || 'core';
    const subskill = question?.subskill;

    if (subskill === 'application') {
        if (currentVariant === 'core') return 'guided';
        if (currentVariant === 'guided') return 'reworded';
        return 'transfer';
    }

    if (currentVariant === 'core') return 'guided';
    if (currentVariant === 'guided') return 'reworded';
    return 'reworded';
};


const buildRetryConfig = (question) => ({
    learning_objective_id: question?.learning_objective_id,
    concept_id: question?.concept_id,
    concept_group: question?.concept_group,
    question_family_id: question?.question_family_id,
    scenario_family_id: question?.scenario_family_id,
    retry_variant: getNextRetryVariant(question),
});


export const Grade11BSInfluencesScaffold = ({
    scaffoldSteps,
    scaffoldStepIndex,
    setScaffoldStepIndex,
    scaffoldQuestion,
    scaffoldAnswer,
    setScaffoldAnswer,
    scaffoldFeedback,
    setScaffoldFeedback,
    scaffoldHintLevel,
    setScaffoldHintLevel,
    scaffoldShowMemo,
    setScaffoldShowMemo,
    scaffoldLoading,
    scaffoldError,
    scaffoldDifficulty,
    scaffoldMasteryProgress,
    scaffoldTopicCompleted,
    scaffoldMasteryRequirements,
    isScaffoldStepMastered,
    hasCompletedAllScaffoldSteps,
    resetScaffoldSession,
    completeScaffoldTopic,
    fetchScaffoldQuestion,
    questionSlotEnabled,
    markScaffoldAnswer,
}) => {
    const currentStep = scaffoldSteps[scaffoldStepIndex];
    const currentStepKey = currentStep?.key || 'concepts';
    const hintSections = scaffoldQuestion?.hint_sections || [];
    const visibleHints = hintSections.slice(0, scaffoldHintLevel);
    const hasMastered = scaffoldFeedback?.is_mastered ?? scaffoldFeedback?.is_correct ?? false;
    const canCompareMemo = Boolean(scaffoldFeedback);
    const currentStepProgress = scaffoldMasteryProgress?.[currentStepKey] || {
        successCount: 0,
        familyIds: [],
        evidenceKeys: [],
    };
    const currentStepIsMastered = typeof isScaffoldStepMastered === 'function'
        ? isScaffoldStepMastered(currentStepKey)
        : false;
    const requiredSuccessCount = scaffoldMasteryRequirements?.requiredSuccessCount || 2;
    const requiredDistinctEvidence = scaffoldMasteryRequirements?.requiredDistinctEvidence || 2;
    const requiredDistinctFamilies = scaffoldMasteryRequirements?.requiredDistinctFamilies?.[currentStepKey]
        || (currentStepKey === 'discussion' ? 1 : 2);

    useEffect(() => {
        if (scaffoldTopicCompleted) {
            return;
        }

        fetchScaffoldQuestion({
            subskill: currentStepKey,
            difficulty: scaffoldDifficulty,
        });
        setScaffoldAnswer('');
        setScaffoldFeedback(null);
    }, [currentStep, currentStepKey, scaffoldDifficulty, scaffoldTopicCompleted]);

    const submitAnswer = async () => {
        if (scaffoldQuestion?.question_type !== 'mcq' && !String(scaffoldAnswer || '').trim()) {
            return;
        }
        await markScaffoldAnswer(scaffoldQuestion, scaffoldAnswer);
    };

    const nextPrompt = () => {
        if (hasMastered && hasCompletedAllScaffoldSteps) {
            completeScaffoldTopic();
            return;
        }

        if (hasMastered && currentStepIsMastered && scaffoldStepIndex < scaffoldSteps.length - 1) {
            setScaffoldStepIndex((current) => current + 1);
            return;
        }

        if (hasMastered && currentStepIsMastered) {
            completeScaffoldTopic();
            return;
        }

        const retryConfig = !hasMastered && scaffoldQuestion
            ? buildRetryConfig(scaffoldQuestion)
            : undefined;

        fetchScaffoldQuestion({
            subskill: currentStepKey,
            difficulty: scaffoldDifficulty,
            config: retryConfig,
            avoidQuestionFamilyIds: hasMastered ? currentStepProgress.familyIds : undefined,
            avoidEvidenceKeys: hasMastered ? currentStepProgress.evidenceKeys : undefined,
        });
    };

    return (
        <div className="max-w-4xl mx-auto space-y-6 animate-in fade-in duration-500">
            <div className="flex justify-between mb-8 overflow-x-auto pb-4 custom-scrollbar">
                {scaffoldSteps.map((step, index) => (
                    <button
                        key={step.key}
                        type="button"
                        disabled
                        className={`flex flex-col items-center flex-1 min-w-[130px] transition-all duration-300 relative ${
                            scaffoldTopicCompleted || index <= scaffoldStepIndex ? 'opacity-100' : 'opacity-50'
                        }`}
                    >
                        <div className={`w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold border-2 z-10 bg-white ${
                            scaffoldTopicCompleted || index < scaffoldStepIndex
                                ? 'border-emerald-500 text-emerald-500 bg-emerald-50'
                                : index === scaffoldStepIndex
                                    ? 'border-indigo-600 text-indigo-600 shadow-lg shadow-indigo-200'
                                    : 'border-slate-300 text-slate-400'
                        }`}>
                            {scaffoldTopicCompleted || index < scaffoldStepIndex ? <CheckCircle2 className="w-6 h-6" /> : index + 1}
                        </div>
                        <span className={`text-xs mt-2 font-medium text-center px-2 ${
                            !scaffoldTopicCompleted && index === scaffoldStepIndex ? 'text-indigo-700' : 'text-slate-500'
                        }`}>
                            {step.title}
                        </span>
                        {index < scaffoldSteps.length - 1 && (
                            <div className={`absolute top-5 left-1/2 w-full h-[2px] -z-10 ${
                                scaffoldTopicCompleted || index < scaffoldStepIndex ? 'bg-emerald-500' : 'bg-slate-200'
                            }`} />
                        )}
                    </button>
                ))}
            </div>

            <Card className="border-none shadow-xl shadow-slate-200/50 overflow-hidden bg-white/80 backdrop-blur-sm">
                <CardContent className="p-8 space-y-6">
                    {scaffoldLoading && (
                        <div className="flex flex-col items-center justify-center py-12 text-slate-500">
                            <Loader2 className="w-8 h-8 animate-spin mb-4 text-indigo-500" />
                            <p>Generating a Grade 11 Business Studies scenario...</p>
                        </div>
                    )}

                    {!scaffoldLoading && scaffoldError && (
                        <div className="flex flex-col items-center justify-center py-8 text-red-500">
                            <AlertCircle className="w-8 h-8 mb-4" />
                            <p>{scaffoldError}</p>
                            <Button
                                onClick={() => fetchScaffoldQuestion({ subskill: currentStep?.key || 'concepts', difficulty: scaffoldDifficulty })}
                                className="mt-4 bg-indigo-600 hover:bg-indigo-700 text-white"
                            >
                                Retry
                            </Button>
                        </div>
                    )}

                    {!scaffoldLoading && !scaffoldError && scaffoldTopicCompleted && (
                        <div className="p-8 rounded-2xl border-2 border-emerald-200 bg-emerald-50 space-y-6">
                            <div className="flex items-start gap-4">
                                <CheckCircle2 className="w-7 h-7 text-emerald-600 mt-1" />
                                <div className="space-y-2">
                                    <h3 className="text-2xl font-semibold text-emerald-900">Topic mastered for now</h3>
                                    <p className="text-sm text-emerald-700">
                                        You completed the repeated-proof scaffold across concepts, scenario analysis, and discussion.
                                    </p>
                                </div>
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                                {scaffoldSteps.map((step) => {
                                    const stepProgress = scaffoldMasteryProgress?.[step.key] || { successCount: 0, familyIds: [], evidenceKeys: [] };
                                    const stepFamiliesRequired = scaffoldMasteryRequirements?.requiredDistinctFamilies?.[step.key]
                                        || (step.key === 'discussion' ? 1 : 2);

                                    return (
                                        <div key={step.key} className="rounded-xl border border-emerald-200 bg-white/80 px-4 py-3 space-y-1">
                                            <p className="text-xs font-semibold uppercase tracking-wide text-emerald-700">{step.title}</p>
                                            <p className="text-sm text-slate-700">Successful proofs: {stepProgress.successCount} / {requiredSuccessCount}</p>
                                            <p className="text-sm text-slate-700">Distinct evidence: {stepProgress.evidenceKeys.length} / {requiredDistinctEvidence}</p>
                                            <p className="text-sm text-slate-700">Distinct families: {stepProgress.familyIds.length} / {stepFamiliesRequired}</p>
                                        </div>
                                    );
                                })}
                            </div>

                            <div className="flex justify-end">
                                <Button
                                    onClick={resetScaffoldSession}
                                    className="bg-slate-800 hover:bg-slate-900 text-white"
                                >
                                    Start Over
                                    <ArrowRight className="w-4 h-4 ml-2" />
                                </Button>
                            </div>
                        </div>
                    )}

                    {!scaffoldLoading && !scaffoldError && scaffoldQuestion && (
                        <div className="space-y-6">
                            <div className="flex flex-wrap items-center gap-3">
                                <span className="px-3 py-1 rounded-full bg-indigo-100 text-indigo-700 text-xs font-semibold uppercase tracking-wide">
                                    {currentStep?.title}
                                </span>
                                {!questionSlotEnabled && scaffoldQuestion.marks && (
                                    <span className="px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-xs font-semibold uppercase tracking-wide">
                                        {scaffoldQuestion.marks} marks
                                    </span>
                                )}
                            </div>

                            {scaffoldQuestion.question_type === 'mcq' && (
                                <div className="space-y-3">
                                    {scaffoldQuestion.options.map((option, index) => (
                                        <button
                                            key={`${scaffoldQuestion.id}-${index}`}
                                            onClick={() => setScaffoldAnswer(String(index))}
                                            className={`w-full text-left p-4 rounded-xl border-2 transition-all duration-200 ${
                                                scaffoldAnswer === String(index)
                                                    ? 'border-indigo-500 bg-indigo-50 text-indigo-800'
                                                    : 'border-slate-200 hover:border-indigo-200 hover:bg-slate-50 text-slate-700'
                                            }`}
                                        >
                                            <span className="font-medium mr-3">{String.fromCharCode(65 + index)}.</span>
                                            {option}
                                        </button>
                                    ))}
                                </div>
                            )}

                            {scaffoldQuestion.question_type === 'typed' && (
                                <div className="space-y-3">
                                    <textarea
                                        className="w-full p-4 border-2 border-slate-200 rounded-xl focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20 transition-all duration-200 text-slate-700 min-h-[170px]"
                                        placeholder="Type your answer here..."
                                        value={scaffoldAnswer || ''}
                                        onChange={(event) => setScaffoldAnswer(event.target.value)}
                                    />
                                    <div className="flex justify-between items-center text-xs text-slate-500">
                                        <span>Build your answer point by point.</span>
                                        <span>{scaffoldQuestion.marks} marks</span>
                                    </div>
                                </div>
                            )}

                            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
                                <Button
                                    onClick={() => setScaffoldHintLevel((current) => Math.min(hintSections.length, current + 1))}
                                    variant="outline"
                                    disabled={hintSections.length === 0 || scaffoldHintLevel >= hintSections.length}
                                    className="border-amber-200 text-amber-700 hover:bg-amber-50"
                                >
                                    <LightbulbIcon className="w-4 h-4 mr-2" />
                                    {hintSections.length === 0
                                        ? 'No hints for this item'
                                        : scaffoldHintLevel >= hintSections.length
                                            ? 'All hints revealed'
                                            : scaffoldHintLevel === 0
                                                ? 'Reveal Hint'
                                                : 'Reveal Next Hint'}
                                </Button>

                                <Button
                                    onClick={() => setScaffoldShowMemo((current) => !current)}
                                    variant="outline"
                                    disabled={!canCompareMemo}
                                    className="border-indigo-200 text-indigo-700 hover:bg-indigo-50"
                                >
                                    <BookOpen className="w-4 h-4 mr-2" />
                                    {scaffoldShowMemo ? 'Hide Memo' : 'Compare to Memo'}
                                </Button>

                                <Button
                                    onClick={submitAnswer}
                                    disabled={scaffoldQuestion.question_type !== 'mcq' && !String(scaffoldAnswer || '').trim()}
                                    className="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white shadow-md shadow-indigo-500/20"
                                >
                                    Check Answer
                                    <ArrowRight className="w-4 h-4 ml-2" />
                                </Button>
                            </div>

                            {visibleHints.length > 0 && (
                                <div className="space-y-3">
                                    {visibleHints.map((hint, index) => (
                                        <div key={`${scaffoldQuestion.id}-hint-${index}`} className="p-4 bg-amber-50 border border-amber-200 rounded-xl text-amber-800">
                                            <p className="font-medium flex items-center gap-2 mb-1">
                                                <LightbulbIcon className="w-4 h-4" />
                                                {hint.title}
                                            </p>
                                            <p className="text-sm">{hint.text}</p>
                                        </div>
                                    ))}
                                </div>
                            )}

                            {canCompareMemo && scaffoldShowMemo && <MemoCard question={scaffoldQuestion} />}

                            {scaffoldFeedback && (
                                <div className={`p-6 rounded-xl border-2 ${
                                    hasMastered
                                        ? 'bg-emerald-50 border-emerald-200'
                                        : scaffoldFeedback.score > 0
                                            ? 'bg-amber-50 border-amber-200'
                                            : 'bg-rose-50 border-rose-200'
                                }`}>
                                    <div className="flex items-start gap-4">
                                        {hasMastered ? (
                                            <CheckCircle2 className="w-6 h-6 text-emerald-500 mt-1" />
                                        ) : scaffoldFeedback.score > 0 ? (
                                            <AlertCircle className="w-6 h-6 text-amber-500 mt-1" />
                                        ) : (
                                            <XCircle className="w-6 h-6 text-rose-500 mt-1" />
                                        )}
                                        <div className="space-y-2">
                                            <h3 className={`font-semibold text-lg ${
                                                hasMastered
                                                    ? 'text-emerald-800'
                                                    : scaffoldFeedback.score > 0
                                                        ? 'text-amber-800'
                                                        : 'text-rose-800'
                                            }`}>
                                                Score: {scaffoldFeedback.score} / {scaffoldFeedback.max_score}
                                            </h3>
                                            <p className={`text-sm ${
                                                hasMastered
                                                    ? 'text-emerald-600'
                                                    : scaffoldFeedback.score > 0
                                                        ? 'text-amber-600'
                                                        : 'text-rose-600'
                                            }`}>
                                                {scaffoldFeedback.feedback}
                                            </p>
                                            {typeof scaffoldFeedback.mastery_threshold === 'number' && (
                                                <p className="text-xs text-slate-500">
                                                    Mastery target: {Math.round(scaffoldFeedback.mastery_threshold * 100)}%
                                                </p>
                                            )}
                                            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 pt-2 text-xs text-slate-600">
                                                <div className="rounded-lg bg-white/70 px-3 py-2 border border-slate-200">
                                                    Successful proofs: {currentStepProgress.successCount} / {requiredSuccessCount}
                                                </div>
                                                <div className="rounded-lg bg-white/70 px-3 py-2 border border-slate-200">
                                                    Distinct evidence: {currentStepProgress.evidenceKeys.length} / {requiredDistinctEvidence}
                                                </div>
                                                <div className="rounded-lg bg-white/70 px-3 py-2 border border-slate-200">
                                                    Distinct families: {currentStepProgress.familyIds.length} / {requiredDistinctFamilies}
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div className="mt-6 flex justify-end">
                                        <Button
                                            onClick={nextPrompt}
                                            className="bg-slate-800 hover:bg-slate-900 text-white"
                                        >
                                            {hasMastered && currentStepIsMastered && scaffoldStepIndex < scaffoldSteps.length - 1
                                                ? 'Move to Next Step'
                                                : hasMastered && currentStepIsMastered
                                                    ? 'Complete Topic'
                                                    : hasMastered
                                                        ? 'Confirm Mastery'
                                                : 'Try Another Question'}
                                            <ArrowRight className="w-4 h-4 ml-2" />
                                        </Button>
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                </CardContent>
            </Card>
        </div>
    );
};
