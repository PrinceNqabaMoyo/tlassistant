/**
 * Construction Guide Data Structure
 * Defines step-by-step construction guides for different geometric shapes
 */

export const CONSTRUCTION_GUIDES = {
  // 2D Shape Constructions
  triangle: {
    title: "Constructing a Triangle",
    description: "Step-by-step guide to construct a triangle with given base and height",
    tools: ["Ruler", "Compass", "Pencil"],
    difficulty: "Easy",
    steps: [
      {
        id: 1,
        title: "Draw the Base",
        description: "Use a ruler to draw a straight line segment for the base",
        instruction: "Draw line segment AB with length equal to the given base",
        visual: "base_line",
        tools: ["Ruler"],
        tips: ["Make sure the line is straight and horizontal", "Mark points A and B clearly"]
      },
      {
        id: 2,
        title: "Mark the Height Point",
        description: "Find the point where the height will be measured from",
        instruction: "Mark the midpoint of line AB as point M",
        visual: "midpoint",
        tools: ["Ruler", "Compass"],
        tips: ["Use compass to find exact midpoint", "This will be the base of the height"]
      },
      {
        id: 3,
        title: "Construct the Height",
        description: "Draw a perpendicular line from the midpoint for the height",
        instruction: "From point M, draw a perpendicular line upward with length equal to the given height",
        visual: "height_line",
        tools: ["Compass", "Ruler"],
        tips: ["Use compass to create right angle", "Measure height accurately"]
      },
      {
        id: 4,
        title: "Complete the Triangle",
        description: "Connect the height endpoint to the base endpoints",
        instruction: "Draw lines from the height endpoint to points A and B to complete the triangle",
        visual: "complete_triangle",
        tools: ["Ruler"],
        tips: ["Ensure lines are straight", "Check that all three sides connect properly"]
      }
    ]
  },

  rectangle: {
    title: "Constructing a Rectangle",
    description: "Step-by-step guide to construct a rectangle with given length and width",
    tools: ["Ruler", "Compass", "Pencil", "Set Square"],
    difficulty: "Easy",
    steps: [
      {
        id: 1,
        title: "Draw the Base",
        description: "Draw the bottom edge of the rectangle",
        instruction: "Draw horizontal line AB with length equal to the given length",
        visual: "base_line",
        tools: ["Ruler"],
        tips: ["Keep the line perfectly horizontal", "Mark endpoints A and B clearly"]
      },
      {
        id: 2,
        title: "Construct Right Angles",
        description: "Create perpendicular lines at both endpoints",
        instruction: "At points A and B, draw perpendicular lines upward using a set square",
        visual: "perpendiculars",
        tools: ["Set Square", "Ruler"],
        tips: ["Ensure angles are exactly 90°", "Both lines should be the same length"]
      },
      {
        id: 3,
        title: "Mark the Width",
        description: "Measure and mark the width on both perpendicular lines",
        instruction: "On both perpendicular lines, mark points C and D at the given width distance",
        visual: "width_marks",
        tools: ["Ruler", "Compass"],
        tips: ["Measure width accurately on both sides", "Ensure both marks are at the same height"]
      },
      {
        id: 4,
        title: "Complete the Rectangle",
        description: "Connect the top points to complete the rectangle",
        instruction: "Draw line CD to connect points C and D, completing the rectangle",
        visual: "complete_rectangle",
        tools: ["Ruler"],
        tips: ["Ensure the top line is parallel to the base", "Check that all angles are 90°"]
      }
    ]
  },

  circle: {
    title: "Constructing a Circle",
    description: "Step-by-step guide to construct a circle with given radius",
    tools: ["Compass", "Ruler", "Pencil"],
    difficulty: "Easy",
    steps: [
      {
        id: 1,
        title: "Mark the Center",
        description: "Choose and mark the center point of the circle",
        instruction: "Mark point O as the center of the circle",
        visual: "center_point",
        tools: ["Pencil"],
        tips: ["Choose a clear, visible point", "Make sure the mark is precise"]
      },
      {
        id: 2,
        title: "Set the Compass",
        description: "Set the compass to the given radius",
        instruction: "Open the compass to the exact radius measurement",
        visual: "compass_setting",
        tools: ["Compass", "Ruler"],
        tips: ["Measure radius carefully", "Ensure compass is set to exact measurement"]
      },
      {
        id: 3,
        title: "Draw the Circle",
        description: "Use the compass to draw the circle",
        instruction: "Place compass point on O and draw a complete circle",
        visual: "drawing_circle",
        tools: ["Compass"],
        tips: ["Keep compass steady", "Draw smooth, continuous curve", "Complete the full circle"]
      },
      {
        id: 4,
        title: "Mark Key Points",
        description: "Mark important points on the circle",
        instruction: "Mark points where the circle intersects with horizontal and vertical lines through the center",
        visual: "key_points",
        tools: ["Ruler", "Pencil"],
        tips: ["Mark cardinal points clearly", "These help with measurements and further constructions"]
      }
    ]
  },

  // 3D Shape Constructions
  cube: {
    title: "Constructing a 3D Cube",
    description: "Step-by-step guide to construct a 3D cube with given side length",
    tools: ["Ruler", "Compass", "Pencil", "Protractor"],
    difficulty: "Medium",
    steps: [
      {
        id: 1,
        title: "Draw the Base Square",
        description: "Start with a square base",
        instruction: "Draw square ABCD with side length equal to the given measurement",
        visual: "base_square",
        tools: ["Ruler", "Compass"],
        tips: ["Ensure all angles are 90°", "Make sides equal length"]
      },
      {
        id: 2,
        title: "Add 3D Perspective Lines",
        description: "Draw lines to create 3D perspective",
        instruction: "From each corner, draw lines at 30° angle upward and to the right",
        visual: "perspective_lines",
        tools: ["Protractor", "Ruler"],
        tips: ["Use consistent angle for all lines", "Keep lines parallel to each other"]
      },
      {
        id: 3,
        title: "Draw the Top Face",
        description: "Complete the top square of the cube",
        instruction: "Connect the top ends of the perspective lines to form square EFGH",
        visual: "top_face",
        tools: ["Ruler"],
        tips: ["Ensure top square is parallel to base", "Check that all sides are equal"]
      },
      {
        id: 4,
        title: "Add Hidden Lines",
        description: "Show hidden edges with dashed lines",
        instruction: "Draw dashed lines for edges that would be hidden from view",
        visual: "hidden_lines",
        tools: ["Ruler", "Pencil"],
        tips: ["Use dashed lines for hidden edges", "Keep dashes consistent in length"]
      }
    ]
  },

  cylinder: {
    title: "Constructing a 3D Cylinder",
    description: "Step-by-step guide to construct a 3D cylinder with given radius and height",
    tools: ["Ruler", "Compass", "Pencil", "Protractor"],
    difficulty: "Medium",
    steps: [
      {
        id: 1,
        title: "Draw the Base Circle",
        description: "Start with the bottom circle",
        instruction: "Draw circle with center O and given radius",
        visual: "base_circle",
        tools: ["Compass", "Ruler"],
        tips: ["Mark center point clearly", "Ensure circle is perfectly round"]
      },
      {
        id: 2,
        title: "Add Vertical Lines",
        description: "Draw vertical lines for the height",
        instruction: "Draw two vertical lines from the circle center, height equal to given measurement",
        visual: "vertical_lines",
        tools: ["Ruler"],
        tips: ["Keep lines perfectly vertical", "Ensure they're parallel"]
      },
      {
        id: 3,
        title: "Draw the Top Circle",
        description: "Complete the top circle",
        instruction: "Draw the top circle with same radius, centered on the top of the vertical lines",
        visual: "top_circle",
        tools: ["Compass"],
        tips: ["Ensure top circle is parallel to base", "Same radius as base circle"]
      },
      {
        id: 4,
        title: "Add Elliptical Perspective",
        description: "Show the elliptical view of the circles",
        instruction: "Draw ellipses to show the circular bases in 3D perspective",
        visual: "elliptical_view",
        tools: ["Compass", "Ruler"],
        tips: ["Make ellipses proportional", "Show depth with perspective"]
      }
    ]
  }
};

export const CONSTRUCTION_TOOLS = {
  ruler: {
    name: "Ruler",
    description: "For drawing straight lines and measuring distances",
    icon: "📏"
  },
  compass: {
    name: "Compass",
    description: "For drawing circles and arcs",
    icon: "🧭"
  },
  pencil: {
    name: "Pencil",
    description: "For marking points and drawing",
    icon: "✏️"
  },
  protractor: {
    name: "Protractor",
    description: "For measuring and drawing angles",
    icon: "📐"
  },
  set_square: {
    name: "Set Square",
    description: "For drawing perpendicular lines",
    icon: "📐"
  }
};

export const DIFFICULTY_LEVELS = {
  easy: {
    name: "Easy",
    color: "green",
    description: "Basic construction with simple steps"
  },
  medium: {
    name: "Medium", 
    color: "yellow",
    description: "Requires multiple tools and careful measurement"
  },
  hard: {
    name: "Hard",
    color: "red", 
    description: "Complex construction with precise measurements"
  }
};
