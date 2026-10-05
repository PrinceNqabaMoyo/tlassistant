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

### Deployment & Hosting

#### Frontend Deployment (Firebase Hosting)
To build and deploy the production bundle to Firebase Hosting:
```bash
npm run build
npx firebase deploy --only hosting
```

> **Important Note (Firebase Hosting Post-Oct 15, 2026):**  
> For the existing production project (`caps-ai-math-assistant-app` / `fundile.com`), the hosting site is already provisioned and active.  
> However, if provisioning a **brand-new Firebase project** or fresh staging environment in the future, Firebase will require on-demand site creation before running `firebase deploy` for the first time:
> ```bash
> firebase hosting:sites:create <site-id> --project=<project-id>
> ```
> *(Or click "Get Started" under **Build > Hosting** in the Firebase Console prior to your first CLI deployment).*

#### Backend Deployment (Hugging Face Space)
The Python backend runs in a Dockerized environment on Hugging Face Spaces (`snombi/tlassistant`). Deploy updates via:
```bash
python caps-ai-backend/deploy_hf.py
```

#### Automated Hourly Check, GitHub Sync & Dual Redeployment
Fundile maintains an automated pipeline that checks for codebase updates every hour, pushes verified changes to GitHub, and triggers production redeployments across both frontend (Firebase Hosting) and backend (Hugging Face Spaces):

- **Single Check & Deploy Run:**
  ```bash
  python scripts/hourly_sync_deploy.py --once
  # or via npm:
  npm run sync:hourly
  ```

- **Continuous Local Background Daemon (Runs Every Hour):**
  ```bash
  python scripts/hourly_sync_deploy.py --daemon --interval 3600
  # or via npm:
  npm run sync:daemon
  ```

- **Dry-Run Inspection (Simulate Without Deploying):**
  ```bash
  python scripts/hourly_sync_deploy.py --dry-run
  ```

- **Automated CI/CD via GitHub Actions:**
  A scheduled cron workflow is configured at `.github/workflows/hourly_sync_deploy.yml` which executes automatically every hour on GitHub (`0 * * * *`).

- **AI Agent Background Automation:**
  In Antigravity, the agent maintains the schedule using the `schedule` tool (`CronExpression="0 * * * *"`, `IsDaemon=true`).

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Development Safety

Before editing `src/App.jsx` (a 2,300+ line file), **always make a manual backup** first (e.g. copy `src/App.jsx` to `src/App.jsx.backup`).
This prevents accidental loss of state if an edit goes wrong.

## Mandatory Specialist Agent Routing Protocol

To maintain architectural integrity and prevent inconsistent implementations, all engineering tasks must strictly route to their designated specialist subagent:

| Domain | Assigned Specialist Subagent | Key Invariants |
| :--- | :--- | :--- |
| **Frontend UI & Mobile Ergonomics** | `cognitive_ui_engineer` | React 18, Vite, mobile touch targets (min 44px), portrait/landscape workspace maximization, skeuo-modern folder tabs, cognitive modalities. |
| **Learner Journey & Pacing** | `learner_ux_specialist` | Student psychology, distraction-free workspaces, emotional safety of looping, 3-tier pacing. |
| **Backend Question Generators** | `generator_architect` + Domain Specialist | 6-pillar contract, SymPy AST purity (CC <= 12), South African comma decimals (`{,}`), 3-tier pre-baked hints. |
| **Quality Assurance & Verification** | `qa_test_architect` | Large-scale Monte Carlo determinism, Vite production builds, responsive viewport testing. |
| **Curriculum Alignment & Pacing** | `curriculum_specialist` | CAPS ground truth, Annual Teaching Plan (ATP) weightings, zero proprietary trademarks. |
| **Architecture Manifest Governance** | `architecture_governor` | `fundile-architecture.json` sync (Rule 0a-0c) and `generate_architecture_html.py`. |

### Agent Creation & Modification Governance
For any task that requires the creation of a **new specialist agent** or the **modification of an existing agent** (its configuration, system prompt, or tooling in `.agents/agents/`), the assistant must **ask the user for explicit permission first** before making changes or registering new agent definitions. Never modify or create agents unilaterally.

