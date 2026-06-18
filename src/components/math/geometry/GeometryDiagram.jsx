import React, { useState, useEffect, useCallback } from 'react';
import { useGeometryBackend } from '../../../hooks/useGeometryBackend';
import { Loader2, AlertCircle, RefreshCw } from 'lucide-react';

/**
 * Enhanced GeometryDiagram Component
 * Displays Python-generated diagrams with fallback to Canvas/SVG
 */
const GeometryDiagram = ({ 
    parameters, 
    type, 
    dimension = '2d',
    fallbackToCanvas = true,
    onError = null,
    className = "",
    style = {}
}) => {
    const { generateDiagram, loading, error } = useGeometryBackend();
    const [diagram, setDiagram] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [diagramError, setDiagramError] = useState(null);
    const [retryCount, setRetryCount] = useState(0);
    const [useFallback, setUseFallback] = useState(false);

    const generateDiagramImage = useCallback(async () => {
        if (!parameters || !type) return;

        setIsLoading(true);
        setDiagramError(null);

        try {
            const result = await generateDiagram(type, dimension, parameters);
            
            if (result.success && result.image_data) {
                setDiagram(result.image_data);
                setUseFallback(false);
                setRetryCount(0);
            } else {
                throw new Error('Invalid response from backend');
            }
        } catch (err) {
            console.error('Diagram generation failed:', err);
            setDiagramError(err.message);
            
            if (onError) {
                onError(err);
            }

            if (fallbackToCanvas) {
                setUseFallback(true);
            }
        } finally {
            setIsLoading(false);
        }
    }, [parameters, type, dimension, generateDiagram, fallbackToCanvas, onError]);

    useEffect(() => {
        generateDiagramImage();
    }, [generateDiagramImage]);

    const handleRetry = () => {
        setRetryCount(prev => prev + 1);
        generateDiagramImage();
    };

    // Loading state
    if (isLoading || loading) {
        return (
            <div className={`flex items-center justify-center p-8 ${className}`} style={style}>
                <div className="text-center">
                    <Loader2 className="h-8 w-8 animate-spin text-blue-500 mx-auto mb-2" />
                    <p className="text-sm text-gray-600">Generating diagram...</p>
                </div>
            </div>
        );
    }

    // Error state with retry option
    if (diagramError && !useFallback) {
        return (
            <div className={`flex items-center justify-center p-8 ${className}`} style={style}>
                <div className="text-center">
                    <AlertCircle className="h-8 w-8 text-red-500 mx-auto mb-2" />
                    <p className="text-sm text-red-600 mb-2">Failed to generate diagram</p>
                    <p className="text-xs text-gray-500 mb-3">{diagramError}</p>
                    <button
                        onClick={handleRetry}
                        disabled={retryCount >= 3}
                        className="flex items-center space-x-1 px-3 py-1 bg-blue-500 text-white text-xs rounded hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed mx-auto"
                    >
                        <RefreshCw className="h-3 w-3" />
                        <span>Retry {retryCount > 0 && `(${retryCount}/3)`}</span>
                    </button>
                </div>
            </div>
        );
    }

    // Success state - display Python-generated diagram
    if (diagram && !useFallback) {
        return (
            <div className={`${className}`} style={style}>
                <img
                    src={diagram}
                    alt={`${type} diagram`}
                    className="max-w-full h-auto"
                    onError={() => {
                        console.error('Failed to load diagram image');
                        if (fallbackToCanvas) {
                            setUseFallback(true);
                        }
                    }}
                />
            </div>
        );
    }

    // Fallback state - use Canvas/SVG rendering
    if (useFallback && fallbackToCanvas) {
        return (
            <CanvasFallback 
                parameters={parameters} 
                type={type} 
                dimension={dimension}
                className={className}
                style={style}
                onBackendAvailable={() => {
                    setUseFallback(false);
                    generateDiagramImage();
                }}
            />
        );
    }

    // Default state
    return (
        <div className={`flex items-center justify-center p-8 ${className}`} style={style}>
            <div className="text-center text-gray-500">
                <p className="text-sm">No diagram to display</p>
            </div>
        </div>
    );
};

