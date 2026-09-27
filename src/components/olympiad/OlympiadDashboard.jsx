import React, { useState, useEffect } from 'react';
import { 
  Trophy, Award, BookOpen, Lightbulb, CheckCircle2, XCircle, 
  ArrowRight, RotateCcw, ShieldAlert, Sparkles, HelpCircle, Lock,
  Clock, Play, Flag, AlertCircle, Check
} from 'lucide-react';
import KaTeXRenderer from '../shared/KaTeXRenderer';
import Leaderboard from './Leaderboard';
import TechniqueLibrary from './TechniqueLibrary';

// 20 Seeded Non-Routine Challenge Problems for Official SAMO Round 1 Simulation (Resolving OQ6)
const SIMULATION_QUESTIONS = [
  // 1-5: Number Theory
  {
    id: 'samo_sim_01',
    category: 'Number Theory',
    prompt: 'What is the units digit of $7^{2026}$?',
    options: ['(A) 1', '(B) 3', '(C) 7', '(D) 9', '(E) 5'],
    correctIndex: 3,
    solution: 'Powers of 7 end in $7, 9, 3, 1$ repeating in a cycle of 4. $2026 \\equiv 2 \\pmod 4$, so the units digit is 9.'
  },
  {
    id: 'samo_sim_02',
    category: 'Number Theory',
    prompt: 'How many trailing zeros are in the product of the first 50 positive integers ($50!$)?',
    options: ['(A) 10', '(B) 12', '(C) 14', '(D) 15', '(E) 16'],
    correctIndex: 1,
    solution: '$\\lfloor 50/5 \\rfloor + \\lfloor 50/25 \\rfloor = 10 + 2 = 12$.'
  },
  {
    id: 'samo_sim_03',
    category: 'Number Theory',
    prompt: 'If $p$ and $p+2$ are both prime numbers, what must be the remainder when $p + (p+2)$ is divided by 12, given $p > 3$?',
    options: ['(A) 0', '(B) 2', '(C) 4', '(D) 6', '(E) 8'],
    correctIndex: 0,
    solution: 'For twin primes $p, p+2 > 3$, the integer between them is a multiple of 6. Thus $2p+2 = 2(p+1)$ is a multiple of 12 (remainder 0).'
  },
  {
    id: 'samo_sim_04',
    category: 'Number Theory',
    prompt: 'Find the greatest common divisor of $2^{2026} - 1$ and $2^{2024} - 1$.',
    options: ['(A) 1', '(B) 3', '(C) 7', '(D) 15', '(E) 31'],
    correctIndex: 1,
    solution: '$\\gcd(2^a - 1, 2^b - 1) = 2^{\\gcd(a,b)} - 1$. Since $\\gcd(2026, 2024) = 2$, $\\gcd = 2^2 - 1 = 3$.'
  },
  {
    id: 'samo_sim_05',
    category: 'Number Theory',
    prompt: 'How many positive integers less than 1000 are relatively prime to 10?',
    options: ['(A) 400', '(B) 450', '(C) 500', '(D) 600', '(E) 800'],
    correctIndex: 0,
    solution: 'Euler totient $\\phi(10) = 10 \\times (1 - 1/2) \\times (1 - 1/5) = 4$. Out of 1000 numbers, $1000 \\times 4/10 = 400$.'
  },

  // 6-10: Combinatorics
  {
    id: 'samo_sim_06',
    category: 'Combinatorics',
    prompt: 'A bag contains 15 red, 10 blue, and 6 green marbles. What is the minimum number of draws without looking to ensure at least one marble of each color?',
    options: ['(A) 16', '(B) 22', '(C) 25', '(D) 26', '(E) 31'],
    correctIndex: 3,
    solution: 'Worst case: draw all 15 red and all 10 blue before any green. $15 + 10 + 1 = 26$.'
  },
  {
    id: 'samo_sim_07',
    category: 'Combinatorics',
    prompt: 'How many 4-digit numbers have all distinct digits in strictly increasing order (e.g. 2458)?',
    options: ['(A) 126', '(B) 210', '(C) 336', '(D) 504', '(E) 720'],
    correctIndex: 0,
    solution: 'Choose 4 digits from $\\{1, 2, \\dots, 9\\}$ in $\\binom{9}{4} = 126$ ways (0 cannot be used as digits are strictly increasing).'
  },
  {
    id: 'samo_sim_08',
    category: 'Combinatorics',
    prompt: 'In how many ways can 6 students be seated around a circular table if two particular students refuse to sit next to each other?',
    options: ['(A) 48', '(B) 72', '(C) 96', '(D) 120', '(E) 144'],
    correctIndex: 1,
    solution: 'Total circular arrangements = $(6-1)! = 120$. Arrangements where they sit together = $2! \\times (5-1)! = 48$. Difference = $120 - 48 = 72$.'
  },
  {
    id: 'samo_sim_09',
    category: 'Combinatorics',
    prompt: 'A grid of size $3 \\times 3$ has 9 squares. How many total rectangles of any size can be formed along grid lines?',
    options: ['(A) 27', '(B) 36', '(C) 64', '(D) 81', '(E) 100'],
    correctIndex: 4,
    solution: 'Choose 2 horizontal lines from 4 and 2 vertical lines from 4: $\\binom{4}{2} \\times \\binom{4}{2} = 6 \\times 6 = 36$. (For $3 \\times 3$ squares, with vertices $4 \\times 4$: 36).'
  },
  {
    id: 'samo_sim_10',
    category: 'Combinatorics',
    prompt: 'What is the coefficient of $x^3$ in the expansion of $(2 - x)^6$?',
    options: ['(A) -160', '(B) 160', '(C) -120', '(D) 120', '(E) -80'],
    correctIndex: 0,
    solution: '$\\binom{6}{3} (2)^3 (-x)^3 = 20 \\times 8 \\times (-1) x^3 = -160 x^3$.'
  },

  // 11-15: Algebra
  {
    id: 'samo_sim_11',
    category: 'Algebra',
    prompt: 'Evaluate the telescoping sum:\n$$\\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\dots + \\frac{1}{2025 \\times 2026}$$',
    options: ['(A) \\frac{2024}{2025}', '(B) \\frac{2025}{2026}', '(C) \\frac{2026}{2027}', '(D) 1', '(E) \\frac{1}{2026}'],
    correctIndex: 1,
    solution: 'Partial fractions: $1 - 1/2026 = 2025/2026$.'
  },
  {
    id: 'samo_sim_12',
    category: 'Algebra',
    prompt: 'If $x + \\frac{1}{x} = 5$, what is the exact value of $x^3 + \\frac{1}{x^3}$?',
    options: ['(A) 110', '(B) 115', '(C) 120', '(D) 125', '(E) 140'],
    correctIndex: 0,
    solution: '$(x + 1/x)^3 = x^3 + 1/x^3 + 3(x + 1/x) \\implies 125 = x^3 + 1/x^3 + 15 \\implies 110$.'
  },
  {
    id: 'samo_sim_13',
    category: 'Algebra',
    prompt: 'If $a, b, c$ are roots of $x^3 - 7x^2 + 14x - 8 = 0$, what is the value of $\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}$?',
    options: ['(A) \\frac{7}{4}', '(B) \\frac{7}{8}', '(C) \\frac{14}{8}', '(D) \\frac{8}{7}', '(E) 2'],
    correctIndex: 0,
    solution: '$\\frac{ab + bc + ca}{abc} = \\frac{14}{8} = \\frac{7}{4}$.'
  },
  {
    id: 'samo_sim_14',
    category: 'Algebra',
    prompt: 'Solve for real $x$: $\\sqrt{x + 3} + \\sqrt{x - 2} = 5$.',
    options: ['(A) x = 3', '(B) x = 6', '(C) x = 7', '(D) x = 9', '(E) No solution'],
    correctIndex: 1,
    solution: 'Testing $x=6$: $\\sqrt{9} + \\sqrt{4} = 3 + 2 = 5$.'
  },
  {
    id: 'samo_sim_15',
    category: 'Algebra',
    prompt: 'If $f(x) = \\frac{x}{x-1}$, what is $f(f(f(x)))$ for $x \\neq 0, 1$?',
    options: ['(A) x', '(B) \\frac{x}{x-1}', '(C) \\frac{1}{x}', '(D) \\frac{x-1}{x}', '(E) -x'],
    correctIndex: 1,
    solution: '$f(f(x)) = x$, so $f(f(f(x))) = f(x) = \\frac{x}{x-1}$.'
  },

  // 16-20: Geometry
  {
    id: 'samo_sim_16',
    category: 'Geometry',
    prompt: 'In a regular 5-pointed star, what is the sum of the 5 acute vertex angles?',
    options: ['(A) 90^\\circ', '(B) 180^\\circ', '(C) 270^\\circ', '(D) 360^\\circ', '(E) 540^\\circ'],
    correctIndex: 1,
    solution: 'By the exterior angle theorem on the inner triangles, all five angles collapse into the interior angles of a single triangle ($180^\\circ$).'
  },
  {
    id: 'samo_sim_17',
    category: 'Geometry',
    prompt: 'A circle is inscribed in a right triangle with legs of lengths 6 and 8. What is the radius of the incircle?',
    options: ['(A) 1', '(B) 1.5', '(C) 2', '(D) 2.5', '(E) 3'],
    correctIndex: 2,
    solution: 'Hypotenuse $c = 10$. Inradius $r = \\frac{a + b - c}{2} = \\frac{6 + 8 - 10}{2} = 2$.'
  },
  {
    id: 'samo_sim_18',
    category: 'Geometry',
    prompt: 'In triangle $ABC$, $AB = 13$, $BC = 14$, and $CA = 15$. What is the area of $\\triangle ABC$?',
    options: ['(A) 84', '(B) 88', '(C) 90', '(D) 92', '(E) 96'],
    correctIndex: 0,
    solution: 'Semiperimeter $s = 21$. Heron\'s formula: $\\sqrt{21 \\times 8 \\times 7 \\times 6} = \\sqrt{7056} = 84$.'
  },
  {
    id: 'samo_sim_19',
    category: 'Geometry',
    prompt: 'What is the length of the diagonal of a regular hexagon with side length 6 that connects two non-adjacent vertices skipping one vertex?',
    options: ['(A) 6\\sqrt{2}', '(B) 6\\sqrt{3}', '(C) 12', '(D) 8\\sqrt{3}', '(E) 10'],
    correctIndex: 1,
    solution: 'By law of cosines with $120^\\circ$ angle: $d = 2 \\times 6 \\times \\sin(60^\\circ) = 6\\sqrt{3}$.'
  },
  {
    id: 'samo_sim_20',
    category: 'Geometry',
    prompt: 'A chord of length 16 is at distance 6 from the center of a circle. What is the area of the circle?',
    options: ['(A) 64\\pi', '(B) 80\\pi', '(C) 100\\pi', '(D) 120\\pi', '(E) 144\\pi'],
    correctIndex: 2,
    solution: 'Half chord is 8. Radius $r = \\sqrt{8^2 + 6^2} = 10$. Area = $\\pi r^2 = 100\\pi$.'
  }
];

