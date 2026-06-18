import React, { useRef, useEffect, useState } from 'react';

/**
 * KaTeXRenderer — renders LaTeX math expressions using the KaTeX library
 * loaded via CDN in index.html.
 *
 * @param {string}  latex       - The LaTeX string to render.
 * @param {boolean} displayMode - If true (default), renders in display mode
 *                                (centered, larger). If false, renders inline.
 *
 * Usage:
 *   <KaTeXRenderer latex="\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}" />
 *   <KaTeXRenderer latex="x^2 + y^2 = r^2" displayMode={false} />
 */
function KaTeXRenderer({ latex, displayMode = true }) {
  const containerRef = useRef(null);
  const [katexReady, setKatexReady] = useState(!!window.katex);
  const [error, setError] = useState(null);

  // Poll for window.katex availability (the CDN script uses `defer`)
  useEffect(() => {
    if (window.katex) {
      setKatexReady(true);
      return;
    }

    const interval = setInterval(() => {
      if (window.katex) {
        setKatexReady(true);
        clearInterval(interval);
      }
    }, 100);

    // Stop polling after 10 seconds and show an error
    const timeout = setTimeout(() => {
      clearInterval(interval);
      if (!window.katex) {
        setError('KaTeX library failed to load. Please check your internet connection.');
      }
    }, 10000);

    return () => {
      clearInterval(interval);
      clearTimeout(timeout);
    };
  }, []);

  // Render the LaTeX expression once KaTeX is ready
  useEffect(() => {
    if (!katexReady || !containerRef.current || !latex) return;

    try {
      window.katex.render(latex, containerRef.current, {
        displayMode,
        throwOnError: false,
      });
      setError(null);
    } catch (err) {
      setError(`Failed to render LaTeX: ${err.message}`);
    }
  }, [latex, displayMode, katexReady]);

  // --- Loading state ---
  if (error) {
    return (
      <div
        style={{
          padding: '12px 16px',
          color: '#b91c1c',
          backgroundColor: '#fef2f2',
          border: '1px solid #fecaca',
          borderRadius: '6px',
          fontFamily: 'monospace',
          fontSize: '14px',
        }}
      >
        {error}
      </div>
    );
  }

  if (!katexReady) {
    return (
      <div
        style={{
          padding: '12px 16px',
          color: '#6b7280',
          fontStyle: 'italic',
          fontSize: '14px',
        }}
      >
        Loading math renderer…
      </div>
    );
  }

  // --- Rendered output ---
  return (
    <div
      ref={containerRef}
      style={{
        padding: '12px 16px',
        overflowX: 'auto',
      }}
    />
  );
}

export default KaTeXRenderer;
