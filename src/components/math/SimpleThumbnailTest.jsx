import React from 'react';
import MathComponentThumbnail from './ThumbnailRegistry';

const SimpleThumbnailTest = () => {
    const testComponents = [
        'linear_function',
        'cubic_function',
        'exponential_function'
    ];

    return (
        <div className="p-4 bg-white border rounded">
            <h3 className="text-lg font-bold mb-4">Simple Thumbnail Test</h3>
            
            <div className="space-y-4">
                {testComponents.map(componentId => (
                    <div key={componentId} className="border p-2">
                        <div className="text-sm font-medium mb-2">{componentId}</div>
                        <MathComponentThumbnail 
                            componentId={componentId} 
                            width={120} 
                            height={80} 
                        />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SimpleThumbnailTest;
