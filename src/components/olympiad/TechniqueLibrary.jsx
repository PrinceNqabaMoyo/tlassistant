import React, { useState } from 'react';
import { BookOpen, Sparkles, ChevronRight, Award, Compass, Search } from 'lucide-react';
import KaTeXRenderer from '../shared/KaTeXRenderer';

const TECHNIQUES = [
  {
    id: 'tech_pigeonhole',
    name: 'Pigeonhole Principle (Dirichlet Principle)',
    category: 'Combinatorics',
    tag: 'Worst-Case Analysis',
    summary: 'If $kn + 1$ objects are distributed among $n$ boxes, at least one box must contain at least $k + 1$ objects.',
    formula: '\\text{Objects } > \\text{Boxes} \\implies \\text{Collision Guarantee}',
    example: 'In any group of $367$ people, at least two must share a birthday (since there are at most 366 days in a leap year).',
    tip: 'Always construct the worst-case scenario: fill every box as evenly as possible before placing the deciding element.',
  },
  {
    id: 'tech_modular',
    name: 'Modular Arithmetic & Power Cycles',
    category: 'Number Theory',
    tag: 'Last Digits & Divisibility',
    summary: 'When an integer is repeatedly raised to powers, the sequence of remainders modulo $m$ cycles with a periodic pattern.',
    formula: 'a^k \\pmod m \\quad \\text{cycles with period } \\le m',
    example: 'Powers of $7 \\pmod{10}$: $7^1=7, 7^2=9, 7^3=3, 7^4=1, 7^5=7 \\dots$ Period is 4. So $7^{2026} \\equiv 7^{2} \\equiv 9 \\pmod{10}$.',
    tip: 'Find the period length $p$ by testing small powers. Then calculate exponent $\\pmod p$ to solve in seconds.',
  },
  {
    id: 'tech_telescoping',
    name: 'Telescoping Series & Partial Fractions',
    category: 'Algebra',
    tag: 'Summation Cancellation',
    summary: 'A sum collapses into a few boundary terms when each term is written as a difference of consecutive terms $f(k) - f(k+1)$.',
    formula: '\\sum_{k=1}^n \\left( \\frac{1}{k} - \\frac{1}{k+1} \\right) = 1 - \\frac{1}{n+1} = \\frac{n}{n+1}',
    example: 'Summing $\\frac{1}{1 \\times 2} + \\frac{1}{2 \\times 3} + \\dots + \\frac{1}{2025 \\times 2026} = \\frac{2025}{2026}$.',
    tip: 'Look for fractions with factored denominators and apply partial fractions decomposition.',
  },
  {
    id: 'tech_am_gm',
    name: 'AM-GM Inequality (Arithmetic-Geometric Mean)',
    category: 'Algebra',
    tag: 'Extremal Optimization',
    summary: 'For non-negative real numbers $a, b$, the arithmetic mean is always greater than or equal to the geometric mean.',
    formula: '\\frac{a + b}{2} \\ge \\sqrt{ab}, \\quad \\text{equality holds iff } a = b',
    example: 'To minimize $x + \\frac{16}{x}$ for $x > 0$: $\\frac{x + 16/x}{2} \\ge \\sqrt{16} = 4 \\implies x + 16/x \\ge 8$.',
    tip: 'Equality holds when the two terms are identical: set $x = 16/x \\implies x^2 = 16 \\implies x = 4$.',
  },
  {
    id: 'tech_parity',
    name: 'Parity & Invariant Theory',
    category: 'Geometry & Logic',
    tag: 'Impossibility Proofs',
    summary: 'An invariant is a property (like even/odd parity or color count) that remains unchanged throughout a sequence of legal operations.',
    formula: '\\text{Parity: Even} \\pm \\text{Even} = \\text{Even}, \\quad \\text{Odd} \\pm \\text{Odd} = \\text{Even}',
    example: 'A standard $8 \\times 8$ chessboard has 64 squares (32 black, 32 white). Removing 2 opposite corners leaves 32 white and 30 black squares. Since every $1 \\times 2$ domino covers 1 black and 1 white, it is mathematically impossible to tile the remaining 62 squares.',
    tip: 'To prove an arrangement is impossible, show that the starting and ending states have different invariant values.',
  },
];

export default function TechniqueLibrary() {
  const [activeTab, setActiveTab] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');

  const filteredTechniques = TECHNIQUES.filter((t) => {
    const matchesTab = activeTab === 'all' || t.category.toLowerCase().includes(activeTab);
    const matchesSearch = t.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
                          t.summary.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesTab && matchesSearch;
  });

  return (
    <div className="w-full max-w-5xl mx-auto p-4 md:p-6 space-y-6 text-slate-100 animate-fadeIn">
      {/* Header */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-lg flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 rounded-xl bg-indigo-500/20 border border-indigo-400/40 text-indigo-400 flex items-center justify-center">
            <Compass className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-white">Olympiad Technique Library</h1>
            <p className="text-xs text-slate-400 mt-0.5">
              Core mathematical heuristics and non-routine problem solving patterns for SAMO Round 1
            </p>
          </div>
        </div>

        {/* Search */}
        <div className="relative w-full md:w-64">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-2.5" />
          <input
            type="text"
            placeholder="Search techniques..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-1.5 bg-slate-950 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:border-indigo-400"
          />
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1">
        {['all', 'number theory', 'combinatorics', 'algebra', 'geometry'].map((cat) => (
          <button
            key={cat}
            onClick={() => setActiveTab(cat)}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-semibold uppercase tracking-wider transition-all ${
              activeTab === cat
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20'
                : 'bg-slate-900/80 border border-slate-800 text-slate-400 hover:text-slate-200'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Technique Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredTechniques.map((tech) => (
          <div
            key={tech.id}
            className="bg-slate-900/80 border border-slate-800 hover:border-indigo-500/40 rounded-2xl p-5 shadow-lg transition-all space-y-3.5"
          >
            <div className="flex items-start justify-between gap-2">
              <div>
                <span className="text-[10px] font-bold text-amber-400 uppercase tracking-wider">{tech.category} · {tech.tag}</span>
                <h3 className="text-base font-bold text-white mt-0.5">{tech.name}</h3>
              </div>
            </div>

            <div className="p-3 bg-slate-950/70 border border-slate-800/80 rounded-xl text-xs text-slate-300 leading-relaxed">
              <KaTeXRenderer content={tech.summary} />
            </div>

            {/* Core Formula Box */}
            <div className="p-2.5 bg-indigo-950/30 border border-indigo-500/20 rounded-xl text-center text-xs text-indigo-300 font-mono">
              <KaTeXRenderer content={`$$${tech.formula}$$`} />
            </div>

            {/* Example Problem */}
            <div className="text-xs text-slate-400 space-y-1">
              <span className="font-semibold text-slate-300">Worked Classic Example:</span>
              <p className="italic text-slate-400 pl-2 border-l-2 border-slate-700">
                <KaTeXRenderer content={tech.example} />
              </p>
            </div>

            {/* Pro Tip */}
            <div className="text-[11px] bg-amber-500/10 border border-amber-500/20 rounded-lg p-2 text-amber-200">
              <strong>Competition Tip:</strong> {tech.tip}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
