import { buildApiUrl } from '../../../../utils/apiBaseUrl';
import { useState, useCallback } from 'react';

export const useGrade8EmsMarking = (config = {}) => {
    const { apiUrl = buildApiUrl('/api/grade8_ems/mark') } = config;

    const [markingMode, setMarkingMode] = useState('practice');
    const [markingResults, setMarkingResults] = useState(null);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [markingError, setMarkingError] = useState(null);
    const [submittedAnswers, setSubmittedAnswers] = useState({});

    const toggleMarkingMode = useCallback(() => {
        setMarkingMode((prev) => {
            if (prev === 'practice') {
                setSubmittedAnswers({});
                setMarkingResults(null);
                setMarkingError(null);
                return 'marking_active';
            }
            return 'practice';
        });
    }, []);

    const registerAnswer = useCallback((questionId, answer) => {
        if (!questionId) return;
        setSubmittedAnswers(prev => ({
            ...prev,
            [questionId]: answer
        }));
    }, []);

    const submitAssessment = useCallback(async (questionsList) => {
        if (!questionsList || questionsList.length === 0) {
            setMarkingError('No questions to mark.');
            return;
        }

        setIsSubmitting(true);
        setMarkingError(null);

        try {
            const payload = {
                questions: questionsList,
                answers: submittedAnswers
            };

            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            if (data) {
                setMarkingResults(data);
                setMarkingMode('marking_submitted');
            } else {
                throw new Error('Invalid response format from server.');
            }
        } catch (err) {
            console.error('Error submitting assessment:', err);
            setMarkingError(err.message || 'Failed to submit assessment.');
        } finally {
            setIsSubmitting(false);
        }
    }, [apiUrl, submittedAnswers]);

    const getFeedbackForQuestion = useCallback((questionId) => {
        if (markingMode !== 'marking_submitted' || !markingResults) return null;
        const res = markingResults.results?.[questionId];
        if (!res) return null;

        return {
            kind: res.is_correct ? 'success' : 'error',
            message: `Score: ${res.score}/${res.max_score}. ${res.feedback}`,
            score: res.score,
            maxScore: res.max_score
        };
    }, [markingMode, markingResults]);

    return {
        markingMode,
        setMarkingMode,
        toggleMarkingMode,
        isMarkingActive: markingMode === 'marking_active',
        isMarkingSubmitted: markingMode === 'marking_submitted',
        isPracticeMode: markingMode === 'practice',

        submittedAnswers,
        registerAnswer,

        submitAssessment,
        isSubmitting,
        markingResults,
        markingError,

        getFeedbackForQuestion
    };
};
