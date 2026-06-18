import React from 'react';

import { StudentView } from '../../components/student';
import { Workspace } from '../../components/workspace';
import FeatureGatePanel from '../../components/ui/FeatureGatePanel';
import { canAccessSavedProblems, SAVED_PROBLEMS_PRO_MESSAGE } from '../constants/access';
import { getSubjectKeyFromSelection } from '../utils/subjectKeys';

export default function RenderStudentContent({ studentContentProps }) {
  const {
    components,
    data,
    actions,
    handlers,
    services,
  } = studentContentProps;

  const {
    MySavedProblemsViewComponent,
  } = components;

  const {
    activeAssignment,
    activeEditableRef,
    activeTopic,
    allCurricula,
    chatHistories,
    currentProblemThreadId,
    freeformAnswer,
    freeformWorkAreaRef,
    isCurriculumPageVisible,
    isKeypadVisible,
    loading,
    navigationStack,
    practiceQuestions,
    selectedCurriculumKey,
    selectedFreeformTopic,
    selectedGrade,
    selectedSubject,
    view,
    workspaceMode,
  } = data;

  const {
    setActiveEditableRef,
    setActiveTopic,
    setFreeformAnswer,
    setIsCurriculumPageVisible,
    setIsKeypadVisible,
    setLoading,
    setMessage,
    setNavigationStack,
    setPracticeQuestions,
    setSelectedCurriculumKey,
    setSelectedFreeformTopic,
    setSelectedGrade,
    setSelectedSubject,
    setView,
    setWorkspaceMode,
    updateHelperNavigationLabel,
  } = actions;

  const {
    addQuestionToChat,
    handleAnswerInput,
    handleAssignmentSubmit,
    handleAttempt,
    handleContinueProblem,
    handleExplainMistake,
    handleMarkStrugglingProblemSolved,
    handleSendFreeformQuery,
    handleStartAssignment,
    handleStrugglingProblem,
    handleSubmit,
    handleToggleMathStructure,
    onManageSubscriptionPage,
    updateAnswerInChat,
  } = handlers;

  const {
    currentUser,
    dbService,
    getAgentResponse,
    storage,
  } = services;

  const subjectKey = getSubjectKeyFromSelection({
    selectedCurriculumKey,
    selectedGrade,
    selectedSubject,
  });

  switch (view) {
    case 'my_saved_problems':
      if (!canAccessSavedProblems(currentUser)) {
        return (
          <div className="p-4 sm:p-6 lg:p-8">
            <FeatureGatePanel
              title="My Saved Problems"
              description={SAVED_PROBLEMS_PRO_MESSAGE}
              badge="Pro package only"
              buttonLabel="View subscription options"
              onButtonClick={onManageSubscriptionPage}
            />
          </div>
        );
      }

      return (
        <MySavedProblemsViewComponent
          db={dbService}
          currentUser={currentUser}
          onContinueProblem={handleContinueProblem}
          onMarkSolved={handleMarkStrugglingProblemSolved}
          setMessage={setMessage}
        />
      );
    case 'workspace':
      console.log('[App Debug] Rendering Workspace. activeTopic:', activeTopic);
      return (
        <Workspace
          topic={activeTopic?.name}
          practiceQuestions={practiceQuestions}
          workspaceMode={workspaceMode}
          setWorkspaceMode={setWorkspaceMode}
          freeformWorkAreaRef={freeformWorkAreaRef}
          currentUser={currentUser}
          getAgentResponse={getAgentResponse}
          handleAnswerInput={handleAnswerInput}
          handleSubmit={handleSubmit}
          setView={setView}
          activeAssignment={activeAssignment}
          handleAssignmentSubmit={handleAssignmentSubmit}
          handleExplainMistake={handleExplainMistake}
          loading={loading}
          setLoading={setLoading}
          selectedSubject={selectedSubject}
          selectedGrade={selectedGrade}
          addQuestionToChat={addQuestionToChat}
          updateAnswerInChat={updateAnswerInChat}
          handleSendFreeformQuery={handleSendFreeformQuery}
          freeformAnswer={freeformAnswer}
          setFreeformAnswer={setFreeformAnswer}
          currentProblemThreadId={currentProblemThreadId}
          setSelectedFreeformTopic={setSelectedFreeformTopic}
        />
      );
    default:
      return (
        <StudentView
          view={view}
          setView={setView}
          allCurricula={allCurricula}
          selectedCurriculumKey={selectedCurriculumKey}
          setSelectedCurriculumKey={setSelectedCurriculumKey}
          selectedGrade={selectedGrade}
          setSelectedGrade={setSelectedGrade}
          selectedSubject={selectedSubject}
          setSelectedSubject={setSelectedSubject}
          activeTopic={activeTopic}
          setActiveTopic={setActiveTopic}
          practiceQuestions={practiceQuestions}
          setPracticeQuestions={setPracticeQuestions}
          isCurriculumPageVisible={isCurriculumPageVisible}
          setIsCurriculumPageVisible={setIsCurriculumPageVisible}
          isKeypadVisible={isKeypadVisible}
          setIsKeypadVisible={setIsKeypadVisible}
          activeEditableRef={activeEditableRef}
          setActiveEditableRef={setActiveEditableRef}
          workspaceMode={workspaceMode}
          setWorkspaceMode={setWorkspaceMode}
          freeformWorkAreaRef={freeformWorkAreaRef}
          currentUser={currentUser}
          getAgentResponse={getAgentResponse}
          handleAttempt={handleAttempt}
          handleAnswerInput={handleAnswerInput}
          handleSubmit={handleSubmit}
          navigationStack={navigationStack}
          setNavigationStack={setNavigationStack}
          updateHelperNavigationLabel={updateHelperNavigationLabel}
          db={dbService}
          storage={storage}
          handleStartAssignment={handleStartAssignment}
          activeAssignment={activeAssignment}
          handleAssignmentSubmit={handleAssignmentSubmit}
          handleToggleMathStructure={handleToggleMathStructure}
          loading={loading}
          setLoading={setLoading}
          chatHistory={chatHistories[subjectKey] || []}
          addQuestionToChat={addQuestionToChat}
          updateAnswerInChat={updateAnswerInChat}
          handleSendFreeformQuery={handleSendFreeformQuery}
          freeformAnswer={freeformAnswer}
          setFreeformAnswer={setFreeformAnswer}
          selectedFreeformTopic={selectedFreeformTopic}
          setSelectedFreeformTopic={setSelectedFreeformTopic}
          currentProblemThreadId={currentProblemThreadId}
          handleStrugglingProblem={handleStrugglingProblem}
          handleMarkStrugglingProblemSolved={handleMarkStrugglingProblemSolved}
          handleContinueProblem={handleContinueProblem}
          onManageSubscriptionPage={onManageSubscriptionPage}
          curriculumData={allCurricula[selectedCurriculumKey]?.topicsByGrade || {}}
        />
      );
  }
}
