import React from 'react';
import GeometryBackendTest from './geometry/GeometryBackendTest';

/**
 * GeometryBackendTestPage Component
 * Simple page to access the Geometry Backend Test
 */
const GeometryBackendTestPage = () => {
    return (
        <div className="min-h-screen bg-gray-50">
            <div className="container mx-auto py-8">
                <div className="bg-white rounded-lg shadow-lg p-6">
                    <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">
                        Geometry Backend Integration Test
                    </h1>
                    <GeometryBackendTest />
                </div>
            </div>
        </div>
    );
};

export default GeometryBackendTestPage;




