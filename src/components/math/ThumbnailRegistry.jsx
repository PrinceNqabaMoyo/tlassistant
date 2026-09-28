import React from 'react';
import LinearFunctionGraphThumbnail from './LinearFunctionGraphThumbnail';
import QuadraticGraphThumbnail from './QuadraticGraphThumbnail';
import CoordinatePlaneThumbnail from './CoordinatePlaneThumbnail';
import TestThumbnail from './TestThumbnail';
import CubicFunctionThumbnail from './CubicFunctionThumbnail';

import IntegratedExponentialLogarithmicThumbnail from './IntegratedExponentialLogarithmicThumbnail';
import BoxWhiskerPlotThumbnail from './BoxWhiskerPlotThumbnail';
import HistogramThumbnail from './HistogramThumbnail';
import ScatterPlotThumbnail from './ScatterPlotThumbnail';
import VennDiagramThumbnail from './VennDiagramThumbnail';
import TreeDiagramThumbnail from './TreeDiagramThumbnail';
import NumberLineThumbnail from './NumberLineThumbnail';
import FractionVisualizerThumbnail from './FractionVisualizerThumbnail';
import ComplexNumbersThumbnail from './ComplexNumbersThumbnail';
import GeometricConstructionThumbnail from './GeometricConstructionThumbnail';
import StatisticalAnalysisThumbnail from './StatisticalAnalysisThumbnail';
import ProbabilitySimulatorThumbnail from './ProbabilitySimulatorThumbnail';
import AlgebraicExpressionBuilderThumbnail from './AlgebraicExpressionBuilderThumbnail';
import GeometryStudioThumbnail from './GeometryStudioThumbnail';
import ComplexPlaneExplorerThumbnail from './ComplexPlaneExplorerThumbnail';

// Registry of thumbnail components - using actual component IDs from MathComponentsRepository
const thumbnailRegistry = {
    'linear_function': LinearFunctionGraphThumbnail,
    'quadratic_function': QuadraticGraphThumbnail,
    'coordinate_plane': CoordinatePlaneThumbnail,
    'cubic_function': CubicFunctionThumbnail,
    'exponential_function': IntegratedExponentialLogarithmicThumbnail, // Now uses integrated component
    'logarithmic_function': IntegratedExponentialLogarithmicThumbnail, // Now uses integrated component
    'integrated_exponential_logarithmic': IntegratedExponentialLogarithmicThumbnail, // New dedicated entry
    'box_whisker_plot': BoxWhiskerPlotThumbnail,
    'histogram': HistogramThumbnail,
    'scatter_plot': ScatterPlotThumbnail,
    'venn_diagram': VennDiagramThumbnail,
    'tree_diagram': TreeDiagramThumbnail,
    'number_line': NumberLineThumbnail,
    'fraction_visualizer': FractionVisualizerThumbnail,
    'complex_numbers': ComplexNumbersThumbnail,
    'geometric_construction': GeometricConstructionThumbnail,
    'statistical_analysis': StatisticalAnalysisThumbnail,
    'probability_simulator': ProbabilitySimulatorThumbnail,
    'algebraic_expression_builder': AlgebraicExpressionBuilderThumbnail,
    'geometry_studio': GeometryStudioThumbnail,
    'complex_plane_explorer': ComplexPlaneExplorerThumbnail,
    'test': TestThumbnail, // Test thumbnail
    // Add more thumbnails here as they are created
};

// Component to render thumbnails based on component ID
const MathComponentThumbnail = ({ componentId, width = 80, height = 60 }) => {
    const ThumbnailComponent = thumbnailRegistry[componentId];
    if (!ThumbnailComponent) {
        return null; // No thumbnail available for this component
    }
    return <ThumbnailComponent width={width} height={height} />;
};

// Helper function to check if a component has a thumbnail
// eslint-disable-next-line react-refresh/only-export-components
export const hasThumbnail = (componentId) => {
    return componentId in thumbnailRegistry;
};

export default MathComponentThumbnail;
