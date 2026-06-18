import React, { useEffect, useState } from 'react';
import { Card, CardContent } from '../../../../grade10/ui/card';
import { Button } from '../../../../grade10/ui/button';
import {
    AlertCircle,
    ArrowRight,
    BookOpen,
    CheckCircle2,
    Loader2,
    Target,
    Trophy,
    XCircle,
} from 'lucide-react';

const MemoCard = ({ question }) => {
    const correctOption = question?.question_type === 'mcq' && Array.isArray(question?.options)
        ? question.options[Number(question.correct_index)]
        : null;

    return (
        <div className="rounded-2xl border border-indigo-200 bg-indigo-50 p-5 space-y-4">
            {correctOption && (
                <div className="space-y-1">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Correct answer</p>
                    <p className="text-sm text-slate-700">{correctOption}</p>
                </div>
            )}

            {Array.isArray(question?.marking_points) && question.marking_points.length > 0 && (
                <div className="space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Marking points</p>
                    <ul className="space-y-2 text-sm text-slate-700">
                        {question.marking_points.map((item, index) => (
                            <li key={`${question.id}-memo-mark-${index}`} className="rounded-xl bg-white/80 px-3 py-2 border border-indigo-100">
                                {item}
                            </li>
                        ))}
                    </ul>
                </div>
            )}

            {Array.isArray(question?.answer_part_hints) && question.answer_part_hints.length > 0 && (
                <div className="space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Suggested answer structure</p>
                    <ul className="space-y-2 text-sm text-slate-700">
                        {question.answer_part_hints.map((item, index) => (
                            <li key={`${question.id}-memo-structure-${index}`} className="rounded-xl bg-white/80 px-3 py-2 border border-indigo-100">
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
        </div>
    );
};

export const Grade11BSInfluencesPractice = ({
    practiceQuestions,
    practiceAnswers,
    setPracticeAnswers,
    practiceFeedback,
    practiceLoading,
    practiceError,
    practiceDifficulty,
    practiceSubskill,
    fetchPractice,
    currentQuestionIndex,
    setCurrentQuestionIndex,
    resetMarking,
    markPracticeTest,
    markingStatus,
}) => {
    const [memoOpenById, setMemoOpenById] = useState({});

    const isMarking = markingStatus === 'marking_active';
    const isSubmitted = markingStatus === 'marking_submitted';

    useEffect(() => {
        if (!isSubmitted) {
            setCurrentQuestionIndex(0);
            setMemoOpenById({});
        }
    }, [isSubmitted]);

    const handleAnswerChange = (questionId, value) => {
        if (isMarking || isSubmitted) {
            return;
        }
        setPracticeAnswers((current) => ({
            ...current,
            [questionId]: value,
        }));
    };

    if (practiceLoading) {
        return (
            <div className="flex flex-col items-center justify-center min-h-[400px] text-slate-500">
                <Loader2 className="w-12 h-12 animate-spin mb-4 text-indigo-500" />
                <p className="text-lg">Generating your Grade 11 Business Studies practice set...</p>
            </div>
        );
    }

    if (practiceError) {
        return (
            <div className="flex flex-col items-center justify-center min-h-[400px] text-red-500">
                <AlertCircle className="w-12 h-12 mb-4" />
                <p className="text-lg mb-4 text-center">{practiceError}</p>
                <Button
                    onClick={() => {
                        resetMarking();
                        fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill });
                    }}
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

    if (isSubmitted && practiceFeedback?.results && currentQuestionIndex === -1) {
        const totalScore = practiceFeedback.total_score || 0;
        const maxScore = practiceFeedback.max_score || 1;
        const percentage = Math.round((totalScore / maxScore) * 100);

        return (
            <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in duration-500">
                <Card className="border-none shadow-xl shadow-slate-200/50 bg-white/80 backdrop-blur-sm overflow-hidden">
                    <div className="bg-gradient-to-r from-indigo-600 to-purple-600 p-12 text-center text-white">
                        <Trophy className="w-20 h-20 mx-auto mb-6 text-yellow-300 drop-shadow-lg" />
                        <h2 className="text-4xl font-bold mb-2">Practice Review Ready</h2>
                        <p className="text-indigo-100 text-lg">Use the memo review to compare every answer with the expected Business Studies response.</p>
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
                                onClick={() => {
                                    resetMarking();
                                    fetchPractice({ difficulty: practiceDifficulty, subskill: practiceSubskill });
                                }}
                                className="bg-indigo-600 hover:bg-indigo-700 text-white"
                            >
                                Generate Another Set
                            </Button>
                        </div>
                    </CardContent>
                </Card>
            </div>
        );
    }

    const currentQuestion = practiceQuestions[currentQuestionIndex];
    const questionId = currentQuestion?.id;
    const currentAnswer = practiceAnswers[questionId] || '';
    const feedback = practiceFeedback?.results?.[questionId];

    return (
        <div className="max-w-4xl mx-auto space-y-6 animate-in fade-in duration-500">
            <Card className="border-none shadow-xl shadow-slate-200/50 bg-white/80 backdrop-blur-sm overflow-hidden">
                <CardContent className="p-8 space-y-6">
                    <div className="flex items-center justify-between gap-4">
                        <div className="flex items-center gap-2 bg-slate-50 px-4 py-2 rounded-full border border-slate-200">
                            <Target className="w-4 h-4 text-indigo-500" />
                            <span className="font-medium text-slate-700">
                                Question {currentQuestionIndex + 1} of {practiceQuestions.length}
                            </span>
                        </div>
                    </div>

                    {currentQuestion.question_type === 'mcq' && (
                        <div className="space-y-3 pt-4">
                            {currentQuestion.options.map((option, index) => (
                                <button
                                    key={`${currentQuestion.id}-${index}`}
                                    disabled={isSubmitted || isMarking}
                                    onClick={() => handleAnswerChange(questionId, String(index))}
                                    className={`w-full text-left p-4 rounded-xl border-2 transition-all duration-200 disabled:cursor-default ${
                                        currentAnswer === String(index)
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

                    {currentQuestion.question_type === 'typed' && (
                        <div className="space-y-3 pt-4">
                            <textarea
                                disabled={isSubmitted || isMarking}
                                className="w-full p-4 border-2 border-slate-200 rounded-xl focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20 transition-all duration-200 text-slate-700 min-h-[170px] disabled:bg-slate-50 disabled:text-slate-500"
                                placeholder="Type your answer here..."
                                value={currentAnswer}
                                onChange={(event) => handleAnswerChange(questionId, event.target.value)}
                            />
                        </div>
                    )}

                    {isSubmitted && feedback && (
                        <div className={`p-6 rounded-xl border-2 ${
                            feedback.is_correct
                                ? 'bg-emerald-50 border-emerald-200'
                                : feedback.score > 0
                                    ? 'bg-amber-50 border-amber-200'
                                    : 'bg-rose-50 border-rose-200'
                        }`}>
                            <div className="flex items-start gap-4">
                                {feedback.is_correct ? (
                                    <CheckCircle2 className="w-6 h-6 text-emerald-500 mt-1" />
                                ) : feedback.score > 0 ? (
                                    <AlertCircle className="w-6 h-6 text-amber-500 mt-1" />
                                ) : (
                                    <XCircle className="w-6 h-6 text-rose-500 mt-1" />
                                )}
                                <div className="space-y-2">
                                    <h3 className={`font-semibold text-lg ${
                                        feedback.is_correct
                                            ? 'text-emerald-800'
                                            : feedback.score > 0
                                                ? 'text-amber-800'
                                                : 'text-rose-800'
                                    }`}>
                                        Score: {feedback.score} / {feedback.max_score}
                                    </h3>
                                    <p className={`text-sm ${
                                        feedback.is_correct
                                            ? 'text-emerald-600'
                                            : feedback.score > 0
                                                ? 'text-amber-600'
                                                : 'text-rose-600'
                                    }`}>
                                        {feedback.feedback}
                                    </p>
                                </div>
                            </div>

                            <div className="mt-5 flex flex-wrap gap-3">
                                <Button
                                    onClick={() => setMemoOpenById((current) => ({
                                        ...current,
                                        [questionId]: !current[questionId],
                                    }))}
                                    variant="outline"
                                    className="border-indigo-200 text-indigo-700 hover:bg-indigo-50"
                                >
                                    <BookOpen className="w-4 h-4 mr-2" />
                                    {memoOpenById[questionId] ? 'Hide Memo' : 'Compare to Memo'}
                                </Button>
                            </div>

                            {memoOpenById[questionId] && (
                                <div className="mt-5">
                                    <MemoCard question={currentQuestion} />
                                </div>
                            )}
                        </div>
                    )}
                </CardContent>
            </Card>

            <div className="flex justify-between items-center pt-4">
                <Button
                    variant="outline"
                    onClick={() => {
                        if (isSubmitted && currentQuestionIndex === 0) {
                            setCurrentQuestionIndex(-1);
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

            <div className="flex justify-center gap-2 mt-8">
                {practiceQuestions.map((question, index) => (
                    <button
                        key={question.id || index}
                        onClick={() => setCurrentQuestionIndex(index)}
                        className={`w-2.5 h-2.5 rounded-full transition-all ${
                            index === currentQuestionIndex
                                ? 'bg-indigo-600 scale-125'
                                : isSubmitted && practiceFeedback?.results?.[question.id]
                                    ? practiceFeedback.results[question.id].is_correct
                                        ? 'bg-emerald-400'
                                        : practiceFeedback.results[question.id].score > 0
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
