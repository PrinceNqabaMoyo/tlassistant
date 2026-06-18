import { useState } from 'react';

export const useFreeformTopics = () => {
    const [selectedFreeformTopic, setSelectedFreeformTopic] = useState(null); // This is the topic passed to AI
    const [currentProblemThreadId, setCurrentProblemThreadId] = useState(null); // Tracks the current conversation thread for a problem

    return {
        selectedFreeformTopic,
        setSelectedFreeformTopic,
        currentProblemThreadId,
        setCurrentProblemThreadId
    };
};
