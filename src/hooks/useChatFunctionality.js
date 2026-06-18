import { useState } from 'react';

export const useChatFunctionality = () => {
    const [chatInput, setChatInput] = useState(''); // For general chat input
    const [isChatLoading, setIsChatLoading] = useState(false); // For general chat loading
    const [freeformAnswer, setFreeformAnswer] = useState(''); // User's input in freeform workspace
    const [chatHistories, setChatHistories] = useState({}); // In-memory cache of chat histories by subjectKey
    const [chatHistory, setChatHistory] = useState([]); // This state is now redundant as it's passed from chatHistories[subjectKey]

    return {
        chatInput,
        setChatInput,
        isChatLoading,
        setIsChatLoading,
        freeformAnswer,
        setFreeformAnswer,
        chatHistories,
        setChatHistories,
        chatHistory,
        setChatHistory
    };
};
