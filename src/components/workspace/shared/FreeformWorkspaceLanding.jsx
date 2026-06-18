import React from 'react';
import { ArrowRight, BookOpen, FileText, PenTool, Sparkles } from 'lucide-react';

const FreeformWorkspaceLanding = ({
    selectedSubject,
    selectedGrade,
    availableTopics,
    selectedTopic,
    onSelectTopic,
    onStartWriting,
    onOpenSourceDocuments,
    availableRepositories,
}) => {
    const subjectLabel = selectedSubject?.name || 'your subject';
    const gradeLabel = selectedGrade ? `Grade ${selectedGrade}` : 'your grade';

    return (
        <div className="min-h-screen bg-slate-50 px-4 py-8 sm:px-6 lg:px-8">
            <div className="max-w-5xl mx-auto space-y-6">
                <div className="bg-white border border-slate-200 rounded-3xl shadow-sm p-8 sm:p-10">
                    <div className="max-w-3xl space-y-4">
                        <div className="inline-flex items-center gap-2 rounded-full bg-blue-50 text-blue-700 px-4 py-2 text-sm font-medium">
                            <Sparkles className="h-4 w-4" />
                            <span>Freeform Workspace</span>
                        </div>
                        <div className="space-y-2">
                            <h1 className="text-3xl sm:text-4xl font-bold text-slate-900">
                                Start a fresh problem-solving session in {subjectLabel}
                            </h1>
                            <p className="text-slate-600 text-base sm:text-lg">
                                Choose a topic for better AI context, then jump into an open work area for notes, rough work, and guided help.
                            </p>
                            <p className="text-sm text-slate-500">
                                {gradeLabel} · {subjectLabel}
                            </p>
                        </div>
                    </div>

                    <div className="mt-8 grid grid-cols-1 lg:grid-cols-[1.3fr_0.9fr] gap-6">
                        <div className="rounded-2xl border border-slate-200 bg-slate-50 p-6 space-y-4">
                            <label className="block text-sm font-semibold text-slate-700">
                                Topic for AI context
                            </label>
                            <select
                                value={selectedTopic}
                                onChange={(e) => onSelectTopic(e.target.value)}
                                className="w-full px-4 py-3 text-sm border border-slate-300 rounded-xl bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                            >
                                <option value="">Select a topic</option>
                                {availableTopics.map((topicName) => (
                                    <option key={topicName} value={topicName}>{topicName}</option>
                                ))}
                            </select>
                            <div className="flex flex-wrap gap-3 pt-2">
                                <button
                                    onClick={onStartWriting}
                                    className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-700 transition-colors"
                                >
                                    <PenTool className="h-4 w-4" />
                                    <span>Start Writing</span>
                                </button>
                                <button
                                    onClick={onOpenSourceDocuments}
                                    className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-white text-slate-700 border border-slate-300 font-semibold hover:bg-slate-100 transition-colors"
                                >
                                    <FileText className="h-4 w-4" />
                                    <span>Use Source Documents</span>
                                </button>
                            </div>
                        </div>

                        <div className="rounded-2xl border border-slate-200 bg-white p-6 space-y-4">
                            <div className="flex items-center gap-2 text-slate-900 font-semibold">
                                <BookOpen className="h-5 w-5 text-indigo-600" />
                                <span>Workspace tools</span>
                            </div>
                            <div className="space-y-3">
                                {availableRepositories.length > 0 ? availableRepositories.map((repo) => {
                                    const Icon = repo.icon;
                                    return (
                                        <button
                                            key={repo.key}
                                            onClick={repo.onClick}
                                            className="w-full flex items-center justify-between rounded-xl border border-slate-200 px-4 py-3 text-left hover:bg-slate-50 transition-colors"
                                        >
                                            <span className="flex items-center gap-3 text-slate-700 font-medium">
                                                <Icon className="h-4 w-4 text-slate-500" />
                                                <span>{repo.name}</span>
                                            </span>
                                            <ArrowRight className="h-4 w-4 text-slate-400" />
                                        </button>
                                    );
                                }) : (
                                    <div className="rounded-xl border border-dashed border-slate-300 px-4 py-5 text-sm text-slate-500">
                                        No extra tools are available for this subject yet.
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default FreeformWorkspaceLanding;
