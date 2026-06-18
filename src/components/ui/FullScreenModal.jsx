import React from 'react';
import { X, Maximize2, Minimize2 } from 'lucide-react';

const FullScreenModal = ({ 
    isOpen, 
    onClose, 
    title, 
    children, 
    parameterPanel,
    onToggleFullScreen,
    isFullScreen = false,
    hideFullScreenToggle = false 
}) => {
    if (!isOpen) return null;

    // Always start in full screen mode, skip intermediate state
    const alwaysFullScreen = true;

    return (
        <div className="fixed inset-0 z-50 bg-white">
            <div className="bg-white w-full h-full flex flex-col">
                {/* Header */}
                <div className="flex items-center justify-between p-4 border-b border-gray-200 bg-gray-50">
                    <h2 className="text-xl font-semibold text-gray-800">{title}</h2>
                    <div className="flex items-center space-x-2">
                        {/* Only show minimize button, no expansion button */}
                        <button
                            onClick={onClose}
                            className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-200 rounded-md transition-colors"
                            title="Minimize"
                        >
                            <Minimize2 size={20} />
                        </button>
                        <button
                            onClick={onClose}
                            className="p-2 text-gray-600 hover:text-red-600 hover:bg-gray-200 rounded-md transition-colors"
                            title="Close"
                        >
                            <X size={20} />
                        </button>
                    </div>
                </div>

                {/* Content */}
                <div className="flex flex-1 overflow-hidden">
                    {/* Left Panel - Parameters */}
                    <div className="w-80 bg-gray-50 border-r border-gray-200 overflow-y-auto">
                        <div className="p-4">
                            {parameterPanel}
                        </div>
                    </div>

                    {/* Right Panel - Visual Component */}
                    <div className="flex-1 bg-white overflow-auto">
                        <div className="p-4 h-full">
                            {children}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default FullScreenModal;
