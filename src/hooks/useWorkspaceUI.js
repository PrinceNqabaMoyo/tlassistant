import { useState, useRef } from 'react';

export const useWorkspaceUI = () => {
    const [isKeypadVisible, setIsKeypadVisible] = useState(false);
    const [activeEditableRef, setActiveEditableRef] = useState(null);
    const [workspaceMode, setWorkspaceMode] = useState('freeform');
    const freeformWorkAreaRef = useRef(null);

    return {
        isKeypadVisible,
        setIsKeypadVisible,
        activeEditableRef,
        setActiveEditableRef,
        workspaceMode,
        setWorkspaceMode,
        freeformWorkAreaRef
    };
};
