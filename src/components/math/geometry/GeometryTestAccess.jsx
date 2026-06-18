import React from 'react';
import GeometryBackendTest from './GeometryBackendTest';

/**
 * GeometryTestAccess Component
 * Simple component to access the Geometry Backend Test
 */
const GeometryTestAccess = ({ setView }) => {
    return (
        <div className="p-6">
            <div className="mb-4">
                <button
                    onClick={() => setView('student')}
                    className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded mb-4"
                >
                    ← Back to Main App
                </button>
            </div>
            
            <GeometryBackendTest />
        </div>
    );
};

export default GeometryTestAccess;




