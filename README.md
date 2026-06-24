# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

## Configuration

### Frontend environment

Create `/.env.local` for local frontend configuration.

Use these browser-safe variables:

- `VITE_API_BASE_URL`
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_PUBLISHABLE_KEY`

Template files:

- `/.env.example`
- `/.env.local.example`

Example local frontend configuration:

```env
VITE_API_BASE_URL=http://localhost:5001
VITE_SUPABASE_URL=https://lyytkivhqrrelsucwmie.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=your-publishable-key
```

### Backend environment

Store server-only secrets in `caps-ai-backend/.env`.

Backend variables used for POP uploads:

- `SUPABASE_URL`
- `SUPABASE_SECRET_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `SUPABASE_POP_BUCKET`

Example backend configuration:

```env
SUPABASE_URL=https://lyytkivhqrrelsucwmie.supabase.co
SUPABASE_SECRET_KEY=your-secret-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_POP_BUCKET=proof-of-payment
```

Never place `SUPABASE_SECRET_KEY` or `SUPABASE_SERVICE_ROLE_KEY` in frontend env files.

### Production notes

For production, set `VITE_API_BASE_URL` to your deployed backend URL if the frontend and backend are on different origins.

If the frontend and backend are served from the same origin behind a proxy, the app can fall back to same-origin API calls in production.

The app also supports deploy-time runtime overrides through `public/runtime-config.js`, so `window.__RUNTIME_CONFIG__.VITE_API_BASE_URL` can be used to change the API base URL without rebuilding the frontend.

Keep Supabase bucket secrets on the backend only. The frontend should only ever use browser-safe values such as the publishable key.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Development Safety

Before editing `src/App.jsx` (a 2,300+ line file), **always make a manual backup** first (e.g. copy `src/App.jsx` to `src/App.jsx.backup`).
This prevents accidental loss of state if an edit goes wrong.

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
