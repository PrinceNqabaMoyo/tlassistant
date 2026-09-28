import React from 'react';
import { AlertTriangle, RefreshCw, Home } from 'lucide-react';

/**
 * Standard React Error Boundary
 * Catches JavaScript errors anywhere in their child component tree,
 * logs those errors, and displays a fallback UI instead of crashing the app.
 */
export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('🔴 ErrorBoundary caught an unhandled error:', error, errorInfo);
    this.setState({ error, errorInfo });
  }

  handleReset = () => {
    this.setState({ hasError: false, error: null, errorInfo: null });
    if (this.props.onReset) {
      this.props.onReset();
    }
  };

  render() {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback(this.state.error, this.handleReset);
      }

      return (
        <div className="min-h-[320px] w-full p-6 flex flex-col items-center justify-center text-center bg-slate-50 border border-slate-200 rounded-2xl shadow-xs font-sans">
          <div className="w-12 h-12 rounded-2xl bg-amber-100 border border-amber-300 text-amber-800 flex items-center justify-center mb-4 shadow-2xs">
            <AlertTriangle className="w-6 h-6 text-amber-600" />
          </div>
          <h3 className="text-lg font-bold text-slate-900 mb-1" style={{ fontFamily: 'Afacad, sans-serif' }}>
            {this.props.title || 'Something interrupted this workspace'}
          </h3>
          <p className="text-sm text-slate-600 max-w-md mb-4">
            An unexpected error occurred while loading this view. You can reload this component or return to Today's Desk.
          </p>

          {this.state.error && (
            <div className="mb-4 max-w-lg w-full text-left p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-800 text-xs font-mono overflow-x-auto">
              <strong>Error:</strong> {this.state.error.message || String(this.state.error)}
            </div>
          )}

          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={this.handleReset}
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-[#13519C] text-white text-xs font-bold hover:bg-blue-800 transition cursor-pointer shadow-xs"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              Try Again
            </button>
            <button
              type="button"
              onClick={() => window.location.reload()}
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-white border border-slate-300 text-slate-700 text-xs font-bold hover:bg-slate-50 transition cursor-pointer shadow-2xs"
            >
              <Home className="w-3.5 h-3.5" />
              Reload Page
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
