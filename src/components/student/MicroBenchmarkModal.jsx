import React, { useState, useEffect, useMemo, useRef } from 'react';
import { Sparkles, ArrowRight, X, CheckCircle2, ChevronLeft, Zap } from 'lucide-react';
import { isOwnerEmail } from '../../app/constants/access';
import MathKeypad from '../workspace/shared/mathx/MathKeypad';
import MathText from '../workspace/shared/mathx/MathText';
import { latexify } from '../workspace/shared/mathx/mathLatexify';

/**
 * Authentic, calculation-based benchmark questions for CAPS topics.
 * Strictly tests procedural application and computation — ZERO semantic memorization questions.
 */
const getTopicBenchmarkQuestions = (subject = '', grade = '', topicTitle = '') => {
  const normTopic = String(topicTitle).toLowerCase();
  const normSubject = String(subject).toLowerCase();

  // 1. Exponents & Powers
  if (normTopic.includes('exponent') || normTopic.includes('power') || normTopic.includes('surd') || normTopic.includes('scientific')) {
    return [
      {
        step: 1,
        type: 'Product & Quotient Rules',
        prompt: 'Calculate the exact numeric value without a calculator: 2³ × 2⁴ ÷ 2².',
        hint: 'Apply exponent laws for the same base: 2^(3 + 4 - 2) = 2⁵.',
        sample: '32',
      },
      {
        step: 2,
        type: 'Algebraic Simplification',
        prompt: 'Simplify the expression and write your answer with positive exponents: (3x²)³ × x⁻⁴.',
        hint: 'Distribute the outer power: 3³ × x^(2×3) = 27x⁶. Then multiply by x⁻⁴: 27x^(6-4).',
        sample: '27x²',
      },
      {
        step: 3,
        type: 'Exponential Equations',
        prompt: 'Solve for x in the equation: 3^(x + 1) = 81.',
        hint: 'Rewrite 81 with base 3: 81 = 3⁴. Equate the exponents: x + 1 = 4.',
        sample: 'x = 3',
      },
    ];
  }

  // 2. Whole Numbers & Operations (BODMAS / Factors / Multiples)
  if (normTopic.includes('whole') || normTopic.includes('operation') || (normSubject.includes('math') && normTopic.includes('number') && !normTopic.includes('pattern'))) {
    return [
      {
        step: 1,
        type: 'Order of Operations (BODMAS)',
        prompt: 'Calculate the exact value: 48 − 16 ÷ 4 + 7 × 2.',
        hint: 'Division and Multiplication take precedence: 48 − 4 + 14.',
        sample: '58',
      },
      {
        step: 2,
        type: 'Multi-Step Calculation',
        prompt: 'Calculate without a calculator: 540 ÷ (18 − 9) + 35 × 3.',
        hint: 'Evaluate brackets first: 18 − 9 = 9. Then 540 ÷ 9 = 60, and 35 × 3 = 105.',
        sample: '165',
      },
      {
        step: 3,
        type: 'HCF & LCM Application',
        prompt: 'Find the Highest Common Factor (HCF) and Lowest Common Multiple (LCM) of 24 and 36 using prime factors.',
        hint: 'Prime factors: 24 = 2³ × 3, 36 = 2² × 3². HCF = 2² × 3 = 12; LCM = 2³ × 3² = 72.',
        sample: 'HCF = 12, LCM = 72',
      },
    ];
  }

  // 3. Integers
  if (normTopic.includes('integer') || normTopic.includes('negative')) {
    return [
      {
        step: 1,
        type: 'Signed Addition & Subtraction',
        prompt: 'Calculate the value of: −18 − (−7) + (−14).',
        hint: 'Subtracting a negative becomes positive: −18 + 7 − 14.',
        sample: '−25',
      },
      {
        step: 2,
        type: 'Signed Multiplication & Division',
        prompt: 'Evaluate: (−6) × (−8) ÷ (−4).',
        hint: '(−6) × (−8) = +48. Then divide 48 by −4.',
        sample: '−12',
      },
      {
        step: 3,
        type: 'Combined Integer Operations',
        prompt: 'Calculate: (−3)² − (−4) × 5 + (−16) ÷ 4.',
        hint: '(−3)² = 9; (−4) × 5 = −20; (−16) ÷ 4 = −4. So 9 − (−20) + (−4).',
        sample: '25',
      },
    ];
  }

  // 4. Fractions & Decimals
  if (normTopic.includes('fraction') || normTopic.includes('decimal') || normTopic.includes('percentage') || normTopic.includes('ratio')) {
    return [
      {
        step: 1,
        type: 'Fraction Addition & Subtraction',
        prompt: 'Calculate and give your answer in simplest fraction form: 3/4 + 2/5 − 1/2.',
        hint: 'Find the lowest common denominator (20): 15/20 + 8/20 − 10/20.',
        sample: '13/20',
      },
      {
        step: 2,
        type: 'Fraction Multiplication & Division',
        prompt: 'Evaluate: (7/8) ÷ (14/16) × (4/5).',
        hint: 'Invert and multiply: (7/8) × (16/14) = 1. Then 1 × (4/5).',
        sample: '4/5',
      },
      {
        step: 3,
        type: 'Decimals & Percentages',
        prompt: 'Convert 7/25 to a decimal (use comma `,`), and calculate 15% of R480.',
        hint: '7/25 = 28/100 = 0,28. 15% of 480 = 0,15 × 480 = R72.',
        sample: '0,28 and R72',
      },
    ];
  }

  // 5. Algebraic Expressions
  if (normTopic.includes('algebraic expression') || normTopic.includes('factoris') || normTopic.includes('factoriz') || normTopic.includes('polynomial')) {
    return [
      {
        step: 1,
        type: 'Expansion & Like Terms',
        prompt: 'Expand and simplify: 3(2x − 4) − 2(x + 5).',
        hint: 'Distribute each bracket: 6x − 12 − 2x − 10. Combine like terms.',
        sample: '4x − 22',
      },
      {
        step: 2,
        type: 'Binomial Expansion',
        prompt: 'Expand and simplify the product: (2x − 3)(x + 4).',
        hint: 'Use FOIL: 2x² + 8x − 3x − 12.',
        sample: '2x² + 5x − 12',
      },
      {
        step: 3,
        type: 'Factorisation Application',
        prompt: 'Factorise completely: x² − 7x + 12 and 4x² − 25.',
        hint: 'Find factors of +12 that sum to −7: (x − 3)(x − 4). Second is difference of squares: (2x − 5)(2x + 5).',
        sample: '(x − 3)(x − 4) and (2x − 5)(2x + 5)',
      },
    ];
  }

  // 6. Equations & Inequalities
  if (normTopic.includes('equation') || normTopic.includes('inequal') || normTopic.includes('quadratic')) {
    return [
      {
        step: 1,
        type: 'Linear Equations',
        prompt: 'Solve for x: 4(x − 3) = 2x + 10.',
        hint: 'Expand: 4x − 12 = 2x + 10. Subtract 2x and add 12 to both sides: 2x = 22.',
        sample: 'x = 11',
      },
      {
        step: 2,
        type: 'Fractional Equations',
        prompt: 'Solve for x: (2x − 1)/3 = (x + 4)/2.',
        hint: 'Cross-multiply: 2(2x − 1) = 3(x + 4) => 4x − 2 = 3x + 12.',
        sample: 'x = 14',
      },
      {
        step: 3,
        type: 'Quadratic Equations',
        prompt: 'Solve for x: x² − 5x + 6 = 0.',
        hint: 'Factorise: (x − 2)(x − 3) = 0. Therefore x = 2 or x = 3.',
        sample: 'x = 2 or x = 3',
      },
    ];
  }

  // 7. Patterns, Sequences & Series
  if (normTopic.includes('pattern') || normTopic.includes('sequence') || normTopic.includes('series')) {
    return [
      {
        step: 1,
        type: 'General Term Formula',
        prompt: 'For the arithmetic sequence 7; 11; 15; 19; ..., write down the formula for the nth term (Tn).',
        hint: 'Common difference d = 4. Tn = 4n + c. For n = 1: 4(1) + c = 7 => c = 3.',
        sample: 'Tn = 4n + 3',
      },
      {
        step: 2,
        type: 'Term Calculation',
        prompt: 'Using the sequence Tn = 4n + 3, calculate the 25th term (T25).',
        hint: 'Substitute n = 25 into the formula: 4(25) + 3.',
        sample: 'T25 = 103',
      },
      {
        step: 3,
        type: 'Term Number Application',
        prompt: 'Which term in the sequence 7; 11; 15; 19; ... has a value of 143?',
        hint: 'Set 4n + 3 = 143. Subtract 3 to get 4n = 140. Divide by 4.',
        sample: 'n = 35 (the 35th term)',
      },
    ];
  }

  // 8. Trigonometry
  if (normTopic.includes('trig')) {
    return [
      {
        step: 1,
        type: 'Right-Angled Triangle Ratios',
        prompt: 'In a right-angled triangle, the side opposite angle θ is 6 and the adjacent side is 8. Calculate the hypotenuse and find sin θ and tan θ.',
        hint: 'Hypotenuse = √(6² + 8²) = 10. sin θ = opposite/hypotenuse = 6/10 = 3/5. tan θ = 6/8 = 3/4.',
        sample: 'hypotenuse = 10, sin θ = 3/5, tan θ = 3/4',
      },
      {
        step: 2,
        type: 'Special Angles Without Calculator',
        prompt: 'Calculate the exact value: sin 30° + cos 60° − tan 45°.',
        hint: 'sin 30° = 1/2, cos 60° = 1/2, tan 45° = 1. Compute 1/2 + 1/2 − 1.',
        sample: '0',
      },
      {
        step: 3,
        type: 'Trigonometric Equations',
        prompt: 'Solve for θ in the interval [0°, 90°]: 2 sin θ − √3 = 0.',
        hint: 'Isolate sin θ = (√3)/2. Reference angle for (√3)/2 is 60°.',
        sample: 'θ = 60°',
      },
    ];
  }

  // 9. Functions & Graphs
  if (normTopic.includes('function') || normTopic.includes('graph') || normTopic.includes('parabola') || normTopic.includes('hyperbola')) {
    return [
      {
        step: 1,
        type: 'Linear Intercepts',
        prompt: 'For the line y = 2x − 6, find the coordinates of the x-intercept and y-intercept.',
        hint: 'For x-intercept set y = 0: 2x − 6 = 0 => (3, 0). For y-intercept set x = 0: (0, −6).',
        sample: 'x-intercept: (3, 0); y-intercept: (0, −6)',
      },
      {
        step: 2,
        type: 'Equation of Straight Line',
        prompt: 'Find the equation of the line passing through (2, 5) and (4, 11) in the form y = mx + c.',
        hint: 'Gradient m = (11 − 5)/(4 − 2) = 6/2 = 3. Then y − 5 = 3(x − 2) => y = 3x − 1.',
        sample: 'y = 3x − 1',
      },
      {
        step: 3,
        type: 'Parabola Turning Point',
        prompt: 'Determine the coordinates of the turning point of f(x) = x² − 4x + 3.',
        hint: 'x = −b/(2a) = −(−4)/(2) = 2. Substitute x = 2: f(2) = 4 − 8 + 3 = −1.',
        sample: 'Turning point: (2, −1)',
      },
    ];
  }

  // 10. Euclidean Geometry & Angles
  if (normTopic.includes('geometr') || normTopic.includes('angle') || normTopic.includes('triangle') || normTopic.includes('line')) {
    return [
      {
        step: 1,
        type: 'Angles on a Straight Line',
        prompt: 'Two adjacent angles on a straight line are (3x + 20)° and (2x + 10)°. Solve for x and calculate the size of the larger angle.',
        hint: 'Angles on a straight line add to 180°: (3x + 20) + (2x + 10) = 180 => 5x + 30 = 180.',
        sample: 'x = 30; larger angle = 110°',
      },
      {
        step: 2,
        type: 'Parallel Lines & Transversals',
        prompt: 'Two parallel lines are cut by a transversal. If two co-interior angles are (2x + 15)° and (x + 45)°, calculate the value of x.',
        hint: 'Co-interior angles are supplementary (add to 180°): 3x + 60 = 180.',
        sample: 'x = 40°',
      },
      {
        step: 3,
        type: 'Triangle Interior & Exterior Angles',
        prompt: 'In △ABC, ∠A = 50° and ∠B = 70°. Calculate ∠C and the exterior angle at vertex C.',
        hint: 'Interior sum is 180°: ∠C = 180 − 120 = 60°. Exterior angle equals ∠A + ∠B = 120°.',
        sample: '∠C = 60°, exterior angle = 120°',
      },
    ];
  }

  // 11. Measurement, Perimeter, Area & Volume
  if (normTopic.includes('measurement') || normTopic.includes('perimeter') || normTopic.includes('area') || normTopic.includes('volume') || normTopic.includes('surface')) {
    return [
      {
        step: 1,
        type: '2D Perimeter & Area',
        prompt: 'A rectangle has a length of 12 cm and a width of 7 cm. Calculate its perimeter and area.',
        hint: 'Perimeter = 2(l + w) = 2(19) = 38 cm. Area = l × w = 12 × 7 = 84 cm².',
        sample: 'Perimeter = 38 cm, Area = 84 cm²',
      },
      {
        step: 2,
        type: 'Circle Calculations',
        prompt: 'Calculate the circumference and area of a circle with radius r = 7 cm (take π = 22/7).',
        hint: 'Circumference = 2πr = 2 × (22/7) × 7 = 44 cm. Area = πr² = (22/7) × 49 = 154 cm².',
        sample: 'Circumference = 44 cm, Area = 154 cm²',
      },
      {
        step: 3,
        type: '3D Surface Area & Volume',
        prompt: 'A rectangular prism has length 8 cm, width 5 cm, and height 4 cm. Calculate its total surface area and volume.',
        hint: 'Volume = 8 × 5 × 4 = 160 cm³. Surface Area = 2(40 + 32 + 20) = 2(92) = 184 cm².',
        sample: 'Volume = 160 cm³, Surface Area = 184 cm²',
      },
    ];
  }

  // 12. Financial Mathematics
  if (normTopic.includes('financial') || normTopic.includes('interest') || normTopic.includes('depreciation') || normTopic.includes('loan')) {
    return [
      {
        step: 1,
        type: 'Simple Interest',
        prompt: 'Calculate the accumulated amount A after 3 years if R5 000 is invested at 8% p.a. simple interest (A = P(1 + i·n)).',
        hint: 'P = 5000, i = 0,08, n = 3. A = 5000(1 + 0,24) = 5000 × 1,24.',
        sample: 'R6 200',
      },
      {
        step: 2,
        type: 'Compound Interest',
        prompt: 'Calculate the final balance if R10 000 is invested at 9% p.a. compound interest for 2 years (A = P(1 + i)^n).',
        hint: 'A = 10000(1 + 0,09)² = 10000 × 1,1881.',
        sample: 'R11 881',
      },
      {
        step: 3,
        type: 'Hire Purchase & Installments',
        prompt: 'An item costs R6 000. A 10% deposit is paid. The remaining balance is financed at 15% p.a. simple interest over 2 years. Calculate the monthly installment.',
        hint: 'Deposit = R600, Loan = R5 400. Interest = 5400 × 0,15 × 2 = R1 620. Total = R7 020. Divide by 24 months.',
        sample: 'R292,50 per month',
      },
    ];
  }

  // 13. Data Handling & Probability
  if (normTopic.includes('data') || normTopic.includes('stat') || normTopic.includes('probability')) {
    return [
      {
        step: 1,
        type: 'Measures of Central Tendency',
        prompt: 'For the data set {3, 6, 7, 7, 9, 12, 18}, find the mean, median, and mode.',
        hint: 'Sum = 62 / 7 ≈ 8,86. Median is 4th number = 7. Mode is most frequent = 7.',
        sample: 'Mean = 8,86; Median = 7; Mode = 7',
      },
      {
        step: 2,
        type: 'Five-Number Summary Values',
        prompt: 'For {3, 6, 7, 7, 9, 12, 18}, determine the minimum, lower quartile (Q1), upper quartile (Q3), and maximum.',
        hint: 'Min = 3, Max = 18. Lower half {3, 6, 7} => Q1 = 6. Upper half {7, 9, 12, 18} => Q3 = 12.',
        sample: 'Min = 3, Q1 = 6, Median = 7, Q3 = 12, Max = 18',
      },
      {
        step: 3,
        type: 'Probability Application',
        prompt: 'A bag has 5 blue, 3 red, and 2 green marbles. What is the probability of drawing a red marble? What is the probability of NOT drawing a blue marble?',
        hint: 'Total = 10. P(red) = 3/10. Non-blue = 5/10 = 1/2.',
        sample: 'P(red) = 3/10 (or 0,3); P(not blue) = 1/2 (or 0,5)',
      },
    ];
  }

  // Universal Procedural Fallback — strictly concrete calculation problems, ZERO semantic definitions!
  return [
    {
      step: 1,
      type: 'Prerequisite Operational Check',
      prompt: `Given values a = 6 and b = 4, calculate the numeric value of 2a² − 3b + 5 for ${topicTitle}.`,
      hint: 'Evaluate the square first: a² = 36. Then: 2(36) − 3(4) + 5 = 72 − 12 + 5.',
      sample: '65',
    },
    {
      step: 2,
      type: 'Foundational Procedure Application',
      prompt: `Solve the linear relation 5x − 8 = 2x + 13 for x in the context of ${topicTitle}.`,
      hint: 'Subtract 2x from both sides to get 3x − 8 = 13. Add 8 to both sides to get 3x = 21. Divide by 3.',
      sample: 'x = 7',
    },
    {
      step: 3,
      type: 'CAPS Standard Problem',
      prompt: `Calculate the exact result when the sum of 28 and 56 is divided by 7, and the result is multiplied by 3.`,
      hint: 'Brackets first: (28 + 56) = 84. Then 84 ÷ 7 = 12. Finally 12 × 3.',
      sample: '36',
    },
  ];
};

