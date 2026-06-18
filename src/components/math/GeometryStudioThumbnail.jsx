import React from 'react';
import { Square, Circle, Triangle, Box, Cylinder, Pyramid, Cone, Globe, Ruler, Calculator, Compass } from 'lucide-react';

const GeometryStudioThumbnail = ({ onClick, isSelected }) => {
    return (
        <div
            onClick={onClick}
            className={`w-full h-32 bg-gradient-to-br from-blue-50 to-indigo-100 border-2 rounded-lg cursor-pointer transition-all duration-200 hover:shadow-md ${
                isSelected 
                    ? 'border-blue-500 shadow-lg' 
                    : 'border-gray-200 hover:border-blue-300'
            }`}
        >
            <div className="p-4 h-full flex flex-col">
                {/* Header */}
                <div className="flex items-center justify-between mb-2">
                    <h3 className="text-sm font-semibold text-gray-800">Geometry Studio</h3>
                    <div className="flex items-center space-x-1">
                        <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                        <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                        <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                    </div>
                </div>

                {/* Visual Elements */}
                <div className="flex-1 flex items-center justify-center relative">
                    {/* 2D Shapes */}
                    <div className="absolute left-2 top-2 flex flex-col space-y-1">
                        <div className="w-4 h-4 bg-blue-500 rounded-sm opacity-80"></div>
                        <div className="w-4 h-4 bg-blue-500 rounded-full opacity-80"></div>
                        <div className="w-4 h-4 bg-blue-500 opacity-80" style={{
                            clipPath: 'polygon(50% 0%, 0% 100%, 100% 100%)'
                        }}></div>
                    </div>

                    {/* 3D Shapes */}
                    <div className="absolute right-2 top-2 flex flex-col space-y-1">
                        <div className="w-4 h-4 bg-green-500 opacity-80" style={{
                            transform: 'perspective(10px) rotateX(10deg) rotateY(10deg)',
                            background: 'linear-gradient(45deg, #10B981, #059669)'
                        }}></div>
                        <div className="w-4 h-4 bg-green-500 rounded-full opacity-80" style={{
                            background: 'radial-gradient(circle at 30% 30%, #10B981, #059669)'
                        }}></div>
                        <div className="w-4 h-4 bg-green-500 opacity-80" style={{
                            clipPath: 'polygon(50% 0%, 0% 100%, 100% 100%)',
                            background: 'linear-gradient(45deg, #10B981, #059669)'
                        }}></div>
                    </div>

                    {/* Center Tools */}
                    <div className="flex items-center justify-center space-x-2">
                        <div className="w-6 h-6 bg-purple-500 rounded-full flex items-center justify-center">
                            <Compass className="w-3 h-3 text-white" />
                        </div>
                        <div className="w-6 h-6 bg-purple-500 rounded-full flex items-center justify-center">
                            <Ruler className="w-3 h-3 text-white" />
                        </div>
                        <div className="w-6 h-6 bg-purple-500 rounded-full flex items-center justify-center">
                            <Calculator className="w-3 h-3 text-white" />
                        </div>
                    </div>

                    {/* Grid Lines */}
                    <div className="absolute inset-0 opacity-20">
                        <div className="w-full h-full" style={{
                            backgroundImage: `
                                linear-gradient(to right, #6B7280 1px, transparent 1px),
                                linear-gradient(to bottom, #6B7280 1px, transparent 1px)
                            `,
                            backgroundSize: '8px 8px'
                        }}></div>
                    </div>
                </div>

                {/* Footer */}
                <div className="flex items-center justify-between text-xs text-gray-600">
                    <span>2D • 3D • Advanced</span>
                    <span>Interactive</span>
                </div>
            </div>
        </div>
    );
};

export default GeometryStudioThumbnail;
