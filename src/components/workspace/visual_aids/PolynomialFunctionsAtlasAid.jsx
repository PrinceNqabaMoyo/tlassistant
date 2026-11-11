import React, { useState, useMemo } from 'react';
import { Sliders, BookOpen, TrendingUp, RotateCcw, Crosshair } from 'lucide-react';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import MathText from '../shared/mathx/MathText';

/**
 * PolynomialFunctionsAtlasAid
 * ---------------------------
 * Implements the Mathematics Dual-Capacity Standard (diagram_doctrine.md §2.1):
 * - Mode 1 (Annotated Master Atlas): Static high-resolution Cartesian reference plot
 *   displaying domain, range, intercepts, axis of symmetry, turning points (f'(x) = 0),
 *   point of inflection (f''(x) = 0), and vertical/horizontal asymptotes.
 * - Mode 2 (Live Coefficient Sliders & Derivative Tangent Scrubber):
 *   Interactive sliders for parameters (a, b, c, d / p, q) across Cubic, Quadratic,
 *   Hyperbolic, Exponential, and Linear families. Roots, turning points, and asymptotes
 *   recalculate and drift smoothly across the Cartesian plane in real time, accompanied
 *   by a live tangent scrubber at x₀ showing m = f'(x₀).
 */

const FAMILIES = [
  {
    id: 'cubic',
    label: 'Cubic Polynomial',
    formulaLatex: 'f(x) = ax^3 + bx^2 + cx + d',
    grades: 'Grade 12 Calculus',
    defaults: { a: 1, b: -3, c: 0, d: 2, x0: 1.5 },
  },
  {
    id: 'quadratic',
    label: 'Quadratic Parabola',
    formulaLatex: 'f(x) = a(x - p)^2 + q',
    grades: 'Grades 10–12 Functions',
    defaults: { a: 1, p: 1, q: -4, x0: 2.0 },
  },
  {
    id: 'hyperbola',
    label: 'Hyperbola',
    formulaLatex: 'f(x) = \\frac{a}{x - p} + q',
    grades: 'Grades 10–12 Functions',
    defaults: { a: 2, p: 1, q: 1, x0: 2.5 },
  },
  {
    id: 'exponential',
    label: 'Exponential',
    formulaLatex: 'f(x) = a \\cdot b^{x - p} + q',
    grades: 'Grades 10–12 Functions',
    defaults: { a: 1, bBase: 2, p: 0, q: -2, x0: 1.0 },
  },
  {
    id: 'linear',
    label: 'Linear (Straight Line)',
    formulaLatex: 'f(x) = mx + c',
    grades: 'Grades 8–11 Functions',
    defaults: { m: 1.5, c: -1.5, x0: 1.0 },
  },
];

function fmtSa(num, digits = 2) {
  if (!Number.isFinite(num)) return 'undefined';
  const rounded = Number(num.toFixed(digits));
  const str = Object.is(rounded, -0) ? '0' : rounded.toString();
  return str.replace('.', '{,}');
}

function fmtPlain(num, digits = 2) {
  if (!Number.isFinite(num)) return 'undefined';
  const rounded = Number(num.toFixed(digits));
  const str = Object.is(rounded, -0) ? '0' : rounded.toString();
  return str.replace('.', ',');
}

