import React, { useEffect, useState } from 'react';
import { Card, CardContent } from '../../../ui/card';
import { Button } from '../../../ui/button';
import { 
    CheckCircle2, 
    XCircle, 
    AlertCircle, 
    LightbulbIcon,
    ArrowRight,
    Loader2
} from 'lucide-react';

export const Grade10BSEntrepreneurialQualitiesScaffold = ({
    scaffoldSteps,
    scaffoldStepIndex,
    setScaffoldStepIndex,
    scaffoldQuestion,
    scaffoldAnswer,
    setScaffoldAnswer,
    scaffoldFeedback,
    setScaffoldFeedback,
    scaffoldShowHint,
    setScaffoldShowHint,
    scaffoldLoading,
    scaffoldError,
    fetchScaffoldQuestion,
    questionSlotEnabled,
    markScaffoldAnswer,
}) => {
    const [inputValue, setInputValue] = useState('');

    const currentStep = scaffoldSteps[scaffoldStepIndex];

    useEffect(() => {
        fetchScaffoldQuestion({ subskill: currentStep.key });
        setInputValue('');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [currentStep]);

    const handleAnswerChange = (val) => {
        setInputValue(val);
        setScaffoldAnswer(val);
    };

    const submitAnswer = async () => {
        if (!scaffoldAnswer && scaffoldQuestion?.question_type !== 'mcq') return;
        await markScaffoldAnswer(scaffoldQuestion, scaffoldAnswer);
    };

    const renderQuestionContent = () => {
        if (scaffoldLoading) {
            return (
                <div className="flex flex-col items-center justify-center py-12 text-slate-500">
                    <Loader2 className="w-8 h-8 animate-spin mb-4 text-indigo-500" />
                    <p>Generating scenario...</p>
                </div>
            );
        }

        if (scaffoldError) {
            return (
                <div className="flex flex-col items-center justify-center py-8 text-red-500">
                    <AlertCircle className="w-8 h-8 mb-4" />
                    <p>{scaffoldError}</p>
                    <Button 
                        onClick={() => fetchScaffoldQuestion({ subskill: currentStep.key })}
                        className="mt-4 bg-indigo-600 hover:bg-indigo-700 text-white"
                    >
                        Retry
                    </Button>
                </div>
            );
        }

        if (!scaffoldQuestion) return null;

        return (
            <div className="space-y-6">
                {!questionSlotEnabled && (
                    <div className="prose max-w-none text-slate-700">
                        <div className="whitespace-pre-wrap">{scaffoldQuestion.prompt}</div>
                    </div>
                )}

                {scaffoldQuestion.question_type === 'mcq' && (
                    <div className="space-y-3">
                        {scaffoldQuestion.options.map((opt, idx) => (
                            <button
                                key={idx}
                                onClick={() => handleAnswerChange(String(idx))}
                                className={`w-full text-left p-4 rounded-xl border-2 transition-all duration-200 ${
                                    scaffoldAnswer === String(idx)
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

                {scaffoldQuestion.question_type === 'typed' && (
                    <div className="space-y-3">
                        <textarea
                            className="w-full p-4 border-2 border-slate-200 rounded-xl focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20 transition-all duration-200 text-slate-700 min-h-[150px]"
                            placeholder="Type your discussion or essay answer here..."
                            value={inputValue}
                            onChange={(e) => handleAnswerChange(e.target.value)}
                        />
                        <div className="flex justify-between items-center text-xs text-slate-500">
                            <span>Take your time to structure your answer.</span>
                            <span>Points: {scaffoldQuestion.marks || '1'}</span>
                        </div>
                    </div>
                )}

                {/* Controls */}
                <div className="flex gap-4 pt-4 border-t border-slate-100">
                    <Button
                        onClick={() => setScaffoldShowHint(!scaffoldShowHint)}
                        variant="outline"
                        className="flex-1 border-indigo-200 text-indigo-700 hover:bg-indigo-50"
                    >
                        <LightbulbIcon className="w-4 h-4 mr-2" />
                        {scaffoldShowHint ? 'Hide Hint' : 'Need a Hint?'}
                    </Button>

                    <Button
                        onClick={submitAnswer}
                        disabled={!scaffoldAnswer && scaffoldQuestion.question_type !== 'mcq'}
                        className="flex-1 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white shadow-md shadow-indigo-500/20"
                    >
                        Check Answer
                        <ArrowRight className="w-4 h-4 ml-2" />
                    </Button>
                </div>

                {scaffoldShowHint && scaffoldQuestion.explanation && (
                    <div className="p-4 bg-amber-50 border border-amber-200 rounded-xl text-amber-800 animate-in fade-in slide-in-from-top-2">
                        <p className="font-medium flex items-center gap-2 mb-1">
                            <LightbulbIcon className="w-4 h-4" />
                            Hint
                        </p>
                        <p className="text-sm">{scaffoldQuestion.explanation}</p>
                    </div>
                )}

                {/* Feedback */}
                {scaffoldFeedback && (
                    <div className={`p-6 rounded-xl border-2 animate-in fade-in slide-in-from-top-4 ${
                        scaffoldFeedback.is_correct 
                            ? 'bg-emerald-50 border-emerald-200' 
                            : scaffoldFeedback.score > 0 
                                ? 'bg-amber-50 border-amber-200'
                                : 'bg-rose-50 border-rose-200'
                    }`}>
                        <div className="flex items-start gap-4">
                            {scaffoldFeedback.is_correct ? (
                                <CheckCircle2 className="w-6 h-6 text-emerald-500 mt-1" />
                            ) : scaffoldFeedback.score > 0 ? (
                                <AlertCircle className="w-6 h-6 text-amber-500 mt-1" />
                            ) : (
                                <XCircle className="w-6 h-6 text-rose-500 mt-1" />
                            )}
                            <div>
                                <h3 className={`font-semibold text-lg mb-1 ${
                                    scaffoldFeedback.is_correct ? 'text-emerald-800' 
                                    : scaffoldFeedback.score > 0 ? 'text-amber-800' : 'text-rose-800'
                                }`}>
                                    {scaffoldFeedback.is_correct ? 'Excellent!' : scaffoldFeedback.score > 0 ? 'Good effort!' : 'Not quite right'}
                                </h3>
                                <p className={`text-sm ${
                                    scaffoldFeedback.is_correct ? 'text-emerald-600' 
                                    : scaffoldFeedback.score > 0 ? 'text-amber-600' : 'text-rose-600'
                                }`}>
                                    {scaffoldFeedback.feedback}
                                </p>
                            </div>
                        </div>

                        {scaffoldFeedback.is_correct && (
                            <div className="mt-6 flex justify-end">
                                <Button
                                    onClick={() => {
                                        if (scaffoldStepIndex < scaffoldSteps.length - 1) {
                                            setScaffoldStepIndex(i => i + 1);
                                        } else {
                                            setScaffoldStepIndex(0); // Reset or show completion
                                        }
                                    }}
                                    className="bg-emerald-600 hover:bg-emerald-700 text-white shadow-md shadow-emerald-500/20"
                                >
                                    {scaffoldStepIndex < scaffoldSteps.length - 1 ? 'Next Challenge' : 'Start Over'}
                                    <ArrowRight className="w-4 h-4 ml-2" />
                                </Button>
                            </div>
                        )}
                    </div>
                )}
            </div>
        );
    };

    return (
        <div className="max-w-4xl mx-auto space-y-6 animate-in fade-in duration-500">
            {/* Header */}
            <div className="text-center space-y-2 mb-8">
                <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-indigo-600 to-purple-600">
                    Understanding Entrepreneurial Qualities
                </h1>
                <p className="text-slate-500">Step-by-step guided practice</p>
            </div>

            {/* Progress Bar */}
            <div className="flex justify-between mb-8 overflow-x-auto pb-4 custom-scrollbar">
                {scaffoldSteps.map((step, index) => (
                    <button
                        key={step.key}
                        onClick={() => setScaffoldStepIndex(index)}
                        className={`flex flex-col items-center flex-1 min-w-[120px] transition-all duration-300 relative ${
                            index <= scaffoldStepIndex ? 'opacity-100' : 'opacity-50'
                        }`}
                    >
                        <div className={`w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold border-2 z-10 bg-white ${
                            index < scaffoldStepIndex 
                                ? 'border-emerald-500 text-emerald-500 bg-emerald-50' 
                                : index === scaffoldStepIndex
                                    ? 'border-indigo-600 text-indigo-600 shadow-lg shadow-indigo-200'
                                    : 'border-slate-300 text-slate-400'
                        }`}>
                            {index < scaffoldStepIndex ? <CheckCircle2 className="w-6 h-6" /> : index + 1}
                        </div>
                        <span className={`text-xs mt-2 font-medium text-center px-2 ${
                            index === scaffoldStepIndex ? 'text-indigo-700' : 'text-slate-500'
                        }`}>
                            {step.title}
                        </span>
                        
                        {/* Connecting line */}
                        {index < scaffoldSteps.length - 1 && (
                            <div className={`absolute top-5 left-1/2 w-full h-[2px] -z-10 ${
                                index < scaffoldStepIndex ? 'bg-emerald-500' : 'bg-slate-200'
                            }`} />
                        )}
                    </button>
                ))}
            </div>

            {/* Main Content */}
            <Card className="border-none shadow-xl shadow-slate-200/50 overflow-hidden bg-white/80 backdrop-blur-sm">
                <CardContent className="p-8">
                    {renderQuestionContent()}
                </CardContent>
            </Card>
        </div>
    );
};