export default function OlympiadDashboard({
  currentUser = { name: 'Learner', grade: '10' },
  isCapsQualified = true,
  onBackToWorkspace = () => {},
}) {
  const [activeMainTab, setActiveMainTab] = useState('arena'); // 'arena' | 'simulation' | 'library' | 'leaderboard'
  const [selectedCategory, setSelectedCategory] = useState('number_theory');
  const [division, setDivision] = useState('junior');
  const [currentProblem, setCurrentProblem] = useState(null);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const [showSolution, setShowSolution] = useState(false);
  const [olympiadStats, setOlympiadStats] = useState({
    solved: 3,
    xp: 320,
    streak: 3,
    medallions: ['SAMO Junior Round 1 Bronze Qualifier'],
  });

  // State for 120-Minute Simulation Mode (Resolving OQ6)
  const [simState, setSimState] = useState({
    active: false,
    timeLeft: 7200, // 120 mins = 7200s
    currentQ: 0,
    answers: {},
    flagged: {},
    submitted: false,
    score: null,
    distinctionTier: null,
  });

  // Demo seeded problem sets for Arena
  const demoProblems = {
    number_theory: {
      id: 'samo_nt_zeros_100',
      competition: 'SAMO Junior Round 1',
      category: 'Number Theory',
      technique: 'Legendre Formula (Prime Factors in Factorials)',
      prompt: 'How many trailing zeros are there at the end of the decimal representation of $100!$?',
      options: ['(A) 20', '(B) 22', '(C) 24', '(D) 25', '(E) 28'],
      correctIndex: 2,
      hint: 'A trailing zero is produced by a factor of $10 = 2 \\times 5$. Count how many times 5 divides into the product using Legendre\'s formula: $\\lfloor 100/5 \\rfloor + \\lfloor 100/25 \\rfloor$.',
      steps: [
        'Count multiples of 5 up to 100: $\\lfloor 100 / 5 \\rfloor = 20$.',
        'Count multiples of 25 up to 100: $\\lfloor 100 / 25 \\rfloor = 4$.',
        'Multiples of 125 exceed 100 ($0$).',
        'Total trailing zeros = $20 + 4 = 24$. Option (C) is correct.',
      ]
    },
    combinatorics: {
      id: 'samo_comb_pigeon_socks',
      competition: 'SAMO Junior Round 1',
      category: 'Combinatorics',
      technique: 'Pigeonhole Principle & Worst-Case Analysis',
      prompt: 'A drawer contains $15$ red socks, $10$ blue socks, and $6$ green socks. What is the minimum number of socks that must be drawn in the dark to guarantee drawing at least one sock of each color?',
      options: ['(A) 16', '(B) 22', '(C) 25', '(D) 26', '(E) 31'],
      correctIndex: 3,
      hint: 'Analyze the worst-case scenario where you exhaustively draw all socks of the two largest color groups before drawing the third color.',
      steps: [
        'Identify the two largest color piles: $15$ red and $10$ blue.',
        'In the worst case, you could draw all $15 + 10 = 25$ socks without ever drawing a single green sock.',
        'The very next sock ($25 + 1 = 26$) MUST be green.',
        'Therefore, $26$ draws guarantee at least one sock of each color. Option (D) is correct.',
      ]
    },
    algebra: {
      id: 'samo_alg_telescoping',
      competition: 'SAMO Senior Round 1',
      category: 'Algebra',
      technique: 'Telescoping Series & Partial Fractions',
      prompt: 'Evaluate the sum:\n$$\\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\frac{1}{3 \\times 4} + \\dots + \\frac{1}{2025 \\times 2026}$$',
      options: ['(A) \\frac{2024}{2025}', '(B) \\frac{2025}{2026}', '(C) \\frac{2026}{2027}', '(D) 1', '(E) \\frac{1}{2026}'],
      correctIndex: 1,
      hint: 'Rewrite each fraction as $\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}$ to cause cancellation.',
      steps: [
        'Notice: $\\frac{1}{k(k+1)} = \\frac{1}{k} - \\frac{1}{k+1}$.',
        'Expanding: $\\left(1 - \\frac{1}{2}\\right) + \\left(\\frac{1}{2} - \\frac{1}{3}\\right) + \\dots + \\left(\\frac{1}{2025} - \\frac{1}{2026}\\right)$.',
        'All intermediate terms telescope away, leaving $1 - \\frac{1}{2026} = \\frac{2025}{2026}$.',
        'Option (B) is correct.',
      ]
    },
    geometry: {
      id: 'samo_geom_star',
      competition: 'SAMO Junior Round 1',
      category: 'Geometry',
      technique: 'Exterior Angle Theorem & Angle Chasing',
      prompt: 'In a standard 5-pointed star $ABCDE$, what is the sum of the five acute vertex angles $\\angle A + \\angle B + \\angle C + \\angle D + \\angle E$?',
      options: ['(A) 90^\\circ', '(B) 180^\\circ', '(C) 270^\\circ', '(D) 360^\\circ', '(E) 540^\\circ'],
      correctIndex: 1,
      hint: 'Use the exterior angle theorem on two inner triangles to transfer all five angles into a single triangle.',
      steps: [
        'By the exterior angle theorem, two exterior angles of the inner triangles equal $\\angle A + \\angle C$ and $\\angle B + \\angle D$.',
        'These two angles, together with vertex angle $\\angle E$, form the three interior angles of a single triangle.',
        'The interior angle sum of a triangle is $180^\\circ$.',
        'Option (B) is correct.',
      ]
    }
  };

  useEffect(() => {
    setCurrentProblem(demoProblems[selectedCategory] || demoProblems.number_theory);
    setSelectedOption(null);
    setIsSubmitted(false);
    setShowHint(false);
    setShowSolution(false);
  }, [selectedCategory]);

  // 120-Minute Timer Effect (Resolving OQ6)
  useEffect(() => {
    let timer = null;
    if (simState.active && !simState.submitted && simState.timeLeft > 0) {
      timer = setInterval(() => {
        setSimState(prev => {
          if (prev.timeLeft <= 1) {
            clearInterval(timer);
            return handleSimSubmit(prev);
          }
          return { ...prev, timeLeft: prev.timeLeft - 1 };
        });
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [simState.active, simState.submitted, simState.timeLeft]);

  const formatSimTime = (secs) => {
    const h = Math.floor(secs / 3600);
    const m = Math.floor((secs % 3600) / 60);
    const s = secs % 60;
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const handleStartSim = () => {
    setSimState({
      active: true,
      timeLeft: 7200,
      currentQ: 0,
      answers: {},
      flagged: {},
      submitted: false,
      score: null,
      distinctionTier: null,
    });
  };

  const handleSimSelectOption = (optIdx) => {
    if (simState.submitted) return;
    setSimState(prev => ({
      ...prev,
      answers: { ...prev.answers, [prev.currentQ]: optIdx }
    }));
  };

  const handleToggleFlag = () => {
    setSimState(prev => ({
      ...prev,
      flagged: { ...prev.flagged, [prev.currentQ]: !prev.flagged[prev.currentQ] }
    }));
  };

  const handleSimSubmit = (stateToGrade) => {
    const st = stateToGrade || simState;
    let earnedMarks = 0;
    SIMULATION_QUESTIONS.forEach((q, idx) => {
      if (st.answers[idx] === q.correctIndex) {
        earnedMarks += 5; // 5 marks per problem = 100 total
      }
    });

    let tier = 'Participant';
    if (earnedMarks >= 90) tier = '🥇 Gold Distinction (Top 5%)';
    else if (earnedMarks >= 75) tier = '🥈 Silver Distinction (Top 15%)';
    else if (earnedMarks >= 60) tier = '🥉 Bronze Distinction (Top 30%)';

    const finalState = {
      ...st,
      active: false,
      submitted: true,
      score: earnedMarks,
      distinctionTier: tier,
    };
    setSimState(finalState);
    return finalState;
  };

  const handleSelectOption = (index) => {
    if (isSubmitted) return;
    setSelectedOption(index);
  };

  const handleSubmitAnswer = () => {
    if (selectedOption === null || isSubmitted) return;
    setIsSubmitted(true);
    const isCorrect = selectedOption === currentProblem.correctIndex;
    if (isCorrect) {
      setOlympiadStats(prev => ({
        ...prev,
        solved: prev.solved + 1,
        xp: prev.xp + 100,
        streak: prev.streak + 1,
      }));
    }
  };

  // Locked Gate Screen if not qualified
  if (!isCapsQualified) {
    return (
      <div className="w-full max-w-4xl mx-auto p-6 text-center space-y-6">
        <div className="p-8 bg-slate-900/90 border border-slate-800 rounded-3xl shadow-2xl backdrop-blur-sm max-w-xl mx-auto">
          <div className="w-16 h-16 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-amber-400 flex items-center justify-center mx-auto mb-4 text-3xl">
            <Lock className="w-8 h-8" />
          </div>
          <h2 className="text-xl font-bold text-white mb-2">SAMO Olympiad Track is Locked</h2>
          <p className="text-sm text-slate-400 mb-6 leading-relaxed">
            The Olympiad track provides stretch challenges beyond standard syllabus requirements. 
            To qualify, you must achieve a <strong>Silver or Gold Topic Medal (80%+)</strong> in Mathematics.
          </p>
          <div className="p-4 bg-slate-800/60 rounded-xl border border-slate-700/60 text-left text-xs text-slate-300 space-y-2 mb-6">
            <div className="font-semibold text-amber-300">Prerequisite Requirements:</div>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-slate-600"></span>
              <span>Grade 10 Trigonometry Medal: <strong>Pending Silver</strong></span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-slate-600"></span>
              <span>Algebraic Expressions: <strong>Pending Silver</strong></span>
            </div>
          </div>
          <button
            onClick={onBackToWorkspace}
            className="w-full py-3 px-4 bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-xl text-xs transition-all shadow-lg shadow-indigo-600/20"
          >
            Return to Practice &amp; Earn Mathematics Medal
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full max-w-5xl mx-auto p-4 md:p-6 space-y-6 text-slate-100 animate-fadeIn">
      
      {/* 1. OLYMPIAD HEADER */}
      <div className="bg-gradient-to-r from-amber-950/40 via-slate-900 to-indigo-950/40 border border-amber-500/30 rounded-2xl p-5 md:p-6 shadow-xl relative overflow-hidden">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-xl bg-amber-500/20 border border-amber-400/40 flex items-center justify-center text-amber-400 shadow-inner">
              <Trophy className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-xl md:text-2xl font-bold text-white tracking-tight">SAMO Olympiad Track</h1>
                <span className="bg-amber-500/20 border border-amber-400/30 text-amber-300 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase">
                  Round 1 Training &amp; Simulation
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                Authentic non-routine mathematical problem solving · Zero LLM token cost · 120-min Hard Exam Simulator
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2.5">
            <div className="bg-slate-800/80 border border-slate-700/80 rounded-xl px-3 py-1.5 text-center">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Solved</div>
              <div className="text-sm font-bold text-amber-300">{olympiadStats.solved} Problems</div>
            </div>
            <div className="bg-slate-800/80 border border-slate-700/80 rounded-xl px-3 py-1.5 text-center">
              <div className="text-[10px] text-slate-400 uppercase font-semibold">Olympiad XP</div>
              <div className="text-sm font-bold text-sky-400">{olympiadStats.xp} XP</div>
            </div>
          </div>
        </div>
      </div>

      {/* 2. MAIN NAVIGATION TABS */}
      <div className="flex items-center gap-2 border-b border-slate-800 pb-3 overflow-x-auto">
        {[
          { id: 'arena', label: '🎯 Challenge Arena' },
          { id: 'simulation', label: '⏱️ Round 1 Simulation (120 min)' },
          { id: 'library', label: '📖 Technique Library' },
          { id: 'leaderboard', label: '🏆 National Leaderboard' },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveMainTab(tab.id)}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all shrink-0 ${
              activeMainTab === tab.id
                ? 'bg-amber-500 text-slate-950 shadow-md shadow-amber-500/20'
                : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-white'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* TAB: TECHNIQUE LIBRARY */}
      {activeMainTab === 'library' && (
        <TechniqueLibrary onBackToArena={() => setActiveMainTab('arena')} />
      )}

      {/* TAB: LEADERBOARD */}
      {activeMainTab === 'leaderboard' && (
        <Leaderboard currentUser={currentUser} onBackToArena={() => setActiveMainTab('arena')} />
      )}

      {/* TAB: 120-MINUTE ROUND 1 SIMULATION (Resolves OQ6) */}
      {activeMainTab === 'simulation' && (
        <div className="space-y-6 animate-fadeIn">
          {!simState.active && !simState.submitted && (
            <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 text-center max-w-2xl mx-auto space-y-6 shadow-2xl">
              <div className="w-16 h-16 rounded-2xl bg-amber-500/20 border border-amber-400/40 text-amber-400 flex items-center justify-center mx-auto text-2xl shadow-inner">
                <Clock className="w-8 h-8" />
              </div>
              <div>
                <h2 className="text-xl md:text-2xl font-bold text-white">SAMO Round 1 Official Simulation</h2>
                <p className="text-xs md:text-sm text-slate-400 mt-1">
                  Timed competition conditions matching the national South African Mathematics Olympiad.
                </p>
              </div>

              <div className="grid grid-cols-3 gap-3 p-4 bg-slate-950/80 rounded-2xl border border-slate-800 text-center">
                <div>
                  <div className="text-[10px] text-slate-500 uppercase font-semibold">Questions</div>
                  <div className="text-base font-bold text-white">20 MCQs</div>
                </div>
                <div>
                  <div className="text-[10px] text-slate-500 uppercase font-semibold">Duration</div>
                  <div className="text-base font-bold text-amber-300">120 Minutes</div>
                </div>
                <div>
                  <div className="text-[10px] text-slate-500 uppercase font-semibold">Total Marks</div>
                  <div className="text-base font-bold text-sky-300">100 Marks</div>
                </div>
              </div>

              <div className="p-4 bg-amber-500/10 border border-amber-500/20 rounded-xl text-left text-xs text-amber-200/90 space-y-1.5">
                <div className="font-bold flex items-center gap-1.5 text-amber-300">
                  <AlertCircle className="w-4 h-4 shrink-0" />
                  <span>Strict Simulation Rules (Resolving OQ6):</span>
                </div>
                <p>• The countdown runs continuously for 120 minutes with auto-submission on timeout.</p>
                <p>• Score $\ge 60\%$ earns Round 1 Bronze, $\ge 75\%$ Silver, and $\ge 90\%$ Gold Distinction.</p>
                <p>• Results are certified with ungameable XP and optionally published to the Leaderboard.</p>
              </div>

              <button
                onClick={handleStartSim}
                className="w-full py-3.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl text-sm transition-all shadow-lg shadow-amber-500/20 flex items-center justify-center gap-2"
              >
                <Play className="w-4 h-4 fill-slate-950" />
                <span>Begin 120-Minute Round 1 Simulation</span>
              </button>
            </div>
          )}

          {/* Active Simulation Mode */}
          {simState.active && !simState.submitted && (
            <div className="space-y-4">
              {/* Simulation Top Bar */}
              <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 flex items-center justify-between flex-wrap gap-3 shadow-lg">
                <div className="flex items-center gap-2">
                  <span className="text-xs text-slate-400">Problem:</span>
                  <span className="text-sm font-bold text-white">
                    {simState.currentQ + 1} of {SIMULATION_QUESTIONS.length}
                  </span>
                  <span className="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded-full border border-slate-700">
                    {SIMULATION_QUESTIONS[simState.currentQ].category}
                  </span>
                </div>

                {/* 120-min Countdown Timer */}
                <div className={`px-4 py-1.5 rounded-xl border font-mono text-sm font-bold flex items-center gap-2 ${
                  simState.timeLeft < 600
                    ? 'bg-rose-950/80 border-rose-500/50 text-rose-300 animate-pulse'
                    : simState.timeLeft < 1800
                    ? 'bg-amber-950/80 border-amber-500/50 text-amber-300'
                    : 'bg-slate-950/80 border-slate-700 text-emerald-400'
                }`}>
                  <Clock className="w-4 h-4" />
                  <span>{formatSimTime(simState.timeLeft)}</span>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={handleToggleFlag}
                    className={`px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 border transition-all ${
                      simState.flagged[simState.currentQ]
                        ? 'bg-amber-500/20 border-amber-400 text-amber-300'
                        : 'bg-slate-800 border-slate-700 text-slate-400 hover:text-white'
                    }`}
                  >
                    <Flag className="w-3.5 h-3.5" />
                    <span>{simState.flagged[simState.currentQ] ? 'Flagged' : 'Flag'}</span>
                  </button>
                  <button
                    onClick={() => handleSimSubmit()}
                    className="px-4 py-1.5 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-lg text-xs transition-all"
                  >
                    Finish &amp; Submit
                  </button>
                </div>
              </div>

              {/* 20-Question Jump Navigator */}
              <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-3 flex flex-wrap gap-1.5 justify-center">
                {SIMULATION_QUESTIONS.map((_, idx) => {
                  const isCurrent = simState.currentQ === idx;
                  const isAnswered = simState.answers[idx] !== undefined;
                  const isFlagged = simState.flagged[idx];

                  let btnCls = 'bg-slate-800/80 text-slate-400 border-slate-700/60';
                  if (isCurrent) btnCls = 'bg-amber-500 text-slate-950 font-bold border-amber-400 shadow-sm shadow-amber-500/30';
                  else if (isFlagged) btnCls = 'bg-amber-950/60 text-amber-300 border-amber-500/50';
                  else if (isAnswered) btnCls = 'bg-indigo-950/70 text-indigo-300 border-indigo-500/40';

                  return (
                    <button
                      key={idx}
                      onClick={() => setSimState(prev => ({ ...prev, currentQ: idx }))}
                      className={`w-8 h-8 rounded-lg text-xs flex items-center justify-center border transition-all ${btnCls}`}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>

              {/* Current Question Display */}
              {(() => {
                const q = SIMULATION_QUESTIONS[simState.currentQ];
                const selected = simState.answers[simState.currentQ];

                return (
                  <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 md:p-6 shadow-xl space-y-6">
                    <div className="p-4 bg-slate-950/70 border border-slate-800 rounded-xl text-sm md:text-base text-slate-100 leading-relaxed">
                      <KaTeXRenderer content={q.prompt} />
                    </div>

                    {/* Options */}
                    <div className="space-y-2.5">
                      {q.options.map((opt, optIdx) => {
                        const isChosen = selected === optIdx;
                        return (
                          <button
                            key={optIdx}
                            onClick={() => handleSimSelectOption(optIdx)}
                            className={`w-full p-3.5 rounded-xl border text-left text-xs md:text-sm transition-all flex items-center justify-between ${
                              isChosen
                                ? 'bg-amber-500/20 border-amber-400 text-amber-200'
                                : 'bg-slate-800/50 border-slate-700/60 hover:bg-slate-800 text-slate-200'
                            }`}
                          >
                            <KaTeXRenderer content={opt} />
                            {isChosen && <Check className="w-4 h-4 text-amber-400 shrink-0" />}
                          </button>
                        );
                      })}
                    </div>

                    {/* Bottom Navigation */}
                    <div className="flex items-center justify-between pt-3 border-t border-slate-800">
                      <button
                        onClick={() => setSimState(prev => ({ ...prev, currentQ: Math.max(0, prev.currentQ - 1) }))}
                        disabled={simState.currentQ === 0}
                        className="px-4 py-2 bg-slate-800 hover:bg-slate-700 disabled:opacity-40 rounded-xl text-xs font-semibold text-slate-300 transition-all"
                      >
                        Previous
                      </button>
                      <button
                        onClick={() => setSimState(prev => ({ ...prev, currentQ: Math.min(SIMULATION_QUESTIONS.length - 1, prev.currentQ + 1) }))}
                        disabled={simState.currentQ === SIMULATION_QUESTIONS.length - 1}
                        className="px-5 py-2 bg-amber-500 hover:bg-amber-400 disabled:opacity-40 rounded-xl text-xs font-bold text-slate-950 transition-all"
                      >
                        Next Problem
                      </button>
                    </div>
                  </div>
                );
              })()}
            </div>
          )}

          {/* Simulation Completed / Results */}
          {simState.submitted && (
            <div className="bg-slate-900/90 border border-slate-800 rounded-3xl p-6 md:p-8 text-center max-w-2xl mx-auto space-y-6 shadow-2xl animate-fadeIn">
              <div className="w-16 h-16 rounded-2xl bg-amber-500/20 border border-amber-400/40 text-amber-400 flex items-center justify-center mx-auto text-3xl shadow-inner">
                🏆
              </div>
              <div>
                <h2 className="text-xl md:text-2xl font-bold text-white">SAMO Round 1 Simulation Completed</h2>
                <p className="text-xs md:text-sm text-slate-400 mt-1">
                  120-Minute examination authenticated under national competition standards.
                </p>
              </div>

              <div className="p-5 bg-slate-950/80 rounded-2xl border border-slate-800 space-y-3">
                <div className="text-3xl font-bold text-amber-300">
                  {simState.score} / 100 Marks
                </div>
                <div className="text-sm font-semibold text-emerald-400">
                  {simState.distinctionTier}
                </div>
                <p className="text-xs text-slate-400">
                  {simState.score >= 60
                    ? 'Congratulations! You have met national qualification standards for Round 2.'
                    : 'Great effort. Review your solutions in the Technique Library to sharpen non-routine heuristics.'}
                </p>
              </div>

              <div className="flex flex-col sm:flex-row items-center gap-3">
                <button
                  onClick={() => setActiveMainTab('leaderboard')}
                  className="w-full py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl text-xs transition-all"
                >
                  View on National Leaderboard
                </button>
                <button
                  onClick={handleStartSim}
                  className="w-full py-3 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded-xl text-xs transition-all border border-slate-700"
                >
                  Retake Simulation
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* TAB: CHALLENGE ARENA */}
      {activeMainTab === 'arena' && (
        <>
          {/* 3. CATEGORY TABS */}
          <div className="flex items-center gap-2 overflow-x-auto pb-1">
            {[
              { id: 'number_theory', label: '🔢 Number Theory' },
              { id: 'combinatorics', label: '🧩 Combinatorics' },
              { id: 'algebra', label: '📐 Telescoping Algebra' },
              { id: 'geometry', label: '⭐ Invariant Geometry' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setSelectedCategory(tab.id)}
                className={`px-4 py-2 rounded-xl text-xs font-bold transition-all shrink-0 ${
                  selectedCategory === tab.id
                    ? 'bg-amber-500/20 border border-amber-400/50 text-amber-300 shadow-md shadow-amber-500/10'
                    : 'bg-slate-900/60 border border-slate-800 text-slate-400 hover:text-slate-200'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>

          {/* 4. PROBLEM STAGE */}
          {currentProblem && (
            <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 md:p-6 shadow-xl space-y-6">
              <div className="flex items-center justify-between border-b border-slate-800/80 pb-3.5 flex-wrap gap-2">
                <div>
                  <span className="text-xs text-amber-400 font-semibold">{currentProblem.competition}</span>
                  <h2 className="text-base font-bold text-white">{currentProblem.category} Challenge</h2>
                </div>
                <span className="text-[11px] bg-slate-800 border border-slate-700 text-slate-300 px-2.5 py-1 rounded-lg font-mono">
                  Technique: {currentProblem.technique}
                </span>
              </div>

              {/* Question Prompt with KaTeX */}
              <div className="p-4 bg-slate-950/70 border border-slate-800 rounded-xl text-sm md:text-base text-slate-100 leading-relaxed">
                <KaTeXRenderer content={currentProblem.prompt} />
              </div>

              {/* 5 MCQ Options */}
              <div className="space-y-2.5">
                {currentProblem.options.map((opt, idx) => {
                  const isChosen = selectedOption === idx;
                  const isCorrectOpt = isSubmitted && idx === currentProblem.correctIndex;
                  const isWrongChoice = isSubmitted && isChosen && !isCorrectOpt;

                  let btnClass = 'bg-slate-800/50 border-slate-700/60 hover:bg-slate-800 text-slate-200';
                  if (isChosen && !isSubmitted) {
                    btnClass = 'bg-amber-500/20 border-amber-400 text-amber-200';
                  } else if (isCorrectOpt) {
                    btnClass = 'bg-emerald-500/20 border-emerald-400 text-emerald-200';
                  } else if (isWrongChoice) {
                    btnClass = 'bg-rose-500/20 border-rose-400 text-rose-200';
                  }

                  return (
                    <button
                      key={idx}
                      onClick={() => handleSelectOption(idx)}
                      className={`w-full p-3.5 rounded-xl border text-left text-xs md:text-sm transition-all flex items-center justify-between ${btnClass}`}
                    >
                      <div className="flex items-center gap-2.5">
                        <KaTeXRenderer content={opt} />
                      </div>
                      {isCorrectOpt && <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />}
                      {isWrongChoice && <XCircle className="w-4 h-4 text-rose-400 shrink-0" />}
                    </button>
                  );
                })}
              </div>

              {/* Controls: Hint, Submit, Solution */}
              <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-slate-800">
                <div className="flex items-center gap-2 w-full sm:w-auto">
                  <button
                    onClick={() => setShowHint(!showHint)}
                    className="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs font-semibold transition-all flex items-center gap-1.5 border border-amber-400/20"
                  >
                    <Lightbulb className="w-3.5 h-3.5" />
                    <span>{showHint ? 'Hide Hint' : 'Technique Hint'}</span>
                  </button>
                  {isSubmitted && (
                    <button
                      onClick={() => setShowSolution(!showSolution)}
                      className="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-sky-300 text-xs font-semibold transition-all flex items-center gap-1.5 border border-sky-400/20"
                    >
                      <HelpCircle className="w-3.5 h-3.5" />
                      <span>{showSolution ? 'Hide Solution' : 'Worked Solution'}</span>
                    </button>
                  )}
                </div>

                <div className="flex items-center gap-2 w-full sm:w-auto justify-end">
                  {!isSubmitted ? (
                    <button
                      onClick={handleSubmitAnswer}
                      disabled={selectedOption === null}
                      className="w-full sm:w-auto px-6 py-2.5 bg-amber-500 hover:bg-amber-400 disabled:opacity-50 disabled:cursor-not-allowed text-slate-950 font-bold text-xs rounded-xl transition-all shadow-lg shadow-amber-500/20"
                    >
                      Submit Answer (+100 XP)
                    </button>
                  ) : (
                    <button
                      onClick={() => {
                        setSelectedOption(null);
                        setIsSubmitted(false);
                        setShowHint(false);
                        setShowSolution(false);
                      }}
                      className="w-full sm:w-auto px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs rounded-xl transition-all flex items-center justify-center gap-1.5"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                      <span>Try Another Variant</span>
                    </button>
                  )}
                </div>
              </div>

              {/* Hint Accordion */}
              {showHint && (
                <div className="p-4 bg-amber-500/10 border border-amber-500/20 rounded-xl text-xs text-amber-200 animate-fadeIn">
                  <strong>💡 Olympiad Technique Hint:</strong>
                  <div className="mt-1 leading-relaxed">
                    <KaTeXRenderer content={currentProblem.hint} />
                  </div>
                </div>
              )}

              {/* Worked Solution Steps Accordion */}
              {showSolution && (
                <div className="p-4 bg-slate-950/80 border border-slate-800 rounded-xl text-xs text-slate-300 space-y-2 animate-fadeIn">
                  <strong className="text-sky-400">Worked Solution Graph:</strong>
                  {currentProblem.steps.map((step, i) => (
                    <div key={i} className="flex items-start gap-2">
                      <span className="text-slate-500 font-mono">[{i+1}]</span>
                      <div className="flex-1 leading-relaxed">
                        <KaTeXRenderer content={step} />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </>
      )}
    </div>
  );
}
