import React from 'react';
import JXG from 'jsxgraph';
import { evalFamily, yBoundsFor, isTrigFamily, FAMILY_LABELS } from './functionFamilies';

const { JSXGraph } = JXG;

let _grapherSeq = 0;

const COLORS = {
    curve: '#6366f1',
    target: '#94a3b8',
    correct: '#059669',
    label: '#0f172a',
};

/**
 * FunctionGrapher — the reusable, parametric parameter-manipulation visual aid.
 *
 * Driven entirely by a `function_graph` Diagram Spec with an `interactive`
 * block (`{ sliders: ["a","q"], target: {a,q,b} }`). The learner drags the
 * sliders; the solid curve transforms live while a dashed target curve stays
 * fixed. The current `{a,q,b}` is reported via `onChange` and submitted for
 * deterministic, structural marking (never pixels). Nothing here is
 * grade-specific — any subject that emits the spec gets this identical widget.
 *
 * Props:
 *   spec      the function_graph spec (with `interactive`)
 *   value     current params { a, q, b } (controlled)
 *   onChange  (params) => void
 *   graded    once marked, recolour the curve to show success
 *   disabled  freeze interaction (after submit)
 */
const FunctionGrapher = ({ spec, value, onChange, graded = false, disabled = false }) => {
    const boxRef = React.useRef(null);
    const idRef = React.useRef(`fgrapher-${++_grapherSeq}`);
    const onChangeRef = React.useRef(onChange);
    onChangeRef.current = onChange;

    const family = spec?.family || 'linear';
    const interactive = spec?.interactive || {};
    const sliders = interactive.sliders || ['a', 'q'];
    const target = interactive.target || {};
    const domain = spec?.domain || (isTrigFamily(family) ? [0, 360] : [-5, 5]);

    const current = React.useMemo(() => ({
        a: value?.a ?? 1,
        q: value?.q ?? 0,
        b: value?.b ?? target.b ?? 2,
    }), [value, target.b]);

    // Build the board once; slider movement drives React state via onChange.
    React.useEffect(() => {
        if (!spec || !boxRef.current) return undefined;
        const [xlo, xhi] = domain;
        const tBounds = yBoundsFor(family, domain, target);
        const cBounds = yBoundsFor(family, domain, { a: 0, q: 0, b: current.b });
        const ylo = Math.min(tBounds[0], cBounds[0], -3);
        const yhi = Math.max(tBounds[1], cBounds[1], 3);
        const padX = isTrigFamily(family) ? 20 : 0.8;

        const board = JSXGraph.initBoard(idRef.current, {
            boundingbox: [xlo - padX, yhi, xhi + padX, ylo],
            axis: true,
            grid: true,
            showNavigation: false,
            showCopyright: false,
            keepAspectRatio: false,
            pan: { enabled: false },
            zoom: { enabled: false },
        });

        // Dashed target curve (fixed reference).
        const plotTarget = (xfrom, xto) => board.create(
            'functiongraph',
            [(x) => evalFamily(family, x, target), xfrom, xto],
            { strokeColor: COLORS.target, strokeWidth: 2, dash: 3, fixed: true, highlight: false },
        );
        if (family === 'hyperbola') { plotTarget(xlo, -0.05); plotTarget(0.05, xhi); } else { plotTarget(xlo, xhi); }

        // In-board sliders for the exposed params.
        const sliderRange = (key) => (key === 'a' ? [-4, 4] : [-5, 5]);
        const sliderObjs = {};
        sliders.forEach((key, i) => {
            const yPos = yhi - (i + 1) * (yhi - ylo) * 0.08;
            const x0 = xlo - padX + (xhi - xlo + 2 * padX) * 0.06;
            const x1 = x0 + (xhi - xlo + 2 * padX) * 0.34;
            const [smin, smax] = sliderRange(key);
            sliderObjs[key] = board.create(
                'slider',
                [[x0, yPos], [x1, yPos], [smin, current[key], smax]],
                { name: key, snapWidth: 1, fillColor: COLORS.curve, strokeColor: COLORS.curve, label: { fontSize: 13 } },
            );
        });

        const liveParams = () => {
            const p = { ...current };
            sliders.forEach((key) => { p[key] = Math.round(sliderObjs[key].Value()); });
            return p;
        };

        // Solid learner curve, recomputed from slider values each frame.
        const plotCurve = (xfrom, xto) => board.create(
            'functiongraph',
            [(x) => evalFamily(family, x, liveParams()), xfrom, xto],
            { strokeColor: graded ? COLORS.correct : COLORS.curve, strokeWidth: 3, fixed: true, highlight: false },
        );
        if (family === 'hyperbola') { plotCurve(xlo, -0.05); plotCurve(0.05, xhi); } else { plotCurve(xlo, xhi); }

        if (!disabled) {
            sliders.forEach((key) => {
                sliderObjs[key].on('drag', () => onChangeRef.current && onChangeRef.current(liveParams()));
            });
        } else {
            sliders.forEach((key) => { sliderObjs[key].setAttribute({ fixed: true, frozen: true }); });
        }

        return () => { try { JSXGraph.freeBoard(board); } catch { /* freed */ } };
        // Rebuild only when the question (spec) or graded state changes.
    }, [JSON.stringify(spec), graded, disabled]); // eslint-disable-line react-hooks/exhaustive-deps

    if (!spec) return null;

    return (
        <div className="flex flex-col items-center">
            <div
                id={idRef.current}
                ref={boxRef}
                className="jxgbox rounded-xl border border-slate-200 bg-white"
                style={{ width: 380, height: 340, position: 'relative', overflow: 'hidden', userSelect: 'none' }}
            />
            <div className="mt-2 flex items-center gap-4 text-xs text-slate-500">
                <span className="inline-flex items-center gap-1">
                    <span className="inline-block h-0.5 w-5" style={{ background: COLORS.target, borderTop: `2px dashed ${COLORS.target}` }} />
                    target ({FAMILY_LABELS[family] || family})
                </span>
                <span className="inline-flex items-center gap-1">
                    <span className="inline-block h-0.5 w-5" style={{ background: graded ? COLORS.correct : COLORS.curve }} />
                    your curve
                </span>
            </div>
            <p className="mt-1 font-mono text-xs text-slate-600">
                {sliders.map((k) => `${k} = ${current[k]}`).join('   ')}
            </p>
            {spec.caption ? <p className="mt-1 text-xs text-slate-400">{spec.caption}</p> : null}
        </div>
    );
};

export default FunctionGrapher;
