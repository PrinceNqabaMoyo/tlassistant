import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useGeometryBackend } from '../../../hooks/useGeometryBackend';
import DiagramLoadingSpinner from './DiagramLoadingSpinner';
import DiagramError from './DiagramError';

/**
 * LazyGeometryDiagram Component
 * Implements lazy loading for geometry diagrams with intersection observer
 * Only loads diagrams when they come into view
 */
const LazyGeometryDiagram = ({ 
    diagramType, 
    dimension = '2d', 
    parameters = {}, 
    fallbackToCanvas = true, 
    CanvasFallbackComponent = null,
    threshold = 0.1,
    rootMargin = '50px'
}) => {
    const { generateDiagram, loading, error, setError } = useGeometryBackend();
    const [diagram, setDiagram] = useState(null);
    const [internalError, setInternalError] = useState(null);
    const [isVisible, setIsVisible] = useState(false);
    const [hasLoaded, setHasLoaded] = useState(false);
    const elementRef = useRef(null);

    // Intersection Observer for lazy loading
    useEffect(() => {
        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting && !hasLoaded) {
                    setIsVisible(true);
                    setHasLoaded(true);
                }
            },
            {
                threshold,
                rootMargin
            }
        );

        if (elementRef.current) {
            observer.observe(elementRef.current);
        }

        return () => {
            if (elementRef.current) {
                observer.unobserve(elementRef.current);
            }
        };
    }, [threshold, rootMargin, hasLoaded]);

    // Load diagram when visible
    useEffect(() => {
        if (!isVisible || hasLoaded) return;

        const fetchDiagram = async () => {
            setDiagram(null);
            setInternalError(null);
            try {
                const result = await generateDiagram(diagramType, dimension, parameters);
                if (result && result.image_data) {
                    setDiagram(result.image_data);
                } else if (result && result.plotly_data) {
                    // Handle Plotly JSON data for 3D diagrams
                    console.log("Received Plotly 3D data:", result.plotly_data);
                    setDiagram(JSON.stringify(result.plotly_data));
                } else {
                    throw new Error('No diagram data received from backend.');
                }
            } catch (err) {
                console.error('Error fetching diagram:', err);
                setInternalError(err.message);
                if (!error) setError(err.message);
            }
        };

        fetchDiagram();
    }, [isVisible, diagramType, dimension, parameters, generateDiagram, error, setError, hasLoaded]);

    // Show placeholder while not visible
    if (!isVisible) {
        return (
            <div 
                ref={elementRef}
                className="min-h-[150px] bg-gray-100 rounded-lg flex items-center justify-center"
            >
                <div className="text-gray-400 text-sm">Loading diagram...</div>
            </div>
        );
    }

    // Show loading spinner while fetching
    if (loading && !diagram) {
        return (
            <div ref={elementRef}>
                <DiagramLoadingSpinner message="Generating diagram..." />
            </div>
        );
    }

    // Show error if failed and no fallback
    if (internalError && !fallbackToCanvas) {
        return (
            <div ref={elementRef}>
                <DiagramError message={`Failed to load diagram: ${internalError}`} />
            </div>
        );
    }

    // Show diagram if loaded
    if (diagram) {
        if (dimension === '2d') {
            return (
                <div ref={elementRef}>
                    <img 
                        src={diagram} 
                        alt={`${diagramType} Diagram`} 
                        className="max-w-full h-auto object-contain"
                        loading="lazy"
                    />
                </div>
            );
        } else if (dimension === '3d') {
            return (
                <div ref={elementRef} className="bg-gray-100 p-4 rounded-md text-sm text-gray-700">
                    <p>3D Plotly Diagram Data (render with a Plotly component):</p>
                    <pre className="whitespace-pre-wrap break-all">{diagram}</pre>
                </div>
            );
        }
    }

    // Show fallback if enabled
    if (fallbackToCanvas && CanvasFallbackComponent) {
        return (
            <div ref={elementRef}>
                <CanvasFallbackComponent {...parameters} />
            </div>
        );
    }

    // Default state
    return (
        <div ref={elementRef} className="text-center text-gray-500 py-8">
            <p>No diagram available.</p>
            {internalError && <p className="text-red-500 text-sm mt-2">{internalError}</p>}
        </div>
    );
};

export default LazyGeometryDiagram;
