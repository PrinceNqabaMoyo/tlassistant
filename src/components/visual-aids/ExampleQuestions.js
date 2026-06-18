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

    // Free Fall Simulator Examples
    freeFallSimulator: {
        title: "Free Fall Analysis",
        question: "An object is dropped from a height of 100 meters. Use the free fall simulator to determine the time it takes to reach the ground and its final velocity. Assume g = 9.8 m/s².",
        visualAid: {
            type: "free-fall-simulator",
            data: {
                initialHeight: 100,
                initialVelocity: 0,
                gravity: 9.8,
                airResistance: 0,
                isAnimating: false,
                showTrajectory: true,
                showVelocityVectors: true,
                showTimeMarkers: true,
                selectedPlanet: "earth"
            }
        },
        expectedAnswer: "Time to ground = √(2h/g) = √(2×100/9.8) ≈ 4.52s. Final velocity = gt = 9.8×4.52 ≈ 44.3 m/s"
    },

    // Superposition Visualizer Examples
    superpositionVisualizer: {
        title: "Wave Interference Analysis",
        question: "Two waves with amplitudes 50 and 30, frequencies 2 Hz and 3 Hz respectively, are superimposed. Use the superposition visualizer to show the resulting wave pattern and identify the beat frequency.",
        visualAid: {
            type: "superposition-visualizer",
            data: {
                waveType: "sine",
                wave1: { amplitude: 50, frequency: 2, phase: 0, color: "#3B82F6" },
                wave2: { amplitude: 30, frequency: 3, phase: 0, color: "#EF4444" },
                showIndividualWaves: true,
                showSuperposition: true,
                showInterference: true,
                isAnimating: true,
                timeRange: [0, 10]
            }
        },
        expectedAnswer: "Beat frequency = |f₁ - f₂| = |2 - 3| = 1 Hz. The resulting wave shows amplitude modulation at 1 Hz."
    },

    // Electric Field Visualizer Examples
    electricFieldVisualizer: {
        title: "Electric Field Analysis",
        question: "Two point charges are placed 10 cm apart: a +2 μC charge at (0,0) and a -1 μC charge at (10,0). Use the electric field visualizer to show the field lines and calculate the electric field strength at point (5,5).",
        visualAid: {
            type: "electric-field-visualizer",
            data: {
                chargeType: "point",
                charges: [
                    { x: 0, y: 0, magnitude: 2, type: "positive", color: "#ef4444" },
                    { x: 10, y: 0, magnitude: 1, type: "negative", color: "#3b82f6" }
                ],
                showFieldLines: true,
                showEquipotential: true,
                showVectors: true,
                fieldStrength: 1.0
            }
        },
        expectedAnswer: "The electric field at (5,5) can be calculated using superposition. E = kq/r² for each charge, then vector addition."
    },

    // Capacitor Charging Simulator Examples
    capacitorChargingSimulator: {
        title: "RC Circuit Analysis",
        question: "A 1000 Ω resistor is connected in series with a 100 μF capacitor and a 12V battery. Use the capacitor charging simulator to determine the time constant and the voltage across the capacitor after 2 time constants.",
        visualAid: {
            type: "capacitor-charging-simulator",
            data: {
                voltage: 12.0,
                resistance: 1000,
                capacitance: 100,
                timeRange: [0, 5],
                showCharging: true,
                showCurrent: true,
                showPower: false
            }
        },
        expectedAnswer: "Time constant τ = RC = 1000 × 100×10⁻⁶ = 0.1s. After 2τ, V = V₀(1-e⁻²) = 12(1-e⁻²) ≈ 10.4V"
    },

    // Electromagnetic Induction Simulator Examples
    electromagneticInductionSimulator: {
        title: "Faraday's Law Application",
        question: "A circular coil with 100 turns and area 0.01 m² rotates at 60 RPM in a uniform magnetic field of 0.5 T. Use the electromagnetic induction simulator to calculate the maximum induced EMF and its frequency.",
        visualAid: {
            type: "electromagnetic-induction-simulator",
            data: {
                magneticFieldStrength: 0.5,
                coilArea: 0.01,
                numberOfTurns: 100,
                rotationSpeed: 60,
                rotationAxis: "horizontal",
                showMagneticField: true,
                showInducedEMF: true,
                showFlux: true
            }
        },
        expectedAnswer: "Max EMF = N×B×A×ω = 100×0.5×0.01×(2π×60/60) = 0.314V. Frequency = 60/60 = 1 Hz"
    },

    // AC Circuit Analyzer Examples
    acCircuitAnalyzer: {
        title: "RLC Series Circuit Analysis",
        question: "An RLC series circuit has R=100Ω, L=0.1H, C=100μF, and is connected to a 120V, 60Hz AC source. Use the AC circuit analyzer to determine the impedance, current, and phase angle.",
        visualAid: {
            type: "ac-circuit-analyzer",
            data: {
                circuitType: "rlc_series",
                voltage: 120,
                frequency: 60,
                resistance: 100,
                inductance: 0.1,
                capacitance: 100,
                showPhasor: true,
                showImpedance: true,
                showPower: true
            }
        },
        expectedAnswer: "Z = √(R² + (X_L - X_C)²), I = V/Z, φ = tan⁻¹((X_L - X_C)/R). Calculate X_L = ωL and X_C = 1/(ωC)."
    }
};

