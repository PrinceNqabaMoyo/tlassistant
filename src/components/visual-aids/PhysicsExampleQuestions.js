/**
 * Physics Visual Aid Example Questions
 * Example specifications for AI-generated questions with visual aids
 */

export const physicsExampleQuestions = {
    // Motion Graphs Examples
    motionGraphs: {
        title: "Analyzing Motion Graphs",
        question: "A car accelerates uniformly from rest. Use the motion graph builder to show the position vs time graph for the first 10 seconds with an acceleration of 2 m/s². What is the car's position after 5 seconds?",
        visualAid: {
            type: "motion-graph-builder",
            data: {
                motionType: "uniform_acceleration",
                initialVelocity: 0,
                acceleration: 2,
                timeRange: [0, 10],
                showPosition: true,
                showVelocity: true,
                showAcceleration: false
            }
        },
        expectedAnswer: "The car's position after 5 seconds is 25 meters (using s = ½at² = ½ × 2 × 5² = 25 m)"
    },

    // Force Diagram Examples
    forceDiagram: {
        title: "Force Analysis on an Inclined Plane",
        question: "A 5kg block slides down a frictionless inclined plane at 30°. Use the force diagram to show the forces acting on the block and calculate the net force.",
        visualAid: {
            type: "force-diagram",
            data: {
                forces: [
                    { name: "Weight", magnitude: 49, direction: "down", color: "#ef4444" },
                    { name: "Normal", magnitude: 42.4, direction: "up", color: "#3b82f6" }
                ],
                showComponents: true,
                showResultant: true
            }
        },
        expectedAnswer: "The net force is 24.5N down the incline (mg sin θ = 5 × 9.8 × sin 30° = 24.5N)"
    },

    // Pulse Simulator Examples
    pulseSimulator: {
        title: "Wave Pulse Analysis",
        question: "A transverse pulse travels along a string with amplitude 30 units and width 60 units. Use the pulse simulator to demonstrate this wave and explain the difference between transverse and longitudinal waves.",
        visualAid: {
            type: "pulse-simulator",
            data: {
                pulseType: "transverse",
                amplitude: 30,
                pulseWidth: 60,
                speed: 3,
                selectedMedium: "string",
                showGrid: true,
                showMeasurements: true
            }
        },
        expectedAnswer: "In transverse waves, particles move perpendicular to wave direction. In longitudinal waves, particles move parallel to wave direction."
    },

    // Sound Wave Analyzer Examples
    soundWaveAnalyzer: {
        title: "Musical Note Analysis",
        question: "Use the sound wave analyzer to generate a 440 Hz sine wave (A4 note). Calculate the wavelength of this sound wave in air and explain how frequency relates to pitch.",
        visualAid: {
            type: "sound-wave-analyzer",
            data: {
                frequency: 440,
                amplitude: 60,
                waveform: "sine",
                selectedNote: "A4",
                showHarmonics: true,
                showSpectrum: true
            }
        },
        expectedAnswer: "Wavelength = speed of sound / frequency = 343 m/s / 440 Hz = 0.78 m. Higher frequency = higher pitch."
    },

    // Free Fall Simulator Examples
    freeFallSimulator: {
        title: "Free Fall on Different Planets",
        question: "Compare free fall on Earth and the Moon. Use the simulator to show a 100m drop on both planets. How long does it take to reach the ground on each?",
        visualAid: {
            type: "free-fall-simulator",
            data: {
                initialHeight: 100,
                initialVelocity: 0,
                selectedPlanet: "earth",
                showTrajectory: true,
                showVelocityVectors: true,
                showTimeMarkers: true
            }
        },
        expectedAnswer: "Earth: t = √(2h/g) = √(200/9.8) = 4.52s. Moon: t = √(200/1.62) = 11.1s. Moon takes longer due to lower gravity."
    },

    // Motion Graph Builder Examples
    motionGraphBuilder: {
        title: "Complex Motion Analysis",
        question: "A ball is thrown upward with initial velocity 20 m/s from ground level. Use the motion graph builder to show the position vs time graph and determine the maximum height reached.",
        visualAid: {
            type: "motion-graph-builder",
            data: {
                motionType: "uniform_acceleration",
                initialVelocity: 20,
                acceleration: -9.8,
                timeRange: [0, 5],
                showPosition: true,
                showVelocity: true,
                showAcceleration: false
            }
        },
        expectedAnswer: "Maximum height = v₀²/(2g) = 20²/(2×9.8) = 20.4 meters. Time to reach max height = v₀/g = 20/9.8 = 2.04s"
    }
};

/**
 * POML Format Examples for Physics Questions
 */
export const physicsPOMLExamples = {
    motionGraphs: `[question]
title=Analyzing Motion Graphs
text=A car accelerates uniformly from rest. Use the motion graph builder to show the position vs time graph for the first 10 seconds with an acceleration of 2 m/s². What is the car's position after 5 seconds?

[visual_aid]
type=motion-graph-builder
motion_type=uniform_acceleration
initial_velocity=0
acceleration=2
time_range=[0,10]
show_position=true
show_velocity=true
show_acceleration=false

[answer]
expected=The car's position after 5 seconds is 25 meters (using s = ½at² = ½ × 2 × 5² = 25 m)`,

    freeFall: `[question]
title=Free Fall on Different Planets
text=Compare free fall on Earth and the Moon. Use the simulator to show a 100m drop on both planets. How long does it take to reach the ground on each?

[visual_aid]
type=free-fall-simulator
initial_height=100
initial_velocity=0
selected_planet=earth
show_trajectory=true
show_velocity_vectors=true
show_time_markers=true

[answer]
expected=Earth: t = √(2h/g) = √(200/9.8) = 4.52s. Moon: t = √(200/1.62) = 11.1s. Moon takes longer due to lower gravity.`
};

/**
 * JSON Format Examples for Physics Questions
 */
export const physicsJSONExamples = {
    motionGraphs: {
        title: "Analyzing Motion Graphs",
        question: "A car accelerates uniformly from rest. Use the motion graph builder to show the position vs time graph for the first 10 seconds with an acceleration of 2 m/s². What is the car's position after 5 seconds?",
        visual_aid: {
            type: "motion-graph-builder",
            data: {
                motionType: "uniform_acceleration",
                initialVelocity: 0,
                acceleration: 2,
                timeRange: [0, 10],
                showPosition: true,
                showVelocity: true,
                showAcceleration: false
            }
        },
        expected_answer: "The car's position after 5 seconds is 25 meters (using s = ½at² = ½ × 2 × 5² = 25 m)"
    },

    freeFall: {
        title: "Free Fall on Different Planets",
        question: "Compare free fall on Earth and the Moon. Use the simulator to show a 100m drop on both planets. How long does it take to reach the ground on each?",
        visual_aid: {
            type: "free-fall-simulator",
            data: {
                initialHeight: 100,
                initialVelocity: 0,
                selectedPlanet: "earth",
                showTrajectory: true,
                showVelocityVectors: true,
                showTimeMarkers: true
            }
        },
        expected_answer: "Earth: t = √(2h/g) = √(200/9.8) = 4.52s. Moon: t = √(200/1.62) = 11.1s. Moon takes longer due to lower gravity."
    }
};

export default {
    physicsExampleQuestions,
    physicsPOMLExamples,
    physicsJSONExamples
};
