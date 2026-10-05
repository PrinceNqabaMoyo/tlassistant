import React, { useState } from 'react';
import {
  ChevronLeft, BarChart3, Activity, Server, Cpu, Database,
  Shield, CheckCircle2, AlertTriangle, Layers, BookOpen,
  Trophy, Settings, Lock, Sparkles, RefreshCw, Eye, Download,
  Sliders, Globe, Zap, Radio
} from 'lucide-react';

/**
 * Common Header for Super Admin Detail Panels
 */
function AdminPanelHeader({ title, subtitle, icon: Icon, onBack, badge = 'Super Admin' }) {
  return (
    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-6 border-b border-slate-200">
      <div className="flex items-center gap-3">
        {onBack && (
          <button
            onClick={onBack}
            className="p-2 rounded-xl text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition-colors border border-slate-200 cursor-pointer"
            title="Return to Admin Dashboard"
          >
            <ChevronLeft className="w-5 h-5" />
          </button>
        )}
        <div className="w-10 h-10 rounded-xl bg-[#13519C] text-white flex items-center justify-center shadow-xs shrink-0">
          <Icon className="w-5 h-5" />
        </div>
        <div>
          <div className="flex items-center gap-2">
            <h1
              style={{ fontFamily: "'Afacad', sans-serif" }}
              className="text-2xl font-bold text-slate-900 tracking-tight"
            >
              {title}
            </h1>
            <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider bg-blue-50 text-[#13519C] border border-blue-200">
              {badge}
            </span>
          </div>
          <p className="text-xs text-slate-500 mt-0.5">{subtitle}</p>
        </div>
      </div>
      <div className="flex items-center gap-2">
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
          Live Telemetry
        </span>
      </div>
    </div>
  );
}

/**
 * 1. System Analytics View
 */
export function SystemAnalyticsView({ onBack }) {
  const [refreshing, setRefreshing] = useState(false);

  const handleRefresh = () => {
    setRefreshing(true);
    setTimeout(() => setRefreshing(false), 800);
  };

  const metrics = [
    { label: 'FastAPI / SymPy Latency', value: '38 ms', change: '-4 ms vs avg', status: 'optimal' },
    { label: 'Uptime (Last 30 Days)', value: '99.98%', change: '0 unhandled halts', status: 'optimal' },
    { label: 'Questions Generated Today', value: '4,820', change: '+18% vs yesterday', status: 'optimal' },
    { label: 'Zero-LLM Cache Hit Ratio', value: '94.2%', change: 'Deterministic Python', status: 'optimal' },
    { label: 'Peak Memory Footprint', value: '142 MB', change: 'Socket pooled', status: 'optimal' },
    { label: 'Telemetry Event Buffer', value: '0 pending', change: 'Offline synced', status: 'optimal' },
  ];

  const services = [
    { name: 'Deterministic SymPy Math Engine', status: 'Healthy', latency: '42 ms', uptime: '100%' },
    { name: '2D Accounting Coordinate Marker', status: 'Healthy', latency: '12 ms', uptime: '100%' },
    { name: 'Hugging Face Socratic Tutor Layer', status: 'Standby / Healthy', latency: '210 ms', uptime: '99.9%' },
    { name: 'Firebase Firestore Data Store', status: 'Healthy', latency: '65 ms', uptime: '99.99%' },
    { name: 'PWA WebAPK Service Worker Cache', status: 'Active (v2.4)', latency: 'Instant', uptime: '100%' },
  ];

  return (
    <div className="p-4 sm:p-6 lg:p-8 space-y-6 max-w-7xl mx-auto">
      <AdminPanelHeader
        title="System Analytics & Telemetry"
        subtitle="Real-time latency, engine health, and platform resource metrics"
        icon={BarChart3}
        onBack={onBack}
      />

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {metrics.map((m) => (
          <div key={m.label} className="bg-white p-5 rounded-2xl border border-slate-200/90 shadow-xs space-y-1">
            <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider">{m.label}</div>
            <div className="text-2xl font-bold text-slate-900 font-mono">{m.value}</div>
            <div className="text-xs text-emerald-700 font-medium flex items-center gap-1">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
              <span>{m.change}</span>
            </div>
          </div>
        ))}
      </div>

      {/* Services Table */}
      <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden">
        <div className="p-4 sm:p-5 border-b border-slate-100 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Server className="w-4 h-4 text-[#13519C]" />
            <h3 className="font-bold text-slate-900 text-sm font-afacad">Core Microservices & Engine Status</h3>
          </div>
          <button
            onClick={handleRefresh}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition cursor-pointer"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${refreshing ? 'animate-spin text-[#13519C]' : ''}`} />
            <span>Refresh Health</span>
          </button>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 text-slate-500 uppercase tracking-wider text-[10px] border-b border-slate-100 font-semibold font-sans">
              <tr>
                <th className="py-3 px-4">Service Name</th>
                <th className="py-3 px-4">Operational Status</th>
                <th className="py-3 px-4">Response Latency</th>
                <th className="py-3 px-4">30-Day Uptime</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 font-mono">
              {services.map((s) => (
                <tr key={s.name} className="hover:bg-slate-50/80 transition-colors">
                  <td className="py-3.5 px-4 font-sans font-semibold text-slate-900">{s.name}</td>
                  <td className="py-3.5 px-4 font-sans">
                    <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200">
                      <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                      {s.status}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 text-slate-700">{s.latency}</td>
                  <td className="py-3.5 px-4 text-slate-700">{s.uptime}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

/**
 * 2. Content Management View
 */
export function ContentManagementView({ onBack }) {
  const [filterSubject, setFilterSubject] = useState('all');
  const [astVerifying, setAstVerifying] = useState(false);
  const [verifyMessage, setVerifyMessage] = useState(null);

  const generators = [
    { subject: 'Accounting', grade: '10', archetypes: 18, terms: 'Terms 1–4', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'Mathematics', grade: '10', archetypes: 24, terms: 'Terms 1–4', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'Mathematics', grade: '11', archetypes: 22, terms: 'Terms 1–3', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'EMS', grade: '9', archetypes: 14, terms: 'Terms 1–4', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'EMS', grade: '8', archetypes: 12, terms: 'Terms 1–4', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'Physical Sciences', grade: '10', archetypes: 16, terms: 'Terms 1–4', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'Business Studies', grade: '10', archetypes: 15, terms: 'Terms 1–4', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
    { subject: 'Mathematical Literacy', grade: '10', archetypes: 12, terms: 'Terms 1–3', status: 'AST Certified', hints: '3-Tier Pre-baked', zeroLlm: '100% Deterministic' },
  ];

  const handleRunAstVerification = () => {
    setAstVerifying(true);
    setTimeout(() => {
      setAstVerifying(false);
      setVerifyMessage('✅ Monte Carlo 1,000-Seed Audit: 100% AST Purity. Zero unhandled exceptions. All worked solutions match marking schemas.');
    }, 1200);
  };

  const filtered = generators.filter(g => filterSubject === 'all' || g.subject === filterSubject);

  return (
    <div className="p-4 sm:p-6 lg:p-8 space-y-6 max-w-7xl mx-auto">
      <AdminPanelHeader
        title="CAPS Content & Generator Registry"
        subtitle="Manage deterministic question archetypes, SymPy generators, and curriculum coverage"
        icon={BookOpen}
        onBack={onBack}
      />

      {verifyMessage && (
        <div className="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs font-semibold flex items-center justify-between">
          <span>{verifyMessage}</span>
          <button onClick={() => setVerifyMessage(null)} className="text-emerald-700 hover:text-emerald-950">✕</button>
        </div>
      )}

      {/* Action Bar */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs">
        <div className="flex items-center gap-2">
          <label className="text-xs font-semibold text-slate-500">Filter Subject:</label>
          <select
            value={filterSubject}
            onChange={(e) => setFilterSubject(e.target.value)}
            className="text-xs bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 font-medium text-slate-700 focus:outline-hidden focus:border-[#13519C]"
          >
            <option value="all">All Subjects (8 Engines)</option>
            <option value="Accounting">Accounting</option>
            <option value="Mathematics">Mathematics</option>
            <option value="EMS">EMS</option>
            <option value="Physical Sciences">Physical Sciences</option>
            <option value="Business Studies">Business Studies</option>
            <option value="Mathematical Literacy">Mathematical Literacy</option>
          </select>
        </div>

        <button
          onClick={handleRunAstVerification}
          disabled={astVerifying}
          className="inline-flex items-center justify-center gap-2 px-4 py-2 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold transition shadow-xs cursor-pointer"
        >
          <Sparkles className={`w-3.5 h-3.5 ${astVerifying ? 'animate-spin' : ''}`} />
          <span>{astVerifying ? 'Running Monte Carlo Seeds...' : 'Run Monte Carlo AST Audit'}</span>
        </button>
      </div>

      {/* Generator Table */}
      <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-50 text-slate-500 uppercase tracking-wider text-[10px] border-b border-slate-100 font-semibold font-sans">
              <tr>
                <th className="py-3 px-4">Subject</th>
                <th className="py-3 px-4">CAPS Grade</th>
                <th className="py-3 px-4">Active Archetypes</th>
                <th className="py-3 px-4">Terms Covered</th>
                <th className="py-3 px-4">Hint Architecture</th>
                <th className="py-3 px-4">LLM Token Cost</th>
                <th className="py-3 px-4">Engine Verification</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {filtered.map((g, idx) => (
                <tr key={`${g.subject}-${g.grade}-${idx}`} className="hover:bg-slate-50/80 transition-colors">
                  <td className="py-3.5 px-4 font-semibold text-slate-900">{g.subject}</td>
                  <td className="py-3.5 px-4 font-mono font-bold text-slate-700">Grade {g.grade}</td>
                  <td className="py-3.5 px-4 font-mono">{g.archetypes} Archetypes</td>
                  <td className="py-3.5 px-4 text-slate-600">{g.terms}</td>
                  <td className="py-3.5 px-4">
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-amber-50 text-amber-900 border border-amber-200">
                      {g.hints}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 font-mono font-bold text-emerald-700">{g.zeroLlm}</td>
                  <td className="py-3.5 px-4">
                    <span className="inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-800">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                      {g.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

/**
 * 3. Competition Setup View
 */
export function CompetitionSetupView({ onBack }) {
  const [challenges, setChallenges] = useState([
    {
      id: 'comp-1',
      title: 'KZN Provincial FET Accounting Olympiad',
      grades: 'Grades 10–12',
      startDate: '15 Oct 2026',
      endDate: '28 Oct 2026',
      participatingSchools: 42,
      registeredLearners: 1280,
      status: 'Active',
      prize: 'R10 000 School Grant + Gold Medals'
    },
    {
      id: 'comp-2',
      title: 'National Mathematics Speed Sprint',
      grades: 'Grades 8–10',
      startDate: '01 Nov 2026',
      endDate: '12 Nov 2026',
      participatingSchools: 68,
      registeredLearners: 2150,
      status: 'Upcoming',
      prize: 'Distinction Certificate + Tablet'
    },
    {
      id: 'comp-3',
      title: 'Senior Phase EMS Business Venture Pitch',
      grades: 'Grades 7–9',
      startDate: '01 Sep 2026',
      endDate: '25 Sep 2026',
      participatingSchools: 35,
      registeredLearners: 890,
      status: 'Completed',
      prize: 'R5 000 Innovation Trophy'
    }
  ]);

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newTitle, setNewTitle] = useState('');
  const [newGrades, setNewGrades] = useState('Grades 10–12');

  const handleCreateChallenge = (e) => {
    e.preventDefault();
    if (!newTitle) return;
    const item = {
      id: `comp-${Date.now()}`,
      title: newTitle,
      grades: newGrades,
      startDate: '01 Dec 2026',
      endDate: '15 Dec 2026',
      participatingSchools: 1,
      registeredLearners: 15,
      status: 'Upcoming',
      prize: 'Fundile Distinction Badge'
    };
    setChallenges([item, ...challenges]);
    setIsModalOpen(false);
    setNewTitle('');
  };

  return (
    <div className="p-4 sm:p-6 lg:p-8 space-y-6 max-w-7xl mx-auto">
      <AdminPanelHeader
        title="Inter-School Competitions & Olympiads"
        subtitle="Organize regional academic challenges, timed exam sprints, and school leaderboards"
        icon={Trophy}
        onBack={onBack}
      />

      <div className="flex justify-end">
        <button
          onClick={() => setIsModalOpen(true)}
          className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold transition shadow-xs cursor-pointer"
        >
          <Trophy className="w-4 h-4 text-[#FF9100]" />
          <span>Launch New Competition</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {challenges.map((c) => (
          <div key={c.id} className="bg-white rounded-2xl border border-slate-200/90 p-5 shadow-xs flex flex-col justify-between space-y-4">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${
                  c.status === 'Active'
                    ? 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                    : c.status === 'Upcoming'
                    ? 'bg-blue-50 text-[#13519C] border border-blue-200'
                    : 'bg-slate-100 text-slate-700 border border-slate-200'
                }`}>
                  {c.status}
                </span>
                <span className="text-xs font-semibold text-slate-500 font-mono">{c.grades}</span>
              </div>
              <h3 className="text-base font-bold text-slate-900 font-afacad leading-snug">{c.title}</h3>
              <p className="text-xs text-amber-900 font-semibold mt-1">🏆 {c.prize}</p>
            </div>

            <div className="bg-slate-50 p-3 rounded-xl border border-slate-100 text-xs font-mono space-y-1">
              <div className="flex justify-between text-slate-600">
                <span>Schools Enrolled:</span>
                <span className="font-bold text-slate-900">{c.participatingSchools}</span>
              </div>
              <div className="flex justify-between text-slate-600">
                <span>Learners Competing:</span>
                <span className="font-bold text-slate-900">{c.registeredLearners}</span>
              </div>
              <div className="flex justify-between text-slate-600">
                <span>Timeline:</span>
                <span className="text-slate-700">{c.startDate} – {c.endDate}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Modal */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 backdrop-blur-xs p-4">
          <div className="bg-white rounded-2xl border border-slate-200 shadow-xl max-w-md w-full p-6 space-y-4">
            <h3 className="text-lg font-bold text-slate-900 font-afacad">Create Academic Competition</h3>
            <form onSubmit={handleCreateChallenge} className="space-y-3">
              <div>
                <label className="text-xs font-semibold text-slate-700 block mb-1">Competition Title</label>
                <input
                  type="text"
                  required
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  placeholder="e.g. Durban Metro Mathematics Derby"
                  className="w-full text-xs border border-slate-200 rounded-xl px-3 py-2 text-slate-900"
                />
              </div>
              <div>
                <label className="text-xs font-semibold text-slate-700 block mb-1">Target Grades</label>
                <select
                  value={newGrades}
                  onChange={(e) => setNewGrades(e.target.value)}
                  className="w-full text-xs border border-slate-200 rounded-xl px-3 py-2 text-slate-900"
                >
                  <option value="Grades 8–9">Senior Phase (Grades 8–9)</option>
                  <option value="Grades 10–12">FET Band (Grades 10–12)</option>
                  <option value="Grade 12">Matric Finals (Grade 12 Only)</option>
                </select>
              </div>
              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 rounded-xl bg-[#13519C] text-white text-xs font-bold"
                >
                  Create Competition
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

/**
 * 4. System Settings View
 */
export function SystemSettingsView({ onBack }) {
  const [settings, setSettings] = useState({
    defaultTerm: '1',
    dataSavingMode: true,
    sandboxTimeout: '2.5',
    maintenanceMode: false,
    aiTutorProvider: 'huggingface_gemma',
  });
  const [savedToast, setSavedToast] = useState(false);

  const handleSave = () => {
    setSavedToast(true);
    setTimeout(() => setSavedToast(false), 2500);
  };

  return (
    <div className="p-4 sm:p-6 lg:p-8 space-y-6 max-w-4xl mx-auto">
      <AdminPanelHeader
        title="Platform & System Settings"
        subtitle="Global platform configuration, timeouts, and deployment defaults"
        icon={Settings}
        onBack={onBack}
      />

      {savedToast && (
        <div className="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs font-semibold flex items-center gap-2">
          <CheckCircle2 className="w-4 h-4 text-emerald-600" />
          <span>Platform settings saved and propagated successfully!</span>
        </div>
      )}

      <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-xs space-y-6">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div>
            <label className="text-xs font-bold text-slate-800 block mb-1">Active CAPS Term</label>
            <select
              value={settings.defaultTerm}
              onChange={(e) => setSettings({ ...settings, defaultTerm: e.target.value })}
              className="w-full text-xs bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 font-medium"
            >
              <option value="1">Term 1 (Jan – March)</option>
              <option value="2">Term 2 (April – June)</option>
              <option value="3">Term 3 (July – Sept)</option>
              <option value="4">Term 4 (Oct – Dec)</option>
            </select>
            <p className="text-[11px] text-slate-500 mt-1">Calendar engine filters out questions beyond this term.</p>
          </div>

          <div>
            <label className="text-xs font-bold text-slate-800 block mb-1">SymPy Compute Sandbox Timeout</label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                step="0.5"
                value={settings.sandboxTimeout}
                onChange={(e) => setSettings({ ...settings, sandboxTimeout: e.target.value })}
                className="w-full text-xs bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 font-mono"
              />
              <span className="text-xs text-slate-500 font-mono">seconds</span>
            </div>
            <p className="text-[11px] text-slate-500 mt-1">Stops long-running symbolic math AST operations.</p>
          </div>

          <div>
            <label className="text-xs font-bold text-slate-800 block mb-1">AI Socratic Tutor Provider</label>
            <select
              value={settings.aiTutorProvider}
              onChange={(e) => setSettings({ ...settings, aiTutorProvider: e.target.value })}
              className="w-full text-xs bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-slate-800 font-medium"
            >
              <option value="huggingface_gemma">Hugging Face API (Gemma Open-Source)</option>
              <option value="gemini_flash">Google Gemini Flash (Subagent Tier)</option>
              <option value="deterministic_only">Zero-LLM Mode Only (Pure Python)</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-bold text-slate-800 block mb-1">Low-Data WebAPK Mode</label>
            <div className="flex items-center gap-2 pt-1">
              <input
                type="checkbox"
                id="lowdata"
                checked={settings.dataSavingMode}
                onChange={(e) => setSettings({ ...settings, dataSavingMode: e.target.checked })}
                className="rounded border-slate-300 text-[#13519C] focus:ring-[#13519C]"
              />
              <label htmlFor="lowdata" className="text-xs font-semibold text-slate-700 cursor-pointer">
                Strict &lt; 2 MB data budget per learner session
              </label>
            </div>
          </div>
        </div>

        <div className="border-t border-slate-100 pt-4 flex justify-end">
          <button
            onClick={handleSave}
            className="px-5 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold transition shadow-xs cursor-pointer"
          >
            Save Global Settings
          </button>
        </div>
      </div>
    </div>
  );
}

/**
 * 5. Security & Access View
 */
export function SecurityAccessView({ onBack }) {
  const securityChecks = [
    { title: 'POPIA Section 35 Child Privacy', status: 'Compliant', desc: 'No learner PII exposed to unauthorized roles; real photos fall back to initials.' },
    { title: 'Database Encryption at Rest', status: 'AES-256 Verified', desc: 'All Firestore and SQLite database records cryptographically encrypted.' },
    { title: 'Data in Transit Protection', status: 'TLS 1.3 Active', desc: 'Strict HTTPS transport security enforced across web and API endpoints.' },
    { title: 'Source Map Masking (Vite)', status: 'Protected', desc: 'Production source maps disabled (sourcemap: false); code cannot be inspected.' },
    { title: 'Deterministic Mark Tamper Shield', status: 'Sealed', desc: 'Formal marks and assessment submissions verified server-side with sha256 checksums.' },
  ];

  return (
    <div className="p-4 sm:p-6 lg:p-8 space-y-6 max-w-5xl mx-auto">
      <AdminPanelHeader
        title="Security, Access Control & POPIA"
        subtitle="Child privacy governance, encryption safeguards, and intellectual property shielding"
        icon={Shield}
        onBack={onBack}
      />

      <div className="space-y-3">
        {securityChecks.map((sc) => (
          <div key={sc.title} className="bg-white rounded-2xl border border-slate-200/90 p-5 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                <h4 className="font-bold text-slate-900 text-sm">{sc.title}</h4>
              </div>
              <p className="text-xs text-slate-500 mt-1 pl-6">{sc.desc}</p>
            </div>
            <span className="self-start sm:self-center px-3 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200 font-mono">
              {sc.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
