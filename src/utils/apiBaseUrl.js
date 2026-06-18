export const getApiBaseUrl = () => {
  // 1. Fallback to local development if running on localhost (Highest priority to override any baked-in env vars)
  if (typeof window !== 'undefined' && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')) {
     return 'http://localhost:5001'; 
  }

  // 2. Check window runtime config (useful if they inject it at runtime, not build time)
  const runtime = typeof window !== 'undefined' ? window.__RUNTIME_CONFIG__?.VITE_API_BASE_URL : undefined;
  if (runtime && String(runtime).trim() && !String(runtime).includes('localhost')) {
    return String(runtime).trim().replace(/\/$/, '');
  }

  // 3. Check Vite Environment Variable (but ignore if it baked in localhost for a production deployment)
  const envVar = typeof import.meta !== 'undefined' ? import.meta.env?.VITE_API_BASE_URL : undefined;
  if (envVar && String(envVar).trim() && !String(envVar).includes('localhost')) {
    return String(envVar).trim().replace(/\/$/, '');
  }

  // 4. Default Fallback to Hugging Face Cloud backend
  return 'https://snombi-tlassistant.hf.space';
};

export const buildApiUrl = (path) => {
  const base = getApiBaseUrl();
  const p = path ? String(path) : '';
  if (!p) return base;
  return `${base}${p.startsWith('/') ? '' : '/'}${p}`;
};
