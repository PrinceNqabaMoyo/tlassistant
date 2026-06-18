import React, { useState, useEffect } from 'react';
import MathComponentThumbnail, { hasThumbnail } from './ThumbnailRegistry';

/**
 * Hybrid Thumbnail System
 * Attempts to use backend API first, falls back to frontend canvas thumbnails
 */
const HybridThumbnailSystem = ({ 
    componentId, 
    width = 80, 
    height = 60, 
    useBackend = true,
    backendUrl = '/api/thumbnails/generate'
}) => {
    const [thumbnailData, setThumbnailData] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [useFrontend, setUseFrontend] = useState(false);
    const [error, setError] = useState(null);

    // Check if component has frontend thumbnail
    const hasFrontendThumbnail = hasThumbnail(componentId);

    useEffect(() => {
        console.log(`HybridThumbnailSystem: componentId=${componentId}, useBackend=${useBackend}, hasFrontendThumbnail=${hasFrontendThumbnail}`);
        
        // If backend is disabled or component doesn't have frontend thumbnail, use frontend immediately
        if (!useBackend || !hasFrontendThumbnail) {
            console.log(`Setting useFrontend=true for ${componentId}`);
            setUseFrontend(true);
            return;
        }

        // Try backend first, with a timeout to prevent hanging
        const timeoutId = setTimeout(() => {
            console.warn('Backend timeout, falling back to frontend');
            setUseFrontend(true);
        }, 3000); // 3 second timeout

        generateBackendThumbnail().finally(() => {
            clearTimeout(timeoutId);
        });
    }, [componentId, useBackend, hasFrontendThumbnail]);

    const generateBackendThumbnail = async () => {
        setIsLoading(true);
        setError(null);

        try {
            // Generate appropriate parameters based on component type
            const params = generateComponentParams(componentId);
            
            const response = await fetch(backendUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    type: componentId,
                    params: {
                        ...params,
                        width,
                        height
                    }
                }),
                // Add timeout to prevent hanging
                signal: AbortSignal.timeout(2000) // 2 second timeout
            });

            if (!response.ok) {
                throw new Error(`Backend error: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                setThumbnailData(data.thumbnail);
                setUseFrontend(false);
            } else {
                throw new Error(data.error || 'Backend thumbnail generation failed');
            }
        } catch (err) {
            console.warn('Backend thumbnail failed, falling back to frontend:', err);
            setError(err.message);
            setUseFrontend(true);
        } finally {
            setIsLoading(false);
        }
    };

    const generateComponentParams = (componentType) => {
        // Generate appropriate default parameters for each component type
        const defaultParams = {
            'linear_function': { m: 2, c: 3, x_range: [-10, 10] },
            'quadratic_function': { a: 1, b: -2, c: 1, x_range: [-5, 5] },
            'cubic_function': { a: 1, b: 0, c: -4, d: 0, x_range: [-5, 5] },
            'exponential_function': { a: 1, b: 2, c: 0, d: 0, x_range: [-5, 5] },
            'logarithmic_function': { a: 1, b: 1, c: 0, d: 0, base: 2, x_range: [0.1, 10] },
            'box_whisker_plot': { 
                data: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], 
                labels: ['Group A', 'Group B'] 
            },
            'coordinate_plane': { x_range: [-10, 10], y_range: [-10, 10] },
            'histogram': { data: [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8], bins: 6 },
            'scatter_plot': { 
                x_data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                y_data: [2, 3, 2.5, 4, 3.5, 5, 4.5, 6, 5.5, 7] 
            },
            'venn_diagram': { sets: ['A', 'B'], sizes: [10, 15], colors: ['#3B82F6', '#10B981'] },
            'tree_diagram': { labels: ['Root', 'Child 1', 'Child 2'], sizes: [100, 50, 25] },
            'bar_chart': { x_data: ['A', 'B', 'C'], y_data: [10, 20, 15] },
            'line_graph': { x_data: Array.from({length: 100}, (_, i) => i/10), y_data: Array.from({length: 100}, (_, i) => Math.sin(i/10) + Math.random() * 0.5) },
            'pie_chart': { labels: ['A', 'B', 'C'], sizes: [10, 20, 30] }
        };

        return defaultParams[componentType] || {};
    };

    const handleRetryBackend = () => {
        setUseFrontend(false);
        setError(null);
        generateBackendThumbnail();
    };

    // Loading state
    if (isLoading) {
        return (
            <div 
                className="flex items-center justify-center bg-gray-100 border border-gray-200 rounded"
                style={{ width, height }}
            >
                <div className="text-xs text-gray-500">Loading...</div>
            </div>
        );
    }

    // Backend thumbnail (success)
    if (thumbnailData && !useFrontend) {
        return (
            <div className="relative">
                <img 
                    src={thumbnailData} 
                    alt={`${componentId} thumbnail`}
                    style={{ width, height }}
                    className="border border-gray-200 rounded"
                />
                <button
                    onClick={handleRetryBackend}
                    className="absolute top-0 right-0 bg-blue-500 text-white text-xs px-1 rounded opacity-0 hover:opacity-100 transition-opacity"
                    title="Regenerate thumbnail"
                >
                    ↻
                </button>
            </div>
        );
    }

    // Frontend thumbnail (fallback)
    if (useFrontend && hasFrontendThumbnail) {
        console.log(`Rendering frontend thumbnail for ${componentId}`);
        return (
            <div className="relative">
                <MathComponentThumbnail 
                    componentId={componentId} 
                    width={width} 
                    height={height} 
                />
                <button
                    onClick={handleRetryBackend}
                    className="absolute top-0 right-0 bg-orange-500 text-white text-xs px-1 rounded opacity-0 hover:opacity-100 transition-opacity"
                    title="Try backend thumbnail"
                >
                    ⚡
                </button>
            </div>
        );
    }

    // No thumbnail available
    console.log(`No thumbnail available for ${componentId}`);
    return (
        <div 
            className="flex items-center justify-center bg-gray-100 border border-gray-200 rounded text-xs text-gray-500"
            style={{ width, height }}
        >
            No thumbnail
        </div>
    );
};

export default HybridThumbnailSystem;