export default function PolynomialFunctionsAtlasAid({ initialFamily = 'cubic' }) {
  const [familyId, setFamilyId] = useState(
    FAMILIES.some((f) => f.id === initialFamily) ? initialFamily : 'cubic'
  );
  const [viewMode, setViewMode] = useState('simulation'); // 'atlas' | 'simulation'
  const [showTangent, setShowTangent] = useState(true);
  const [selectedCalcId, setSelectedCalcId] = useState('turning_points');

  // Parameter states
  const [a, setA] = useState(1);
  const [b, setB] = useState(-3);
  const [c, setC] = useState(0);
  const [d, setD] = useState(2);
  const [p, setP] = useState(1);
  const [q, setQ] = useState(-4);
  const [bBase, setBBase] = useState(2);
  const [mSlope, setMSlope] = useState(1.5);
  const [x0, setX0] = useState(1.5);

  const selectFamily = (id) => {
    setFamilyId(id);
    const fam = FAMILIES.find((f) => f.id === id) || FAMILIES[0];
    const def = fam.defaults;
    if (def.a !== undefined) setA(def.a);
    if (def.b !== undefined) setB(def.b);
    if (def.c !== undefined) setC(def.c);
    if (def.d !== undefined) setD(def.d);
    if (def.p !== undefined) setP(def.p);
    if (def.q !== undefined) setQ(def.q);
    if (def.bBase !== undefined) setBBase(def.bBase);
    if (def.m !== undefined) setMSlope(def.m);
    if (def.x0 !== undefined) setX0(def.x0);
  };

  const resetDefaults = () => selectFamily(familyId);

  // Evaluate f(x), f'(x), f''(x)
  const evalFn = useMemo(() => {
    if (familyId === 'cubic') {
      const f = (x) => a * x * x * x + b * x * x + c * x + d;
      const df = (x) => 3 * a * x * x + 2 * b * x + c;
      const d2f = (x) => 6 * a * x + 2 * b;
      return { f, df, d2f };
    }
    if (familyId === 'quadratic') {
      const f = (x) => a * (x - p) * (x - p) + q;
      const df = (x) => 2 * a * (x - p);
      const d2f = () => 2 * a;
      return { f, df, d2f };
    }
    if (familyId === 'hyperbola') {
      const f = (x) => (Math.abs(x - p) < 0.03 ? NaN : a / (x - p) + q);
      const df = (x) => (Math.abs(x - p) < 0.03 ? NaN : -a / ((x - p) * (x - p)));
      const d2f = (x) => (Math.abs(x - p) < 0.03 ? NaN : (2 * a) / Math.pow(x - p, 3));
      return { f, df, d2f };
    }
    if (familyId === 'exponential') {
      const safeBase = Math.max(0.25, bBase);
      const lnB = Math.log(safeBase);
      const f = (x) => a * Math.pow(safeBase, x - p) + q;
      const df = (x) => a * lnB * Math.pow(safeBase, x - p);
      const d2f = (x) => a * lnB * lnB * Math.pow(safeBase, x - p);
      return { f, df, d2f };
    }
    // linear
    const f = (x) => mSlope * x + c;
    const df = () => mSlope;
    const d2f = () => 0;
    return { f, df, d2f };
  }, [familyId, a, b, c, d, p, q, bBase, mSlope]);

  // Compute critical landmarks (intercepts, stationary points, inflection, asymptotes)
  const landmarks = useMemo(() => {
    const { f, df, d2f } = evalFn;
    const yInt = f(0);
    const stationaryPts = [];
    const inflectionPts = [];
    const roots = [];
    const asymptotes = { vertical: null, horizontal: null };

    if (familyId === 'cubic') {
      if (Math.abs(a) > 0.01) {
        // Stationary points: 3ax^2 + 2bx + c = 0
        const disc = 4 * b * b - 12 * a * c;
        if (disc >= 0) {
          const s1 = (-2 * b - Math.sqrt(disc)) / (6 * a);
          const s2 = (-2 * b + Math.sqrt(disc)) / (6 * a);
          stationaryPts.push({ x: s1, y: f(s1), kind: d2f(s1) < 0 ? 'Local Max' : 'Local Min' });
          if (disc > 0.0001) {
            stationaryPts.push({ x: s2, y: f(s2), kind: d2f(s2) < 0 ? 'Local Max' : 'Local Min' });
          }
        }
        // Inflection: 6ax + 2b = 0 => x = -b / (3a)
        const xInf = -b / (3 * a);
        inflectionPts.push({ x: xInf, y: f(xInf) });
      }
    } else if (familyId === 'quadratic') {
      stationaryPts.push({
        x: p,
        y: q,
        kind: a > 0 ? 'Minimum Turning Point' : 'Maximum Turning Point',
      });
      if (a !== 0 && -q / a >= 0) {
        const dx = Math.sqrt(-q / a);
        roots.push({ x: p - dx, y: 0 });
        if (dx > 0.001) roots.push({ x: p + dx, y: 0 });
      }
    } else if (familyId === 'hyperbola') {
      asymptotes.vertical = p;
      asymptotes.horizontal = q;
      if (Math.abs(q) > 0.01) {
        const xr = p - a / q;
        roots.push({ x: xr, y: 0 });
      }
    } else if (familyId === 'exponential') {
      asymptotes.horizontal = q;
      const safeBase = Math.max(0.25, bBase);
      if (a !== 0 && -q / a > 0 && Math.abs(safeBase - 1) > 0.01) {
        const xr = p + Math.log(-q / a) / Math.log(safeBase);
        roots.push({ x: xr, y: 0 });
      }
    } else if (familyId === 'linear') {
      if (Math.abs(mSlope) > 0.01) {
        roots.push({ x: -c / mSlope, y: 0 });
      }
    }

    // Numeric root scan for cubic if roots array empty
    if (familyId === 'cubic') {
      let prevX = -6;
      let prevY = f(prevX);
      for (let x = -5.95; x <= 6.0; x += 0.05) {
        const curY = f(x);
        if (prevY * curY <= 0 && Number.isFinite(prevY) && Number.isFinite(curY)) {
          const rX = prevX - (prevY * (x - prevX)) / (curY - prevY || 1);
          if (!roots.some((r) => Math.abs(r.x - rX) < 0.12)) {
            roots.push({ x: rX, y: 0 });
          }
        }
        prevX = x;
        prevY = curY;
      }
    }

    const y0 = f(x0);
    const mTan = df(x0);
    const conc0 = d2f(x0);

    return {
      yInt,
      stationaryPts,
      inflectionPts,
      roots,
      asymptotes,
      y0,
      mTan,
      conc0,
    };
  }, [evalFn, familyId, a, b, c, p, q, bBase, mSlope, x0]);

  // Build Calculations Map for CalculationPopoverCard
  const calculationsMap = useMemo(() => {
    const { yInt, stationaryPts, inflectionPts, asymptotes, y0, mTan } = landmarks;

    if (familyId === 'cubic') {
      const xInf = Math.abs(a) > 0.01 ? -b / (3 * a) : 0;
      const yInf = evalFn.f(xInf);
      const tpSummary =
        stationaryPts.length > 0
          ? stationaryPts.map((pt) => `(${fmtSa(pt.x, 2)};\\, ${fmtSa(pt.y, 2)})`).join(',\\; ')
          : '\\text{No real stationary points } (\\Delta < 0)';

      return {
        turning_points: {
          id: 'turning_points',
          shortLabel: "Turning Points f'(x)=0",
          label: 'Stationary Turning Points (First Derivative Test)',
          color: '#2B5B84',
          badgeText: `${stationaryPts.length} TP(s)`,
          formula: "f'(x) = 3ax^2 + 2bx + c = 0",
          substitution: `3(${fmtSa(a)})x^2 + 2(${fmtSa(b)})x + (${fmtSa(c)}) = 0`,
          result: tpSummary,
          meaning:
            'Changing coefficients a, b, and c shifts the discriminant Δ = 4b² − 12ac. When Δ > 0, the cubic has two distinct turning points (a local maximum and a local minimum).',
        },
        inflection_point: {
          id: 'inflection_point',
          shortLabel: "Inflection f''(x)=0",
          label: 'Point of Inflection & Concavity Switch',
          color: '#D97706',
          badgeText: `x = ${fmtPlain(xInf, 2)}`,
          formula: "f''(x) = 6ax + 2b = 0 \\implies x = -\\frac{b}{3a}",
          substitution: `x_{\\text{inf}} = -\\frac{${fmtSa(b)}}{3(${fmtSa(a)})} = ${fmtSa(xInf, 2)}`,
          result: `I\\left(${fmtSa(xInf, 2)};\\, ${fmtSa(yInf, 2)}\\right)`,
          meaning:
            'The point of inflection lies dead-center halfway between the two stationary turning points and marks where concavity switches between concave up (f″ > 0) and concave down (f″ < 0).',
        },
        tangent_line: {
          id: 'tangent_line',
          shortLabel: `Tangent at x₀=${fmtPlain(x0, 1)}`,
          label: `Instantaneous Gradient & Tangent at x₀ = ${fmtPlain(x0, 2)}`,
          color: '#2D6A4F',
          badgeText: `m = ${fmtPlain(mTan, 2)}`,
          formula: "m_{\\text{tan}} = f'(x_0), \\quad y - f(x_0) = m_{\\text{tan}}(x - x_0)",
          substitution: `f'(${fmtSa(x0, 2)}) = 3(${fmtSa(a)})(${fmtSa(x0, 2)})^2 + 2(${fmtSa(b)})(${fmtSa(x0, 2)}) + (${fmtSa(c)})`,
          result: `m_{\\text{tan}} = ${fmtSa(mTan, 2)} \\text{ at } (${fmtSa(x0, 2)};\\, ${fmtSa(y0, 2)})`,
          meaning:
            'Scrubbing x₀ slides the point of tangency along the curve. Notice how m_tan = 0 at the turning points and reaches an extreme slope at the point of inflection.',
        },
      };
    }

    if (familyId === 'quadratic') {
      return {
        turning_points: {
          id: 'turning_points',
          shortLabel: 'Turning Point (p; q)',
          label: 'Parabola Turning Point & Axis of Symmetry',
          color: '#2B5B84',
          badgeText: `TP(${fmtPlain(p, 1)}; ${fmtPlain(q, 1)})`,
          formula: 'f(x) = a(x - p)^2 + q \\implies \\text{TP} = (p;\\, q), \\; x = p',
          substitution: `f(x) = ${fmtSa(a)}(x - (${fmtSa(p)}))^2 + (${fmtSa(q)})`,
          result: `\\text{TP}\\left(${fmtSa(p)};\\, ${fmtSa(q)}\\right), \\quad y\\text{-int} = (0;\\, ${fmtSa(yInt)})`,
          meaning:
            'Coefficient a controls vertical stretch and concavity (a > 0 happy/minimum; a < 0 sad/maximum), p shifts the axis of symmetry horizontally, and q shifts the vertex vertically.',
        },
        tangent_line: {
          id: 'tangent_line',
          shortLabel: `Tangent at x₀=${fmtPlain(x0, 1)}`,
          label: `First Derivative Gradient at x₀ = ${fmtPlain(x0, 2)}`,
          color: '#2D6A4F',
          badgeText: `m = ${fmtPlain(mTan, 2)}`,
          formula: "f'(x_0) = 2a(x_0 - p)",
          substitution: `f'(${fmtSa(x0)}) = 2(${fmtSa(a)})(${fmtSa(x0)} - (${fmtSa(p)}))`,
          result: `m_{\\text{tan}} = ${fmtSa(mTan, 2)}`,
          meaning: 'At x₀ = p, the gradient is zero (horizontal tangent at the vertex).',
        },
      };
    }

    if (familyId === 'hyperbola') {
      return {
        turning_points: {
          id: 'turning_points',
          shortLabel: 'Asymptotes & Symmetry',
          label: 'Hyperbolic Asymptotes & Axes of Symmetry',
          color: '#2B5B84',
          badgeText: `x=${fmtPlain(asymptotes.vertical, 1)}, y=${fmtPlain(asymptotes.horizontal, 1)}`,
          formula: 'x = p \\text{ (Vertical Asymptote)}, \\quad y = q \\text{ (Horizontal Asymptote)}',
          substitution: `f(x) = \\frac{${fmtSa(a)}}{x - (${fmtSa(p)})} + (${fmtSa(q)})`,
          result: `x = ${fmtSa(p)}, \\quad y = ${fmtSa(q)}`,
          meaning:
            'Sign of a determines occupied quadrants relative to (p; q): a > 0 places branches in Quadrants I & III; a < 0 places branches in Quadrants II & IV.',
        },
        tangent_line: {
          id: 'tangent_line',
          shortLabel: 'Axes of Symmetry',
          label: '45° Axes of Symmetry Intersection at (p; q)',
          color: '#D97706',
          badgeText: `Centre (${fmtPlain(p, 1)}; ${fmtPlain(q, 1)})`,
          formula: 'y = (x - p) + q \\quad \\text{and} \\quad y = -(x - p) + q',
          substitution: `y = x - (${fmtSa(p)}) + (${fmtSa(q)})`,
          result: `y = x + ${fmtSa(q - p)} \\; \\text{\\&} \\; y = -x + ${fmtSa(p + q)}`,
          meaning: 'Both axes of symmetry intersect at the asymptote crossover point (p; q) with gradients +1 and −1.',
        },
      };
    }

    if (familyId === 'exponential') {
      return {
        turning_points: {
          id: 'turning_points',
          shortLabel: 'Horizontal Asymptote & Growth',
          label: 'Exponential Growth/Decay & Horizontal Asymptote',
          color: '#2B5B84',
          badgeText: `y = ${fmtPlain(q, 1)}`,
          formula: 'f(x) = a \\cdot b^{x - p} + q, \\quad \\text{Asymptote: } y = q',
          substitution: `f(0) = ${fmtSa(a)} \\cdot (${fmtSa(bBase)})^{0 - (${fmtSa(p)})} + (${fmtSa(q)})`,
          result: `y = ${fmtSa(q)}, \\quad y\\text{-int} = (0;\\, ${fmtSa(yInt, 2)})`,
          meaning:
            'When base b > 1 the curve grows exponentially; when 0 < b < 1 it decays. Parameter q shifts the horizontal asymptote vertically.',
        },
      };
    }

    return {
      turning_points: {
        id: 'turning_points',
        shortLabel: 'Gradient & Intercepts',
        label: 'Linear Gradient m and Intercepts',
        color: '#2B5B84',
        badgeText: `m = ${fmtPlain(mSlope, 2)}`,
        formula: 'f(x) = mx + c, \\quad x\\text{-int} = -\\frac{c}{m}, \\quad y\\text{-int} = c',
        substitution: `f(x) = ${fmtSa(mSlope)}x + (${fmtSa(c)})`,
        result: `m = ${fmtSa(mSlope)}, \\quad (0;\\, ${fmtSa(c)})`,
        meaning: 'Gradient m controls the steepness and direction of the line, while c sets the vertical y-intercept.',
      },
    };
  }, [landmarks, familyId, a, b, c, p, q, bBase, mSlope, x0, evalFn]);

  const activeCalc = calculationsMap[selectedCalcId] || Object.values(calculationsMap)[0];

  // SVG Coordinate Transform: x in [-6, 6], y in [-8, 8] -> 600 x 360
  const W = 600;
  const H = 360;
  const xMin = -6;
  const xMax = 6;
  const yMin = -8;
  const yMax = 8;
  const toSvgX = (x) => ((x - xMin) / (xMax - xMin)) * W;
  const toSvgY = (y) => H - ((y - yMin) / (yMax - yMin)) * H;

  // Generate SVG path segments for the curve
  const curvePaths = useMemo(() => {
    const segments = [];
    let current = [];
    for (let x = xMin; x <= xMax; x += 0.04) {
      if (familyId === 'hyperbola' && Math.abs(x - p) < 0.08) {
        if (current.length > 1) segments.push(current);
        current = [];
        continue;
      }
      const y = evalFn.f(x);
      if (!Number.isFinite(y) || y < yMin - 6 || y > yMax + 6) {
        if (current.length > 1) segments.push(current);
        current = [];
        continue;
      }
      current.push(`${current.length === 0 ? 'M' : 'L'} ${toSvgX(x).toFixed(1)} ${toSvgY(y).toFixed(1)}`);
    }
    if (current.length > 1) segments.push(current);
    return segments.map((seg) => seg.join(' '));
  }, [evalFn, familyId, p]);

  const currentFamilyMeta = FAMILIES.find((f) => f.id === familyId) || FAMILIES[0];

  return (
    <div
      data-testid="polynomial-functions-atlas-aid"
      className="space-y-3.5 text-slate-800 font-sans"
    >
      {/* Top Header & Family Selector */}
      <div className="bg-[#FAF8F3] rounded-xl border border-[#EAE5DC] p-3.5 shadow-2xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-indigo-100 text-indigo-900 uppercase tracking-wider">
              {currentFamilyMeta.grades} • Dual-Capacity Explorer
            </span>
            <h4 className="text-sm font-bold text-[#1E2022] mt-1 flex items-center gap-2">
              <span>Cartesian Functions & Polynomial Coefficient Lab</span>
              <span className="text-xs font-normal text-slate-600">
                (<MathText text={`$${currentFamilyMeta.formulaLatex}$`} />)
              </span>
            </h4>
          </div>

          {/* Mode Toggle: Annotated Master Atlas vs. Live Coefficient Simulation */}
          <div className="flex items-center gap-1.5 bg-white p-1 rounded-lg border border-[#EAE5DC]">
            <button
              type="button"
              data-testid="btn-poly-mode-atlas"
              onClick={() => setViewMode('atlas')}
              className={`px-2.5 py-1 rounded-md text-xs font-bold flex items-center gap-1 transition cursor-pointer ${
                viewMode === 'atlas'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Annotated Atlas</span>
            </button>
            <button
              type="button"
              data-testid="btn-poly-mode-simulation"
              onClick={() => setViewMode('simulation')}
              className={`px-2.5 py-1 rounded-md text-xs font-bold flex items-center gap-1 transition cursor-pointer ${
                viewMode === 'simulation'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              <Sliders className="w-3.5 h-3.5" />
              <span>Live Coefficient Sliders</span>
            </button>
          </div>
        </div>

        {/* Function Family Tabs */}
        <div className="flex flex-wrap items-center gap-1.5 pt-1 border-t border-[#EAE5DC]">
          {FAMILIES.map((fam) => (
            <button
              key={fam.id}
              type="button"
              data-testid={`btn-family-${fam.id}`}
              onClick={() => selectFamily(fam.id)}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition cursor-pointer border ${
                familyId === fam.id
                  ? 'bg-[#2B5B84] text-white border-[#2B5B84]'
                  : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
              }`}
            >
              {fam.label}
            </button>
          ))}
          <button
            type="button"
            data-testid="btn-reset-poly-params"
            onClick={resetDefaults}
            className="ml-auto px-2 py-1 rounded-lg text-[11px] font-semibold bg-white border border-slate-200 text-slate-600 hover:bg-slate-100 flex items-center gap-1 cursor-pointer"
            title="Reset coefficients to canonical defaults"
          >
            <RotateCcw className="w-3 h-3" />
            <span>Reset</span>
          </button>
        </div>

        {/* Live Coefficient Sliders (Visible in Live Simulation mode) */}
        {viewMode === 'simulation' && (
          <div
            data-testid="polynomial-coefficient-sliders"
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5 bg-white p-3 rounded-xl border border-[#EAE5DC]"
          >
            {familyId === 'cubic' && (
              <>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Leading Coeff (a)</span>
                    <span className="font-mono font-bold text-[#13519C]">a = {fmtPlain(a, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-a"
                    min="-2.0"
                    max="2.0"
                    step="0.2"
                    value={a}
                    onChange={(e) => setA(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Quadratic Coeff (b)</span>
                    <span className="font-mono font-bold text-[#13519C]">b = {fmtPlain(b, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-b"
                    min="-5.0"
                    max="5.0"
                    step="0.5"
                    value={b}
                    onChange={(e) => setB(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Linear Coeff (c)</span>
                    <span className="font-mono font-bold text-[#13519C]">c = {fmtPlain(c, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-c"
                    min="-5.0"
                    max="5.0"
                    step="0.5"
                    value={c}
                    onChange={(e) => setC(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Constant y-Int (d)</span>
                    <span className="font-mono font-bold text-[#13519C]">d = {fmtPlain(d, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-d"
                    min="-5.0"
                    max="5.0"
                    step="0.5"
                    value={d}
                    onChange={(e) => setD(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
              </>
            )}

            {(familyId === 'quadratic' || familyId === 'hyperbola' || familyId === 'exponential') && (
              <>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Stretch / Sign (a)</span>
                    <span className="font-mono font-bold text-[#13519C]">a = {fmtPlain(a, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-a"
                    min="-3.0"
                    max="3.0"
                    step="0.5"
                    value={a}
                    onChange={(e) => setA(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
                {familyId === 'exponential' && (
                  <label className="flex flex-col gap-1 text-xs">
                    <div className="flex justify-between font-semibold text-slate-700">
                      <span>Base (b &gt; 0)</span>
                      <span className="font-mono font-bold text-[#13519C]">b = {fmtPlain(bBase, 1)}</span>
                    </div>
                    <input
                      type="range"
                      data-testid="slider-coeff-base"
                      min="0.5"
                      max="3.0"
                      step="0.25"
                      value={bBase}
                      onChange={(e) => setBBase(parseFloat(e.target.value))}
                      className="w-full accent-[#13519C] cursor-pointer h-1.5"
                    />
                  </label>
                )}
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Horizontal Shift (p)</span>
                    <span className="font-mono font-bold text-[#13519C]">p = {fmtPlain(p, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-p"
                    min="-4.0"
                    max="4.0"
                    step="0.5"
                    value={p}
                    onChange={(e) => setP(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Vertical Shift (q)</span>
                    <span className="font-mono font-bold text-[#13519C]">q = {fmtPlain(q, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-q"
                    min="-5.0"
                    max="5.0"
                    step="0.5"
                    value={q}
                    onChange={(e) => setQ(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
              </>
            )}

            {familyId === 'linear' && (
              <>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>Gradient (m)</span>
                    <span className="font-mono font-bold text-[#13519C]">m = {fmtPlain(mSlope, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-m"
                    min="-3.0"
                    max="3.0"
                    step="0.25"
                    value={mSlope}
                    onChange={(e) => setMSlope(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
                <label className="flex flex-col gap-1 text-xs">
                  <div className="flex justify-between font-semibold text-slate-700">
                    <span>y-Intercept (c)</span>
                    <span className="font-mono font-bold text-[#13519C]">c = {fmtPlain(c, 1)}</span>
                  </div>
                  <input
                    type="range"
                    data-testid="slider-coeff-c"
                    min="-5.0"
                    max="5.0"
                    step="0.5"
                    value={c}
                    onChange={(e) => setC(parseFloat(e.target.value))}
                    className="w-full accent-[#13519C] cursor-pointer h-1.5"
                  />
                </label>
              </>
            )}

            {/* Derivative Tangent Scrubber x0 */}
            <label className="flex flex-col gap-1 text-xs sm:col-span-2 lg:col-span-2 bg-emerald-50/70 p-2 rounded-lg border border-emerald-200">
              <div className="flex items-center justify-between font-semibold text-emerald-950">
                <span className="flex items-center gap-1">
                  <TrendingUp className="w-3.5 h-3.5 text-emerald-700" />
                  <span>Tangent Point Scrubber (x₀)</span>
                </span>
                <span className="font-mono font-bold text-emerald-800">
                  x₀ = {fmtPlain(x0, 2)} → f&apos;(x₀) = {fmtPlain(landmarks.mTan, 2)}
                </span>
              </div>
              <input
                type="range"
                data-testid="slider-tangent-x0"
                min="-4.5"
                max="4.5"
                step="0.1"
                value={x0}
                onChange={(e) => setX0(parseFloat(e.target.value))}
                className="w-full accent-emerald-700 cursor-pointer h-1.5"
              />
            </label>
          </div>
        )}
      </div>

      {/* Interactive Cartesian SVG Plot */}
      <div className="bg-white rounded-xl border border-[#EAE5DC] shadow-xs overflow-hidden">
        <div className="px-3.5 py-2 bg-[#FAF8F3] border-b border-[#EAE5DC] flex flex-wrap items-center justify-between gap-2 text-xs">
          <span className="font-bold text-[#1E2022] flex items-center gap-1.5">
            <Crosshair className="w-3.5 h-3.5 text-[#13519C]" />
            <span>
              {viewMode === 'atlas'
                ? 'Master Reference Atlas: Intercepts, Stationary Points & Asymptotes'
                : 'Live Coordinate Plane (Real-Time Root & Turning Point Drift)'}
            </span>
          </span>
          <label className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-700 cursor-pointer">
            <input
              type="checkbox"
              checked={showTangent}
              onChange={(e) => setShowTangent(e.target.checked)}
              className="accent-emerald-700 rounded"
            />
            <span>Show Derivative Tangent Line</span>
          </label>
        </div>

        <svg
          viewBox={`0 0 ${W} ${H}`}
          data-testid="polynomial-cartesian-svg"
          className="w-full h-auto bg-white select-none"
        >
          {/* Coordinate Grid Lines */}
          {Array.from({ length: 13 }, (_, i) => xMin + i).map((gx) => (
            <g key={`gx-${gx}`}>
              <line
                x1={toSvgX(gx)}
                y1={0}
                x2={toSvgX(gx)}
                y2={H}
                stroke={gx === 0 ? '#1E2022' : '#F1F5F9'}
                strokeWidth={gx === 0 ? 1.8 : 1}
              />
              {gx !== 0 && gx % 2 === 0 && (
                <text
                  x={toSvgX(gx)}
                  y={toSvgY(0) + 14}
                  textAnchor="middle"
                  fontSize="10"
                  fill="#64748B"
                  fontFamily="monospace"
                >
                  {gx}
                </text>
              )}
            </g>
          ))}
          {Array.from({ length: 9 }, (_, i) => yMin + i * 2).map((gy) => (
            <g key={`gy-${gy}`}>
              <line
                x1={0}
                y1={toSvgY(gy)}
                x2={W}
                y2={toSvgY(gy)}
                stroke={gy === 0 ? '#1E2022' : '#F1F5F9'}
                strokeWidth={gy === 0 ? 1.8 : 1}
              />
              {gy !== 0 && (
                <text
                  x={toSvgX(0) - 8}
                  y={toSvgY(gy) + 3}
                  textAnchor="end"
                  fontSize="10"
                  fill="#64748B"
                  fontFamily="monospace"
                >
                  {gy}
                </text>
              )}
            </g>
          ))}

          {/* Axis Labels */}
          <text x={W - 14} y={toSvgY(0) - 6} fontSize="11" fontWeight="bold" fill="#1E2022">
            x
          </text>
          <text x={toSvgX(0) + 10} y={16} fontSize="11" fontWeight="bold" fill="#1E2022">
            y
          </text>

          {/* Asymptotes (Dashed Red/Amber) */}
          {landmarks.asymptotes.vertical !== null && (
            <g data-testid="asymptote-vertical">
              <line
                x1={toSvgX(landmarks.asymptotes.vertical)}
                y1={0}
                x2={toSvgX(landmarks.asymptotes.vertical)}
                y2={H}
                stroke="#DC2626"
                strokeWidth="1.8"
                strokeDasharray="6 4"
              />
              <text
                x={toSvgX(landmarks.asymptotes.vertical) + 6}
                y={26}
                fontSize="10"
                fontWeight="bold"
                fill="#DC2626"
                fontFamily="monospace"
              >
                x = {fmtPlain(landmarks.asymptotes.vertical, 1)}
              </text>
            </g>
          )}
          {landmarks.asymptotes.horizontal !== null && (
            <g data-testid="asymptote-horizontal">
              <line
                x1={0}
                y1={toSvgY(landmarks.asymptotes.horizontal)}
                x2={W}
                y2={toSvgY(landmarks.asymptotes.horizontal)}
                stroke="#DC2626"
                strokeWidth="1.8"
                strokeDasharray="6 4"
              />
              <text
                x={W - 70}
                y={toSvgY(landmarks.asymptotes.horizontal) - 6}
                fontSize="10"
                fontWeight="bold"
                fill="#DC2626"
                fontFamily="monospace"
              >
                y = {fmtPlain(landmarks.asymptotes.horizontal, 1)}
              </text>
            </g>
          )}

          {/* Quadratic Axis of Symmetry */}
          {familyId === 'quadratic' && (
            <line
              x1={toSvgX(p)}
              y1={0}
              x2={toSvgX(p)}
              y2={H}
              stroke="#6366F1"
              strokeWidth="1.4"
              strokeDasharray="4 4"
            />
          )}

          {/* Main Function Curve */}
          {curvePaths.map((dPath, idx) => (
            <path
              key={`curve-${idx}`}
              d={dPath}
              fill="none"
              stroke="#13519C"
              strokeWidth="2.8"
              strokeLinecap="round"
            />
          ))}

          {/* Live Tangent Line at x0 */}
          {showTangent && Number.isFinite(landmarks.y0) && Number.isFinite(landmarks.mTan) && (
            <g data-testid="tangent-line-group">
              <line
                x1={toSvgX(x0 - 2.2)}
                y1={toSvgY(landmarks.y0 - landmarks.mTan * 2.2)}
                x2={toSvgX(x0 + 2.2)}
                y2={toSvgY(landmarks.y0 + landmarks.mTan * 2.2)}
                stroke="#059669"
                strokeWidth="2"
                strokeDasharray="5 3"
              />
              <circle
                cx={toSvgX(x0)}
                cy={toSvgY(landmarks.y0)}
                r="5.5"
                fill="#059669"
                stroke="#FFFFFF"
                strokeWidth="1.5"
              />
              <rect
                x={Math.min(W - 145, Math.max(8, toSvgX(x0) + 8))}
                y={Math.min(H - 32, Math.max(8, toSvgY(landmarks.y0) - 26))}
                width="135"
                height="20"
                rx="4"
                fill="#ECFDF5"
                stroke="#10B981"
              />
              <text
                x={Math.min(W - 145, Math.max(8, toSvgX(x0) + 8)) + 6}
                y={Math.min(H - 32, Math.max(8, toSvgY(landmarks.y0) - 26)) + 14}
                fontSize="10"
                fontWeight="bold"
                fill="#065F46"
                fontFamily="monospace"
              >
                m = f&apos;({fmtPlain(x0, 1)}) = {fmtPlain(landmarks.mTan, 2)}
              </text>
            </g>
          )}

          {/* Roots (x-intercepts) */}
          {landmarks.roots.map((rt, i) => (
            <g key={`root-${i}`}>
              <circle
                cx={toSvgX(rt.x)}
                cy={toSvgY(0)}
                r="4.5"
                fill="#0284C7"
                stroke="#FFFFFF"
                strokeWidth="1.5"
              />
              <text
                x={toSvgX(rt.x)}
                y={toSvgY(0) - 8}
                textAnchor="middle"
                fontSize="9.5"
                fontWeight="bold"
                fill="#0369A1"
                fontFamily="monospace"
              >
                ({fmtPlain(rt.x, 1)}; 0)
              </text>
            </g>
          ))}

          {/* Stationary Turning Points */}
          {landmarks.stationaryPts.map((tp, i) => (
            <g key={`tp-${i}`} data-testid={`landmark-tp-${i}`}>
              <circle
                cx={toSvgX(tp.x)}
                cy={toSvgY(tp.y)}
                r="6"
                fill="#D97706"
                stroke="#FFFFFF"
                strokeWidth="1.5"
              />
              <text
                x={toSvgX(tp.x)}
                y={toSvgY(tp.y) + (tp.y >= 0 ? -10 : 16)}
                textAnchor="middle"
                fontSize="10"
                fontWeight="bold"
                fill="#B45309"
                fontFamily="monospace"
              >
                TP({fmtPlain(tp.x, 1)}; {fmtPlain(tp.y, 1)})
              </text>
            </g>
          ))}

          {/* Inflection Point */}
          {landmarks.inflectionPts.map((inf, i) => (
            <g key={`inf-${i}`} data-testid="landmark-inflection">
              <circle
                cx={toSvgX(inf.x)}
                cy={toSvgY(inf.y)}
                r="5.5"
                fill="#7C3AED"
                stroke="#FFFFFF"
                strokeWidth="1.5"
              />
              <text
                x={toSvgX(inf.x) + 8}
                y={toSvgY(inf.y) + 4}
                fontSize="10"
                fontWeight="bold"
                fill="#6D28D9"
                fontFamily="monospace"
              >
                Inf({fmtPlain(inf.x, 1)}; {fmtPlain(inf.y, 1)})
              </text>
            </g>
          ))}
        </svg>
      </div>

      {/* Live Formula & Substitution Breakdown Card */}
      <CalculationPopoverCard
        calculation={activeCalc}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedCalcId}
      />
    </div>
  );
}
