import { useCallback } from 'react';
import { deleteDoc, doc, serverTimestamp, setDoc } from 'firebase/firestore';
import { getSubjectKeyFromSelection } from '../utils/subjectKeys';

export const useFreeformProblemFlow = ({
  addViewToStack,
  allCurricula,
  chatHistories,
  currentProblemThreadId,
  currentUser,
  dbService,
  getAgentResponse,
  loading,
  selectedCurriculumKey,
  selectedFreeformTopic,
  selectedGrade,
  selectedSubject,
  setChatHistories,
  setCurrentProblemThreadId,
  setFreeformAnswer,
  setLoading,
  setMessage,
  setSelectedCurriculumKey,
  setSelectedFreeformTopic,
  setSelectedGrade,
  setSelectedSubject,
  setWorkspaceMode,
}) => {
  const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';

  const getSubjectKey = useCallback(() => {
    return getSubjectKeyFromSelection({
      selectedCurriculumKey,
      selectedGrade,
      selectedSubject,
    });
  }, [selectedCurriculumKey, selectedGrade, selectedSubject]);

  const saveSuccessfulProblem = useCallback(async (question, answer, topic, subject, grade, userId) => {
    if (!dbService) {
      console.error('Database service not available for saving successful problem.');
      return;
    }

    const problemId = `solved-${Date.now()}`;
    const docRef = doc(dbService, 'artifacts', appId, 'users', userId, 'solved_freeform_problems', problemId);
    const retentionDate = new Date();
    retentionDate.setDate(retentionDate.getDate() + 90);

    try {
      await setDoc(docRef, {
        question,
        answer,
        topic,
        subject,
        grade,
        timestamp: serverTimestamp(),
        retentionDate,
        isSolved: true,
      });
      console.log('Successful problem saved:', problemId);
    } catch (e) {
      console.error('Error saving successful problem: ', e);
    }
  }, [appId, dbService]);

  const saveStrugglingProblem = useCallback(async (threadId, history, topic, subject, grade, userId) => {
    if (!dbService) {
      console.error('Database service not available for saving struggling problem.');
      return;
    }

    const docRef = doc(dbService, 'artifacts', appId, 'users', userId, 'struggling_problems', threadId);

    try {
      await setDoc(docRef, {
        threadId,
        chatHistory: history,
        topic,
        subject,
        grade,
        lastUpdated: serverTimestamp(),
        isSolved: false,
      }, { merge: true });
      console.log('Struggling problem saved/updated:', threadId);
    } catch (e) {
      console.error('Error saving struggling problem: ', e);
    }
  }, [appId, dbService]);

  const handleMarkStrugglingProblemSolved = useCallback(async (threadId) => {
    if (!dbService || !currentUser) {
      console.error('Database or user not available for marking problem as solved.');
      setMessage('Error: Could not mark problem as solved. Please try again.');
      return;
    }

    const docRef = doc(dbService, 'artifacts', appId, 'users', currentUser.uid, 'struggling_problems', threadId);

    try {
      await deleteDoc(docRef);
      console.log(`Struggling problem with threadId ${threadId} marked as solved and deleted.`);
      setMessage('Problem marked as solved and removed from your struggling problems.');
      if (currentProblemThreadId === threadId) {
        setCurrentProblemThreadId(null);
      }
    } catch (e) {
      console.error('Error marking struggling problem as solved: ', e);
      setMessage('Failed to mark problem as solved. Please try again.');
    }
  }, [appId, currentProblemThreadId, currentUser, dbService, setCurrentProblemThreadId, setMessage]);

  const addQuestionToChat = useCallback((question) => {
    const subjectKey = getSubjectKey();
    const newQuestion = {
      id: Date.now(),
      question,
      answer: null,
      loading: true,
      timestamp: new Date().toISOString(),
      topic: selectedFreeformTopic,
      threadId: currentProblemThreadId || `thread-${Date.now()}`,
      isSuccessful: false,
    };

    setChatHistories((prevHistories) => {
      const currentHistory = prevHistories[subjectKey] || [];
      const updatedHistory = [...currentHistory, newQuestion];
      return {
        ...prevHistories,
        [subjectKey]: updatedHistory,
      };
    });

    return newQuestion.id;
  }, [currentProblemThreadId, getSubjectKey, selectedFreeformTopic, setChatHistories]);

  const updateAnswerInChat = useCallback((questionId, answer, isCorrect = false) => {
    const subjectKey = getSubjectKey();

    setChatHistories((prevHistories) => {
      const currentHistory = prevHistories[subjectKey] || [];
      let updatedHistory = currentHistory.map((message) =>
        message.id === questionId ? { ...message, answer, loading: false, isSuccessful: isCorrect } : message
      );

      const currentThreadIdForQuestion = updatedHistory.find((msg) => msg.id === questionId)?.threadId;
      const currentThreadHistory = updatedHistory.filter((msg) => msg.threadId === currentThreadIdForQuestion);
      const maxHistoryLength = 10;
      let truncatedThreadHistory = currentThreadHistory;

      if (currentThreadHistory.length > maxHistoryLength) {
        truncatedThreadHistory = currentThreadHistory.slice(-maxHistoryLength);
      }

      updatedHistory = updatedHistory.filter((msg) => msg.threadId !== currentThreadIdForQuestion).concat(truncatedThreadHistory);

      if (isCorrect) {
        setCurrentProblemThreadId(null);
      } else {
        setCurrentProblemThreadId(currentThreadIdForQuestion);
      }

      return {
        ...prevHistories,
        [subjectKey]: updatedHistory,
      };
    });
  }, [getSubjectKey, setChatHistories, setCurrentProblemThreadId]);

  const handleStrugglingProblem = useCallback((problemItem) => {
    if (!currentProblemThreadId) {
      setCurrentProblemThreadId(`thread-${Date.now()}`);
    } else {
      setCurrentProblemThreadId(problemItem.threadId);
    }
    setMessage('Problem marked as struggling. You can continue the conversation or revisit it later.');
  }, [currentProblemThreadId, setCurrentProblemThreadId, setMessage]);

  const handleSendFreeformQuery = useCallback(async (queryText) => {
    if (!queryText.trim() || loading || !selectedFreeformTopic || !currentUser || !dbService) {
      console.warn('Cannot send query: Missing input, loading, topic, user, or dbService.');
      return;
    }

    setLoading(true);
    const question = queryText;
    const questionId = addQuestionToChat(question);
    setFreeformAnswer('');

    try {
      const subjectKey = getSubjectKey();
      const currentChatHistoryForRAG = [...(chatHistories[subjectKey] || [])];
      const newAIAnswer = await getAgentResponse(question, currentChatHistoryForRAG.map((item) => ({
        role: 'user',
        content: item.question,
      })));

      const isCorrect = newAIAnswer.toLowerCase().includes('correct');
      updateAnswerInChat(questionId, newAIAnswer, isCorrect);

      const updatedLocalChatHistory = chatHistories[subjectKey] || [];
      const threadIdForSaving = updatedLocalChatHistory.find((msg) => msg.id === questionId)?.threadId;

      if (isCorrect) {
        saveSuccessfulProblem(
          question,
          newAIAnswer,
          selectedFreeformTopic,
          selectedSubject?.name,
          selectedGrade,
          currentUser.uid
        );
        setCurrentProblemThreadId(null);
      } else {
        const fullThreadHistory = updatedLocalChatHistory.filter((msg) => msg.threadId === threadIdForSaving);
        saveStrugglingProblem(
          threadIdForSaving,
          fullThreadHistory,
          selectedFreeformTopic,
          selectedSubject?.name,
          selectedGrade,
          currentUser.uid
        );
        setCurrentProblemThreadId(threadIdForSaving);
      }
    } catch (error) {
      console.error('Error sending query to AI or saving problem:', error);
      updateAnswerInChat(questionId, 'Error fetching AI response or saving problem.');
    } finally {
      setLoading(false);
    }
  }, [addQuestionToChat, chatHistories, currentUser, dbService, getAgentResponse, getSubjectKey, loading, saveStrugglingProblem, saveSuccessfulProblem, selectedFreeformTopic, selectedGrade, selectedSubject, setCurrentProblemThreadId, setFreeformAnswer, setLoading, updateAnswerInChat]);

  const handleContinueProblem = useCallback((problem) => {
    setSelectedCurriculumKey(problem.curriculumKey || 'all');
    setSelectedGrade(problem.grade);

    let subjectObject = null;
    for (const key in allCurricula) {
      const curriculum = allCurricula[key];
      const foundSubject = curriculum.subjects.find((s) => s.name === problem.subject);
      if (foundSubject) {
        subjectObject = foundSubject;
        break;
      }
    }

    setSelectedSubject(subjectObject);
    setSelectedFreeformTopic(problem.topic);
    setCurrentProblemThreadId(problem.threadId);

    const problemSubjectKey = `${problem.curriculumKey || 'all'}_${problem.grade || 'all'}_${problem.subject || 'all'}`;
    setChatHistories((prevHistories) => ({
      ...prevHistories,
      [problemSubjectKey]: problem.chatHistory || [],
    }));

    setWorkspaceMode('freeform');
    addViewToStack('workspace', `Continuing: ${problem.topic}`, {
      view: 'workspace',
      curriculumKey: problem.curriculumKey,
      grade: problem.grade,
      subject: problem.subject,
      topic: problem.topic,
      threadId: problem.threadId,
    });
    setMessage(`Loaded problem: ${problem.topic}. You can continue the conversation.`);
  }, [addViewToStack, allCurricula, setChatHistories, setCurrentProblemThreadId, setMessage, setSelectedCurriculumKey, setSelectedFreeformTopic, setSelectedGrade, setSelectedSubject, setWorkspaceMode]);

  return {
    addQuestionToChat,
    handleContinueProblem,
    handleMarkStrugglingProblemSolved,
    handleSendFreeformQuery,
    handleStrugglingProblem,
    updateAnswerInChat,
  };
};
