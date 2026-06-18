import { useState } from 'react';

export const useAssignmentsPractice = () => {
    const [pendingAssignments, setPendingAssignments] = useState([]);
    const [activeAssignment, setActiveAssignment] = useState(null);
    const [activeQuestionId, setActiveQuestionId] = useState(null);
    const [practiceQuestions, setPracticeQuestions] = useState([]);

    return {
        pendingAssignments,
        setPendingAssignments,
        activeAssignment,
        setActiveAssignment,
        activeQuestionId,
        setActiveQuestionId,
        practiceQuestions,
        setPracticeQuestions
    };
};
