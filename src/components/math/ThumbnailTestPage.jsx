import React, { useState } from 'react';
import MathComponentThumbnail, { hasThumbnail } from './ThumbnailRegistry';

const ThumbnailTestPage = ({ setView }) => {
    console.log('🔍 ThumbnailTestPage: Component rendered');

    // All available thumbnail components
    const allComponents = [
        'linear_function',
        'quadratic_function', 
        'coordinate_plane',
        'cubic_function',
        'exponential_function',
        'logarithmic_function',
        'box_whisker_plot',
        'histogram',
        'scatter_plot',
        'venn_diagram',
        'tree_diagram',
        'number_line',
        'fraction_visualizer',
        'geometric_construction',
        'statistical_analysis',
        'probability_simulator',
        'algebraic_expression_builder',
        'test'
    ];

    console.log('🔍 ThumbnailTestPage: allComponents array:', allComponents);
    console.log('🔍 ThumbnailTestPage: algebraic_expression_builder in array:', allComponents.includes('algebraic_expression_builder'));

    return (
        <div className="min-h-screen bg-gray-50 py-8">
            <div className="max-w-7xl mx-auto px-4">
                <div className="text-center mb-8">
                    <h1 className="text-3xl font-bold text-gray-900 mb-4">
                        Math Component Thumbnail Test Page
                    </h1>
                    <p className="text-lg text-gray-600">
                        Test and verify all math component thumbnails are working correctly
                    </p>
                    
                    {/* Integration Demo Button */}
                    <div className="mt-6">
                        <button
                            onClick={() => setView('integration_demo')}
                            className="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-lg shadow-lg hover:from-blue-700 hover:to-purple-700 transition-all duration-200 transform hover:scale-105"
                        >
                            🚀 View Exponential-Logarithmic Integration Demo
                        </button>
                        <p className="text-sm text-gray-500 mt-2">
                            See the new unified component in action
                        </p>
                    </div>
                </div>

                <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">
                        Thumbnail Availability Status
                    </h2>
                    <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
                        {allComponents.map(componentId => (
                            <div key={componentId} className="text-center p-3 border rounded-lg">
                                <div className="text-sm font-medium text-gray-700">
                                    {componentId}
                                </div>
                                <div className={`text-xs ${
                                    hasThumbnail(componentId) 
                                        ? 'text-green-600' 
                                        : 'text-red-600'
                                }`}>
                                    {hasThumbnail(componentId) ? '✓ Available' : '✗ Missing'}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>

                <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">
                        Individual Thumbnail Tests
                    </h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {allComponents.map(componentId => {
                            console.log('🔍 ThumbnailTestPage: Rendering component:', componentId);
                            const hasThumb = hasThumbnail(componentId);
                            console.log('🔍 ThumbnailTestPage: Has thumbnail for', componentId, ':', hasThumb);
                            
                            return (
                                <div 
                                    key={componentId}
                                    className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
                                >
                                    <h3 className="text-lg font-medium text-gray-800 mb-3 capitalize">
                                        {componentId.replace(/_/g, ' ')}
                                    </h3>
                                    
                                    {hasThumb ? (
                                        <div className="space-y-3">
                                            <div className="text-sm text-gray-600">
                                                <strong>Small (80x60):</strong>
                                            </div>
                                            <MathComponentThumbnail 
                                                componentId={componentId} 
                                                width={80} 
                                                height={60} 
                                            />
                                            
                                            <div className="text-sm text-gray-600">
                                                <strong>Medium (120x80):</strong>
                                            </div>
                                            <MathComponentThumbnail 
                                                componentId={componentId} 
                                                width={120} 
                                                height={80} 
                                            />
                                            
                                            <div className="text-sm text-gray-600">
                                                <strong>Large (200x150):</strong>
                                            </div>
                                            <MathComponentThumbnail 
                                                componentId={componentId} 
                                                width={200} 
                                                height={150} 
                                            />
                                        </div>
                                    ) : (
                                        <div className="text-red-500 text-sm">
                                            No thumbnail component available for this type.
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </div>
                </div>

                <div className="bg-white rounded-lg shadow-lg p-6">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">
                        Test Results Summary
                    </h2>
                    <div className="space-y-2">
                        <div className="flex justify-between items-center">
                            <span className="text-gray-700">Total Components:</span>
                            <span className="font-medium">{allComponents.length}</span>
                        </div>
                        <div className="flex justify-between items-center">
                            <span className="text-gray-700">Available Thumbnails:</span>
                            <span className="font-medium text-green-600">
                                {allComponents.filter(id => hasThumbnail(id)).length}
                            </span>
                        </div>
                        <div className="flex justify-between items-center">
                            <span className="text-gray-700">Missing Thumbnails:</span>
                            <span className="font-medium text-red-600">
                                {allComponents.filter(id => !hasThumbnail(id)).length}
                            </span>
                        </div>
                        <div className="flex justify-between items-center">
                            <span className="text-gray-700">Coverage:</span>
                            <span className="font-medium text-blue-600">
                                {Math.round((allComponents.filter(id => hasThumbnail(id)).length / allComponents.length) * 100)}%
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ThumbnailTestPage;
