import React, { useState } from 'react';
import { Maximize2 } from 'lucide-react';
import FullScreenModal from './FullScreenModal';

const withFullScreen = (WrappedComponent, componentName) => {
    return function EnhancedComponent(props) {
        const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
        const [isFullScreen, setIsFullScreen] = useState(false);

        const handleToggleFullScreen = () => {
            setIsFullScreen(!isFullScreen);
        };

        const handleOpenFullScreen = () => {
            setIsFullScreenOpen(true);
        };

        const handleCloseFullScreen = () => {
            setIsFullScreenOpen(false);
        };

        // Extract the parameter controls from the original component
        const extractParameterPanel = () => {
            // This will be overridden by each component
            return null;
        };

        return (
            <>
                {/* Original Component with Full Screen Button */}
                <div className="relative">
                    <WrappedComponent {...props} />
                    
                    {/* Full Screen Button */}
                    <button
                        onClick={handleOpenFullScreen}
                        className="absolute top-4 right-4 p-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md shadow-lg transition-colors z-10"
                        title="Open Full Screen Mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>

                {/* Full Screen Modal */}
                <FullScreenModal
                    isOpen={isFullScreenOpen}
                    onClose={handleCloseFullScreen}
                    title={componentName}
                    onToggleFullScreen={handleToggleFullScreen}
                    isFullScreen={isFullScreen}
                    parameterPanel={
                        <div className="space-y-4">
                            <h3 className="font-semibold text-gray-800 mb-4">Parameters</h3>
                            {/* The parameter panel will be passed as a prop */}
                            {props.parameterPanel || extractParameterPanel()}
                        </div>
                    }
                >
                    <div className="h-full flex items-center justify-center">
                        <WrappedComponent {...props} />
                    </div>
                </FullScreenModal>
            </>
        );
    };
};

export default withFullScreen;