export default function MicroBenchmarkModal({
  isOpen,
  topicTitle = '',
  topic = '',
  subject = 'Mathematics',
  grade = '7',
  currentUser = null,
  onCompleteBenchmark,
  onComplete,
  onClose,
}) {
  const resolvedTopicTitle = topicTitle || topic || 'Topic Calibration';
  const handleComplete = onCompleteBenchmark || onComplete;
  const [currentStep, setCurrentStep] = useState(0);
  const [answers, setAnswers] = useState({});
  const inputRef = useRef(null);

  const isSuperAdmin = Boolean(
    currentUser?.isSuperAdmin ||
    currentUser?.isOwner ||
    (currentUser?.email && isOwnerEmail(currentUser.email)) ||
    (currentUser?.email && currentUser.email.toLowerCase().includes('admin'))
  );

  const storageKey = `fundile_benchmark_${subject}_${grade}_${String(resolvedTopicTitle).replace(/\s+/g, '_')}`;

  const questions = useMemo(
    () => getTopicBenchmarkQuestions(subject, grade, resolvedTopicTitle),
    [subject, grade, resolvedTopicTitle]
  );

  // Restore cached progress if interrupted
  useEffect(() => {
    if (isOpen) {
      try {
        const cached = localStorage.getItem(storageKey);
        if (cached) {
          const parsed = JSON.parse(cached);
          if (parsed.answers) setAnswers(parsed.answers);
          if (typeof parsed.step === 'number') setCurrentStep(parsed.step);
        }
      } catch (e) {
        console.warn('Could not restore benchmark state:', e);
      }
    }
  }, [isOpen, storageKey]);

  const handleAnswerChange = (val) => {
    const nextAnswers = { ...answers, [currentStep]: val };
    setAnswers(nextAnswers);
    try {
      localStorage.setItem(storageKey, JSON.stringify({ step: currentStep, answers: nextAnswers }));
    } catch (e) {}
  };

  const handleInsertMathToken = (token, offset = 0) => {
    const el = inputRef.current;
    const currentVal = answers[currentStep] || '';
    const start = el?.selectionStart ?? currentVal.length;
    const end = el?.selectionEnd ?? currentVal.length;
    const nextVal = currentVal.slice(0, start) + token + currentVal.slice(end);
    handleAnswerChange(nextVal);
    const nextCaret = start + token.length + offset;
    requestAnimationFrame(() => {
      if (el) {
        el.focus();
        el.setSelectionRange(nextCaret, nextCaret);
      }
    });
  };

  const handleNext = () => {
    if (currentStep < questions.length - 1) {
      const nextStep = currentStep + 1;
      setCurrentStep(nextStep);
      try {
        localStorage.setItem(storageKey, JSON.stringify({ step: nextStep, answers }));
      } catch (e) {}
    } else {
      // Completed all questions
      try {
        localStorage.removeItem(storageKey);
      } catch (e) {}
      if (handleComplete) {
        handleComplete(answers);
      }
    }
  };

  const handleSuperAdminBypass = () => {
    try {
      localStorage.setItem(storageKey, JSON.stringify({ calibrated: true, bypassed: true }));
    } catch (e) {}
    if (handleComplete) {
      handleComplete({ bypassed: true });
    }
  };

  if (!isOpen) return null;

  const currentQ = questions[currentStep] || questions[0];
  const hasAnswer = Boolean(answers[currentStep]?.trim());
  const canAdvance = hasAnswer || isSuperAdmin;

  return (
    <div className="fixed inset-0 z-50 bg-slate-50 text-slate-900 flex flex-col min-h-screen overflow-y-auto animate-in fade-in duration-200">
      {/* ── Top Full-Width Brand Ribbon Header ── */}
      <header className="sticky top-0 z-30 bg-brand-blue border-b border-white/10 h-16 shadow-lg shadow-brand-blue/20 px-4 sm:px-8">
        <div className="max-w-5xl mx-auto h-full flex items-center justify-between gap-4 flex-wrap">
          {/* Left: Brand Icon + Back button + Context Title */}
          <div className="flex items-center gap-3 sm:gap-4">
            <div className="flex items-center gap-2 text-white">
              <span className="grid place-items-center h-9 w-9 rounded-xl bg-white/10 ring-1 ring-white/20">
                <span className="text-base">🎓</span>
              </span>
              <span className="font-display font-bold text-lg sm:text-xl tracking-tight hidden sm:inline">Fundile</span>
            </div>

            {onClose && (
              <button
                onClick={onClose}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-white/20 bg-white/10 text-white hover:bg-white/20 transition-colors text-xs font-semibold shadow-2xs cursor-pointer"
                title="Return to topic list"
              >
                <ChevronLeft className="h-4 w-4" />
                <span className="hidden sm:inline">Back to Topics</span>
              </button>
            )}

            <div className="flex items-center gap-2 flex-wrap">
              <span className="px-2.5 py-0.5 rounded-full bg-white/10 border border-white/15 text-white/90 text-xs font-medium">
                Grade {grade} • {subject}
              </span>
              <span className="px-3 py-0.5 rounded-full bg-brand-orange text-white font-semibold text-xs shadow-sm">
                {resolvedTopicTitle}
              </span>
            </div>
          </div>

          {/* Right: Super Admin Bypass + Progress Step + Close */}
          <div className="flex items-center gap-2.5 sm:gap-3">
            {isSuperAdmin && (
              <button
                onClick={handleSuperAdminBypass}
                className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-brand-amber hover:bg-amber-400 text-brand-navy text-xs font-bold transition-all shadow-sm cursor-pointer shrink-0"
                title="Super Admin: Skip diagnostic and enter workspace immediately"
              >
                <Zap className="h-3.5 w-3.5 text-brand-navy fill-current" />
                <span>Skip (Admin Bypass)</span>
              </button>
            )}

            <div className="flex items-center gap-1.5 bg-white/10 border border-white/15 px-3 py-1.5 rounded-xl text-xs font-semibold text-white">
              <Sparkles className="w-3.5 h-3.5 text-brand-amber" />
              <span>Step {currentStep + 1} of {questions.length}</span>
            </div>

            {onClose && (
              <button
                onClick={onClose}
                className="p-1.5 rounded-lg text-white/70 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
                title="Close"
              >
                <X className="h-5 w-5" />
              </button>
            )}
          </div>
        </div>
      </header>

      {/* ── Brand Gradient Progress Ribbon ── */}
      <div className="w-full bg-slate-200/80 h-1.5">
        <div
          className="bg-gradient-to-r from-brand-orange to-brand-amber h-full transition-all duration-300"
          style={{ width: `${((currentStep + 1) / questions.length) * 100}%` }}
        />
      </div>

      {/* ── Main Expansive Stage Area ── */}
      <main className="max-w-4xl mx-auto w-full flex-1 p-4 sm:p-8 flex flex-col justify-center space-y-6">
        {/* Step Navigation Tabs */}
        <div className="flex items-center justify-between flex-wrap gap-3 pb-1">
          <div className="flex items-center gap-2 flex-wrap">
            {questions.map((q, idx) => (
              <button
                key={idx}
                onClick={() => setCurrentStep(idx)}
                className={`flex items-center gap-1.5 px-4 py-2 rounded-full text-xs font-semibold transition-all cursor-pointer ${
                  currentStep === idx
                    ? 'bg-brand-blue text-white shadow-md ring-2 ring-brand-blue/30 font-bold'
                    : answers[idx]?.trim()
                      ? 'bg-emerald-50 text-emerald-700 border border-emerald-200 hover:bg-emerald-100'
                      : 'bg-white text-brand-blue border border-slate-200 hover:bg-slate-50'
                }`}
              >
                <span>Question {idx + 1}</span>
                <span className="hidden sm:inline font-normal text-[11px] opacity-80">• {q.type}</span>
                {answers[idx]?.trim() && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />}
              </button>
            ))}
          </div>

          <span className="text-xs text-slate-500 font-medium">
            3 diagnostic calculations calibrate your prerequisite starting tier
          </span>
        </div>

        {/* Question Learning Card */}
        <div className="bg-white border border-slate-200 rounded-2xl shadow-lift p-6 sm:p-8 space-y-6">
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 rounded-full bg-brand-blue/10 text-brand-blue text-xs font-bold uppercase tracking-wider border border-brand-blue/20">
                {currentQ.type}
              </span>
              <span className="text-xs font-semibold text-slate-400">
                Question {currentStep + 1} of {questions.length}
              </span>
            </div>

            {/* Question Box */}
            <div className="rounded-xl border border-slate-200 bg-slate-50 p-5 space-y-2">
              <div className="text-xs font-bold uppercase tracking-[0.2em] text-brand-blue">Problem Statement</div>
              <h2 className="text-lg sm:text-xl font-medium text-slate-900 leading-relaxed font-display">
                {currentQ.prompt}
              </h2>
            </div>
          </div>

          {currentQ.hint && (
            <div className="flex items-start gap-3 rounded-xl border border-brand-orange/30 bg-amber-50/70 p-4 text-xs sm:text-sm text-slate-700">
              <span className="text-base shrink-0">💡</span>
              <p>
                <span className="font-semibold text-slate-900">Pedagogical Hint: </span>
                {currentQ.hint}
              </p>
            </div>
          )}

          {/* Specialized Mathematics Keypad */}
          <div className="rounded-xl border border-slate-200 bg-slate-50/90 p-3.5 space-y-2">
            <div className="flex items-center justify-between text-xs text-slate-600 font-medium">
              <span className="font-semibold text-slate-700">Specialized Math Keypad (powers, roots, fractions, subscripts):</span>
              <span className="text-[11px] text-slate-400">Click any key to insert at cursor</span>
            </div>
            <MathKeypad
              topic={resolvedTopicTitle}
              onInsert={handleInsertMathToken}
            />
          </div>

          {/* Spacious Multi-line Working Pad & Answer Input */}
          <div className="space-y-2">
            <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
              Your Answer & Working Steps:
            </label>
            <textarea
              ref={inputRef}
              value={answers[currentStep] || ''}
              onChange={(e) => handleAnswerChange(e.target.value)}
              placeholder="Type your final answer or step-by-step working here (use keypad above for exponents, roots, fractions)..."
              className="w-full bg-white border-2 border-slate-200 focus:border-brand-blue rounded-xl p-4 text-sm sm:text-base text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-4 focus:ring-brand-blue/10 transition-all font-mono leading-relaxed min-h-[120px] sm:min-h-[140px] resize-y shadow-2xs"
              autoFocus
            />

            {/* Live Math Preview */}
            {answers[currentStep]?.trim() && (
              <div className="bg-blue-50/70 border border-brand-blue/20 rounded-xl p-3 flex items-center justify-between gap-3 text-xs sm:text-sm">
                <span className="text-brand-blue font-bold shrink-0">Live Math Preview:</span>
                <div className="text-slate-800 font-mono overflow-x-auto py-0.5">
                  <MathText latex={latexify(answers[currentStep])} />
                </div>
              </div>
            )}

            <p className="text-[11px] text-slate-400">
              Tip: South African comma decimal (`,`) is supported. You can show your working steps or enter the final calculated value.
            </p>
          </div>

          {/* Action Footer Bar */}
          <div className="border-t border-slate-200 bg-slate-50 px-2 py-3 rounded-xl flex flex-wrap gap-3 items-center justify-between">
            {currentStep > 0 ? (
              <button
                onClick={() => setCurrentStep(prev => prev - 1)}
                className="px-4 py-2.5 rounded-xl border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 text-xs font-semibold transition-colors cursor-pointer flex items-center gap-1.5"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous</span>
              </button>
            ) : <div />}

            <button
              onClick={handleNext}
              disabled={!canAdvance}
              className={`flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
                canAdvance
                  ? 'bg-brand-orange hover:bg-brand-orangeDark text-white shadow-ribbon active:scale-95'
                  : 'bg-slate-200 text-slate-400 cursor-not-allowed'
              }`}
            >
              <span>{currentStep === questions.length - 1 ? 'Finish & Calibrate ✓' : 'Next Question →'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
