import React from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

/**
 * MathText — renders a LaTeX string with KaTeX.
 *
 * The backend emits LaTeX using the South-African decimal **comma** convention
 * (e.g. ``0{,}5``), so nothing special is needed here — KaTeX renders it tight.
 *
 * Props:
 *   latex      the LaTeX source
 *   display    block (true) vs inline (false) maths
 *   className   extra classes for the wrapper
 */
const MathText = ({ latex = '', display = false, className = '' }) => {
    const html = React.useMemo(() => {
        try {
            return katex.renderToString(String(latex), {
                throwOnError: false,
                displayMode: display,
                strict: false,
            });
        } catch {
            return String(latex);
        }
    }, [latex, display]);

    return (
        <span
            className={className}
            dangerouslySetInnerHTML={{ __html: html }}
        />
    );
};

export default MathText;
