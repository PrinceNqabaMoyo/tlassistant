import React from 'react';
import GeometryDiagram from './GeometryDiagram';

/**
 * PythonGeometryVisual Component
 * Replaces the basic SVG visuals with Python-generated diagrams
 * Provides consistent parameters for different geometric elements
 */
const PythonGeometryVisual = ({ type, className = '' }) => {
    // Define parameters for different geometric elements
    const getParameters = (visualType) => {
        const baseParams = {
            color: '#3b82f6'
        };

        switch (visualType) {
            case 'point':
                return {
                    ...baseParams,
                    x: 0,
                    y: 0,
                    label: 'P'
                };

            case 'line':
                return {
                    ...baseParams,
                    start: [-3, 0],
                    end: [3, 0],
                    label: 'AB'
                };

            case 'ray':
                return {
                    ...baseParams,
                    start: [-2, 0],
                    end: [3, 0],
                    label: 'AB'
                };

            case 'segment':
                return {
                    ...baseParams,
                    start: [-2, 0],
                    end: [2, 0],
                    label: 'AB'
                };

            case 'parallel_lines':
                return {
                    ...baseParams,
                    line1: { start: [-3, -1], end: [3, -1] },
                    line2: { start: [-3, 1], end: [3, 1] }
                };

            case 'perpendicular_lines':
                return {
                    ...baseParams,
                    line1: { start: [-3, 0], end: [3, 0] },
                    line2: { start: [0, -2], end: [0, 2] },
                    intersection: [0, 0]
                };

            case 'angle_acute':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [1.5, 1.5],
                    type: 'acute'
                };

            case 'angle_right':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [0, 2],
                    type: 'right'
                };

            case 'angle_obtuse':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [-1, 1.5],
                    type: 'obtuse'
                };

            case 'angle_straight':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [-2, 0],
                    arm2: [2, 0],
                    type: 'straight'
                };

            case 'angle_reflex':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [0, 2],
                    type: 'reflex'
                };

            case 'angle_revolution':
                return {
                    ...baseParams,
                    vertex: [0, 0],
                    arm1: [2, 0],
                    arm2: [2, 0],
                    type: 'revolution'
                };

            case 'circle':
                return {
                    ...baseParams,
                    center: [0, 0],
                    radius: 2
                };

            case 'triangle':
                return {
                    ...baseParams,
                    vertices: [[-1.5, -1], [1.5, -1], [0, 2]]
                };

            case 'quadrilateral':
                return {
                    ...baseParams,
                    vertices: [[-1.5, -1], [1.5, -1], [1.5, 1], [-1.5, 1]]
                };

            default:
                return baseParams;
        }
    };

    const parameters = getParameters(type);

    return (
        <div className={`python-geometry-visual ${className}`}>
            <GeometryDiagram
                diagramType={type}
                dimension="2d"
                parameters={parameters}
                className="w-full h-auto"
                showLoading={true}
            />
        </div>
    );
};

export default PythonGeometryVisual;




