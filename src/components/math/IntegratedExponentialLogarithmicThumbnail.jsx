import React from 'react';

const IntegratedExponentialLogarithmicThumbnail = ({ width = 80, height = 60 }) => {
    return (
        <div 
            className="bg-white border border-gray-300 rounded-lg flex flex-col items-center justify-center p-1"
            style={{ width: `${width}px`, height: `${height}px` }}
        >
            {/* Header */}
            <div className="text-xs font-medium text-gray-700 mb-1 text-center">
                Exp+Log
            </div>
            
            {/* Mini Graph Representation */}
            <div className="relative w-full h-3/4 flex items-center justify-center">
                {/* Exponential curve (blue) */}
                <svg width="100%" height="100%" viewBox="0 0 60 40" className="absolute">
                    <defs>
                        <linearGradient id="expGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stopColor="#3B82F6" stopOpacity="0.8" />
                            <stop offset="100%" stopColor="#3B82F6" stopOpacity="0.4" />
                        </linearGradient>
                    </defs>
                    <path
                        d="M 5 35 Q 15 30 25 25 Q 35 20 45 15 Q 50 12 55 8"
                        stroke="#3B82F6"
                        strokeWidth="2"
                        fill="none"
                        strokeLinecap="round"
                    />
                    <circle cx="5" cy="35" r="1.5" fill="#3B82F6" />
                    <circle cx="25" cy="25" r="1.5" fill="#3B82F6" />
                    <circle cx="45" cy="15" r="1.5" fill="#3B82F6" />
                </svg>
                
                {/* Logarithmic curve (green) */}
                <svg width="100%" height="100%" viewBox="0 0 60 40" className="absolute">
                    <defs>
                        <linearGradient id="logGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stopColor="#10B981" stopOpacity="0.8" />
                            <stop offset="100%" stopColor="#10B981" stopOpacity="0.4" />
                        </linearGradient>
                    </defs>
                    <path
                        d="M 15 35 Q 25 30 35 25 Q 45 20 55 15"
                        stroke="#10B981"
                        strokeWidth="2"
                        fill="none"
                        strokeLinecap="round"
                    />
                    <circle cx="15" cy="35" r="1.5" fill="#10B981" />
                    <circle cx="35" cy="25" r="1.5" fill="#10B981" />
                    <circle cx="55" cy="15" r="1.5" fill="#10B981" />
                </svg>
                
                {/* Function type indicators */}
                <div className="absolute top-0 left-1">
                    <div className="w-2 h-2 bg-blue-500 rounded-full mb-1"></div>
                    <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                </div>
            </div>
            
            {/* Function labels */}
            <div className="text-xs text-gray-500 text-center">
                y = a×b^(x+c)+d
            </div>
        </div>
    );
};

export default IntegratedExponentialLogarithmicThumbnail;
