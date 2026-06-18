import React, { useEffect, useState } from 'react';
import { AlertCircle, ArrowRight, CheckCircle2, FileText, Loader2, Target, Trophy, XCircle } from 'lucide-react';

export const Grade10BSConceptOfQualityPractice = ({
    practiceQuestions,
    practiceAnswers,
    setPracticeAnswers,
    practiceLoading,
    practiceError,
    practiceDifficulty,
    fetchPractice,
    practiceFeedback,
    markPracticeTest,
    markingStatus,
    currentQuestionIndex: externalCurrentQuestionIndex,
    setCurrentQuestionIndex: externalSetCurrentQuestionIndex,
    questionSlotEnabled,
}) => {
    const [internalCurrentQuestionIndex, setInternalCurrentQuestionIndex] = useState(0);
    const currentQuestionIndex = typeof externalCurrentQuestionIndex === 'number' ? externalCurrentQuestionIndex : internalCurrentQuestionIndex;
    const setCurrentQuestionIndex = typeof externalSetCurrentQuestionIndex === 'function' ? externalSetCurrentQuestionIndex : setInternalCurrentQuestionIndex;

    const isMarking = markingStatus === 'marking_active' || markingStatus === 'marking';
    const hasResults = practiceFeedback?.results;
    const isSubmitted = !!hasResults;

    useEffect(() => {
        if (!isSubmitted) {
            setCurrentQuestionIndex(0);
        }
    }, [isSubmitted, setCurrentQuestionIndex]);

    const handleAnswerChange = (qIndex, answer) => {
        if (isSubmitted || isMarking) return;
        const newAnswers = [...(practiceAnswers || [])];
        newAnswers[qIndex] = answer;
        setPracticeAnswers(newAnswers);
    };

    const totalScore = practiceFeedback?.total_score || 0;
    const maxScore = practiceFeedback?.max_score || 1;

    if (practiceLoading) {
        return (
            <div className="flex flex-col items-center justify-center min-h-[400px] text-slate-500">
                <Loader2 className="w-12 h-12 animate-spin mb-4 text-indigo-500" />
                <p className="text-lg">Generating practice assessment...</p>
            </div>
        );
    }

    if (practiceError) {
        return (
            <div className="flex flex-col items-center justify-center min-h-[400px] text-red-500">
                <AlertCircle className="w-12 h-12 mb-4" />
                <p className="text-lg mb-4 text-center">{practiceError}</p>
                <button
                    onClick={() => fetchPractice?.({ difficulty: practiceDifficulty })}
                    className="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-colors"
                >
                    Retry
                </button>
            </div>
        );
    }

    if (!practiceQuestions || practiceQuestions.length === 0) {
        return (
            <div className="flex flex-col items-center justify-center py-20 px-4 text-center">
                <FileText className="w-16 h-16 text-slate-300 mb-4" />
                <h3 className="text-lg font-medium text-slate-900 mb-2">Ready to Practice?</h3>
                <p className="text-slate-500 max-w-md">
                    Generate a practice set to test your knowledge of Concept of Quality.
                </p>
            </div>
        );
    }

    if (isSubmitted && currentQuestionIndex === -1) {
        const percentage = Math.round((totalScore / maxScore) * 100);

        return (
            <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in duration-500">
                <div className="border-none shadow-xl shadow-slate-200/50 bg-white/80 backdrop-blur-sm overflow-hidden rounded-2xl">
                    <div className="bg-gradient-to-r from-indigo-600 to-purple-600 p-12 text-center text-white">
                        <Trophy className="w-20 h-20 mx-auto mb-6 text-yellow-300 drop-shadow-lg" />
                        <h2 className="text-4xl font-bold mb-2">Practice Complete!</h2>
                        <p className="text-indigo-100 text-lg">Review each response against the expected quality concepts and explanations.</p>
                    </div>

                    <div className="p-8">
                        <div className="flex justify-center items-center gap-12 mb-12">
                            <div className="text-center">
                                <div className="text-sm font-medium text-slate-500 mb-1 uppercase tracking-wider">Total Score</div>
                                <div className="text-4xl font-bold text-slate-800">{totalScore} <span className="text-2xl text-slate-400">/ {maxScore}</span></div>
                            </div>
                            <div className="w-px h-16 bg-slate-200"></div>
                            <div className="text-center">
                                <div className="text-sm font-medium text-slate-500 mb-1 uppercase tracking-wider">Percentage</div>
                                <div className={`text-4xl font-bold ${percentage >= 80 ? 'text-emerald-500' : percentage >= 50 ? 'text-amber-500' : 'text-rose-500'}`}>
                                    {percentage}%
                                </div>
                            </div>
                        </div>

                        <div className="flex justify-center gap-4">
                            <button
                                onClick={() => setCurrentQuestionIndex(0)}
                                className="px-6 py-2.5 bg-indigo-100 text-indigo-700 font-medium rounded-lg hover:bg-indigo-200 transition-colors"
                            >
                                Review Answers
                            </button>
                            <button
                                onClick={() => fetchPractice?.({ difficulty: practiceDifficulty })}
                                className="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-colors"
                            >
                                Generate Another Set
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    const currentQuestion = practiceQuestions[currentQuestionIndex];
    const questionId = currentQuestion?.id;
    const currentAnswer = (practiceAnswers || [])[currentQuestionIndex];
    const feedback = hasResults ? practiceFeedback.results[questionId] : null;
    const isDiscussion = currentQuestion?.question_type === 'typed';

    return (
        <div className="max-w-4xl mx-auto space-y-6 animate-in fade-in duration-500">
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-2xl font-bold text-slate-800">Practice Assessment</h1>
                    <p className="text-slate-500">Topic: Concept of Quality</p>
                </div>

                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2 bg-white px-4 py-2 rounded-full shadow-sm border border-slate-200">
                        <Target className="w-4 h-4 text-indigo-500" />
                        <span className="font-medium text-slate-700">
                            Question {currentQuestionIndex + 1} of {practiceQuestions.length}
                        </span>
                    </div>
                </div>
            </div>

            <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
                <div className="p-4 sm:p-6 space-y-4">
                    {!questionSlotEnabled && (
                        <div className="flex justify-between items-start gap-4">
                            <div className="text-base font-medium text-slate-800 whitespace-pre-wrap">
                                {currentQuestion.prompt}
                            </div>
                            {currentQuestion.marks && (
                                <span className="text-sm font-medium text-slate-500 bg-white px-2 py-1 rounded border border-slate-200">
                                    {currentQuestion.marks} {currentQuestion.marks === 1 ? 'mark' : 'marks'}
                                </span>
                            )}
                        </div>
                    )}

                    {!isDiscussion && currentQuestion.options && (
                        <div className="space-y-2 mt-4">
                            {currentQuestion.options.map((opt, i) => {
                                const isSelected = currentAnswer === i;
                                const isCorrect = currentQuestion.correct_option_index === i;

                                let btnClass = 'w-full text-left p-3 rounded-lg border text-sm transition-colors ';
                                if (isSubmitted) {
                                    if (isCorrect) btnClass += 'bg-green-50 border-green-500 text-green-900';
                                    else if (isSelected) btnClass += 'bg-red-50 border-red-500 text-red-900';
                                    else btnClass += 'bg-white border-slate-200 text-slate-500 opacity-50';
                                } else {
                                    btnClass += isSelected ? 'bg-indigo-50 border-indigo-500 text-indigo-900' : 'bg-white border-slate-200 hover:border-indigo-300 text-slate-700 hover:bg-slate-50';
                                }

                                return (
                                    <button
                                        key={i}
                                        disabled={isSubmitted || isMarking}
                                        onClick={() => handleAnswerChange(currentQuestionIndex, i)}
                                        className={btnClass}
                                    >
                                        <div className="flex justify-between items-center">
                                            <span>{opt}</span>
                                            {isSubmitted && isCorrect && <CheckCircle2 className="w-4 h-4 text-green-600" />}
                                            {isSubmitted && isSelected && !isCorrect && <XCircle className="w-4 h-4 text-red-600" />}
                                        </div>
                                    </button>
                                );
                            })}
                        </div>
                    )}

                    {isDiscussion && (
                        <div className="mt-4">
                            <textarea
                                value={currentAnswer || ''}
                                onChange={(e) => handleAnswerChange(currentQuestionIndex, e.target.value)}
                                disabled={isSubmitted || isMarking}
                                placeholder="Type your discussion or explanation here..."
                                className="w-full min-h-[120px] p-3 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 disabled:bg-slate-50 disabled:text-slate-500"
                            />
                        </div>
                    )}

                    {feedback && (
                        <div className={`mt-4 p-4 rounded-lg border ${feedback.is_correct || feedback.score > 0 ? 'bg-green-50 border-green-200' : 'bg-orange-50 border-orange-200'}`}>
                            <div className="flex justify-between items-start mb-2">
                                <h4 className={`font-semibold ${feedback.is_correct || feedback.score > 0 ? 'text-green-800' : 'text-orange-800'}`}>
                                    {isDiscussion ? `Score: ${feedback.score}/${currentQuestion.marks}` : (feedback.is_correct ? 'Correct' : 'Incorrect')}
                                </h4>
                            </div>

                            {isDiscussion ? (
                                <div className="text-sm text-slate-700 space-y-2">
                                    <p>{feedback.feedback}</p>
                                    <div className="bg-white p-3 rounded border border-slate-200 mt-2">
                                        <span className="font-semibold text-xs text-slate-500 uppercase tracking-wider">Model Explanation:</span>
                                        <div className="prose prose-sm max-w-none mt-1 whitespace-pre-wrap">{currentQuestion.explanation}</div>
                                    </div>
                                </div>
                            ) : (
                                <div className="text-sm text-slate-700">
                                    <div className="prose prose-sm max-w-none whitespace-pre-wrap">{currentQuestion.explanation}</div>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>

            <div className="flex justify-between items-center pt-4">
                <button
                    onClick={() => {
                        if (isSubmitted && currentQuestionIndex === 0) {
                            setCurrentQuestionIndex(-1);
                        } else {
                            setCurrentQuestionIndex(Math.max(0, currentQuestionIndex - 1));
                        }
                    }}
                    disabled={currentQuestionIndex === 0 && !isSubmitted}
                    className="px-6 py-2.5 rounded-lg border border-slate-300 text-slate-700 hover:bg-slate-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                    Previous
                </button>

                {currentQuestionIndex < practiceQuestions.length - 1 ? (
                    <button
                        onClick={() => setCurrentQuestionIndex(currentQuestionIndex + 1)}
                        className="px-6 py-2.5 bg-slate-800 text-white font-medium rounded-lg hover:bg-slate-900 transition-colors flex items-center gap-2"
                    >
                        Next
                        <ArrowRight className="w-4 h-4" />
                    </button>
                ) : !isSubmitted ? (
                    <button
                        onClick={markPracticeTest}
                        disabled={isMarking}
                        className="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center gap-2"
                    >
                        {isMarking ? (
                            <>
                                <Loader2 className="w-4 h-4 animate-spin" />
                                Submitting...
                            </>
                        ) : (
                            <>
                                Finish and Review
                                <CheckCircle2 className="w-4 h-4" />
                            </>
                        )}
                    </button>
                ) : (
                    <button
                        onClick={() => setCurrentQuestionIndex(-1)}
                        className="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition-colors"
                    >
                        View Results
                    </button>
                )}
            </div>

            <div className="flex justify-center gap-2 mt-8">
                {practiceQuestions.map((q, idx) => (
                    <button
                        key={q.id || idx}
                        onClick={() => setCurrentQuestionIndex(idx)}
                        className={`w-2.5 h-2.5 rounded-full transition-all ${
                            idx === currentQuestionIndex
                                ? 'bg-indigo-600 scale-125'
                                : isSubmitted && practiceFeedback?.results?.[q.id]
                                    ? practiceFeedback.results[q.id].is_correct
                                        ? 'bg-emerald-400'
                                        : practiceFeedback.results[q.id].score > 0
                                            ? 'bg-amber-400'
                                            : 'bg-rose-400'
                                    : 'bg-slate-300 hover:bg-slate-400'
                        }`}
                    />
                ))}
            </div>
        </div>
    );
};