export const physicsPOMLExamples = {
    electricFieldVisualizer: `
<question>
  <title>Electric Field Analysis</title>
  <text>Two point charges are placed 10 cm apart: a +2 μC charge at (0,0) and a -1 μC charge at (10,0). Use the electric field visualizer to show the field lines and calculate the electric field strength at point (5,5).</text>
  <visual-aid type="electric-field-visualizer">
    <charges>
      <charge x="0" y="0" magnitude="2" type="positive" color="#ef4444"/>
      <charge x="10" y="0" magnitude="1" type="negative" color="#3b82f6"/>
    </charges>
    <display show-field-lines="true" show-equipotential="true" show-vectors="true"/>
  </visual-aid>
  <expected-answer>The electric field at (5,5) can be calculated using superposition. E = kq/r² for each charge, then vector addition.</expected-answer>
</question>
    `,

    capacitorChargingSimulator: `
<question>
  <title>RC Circuit Analysis</title>
  <text>A 1000 Ω resistor is connected in series with a 100 μF capacitor and a 12V battery. Use the capacitor charging simulator to determine the time constant and the voltage across the capacitor after 2 time constants.</text>
  <visual-aid type="capacitor-charging-simulator">
    <circuit voltage="12.0" resistance="1000" capacitance="100"/>
    <display show-charging="true" show-current="true" show-power="false"/>
  </visual-aid>
  <expected-answer>Time constant τ = RC = 1000 × 100×10⁻⁶ = 0.1s. After 2τ, V = V₀(1-e⁻²) = 12(1-e⁻²) ≈ 10.4V</expected-answer>
</question>
    `,

    electromagneticInductionSimulator: `
<question>
  <title>Faraday's Law Application</title>
  <text>A circular coil with 100 turns and area 0.01 m² rotates at 60 RPM in a uniform magnetic field of 0.5 T. Use the electromagnetic induction simulator to calculate the maximum induced EMF and its frequency.</text>
  <visual-aid type="electromagnetic-induction-simulator">
    <coil turns="100" area="0.01" rotation-speed="60" axis="horizontal"/>
    <magnetic-field strength="0.5"/>
    <display show-magnetic-field="true" show-induced-emf="true" show-flux="true"/>
  </visual-aid>
  <expected-answer>Max EMF = N×B×A×ω = 100×0.5×0.01×(2π×60/60) = 0.314V. Frequency = 60/60 = 1 Hz</expected-answer>
</question>
    `,

    acCircuitAnalyzer: `
<question>
  <title>RLC Series Circuit Analysis</title>
  <text>An RLC series circuit has R=100Ω, L=0.1H, C=100μF, and is connected to a 120V, 60Hz AC source. Use the AC circuit analyzer to determine the impedance, current, and phase angle.</text>
  <visual-aid type="ac-circuit-analyzer">
    <circuit type="rlc_series" voltage="120" frequency="60"/>
    <components resistance="100" inductance="0.1" capacitance="100"/>
    <display show-phasor="true" show-impedance="true" show-power="true"/>
  </visual-aid>
  <expected-answer>Z = √(R² + (X_L - X_C)²), I = V/Z, φ = tan⁻¹((X_L - X_C)/R). Calculate X_L = ωL and X_C = 1/(ωC).</expected-answer>
</question>
    `
};

