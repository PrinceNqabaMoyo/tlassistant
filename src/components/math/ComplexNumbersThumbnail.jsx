import React from 'react';

const ComplexNumbersThumbnail = ({ width = 80, height = 60 }) => {
    return (
        <div 
            className="w-full h-full bg-gradient-to-br from-purple-100 to-purple-200 rounded-lg flex flex-col items-center justify-center p-2 border border-purple-300"
            style={{ width: `${width}px`, height: `${height}px` }}
        >
            {/* Complex plane representation */}
            <div className="relative w-12 h-12 mb-1">
                {/* Axes */}
                <div className="absolute inset-0 flex items-center justify-center">
                    {/* Horizontal axis (real) */}
                    <div className="w-full h-px bg-purple-600"></div>
                </div>
                <div className="absolute inset-0 flex items-center justify-center">
                    {/* Vertical axis (imaginary) */}
                    <div className="w-px h-full bg-purple-600"></div>
                </div>
                
                {/* Complex number point */}
                <div 
                    className="absolute w-2 h-2 bg-red-500 rounded-full"
                    style={{ 
                        left: '60%', 
                        top: '40%',
                        transform: 'translate(-50%, -50%)'
                    }}
                ></div>
                
                {/* Vector from origin */}
                <div 
                    className="absolute w-px bg-red-500"
                    style={{ 
                        left: '50%', 
                        top: '50%',
                        height: '20px',
                        transform: 'translate(-50%, -50%) rotate(30deg)',
                        transformOrigin: 'bottom center'
                    }}
                ></div>
            </div>
            
            {/* Labels */}
            <div className="text-xs font-medium text-purple-800 text-center">
                <div className="font-bold">Complex</div>
                <div className="text-xs">Numbers</div>
            </div>
        </div>
    );
};

export default ComplexNumbersThumbnail;
