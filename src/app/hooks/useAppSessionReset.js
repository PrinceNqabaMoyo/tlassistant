import { useCallback } from 'react';
import { getCurriculumRootNavigationStack } from '../utils/navigationReset';

export const useAppSessionReset = ({
  handleLogout,
  resetTopLevelRouting,
  setMessage,
  setShowSplash,
  setView,
  setNavigationStack,
  setSelectedCurriculumKey,
  setSelectedGrade,
  setSelectedSubject,
  setActiveTopic,
  setActiveAssignment,
  setPracticeQuestions,
  setPendingAssignments,
  setSelectedFreeformTopic,
  setCurrentProblemThreadId,
  setChatHistory,
  setFreeformAnswer,
}) => {
  const handleAppLogout = useCallback(async () => {
    const result = await handleLogout();

    if (!result?.success) {
      setMessage(result?.error || 'Failed to sign out. Please try again.');
      return result;
    }

    resetTopLevelRouting();
    setShowSplash(false);
    setView('curriculum');
    setNavigationStack(getCurriculumRootNavigationStack());
    setSelectedCurriculumKey(null);
    setSelectedGrade(null);
    setSelectedSubject(null);
    setActiveTopic(null);
    setActiveAssignment(null);
    setPracticeQuestions([]);
    setPendingAssignments([]);
    setSelectedFreeformTopic(null);
    setCurrentProblemThreadId(null);
    setChatHistory([]);
    setFreeformAnswer('');

    return result;
  }, [
    handleLogout,
    resetTopLevelRouting,
    setMessage,
    setShowSplash,
    setView,
    setNavigationStack,
    setSelectedCurriculumKey,
    setSelectedGrade,
    setSelectedSubject,
    setActiveTopic,
    setActiveAssignment,
    setPracticeQuestions,
    setPendingAssignments,
    setSelectedFreeformTopic,
    setCurrentProblemThreadId,
    setChatHistory,
    setFreeformAnswer,
  ]);

  return {
    handleAppLogout,
  };
};
