import React from 'react';
import { ChevronLeft, FileText, FunctionSquare } from 'lucide-react';
import MathTopicModeCards from './MathTopicModeCards';
import AccountingTopicModeCards from './AccountingTopicModeCards';
import BusinessStudiesTopicModeCards from './BusinessStudiesTopicModeCards';
import EmsTopicModeCards from './EmsTopicModeCards';

const TopicOverviewSection = ({
    selectedTopic,
    selectedTopicDisplayName,
    flags,
    updateHelperNavigationLabel,
    setHelperView,
    showTopicSummary,
    setShowTopicSummary,
    setShowMathComponentsRepository,
    availableRepositories,
    navigateToWorkspaceWithMode,
    getTopicTerm,
}) => {
    if (!selectedTopic) return null;

    return (
        <>
            <button
                onClick={() => {
                    setHelperView('topics');
                    updateHelperNavigationLabel('Curriculum Helper > Topics');
                }}
                className="flex items-center text-blue-500 hover:text-blue-700 mb-6 transition-colors"
            >
                <ChevronLeft className="h-5 w-5 mr-1" />
                Back to Topics
            </button>
            <h2 className="text-4xl font-extrabold text-gray-900 mb-2">{selectedTopicDisplayName}</h2>
            <p className="text-lg text-gray-600 mb-8">{selectedTopic.overview || 'No overview available.'}</p>

            <MathTopicModeCards
                selectedTopic={selectedTopic}
                navigateToWorkspaceWithMode={navigateToWorkspaceWithMode}
                flags={flags}
            />
            <AccountingTopicModeCards
                selectedTopic={selectedTopic}
                navigateToWorkspaceWithMode={navigateToWorkspaceWithMode}
                flags={flags}
            />
            <BusinessStudiesTopicModeCards
                selectedTopic={selectedTopic}
                selectedTopicDisplayName={selectedTopicDisplayName}
                getTopicTerm={getTopicTerm}
                navigateToWorkspaceWithMode={navigateToWorkspaceWithMode}
                flags={flags}
            />
            <EmsTopicModeCards
                selectedTopic={selectedTopic}
                navigateToWorkspaceWithMode={navigateToWorkspaceWithMode}
                flags={flags}
            />

            {!flags.isGrade11BusinessStudies && (
                <>
                    <div className="flex flex-wrap gap-3 mb-6">
                        <button onClick={() => setShowTopicSummary((p) => !p)} className="flex items-center space-x-2 px-4 py-2 bg-blue-500 text-white rounded-full text-sm font-semibold hover:bg-blue-600 shadow-md">
                            <FileText size={16} />
                            <span>Topic Summary</span>
                        </button>
                        <button onClick={() => setShowMathComponentsRepository((p) => !p)} className="flex items-center space-x-2 px-4 py-2 bg-purple-500 text-white rounded-full text-sm font-semibold hover:bg-purple-600 shadow-md">
                            <FunctionSquare size={16} />
                            <span>Mathematical Visual Aids</span>
                        </button>

                        {availableRepositories.length > 0 && (
                            <div className="p-2 bg-gray-50 rounded border border-gray-200">
                                <p className="text-xs text-gray-600 mb-2 font-medium">Reference Tools:</p>
                                <div className="flex flex-wrap gap-2">
                                    {availableRepositories.map((repo) => (
                                        <button
                                            key={repo.key}
                                            onClick={repo.onClick}
                                            className="flex items-center space-x-1 bg-white text-gray-700 px-2 py-1 rounded border border-gray-300 hover:bg-gray-100 hover:border-gray-400 transition-colors duration-200 text-xs"
                                            title={`Open ${repo.name}`}
                                        >
                                            <repo.icon size={14} />
                                            <span>{repo.name}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>
                        )}
                    </div>
                    {showTopicSummary && (
                        <div className="bg-blue-50 p-4 rounded-lg border border-blue-200 mb-6">
                            <h4 className="font-semibold text-blue-800 mb-2">Summary of {selectedTopicDisplayName}:</h4>
                            <p className="text-gray-700 text-sm">{selectedTopic.overview || 'No summary.'}</p>
                        </div>
                    )}
                    <h4 className="font-bold text-gray-800 mt-6 mb-4 text-xl">Subtopics:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {selectedTopic.subtopics && selectedTopic.subtopics.length > 0 ? selectedTopic.subtopics.map((subtopic) => (
                            <div key={subtopic} className="bg-gray-50 p-4 rounded-lg border border-gray-200 flex flex-col justify-between">
                                <p className="font-medium text-gray-800 text-lg mb-3">{subtopic}</p>
                                <div className="text-sm text-gray-500">Open this topic through the mode cards above to continue.</div>
                            </div>
                        )) : <p>No subtopics.</p>}
                    </div>
                </>
            )}
        </>
    );
};

export default TopicOverviewSection;
