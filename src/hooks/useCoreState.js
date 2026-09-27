import { useState } from 'react';

/**
 * Checks whether the current window was launched as an installed app
 * (Standalone Desktop PWA or Mobile WebAPK) vs a regular web browser tab.
 */
export const isStandaloneApp = () => {
    if (typeof window === 'undefined') return false;
    return (
        window.matchMedia('(display-mode: standalone)').matches ||
        window.navigator.standalone === true ||
        document.referrer.includes('android-app://')
    );
};

const getInitialShowSplash = () => {
    if (typeof window === 'undefined') {
        return false;
    }

    // Do NOT show splash screen on normal browser page visits.
    // Only display splash screen when launched as an installed app (PWA / WebAPK).
    if (!isStandaloneApp()) {
        return false;
    }

    try {
        const hasSeenSplashThisSession = window.sessionStorage.getItem('fundileSplashSeen') === 'true';

        if (hasSeenSplashThisSession) {
            return false;
        }

        window.sessionStorage.setItem('fundileSplashSeen', 'true');
        return true;
    } catch {
        return false;
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
