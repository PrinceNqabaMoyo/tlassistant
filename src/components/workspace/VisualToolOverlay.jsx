import React, { useState } from 'react';
import { X, Maximize2, Minimize2, Send } from 'lucide-react';

const VisualToolOverlay = ({ 
    isVisible, 
    onClose, 
    title, 
    children, 
    onSendToWorkspace,
    workspaceData = null,
    isFullScreen = false,
    onToggleFullScreen
}) => {
    const [isMinimized, setIsMinimized] = useState(false);

    if (!isVisible) return null;

    const handleSendToWorkspace = () => {
        if (onSendToWorkspace && workspaceData) {
            onSendToWorkspace(workspaceData);
        }
    };

    const overlayClasses = isFullScreen 
        ? "fixed inset-0 bg-white z-50"
        : isMinimized
        ? "fixed bottom-4 right-4 w-96 h-16 bg-white border border-gray-200 rounded-lg shadow-lg z-40"
        : "fixed bottom-4 right-4 w-96 h-96 bg-white border border-gray-200 rounded-lg shadow-lg z-40";

    const contentClasses = isFullScreen 
        ? "h-full flex flex-col"
        : isMinimized
        ? "h-full flex items-center px-4"
        : "h-full flex flex-col";

    return (
        <div className={overlayClasses}>
            {/* Header */}
            <div className="flex items-center justify-between p-3 border-b border-gray-200 bg-gray-50">
                <h3 className="text-sm font-semibold text-gray-800 truncate">{title}</h3>
                <div className="flex items-center space-x-1">
                    {workspaceData && (
                        <button
                            onClick={handleSendToWorkspace}
                            className="p-1 text-green-600 hover:text-green-700 hover:bg-green-50 rounded"
                            title="Send to workspace"
                        >
                            <Send className="h-4 w-4" />
                        </button>
                    )}
                    <button
                        onClick={onToggleFullScreen}
                        className="p-1 text-gray-600 hover:text-gray-700 hover:bg-gray-100 rounded"
                        title={isFullScreen ? "Exit full screen" : "Full screen"}
                    >
                        {isFullScreen ? <Minimize2 className="h-4 w-4" /> : <Maximize2 className="h-4 w-4" />}
                    </button>
                    {!isFullScreen && (
                        <button
                            onClick={() => setIsMinimized(!isMinimized)}
                            className="p-1 text-gray-600 hover:text-gray-700 hover:bg-gray-100 rounded"
                            title={isMinimized ? "Expand" : "Minimize"}
                        >
                            <Minimize2 className="h-4 w-4" />
                        </button>
                    )}
                    <button
                        onClick={onClose}
                        className="p-1 text-gray-600 hover:text-gray-700 hover:bg-gray-100 rounded"
                        title="Close"
                    >
                        <X className="h-4 w-4" />
                    </button>
                </div>
            </div>

            {/* Content */}
            {!isMinimized && (
                <div className={contentClasses}>
                    <div className="flex-1 overflow-auto">
                        {children}
                    </div>
                </div>
            )}
        </div>
    );
};

export default VisualToolOverlay;
