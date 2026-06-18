import React, { useEffect, useState } from 'react';
import { Card, CardContent } from '../../../ui/card';
import { Button } from '../../../ui/button';
import { 
    CheckCircle2, 
    XCircle, 
    AlertCircle, 
    ArrowRight,
    Loader2,
    Trophy,
    Target
} from 'lucide-react';

export const Grade10BSSocialResponsibilityPractice = ({
    practiceQuestions,
    practiceAnswers,
    setPracticeAnswers,
    practiceFeedback,
    setPracticeFeedback,
    practiceLoading,
    practiceError,
    practiceDifficulty,
    setPracticeDifficulty,
    fetchPractice,
    markPracticeTest,
    markingStatus,
    currentQuestionIndex: externalCurrentQuestionIndex,
    setCurrentQuestionIndex: externalSetCurrentQuestionIndex,
    questionSlotEnabled,
}) => {
    const [internalCurrentQuestionIndex, setInternalCurrentQuestionIndex] = useState(0);
    const currentQuestionIndex = typeof externalCurrentQuestionIndex === 'number' ? externalCurrentQuestionIndex : internalCurrentQuestionIndex;
    const setCurrentQuestionIndex = typeof externalSetCurrentQuestionIndex === 'function' ? externalSetCurrentQuestionIndex : setInternalCurrentQuestionIndex;

    const isMarking = markingStatus === 'marking_active';
    const isSubmitted = markingStatus === 'marking_submitted';

    useEffect(() => {
        if (!isSubmitted) {
            setCurrentQuestionIndex(0);
        }
    }, [isSubmitted]);

    const handleAnswerChange = (qId, val) => {
        if (isSubmitted || isMarking) return;
        setPracticeAnswers(prev => ({
            ...prev,
            [qId]: val
        }));
    };

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
                <p className="text-lg mb-4">{practiceError}</p>
                <Button 
                    onClick={() => fetchPractice({ difficulty: practiceDifficulty })}
                    className="bg-indigo-600 hover:bg-indigo-700 text-white"
                >
                    Retry
                </Button>
            </div>
        );
    }

    if (!practiceQuestions || practiceQuestions.length === 0) {
        return null;
    }

    // Results summary view when submitted
    if (isSubmitted && practiceFeedback?.results && currentQuestionIndex === -1) {
        const totalScore = practiceFeedback.total_score || 0;
        const maxScore = practiceFeedback.max_score || 1;
        const percentage = Math.round((totalScore / maxScore) * 100);

        return (
            <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in duration-500">
                <Card className="border-none shadow-xl shadow-slate-200/50 bg-white/80 backdrop-blur-sm overflow-hidden">
                    <div className="bg-gradient-to-r from-indigo-600 to-purple-600 p-12 text-center text-white">
                        <Trophy className="w-20 h-20 mx-auto mb-6 text-yellow-300 drop-shadow-lg" />
                        <h2 className="text-4xl font-bold mb-2">Assessment Complete!</h2>
                        <p className="text-indigo-100 text-lg">Here's how you did on Social Responsibility.</p>
                    </div>
                    
                    <CardContent className="p-8">
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
                            <Button 
                                onClick={() => setCurrentQuestionIndex(0)}
                                className="bg-indigo-100 hover:bg-indigo-200 text-indigo-700"
                            >
                                Review Answers
                            </Button>
                            <Button 
                                onClick={() => fetchPractice({ difficulty: practiceDifficulty })}
                                className="bg-indigo-600 hover:bg-indigo-700 text-white"
                            >
                                Try Another Assessment
                            </Button>
                        </div>
                    </CardContent>
                </Card>
            </div>
        );
    }

    const currentQuestion = practiceQuestions[currentQuestionIndex];
    const qId = currentQuestion?.id;
    const currentAnswer = practiceAnswers[qId] || '';
    const fb = practiceFeedback?.results?.[qId];

    return (
        <div className="max-w-4xl mx-auto space-y-6 animate-in fade-in duration-500">
            {/* Header & Progress */}
            <div className="flex items-center justify-between mb-8">
                <div>
                    <h1 className="text-2xl font-bold text-slate-800">Practice Assessment</h1>
                    <p className="text-slate-500">Topic: Social Responsibility</p>
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

            {/* Main Question Card */}
            <Card className="border-none shadow-xl shadow-slate-200/50 bg-white/80 backdrop-blur-sm overflow-hidden">
                <CardContent className="p-8">
                    <div className="space-y-6">
                        {!questionSlotEnabled && (
                            <div className="flex justify-between items-start">
                                <div className="prose max-w-none text-slate-700">
                                    <div className="whitespace-pre-wrap">{currentQuestion.prompt}</div>
                                </div>
                                {currentQuestion.marks && (
                                    <div className="ml-4 flex-shrink-0 bg-slate-100 px-3 py-1 rounded-md text-sm font-medium text-slate-600">
                                        [{currentQuestion.marks} marks]
                                    </div>
                                )}
                            </div>
                        )}

                        {/* Question Types */}
                        {currentQuestion.question_type === 'mcq' && (
                            <div className="space-y-3 pt-4">
                                {currentQuestion.options.map((opt, idx) => (
                                    <button
                                        key={idx}
                                        disabled={isSubmitted || isMarking}
                                        onClick={() => handleAnswerChange(qId, String(idx))}
                                        className={`w-full text-left p-4 rounded-xl border-2 transition-all duration-200 disabled:cursor-default ${
                                            currentAnswer === String(idx)
                                                ? 'border-indigo-500 bg-indigo-50 text-indigo-800'
                                                : 'border-slate-200 hover:border-indigo-200 hover:bg-slate-50 text-slate-700'
                                        }`}
                                    >
                                        <span className="font-medium mr-3">{String.fromCharCode(65 + idx)}.</span>
                                        {opt}
                                    </button>
                                ))}
                            </div>
                        )}

                        {currentQuestion.question_type === 'typed' && (
                            <div className="space-y-3 pt-4">
                                <textarea
                                    disabled={isSubmitted || isMarking}
                                    className="w-full p-4 border-2 border-slate-200 rounded-xl focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20 transition-all duration-200 text-slate-700 min-h-[150px] disabled:bg-slate-50 disabled:text-slate-500"
                                    placeholder="Type your discussion or essay answer here..."
                                    value={currentAnswer}
                                    onChange={(e) => handleAnswerChange(qId, e.target.value)}
                                />
                            </div>
                        )}

                        {/* Feedback Display */}
                        {isSubmitted && fb && (
                            <div className={`mt-6 p-6 rounded-xl border-2 animate-in fade-in slide-in-from-top-4 ${
                                fb.is_correct 
                                    ? 'bg-emerald-50 border-emerald-200' 
                                    : fb.score > 0 
                                        ? 'bg-amber-50 border-amber-200'
                                        : 'bg-rose-50 border-rose-200'
                            }`}>
                                <div className="flex items-start gap-4">
                                    {fb.is_correct ? (
                                        <CheckCircle2 className="w-6 h-6 text-emerald-500 mt-1" />
                                    ) : fb.score > 0 ? (
                                        <AlertCircle className="w-6 h-6 text-amber-500 mt-1" />
                                    ) : (
                                        <XCircle className="w-6 h-6 text-rose-500 mt-1" />
                                    )}
                                    <div>
                                        <h3 className={`font-semibold text-lg mb-1 ${
                                            fb.is_correct ? 'text-emerald-800' 
                                            : fb.score > 0 ? 'text-amber-800' : 'text-rose-800'
                                        }`}>
                                            Score: {fb.score} / {fb.max_score}
                                        </h3>
                                        <p className={`text-sm ${
                                            fb.is_correct ? 'text-emerald-600' 
                                            : fb.score > 0 ? 'text-amber-600' : 'text-rose-600'
                                        }`}>
                                            {fb.feedback}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </CardContent>
            </Card>

            {/* Navigation Controls */}
            <div className="flex justify-between items-center pt-4">
                <Button
                    variant="outline"
                    onClick={() => {
                        if (isSubmitted && currentQuestionIndex === 0) {
                            setCurrentQuestionIndex(-1); // Go back to results summary
                        } else {
                            setCurrentQuestionIndex(Math.max(0, currentQuestionIndex - 1));
                        }
                    }}
                    disabled={currentQuestionIndex === 0 && !isSubmitted}
                    className="border-slate-300 text-slate-700"
                >
                    Previous
                </Button>

                {currentQuestionIndex < practiceQuestions.length - 1 ? (
                    <Button
                        onClick={() => setCurrentQuestionIndex(currentQuestionIndex + 1)}
                        className="bg-slate-800 hover:bg-slate-900 text-white"
                    >
                        Next
                        <ArrowRight className="w-4 h-4 ml-2" />
                    </Button>
                ) : !isSubmitted ? (
                    <Button
                        onClick={markPracticeTest}
                        disabled={isMarking}
                        className="bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-600 hover:to-emerald-700 text-white shadow-md shadow-emerald-500/20"
                    >
                        {isMarking ? (
                            <>
                                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                                Submitting...
                            </>
                        ) : (
                            <>
                                Finish and Review
                                <CheckCircle2 className="w-4 h-4 ml-2" />
                            </>
                        )}
                    </Button>
                ) : (
                    <Button
                        onClick={() => setCurrentQuestionIndex(-1)}
                        className="bg-indigo-600 hover:bg-indigo-700 text-white"
                    >
                        View Results
                    </Button>
                )}
            </div>
            
            {/* Quick Navigation Dots */}
            <div className="flex justify-center gap-2 mt-8">
                {practiceQuestions.map((_, idx) => (
                    <button
                        key={idx}
                        onClick={() => setCurrentQuestionIndex(idx)}
                        className={`w-2.5 h-2.5 rounded-full transition-all ${
                            idx === currentQuestionIndex 
                                ? 'bg-indigo-600 scale-125' 
                                : isSubmitted && practiceFeedback?.results?.[practiceQuestions[idx].id]
                                    ? practiceFeedback.results[practiceQuestions[idx].id].is_correct
                                        ? 'bg-emerald-400'
                                        : practiceFeedback.results[practiceQuestions[idx].id].score > 0
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