export const physicsJSONExamples = {
    electricFieldVisualizer: {
        title: "Electric Field Analysis",
        question: "Two point charges are placed 10 cm apart: a +2 μC charge at (0,0) and a -1 μC charge at (10,0). Use the electric field visualizer to show the field lines and calculate the electric field strength at point (5,5).",
        visualAid: {
            type: "electric-field-visualizer",
            data: {
                chargeType: "point",
                charges: [
                    { x: 0, y: 0, magnitude: 2, type: "positive", color: "#ef4444" },
                    { x: 10, y: 0, magnitude: 1, type: "negative", color: "#3b82f6" }
                ],
                showFieldLines: true,
                showEquipotential: true,
                showVectors: true,
                fieldStrength: 1.0
            }
        },
        expectedAnswer: "The electric field at (5,5) can be calculated using superposition. E = kq/r² for each charge, then vector addition."
    },

    capacitorChargingSimulator: {
        title: "RC Circuit Analysis",
        question: "A 1000 Ω resistor is connected in series with a 100 μF capacitor and a 12V battery. Use the capacitor charging simulator to determine the time constant and the voltage across the capacitor after 2 time constants.",
        visualAid: {
            type: "capacitor-charging-simulator",
            data: {
                voltage: 12.0,
                resistance: 1000,
                capacitance: 100,
                timeRange: [0, 5],
                showCharging: true,
                showCurrent: true,
                showPower: false
            }
        },
        expectedAnswer: "Time constant τ = RC = 1000 × 100×10⁻⁶ = 0.1s. After 2τ, V = V₀(1-e⁻²) = 12(1-e⁻²) ≈ 10.4V"
    },

    electromagneticInductionSimulator: {
        title: "Faraday's Law Application",
        question: "A circular coil with 100 turns and area 0.01 m² rotates at 60 RPM in a uniform magnetic field of 0.5 T. Use the electromagnetic induction simulator to calculate the maximum induced EMF and its frequency.",
        visualAid: {
            type: "electromagnetic-induction-simulator",
            data: {
                magneticFieldStrength: 0.5,
                coilArea: 0.01,
                numberOfTurns: 100,
                rotationSpeed: 60,
                rotationAxis: "horizontal",
                showMagneticField: true,
                showInducedEMF: true,
                showFlux: true
            }
        },
        expectedAnswer: "Max EMF = N×B×A×ω = 100×0.5×0.01×(2π×60/60) = 0.314V. Frequency = 60/60 = 1 Hz"
    },

    acCircuitAnalyzer: {
        title: "RLC Series Circuit Analysis",
        question: "An RLC series circuit has R=100Ω, L=0.1H, C=100μF, and is connected to a 120V, 60Hz AC source. Use the AC circuit analyzer to determine the impedance, current, and phase angle.",
        visualAid: {
            type: "ac-circuit-analyzer",
            data: {
                circuitType: "rlc_series",
                voltage: 120,
                frequency: 60,
                resistance: 100,
                inductance: 0.1,
                capacitance: 100,
                showPhasor: true,
                showImpedance: true,
                showPower: true
            }
        },
        expectedAnswer: "Z = √(R² + (X_L - X_C)²), I = V/Z, φ = tan⁻¹((X_L - X_C)/R). Calculate X_L = ωL and X_C = 1/(ωC)."
    }
};
