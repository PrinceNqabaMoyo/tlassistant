// Shared evaluator for the function families understood by the grapher.
// Mirrors backend `_diagram.FUNCTION_FAMILIES`. Each family is y = a·f(x) + q
// (with an exponential base b). Reused by the static DiagramRenderer plot and
// the interactive FunctionGrapher so a single source of truth defines the
// curves — shareable across grades' mathematics and Technical Mathematics.

const DEG = Math.PI / 180;

export const FAMILY_LABELS = {
    linear: 'y = ax + q',
    quadratic: 'y = ax² + q',
    hyperbola: 'y = a/x + q',
    exponential: 'y = a·bˣ + q',
    sin: 'y = a·sinθ + q',
    cos: 'y = a·cosθ + q',
    tan: 'y = a·tanθ + q',
};

export function isTrigFamily(family) {
    return family === 'sin' || family === 'cos' || family === 'tan';
}

// Evaluate a family at x for params {a, q, b}. Returns NaN where undefined
// (e.g. hyperbola at x=0) so JSXGraph breaks the curve there.
export function evalFamily(family, x, params = {}) {
    const a = params.a ?? 1;
    const q = params.q ?? 0;
    const b = params.b ?? 2;
    switch (family) {
        case 'linear':
            return a * x + q;
        case 'quadratic':
            return a * x * x + q;
        case 'hyperbola':
            if (Math.abs(x) < 1e-6) return NaN;
            return a / x + q;
        case 'exponential':
            return a * Math.pow(b, x) + q;
        case 'sin':
            return a * Math.sin(x * DEG) + q;
        case 'cos':
            return a * Math.cos(x * DEG) + q;
        case 'tan': {
            const c = Math.cos(x * DEG);
            if (Math.abs(c) < 1e-3) return NaN;
            return a * Math.tan(x * DEG) + q;
        }
        default:
            return NaN;
    }
}

// A sensible y-bounding box for a family/domain so the curve fills the board.
export function yBoundsFor(family, domain, params = {}) {
    if (isTrigFamily(family)) {
        const a = Math.abs(params.a ?? 1);
        const q = params.q ?? 0;
        const amp = Math.max(1, a);
        return [q - amp - 1, q + amp + 1];
    }
    const [lo, hi] = domain || [-5, 5];
    const samples = 80;
    let min = Infinity;
    let max = -Infinity;
    for (let i = 0; i <= samples; i += 1) {
        const x = lo + ((hi - lo) * i) / samples;
        const y = evalFamily(family, x, params);
        if (Number.isFinite(y)) {
            if (y < min) min = y;
            if (y > max) max = y;
        }
    }
    if (!Number.isFinite(min) || !Number.isFinite(max)) return [-6, 6];
    // Clamp very large excursions (hyperbola/exponential) to keep it readable.
    min = Math.max(min, -12);
    max = Math.min(max, 12);
    const padY = Math.max(1, (max - min) * 0.15);
    return [min - padY, max + padY];
}
