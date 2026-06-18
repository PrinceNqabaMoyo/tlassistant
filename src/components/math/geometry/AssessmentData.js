/**
 * Assessment Data Structure
 * Defines assessment types, question templates, and validation rules
 */

export const ASSESSMENT_TYPES = {
  DIAGNOSTIC: {
    name: "Diagnostic Assessment",
    description: "Initial assessment to determine current knowledge level",
    duration: 30, // minutes
    questions: 15,
    difficulty: "mixed"
  },
  FORMATIVE: {
    name: "Formative Assessment", 
    description: "Ongoing assessment during learning process",
    duration: 20,
    questions: 10,
    difficulty: "adaptive"
  },
  SUMMATIVE: {
    name: "Summative Assessment",
    description: "Final assessment to evaluate learning outcomes",
    duration: 45,
    questions: 25,
    difficulty: "mixed"
  },
  PRACTICE: {
    name: "Practice Quiz",
    description: "Self-paced practice with immediate feedback",
    duration: 0, // unlimited
    questions: 5,
    difficulty: "selected"
  }
};

export const QUESTION_TYPES = {
  MULTIPLE_CHOICE: {
    name: "Multiple Choice",
    description: "Select one correct answer from multiple options",
    validation: "exact_match"
  },
  TRUE_FALSE: {
    name: "True/False",
    description: "Determine if a statement is true or false",
    validation: "boolean"
  },
  NUMERICAL: {
    name: "Numerical Answer",
    description: "Enter a numerical value as the answer",
    validation: "numerical_range"
  },
  CONSTRUCTION: {
    name: "Construction Task",
    description: "Perform a geometric construction",
    validation: "step_verification"
  },
  CALCULATION: {
    name: "Calculation Problem",
    description: "Solve a mathematical calculation",
    validation: "formula_based"
  },
  IDENTIFICATION: {
    name: "Shape Identification",
    description: "Identify geometric shapes or properties",
    validation: "categorical"
  }
};

export const DIFFICULTY_LEVELS = {
  EASY: {
    name: "Easy",
    points: 1,
    timeLimit: 60, // seconds
    description: "Basic concepts and simple calculations"
  },
  MEDIUM: {
    name: "Medium", 
    points: 2,
    timeLimit: 120,
    description: "Intermediate concepts with multiple steps"
  },
  HARD: {
    name: "Hard",
    points: 3,
    timeLimit: 180,
    description: "Advanced concepts requiring complex reasoning"
  }
};

export const TOPIC_AREAS = {
  SHAPES_2D: {
    name: "2D Shapes",
    topics: ["triangles", "quadrilaterals", "circles", "polygons"],
    weight: 0.3
  },
  SHAPES_3D: {
    name: "3D Shapes", 
    topics: ["cubes", "prisms", "cylinders", "spheres"],
    weight: 0.25
  },
  MEASUREMENTS: {
    name: "Measurements",
    topics: ["area", "perimeter", "volume", "surface_area"],
    weight: 0.25
  },
  CONSTRUCTIONS: {
    name: "Constructions",
    topics: ["basic_constructions", "angle_measurement", "shape_construction"],
    weight: 0.2
  }
};

