import React, { useState, useEffect } from 'react';
import MathComponentThumbnail, { hasThumbnail } from './ThumbnailRegistry';

const ThumbnailRenderer = ({ componentId, width = 80, height = 60, fallbackData = null }) => {
    const [thumbnailPriority, setThumbnailPriority] = useState(1);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    // Priority 1: Backend Thumbnail (Future Implementation)
    const renderBackendThumbnail = () => {
        // TODO: Implement backend thumbnail generation
        // For now, this will always fail and move to priority 2
        return null;
    };

    // Priority 2: Frontend Canvas Thumbnail
    const renderFrontendThumbnail = () => {
        if (!hasThumbnail(componentId)) {
            throw new Error('No frontend thumbnail available');
        }
        
        return (
            <MathComponentThumbnail 
                componentId={componentId} 
                width={width} 
                height={height} 
            />
        );
    };

    // Priority 3: Hardcoded Fallback
    const renderFallbackThumbnail = () => {
        if (!fallbackData) {
            // Default fallback if no data provided
            return (
                <div className="bg-white p-2 rounded border border-gray-200">
                    <div className="h-16 bg-gradient-to-r from-gray-100 to-gray-200 rounded flex items-center justify-center text-xs text-gray-800 font-medium">
                        {componentId.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                    </div>
                    <p className="text-xs text-gray-600 mt-1 text-center">Component Preview</p>
                </div>
            );
        }

        // Custom fallback based on provided data
        return (
            <div className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors">
                <div className={`h-16 bg-gradient-to-r ${fallbackData.gradient || 'from-gray-100 to-gray-200'} rounded flex items-center justify-center text-xs ${fallbackData.textColor || 'text-gray-800'} font-medium`}>
                    {fallbackData.title || componentId.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                </div>
                <p className="text-xs text-gray-600 mt-1 text-center">
                    {fallbackData.description || 'Component Preview'}
                </p>
            </div>
        );
    };

    // Priority management logic
    useEffect(() => {
        const tryPriority = async (priority) => {
            setIsLoading(true);
            setError(null);
            
            try {
                let result = null;
                
                switch (priority) {
                    case 1:
                        // Try backend thumbnail
                        result = renderBackendThumbnail();
                        if (result) {
                            setThumbnailPriority(1);
                            return;
                        }
                        // If backend fails, try priority 2
                        throw new Error('Backend thumbnail not implemented yet');
                        
                    case 2:
                        // Try frontend canvas thumbnail
                        result = renderFrontendThumbnail();
                        if (result) {
                            setThumbnailPriority(2);
                            return;
                        }
                        break;
                        
                    case 3:
                        // Fallback thumbnail (always works)
                        result = renderFallbackThumbnail();
                        setThumbnailPriority(3);
                        return;
                        
                    default:
                        throw new Error('Invalid priority level');
                }
            } catch (err) {
                setError(err.message);
                // Move to next priority
                if (priority < 3) {
                    tryPriority(priority + 1);
                } else {
                    // All priorities failed, use fallback
                    setThumbnailPriority(3);
                }
            } finally {
                setIsLoading(false);
            }
        };

        // Start with priority 1
        tryPriority(1);
    }, [componentId, width, height, fallbackData]);

    // Render based on current priority
    const renderCurrentThumbnail = () => {
        switch (thumbnailPriority) {
            case 1:
                return renderBackendThumbnail();
            case 2:
                return renderFrontendThumbnail();
            case 3:
                return renderFallbackThumbnail();
            default:
                return renderFallbackThumbnail();
        }
    };

    if (isLoading) {
        return (
            <div className="bg-white p-2 rounded border border-gray-200">
                <div className="h-16 bg-gray-100 rounded flex items-center justify-center">
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-blue-600"></div>
                </div>
                <p className="text-xs text-gray-600 mt-1 text-center">Loading...</p>
            </div>
        );
    }

    return (
        <div className="relative">
            {renderCurrentThumbnail()}
            
            {/* Priority indicator (for debugging) */}
            {process.env.NODE_ENV === 'development' && (
                <div className="absolute top-0 right-0 bg-blue-500 text-white text-xs px-1 rounded-bl">
                    P{thumbnailPriority}
                </div>
            )}
            
            {/* Error display (for debugging) */}
            {error && process.env.NODE_ENV === 'development' && (
                <div className="absolute bottom-0 left-0 bg-red-500 text-white text-xs px-1 rounded-tr">
                    {error}
                </div>
            )}
        </div>
    );
};

export default ThumbnailRenderer;
