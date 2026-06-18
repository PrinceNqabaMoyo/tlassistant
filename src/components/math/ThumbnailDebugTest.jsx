import React from 'react';
import MathComponentThumbnail, { hasThumbnail } from './ThumbnailRegistry';

const ThumbnailDebugTest = () => {
    const testComponents = [
        'linear_function',
        'quadratic_function', 
        'cubic_function',
        'exponential_function',
        'logarithmic_function',
        'box_whisker_plot',
        'number_line',
        'histogram',
        'scatter_plot',
        'venn_diagram',
        'tree_diagram'
    ];

    return (
        <div className="p-4 bg-white border rounded">
            <h3 className="text-lg font-bold mb-4">Thumbnail Debug Test</h3>
            
            <div className="space-y-4">
                {testComponents.map(componentId => {
                    const hasThumb = hasThumbnail(componentId);
                    return (
                        <div key={componentId} className="border p-2">
                            <div className="text-sm font-medium mb-2">
                                {componentId} - hasThumbnail: {hasThumb.toString()}
                            </div>
                            {hasThumb ? (
                                <MathComponentThumbnail 
                                    componentId={componentId} 
                                    width={120} 
                                    height={80} 
                                />
                            ) : (
                                <div className="text-red-500">No thumbnail available</div>
                            )}
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default ThumbnailDebugTest;
