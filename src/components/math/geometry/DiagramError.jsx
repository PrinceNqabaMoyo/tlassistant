import React from 'react';
import { AlertCircle, RefreshCw } from 'lucide-react';

const DiagramError = ({ 
    error, 
    onRetry = null, 
    retryCount = 0,
    maxRetries = 3 
}) => {
    return (
        <div className="flex items-center justify-center p-8">
            <div className="text-center">
                <AlertCircle className="h-8 w-8 text-red-500 mx-auto mb-2" />
                <p className="text-sm text-red-600 mb-2">Failed to generate diagram</p>
                <p className="text-xs text-gray-500 mb-3">{error}</p>
                {onRetry && retryCount < maxRetries && (
                    <button
                        onClick={onRetry}
                        className="flex items-center space-x-1 px-3 py-1 bg-blue-500 text-white text-xs rounded hover:bg-blue-600 mx-auto"
                    >
                        <RefreshCw className="h-3 w-3" />
                        <span>Retry {retryCount > 0 && `(${retryCount}/${maxRetries})`}</span>
                    </button>
                )}
            </div>
        </div>
    );
};

export default DiagramError;
