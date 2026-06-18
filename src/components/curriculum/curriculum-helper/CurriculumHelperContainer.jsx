import React, { useEffect, useMemo, useState } from 'react';
import { buildAvailableTopics, buildSubjectFlags } from './subjectFlags';
import { getScaffoldRouteForTopic } from './topicRouting';
import {
    getTopicDisplayName,
    getOrderedTopicNames,
    getSelectedTopicDisplayName,
    getTopicCardTitle,
    getTopicTerm,
} from './topicMetadata';
import { getAvailableRepositories } from './repositories';
import TopicListSection from './components/TopicListSection';
import TopicOverviewSection from './components/TopicOverviewSection';
import RepositoryModals from './components/RepositoryModals';

const CurriculumHelperContainer = React.memo(({
    onClose,
    selectedGrade,
    selectedSubject,
    setWorkspaceMode,
    setActiveTopic,
    updateHelperNavigationLabel,
    setView,
    setNavigationStack,
    navigationStack,
    onGoToClasswork,
    currentUser,
    onManageSubscriptionPage,
}) => {
    const [showTopicSummary, setShowTopicSummary] = useState(false);
    const [helperView, setHelperView] = useState('topics');
    const [selectedTopic, setSelectedTopic] = useState(null);
    const [showMathComponentsRepository, setShowMathComponentsRepository] = useState(false);
    const [showChemistryComponentsRepository, setShowChemistryComponentsRepository] = useState(false);
    const [showPhysicsComponentsRepository, setShowPhysicsComponentsRepository] = useState(false);
    const [showCrossDisciplinaryComponentsRepository, setShowCrossDisciplinaryComponentsRepository] = useState(false);
    const [selectedComponent, setSelectedComponent] = useState(null);
    const [isComponentOverlayVisible, setIsComponentOverlayVisible] = useState(false);
    const [isComponentFullscreen, setIsComponentFullscreen] = useState(false);

    const flags = useMemo(
        () => buildSubjectFlags({ selectedGrade, selectedSubject }),
        [selectedGrade, selectedSubject]
    );

    const availableTopics = useMemo(
        () => buildAvailableTopics({ selectedGrade, selectedSubject }),
        [selectedGrade, selectedSubject]
    );

    const orderedTopicNames = useMemo(
        () => getOrderedTopicNames(availableTopics, flags),
        [availableTopics, flags]
    );

    const hasSyllabus = selectedSubject?.topicsByGrade?.[selectedGrade]?.syllabus_info || false;

    useEffect(() => {
        setHelperView('topics');
        setSelectedTopic(null);
        setShowTopicSummary(false);
        updateHelperNavigationLabel('Curriculum Helper > Topics');
    }, [selectedGrade, selectedSubject, updateHelperNavigationLabel]);

    const navigateToWorkspaceWithMode = (mode, label, topicData = null) => {
        if (!setWorkspaceMode || !setView || !setNavigationStack) return;

        setWorkspaceMode(mode);

        const topicToUse = topicData || selectedTopic;
        if (setActiveTopic && topicToUse) {
            setActiveTopic(topicToUse);
        }

        const currentStack = Array.isArray(navigationStack) ? navigationStack : [];
        const nextStack = [
            ...currentStack,
            {
                view: 'workspace',
                label,
                data: {
                    grade: selectedGrade,
                    subject: selectedSubject,
                    topic: selectedTopic,
                },
            },
        ];
        setNavigationStack(nextStack);
        setView('workspace');
    };

    const handleTopicSelect = (topic) => {
        const topicName = typeof topic === 'string' ? topic : topic?.name;
        if (!topicName) return;

        const topicData = typeof topic === 'string' ? { name: topicName } : topic;
        const scaffoldRoute = getScaffoldRouteForTopic(topicName, flags);

        if (scaffoldRoute) {
            navigateToWorkspaceWithMode(
                scaffoldRoute,
                getTopicDisplayName(topicName, flags),
                topicData
            );
            return;
        }

        const overview = selectedSubject?.topicsByGrade?.[selectedGrade]?.overview?.[topicName] || 'No overview available for this topic yet.';
        const subtopics = selectedSubject?.topicsByGrade?.[selectedGrade]?.subtopics?.[topicName] || [];

        setSelectedTopic({
            name: topicName,
            overview,
            subtopics,
        });
        setHelperView('topic_overview');
        setShowTopicSummary(false);
    };

    const availableRepositories = useMemo(
        () => getAvailableRepositories(selectedSubject, selectedGrade, {
            openMathComponentsRepository: () => setShowMathComponentsRepository(true),
            openChemistryComponentsRepository: () => setShowChemistryComponentsRepository(true),
            openPhysicsComponentsRepository: () => setShowPhysicsComponentsRepository(true),
            openCrossDisciplinaryComponentsRepository: () => setShowCrossDisciplinaryComponentsRepository(true),
        }),
        [selectedSubject, selectedGrade]
    );

    const selectedTopicDisplayName = getSelectedTopicDisplayName(selectedTopic?.name, flags);
    const getTopicTermForCurrentFlags = (topicName) => getTopicTerm(topicName, flags);
    const getTopicCardTitleForCurrentFlags = (topicName) => getTopicCardTitle(topicName, flags);

    if (!selectedGrade || !selectedSubject) {
        return (
            <div className="p-8 text-center bg-white rounded-xl shadow-lg min-h-[60vh] flex flex-col justify-center items-center">
                <h2 className="text-2xl font-bold text-gray-800 mb-4">Curriculum Helper</h2>
                <p className="text-gray-600">Please select a curriculum, grade, and subject first.</p>
                <button onClick={onClose} className="mt-8 bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600">Go Back</button>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-white rounded-xl shadow-xl min-h-[80vh]">
            <RepositoryModals
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
                setView={setView}
                showMathComponentsRepository={showMathComponentsRepository}
                setShowMathComponentsRepository={setShowMathComponentsRepository}
                showChemistryComponentsRepository={showChemistryComponentsRepository}
                setShowChemistryComponentsRepository={setShowChemistryComponentsRepository}
                showPhysicsComponentsRepository={showPhysicsComponentsRepository}
                setShowPhysicsComponentsRepository={setShowPhysicsComponentsRepository}
                showCrossDisciplinaryComponentsRepository={showCrossDisciplinaryComponentsRepository}
                setShowCrossDisciplinaryComponentsRepository={setShowCrossDisciplinaryComponentsRepository}
                selectedComponent={selectedComponent}
                setSelectedComponent={setSelectedComponent}
                isComponentOverlayVisible={isComponentOverlayVisible}
                setIsComponentOverlayVisible={setIsComponentOverlayVisible}
                isComponentFullscreen={isComponentFullscreen}
                setIsComponentFullscreen={setIsComponentFullscreen}
            />

            {helperView === 'topics' && (
                <TopicListSection
                    selectedSubject={selectedSubject}
                    selectedGrade={selectedGrade}
                    onGoToClasswork={onGoToClasswork}
                    hasSyllabus={hasSyllabus}
                    orderedTopicNames={orderedTopicNames}
                    currentUser={currentUser}
                    onTopicSelect={handleTopicSelect}
                    onLockedTopicSelect={() => onManageSubscriptionPage?.()}
                    getTopicCardTitle={getTopicCardTitleForCurrentFlags}
                    getTopicTerm={getTopicTermForCurrentFlags}
                />
            )}

            {helperView === 'topic_overview' && (
                <TopicOverviewSection
                    selectedTopic={selectedTopic}
                    selectedTopicDisplayName={selectedTopicDisplayName}
                    flags={flags}
                    updateHelperNavigationLabel={updateHelperNavigationLabel}
                    setHelperView={setHelperView}
                    showTopicSummary={showTopicSummary}
                    setShowTopicSummary={setShowTopicSummary}
                    setShowMathComponentsRepository={setShowMathComponentsRepository}
                    availableRepositories={availableRepositories}
                    navigateToWorkspaceWithMode={navigateToWorkspaceWithMode}
                    getTopicTerm={getTopicTermForCurrentFlags}
                />
            )}
        </div>
    );
});

export default CurriculumHelperContainer;
