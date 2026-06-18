/**
 * Example Question Specifications
 * Demonstrates how AI can generate questions with embedded visual aids
 */

// Example 1: Linear Function Question (JSON format)
export const linearFunctionQuestionJSON = {
    title: "Linear Function Analysis",
    description: "Analyze the given linear function and answer the questions below.",
    difficulty: "medium",
    subject: "mathematics",
    grade_level: "12",
    topic: "linear_functions",
    points: 5,
    question_text: "Given the linear function f(x) = 2x + 3:\n\n1. What is the slope of this function?\n2. What is the y-intercept?\n3. What is the x-intercept?\n4. If x = 5, what is f(5)?\n5. For what value of x does f(x) = 11?",
    answer_type: "text",
    visual_aid: {
        type: "linear_function",
        config: {
            m: 2,
            c: 3,
            x_range: [-5, 10],
            y_range: [-10, 25],
            showGrid: true,
            showPoints: true,
            showSlope: true,
            showYIntercept: true,
            showXIntercept: true
        }
    }
};

// Example 2: Quadratic Function Question (POML format)
export const quadraticFunctionQuestionPOML = `# Quadratic Function Question
# This demonstrates POML format for AI-generated questions

[metadata]
title = "Quadratic Function Vertex Analysis"
description = "Find the vertex and roots of the given quadratic function"
difficulty = "hard"
subject = "mathematics"
grade_level = "12"
topic = "quadratic_functions"
points = 8

[question]
question_text = "For the quadratic function f(x) = x² - 4x + 3:\n\n1. Find the vertex of the parabola\n2. Determine the roots (x-intercepts)\n3. What is the axis of symmetry?\n4. Does the parabola open upward or downward?\n5. What is the minimum/maximum value?"
answer_type = "text"

[visual_aid]
type = "quadratic_function"
config.a = 1
config.b = -4
config.c = 3
config.x_range = [-2, 6]
config.y_range = [-2, 8]
config.showGrid = true
config.showPoints = true
config.showVertex = true
config.showRoots = true`;

// Example 3: Box and Whisker Plot Question (JSON format)
export const boxPlotQuestionJSON = {
    title: "Statistical Data Analysis",
    description: "Analyze the box and whisker plot to answer the statistical questions.",
    difficulty: "medium",
    subject: "mathematics",
    grade_level: "11",
    topic: "statistics",
    points: 6,
    question_text: "Based on the box and whisker plot:\n\n1. What is the median of the dataset?\n2. What is the interquartile range (IQR)?\n3. Are there any outliers? If yes, identify them.\n4. What percentage of data falls between Q1 and Q3?\n5. What is the range of the data?\n6. Is the data skewed left, right, or symmetric?",
    answer_type: "text",
    visual_aid: {
        type: "box_whisker_plot",
        config: {
            dataSet: [
                {
                    label: "Test Scores",
                    values: [45, 52, 58, 62, 65, 68, 72, 75, 78, 82, 85, 88, 92, 95, 98]
                }
            ],
            showOutliers: true,
            showMean: true,
            showMedian: true,
            showQuartiles: true
        }
    }
};

// Example 4: Exponential Function Question (POML format)
export const exponentialFunctionQuestionPOML = `# Exponential Growth Question
# Population growth modeling with exponential functions

[metadata]
title = "Population Growth Modeling"
description = "Model population growth using exponential functions and analyze the results"
difficulty = "hard"
subject = "mathematics"
grade_level = "12"
topic = "exponential_functions"
points = 10

[question]
question_text = "A population of bacteria doubles every 3 hours. If the initial population is 1000:\n\n1. Write the exponential function P(t) that models this growth\n2. What will be the population after 12 hours?\n3. How long will it take for the population to reach 50,000?\n4. What is the growth rate per hour?\n5. Graph the function for t = 0 to t = 24 hours\n6. What is the domain and range of this function?"
answer_type = "text"

[visual_aid]
type = "exponential_function"
config.base = 2
config.coefficient = 1000
config.exponentCoefficient = 0.333
config.x_range = [0, 24]
config.y_range = [0, 2000000]
config.showGrid = true
config.showPoints = true
config.showAsymptote = false`;