export const ASSESSMENT_TEMPLATES = {
  // 2D Shape Questions
  triangle_area: {
    type: "CALCULATION",
    difficulty: "EASY",
    topic: "SHAPES_2D",
    template: "Calculate the area of a triangle with base {base} cm and height {height} cm.",
    formula: "A = ½ × b × h",
    validation: {
      type: "numerical_range",
      tolerance: 0.1,
      expected: "base * height / 2"
    }
  },
  
  rectangle_perimeter: {
    type: "CALCULATION", 
    difficulty: "EASY",
    topic: "SHAPES_2D",
    template: "Find the perimeter of a rectangle with length {length} cm and width {width} cm.",
    formula: "P = 2(l + w)",
    validation: {
      type: "numerical_range",
      tolerance: 0.1,
      expected: "2 * (length + width)"
    }
  },

  circle_area: {
    type: "CALCULATION",
    difficulty: "MEDIUM", 
    topic: "SHAPES_2D",
    template: "Calculate the area of a circle with radius {radius} cm. Use π = 3.14",
    formula: "A = πr²",
    validation: {
      type: "numerical_range",
      tolerance: 0.1,
      expected: "3.14 * radius * radius"
    }
  },

  // 3D Shape Questions
  cube_volume: {
    type: "CALCULATION",
    difficulty: "EASY",
    topic: "SHAPES_3D", 
    template: "Find the volume of a cube with side length {side_length} cm.",
    formula: "V = s³",
    validation: {
      type: "numerical_range",
      tolerance: 0.1,
      expected: "side_length * side_length * side_length"
    }
  },

  cylinder_volume: {
    type: "CALCULATION",
    difficulty: "MEDIUM",
    topic: "SHAPES_3D",
    template: "Calculate the volume of a cylinder with radius {radius} cm and height {height} cm. Use π = 3.14",
    formula: "V = πr²h", 
    validation: {
      type: "numerical_range",
      tolerance: 0.1,
      expected: "3.14 * radius * radius * height"
    }
  },

  // Multiple Choice Questions
  shape_identification: {
    type: "MULTIPLE_CHOICE",
    difficulty: "EASY",
    topic: "SHAPES_2D",
    template: "Which shape has {property}?",
    options: ["{option1}", "{option2}", "{option3}", "{option4}"],
    correct: "{correct_option}",
    validation: {
      type: "exact_match",
      case_sensitive: false
    }
  },

  // True/False Questions
  property_statement: {
    type: "TRUE_FALSE",
    difficulty: "MEDIUM",
    topic: "MEASUREMENTS",
    template: "The area of a rectangle is always greater than its perimeter.",
    correct: false,
    explanation: "This is not always true. For example, a 1cm × 2cm rectangle has area 2cm² but perimeter 6cm.",
    validation: {
      type: "boolean"
    }
  },

  // Construction Questions
  triangle_construction: {
    type: "CONSTRUCTION",
    difficulty: "MEDIUM",
    topic: "CONSTRUCTIONS",
    template: "Construct a triangle with base {base} cm and height {height} cm.",
    steps: [
      "Draw base line segment",
      "Mark midpoint of base", 
      "Draw perpendicular height line",
      "Connect endpoints to form triangle"
    ],
    validation: {
      type: "step_verification",
      required_steps: 4
    }
  }
};

export const FEEDBACK_MESSAGES = {
  CORRECT: {
    easy: [
      "Excellent! You got it right!",
      "Perfect! Well done!",
      "Great job! You understand this concept well.",
      "Correct! Keep up the good work!"
    ],
    medium: [
      "Very good! You solved that correctly.",
      "Excellent work! That was a challenging problem.",
      "Perfect! You're mastering this topic.",
      "Great job! Your understanding is improving."
    ],
    hard: [
      "Outstanding! That was a difficult problem and you solved it!",
      "Excellent! You've mastered this advanced concept.",
      "Fantastic work! Your problem-solving skills are impressive.",
      "Brilliant! You tackled that complex problem perfectly."
    ]
  },
  INCORRECT: {
    easy: [
      "Not quite right, but don't worry! Let's try again.",
      "That's okay! This is how we learn. Try again.",
      "Not correct, but you're on the right track!",
      "Close! Let's work through this together."
    ],
    medium: [
      "That's not quite right, but you're thinking in the right direction.",
      "Not correct, but I can see you understand some of the concepts.",
      "That's okay! This is a challenging topic. Let's review it.",
      "Not quite, but you're making progress. Keep trying!"
    ],
    hard: [
      "That's not correct, but this is a very challenging problem.",
      "Not quite right, but your approach shows good thinking.",
      "That's okay! This advanced concept takes time to master.",
      "Not correct, but you're tackling difficult material. Keep going!"
    ]
  },
  HINTS: {
    easy: [
      "Remember the basic formula for this calculation.",
      "Think about what each measurement represents.",
      "Check your arithmetic carefully.",
      "Use the given values in the correct places."
    ],
    medium: [
      "Consider the relationship between the given measurements.",
      "Think about which formula applies to this situation.",
      "Break the problem down into smaller steps.",
      "Check if you need to convert any units first."
    ],
    hard: [
      "This problem requires multiple steps. Plan your approach first.",
      "Consider what information you have and what you need to find.",
      "Think about the mathematical relationships involved.",
      "Don't forget to check your work at each step."
    ]
  }
};

export const ASSESSMENT_RULES = {
  TIME_LIMITS: {
    per_question: {
      easy: 60,
      medium: 120, 
      hard: 180
    },
    total: {
      diagnostic: 1800, // 30 minutes
      formative: 1200,  // 20 minutes
      summative: 2700,  // 45 minutes
      practice: 0       // unlimited
    }
  },
  SCORING: {
    points_per_question: {
      easy: 1,
      medium: 2,
      hard: 3
    },
    passing_percentage: 70,
    mastery_percentage: 90
  },
  ATTEMPTS: {
    max_attempts: 3,
    cooldown_minutes: 5
  }
};