/**
 * Canvas Fallback Component
 * Renders diagrams using Canvas/SVG when backend is unavailable
 */
const CanvasFallback = ({ 
    parameters, 
    type, 
    dimension,
    className = "",
    style = {},
    onBackendAvailable = null
}) => {
    const canvasRef = React.useRef(null);
    const [isRendering, setIsRendering] = useState(false);

    useEffect(() => {
        if (!canvasRef.current) return;

        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        
        // Set canvas size
        canvas.width = 400;
        canvas.height = 300;

        // Clear canvas
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Draw grid
        drawGrid(ctx, canvas.width, canvas.height);
        
        // Draw axes
        drawAxes(ctx, canvas.width, canvas.height);

        // Draw the specific diagram type
        drawDiagram(ctx, canvas.width, canvas.height, type, parameters);

    }, [parameters, type, dimension]);

    const drawGrid = (ctx, width, height) => {
        ctx.strokeStyle = '#e5e7eb';
        ctx.lineWidth = 0.5;
        
        const gridSize = 20;
        for (let x = 0; x < width; x += gridSize) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }
        
        for (let y = 0; y < height; y += gridSize) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }
    };

    const drawAxes = (ctx, width, height) => {
        ctx.strokeStyle = '#374151';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(0, height / 2);
        ctx.lineTo(width, height / 2);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(width / 2, 0);
        ctx.lineTo(width / 2, height);
        ctx.stroke();
    };

    const drawDiagram = (ctx, width, height, diagramType, params) => {
        const centerX = width / 2;
        const centerY = height / 2;

        ctx.strokeStyle = '#3B82F6';
        ctx.fillStyle = '#3B82F6';
        ctx.lineWidth = 2;

        switch (diagramType) {
            case 'point':
                const x = centerX + (params.x || 0) * 20;
                const y = centerY - (params.y || 0) * 20;
                ctx.beginPath();
                ctx.arc(x, y, 4, 0, 2 * Math.PI);
                ctx.fill();
                break;

            case 'line':
                const startX = centerX + (params.start?.[0] || -2) * 20;
                const startY = centerY - (params.start?.[1] || 0) * 20;
                const endX = centerX + (params.end?.[0] || 2) * 20;
                const endY = centerY - (params.end?.[1] || 0) * 20;
                ctx.beginPath();
                ctx.moveTo(startX, startY);
                ctx.lineTo(endX, endY);
                ctx.stroke();
                break;

            case 'circle':
                const radius = (params.radius || 2) * 20;
                ctx.beginPath();
                ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
                ctx.stroke();
                break;

            case 'triangle':
                const vertices = params.vertices || [[-1, -1], [1, -1], [0, 1]];
                ctx.beginPath();
                vertices.forEach((vertex, index) => {
                    const x = centerX + vertex[0] * 20;
                    const y = centerY - vertex[1] * 20;
                    if (index === 0) {
                        ctx.moveTo(x, y);
                    } else {
                        ctx.lineTo(x, y);
                    }
                });
                ctx.closePath();
                ctx.stroke();
                break;

            default:
                ctx.fillStyle = '#6B7280';
                ctx.font = '14px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`${diagramType} (fallback)`, centerX, centerY);
        }
    };

    return (
        <div className={`${className}`} style={style}>
            <div className="relative">
                <canvas
                    ref={canvasRef}
                    className="border border-gray-200 rounded"
                />
                <div className="absolute top-2 right-2">
                    <div className="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded">
                        Fallback Mode
                    </div>
                </div>
            </div>
            {onBackendAvailable && (
                <div className="mt-2 text-center">
                    <button
                        onClick={onBackendAvailable}
                        className="text-xs text-blue-600 hover:text-blue-800 underline"
                    >
                        Try Backend Again
                    </button>
                </div>
            )}
        </div>
    );
};

export default GeometryDiagram;