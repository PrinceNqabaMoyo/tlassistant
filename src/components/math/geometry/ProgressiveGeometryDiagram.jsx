import React, { useState, useEffect } from 'react';
import { useGeometryBackend } from '../../../hooks/useGeometryBackend';
import { optimizeImage } from '../../../utils/imageCompression';
import DiagramLoadingSpinner from './DiagramLoadingSpinner';
import DiagramError from './DiagramError';

/**
 * ProgressiveGeometryDiagram Component
 * Implements progressive loading with placeholders and image optimization
 * Shows skeleton loading, then low-quality preview, then full quality
 */
const ProgressiveGeometryDiagram = ({ 
    diagramType, 
    dimension = '2d', 
    parameters = {}, 
    fallbackToCanvas = true, 
    CanvasFallbackComponent = null,
    enableOptimization = true,
    maxSizeKB = 100
}) => {
    const { generateDiagram, loading, error, setError } = useGeometryBackend();
    const [diagram, setDiagram] = useState(null);
    const [optimizedDiagram, setOptimizedDiagram] = useState(null);
    const [internalError, setInternalError] = useState(null);
    const [loadingStage, setLoadingStage] = useState('initial'); // initial, generating, optimizing, complete

    useEffect(() => {
        const fetchDiagram = async () => {
            setDiagram(null);
            setOptimizedDiagram(null);
            setInternalError(null);
            setLoadingStage('generating');

            try {
                const result = await generateDiagram(diagramType, dimension, parameters);
                
                if (result && result.image_data) {
                    setDiagram(result.image_data);
                    setLoadingStage('optimizing');

                    // Optimize image if enabled
                    if (enableOptimization) {
                        try {
                            const optimized = await optimizeImage(result.image_data, maxSizeKB);
                            setOptimizedDiagram(optimized);
                        } catch (optError) {
                            console.warn('Image optimization failed, using original:', optError);
                            setOptimizedDiagram(result.image_data);
                        }
                    } else {
                        setOptimizedDiagram(result.image_data);
                    }
                    
                    setLoadingStage('complete');
                } else if (result && result.plotly_data) {
                    // Handle Plotly JSON data for 3D diagrams
                    console.log("Received Plotly 3D data:", result.plotly_data);
                    setDiagram(JSON.stringify(result.plotly_data));
                    setOptimizedDiagram(JSON.stringify(result.plotly_data));
                    setLoadingStage('complete');
                } else {
                    throw new Error('No diagram data received from backend.');
                }
            } catch (err) {
                console.error('Error fetching diagram:', err);
                setInternalError(err.message);
                setLoadingStage('error');
                if (!error) setError(err.message);
            }
        };

        fetchDiagram();
    }, [diagramType, dimension, parameters, generateDiagram, error, setError, enableOptimization, maxSizeKB]);

    // Show skeleton loading
    if (loadingStage === 'initial' || loadingStage === 'generating') {
        return <DiagramLoadingSpinner message="Generating diagram..." />;
    }

    // Show error
    if (loadingStage === 'error' && internalError && !fallbackToCanvas) {
        return <DiagramError message={`Failed to load diagram: ${internalError}`} />;
    }

    // Show optimizing state
    if (loadingStage === 'optimizing') {
        return (
            <div className="flex flex-col items-center justify-center h-full min-h-[150px] bg-gray-50 text-gray-600 rounded-lg p-4">
                <div className="w-8 h-8 border-2 border-blue-500 border-t-transparent rounded-full animate-spin mb-3"></div>
                <p className="text-sm font-medium">Optimizing image...</p>
            </div>
        );
    }

    // Show diagram
    if (optimizedDiagram && loadingStage === 'complete') {
        if (dimension === '2d') {
            return (
                <div className="relative">
                    {/* Low-quality placeholder while high-quality loads */}
                    {diagram && diagram !== optimizedDiagram && (
                        <img 
                            src={diagram} 
                            alt={`${diagramType} Diagram (preview)`} 
                            className="absolute inset-0 max-w-full h-auto object-contain opacity-50 blur-sm"
                        />
                    )}
                    
                    {/* High-quality image */}
                    <img 
                        src={optimizedDiagram} 
                        alt={`${diagramType} Diagram`} 
                        className="max-w-full h-auto object-contain transition-opacity duration-300"
                        style={{ 
                            opacity: diagram && diagram !== optimizedDiagram ? 0 : 1 
                        }}
                        onLoad={() => {
                            // Fade in the high-quality image
                            if (diagram && diagram !== optimizedDiagram) {
                                setTimeout(() => {
                                    setDiagram(optimizedDiagram);
                                }, 100);
                            }
                        }}
                    />
                </div>
            );
        } else if (dimension === '3d') {
            return (
                <div className="bg-gray-100 p-4 rounded-md text-sm text-gray-700">
                    <p>3D Plotly Diagram Data (render with a Plotly component):</p>
                    <pre className="whitespace-pre-wrap break-all">{optimizedDiagram}</pre>
                </div>
            );
        }
    }

    // Show fallback if enabled
    if (fallbackToCanvas && CanvasFallbackComponent) {
        return <CanvasFallbackComponent {...parameters} />;
    }

    // Default state
    return (
        <div className="text-center text-gray-500 py-8">
            <p>No diagram available.</p>
            {internalError && <p className="text-red-500 text-sm mt-2">{internalError}</p>}
        </div>
    );
};

export default ProgressiveGeometryDiagram;
