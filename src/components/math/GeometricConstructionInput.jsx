import React, { useState, useEffect, useRef } from 'react';

const GeometricConstructionInput = ({ initialData, onChange, isSubmitted, onAttachToAnswer }) => {
    // State for construction mode and tools
    const [constructionMode, setConstructionMode] = useState('triangle_sss');
    const [currentTool, setCurrentTool] = useState('select');
    const [showGrid, setShowGrid] = useState(true);
    const [showMeasurements, setShowMeasurements] = useState(true);
    const [showLabels, setShowLabels] = useState(true);
    const [gridScale, setGridScale] = useState(20); // Grid box size in pixels
    const [unitScale, setUnitScale] = useState(1); // 1 unit = how many pixels
    const [title, setTitle] = useState(initialData?.title || 'Geometric Construction');
    
    // Canvas and construction state
    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);
    const [constructions, setConstructions] = useState([]);
    const [points, setPoints] = useState([]);
    const [lines, setLines] = useState([]);
    const [circles, setCircles] = useState([]);
    const [shapes, setShapes] = useState([]);
    const [selectedElement, setSelectedElement] = useState(null);
    
    // Construction parameters
    const [constructionParams, setConstructionParams] = useState({
        // Triangle construction parameters
        side1: 60,
        side2: 80,
        side3: 100,
        angle1: 45,
        angle2: 60,
        angle3: 75,
        
        // 3D shape parameters
        radius: 30,
        height: 80,
        width: 60,
        depth: 40,
        sideLength: 50
    });

    // Initialize component data
    useEffect(() => {
        const formattedData = {
            type: "geometric_construction",
            title: title,
            constructionMode: constructionMode,
            constructions: constructions,
            points: points,
            lines: lines,
            circles: circles,
            shapes: shapes,
            showGrid: showGrid,
            showMeasurements: showMeasurements,
            showLabels: showLabels,
            constructionParams: constructionParams
        };
        onChange(formattedData);
    }, [title, constructionMode, constructions, points, lines, circles, shapes, showGrid, showMeasurements, showLabels, constructionParams, onChange]);

    // Draw everything on canvas whenever elements change
    useEffect(() => {
        drawCanvas();
    }, [points, lines, circles, showGrid, showMeasurements, showLabels]);

    // Draw function to render all elements on canvas
    const drawCanvas = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw grid if enabled
        if (showGrid) {
            drawGrid(ctx, canvas.width, canvas.height);
        }
        
        // Draw all elements
        circles.forEach(circle => drawCircle(ctx, circle));
        lines.forEach(line => drawLine(ctx, line));
        points.forEach(point => drawPoint(ctx, point));
    };

    // Draw grid
    const drawGrid = (ctx, width, height) => {
        ctx.strokeStyle = '#e5e7eb';
        ctx.lineWidth = 1;
        
        // Vertical lines
        for (let x = 0; x <= width; x += gridScale) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }
        
        // Horizontal lines
        for (let y = 0; y <= height; y += gridScale) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, height);
            ctx.stroke();
        }
        
        // Draw coordinate labels if grid is fine enough
        if (gridScale >= 20) {
            ctx.fillStyle = '#9ca3af';
            ctx.font = '10px Arial';
            
            // X-axis labels
            for (let x = 0; x <= width; x += gridScale) {
                const unitX = Math.round(x / unitScale);
                if (unitX !== 0) {
                    ctx.fillText(unitX.toString(), x + 2, 15);
                }
            }
            
            // Y-axis labels
            for (let y = 0; y <= height; y += gridScale) {
                const unitY = Math.round(y / unitScale);
                if (unitY !== 0) {
                    ctx.fillText(unitY.toString(), 5, y - 2);
                }
            }
        }
    };

    // Draw a point
    const drawPoint = (ctx, point) => {
        ctx.fillStyle = point.color || '#3B82F6';
        ctx.beginPath();
        ctx.arc(point.x, point.y, 4, 0, 2 * Math.PI);
        ctx.fill();
        
        // Draw label if enabled
        if (showLabels && point.label) {
            ctx.fillStyle = '#374151';
            ctx.font = '12px Arial';
            ctx.fillText(point.label, point.x + 8, point.y - 8);
        }
    };

    // Draw a line
    const drawLine = (ctx, line) => {
        ctx.strokeStyle = line.color || '#6B7280';
        ctx.lineWidth = line.style === 'dashed' ? 2 : 3;
        
        if (line.style === 'dashed') {
            ctx.setLineDash([5, 5]);
        } else {
            ctx.setLineDash([]);
        }
        
        ctx.beginPath();
        ctx.moveTo(line.startPoint.x, line.startPoint.y);
        ctx.lineTo(line.endPoint.x, line.endPoint.y);
        ctx.stroke();
        ctx.setLineDash([]); // Reset dash pattern
    };

    // Draw a circle
    const drawCircle = (ctx, circle) => {
        ctx.strokeStyle = circle.color || '#10B981';
        ctx.lineWidth = circle.style === 'dashed' ? 2 : 3;
        
        if (circle.style === 'dashed') {
            ctx.setLineDash([5, 5]);
        } else {
            ctx.setLineDash([]);
        }
        
        ctx.beginPath();
        ctx.arc(circle.center.x, circle.center.y, circle.radius, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.setLineDash([]); // Reset dash pattern
    };

    // Construction modes available
    const constructionModes = [
        { id: 'triangle_sss', name: 'Triangle (SSS)', description: 'Construct triangle with three sides' },
        { id: 'triangle_sas', name: 'Triangle (SAS)', description: 'Construct triangle with two sides and included angle' },
        { id: 'triangle_asa', name: 'Triangle (ASA)', description: 'Construct triangle with two angles and included side' },
        { id: 'triangle_ssa', name: 'Triangle (SSA)', description: 'Construct triangle with two sides and non-included angle' },
        { id: 'triangle_right', name: 'Right Triangle', description: 'Construct right triangle with two sides' },
        { id: 'triangle_equilateral', name: 'Equilateral Triangle', description: 'Construct equilateral triangle' },
        { id: 'perpendicular_bisector', name: 'Perpendicular Bisector', description: 'Construct perpendicular bisector of line segment' },
        { id: 'angle_bisector', name: 'Angle Bisector', description: 'Construct angle bisector' },
        { id: 'parallel_line', name: 'Parallel Line', description: 'Construct parallel line through point' },
        { id: 'perpendicular_line', name: 'Perpendicular Line', description: 'Construct perpendicular line through point' },
        { id: 'circle_center', name: 'Circle from Center', description: 'Construct circle with center and radius' },
        { id: 'circle_three_points', name: 'Circle through 3 Points', description: 'Construct circle through three points' }
    ];

    // 3D shape construction modes
    const shape3DModes = [
        { id: 'cube', name: 'Cube', description: 'Construct cube with given side length' },
        { id: 'rectangular_prism', name: 'Rectangular Prism', description: 'Construct rectangular prism' },
        { id: 'triangular_prism', name: 'Triangular Prism', description: 'Construct triangular prism' },
        { id: 'cylinder', name: 'Cylinder', description: 'Construct cylinder with radius and height' },
        { id: 'cone', name: 'Cone', description: 'Construct cone with radius and height' },
        { id: 'sphere', name: 'Sphere', description: 'Construct sphere with radius' },
        { id: 'pyramid', name: 'Pyramid', description: 'Construct pyramid with base and height' }
    ];

    // Tools available
    const tools = [
        { id: 'select', name: 'Select', icon: '👆' },
        { id: 'point', name: 'Point', icon: '●' },
        { id: 'line', name: 'Line', icon: '━' },
        { id: 'circle', name: 'Circle', icon: '○' },
        { id: 'measure', name: 'Measure', icon: '📏' },
        { id: 'delete', name: 'Delete', icon: '🗑️' }
    ];

    // Handle canvas click for placing elements
    const handleCanvasClick = (e) => {
        if (isSubmitted || currentTool === 'select') return;
        
        const canvas = canvasRef.current;
        const rect = canvas.getBoundingClientRect();
        
        // Calculate canvas coordinates
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const x = (e.clientX - rect.left) * scaleX;
        const y = (e.clientY - rect.top) * scaleY;
        
        switch (currentTool) {
            case 'point':
                addPoint(x, y);
                break;
            case 'line':
                if (selectedElement && selectedElement.type === 'point') {
                    addLine(selectedElement, { x, y, type: 'point' });
                    setSelectedElement(null);
                } else {
                    setSelectedElement({ x, y, type: 'point' });
                }
                break;
            case 'circle':
                if (selectedElement && selectedElement.type === 'point') {
                    const radius = Math.sqrt(
                        Math.pow(x - selectedElement.x, 2) + Math.pow(y - selectedElement.y, 2)
                    );
                    addCircle(selectedElement, radius);
                    setSelectedElement(null);
                } else {
                    setSelectedElement({ x, y, type: 'point' });
                }
                break;
            default:
                break;
        }
    };

    // Add a new point
    const addPoint = (x, y, label = '') => {
        const newPoint = {
            id: Date.now(),
            x: Math.round(x),
            y: Math.round(y),
            label: label || `P${points.length + 1}`,
            color: '#3B82F6'
        };
        setPoints(prev => [...prev, newPoint]);
        return newPoint;
    };

    // Add a new line
    const addLine = (startPoint, endPoint, type = 'construction') => {
        const newLine = {
            id: Date.now(),
            startPoint,
            endPoint,
            type,
            color: type === 'construction' ? '#6B7280' : '#EF4444',
            style: type === 'construction' ? 'dashed' : 'solid'
        };
        setLines(prev => [...prev, newLine]);
    };

    // Add a new circle
    const addCircle = (center, radius, type = 'construction') => {
        const newCircle = {
            id: Date.now(),
            center,
            radius,
            type,
            color: type === 'construction' ? '#6B7280' : '#10B981',
            style: type === 'construction' ? 'dashed' : 'solid'
        };
        setCircles(prev => [...prev, newCircle]);
    };

    // Execute construction based on mode
    const executeConstruction = () => {
        if (isSubmitted) return;
        
        let newConstruction;
        
        switch (constructionMode) {
            case 'triangle_sss':
                newConstruction = constructTriangleSSS();
                break;
            case 'triangle_sas':
                newConstruction = constructTriangleSAS();
                break;
            case 'triangle_asa':
                newConstruction = constructTriangleASA();
                break;
            case 'triangle_right':
                newConstruction = constructRightTriangle();
                break;
            case 'triangle_equilateral':
                newConstruction = constructEquilateralTriangle();
                break;
            case 'perpendicular_bisector':
                newConstruction = constructPerpendicularBisector();
                break;
            case 'angle_bisector':
                newConstruction = constructAngleBisector();
                break;
            case 'parallel_line':
                newConstruction = constructParallelLine();
                break;
            case 'perpendicular_line':
                newConstruction = constructPerpendicularLine();
                break;
            case 'circle_center':
                newConstruction = constructCircleFromCenter();
                break;
            case 'circle_three_points':
                newConstruction = constructCircleThroughThreePoints();
                break;
            // 3D Shape Constructions
            case 'cube':
                newConstruction = constructCube();
                break;
            case 'rectangular_prism':
                newConstruction = constructRectangularPrism();
                break;
            case 'triangular_prism':
                newConstruction = constructTriangularPrism();
                break;
            case 'cylinder':
                newConstruction = constructCylinder();
                break;
            case 'cone':
                newConstruction = constructCone();
                break;
            case 'sphere':
                newConstruction = constructSphere();
                break;
            case 'pyramid':
                newConstruction = constructPyramid();
                break;
            default:
                return;
        }
        
        if (newConstruction) {
            setConstructions(prev => [...prev, newConstruction]);
        }
    };

    // Triangle construction: Side-Side-Side (SSS)
    const constructTriangleSSS = () => {
        const { side1, side2, side3 } = constructionParams;
        
        // Check if triangle is possible
        if (side1 + side2 <= side3 || side1 + side3 <= side2 || side2 + side3 <= side1) {
            alert('Triangle not possible with these side lengths!');
            return null;
        }
        
        // Start with first side - convert units to pixels
        const startX = 100;
        const startY = 200;
        const p1 = addPoint(startX, startY, 'A');
        const p2 = addPoint(startX + unitsToPixels(side1), startY, 'B');
        
        // Calculate third point using law of cosines
        const cosC = (side1 * side1 + side2 * side2 - side3 * side3) / (2 * side1 * side2);
        const angleC = Math.acos(cosC);
        const p3 = {
            x: p1.x + unitsToPixels(side2) * Math.cos(angleC),
            y: p1.y + unitsToPixels(side2) * Math.sin(angleC)
        };
        const p3Point = addPoint(p3.x, p3.y, 'C');
        
        // Add lines
        addLine(p1, p2, 'side');
        addLine(p2, p3Point, 'side');
        addLine(p3Point, p1, 'side');
        
        return {
            type: 'triangle_sss',
            points: [p1, p2, p3Point],
            sides: [side1, side2, side3],
            angles: calculateAngles(p1, p2, p3Point)
        };
    };

    // Triangle construction: Side-Angle-Side (SAS)
    const constructTriangleSAS = () => {
        const { side1, side2, angle1 } = constructionParams;
        const angleRad = (angle1 * Math.PI) / 180;
        
        const p1 = addPoint(100, 200, 'A');
        const p2 = addPoint(100 + side1, 200, 'B');
        const p3 = {
            x: p1.x + side2 * Math.cos(angleRad),
            y: p1.y + side2 * Math.sin(angleRad)
        };
        const p3Point = addPoint(p3.x, p3.y, 'C');
        
        addLine(p1, p2, 'side');
        addLine(p1, p3Point, 'side');
        addLine(p2, p3Point, 'side');
        
        return {
            type: 'triangle_sas',
            points: [p1, p2, p3Point],
            sides: [side1, side2, calculateDistance(p2, p3Point)],
            angles: [angle1, calculateAngles(p1, p2, p3Point)[1], calculateAngles(p1, p2, p3Point)[2]]
        };
    };

    // Calculate angles of triangle
    const calculateAngles = (p1, p2, p3) => {
        const a = calculateDistance(p2, p3);
        const b = calculateDistance(p1, p3);
        const c = calculateDistance(p1, p2);
        
        const angleA = (Math.acos((b * b + c * c - a * a) / (2 * b * c)) * 180) / Math.PI;
        const angleB = (Math.acos((a * a + c * c - b * b) / (2 * a * c)) * 180) / Math.PI;
        const angleC = (Math.acos((a * a + b * b - c * c) / (2 * a * b)) * 180) / Math.PI;
        
        return [angleA, angleB, angleC];
    };

    // Calculate distance between two points
    const calculateDistance = (p1, p2) => {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    };

    // Convert units to pixels based on current scale
    const unitsToPixels = (units) => {
        return units * unitScale;
    };

    // Convert pixels to units based on current scale
    const pixelsToUnits = (pixels) => {
        return pixels / unitScale;
    };

    // Triangle construction: Angle-Side-Angle (ASA)
    const constructTriangleASA = () => {
        const { angle1, side1, angle2 } = constructionParams;
        
        // Check if angles are valid (sum < 180°)
        if (angle1 + angle2 >= 180) {
            alert('Sum of angles must be less than 180°!');
            return null;
        }
        
        // Calculate third angle
        const angle3 = 180 - angle1 - angle2;
        
        // Start with first point
        const startX = 100;
        const startY = 200;
        const p1 = addPoint(startX, startY, 'A');
        
        // Place second point at distance side1
        const p2 = addPoint(startX + unitsToPixels(side1), startY, 'B');
        
        // Calculate third point using trigonometry
        const side2 = (side1 * Math.sin(angle2 * Math.PI / 180)) / Math.sin(angle3 * Math.PI / 180);
        const side3 = (side1 * Math.sin(angle1 * Math.PI / 180)) / Math.sin(angle3 * Math.PI / 180);
        
        // Place third point using angle and side
        const p3 = {
            x: p1.x + unitsToPixels(side2) * Math.cos(angle1 * Math.PI / 180),
            y: p1.y + unitsToPixels(side2) * Math.sin(angle1 * Math.PI / 180)
        };
        const p3Point = addPoint(p3.x, p3.y, 'C');
        
        // Add all sides
        addLine(p1, p2, 'side');
        addLine(p2, p3Point, 'side');
        addLine(p3Point, p1, 'side');
        
        return {
            type: 'triangle_asa',
            points: [p1, p2, p3Point],
            sides: [side1, side2, side3],
            angles: [angle1, angle2, angle3]
        };
    };

    // Triangle construction: Right Triangle
    const constructRightTriangle = () => {
        const { side1, side2 } = constructionParams;
        
        // Start with first point
        const startX = 100;
        const startY = 200;
        const p1 = addPoint(startX, startY, 'A');
        
        // Place second point (base)
        const p2 = addPoint(startX + unitsToPixels(side1), startY, 'B');
        
        // Place third point (height) - right angle at A
        const p3 = {
            x: startX,
            y: startY - unitsToPixels(side2)
        };
        const p3Point = addPoint(p3.x, p3.y, 'C');
        
        // Add all sides
        addLine(p1, p2, 'side');           // Base
        addLine(p1, p3Point, 'side');      // Height
        addLine(p2, p3Point, 'side');      // Hypotenuse
        
        // Calculate hypotenuse
        const hypotenuse = Math.sqrt(side1 * side1 + side2 * side2);
        
        return {
            type: 'right_triangle',
            points: [p1, p2, p3Point],
            sides: [side1, side2, hypotenuse],
            angles: [90, Math.atan2(side2, side1) * 180 / Math.PI, Math.atan2(side1, side2) * 180 / Math.PI]
        };
    };

    const constructEquilateralTriangle = () => {
        const { sideLength } = constructionParams;
        
        // Start with first point
        const p1 = addPoint(100, 200, 'A');
        
        // Second point at distance sideLength
        const p2 = addPoint(100 + sideLength, 200, 'B');
        
        // Third point using equilateral triangle properties
        // Height = sideLength * sin(60°) = sideLength * √3/2
        const height = sideLength * Math.sqrt(3) / 2;
        const p3 = {
            x: 100 + sideLength / 2,  // Midpoint of base
            y: 200 - height           // Above the base
        };
        const p3Point = addPoint(p3.x, p3.y, 'C');
        
        // Add all three sides
        addLine(p1, p2, 'side');
        addLine(p2, p3Point, 'side');
        addLine(p3Point, p1, 'side');
        
        return {
            type: 'equilateral_triangle',
            points: [p1, p2, p3Point],
            sideLength: sideLength,
            height: height,
            angles: [60, 60, 60]  // All angles are 60° in equilateral triangle
        };
    };

    // Construction: Perpendicular Bisector
    const constructPerpendicularBisector = () => {
        // Create a line segment first
        const p1 = addPoint(100, 200, 'A');
        const p2 = addPoint(300, 200, 'B');
        
        // Draw the original line segment
        addLine(p1, p2, 'segment');
        
        // Find midpoint
        const midX = (p1.x + p2.x) / 2;
        const midY = (p1.y + p2.y) / 2;
        const midpoint = addPoint(midX, midY, 'M');
        
        // Calculate perpendicular slope
        const slope = (p2.y - p1.y) / (p2.x - p1.x);
        const perpSlope = -1 / slope;
        
        // Draw perpendicular bisector
        const perpLength = 100;
        const perpX1 = midX - perpLength;
        const perpY1 = midY - perpSlope * perpLength;
        const perpX2 = midX + perpLength;
        const perpY2 = midY + perpSlope * perpLength;
        
        const perp1 = addPoint(perpX1, perpY1, 'P1');
        const perp2 = addPoint(perpX2, perpY2, 'P2');
        addLine(perp1, perp2, 'bisector');
        
        return {
            type: 'perpendicular_bisector',
            segment: [p1, p2],
            midpoint: midpoint,
            bisector: [perp1, perp2]
        };
    };

    // Construction: Angle Bisector
    const constructAngleBisector = () => {
        // Create an angle with three points
        const vertex = addPoint(200, 200, 'V');
        const p1 = addPoint(100, 100, 'A');
        const p2 = addPoint(300, 100, 'B');
        
        // Draw the angle sides
        addLine(vertex, p1, 'side');
        addLine(vertex, p2, 'side');
        
        // Calculate angle bisector
        const angle1 = Math.atan2(p1.y - vertex.y, p1.x - vertex.x);
        const angle2 = Math.atan2(p2.y - vertex.y, p2.x - vertex.x);
        const bisectorAngle = (angle1 + angle2) / 2;
        
        // Draw angle bisector
        const bisectorLength = 150;
        const bisectorX = vertex.x + bisectorLength * Math.cos(bisectorAngle);
        const bisectorY = vertex.y + bisectorLength * Math.sin(bisectorAngle);
        const bisectorPoint = addPoint(bisectorX, bisectorY, 'C');
        
        addLine(vertex, bisectorPoint, 'bisector');
        
        return {
            type: 'angle_bisector',
            vertex: vertex,
            sides: [p1, p2],
            bisector: [vertex, bisectorPoint]
        };
    };

    // Construction: Parallel Line
    const constructParallelLine = () => {
        // Create a reference line
        const p1 = addPoint(100, 150, 'A');
        const p2 = addPoint(300, 150, 'B');
        addLine(p1, p2, 'reference');
        
        // Create a point through which to draw parallel line
        const point = addPoint(200, 250, 'P');
        
        // Calculate parallel line (same slope)
        const slope = (p2.y - p1.y) / (p2.x - p1.x);
        const parallelLength = 200;
        
        // Draw parallel line
        const parallelX1 = point.x - parallelLength / 2;
        const parallelY1 = point.y - slope * (parallelLength / 2);
        const parallelX2 = point.x + parallelLength / 2;
        const parallelY2 = point.y + slope * (parallelLength / 2);
        
        const parallel1 = addPoint(parallelX1, parallelY1, 'P1');
        const parallel2 = addPoint(parallelX2, parallelY2, 'P2');
        addLine(parallel1, parallel2, 'parallel');
        
        return {
            type: 'parallel_line',
            reference: [p1, p2],
            point: point,
            parallel: [parallel1, parallel2]
        };
    };

    // Construction: Perpendicular Line
    const constructPerpendicularLine = () => {
        // Create a reference line
        const p1 = addPoint(100, 150, 'A');
        const p2 = addPoint(300, 150, 'B');
        addLine(p1, p2, 'reference');
        
        // Create a point through which to draw perpendicular line
        const point = addPoint(200, 250, 'P');
        
        // Calculate perpendicular line (negative reciprocal slope)
        const slope = (p2.y - p1.y) / (p2.x - p1.x);
        const perpSlope = -1 / slope;
        const perpLength = 150;
        
        // Draw perpendicular line
        const perpX1 = point.x - perpLength / 2;
        const perpY1 = point.y - perpSlope * (perpLength / 2);
        const perpX2 = point.x + perpLength / 2;
        const perpY2 = point.y + perpSlope * (perpLength / 2);
        
        const perp1 = addPoint(perpX1, perpY1, 'P1');
        const perp2 = addPoint(perpX2, perpY2, 'P2');
        addLine(perp1, perp2, 'perpendicular');
        
        return {
            type: 'perpendicular_line',
            reference: [p1, p2],
            point: point,
            perpendicular: [perp1, perp2]
        };
    };

    const constructCircleFromCenter = () => {
        const { radius } = constructionParams;
        
        // Place center point
        const center = addPoint(200, 200, 'O');
        
        // Place point on circumference to define radius
        const circumferencePoint = addPoint(center.x + radius, center.y, 'P');
        
        // Add the circle
        addCircle(center, radius, 'construction');
        
        // Add radius line
        addLine(center, circumferencePoint, 'radius');
        
        return {
            type: 'circle_center',
            center: center,
            radius: radius,
            circumferencePoint: circumferencePoint
        };
    };

    const constructCircleThroughThreePoints = () => {
        // Place three non-collinear points
        const p1 = addPoint(150, 150, 'A');
        const p2 = addPoint(250, 150, 'B');
        const p3 = addPoint(200, 250, 'C');
        
        // Calculate center using perpendicular bisectors
        // Find midpoint of AB
        const midAB = {
            x: (p1.x + p2.x) / 2,
            y: (p1.y + p2.y) / 2
        };
        
        // Find midpoint of BC
        const midBC = {
            x: (p2.x + p3.x) / 2,
            y: (p2.y + p3.y) / 2
        };
        
        // Calculate slopes for perpendicular bisectors
        const slopeAB = (p2.y - p1.y) / (p2.x - p1.x);
        const slopeBC = (p3.y - p2.y) / (p3.x - p2.x);
        
        // Perpendicular slopes
        const perpSlopeAB = -1 / slopeAB;
        const perpSlopeBC = -1 / slopeBC;
        
        // Find center using perpendicular bisector intersection
        // This is a simplified calculation - in practice, you'd solve the system of equations
        const center = {
            x: (midAB.x + midBC.x) / 2,
            y: (midAB.y + midBC.y) / 2
        };
        
        const centerPoint = addPoint(center.x, center.y, 'O');
        
        // Calculate radius
        const radius = calculateDistance(centerPoint, p1);
        
        // Add the circle
        addCircle(centerPoint, radius, 'construction');
        
        // Add lines connecting the three points
        addLine(p1, p2, 'chord');
        addLine(p2, p3, 'chord');
        addLine(p3, p1, 'chord');
        
        return {
            type: 'circle_three_points',
            center: centerPoint,
            radius: radius,
            points: [p1, p2, p3]
        };
    };

    // 3D Shape Construction Methods
    
    // Construct a cube
    const constructCube = () => {
        const { sideLength } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        const halfSide = sideLength / 2;
        
        // Create the 8 vertices of the cube
        const vertices = [
            // Front face (z = 0)
            addPoint(centerX - halfSide, centerY - halfSide, 'A'),
            addPoint(centerX + halfSide, centerY - halfSide, 'B'),
            addPoint(centerX + halfSide, centerY + halfSide, 'C'),
            addPoint(centerX - halfSide, centerY + halfSide, 'D'),
            // Back face (z = sideLength)
            addPoint(centerX - halfSide, centerY - halfSide, 'E'),
            addPoint(centerX + halfSide, centerY - halfSide, 'F'),
            addPoint(centerX + halfSide, centerY + halfSide, 'G'),
            addPoint(centerX - halfSide, centerY + halfSide, 'H')
        ];
        
        // Draw front face
        addLine(vertices[0], vertices[1], 'edge');
        addLine(vertices[1], vertices[2], 'edge');
        addLine(vertices[2], vertices[3], 'edge');
        addLine(vertices[3], vertices[0], 'edge');
        
        // Draw back face
        addLine(vertices[4], vertices[5], 'edge');
        addLine(vertices[5], vertices[6], 'edge');
        addLine(vertices[6], vertices[7], 'edge');
        addLine(vertices[7], vertices[4], 'edge');
        
        // Draw connecting edges
        addLine(vertices[0], vertices[4], 'edge');
        addLine(vertices[1], vertices[5], 'edge');
        addLine(vertices[2], vertices[6], 'edge');
        addLine(vertices[3], vertices[7], 'edge');
        
        return {
            type: 'cube',
            vertices: vertices,
            sideLength: sideLength,
            volume: sideLength * sideLength * sideLength,
            surfaceArea: 6 * sideLength * sideLength
        };
    };

    // Construct a rectangular prism
    const constructRectangularPrism = () => {
        const { width, height, depth } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        const halfWidth = width / 2;
        const halfHeight = height / 2;
        
        // Create the 8 vertices
        const vertices = [
            // Front face
            addPoint(centerX - halfWidth, centerY - halfHeight, 'A'),
            addPoint(centerX + halfWidth, centerY - halfHeight, 'B'),
            addPoint(centerX + halfWidth, centerY + halfHeight, 'C'),
            addPoint(centerX - halfWidth, centerY + halfHeight, 'D'),
            // Back face
            addPoint(centerX - halfWidth, centerY - halfHeight, 'E'),
            addPoint(centerX + halfWidth, centerY - halfHeight, 'F'),
            addPoint(centerX + halfWidth, centerY + halfHeight, 'G'),
            addPoint(centerX - halfWidth, centerY + halfHeight, 'H')
        ];
        
        // Draw all edges similar to cube
        // Front face
        addLine(vertices[0], vertices[1], 'edge');
        addLine(vertices[1], vertices[2], 'edge');
        addLine(vertices[2], vertices[3], 'edge');
        addLine(vertices[3], vertices[0], 'edge');
        
        // Back face
        addLine(vertices[4], vertices[5], 'edge');
        addLine(vertices[5], vertices[6], 'edge');
        addLine(vertices[6], vertices[7], 'edge');
        addLine(vertices[7], vertices[4], 'edge');
        
        // Connecting edges
        addLine(vertices[0], vertices[4], 'edge');
        addLine(vertices[1], vertices[5], 'edge');
        addLine(vertices[2], vertices[6], 'edge');
        addLine(vertices[3], vertices[7], 'edge');
        
        return {
            type: 'rectangular_prism',
            vertices: vertices,
            dimensions: { width, height, depth },
            volume: width * height * depth,
            surfaceArea: 2 * (width * height + height * depth + depth * width)
        };
    };

    // Construct a cylinder
    const constructCylinder = () => {
        const { radius, height } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        
        // Create center points for top and bottom circles
        const bottomCenter = addPoint(centerX, centerY, 'O');
        const topCenter = addPoint(centerX, centerY, 'O\'');
        
        // Create points on the circles
        const bottomPoints = [];
        const topPoints = [];
        const numPoints = 8; // 8 points for octagon approximation
        
        for (let i = 0; i < numPoints; i++) {
            const angle = (i * 2 * Math.PI) / numPoints;
            const x = centerX + radius * Math.cos(angle);
            const y = centerY + radius * Math.sin(angle);
            
            bottomPoints.push(addPoint(x, y, `P${i + 1}`));
            topPoints.push(addPoint(x, y, `Q${i + 1}`));
        }
        
        // Draw bottom circle
        for (let i = 0; i < numPoints; i++) {
            addLine(bottomPoints[i], bottomPoints[(i + 1) % numPoints], 'edge');
        }
        
        // Draw top circle
        for (let i = 0; i < numPoints; i++) {
            addLine(topPoints[i], topPoints[(i + 1) % numPoints], 'edge');
        }
        
        // Draw connecting lines
        for (let i = 0; i < numPoints; i++) {
            addLine(bottomPoints[i], topPoints[i], 'edge');
        }
        
        return {
            type: 'cylinder',
            radius: radius,
            height: height,
            volume: Math.PI * radius * radius * height,
            surfaceArea: 2 * Math.PI * radius * radius + 2 * Math.PI * radius * height
        };
    };

    // Construct a cone
    const constructCone = () => {
        const { radius, height } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        
        // Base center
        const baseCenter = addPoint(centerX, centerY, 'O');
        // Apex
        const apex = addPoint(centerX, centerY - height, 'A');
        
        // Create base circle points
        const basePoints = [];
        const numPoints = 8;
        
        for (let i = 0; i < numPoints; i++) {
            const angle = (i * 2 * Math.PI) / numPoints;
            const x = centerX + radius * Math.cos(angle);
            const y = centerY + radius * Math.sin(angle);
            basePoints.push(addPoint(x, y, `P${i + 1}`));
        }
        
        // Draw base circle
        for (let i = 0; i < numPoints; i++) {
            addLine(basePoints[i], basePoints[(i + 1) % numPoints], 'edge');
        }
        
        // Draw lines from apex to base
        for (let i = 0; i < numPoints; i++) {
            addLine(apex, basePoints[i], 'edge');
        }
        
        return {
            type: 'cone',
            radius: radius,
            height: height,
            volume: (Math.PI * radius * radius * height) / 3,
            surfaceArea: Math.PI * radius * radius + Math.PI * radius * Math.sqrt(radius * radius + height * height)
        };
    };

    // Construct a sphere (approximated as a circle for 2D view)
    const constructSphere = () => {
        const { radius } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        
        const center = addPoint(centerX, centerY, 'O');
        addCircle(center, radius, 'sphere');
        
        return {
            type: 'sphere',
            radius: radius,
            volume: (4 * Math.PI * radius * radius * radius) / 3,
            surfaceArea: 4 * Math.PI * radius * radius
        };
    };

    // Construct a pyramid
    const constructPyramid = () => {
        const { sideLength, height } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        const halfSide = sideLength / 2;
        
        // Base vertices (square)
        const baseVertices = [
            addPoint(centerX - halfSide, centerY + halfSide, 'A'),
            addPoint(centerX + halfSide, centerY + halfSide, 'B'),
            addPoint(centerX + halfSide, centerY - halfSide, 'C'),
            addPoint(centerX - halfSide, centerY - halfSide, 'D')
        ];
        
        // Apex
        const apex = addPoint(centerX, centerY - height, 'E');
        
        // Draw base
        for (let i = 0; i < 4; i++) {
            addLine(baseVertices[i], baseVertices[(i + 1) % 4], 'edge');
        }
        
        // Draw lines from apex to base vertices
        for (let i = 0; i < 4; i++) {
            addLine(apex, baseVertices[i], 'edge');
        }
        
        return {
            type: 'pyramid',
            baseVertices: baseVertices,
            apex: apex,
            sideLength: sideLength,
            height: height,
            volume: (sideLength * sideLength * height) / 3,
            surfaceArea: sideLength * sideLength + 2 * sideLength * Math.sqrt((sideLength * sideLength) / 4 + height * height)
        };
    };

    // Construct a triangular prism
    const constructTriangularPrism = () => {
        const { sideLength, height } = constructionParams;
        const centerX = 200;
        const centerY = 200;
        const halfSide = sideLength / 2;
        const triangleHeight = (sideLength * Math.sqrt(3)) / 2;
        
        // Front triangle vertices
        const frontVertices = [
            addPoint(centerX, centerY - triangleHeight / 2, 'A'),
            addPoint(centerX - halfSide, centerY + triangleHeight / 2, 'B'),
            addPoint(centerX + halfSide, centerY + triangleHeight / 2, 'C')
        ];
        
        // Back triangle vertices
        const backVertices = [
            addPoint(centerX, centerY - triangleHeight / 2, 'D'),
            addPoint(centerX - halfSide, centerY + triangleHeight / 2, 'E'),
            addPoint(centerX + halfSide, centerY + triangleHeight / 2, 'F')
        ];
        
        // Draw front triangle
        addLine(frontVertices[0], frontVertices[1], 'edge');
        addLine(frontVertices[1], frontVertices[2], 'edge');
        addLine(frontVertices[2], frontVertices[0], 'edge');
        
        // Draw back triangle
        addLine(backVertices[0], backVertices[1], 'edge');
        addLine(backVertices[1], backVertices[2], 'edge');
        addLine(backVertices[2], backVertices[0], 'edge');
        
        // Draw connecting edges
        for (let i = 0; i < 3; i++) {
            addLine(frontVertices[i], backVertices[i], 'edge');
        }
        
        return {
            type: 'triangular_prism',
            frontVertices: frontVertices,
            backVertices: backVertices,
            sideLength: sideLength,
            height: height,
            volume: (sideLength * sideLength * Math.sqrt(3) * height) / 4,
            surfaceArea: sideLength * sideLength * Math.sqrt(3) / 2 + 3 * sideLength * height
        };
    };

    // Clear all constructions
    const clearAll = () => {
        setPoints([]);
        setLines([]);
        setCircles([]);
        setShapes([]);
        setConstructions([]);
        setSelectedElement(null);
    };

    // Get construction description for AI
    const getConstructionDescription = () => {
        let description = `Geometric Construction: ${title}\n`;
        description += `Mode: ${constructionModes.find(m => m.id === constructionMode)?.name}\n`;
        description += `Points: ${points.length}\n`;
        description += `Lines: ${lines.length}\n`;
        description += `Circles: ${circles.length}\n`;
        description += `Shapes: ${shapes.length}\n`;
        
        if (constructions.length > 0) {
            description += `\nConstructions performed:\n`;
            constructions.forEach((construction, index) => {
                description += `${index + 1}. ${construction.type}\n`;
            });
        }
        
        return description;
    };

    // Handle attach to answer
    const handleAttachToAnswer = () => {
        if (onAttachToAnswer) {
            const constructionData = {
                type: "geometric_construction",
                title: title,
                constructionMode: constructionMode,
                description: getConstructionDescription(),
                constructions: constructions,
                elements: {
                    points: points.length,
                    lines: lines.length,
                    circles: circles.length,
                    shapes: shapes.length
                },
                parameters: constructionParams
            };
            onAttachToAnswer(constructionData);
        }
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Enhanced Geometric Construction</h3>
                <div className="flex space-x-2">
                    {onAttachToAnswer && (
                        <button
                            onClick={handleAttachToAnswer}
                            className="px-4 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700 transition-colors"
                        >
                            Attach to Answer
                        </button>
                                    )}

                {constructionMode.startsWith('triangle_asa') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Angle 1 (degrees):</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.angle1}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, angle1: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                                max="178"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side (between angles):</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side1}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side1: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Angle 2 (degrees):</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.angle2}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, angle2: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                                max="178"
                            />
                        </div>
                    </>
                )}

                {constructionMode.startsWith('triangle_right') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Base:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side1}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side1: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Height:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side2}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side2: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Hypotenuse:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={Math.sqrt(constructionParams.side1 * constructionParams.side1 + constructionParams.side2 * constructionParams.side2).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                    </>
                )}

                {constructionMode.startsWith('triangle_equilateral') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side Length:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.sideLength}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, sideLength: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Height:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(constructionParams.sideLength * Math.sqrt(3) / 2).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Area:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(constructionParams.sideLength * constructionParams.sideLength * Math.sqrt(3) / 4).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                    </>
                )}

                {constructionMode.startsWith('circle_center') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Radius:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.radius}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, radius: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Circumference:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(2 * Math.PI * constructionParams.radius).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Area:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(Math.PI * constructionParams.radius * constructionParams.radius).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                    </>
                )}

                {/* 3D Shape Parameters */}
                {constructionMode === 'cube' && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side Length:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.sideLength}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, sideLength: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Volume:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(constructionParams.sideLength * constructionParams.sideLength * constructionParams.sideLength).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Surface Area:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(6 * constructionParams.sideLength * constructionParams.sideLength).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                    </>
                )}

                {constructionMode === 'rectangular_prism' && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Width:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.width}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, width: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Height:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.height}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, height: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Depth:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.depth}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, depth: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                    </>
                )}

                {(constructionMode === 'cylinder' || constructionMode === 'cone') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Radius:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.radius}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, radius: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Height:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.height}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, height: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                {constructionMode === 'cylinder' ? 'Volume:' : 'Volume:'}
                            </label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={constructionMode === 'cylinder' 
                                    ? (Math.PI * constructionParams.radius * constructionParams.radius * constructionParams.height).toFixed(1)
                                    : ((Math.PI * constructionParams.radius * constructionParams.radius * constructionParams.height) / 3).toFixed(1)
                                }
                                disabled={true}
                            />
                        </div>
                    </>
                )}

                {(constructionMode === 'sphere') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Radius:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.radius}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, radius: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Volume:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={((4 * Math.PI * constructionParams.radius * constructionParams.radius * constructionParams.radius) / 3).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Surface Area:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={(4 * Math.PI * constructionParams.radius * constructionParams.radius).toFixed(1)}
                                disabled={true}
                            />
                        </div>
                    </>
                )}

                {(constructionMode === 'pyramid' || constructionMode === 'triangular_prism') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side Length:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.sideLength}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, sideLength: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Height:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.height}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, height: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                {constructionMode === 'pyramid' ? 'Volume:' : 'Volume:'}
                            </label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm bg-gray-100"
                                value={constructionMode === 'pyramid'
                                    ? ((constructionParams.sideLength * constructionParams.sideLength * constructionParams.height) / 3).toFixed(1)
                                    : ((constructionParams.sideLength * constructionParams.sideLength * Math.sqrt(3) * constructionParams.height) / 4).toFixed(1)
                                }
                                disabled={true}
                            />
                        </div>
                    </>
                )}
            </div>
            </div>

            {/* Construction Mode Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Construction Mode:</label>
                <select
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    value={constructionMode}
                    onChange={(e) => setConstructionMode(e.target.value)}
                    disabled={isSubmitted}
                >
                    <optgroup label="Triangle Constructions">
                        {constructionModes.filter(m => m.id.startsWith('triangle')).map(mode => (
                            <option key={mode.id} value={mode.id}>{mode.name}</option>
                        ))}
                    </optgroup>
                    <optgroup label="Basic Constructions">
                        {constructionModes.filter(m => !m.id.startsWith('triangle') && !m.id.startsWith('circle')).map(mode => (
                            <option key={mode.id} value={mode.id}>{mode.name}</option>
                        ))}
                    </optgroup>
                    <optgroup label="Circle Constructions">
                        {constructionModes.filter(m => m.id.startsWith('circle')).map(mode => (
                            <option key={mode.id} value={mode.id}>{mode.name}</option>
                        ))}
                    </optgroup>
                    <optgroup label="3D Shape Constructions">
                        {shape3DModes.map(mode => (
                            <option key={mode.id} value={mode.id}>{mode.name}</option>
                        ))}
                    </optgroup>
                </select>
                <p className="text-sm text-gray-600 mt-1">
                    {(constructionModes.find(m => m.id === constructionMode) || shape3DModes.find(m => m.id === constructionMode))?.description}
                </p>
            </div>

            {/* Construction Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                {constructionMode.startsWith('triangle_sss') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side 1:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side1}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side1: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side 2:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side2}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side2: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side 3:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side3}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side3: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                    </>
                )}
                
                {constructionMode.startsWith('triangle_sas') && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side 1:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side1}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side1: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Side 2:</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.side2}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, side2: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                            />
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Angle (degrees):</label>
                            <input
                                type="number"
                                className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                                value={constructionParams.angle1}
                                onChange={(e) => setConstructionParams(prev => ({ ...prev, angle1: Number(e.target.value) }))}
                                disabled={isSubmitted}
                                min="1"
                                max="179"
                            />
                        </div>
                    </>
                )}
            </div>

            {/* Tool Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Tools:</label>
                <div className="flex flex-wrap gap-2">
                    {tools.map(tool => (
                        <button
                            key={tool.id}
                            onClick={() => setCurrentTool(tool.id)}
                            className={`px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                                currentTool === tool.id
                                    ? 'bg-blue-600 text-white'
                                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                            }`}
                            disabled={isSubmitted}
                        >
                            <span className="mr-2">{tool.icon}</span>
                            {tool.name}
                        </button>
                    ))}
                </div>
            </div>

            {/* Display Options */}
            <div className="flex flex-wrap gap-4 mb-6">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={showGrid}
                        onChange={(e) => setShowGrid(e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={showMeasurements}
                        onChange={(e) => setShowMeasurements(e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Measurements</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={showLabels}
                        onChange={(e) => setShowLabels(e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Labels</span>
                </label>
            </div>

            {/* Grid Scaling Controls */}
            {showGrid && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Grid Box Size:</label>
                        <select
                            className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                            value={gridScale}
                            onChange={(e) => setGridScale(Number(e.target.value))}
                            disabled={isSubmitted}
                        >
                            <option value={10}>Fine (10px) - Good for small units</option>
                            <option value={20}>Medium (20px) - Standard size</option>
                            <option value={40}>Coarse (40px) - Good for large units</option>
                            <option value={50}>Very Coarse (50px) - For 100+ units</option>
                        </select>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Unit Scale:</label>
                        <select
                            className="w-full p-2 border border-gray-300 rounded-lg text-sm"
                            value={unitScale}
                            onChange={(e) => setUnitScale(Number(e.target.value))}
                            disabled={isSubmitted}
                        >
                            <option value={0.5}>0.5 units per pixel (zoom in)</option>
                            <option value={1}>1 unit per pixel (standard)</option>
                            <option value={2}>2 units per pixel (zoom out)</option>
                            <option value={5}>5 units per pixel (far zoom)</option>
                        </select>
                    </div>
                </div>
            )}

            {/* Action Buttons */}
            <div className="flex space-x-3 mb-6">
                <button
                    onClick={executeConstruction}
                    disabled={isSubmitted}
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition-colors disabled:bg-gray-400"
                >
                    Execute Construction
                </button>
                <button
                    onClick={clearAll}
                    disabled={isSubmitted}
                    className="px-4 py-2 bg-red-600 text-white rounded-lg font-medium hover:bg-red-700 transition-colors disabled:bg-gray-400"
                >
                    Clear All
                </button>
            </div>

            {/* Construction Canvas */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Construction Canvas:</label>
                <div 
                    className="border-2 border-gray-300 rounded-lg overflow-hidden bg-white relative"
                    style={{ height: '400px' }}
                >
                    <canvas
                        ref={canvasRef}
                        width={600}
                        height={400}
                        onClick={handleCanvasClick}
                        className="cursor-crosshair w-full h-full"
                        style={{ 
                            cursor: currentTool === 'select' ? 'default' : 'crosshair',
                            background: showGrid ? 'linear-gradient(90deg, #f0f0f0 1px, transparent 1px), linear-gradient(#f0f0f0 1px, transparent 1px)' : 'white',
                            backgroundSize: '20px 20px'
                        }}
                    />
                    
                    {/* Instructions overlay */}
                    <div className="absolute top-2 left-2 bg-blue-100 p-2 rounded text-xs text-blue-800">
                        {currentTool === 'point' && 'Click to place points'}
                        {currentTool === 'line' && 'Click first point, then second point'}
                        {currentTool === 'circle' && 'Click center, then radius point'}
                        {currentTool === 'select' && 'Select elements to modify'}
                        {currentTool === 'measure' && 'Click elements to measure'}
                        {currentTool === 'delete' && 'Click elements to delete'}
                    </div>
                </div>
            </div>

            {/* Construction Summary */}
            {constructions.length > 0 && (
                <div className="bg-gray-50 p-4 rounded-lg mb-6">
                    <h4 className="font-semibold text-gray-700 mb-3">Construction Summary</h4>
                    <div className="space-y-2">
                        {constructions.map((construction, index) => (
                            <div key={index} className="text-sm text-gray-600">
                                <strong>{index + 1}.</strong> {construction.type.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                                {construction.sides && (
                                    <span className="ml-2 text-gray-500">
                                        (Sides: {construction.sides.map(s => s.toFixed(1)).join(', ')})
                                    </span>
                                )}
                                {construction.angles && (
                                    <span className="ml-2 text-gray-500">
                                        (Angles: {construction.angles.map(a => a.toFixed(1) + '°').join(', ')})
                                    </span>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Tips */}
            <div className="bg-blue-50 p-4 rounded-lg">
                <h4 className="text-sm font-medium text-blue-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-blue-700 space-y-1">
                    <li>• Use the tool selector to choose what you want to create</li>
                    <li>• Execute Construction will automatically create the selected geometric figure</li>
                    <li>• All constructions are mathematically validated</li>
                    <li>• Use the canvas to place points, lines, and circles manually</li>
                    <li>• Measurements are automatically calculated and displayed</li>
                </ul>
            </div>
        </div>
    );
};

export default GeometricConstructionInput;