// Example 5: Mixed Visual Aids Question (JSON format)
export const mixedVisualAidsQuestionJSON = {
    title: "Function Comparison Analysis",
    description: "Compare different types of functions using the provided visual aids.",
    difficulty: "hard",
    subject: "mathematics",
    grade_level: "12",
    topic: "function_analysis",
    points: 12,
    question_text: "Using the provided visual aids, compare the following functions:\n\n1. Linear: f(x) = 2x + 1\n2. Quadratic: g(x) = x² - 2x + 1\n3. Exponential: h(x) = 2^x\n\nQuestions:\n1. Which function grows fastest for large values of x?\n2. Which function has the most x-intercepts?\n3. Compare the behavior as x approaches negative infinity\n4. Which function is always positive?\n5. Find the points of intersection between f(x) and g(x)\n6. Analyze the rate of change for each function",
    answer_type: "text",
    visual_aids: [
        {
            type: "linear_function",
            config: {
                m: 2,
                c: 1,
                x_range: [-5, 10],
                y_range: [-10, 25],
                showGrid: true,
                showPoints: true,
                showSlope: true
            }
        },
        {
            type: "quadratic_function",
            config: {
                a: 1,
                b: -2,
                c: 1,
                x_range: [-5, 10],
                y_range: [-5, 25],
                showGrid: true,
                showPoints: true,
                showVertex: true
            }
        },
        {
            type: "exponential_function",
            config: {
                base: 2,
                coefficient: 1,
                exponentCoefficient: 1,
                x_range: [-5, 10],
                y_range: [0, 1000],
                showGrid: true,
                showPoints: true
            }
        }
    ]
};

// Example 6: Coordinate Plane Question (POML format)
export const coordinatePlaneQuestionPOML = `# Coordinate Geometry Question
# Plotting points and analyzing geometric relationships

[metadata]
title = "Coordinate Geometry Challenge"
description = "Plot points and analyze geometric relationships on the coordinate plane"
difficulty = "medium"
subject = "mathematics"
grade_level = "10"
topic = "coordinate_geometry"
points = 7

[question]
question_text = "On the coordinate plane:\n\n1. Plot the points A(2, 3), B(5, 7), and C(8, 3)\n2. Connect the points to form triangle ABC\n3. What type of triangle is ABC? Justify your answer\n4. Find the perimeter of triangle ABC\n5. Find the area of triangle ABC\n6. What are the coordinates of the centroid?\n7. Is triangle ABC isosceles, equilateral, or scalene?",
answer_type = "text"

[visual_aid]
type = "coordinate_plane"
config.x_range = [0, 10]
config.y_range = [0, 10]
config.showGrid = true
config.showAxes = true
config.showPoints = true
config.points = [[2, 3, "A"], [5, 7, "B"], [8, 3, "C"]]
config.lines = [[2, 3, 5, 7], [5, 7, 8, 3], [8, 3, 2, 3]]`;

// Helper function to get random question
export const getRandomQuestion = () => {
    const questions = [
        linearFunctionQuestionJSON,
        quadraticFunctionQuestionPOML,
        boxPlotQuestionJSON,
        exponentialFunctionQuestionPOML,
        mixedVisualAidsQuestionJSON,
        coordinatePlaneQuestionPOML
    ];
    
    const randomIndex = Math.floor(Math.random() * questions.length);
    return questions[randomIndex];
};

// Helper function to get questions by difficulty
export const getQuestionsByDifficulty = (difficulty) => {
    const allQuestions = [
        linearFunctionQuestionJSON,
        quadraticFunctionQuestionPOML,
        boxPlotQuestionJSON,
        exponentialFunctionQuestionPOML,
        mixedVisualAidsQuestionJSON,
        coordinatePlaneQuestionPOML
    ];
    
    return allQuestions.filter(q => {
        if (typeof q === 'string') {
            // Parse POML to check difficulty
            const lines = q.split('\n');
            const difficultyLine = lines.find(line => line.includes('difficulty ='));
            if (difficultyLine) {
                const qDifficulty = difficultyLine.split('=')[1].trim();
                return qDifficulty === difficulty;
            }
        } else {
            return q.difficulty === difficulty;
        }
        return false;
    });
};

// Helper function to get questions by topic
export const getQuestionsByTopic = (topic) => {
    const allQuestions = [
        linearFunctionQuestionJSON,
        quadraticFunctionQuestionPOML,
        boxPlotQuestionJSON,
        exponentialFunctionQuestionPOML,
        mixedVisualAidsQuestionJSON,
        coordinatePlaneQuestionPOML
    ];
    
    return allQuestions.filter(q => {
        if (typeof q === 'string') {
            // Parse POML to check topic
            const lines = q.split('\n');
            const topicLine = lines.find(line => line.includes('topic ='));
            if (topicLine) {
                const qTopic = topicLine.split('=')[1].trim();
                return qTopic === topic;
            }
        } else {
            return q.topic === topic;
        }
        return false;
    });
};

export default {
    linearFunctionQuestionJSON,
    quadraticFunctionQuestionPOML,
    boxPlotQuestionJSON,
    exponentialFunctionQuestionPOML,
    mixedVisualAidsQuestionJSON,
    coordinatePlaneQuestionPOML,
    getRandomQuestion,
    getQuestionsByDifficulty,
    getQuestionsByTopic
};
