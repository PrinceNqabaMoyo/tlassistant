import { useCallback, useMemo, useState } from 'react';

export const useGrade10BusinessStudiesMarking = (config = {}) => {
    const { buildApiUrl, apiUrl } = config;
    const resolvedApiUrl = useMemo(() => {
        if (typeof buildApiUrl === 'function') {
            return buildApiUrl('/api/business-studies/grade10/mark');
        }
        return apiUrl;
    }, [buildApiUrl, apiUrl]);

    const [status, setStatus] = useState('idle');
    const [scoreState, setScoreState] = useState({ totalScore: 0, maxScore: 0 });
    const [error, setError] = useState(null);

    const resetMarking = useCallback(() => {
        setStatus('idle');
        setScoreState({ totalScore: 0, maxScore: 0 });
        setError(null);
    }, []);

    const markQuestions = useCallback(async (questions, answers) => {
        if (!questions || questions.length === 0) {
            return null;
        }

        setStatus('marking_active');
        setError(null);

        try {
            const response = await fetch(resolvedApiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    questions,
                    answers,
                }),
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.error || `HTTP error ${response.status}`);
            }

            const data = await response.json();
            setScoreState({
                totalScore: data.total_score || 0,
                maxScore: data.max_score || 0,
            });
            setStatus('marking_submitted');
            return data.results || null;
        } catch (err) {
            console.error('Failed to mark Grade 10 Business Studies questions:', err);
            setError(err.message || 'Failed to mark questions.');
            setStatus('idle');
            return null;
        }
    }, [resolvedApiUrl]);

    return {
        status,
        scoreState,
        error,
        resetMarking,
        markQuestions,
    };
};
