import React from 'react';
import { AlertCircle, Target, CheckCircle2, ChevronRight, XCircle, ArrowRight } from 'lucide-react';

export const Grade10BSConceptOfQualityScaffold = ({
    onBack,
    scaffoldSteps,
    scaffoldStepIndex,
    setScaffoldStepIndex,
    fetchScaffoldQuestion,
    scaffoldLoading,
    scaffoldQuestion,
    scaffoldAnswer,
    setScaffoldAnswer,
    scaffoldFeedback,
    markScaffoldAnswer,
}) => {
    const isDiscussion = scaffoldQuestion?.question_type === 'typed';

    const renderMCQOptions = () => {
        if (!scaffoldQuestion?.options) return null;
        
        return (
            <div className="space-y-2 mt-4">
                {scaffoldQuestion.options.map((opt, i) => {
                    const isSelected = scaffoldAnswer === i;
                    const isSubmitted = scaffoldFeedback !== null;
                    const isCorrect = scaffoldQuestion.correct_option_index === i;
                    
                    let btnClass = "w-full text-left p-3 rounded-lg border text-sm transition-colors ";
                    if (isSubmitted) {
                        if (isCorrect) btnClass += "bg-green-50 border-green-500 text-green-900";
                        else if (isSelected) btnClass += "bg-red-50 border-red-500 text-red-900";
                        else btnClass += "bg-white border-slate-200 text-slate-500 opacity-50";
                    } else {
                        btnClass += isSelected ? "bg-indigo-50 border-indigo-500 text-indigo-900" : "bg-white border-slate-200 hover:border-indigo-300 text-slate-700 hover:bg-slate-50";
                    }

                    return (
                        <button
                            key={i}
                            disabled={isSubmitted}
                            onClick={() => setScaffoldAnswer(i)}
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
        );
    };

    const renderDiscussionInput = () => {
        return (
            <div className="mt-4">
                <textarea
                    value={scaffoldAnswer || ''}
                    onChange={(e) => setScaffoldAnswer(e.target.value)}
                    disabled={scaffoldFeedback !== null}
                    placeholder="Type your discussion or explanation here..."
                    className="w-full min-h-[120px] p-3 rounded-lg border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 disabled:bg-slate-50 disabled:text-slate-500"
                />
            </div>
        );
    };

    return (
        <div className="max-w-4xl mx-auto space-y-6">
            <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
                <div className="p-4 sm:p-6 bg-slate-50 border-b border-slate-200">
                    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <div className="flex items-center gap-3 text-slate-800">
                            <Target className="w-6 h-6 text-indigo-600" />
                            <h1 className="text-xl font-bold">Concept of Quality</h1>
                        </div>
                    </div>
                    
                    <div className="flex flex-wrap gap-2 mt-4">
                        {scaffoldSteps.map((step, idx) => (
                            <button
                                key={step.key}
                                onClick={() => setScaffoldStepIndex(idx)}
                                className={`px-3 py-1.5 text-xs font-medium rounded-full transition-colors ${
                                    scaffoldStepIndex === idx
                                        ? 'bg-indigo-100 text-indigo-800 border border-indigo-200'
                                        : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50'
                                }`}
                            >
                                {step.title}
                            </button>
                        ))}
                    </div>
                </div>

                <div className="p-4 sm:p-6">
                    {scaffoldLoading ? (
                        <div className="flex flex-col items-center justify-center py-12">
                            <div className="w-8 h-8 border-4 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></div>
                            <p className="mt-4 text-slate-500">Generating question...</p>
                        </div>
                    ) : scaffoldQuestion ? (
                        <div className="space-y-6">
                            <div className="bg-white">
                                {isDiscussion ? renderDiscussionInput() : renderMCQOptions()}
                            </div>

                            {scaffoldFeedback && (
                                <div className={`p-4 rounded-lg border ${scaffoldFeedback.is_correct || scaffoldFeedback.score > 0 ? 'bg-green-50 border-green-200' : 'bg-orange-50 border-orange-200'}`}>
                                    <div className="flex gap-3">
                                        {scaffoldFeedback.is_correct || scaffoldFeedback.score > 0 ? (
                                            <CheckCircle2 className="w-5 h-5 text-green-600 flex-shrink-0" />
                                        ) : (
                                            <AlertCircle className="w-5 h-5 text-orange-600 flex-shrink-0" />
                                        )}
                                        <div className="space-y-2">
                                            <h4 className={`font-medium ${scaffoldFeedback.is_correct || scaffoldFeedback.score > 0 ? 'text-green-800' : 'text-orange-800'}`}>
                                                {scaffoldFeedback.is_correct || scaffoldFeedback.score > 0 ? 'Good work!' : 'Needs Review'}
                                                {isDiscussion && ` (Score: ${scaffoldFeedback.score}/${scaffoldQuestion.marks})`}
                                            </h4>
                                            
                                            {isDiscussion ? (
                                                <div className="text-sm text-slate-700 space-y-2">
                                                    <p>{scaffoldFeedback.feedback}</p>
                                                    <div className="bg-white p-3 rounded border border-slate-200 mt-2">
                                                        <span className="font-semibold text-xs text-slate-500 uppercase tracking-wider">Model Explanation:</span>
                                                        <div className="prose prose-sm max-w-none mt-1 whitespace-pre-wrap">{scaffoldQuestion.explanation}</div>
                                                    </div>
                                                </div>
                                            ) : (
                                                <div className="text-sm text-slate-700">
                                                    <div className="prose prose-sm max-w-none whitespace-pre-wrap">{scaffoldQuestion.explanation}</div>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            )}

                            <div className="flex justify-end gap-3 pt-4 border-t border-slate-100">
                                {!scaffoldFeedback ? (
                                    <button
                                        onClick={() => markScaffoldAnswer(scaffoldQuestion, scaffoldAnswer)}
                                        disabled={scaffoldAnswer === null || (typeof scaffoldAnswer === 'string' && scaffoldAnswer.trim() === '')}
                                        className="px-6 py-2.5 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                                    >
                                        Check Answer
                                    </button>
                                ) : (
                                    <button
                                        onClick={() => fetchScaffoldQuestion({ subskill: scaffoldSteps[scaffoldStepIndex].key })}
                                        className="px-6 py-2.5 bg-slate-800 text-white font-medium rounded-lg hover:bg-slate-900 transition-colors flex items-center gap-2"
                                    >
                                        Next Question
                                        <ArrowRight className="w-4 h-4" />
                                    </button>
                                )}
                            </div>
                        </div>
                    ) : (
                        <div className="text-center py-12 text-slate-500">
                            Select a subskill above to start learning.
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};
