import { useState } from 'react';

export const useCoreState = () => {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');
    const hasSeenSplash = typeof window !== 'undefined' && window.sessionStorage.getItem('fundileSeenSplash') === 'true';
    const [showSplash, setShowSplash] = useState(!hasSeenSplash);
    const [showLandingPage, setShowLandingPage] = useState(hasSeenSplash);
    const [chatRoomId, setChatRoomId] = useState(null);
    const [chatPermissionsAvailable, setChatPermissionsAvailable] = useState(true);
    const [messages, setMessages] = useState([]);

    return {
        loading,
        setLoading,
        message,
        setMessage,
        showSplash,
        setShowSplash,
        showLandingPage,
        setShowLandingPage,
        chatRoomId,
        setChatRoomId,
        chatPermissionsAvailable,
        setChatPermissionsAvailable,
        messages,
        setMessages
    };
};
