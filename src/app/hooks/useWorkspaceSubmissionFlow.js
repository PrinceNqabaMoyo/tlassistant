import { buildApiUrl } from '../../utils/apiBaseUrl';
import { useCallback } from 'react';
import { addDoc, collection, serverTimestamp } from 'firebase/firestore';

export const useWorkspaceSubmissionFlow = ({
  activeAssignment,
  activeEditableRef,
  activeTopic,
  addViewToStack,
  allCurricula,
  chatHistory,
  currentUser,
  dbService,
  getAgentResponse,
  numbersMatchForCurrency,
  parseFlexibleNumber,
  practiceQuestions,
  processMathematicalContent,
  selectedGrade,
  selectedSubject,
  setActiveAssignment,
  setActiveEditableRef,
  setActiveTopic,
  setChatHistory,
  setLoading,
  setMessage,
  setPracticeQuestions,
  setSelectedCurriculumKey,
  setSelectedGrade,
  setSelectedSubject,
  setView,
  setWorkspaceMode,
  shouldUseMathStructure,
}) => {
  const handleToggleMathStructure = useCallback((questionId) => {
    setPracticeQuestions((prev) => prev.map((q) => {
      if (q.id === questionId) {
        const needsMathStructure = shouldUseMathStructure(selectedSubject?.name, q.feedback.content);
        return {
          ...q,
          feedback: {
            ...q.feedback,
            mathStructureEnabled: !q.feedback.mathStructureEnabled,
            autoDetected: needsMathStructure,
          },
        };
      }
      return q;
    }));
  }, [selectedSubject, setPracticeQuestions, shouldUseMathStructure]);

  const handleAttempt = useCallback((questionId, ref) => {
    setPracticeQuestions((prev) => {
      const updatedQuestions = prev.map((q) => q.id === questionId ? { ...q, isAttempted: true } : q);
      const question = updatedQuestions.find((q) => q.id === questionId);
      if (question && question.expected_answer_type === 'text') setActiveEditableRef(ref);
      else setActiveEditableRef(null);
      return updatedQuestions;
    });
  }, [setActiveEditableRef, setPracticeQuestions]);

  const handleAnswerInput = useCallback((questionId, answer) => {
    setPracticeQuestions((prev) => prev.map((q) => q.id === questionId ? { ...q, answer } : q));
  }, [setPracticeQuestions]);

  const evaluateDeterministic = useCallback((questionToSubmit, studentAnswer) => {
    const qType = questionToSubmit.question_type || questionToSubmit.expected_answer_type;

    if (qType === 'mcq') {
      const correctIdx = questionToSubmit.correct_index;
      const studentIdx = typeof studentAnswer === 'number' ? studentAnswer : parseInt(studentAnswer, 10);
      const isCorrect = studentIdx === correctIdx;
      const correctOption = questionToSubmit.options?.[correctIdx] || '';
      return {
        is_correct: isCorrect,
        score: isCorrect ? 100 : 0,
        feedback: isCorrect
          ? `Correct! ${questionToSubmit.explanation || ''}`
          : `Incorrect. The correct answer is: "${correctOption}". ${questionToSubmit.explanation || ''}`,
      };
    }

    if (qType === 'calc' || questionToSubmit.expected_answer_type === 'number') {
      const correctVal = parseFloat(questionToSubmit.correct_value);
      const studentVal = parseFlexibleNumber(studentAnswer);
      const unit = questionToSubmit.unit || '';
      const allowRoundedCurrency = String(unit).toUpperCase().includes('R');
      const isCorrect = Number.isFinite(correctVal) && studentVal !== null && (
        allowRoundedCurrency
          ? numbersMatchForCurrency(studentVal, correctVal)
          : Math.abs(studentVal - correctVal) <= 0.01
      );
      return {
        is_correct: isCorrect,
        score: isCorrect ? 100 : 0,
        feedback: isCorrect
          ? `Correct! The answer is ${unit}${correctVal.toFixed(2)}.`
          : `Incorrect. The correct answer is ${unit}${correctVal.toFixed(2)}. You answered ${unit}${studentVal === null ? studentAnswer : studentVal.toFixed(2)}.`,
      };
    }

    if (qType === 'table_wordbank') {
      const correctMap = questionToSubmit.correct_map || {};
      let totalCells = 0;
      let correctCells = 0;
      const mistakes = [];

      for (const [rowIdx, cols] of Object.entries(correctMap)) {
        for (const [colIdx, expectedId] of Object.entries(cols)) {
          totalCells++;
          const studentPlaced = studentAnswer?.[rowIdx]?.[colIdx];
          if (studentPlaced === expectedId) {
            correctCells++;
          } else {
            mistakes.push(`Row ${parseInt(rowIdx) + 1}, Column ${parseInt(colIdx) + 1}`);
          }
        }
      }

      const score = totalCells > 0 ? Math.round((correctCells / totalCells) * 100) : 0;
      const isCorrect = score >= 50;
      return {
        is_correct: isCorrect,
        score,
        feedback: score === 100
          ? 'Excellent! All items placed correctly.'
          : `You got ${correctCells} out of ${totalCells} correct (${score}%).${mistakes.length > 0 ? ` Check: ${mistakes.join(', ')}.` : ''}`,
      };
    }

    return null;
  }, [numbersMatchForCurrency, parseFlexibleNumber]);

  const handleSubmit = useCallback(async (questionId, questionText, expectedAnswerType, studentAnswer, questionSolution, currentQuestionBlockRef) => {
    const questionToSubmit = practiceQuestions.find((q) => q.id === questionId);
    if (!questionToSubmit) return;

    if (activeAssignment?.feedbackMode !== 'instant') {
      setPracticeQuestions((prev) => prev.map((q) => q.id === questionId ? { ...q, isSubmitted: true } : q));
      return;
    }

    const deterministicResult = evaluateDeterministic(questionToSubmit, studentAnswer);
    if (deterministicResult) {
      const feedbackContent = deterministicResult.feedback;
      setPracticeQuestions((prev) => prev.map((q) =>
        q.id === questionId ? {
          ...q,
          isSubmitted: true,
          feedback: {
            content: feedbackContent,
            is_correct: deterministicResult.is_correct,
            score: deterministicResult.score,
            mathStructureEnabled: false,
            autoDetected: false,
            processedContent: feedbackContent,
          },
        } : q
      ));
      setChatHistory((prev) => [...prev,
        { role: 'user', content: `Student's answer for "${questionText}": ${typeof studentAnswer === 'object' ? JSON.stringify(studentAnswer) : studentAnswer}` },
        { role: 'ai', content: feedbackContent },
      ]);
      return;
    }

    setLoading(true);

    let userMessageContent;
    if (typeof studentAnswer === 'object' && studentAnswer !== null) {
      userMessageContent = `Student's structured answer for "${questionText}":\n\`\`\`json\n${JSON.stringify(studentAnswer, null, 2)}\n\`\`\``;
    } else {
      userMessageContent = `Student's answer for "${questionText}":\n${studentAnswer}`;
    }
    setChatHistory((prev) => [...prev, { role: 'user', content: userMessageContent }]);

    const loadingMessageId = `loading-feedback-${Date.now()}`;
    setChatHistory((prev) => [...prev, { id: loadingMessageId, role: 'ai', content: 'Evaluating...', isLoading: true }]);

    try {
      const sampleAnswer = questionToSubmit.sample_answer || questionSolution || '';
      const evalResponse = await fetch(buildApiUrl('/api/evaluate-typed'), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question_prompt: questionText,
          sample_answer: sampleAnswer,
          student_answer: typeof studentAnswer === 'object' ? JSON.stringify(studentAnswer) : studentAnswer,
          subject: selectedSubject?.name || '',
          grade: selectedGrade || '',
        }),
      });

      let feedbackContent;
      let isCorrect = false;
      let score = 0;

      if (evalResponse.ok) {
        const evalData = await evalResponse.json();
        const evaluation = evalData.evaluation || {};
        isCorrect = evaluation.is_correct || false;
        score = evaluation.score || 0;
        feedbackContent = evaluation.feedback || 'No feedback available.';
        if (evaluation.key_points_hit?.length > 0) {
          feedbackContent += '\n\nKey points covered: ' + evaluation.key_points_hit.join('; ');
        }
        if (evaluation.key_points_missed?.length > 0) {
          feedbackContent += '\nPoints to improve: ' + evaluation.key_points_missed.join('; ');
        }
        feedbackContent += `\n\nScore: ${score}/100`;
      } else {
        const payload = {
          question: questionText,
          expected_answer_type: expectedAnswerType,
          student_answer: studentAnswer,
          solution: questionSolution,
          context: {
            subject: selectedSubject?.name,
            grade: selectedGrade,
            topic: activeTopic?.name,
            document_type: 'question_feedback',
          },
        };
        feedbackContent = await getAgentResponse(payload, chatHistory);
      }

      setPracticeQuestions((prev) => prev.map((q) =>
        q.id === questionId ? {
          ...q,
          isSubmitted: true,
          feedback: {
            content: feedbackContent,
            is_correct: isCorrect,
            score,
            mathStructureEnabled: shouldUseMathStructure(selectedSubject?.name, feedbackContent),
            autoDetected: shouldUseMathStructure(selectedSubject?.name, feedbackContent),
            processedContent: processMathematicalContent(feedbackContent, selectedSubject),
          },
        } : q
      ));

      setChatHistory((prev) => prev.map((msg) =>
        msg.id === loadingMessageId ? { ...msg, content: feedbackContent, isLoading: false } : msg
      ));

      if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
        window.MathJax.typesetPromise();
      }
    } catch (error) {
      console.error('Error getting feedback:', error);
      setChatHistory((prev) => prev.map((msg) =>
        msg.id === loadingMessageId ? { ...msg, content: 'Error: Could not get feedback.', isLoading: false } : msg
      ));
      setPracticeQuestions((prev) => prev.map((q) =>
        q.id === questionId ? {
          ...q,
          isSubmitted: true,
          feedback: {
            content: 'Error: Failed to get feedback. Please try again.',
            mathStructureEnabled: false,
            autoDetected: false,
            processedContent: 'Error: Failed to get feedback. Please try again.',
          },
        } : q
      ));
    } finally {
      setLoading(false);
    }
  }, [activeAssignment, activeTopic, chatHistory, evaluateDeterministic, getAgentResponse, practiceQuestions, processMathematicalContent, selectedGrade, selectedSubject, setChatHistory, setLoading, setPracticeQuestions, shouldUseMathStructure]);

  const handleMathInput = useCallback((symbol) => {
    const targetElement = activeEditableRef?.current;
    if (targetElement && targetElement.isContentEditable) {
      targetElement.focus();
      if (symbol === 'x²') document.execCommand('insertHTML', false, '<sup>2</sup>');
      else if (symbol === 'x₂') document.execCommand('insertHTML', false, '<sub>2</sub>');
      else document.execCommand('insertHTML', false, symbol);
    }
  }, [activeEditableRef]);

  const handleStartAssignment = useCallback((assignment) => {
    let subjectObject = null;
    let curriculumKey = null;

    for (const key in allCurricula) {
      const curriculum = allCurricula[key];
      const foundSubject = curriculum.subjects.find((s) => s.name === assignment.subject);
      if (foundSubject) {
        subjectObject = foundSubject;
        curriculumKey = key;
        break;
      }
    }

    if (!subjectObject) {
      console.error('Could not find matching subject for assignment:', assignment);
      return;
    }

    setActiveAssignment(assignment);
    setSelectedCurriculumKey(curriculumKey);
    setSelectedSubject(subjectObject);
    setSelectedGrade(assignment.grade);
    setActiveTopic({ name: assignment.topic });

    const questions = assignment.questions.map((q, index) => ({
      id: `q-${Date.now()}-${index}`,
      text: q.question_text,
      table: null,
      shape: null,
      graph: null,
      expected_answer_type: q.question_type,
      solution: q.solution,
      answer: '',
      isSubmitted: false,
      isAttempted: false,
      feedback: null,
    }));
    setPracticeQuestions(questions);
    setWorkspaceMode('practice');

    addViewToStack('workspace', `Assignment: ${assignment.topic}`, {
      value: 'Class Assignment',
      curriculumKey,
      grade: assignment.grade,
      subject: subjectObject,
      topic: { name: assignment.topic },
    });
  }, [addViewToStack, allCurricula, setActiveAssignment, setActiveTopic, setPracticeQuestions, setSelectedCurriculumKey, setSelectedGrade, setSelectedSubject, setWorkspaceMode]);

  const handleAssignmentSubmit = useCallback(async () => {
    if (!activeAssignment || !currentUser) return;
    setLoading(true);

    const answers = practiceQuestions.map((q) => ({
      questionId: q.id,
      questionText: q.text,
      answer: q.answer,
    }));

    try {
      await addDoc(collection(dbService, 'submissions'), {
        studentId: currentUser.uid,
        studentName: currentUser.name,
        assessmentId: activeAssignment.id,
        classId: activeAssignment.classId,
        answers,
        submittedAt: serverTimestamp(),
        status: 'submitted',
      });

      if (activeAssignment.feedbackMode === 'on_submission') {
        setPracticeQuestions((prev) => prev.map((q) => ({
          ...q,
          feedback: {
            content: q.solution,
            mathStructureEnabled: shouldUseMathStructure(selectedSubject?.name, q.solution),
            autoDetected: shouldUseMathStructure(selectedSubject?.name, q.solution),
            processedContent: processMathematicalContent(q.solution, selectedSubject),
          },
        })));
        setMessage('Assignment submitted successfully! Feedback is now available.');
      } else {
        setMessage('Assignment submitted successfully for teacher review!');
        setView('classwork');
        setActiveAssignment(null);
      }
    } catch (e) {
      console.error('Error submitting assignment: ', e);
      setMessage('Failed to submit assignment. Please try again.');
    } finally {
      setLoading(false);
    }
  }, [activeAssignment, currentUser, dbService, practiceQuestions, processMathematicalContent, selectedSubject, setActiveAssignment, setLoading, setMessage, setPracticeQuestions, setView, shouldUseMathStructure]);

  return {
    handleAnswerInput,
    handleAssignmentSubmit,
    handleAttempt,
    handleMathInput,
    handleStartAssignment,
    handleSubmit,
    handleToggleMathStructure,
  };
};
