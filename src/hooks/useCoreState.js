import { useState } from 'react';

 const getInitialShowSplash = () => {
     if (typeof window === 'undefined') {
         return true;
     }

     try {
         const hasSeenSplashThisSession = window.sessionStorage.getItem('fundileSplashSeen') === 'true';

         if (hasSeenSplashThisSession) {
             return false;
         }

         window.sessionStorage.setItem('fundileSplashSeen', 'true');
         return true;
     } catch {
         return true;
     }
 };

export const useCoreState = () => {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');
    const [showSplash, setShowSplash] = useState(getInitialShowSplash);
    const [showLandingPage, setShowLandingPage] = useState(false);
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
