import React, { useState } from 'react';
import { ChevronLeft, BarChart2 } from 'lucide-react';
import SubjectShelf from '../../components/navigation/SubjectShelf';
import { StudentView } from '../../components/student';
import { Workspace } from '../../components/workspace';
import MicroBenchmarkModal from '../../components/student/MicroBenchmarkModal';
import FeatureGatePanel from '../../components/ui/FeatureGatePanel';
import { canAccessSavedProblems, SAVED_PROBLEMS_PRO_MESSAGE } from '../constants/access';
import { getSubjectKeyFromSelection } from '../utils/subjectKeys';

export default function RenderStudentContent({ studentContentProps }) {
  const [showWorkspaceBenchmark, setShowWorkspaceBenchmark] = useState(false);
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
      const currentSubjectName = typeof selectedSubject === 'object'
        ? (selectedSubject?.name || selectedSubject?.id || 'Mathematics')
        : (selectedSubject || 'Mathematics');
      const activeTopicTitle = typeof activeTopic === 'object' ? (activeTopic?.name || '') : (activeTopic || '');

      return (
        <div className="flex flex-col min-h-screen bg-slate-50 text-slate-900">
          <SubjectShelf
            currentSubject={currentSubjectName}
            currentGrade={selectedGrade || '7'}
            onSelectSubject={(subj) => {
              if (setSelectedSubject) setSelectedSubject(subj);
              if (setActiveTopic) setActiveTopic(null);
              if (setView) setView('curriculum_helper');
            }}
          />

          {/* Clean White Top Workspace Navigation Bar */}
          <div className="w-full bg-white border-b border-slate-200 px-4 py-2.5 shadow-xs">
            <div className="max-w-7xl mx-auto flex items-center justify-between gap-4 flex-wrap">
              <div className="flex items-center gap-3">
                <button
                  onClick={() => {
                    if (setActiveTopic) setActiveTopic(null);
                    if (setView) setView('curriculum_helper');
                  }}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-slate-200 bg-white text-slate-700 hover:bg-slate-100 hover:text-slate-900 transition-colors text-xs font-semibold shadow-2xs"
                >
                  <ChevronLeft className="h-4 w-4" />
                  <span>Back to Topics</span>
                </button>

                <div className="h-4 w-px bg-slate-200 hidden sm:block" />

                <div className="flex items-center gap-2 text-xs">
                  <span className="px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-700 font-bold border border-indigo-100">
                    Grade {selectedGrade || '7'} {currentSubjectName}
                  </span>
                  {activeTopicTitle && (
                    <span className="text-slate-600 font-medium hidden md:inline">
                      • {activeTopicTitle}
                    </span>
                  )}
                </div>
              </div>

              <div className="flex items-center gap-2">
                <button
                  onClick={() => setShowWorkspaceBenchmark(true)}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold transition-all shadow-xs"
                >
                  <BarChart2 className="h-3.5 w-3.5" />
                  <span>Diagnostic Test</span>
                </button>
              </div>
            </div>
          </div>

          <div className="flex-1 p-2 sm:p-4 max-w-7xl mx-auto w-full">
            <Workspace
              topic={activeTopic?.name || activeTopic}
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
          </div>

          {showWorkspaceBenchmark && (
            <MicroBenchmarkModal
              isOpen={showWorkspaceBenchmark}
              topic={activeTopicTitle || 'General Assessment'}
              subject={currentSubjectName}
              grade={selectedGrade || '7'}
              currentUser={currentUser}
              onComplete={(answers) => {
                setShowWorkspaceBenchmark(false);
              }}
              onClose={() => {
                setShowWorkspaceBenchmark(false);
              }}
            />
          )}
        </div>
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
