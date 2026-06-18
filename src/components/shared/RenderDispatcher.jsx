import React from 'react';
import KaTeXRenderer from './KaTeXRenderer';
import JSXGraphRenderer from './JSXGraphRenderer';
import ChemistryRenderer from '../science/ChemistryRenderer';
import GeographyMapRenderer from '../science/GeographyMapRenderer';
import PlotlyRenderer from '../science/PlotlyRenderer';
import MermaidRenderer from '../science/MermaidRenderer';
import SVGRenderer from '../science/SVGRenderer';

function RenderDispatcher({ payload }) {
  if (!payload || !payload.type) return null;

  switch (payload.type) {
    case 'math':
      return <KaTeXRenderer latex={payload.data || payload.latex} displayMode={payload.displayMode} />;
    case 'geometry':
      return <JSXGraphRenderer config={payload} />;
    case 'chemistry':
      return <ChemistryRenderer smilesData={payload.data} />;
    case 'geography':
      try {
        const mapData = typeof payload.data === 'string' ? JSON.parse(payload.data) : payload.data;
        return <GeographyMapRenderer {...mapData} />;
      } catch (e) {
        return <div className="text-red-500">Error rendering map data</div>;
      }
    case 'graph':
      try {
        const graphData = typeof payload.data === 'string' ? JSON.parse(payload.data) : payload.data;
        return <PlotlyRenderer data={graphData.data} layout={graphData.layout} config={graphData.config} />;
      } catch (e) {
        return <div className="text-red-500">Error rendering graph</div>;
      }
    case 'timeline':
      return <MermaidRenderer chart={payload.data} />;
    case 'diagram':
      return <SVGRenderer svgString={payload.data} title={payload.title} />;
    default:
      return null;
  }
}

export default RenderDispatcher;
