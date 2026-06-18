import React, { useState } from 'react';
import HybridThumbnailSystem from './HybridThumbnailSystem';
import MathComponentThumbnail from './ThumbnailRegistry';

const ThumbnailTestComponent = () => {
    const [useBackend, setUseBackend] = useState(true);
    const [selectedComponent, setSelectedComponent] = useState('linear_function');

    const testComponents = [
        'linear_function',
        'quadratic_function',
        'cubic_function',
        'exponential_function',
        'logarithmic_function',
        'box_whisker_plot',
        'histogram',
        'scatter_plot',
        'venn_diagram',
        'tree_diagram',
        'bar_chart',
        'line_graph',
        'pie_chart'
    ];

    return (
        <div className="p-6 bg-white rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold mb-4">Thumbnail System Test</h2>
            
            {/* Controls */}
            <div className="mb-6 space-y-4">
                <div className="flex items-center space-x-4">
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={useBackend}
                            onChange={(e) => setUseBackend(e.target.checked)}
                            className="mr-2"
                        />
                        Use Backend API
                    </label>
                </div>
                
                <div>
                    <label className="block text-sm font-medium mb-2">Test Component:</label>
                    <select
                        value={selectedComponent}
                        onChange={(e) => setSelectedComponent(e.target.value)}
                        className="px-3 py-2 border border-gray-300 rounded-md"
                    >
                        {testComponents.map(comp => (
                            <option key={comp} value={comp}>
                                {comp.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                            </option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Test Results */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Hybrid System */}
                <div className="border border-gray-200 rounded-lg p-4">
                    <h3 className="text-lg font-semibold mb-3">Hybrid System (Backend + Fallback)</h3>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium mb-2">Component: {selectedComponent}</label>
                            <HybridThumbnailSystem
                                componentId={selectedComponent}
                                width={120}
                                height={80}
                                useBackend={useBackend}
                            />
                        </div>
                    </div>
                </div>

                {/* Frontend Only */}
                <div className="border border-gray-200 rounded-lg p-4">
                    <h3 className="text-lg font-semibold mb-3">Frontend Only (Canvas)</h3>
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium mb-2">Component: {selectedComponent}</label>
                            <MathComponentThumbnail
                                componentId={selectedComponent}
                                width={120}
                                height={80}
                            />
                        </div>
                    </div>
                </div>
            </div>

            {/* Status Information */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="font-semibold mb-2">System Status:</h4>
                <ul className="text-sm space-y-1">
                    <li>✅ Frontend thumbnails: {testComponents.filter(comp => comp !== 'test').length} components</li>
                    <li>🔄 Backend API: {useBackend ? 'Enabled' : 'Disabled'}</li>
                    <li>📡 Backend URL: /api/thumbnails/generate</li>
                    <li>🎨 Fallback system: Automatic frontend fallback</li>
                </ul>
            </div>

            {/* Instructions */}
            <div className="mt-6 p-4 bg-blue-50 rounded-lg">
                <h4 className="font-semibold mb-2">Testing Instructions:</h4>
                <ol className="text-sm space-y-1 list-decimal list-inside">
                    <li>Select a component type from the dropdown</li>
                    <li>Toggle "Use Backend API" to test both systems</li>
                    <li>Compare thumbnail quality between hybrid and frontend-only</li>
                    <li>Check browser console for any API errors</li>
                    <li>Verify fallback behavior when backend is unavailable</li>
                </ol>
            </div>
        </div>
    );
};

export default ThumbnailTestComponent;
