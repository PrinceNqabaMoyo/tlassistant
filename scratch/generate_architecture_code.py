# scratch/generate_architecture_code.py
"""
Builds the upgraded generate_architecture_html.py with the comprehensive
Interactive Component & Feature Test Hub.
"""
from pathlib import Path

ROOT = Path(r"c:\Users\princ\fundile-tlassistant-vite")
TARGET = ROOT / "generate_architecture_html.py"

content = '''"""
generate_architecture_html.py
-----------------------------
Reads fundile-architecture.json and writes fundile-architecture.html.
Run from the project root: python generate_architecture_html.py

No external dependencies — stdlib only.
Includes the Comprehensive Interactive Component & Feature Test Hub (#tab-testhub).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
JSON_FILE = ROOT / "fundile-architecture.json"
HTML_FILE = ROOT / "fundile-architecture.html"

STATUS_CLASS = {
    "built":    "status-built",
    "partial":  "status-partial",
    "planned":  "status-planned",
    "deferred": "status-deferred",
}

STATUS_LABEL = {
    "built":    "Built",
    "partial":  "Partial",
    "planned":  "Planned",
    "deferred": "Deferred",
}

def badge(status: str) -> str:
    cls = STATUS_CLASS.get(status, "status-planned")
    label = STATUS_LABEL.get(status, status.capitalize())
    return f'<span class="status-badge {cls}">{label}</span>'

def h(text: str) -> str:
    """HTML-escape a string."""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))

def build_layers(layers: list) -> str:
    cards = []
    for layer in layers:
        dep_str = ", ".join(layer.get("dependsOn", [])) or "None"
        built_parts = layer.get("builtParts", [])
        planned_parts = layer.get("plannedParts", [])
        parts_html = ""
        if built_parts:
            parts_html += f'<div class="layer-deps">Built: <span>{h(", ".join(built_parts))}</span></div>'
        if planned_parts:
            parts_html += f'<div class="layer-deps">Planned: <span>{h(", ".join(planned_parts))}</span></div>'
        plan_ref = layer.get("planReference", "") or layer.get("planRef", "")
        plan_html = f'<div class="layer-deps">Plan: <span>{h(plan_ref)}</span></div>' if plan_ref else ""
        cards.append(f"""
      <div class="layer-card">
        <div class="layer-id">{h(layer["id"])}</div>
        {badge(layer["status"])}
        <div class="layer-name">{h(layer["name"])}</div>
        <div class="layer-desc">{h(layer["description"])}</div>
        {parts_html}
        <div class="layer-deps">Depends on: <span>{h(dep_str)}</span></div>
        {plan_html}
      </div>""")
    return "\\n".join(cards)

def build_services_table(services: dict) -> str:
    rows = []
    for svc in services.get("built", []):
        rows.append(f"""<tr>
          <td><strong>{h(svc["name"])}</strong></td>
          <td>{badge("built")}</td>
          <td class="mono">{h(svc.get("file",""))}</td>
          <td class="muted">{h(svc.get("responsibility",""))}</td>
        </tr>""")
    for svc in services.get("planned", []):
        ref = svc.get("planRef", "")
        ref_html = f' <em style="color:var(--muted);font-size:0.72rem">{h(ref)}</em>' if ref else ""
        rows.append(f"""<tr>
          <td><strong>{h(svc["name"])}</strong></td>
          <td>{badge("planned")}</td>
          <td class="mono">{h(svc.get("file",""))}</td>
          <td class="muted">{h(svc.get("responsibility",""))}{ref_html}</td>
        </tr>""")
    return "\\n".join(rows)

def build_routes_table(routes: dict) -> str:
    rows = []
    for r in routes.get("built", []):
        rows.append(f"""<tr>
          <td class="mono">{h(r["method"])}</td>
          <td class="mono">{h(r["route"])}</td>
          <td>{badge("built")}</td>
          <td class="muted">{h(r.get("description",""))}</td>
        </tr>""")
    for r in routes.get("planned", []):
        desc = r.get("description", r.get("planRef", ""))
        rows.append(f"""<tr>
          <td class="mono">{h(r["method"])}</td>
          <td class="mono">{h(r["route"])}</td>
          <td>{badge("planned")}</td>
          <td class="muted">{h(desc)}</td>
        </tr>""")
    return "\\n".join(rows)

def build_generators(generators: dict) -> str:
    cards = []
    for g in generators.get("built", []):
        subj = g.get("subject", "")
        grade = g.get("grade", "")
        topic = g.get("topic", "")
        grade_str = f"Grade {grade}" if grade else ""
        desc = h(topic) if topic else ""
        cards.append(f"""<div class="gen-card">
          <div class="gen-subject">{h(subj)}</div>
          <div class="gen-grades">{h(grade_str)}</div>
          <div class="gen-count">&#10003; Built {("— " + desc) if desc else ""}</div>
        </div>""")
    for g in generators.get("planned", []):
        subj = g.get("subject", "")
        desc = g.get("description", "")
        status = g.get("status", "planned")
        sym = "&#9651;" if status == "partial" else "&#9675;"
        colour = "var(--partial)" if status == "partial" else "var(--planned)"
        cards.append(f"""<div class="gen-card" style="border-color:rgba(99,102,241,0.3)">
          <div class="gen-subject">{h(subj)}</div>
          <div class="gen-count" style="color:{colour}">{sym} {h(desc)}</div>
        </div>""")
    return "\\n".join(cards)

def build_frontend_table(components: dict) -> str:
    rows = []
    for c in components.get("built", []):
        note = c.get("note", c.get("description", ""))
        layer = c.get("layer", "A")
        rows.append(f"""<tr>
          <td><strong>{h(c["name"])}</strong></td>
          <td>{badge("built")}</td>
          <td>{h(layer)}</td>
          <td class="muted">{h(note)}</td>
        </tr>""")
    for c in components.get("planned", []):
        note = c.get("note", c.get("description", ""))
        layer = c.get("layer", "")
        rows.append(f"""<tr>
          <td><strong>{h(c["name"])}</strong></td>
          <td>{badge("planned")}</td>
          <td>{h(layer)}</td>
          <td class="muted">{h(note)}</td>
        </tr>""")
    return "\\n".join(rows)

def build_firestore_table(collections: dict) -> str:
    rows = []
    for c in collections.get("built", []):
        rows.append(f"""<tr>
          <td class="mono">{h(c["collection"])}</td>
          <td>{badge("built")}</td>
          <td class="muted">{h(c.get("description",""))}</td>
        </tr>""")
    for c in collections.get("planned", []):
        ref = c.get("planRef", "")
        ref_html = f' <em style="font-size:0.72rem">{h(ref)}</em>' if ref else ""
        rows.append(f"""<tr>
          <td class="mono">{h(c["collection"])}</td>
          <td>{badge("planned")}</td>
          <td class="muted">{h(c.get("description",""))}{ref_html}</td>
        </tr>""")
    return "\\n".join(rows)

def build_stack(stack: dict) -> str:
    def section(title, data: dict) -> str:
        items = "".join(
            f"<dt>{h(k)}</dt><dd>{h(str(v))}</dd>"
            for k, v in data.items()
        )
        return f"""<div class="stack-card"><h3>{h(title)}</h3><dl>{items}</dl></div>"""
    parts = []
    if "frontend" in stack:
        parts.append(section("Frontend", stack["frontend"]))
    if "backend" in stack:
        parts.append(section("Backend", stack["backend"]))
    if "database" in stack:
        parts.append(section("Database & Auth", stack["database"]))
    if "deployment" in stack:
        parts.append(section("Deployment", stack["deployment"]))
    return "\\n".join(parts)

def build_packages(packages: dict) -> str:
    cards = []
    for name, pkg in packages.items():
        note = pkg.get("duration", "") or ""
        if pkg.get("hardPaywall"):
            note += " · Hard paywall"
        if pkg.get("profilePersistsAfterTrial"):
            note += " · Profile persists"
        note_html = f'<div class="pkg-note">{h(note)}</div>' if note else ""
        items = "".join(f"<li>{h(f)}</li>" for f in pkg.get("features", []))
        cards.append(f"""<div class="pkg">
          <div class="pkg-name">{h(name.capitalize())}</div>
          {note_html}
          <ul>{items}</ul>
        </div>""")
    return "\\n".join(cards)

def build_principles(principles: list) -> str:
    items = []
    for i, p in enumerate(principles, 1):
        items.append(
            f'<div class="principle"><span class="principle-num">{i}</span>{h(p)}</div>'
        )
    return "\\n".join(items)

def build_open_questions(questions: list) -> str:
    items = []
    for q in questions:
        ref = q.get("planRef", "")
        ref_html = f' <em style="color:var(--muted);font-size:0.72rem">{h(ref)}</em>' if ref else ""
        items.append(
            f'<div class="question"><span class="q-id">{h(q["id"])}</span>{h(q["question"])}{ref_html}</div>'
        )
    return "\\n".join(items)

def build_workflow_panel(workflow: dict) -> str:
    steps = workflow.get("steps", [])
    step_html = "".join(
        f'<div class="question"><span class="q-id">{i+1}</span>{h(s)}</div>'
        for i, s in enumerate(steps)
    )
    script = workflow.get("htmlGeneratorScript", "")
    script_html = (
        f'<div style="margin-top:0.8rem;padding:0.8rem 1rem;background:var(--surface);border:1px solid var(--border);border-radius:8px;">'
        f'<h3 style="margin-bottom:0.4rem;color:var(--accent)">HTML Generator Command</h3>'
        f'<code style="color:var(--built)">{h(script)}</code>'
        f'</div>'
    ) if script else ""
    return f"""<div class="questions">{step_html}</div>{script_html}"""

def build_test_hub(data: dict) -> str:
    built_components = data.get("frontendComponents", {}).get("built", [])
    built_services = data.get("backendServices", {}).get("built", [])
    built_routes = data.get("apiRoutes", {}).get("built", [])
    
    # Generate component directory rows with jump buttons
    comp_rows = []
    for c in built_components:
        name = c.get("name", "")
        path = c.get("path", "")
        desc = c.get("description", c.get("note", ""))
        layer = c.get("layer", "A")
        # Map component to a quick test action
        test_target = "track1"
        if "Offline" in name or "telemetry" in path:
            test_target = "track2"
        elif "Class" in name or "Join" in name:
            test_target = "track3"
        elif "Geometry" in name or "JSXGraph" in name:
            test_target = "geom"
        elif "Report" in name or "Heatmap" in name or "Diagnostic" in name:
            test_target = "triage"
        elif "SimuLearn" in name:
            test_target = "simulearn"
        elif "Badge" in name or "XP" in name or "Gamification" in name or "ProgressMap" in name:
            test_target = "gamification"
        elif "Generator" in name or "Workspace" in name or "Math" in name or "KaTeX" in name:
            test_target = "generator"
        elif "Subscription" in name or "Trial" in name:
            test_target = "track1"
            
        comp_rows.append(f"""<tr class="comp-row" data-name="{h(name.lower())}" data-layer="{h(layer.lower())}">
          <td><strong>{h(name)}</strong></td>
          <td><span class="status-badge status-built">Layer {h(layer)}</span></td>
          <td class="mono muted" style="font-size:0.75rem">{h(path)}</td>
          <td class="muted" style="font-size:0.78rem">{h(desc)}</td>
          <td><button class="test-btn test-btn-sm" onclick="scrollToTestModule('{test_target}')">⚡ Test Module</button></td>
        </tr>""")

    return f"""
    <section>
      <div class="testhub-header">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;">
          <div>
            <h2>🚀 Interactive Component & Feature Test Hub</h2>
            <p>Live sandbox to test every frontend component, backend service, paywall rule, offline sync queue, and deterministic engine without leaving the architecture report.</p>
          </div>
          <div class="testhub-stats">
            <div class="testhub-stat">Built Components: <strong>{len(built_components)}</strong></div>
            <div class="testhub-stat">Backend Services: <strong>{len(built_services)}</strong></div>
            <div class="testhub-stat">API Endpoints: <strong>{len(built_routes)}</strong></div>
            <div class="testhub-stat">PWA Offline: <strong>Active (sw.js)</strong></div>
          </div>
        </div>

        <div class="testhub-nav">
          <span style="font-size:0.75rem;color:var(--muted);align-self:center;margin-right:0.3rem;">Quick Jump:</span>
          <button onclick="scrollToTestModule('track1')">💳 Track 1: Trial &amp; Paywall</button>
          <button onclick="scrollToTestModule('track2')">⚡ Track 2: Load-Shedding &amp; PWA</button>
          <button onclick="scrollToTestModule('track3')">🏫 Track 3: Class LMS &amp; Join Codes</button>
          <button onclick="scrollToTestModule('geom')">📐 Option 4: Geometry Proofs</button>
          <button onclick="scrollToTestModule('triage')">📊 Option 3: Post-Exam Triage</button>
          <button onclick="scrollToTestModule('audit')">🔍 Option 2: Session Audit Trail</button>
          <button onclick="scrollToTestModule('simulearn')">🎬 Layer B: SimuLearn Player</button>
          <button onclick="scrollToTestModule('gamification')">🏆 Layer E: 4-Tier Badges</button>
          <button onclick="scrollToTestModule('generator')">🎲 Layer A: Zero-LLM Sandbox</button>
          <button onclick="scrollToTestModule('compdir')">📁 Full Component Directory</button>
        </div>
      </div>

      <!-- TEST MODULE 1: Track 1 Trial & Paywall Engine -->
      <div id="test-module-track1" class="test-card full-width" style="border-left:4px solid var(--accent);">
        <div class="test-card-header">
          <div class="test-card-title">
            <span>💳 Track 1: 14-Day Trial &amp; Subscription Paywall Engine</span>
            <span class="test-card-tag">Phase D2 · trial_manager.py · SubscriptionModal.jsx · TrialCountdownBanner.jsx</span>
          </div>
          <span class="status-badge status-built">100% Deterministic Gate</span>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
          <div class="test-form">
            <div class="test-form-row">
              <label class="test-label">Student ID:</label>
              <input type="text" id="trial-student-id" class="test-input" value="std_khumalo_08">
            </div>
            <div class="test-form-row">
              <label class="test-label">Simulate Tier:</label>
              <select id="trial-sim-tier" class="test-select" onchange="updateTrialBannerPreview()">
                <option value="trial_14">Free Trial (14 days remaining - New Student)</option>
                <option value="trial_3">Free Trial (3 days remaining - Warning State)</option>
                <option value="trial_1">Free Trial (1 day remaining - Urgent Critical)</option>
                <option value="trial_expired">Trial Expired (0 days - Hard Paywall Locked)</option>
                <option value="standard">Standard Subscription (R149/mo - Active)</option>
                <option value="pro">Pro AI Socratic Tutor (R249/mo - Active)</option>
                <option value="school">School Institutional License (Active)</option>
              </select>
            </div>
            <div class="test-form-row">
              <label class="test-label">Action to Test:</label>
              <select id="trial-action-test" class="test-select">
                <option value="attempt_question">attempt_question (Standard CAPS Practice)</option>
                <option value="ask_tutor">ask_tutor (Pro Socratic Tutor Help)</option>
                <option value="download_pdf_report">download_pdf_report (Printable PDF Diagnostic)</option>
                <option value="view_class_heatmap">view_class_heatmap (Teacher LMS Diagnostic)</option>
              </select>
            </div>
            <div class="test-btn-group">
              <button class="test-btn test-btn-primary" onclick="simulateCheckTrialAccess()">
                ▶ Simulate /api/trial/check-access
              </button>
              <button class="test-btn" onclick="openSubscriptionModalPreview()">
                👁 Open Subscription Modal Preview
              </button>
              <button class="test-btn test-btn-success" onclick="mockUpgradeToPro()">
                ✨ Mock Upgrade to Pro
              </button>
            </div>
          </div>

          <div class="test-output">
            <div class="test-output-header">
              <span>Live Visual Component Preview (TrialCountdownBanner.jsx)</span>
              <span id="trial-banner-badge" class="status-badge status-built">Active</span>
            </div>
            <!-- Banner Preview Container -->
            <div id="trial-banner-preview" style="padding:0.9rem;border-radius:8px;margin-bottom:0.8rem;transition:all 0.2s;">
              <!-- Dynamic Banner Content -->
            </div>
            <div class="test-output-header">
              <span>Gate Decision JSON (/api/trial/check-access)</span>
              <span id="trial-http-status" class="mono" style="color:var(--built)">HTTP 200 OK</span>
            </div>
            <pre id="trial-json-result" class="test-json">// Click 'Simulate /api/trial/check-access' to inspect response payload</pre>
          </div>
        </div>
      </div>

      <!-- TEST MODULE 2: Track 2 Load-Shedding & Offline PWA -->
      <div id="test-module-track2" class="test-card full-width" style="border-left:4px solid var(--partial);">
        <div class="test-card-header">
          <div class="test-card-title">
            <span>⚡ Track 2: South African Load-Shedding Resilience &amp; Offline PWA Sync</span>
            <span class="test-card-tag">Improvement F · vite-plugin-pwa · OfflineStatusBadge.jsx · telemetryBuffer.js</span>
          </div>
          <span class="status-badge status-built">Service Worker (sw.js) Built</span>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
          <div class="test-form">
            <div style="background:var(--surface2);padding:0.8rem;border-radius:8px;border:1px solid var(--border);">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
                <strong style="font-size:0.85rem;">Eskom Grid &amp; Network Status Simulator</strong>
                <button id="pwa-toggle-net-btn" class="test-btn test-btn-warning" onclick="toggleNetworkSimulation()">
                  🔴 Cut Power (Simulate Stage 6 Load-Shedding)
                </button>
              </div>
              <p style="font-size:0.75rem;color:var(--muted);margin:0;">
                Toggling to Offline activates <code>telemetryBuffer.js</code> local storage queuing (<code>fundile_offline_session_queue</code>). All practice sessions continue seamlessly offline.
              </p>
            </div>

            <div class="test-form-row">
              <label class="test-label">Action Type:</label>
              <select id="pwa-action-type" class="test-select">
                <option value="cell_attempt">Record Ledger Cell (Accounting Grade 10)</option>
                <option value="math_step">SymPy Working Line Transition (Trig Grade 10)</option>
                <option value="hint_requested">Deterministic Tier 2 Hint Requested</option>
                <option value="exam_completed">Submit Mock Exam (Score: 84%)</option>
              </select>
            </div>
            <div class="test-form-row">
              <label class="test-label">Action Data:</label>
              <input type="text" id="pwa-action-data" class="test-input" value="CRJ: Bank Gross R11,500 (+Output VAT R1,500)">
            </div>

            <div class="test-btn-group">
              <button class="test-btn test-btn-primary" onclick="queueOfflineAction()">
                ➕ Queue Action in Offline Buffer
              </button>
              <button class="test-btn test-btn-success" onclick="flushOfflineQueue()">
                🔄 Flush Offline Queue to Backend
              </button>
              <button class="test-btn test-btn-danger" onclick="clearOfflineQueue()">
                🗑 Clear Local Storage
              </button>
            </div>
          </div>

          <div class="test-output">
            <div class="test-output-header">
              <span>Live Visual Component Preview (OfflineStatusBadge.jsx)</span>
              <span id="pwa-badge-status" class="mono" style="color:var(--built)">Online</span>
            </div>
            <div id="pwa-badge-preview" style="padding:0.8rem;background:var(--surface2);border-radius:8px;margin-bottom:0.8rem;display:flex;align-items:center;gap:0.8rem;">
              <!-- Dynamic Offline Badge Content -->
            </div>

            <div class="test-output-header">
              <span>Local Offline Queue (<code>fundile_offline_session_queue</code>)</span>
              <span id="pwa-queue-count" class="mono" style="color:var(--accent)">0 Items Pending</span>
            </div>
            <div id="pwa-queue-list" style="max-height:160px;overflow-y:auto;background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.5rem;font-size:0.75rem;font-family:monospace;">
              <span style="color:var(--muted)">No actions pending in offline buffer.</span>
            </div>

            <div style="margin-top:0.6rem;padding:0.6rem;background:rgba(56,189,248,0.08);border-radius:6px;border:1px solid rgba(56,189,248,0.2);font-size:0.72rem;color:var(--muted);">
              <strong>PWA Cache Specification:</strong> <code>dist/sw.js</code> (6.8 kB) precaches 93 static bundles. <code>workbox.maximumFileSizeToCacheInBytes: 6 MiB</code> handles full vendor chunks for zero load-shedding downtime.
            </div>
          </div>
        </div>
      </div>

      <!-- TEST MODULE 3: Track 3 Teacher LMS Cockpit & Class Join Codes -->
      <div id="test-module-track3" class="test-card full-width" style="border-left:4px solid var(--built);">
        <div class="test-card-header">
          <div class="test-card-title">
            <span>🏫 Track 3: Teacher LMS Cockpit &amp; Unambiguous 6-Char Join Codes</span>
            <span class="test-card-tag">Phase D4 · class_service.py · ClassManagerModal.jsx · JoinClassModal.jsx</span>
          </div>
          <span class="status-badge status-built">Firestore classes/{{classId}} Built</span>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
          <!-- Teacher Side: Create Class -->
          <div class="test-form">
            <div style="border-bottom:1px solid var(--border);padding-bottom:0.4rem;margin-bottom:0.4rem;">
              <strong style="color:var(--accent);font-size:0.85rem;">1. Teacher Cockpit: Create Class &amp; Generate Join Code</strong>
            </div>
            <div class="test-form-row">
              <label class="test-label">Teacher ID:</label>
              <input type="text" id="lms-teacher-id" class="test-input" value="tch_ndlovu_42">
            </div>
            <div class="test-form-row">
              <label class="test-label">Class Name:</label>
              <input type="text" id="lms-class-name" class="test-input" value="Grade 10 Accounting 10A">
            </div>
            <div class="test-form-row">
              <label class="test-label">Grade &amp; Subject:</label>
              <div style="display:flex;gap:0.5rem;">
                <select id="lms-grade" class="test-select" style="width:100px;">
                  <option value="10">Grade 10</option>
                  <option value="11">Grade 11</option>
                  <option value="12">Grade 12</option>
                </select>
                <select id="lms-subject" class="test-select">
                  <option value="Accounting">Accounting</option>
                  <option value="Mathematics">Mathematics</option>
                  <option value="Business Studies">Business Studies</option>
                  <option value="EMS">EMS</option>
                </select>
              </div>
            </div>
            <div class="test-btn-group">
              <button class="test-btn test-btn-primary" onclick="simulateCreateClass()">
                ✨ Create Class &amp; Generate Code (/api/classes/create)
              </button>
            </div>

            <!-- Active Class & Join Code Badge -->
            <div id="lms-class-created-box" style="margin-top:0.8rem;padding:0.8rem;background:var(--surface2);border-radius:8px;border:1px solid var(--border);">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:0.75rem;color:var(--muted)">Active Class Join Code:</span>
                <span id="lms-active-code" class="mono" style="font-size:1.4rem;font-weight:800;color:var(--accent);letter-spacing:3px;">ACC9B2</span>
              </div>
              <p style="font-size:0.72rem;color:var(--muted);margin-top:0.3rem;">
                * Stripped ambiguous characters <code>0, O, 1, I, L</code> to ensure 0 blackboard misreads.
              </p>
              <div style="margin-top:0.5rem;display:flex;gap:0.4rem;">
                <button class="test-btn test-btn-sm" onclick="copyClassCode()">📋 Copy Code</button>
                <button class="test-btn test-btn-sm test-btn-success" onclick="copyWhatsAppShare()">💬 Copy WhatsApp Blackboard Invite</button>
              </div>
            </div>
          </div>

          <!-- Student Side: Join Class & View Roster -->
          <div class="test-form">
            <div style="border-bottom:1px solid var(--border);padding-bottom:0.4rem;margin-bottom:0.4rem;">
              <strong style="color:var(--built);font-size:0.85rem;">2. Student Side: Join Class (JoinClassModal.jsx)</strong>
            </div>
            <div class="test-form-row">
              <label class="test-label">Join Code:</label>
              <input type="text" id="lms-student-code-input" class="test-input mono" value="ACC9B2" style="font-size:1rem;font-weight:700;text-transform:uppercase;">
            </div>
            <div class="test-form-row">
              <label class="test-label">Student Name:</label>
              <input type="text" id="lms-student-name" class="test-input" value="Sipho Sithole">
            </div>
            <div class="test-form-row">
              <label class="test-label">Student ID:</label>
              <input type="text" id="lms-student-id" class="test-input" value="std_sipho_99">
            </div>
            <div class="test-btn-group">
              <button class="test-btn test-btn-success" onclick="simulateJoinClass()">
                🚀 Join Class (/api/classes/join)
              </button>
            </div>

            <!-- Student Roster Table -->
            <div style="margin-top:0.8rem;">
              <div class="test-output-header">
                <span>Teacher Class Roster (<span id="lms-roster-count">3</span> Students Enrolled)</span>
                <span class="mono" style="color:var(--accent)">Live Firestore Mock</span>
              </div>
              <div class="table-wrap" style="max-height:160px;overflow-y:auto;">
                <table style="font-size:0.75rem;">
                  <thead><tr><th>Student</th><th>ID</th><th>Joined</th><th>Status</th></tr></thead>
                  <tbody id="lms-roster-tbody">
                    <tr><td>Thabo Ndlovu</td><td class="mono">std_thabo_01</td><td class="muted">Today 08:14</td><td><span class="status-badge status-built">Enrolled</span></td></tr>
                    <tr><td>Lerato Molefe</td><td class="mono">std_lerato_04</td><td class="muted">Today 08:19</td><td><span class="status-badge status-built">Enrolled</span></td></tr>
                    <tr><td>Anele Zondo</td><td class="mono">std_anele_22</td><td class="muted">Today 08:25</td><td><span class="status-badge status-built">Enrolled</span></td></tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="test-grid">
        <!-- TEST MODULE 4: Option 4 Euclidean & Circle Geometry -->
        <div id="test-module-geom" class="test-card">
          <div class="test-card-header">
            <div class="test-card-title">
              <span>📐 Option 4: Euclidean &amp; Circle Geometry Engine</span>
              <span class="test-card-tag">Phase 5G · JSXGraph · SymPy</span>
            </div>
            <span class="status-badge status-built">SVG / Proof Graph</span>
          </div>
          <div class="test-form">
            <div class="test-form-row">
              <label class="test-label">Select Theorem:</label>
              <select id="geom-theorem-select" class="test-select" onchange="renderGeometryTheorem()">
                <option value="tan_chord">Tangent-Chord Theorem (Tan Chord Thm)</option>
                <option value="centre_circum">Angle at Centre = 2 × Angle at Circumference</option>
                <option value="cyclic_quad">Cyclic Quad: Opposite Angles Supplementary</option>
              </select>
            </div>
          </div>
          <!-- Interactive SVG Geometry Canvas -->
          <div id="geom-svg-canvas" style="background:#0b0d13;border:1px solid var(--border);border-radius:8px;padding:0.5rem;text-align:center;">
            <!-- Rendered dynamically -->
          </div>
          <!-- 2-Column Statement & Reason Proof -->
          <div class="table-wrap">
            <table style="font-size:0.75rem;">
              <thead><tr><th>Statement</th><th>Reason (CAPS Standard Abbr.)</th><th>Mark</th></tr></thead>
              <tbody id="geom-proof-tbody">
                <!-- Dynamically filled -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- TEST MODULE 5: Option 3 Post-Exam Triage Report -->
        <div id="test-module-triage" class="test-card">
          <div class="test-card-header">
            <div class="test-card-title">
              <span>📊 Option 3: Post-Exam Triage &amp; Post-Mortem Report</span>
              <span class="test-card-tag">Phase 5E · Parent WhatsApp Digest</span>
            </div>
            <span class="status-badge status-built">Misconception Taxonomy</span>
          </div>
          <div class="test-form">
            <div class="test-form-row">
              <label class="test-label">Exam Paper:</label>
              <select id="triage-exam-select" class="test-select">
                <option value="acc10_t1">Grade 10 Accounting Term 1 Standardized Exam</option>
                <option value="math10_t1">Grade 10 Mathematics Term 1 Algebra &amp; Trig</option>
              </select>
            </div>
            <div class="test-form-row">
              <label class="test-label">Learner Score:</label>
              <div style="display:flex;align-items:center;gap:0.8rem;">
                <input type="range" id="triage-score-slider" min="20" max="95" value="44" style="flex:1" oninput="document.getElementById('triage-score-val').innerText = this.value + '%'; updateTriageReport();">
                <span id="triage-score-val" class="mono" style="font-weight:700;color:var(--partial);width:45px;">44%</span>
              </div>
            </div>
          </div>
          <div id="triage-report-box" style="background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:0.8rem;font-size:0.78rem;">
            <!-- Dynamically calculated -->
          </div>
          <div style="display:flex;gap:0.5rem;">
            <button class="test-btn test-btn-sm test-btn-primary" onclick="copyParentWhatsAppReport()">💬 Copy Parent WhatsApp Digest</button>
            <button class="test-btn test-btn-sm" onclick="alert('Launching targeted 5-min micro-drill: VAT Net vs Gross Calculation (Elementary Mode)')">🎯 Launch 5-Min Fix Drill</button>
          </div>
        </div>

        <!-- TEST MODULE 6: Option 2 Session Audit Trail Inspector -->
        <div id="test-module-audit" class="test-card">
          <div class="test-card-header">
            <div class="test-card-title">
              <span>🔍 Option 2: Dual-Layer Session Audit Trail</span>
              <span class="test-card-tag">Phase 5F · session_file_writer.py · compute-ready index</span>
            </div>
            <span class="status-badge status-built">Session Inspector</span>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;">
            <div style="background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.7rem;">
              <strong style="font-size:0.75rem;color:var(--accent);display:block;margin-bottom:0.4rem;">Layer 1: Deterministic Engine Log</strong>
              <div style="font-size:0.72rem;font-family:monospace;color:var(--muted);line-height:1.4;">
                seed: 4201<br>
                cell: (row 1, col 3)<br>
                input: "R11 500"<br>
                check: SymPy _decomma() == 11500<br>
                status: <span style="color:var(--built)">CORRECT (+3 marks)</span><br>
                misconception: NONE<br>
                time_in_cell: 14.2s
              </div>
            </div>
            <div style="background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.7rem;">
              <strong style="font-size:0.75rem;color:var(--partial);display:block;margin-bottom:0.4rem;">Layer 2: Agent Socratic Log</strong>
              <div style="font-size:0.72rem;font-family:monospace;color:var(--muted);line-height:1.4;">
                guardrail: <span style="color:var(--built)">APPROVED</span> (Acct G10)<br>
                chip_clicked: "Why mark up?"<br>
                llm: Google Gemini 2.0 Flash<br>
                prompt_tokens: 142<br>
                response_tokens: 68<br>
                latency: 384 ms<br>
                authority: 0% calculation
              </div>
            </div>
          </div>
          <div style="font-size:0.72rem;color:var(--muted);margin-top:0.4rem;">
            Firestore: <code>session_index/{{sessionId}}</code> · Storage: <code>students/{{userId}}/sessions/{{sessionId}}.md</code>
          </div>
        </div>

        <!-- TEST MODULE 7: Layer B SimuLearn Player -->
        <div id="test-module-simulearn" class="test-card">
          <div class="test-card-header">
            <div class="test-card-title">
              <span>🎬 Layer B: SimuLearn Step-by-Step Scenario Player</span>
              <span class="test-card-tag">Phase 5D · SimuLearnPlayer.jsx · Data-light (0.1% cost)</span>
            </div>
            <span class="status-badge status-built">Canvas Animator</span>
          </div>
          <div style="background:#0e111a;border:1px solid var(--border);border-radius:8px;padding:0.8rem;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">
              <strong style="font-size:0.8rem;color:var(--accent);">Scenario: Cash Receipts Journal Entry</strong>
              <span id="sim-step-badge" class="status-badge status-partial">Step 1 of 4</span>
            </div>
            <div id="sim-step-text" style="font-size:0.78rem;color:var(--text);margin-bottom:0.8rem;min-height:38px;">
              Sold merchandise for cash to K. Naidoo, R5,750 (VAT 15% inclusive). Cost of Sales R3,800.
            </div>
            <!-- Simulated Ledger Highlights -->
            <div class="table-wrap">
              <table style="font-size:0.72rem;text-align:center;">
                <thead><tr><th>Doc</th><th>Day</th><th>Details</th><th>Analysis</th><th>Bank</th><th>Sales</th><th>Cost of Sales</th></tr></thead>
                <tbody>
                  <tr id="sim-ledger-row">
                    <td>001</td><td>05</td><td>K. Naidoo</td>
                    <td id="sim-c-analysis" style="color:var(--muted)">-</td>
                    <td id="sim-c-bank" style="color:var(--muted)">-</td>
                    <td id="sim-c-sales" style="color:var(--muted)">-</td>
                    <td id="sim-c-cos" style="color:var(--muted)">-</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div style="display:flex;gap:0.4rem;align-items:center;justify-content:space-between;">
            <button class="test-btn test-btn-sm" onclick="stepSimuLearn(-1)">⏮ Prev Step</button>
            <button class="test-btn test-btn-sm test-btn-primary" onclick="stepSimuLearn(1)">Next Step ⏭</button>
            <button class="test-btn test-btn-sm" onclick="resetSimuLearn()">🔄 Reset</button>
          </div>
        </div>

        <!-- TEST MODULE 8: Layer E Gamification & 4-Tier Badges -->
        <div id="test-module-gamification" class="test-card">
          <div class="test-card-header">
            <div class="test-card-title">
              <span>🏆 Layer E: Ungameable Gamification &amp; 4-Tier Badges</span>
              <span class="test-card-tag">Complete-App §15 · BadgeCard.jsx · XPProgressBar.jsx</span>
            </div>
            <span class="status-badge status-built">4-Tier System</span>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:0.8rem;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.4rem;">
              <span style="font-size:0.78rem;font-weight:700;">Level <span id="game-level">3</span> Mastery Rank</span>
              <span id="game-xp-text" class="mono" style="font-size:0.78rem;color:var(--accent);">350 / 500 XP</span>
            </div>
            <div style="height:8px;background:var(--surface2);border-radius:4px;overflow:hidden;margin-bottom:0.8rem;">
              <div id="game-xp-bar" style="width:70%;height:100%;background:linear-gradient(90deg, #38bdf8, #22c55e);transition:width 0.3s;"></div>
            </div>
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0.4rem;text-align:center;">
              <div style="background:var(--surface);border:1px solid rgba(205,127,50,0.4);border-radius:6px;padding:0.4rem;">
                <div style="font-size:1.1rem;">📌</div>
                <div style="font-size:0.65rem;color:var(--text);font-weight:700;">Subskill Pin</div>
                <div style="font-size:0.62rem;color:var(--built);">Unlocked</div>
              </div>
              <div style="background:var(--surface);border:1px solid rgba(192,192,192,0.4);border-radius:6px;padding:0.4rem;">
                <div style="font-size:1.1rem;">🥈</div>
                <div style="font-size:0.65rem;color:var(--text);font-weight:700;">Topic Medal</div>
                <div style="font-size:0.62rem;color:var(--built);">Unlocked</div>
              </div>
              <div style="background:var(--surface);border:1px solid rgba(245,158,11,0.4);border-radius:6px;padding:0.4rem;">
                <div style="font-size:1.1rem;">🏆</div>
                <div style="font-size:0.65rem;color:var(--text);font-weight:700;">Term Trophy</div>
                <div style="font-size:0.62rem;color:var(--partial);" id="badge-trophy-status">In Progress</div>
              </div>
              <div style="background:var(--surface);border:1px solid rgba(99,102,241,0.4);border-radius:6px;padding:0.4rem;">
                <div style="font-size:1.1rem;">💎</div>
                <div style="font-size:0.65rem;color:var(--text);font-weight:700;">Subject Medallion</div>
                <div style="font-size:0.62rem;color:var(--muted);">Locked</div>
              </div>
            </div>
          </div>
          <div style="display:flex;gap:0.4rem;">
            <button class="test-btn test-btn-sm test-btn-success" onclick="addGamificationXP(50)">+50 XP (Master Subskill)</button>
            <button class="test-btn test-btn-sm test-btn-primary" onclick="addGamificationXP(150)">+150 XP (Pass Assessment)</button>
          </div>
        </div>

        <!-- TEST MODULE 9: Layer A Deterministic Generator Sandbox -->
        <div id="test-module-generator" class="test-card">
          <div class="test-card-header">
            <div class="test-card-title">
              <span>🎲 Layer A: Zero-LLM Deterministic Generator Sandbox</span>
              <span class="test-card-tag">Rule 16 · SymPy · 3-Tier Pre-baked Hints</span>
            </div>
            <span class="status-badge status-built">Zero Token Cost</span>
          </div>
          <div class="test-form">
            <div class="test-form-row">
              <label class="test-label">Subject:</label>
              <select id="gen-subject-select" class="test-select" onchange="runDeterministicGeneratorSandbox()">
                <option value="acc10">Grade 10 Accounting (VAT &amp; Ledgers)</option>
                <option value="math10">Grade 10 Mathematics (Trig &amp; Special Angles)</option>
                <option value="bs10">Grade 10 Business Studies (PESTLE &amp; Macro)</option>
                <option value="ems8">Grade 8 EMS (Financial Accounting Core)</option>
              </select>
            </div>
            <div class="test-form-row">
              <label class="test-label">Random Seed:</label>
              <div style="display:flex;gap:0.4rem;">
                <input type="number" id="gen-seed-input" class="test-input" value="42" style="width:90px;">
                <button class="test-btn test-btn-sm" onclick="document.getElementById('gen-seed-input').value = Math.floor(Math.random()*10000); runDeterministicGeneratorSandbox();">🎲 New Seed</button>
              </div>
            </div>
          </div>
          <div id="gen-preview-box" style="background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.7rem;font-size:0.78rem;">
            <!-- Question rendered here -->
          </div>
          <div style="display:flex;gap:0.4rem;flex-wrap:wrap;">
            <button class="test-btn test-btn-sm" onclick="revealHint(1)">💡 Hint 1 (Location)</button>
            <button class="test-btn test-btn-sm" onclick="revealHint(2)">📘 Hint 2 (Concept Rule)</button>
            <button class="test-btn test-btn-sm" onclick="revealHint(3)">🧮 Hint 3 (Worked Step)</button>
          </div>
          <div id="gen-hint-box" style="font-size:0.75rem;color:var(--muted);background:var(--surface2);padding:0.6rem;border-radius:6px;display:none;">
            <!-- Hint text -->
          </div>
        </div>
      </div>

      <!-- TEST MODULE 10: Complete Component Directory & Matrix Search -->
      <div id="test-module-compdir" class="test-card full-width">
        <div class="test-card-header">
          <div class="test-card-title">
            <span>📁 Complete Frontend Component Directory &amp; Quick-Launch Matrix</span>
            <span class="test-card-tag">{len(built_components)} Built Production Components</span>
          </div>
          <div style="display:flex;gap:0.4rem;align-items:center;">
            <input type="text" id="comp-filter-input" class="test-input" placeholder="Filter components by name..." style="width:220px;padding:0.3rem 0.6rem;" oninput="filterComponentTable()">
          </div>
        </div>
        <div class="table-wrap" style="max-height:450px;overflow-y:auto;">
          <table>
            <thead><tr><th>Component</th><th>Status</th><th>File Path</th><th>Description &amp; Role</th><th>Interactive Test</th></tr></thead>
            <tbody id="comp-matrix-tbody">
              {"".join(comp_rows)}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Subscription Modal Simulation Dialog -->
    <div id="sub-modal-sim" class="sim-modal-overlay" onclick="if(event.target===this) closeSubscriptionModalPreview()">
      <div class="sim-modal">
        <button class="sim-modal-close" onclick="closeSubscriptionModalPreview()">&times;</button>
        <div style="text-align:center;margin-bottom:1.5rem;">
          <h2 style="font-size:1.3rem;color:var(--accent);margin-bottom:0.3rem;">Choose Your Fundile Learning Plan</h2>
          <p style="font-size:0.8rem;color:var(--muted)">100% Aligned with South African Curriculum Standards (CAPS) · Authentic Exam Standards</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.8rem;margin-bottom:1.5rem;">
          <div style="background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:1rem;text-align:center;">
            <strong style="font-size:0.9rem;display:block;">Standard</strong>
            <div style="font-size:1.2rem;font-weight:800;color:var(--text);margin:0.4rem 0;">R149<span style="font-size:0.75rem;font-weight:normal">/mo</span></div>
            <ul style="font-size:0.72rem;color:var(--muted);text-align:left;list-style:none;padding:0;margin:0.8rem 0;">
              <li>✓ Unlimited deterministic questions</li>
              <li>✓ 3-tier pre-baked hints</li>
              <li>✓ SymPy procedure tracker</li>
              <li>✓ Offline load-shedding PWA sync</li>
            </ul>
            <button class="test-btn test-btn-sm" style="width:100%" onclick="mockCompleteUpgrade('standard')">Select Standard</button>
          </div>
          <div style="background:var(--surface2);border:2px solid var(--accent);border-radius:8px;padding:1rem;text-align:center;position:relative;">
            <span style="position:absolute;top:-10px;right:10px;background:var(--accent);color:#0f1117;font-size:0.65rem;font-weight:800;padding:2px 6px;border-radius:4px;">POPULAR</span>
            <strong style="font-size:0.9rem;color:var(--accent);display:block;">Pro Socratic Tutor</strong>
            <div style="font-size:1.2rem;font-weight:800;color:var(--accent);margin:0.4rem 0;">R249<span style="font-size:0.75rem;font-weight:normal">/mo</span></div>
            <ul style="font-size:0.72rem;color:var(--muted);text-align:left;list-style:none;padding:0;margin:0.8rem 0;">
              <li>✓ Everything in Standard</li>
              <li>✓ Live on-rails Socratic Tutor</li>
              <li>✓ Targeted misconception micro-drills</li>
              <li>✓ Downloadable A4 PDF reports</li>
            </ul>
            <button class="test-btn test-btn-sm test-btn-primary" style="width:100%" onclick="mockCompleteUpgrade('pro')">Upgrade to Pro</button>
          </div>
          <div style="background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:1rem;text-align:center;">
            <strong style="font-size:0.9rem;display:block;">School / Class</strong>
            <div style="font-size:1.1rem;font-weight:800;color:var(--text);margin:0.4rem 0;">Bulk Quote</div>
            <ul style="font-size:0.72rem;color:var(--muted);text-align:left;list-style:none;padding:0;margin:0.8rem 0;">
              <li>✓ Teacher LMS Cockpit</li>
              <li>✓ 6-char join codes &amp; rosters</li>
              <li>✓ Class diagnostic heatmap</li>
              <li>✓ Printable test &amp; memo generator</li>
            </ul>
            <button class="test-btn test-btn-sm" style="width:100%" onclick="mockCompleteUpgrade('school')">Select School</button>
          </div>
        </div>
        <div style="text-align:center;font-size:0.72rem;color:var(--muted);">
          Simulating frontend modal trigger. Clicking any tier immediately updates simulated student profile state!
        </div>
      </div>
    </div>
    """

CSS = """
  :root {
    --bg:#0f1117;--surface:#1a1d27;--surface2:#22263a;--border:#2e3250;
    --text:#e2e8f0;--muted:#8892b0;--built:#22c55e;--partial:#f59e0b;
    --planned:#6366f1;--deferred:#64748b;--accent:#38bdf8;--gold:#f59e0b;
    --font:'Inter',system-ui,sans-serif;
  }
  *{box-sizing:border-box;margin:0;padding:0;}
  body{background:var(--bg);color:var(--text);font-family:var(--font);font-size:14px;line-height:1.6;}
  code{font-family:'Fira Code',monospace;font-size:0.85em;}
  .container{max-width:1240px;margin:0 auto;padding:2rem 1.5rem;}
  header{border-bottom:1px solid var(--border);padding-bottom:1.5rem;margin-bottom:2rem;}
  header h1{font-size:1.8rem;font-weight:700;color:var(--accent);letter-spacing:-0.5px;}
  header p{color:var(--muted);margin-top:0.3rem;}
  .meta{display:flex;gap:1rem;margin-top:0.8rem;flex-wrap:wrap;}
  .meta span{font-size:0.75rem;color:var(--muted);background:var(--surface2);padding:2px 8px;border-radius:4px;border:1px solid var(--border);}
  .legend{display:flex;gap:1rem;margin-bottom:2rem;flex-wrap:wrap;}
  .legend-item{display:flex;align-items:center;gap:6px;font-size:0.75rem;color:var(--muted);}
  .dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;}
  h2{font-size:1rem;font-weight:600;color:var(--accent);margin-bottom:1rem;padding-bottom:0.4rem;border-bottom:1px solid var(--border);text-transform:uppercase;letter-spacing:0.05em;}
  h3{font-size:0.85rem;font-weight:600;color:var(--text);margin-bottom:0.6rem;}
  section{margin-bottom:2.5rem;}
  .layers{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:1rem;}
  .layer-card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1.2rem;position:relative;transition:border-color 0.2s;}
  .layer-card:hover{border-color:var(--accent);}
  .layer-id{font-size:2rem;font-weight:800;position:absolute;top:1rem;right:1.2rem;opacity:0.12;}
  .layer-name{font-size:1rem;font-weight:700;margin-bottom:0.3rem;}
  .layer-desc{color:var(--muted);font-size:0.82rem;margin-bottom:0.8rem;}
  .layer-deps{font-size:0.75rem;color:var(--muted);margin-top:2px;}
  .layer-deps span{color:var(--text);}
  .status-badge{display:inline-block;font-size:0.7rem;font-weight:600;padding:2px 8px;border-radius:4px;margin-bottom:0.6rem;text-transform:uppercase;letter-spacing:0.05em;}
  .status-built{background:rgba(34,197,94,0.15);color:var(--built);border:1px solid rgba(34,197,94,0.3);}
  .status-partial{background:rgba(245,158,11,0.15);color:var(--partial);border:1px solid rgba(245,158,11,0.3);}
  .status-planned{background:rgba(99,102,241,0.15);color:var(--planned);border:1px solid rgba(99,102,241,0.3);}
  .status-deferred{background:rgba(100,116,139,0.15);color:var(--deferred);border:1px solid rgba(100,116,139,0.3);}
  .table-wrap{overflow-x:auto;border-radius:8px;border:1px solid var(--border);}
  table{width:100%;border-collapse:collapse;}
  th{background:var(--surface2);color:var(--muted);font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;padding:0.6rem 0.8rem;text-align:left;border-bottom:1px solid var(--border);}
  td{padding:0.55rem 0.8rem;border-bottom:1px solid var(--border);font-size:0.82rem;vertical-align:top;}
  tr:last-child td{border-bottom:none;}
  tr:hover td{background:rgba(255,255,255,0.02);}
  td.mono{font-family:'Fira Code',monospace;font-size:0.78rem;color:var(--accent);}
  td.muted{color:var(--muted);}
  .gen-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:0.6rem;}
  .gen-card{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:0.7rem 0.9rem;}
  .gen-subject{font-weight:600;font-size:0.8rem;color:var(--text);}
  .gen-grades{font-size:0.72rem;color:var(--muted);margin-top:2px;}
  .gen-count{font-size:0.7rem;color:var(--built);margin-top:2px;}
  .principles{display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;}
  .principle{background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:0.7rem 0.9rem;font-size:0.8rem;color:var(--muted);display:flex;gap:0.6rem;align-items:flex-start;}
  .principle-num{color:var(--accent);font-weight:700;flex-shrink:0;font-size:0.75rem;}
  .packages{display:grid;grid-template-columns:repeat(4,1fr);gap:0.8rem;}
  .pkg{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1rem;}
  .pkg-name{font-weight:700;font-size:0.9rem;margin-bottom:0.3rem;color:var(--accent);}
  .pkg-note{font-size:0.72rem;color:var(--gold);margin-bottom:0.6rem;}
  .pkg ul{list-style:none;}
  .pkg li{font-size:0.75rem;color:var(--muted);padding:2px 0;padding-left:1rem;position:relative;}
  .pkg li::before{content:'✓';position:absolute;left:0;color:var(--built);font-size:0.7rem;}
  .questions{display:grid;gap:0.5rem;}
  .question{background:var(--surface);border:1px solid rgba(245,158,11,0.25);border-radius:6px;padding:0.7rem 0.9rem;display:flex;gap:0.8rem;align-items:flex-start;font-size:0.82rem;}
  .q-id{color:var(--partial);font-weight:700;flex-shrink:0;font-size:0.75rem;}
  .tabs{display:flex;gap:0;margin-bottom:1rem;border-bottom:1px solid var(--border);flex-wrap:wrap;}
  .tab{padding:0.5rem 1rem;font-size:0.8rem;cursor:pointer;color:var(--muted);border-bottom:2px solid transparent;transition:all 0.15s;}
  .tab.active{color:var(--accent);border-bottom-color:var(--accent);font-weight:600;}
  .tab-panel{display:none;}
  .tab-panel.active{display:block;}
  .stack-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;}
  .stack-card{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:1rem;}
  .stack-card h3{color:var(--accent);margin-bottom:0.6rem;}
  .stack-card dl{display:grid;grid-template-columns:auto 1fr;gap:0.3rem 0.8rem;font-size:0.8rem;}
  .stack-card dt{color:var(--muted);white-space:nowrap;}
  .stack-card dd{color:var(--text);}
  
  /* Test Hub Custom CSS */
  .testhub-header{background:linear-gradient(135deg,rgba(56,189,248,0.1),rgba(99,102,241,0.1));border:1px solid rgba(56,189,248,0.25);border-radius:12px;padding:1.4rem;margin-bottom:1.5rem;}
  .testhub-header h2{font-size:1.25rem;color:var(--accent);margin-bottom:0.4rem;border:none;padding:0;text-transform:none;letter-spacing:normal;}
  .testhub-header p{color:var(--muted);font-size:0.82rem;margin:0;}
  .testhub-stats{display:flex;gap:0.8rem;margin-top:0.8rem;flex-wrap:wrap;}
  .testhub-stat{background:var(--surface2);padding:4px 10px;border-radius:6px;font-size:0.75rem;border:1px solid var(--border);}
  .testhub-stat strong{color:var(--built);}
  .testhub-nav{display:flex;gap:0.4rem;margin-top:1rem;flex-wrap:wrap;}
  .testhub-nav button{background:var(--surface2);color:var(--text);border:1px solid var(--border);border-radius:6px;padding:0.35rem 0.7rem;font-size:0.75rem;cursor:pointer;transition:all 0.15s;}
  .testhub-nav button:hover{color:var(--accent);border-color:var(--accent);background:rgba(56,189,248,0.1);}
  .test-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.2rem;margin-bottom:1.5rem;}
  .test-card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1.2rem;display:flex;flex-direction:column;gap:0.9rem;}
  .test-card.full-width{grid-column:1 / -1;margin-bottom:1.2rem;}
  .test-card-header{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--border);padding-bottom:0.6rem;}
  .test-card-title{font-size:0.92rem;font-weight:700;color:var(--text);display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;}
  .test-card-tag{font-size:0.68rem;padding:2px 6px;border-radius:4px;background:rgba(56,189,248,0.12);color:var(--accent);border:1px solid rgba(56,189,248,0.25);font-weight:normal;}
  .test-form{display:flex;flex-direction:column;gap:0.7rem;}
  .test-form-row{display:grid;grid-template-columns:110px 1fr;gap:0.8rem;align-items:center;}
  .test-label{font-size:0.78rem;color:var(--muted);}
  .test-input,.test-select{background:var(--bg);border:1px solid var(--border);color:var(--text);padding:0.4rem 0.6rem;border-radius:6px;font-size:0.8rem;font-family:inherit;width:100%;}
  .test-input:focus,.test-select:focus{outline:none;border-color:var(--accent);}
  .test-btn-group{display:flex;gap:0.4rem;flex-wrap:wrap;margin-top:0.2rem;}
  .test-btn{background:var(--surface2);color:var(--text);border:1px solid var(--border);border-radius:6px;padding:0.45rem 0.8rem;font-size:0.78rem;font-weight:600;cursor:pointer;transition:all 0.15s;display:inline-flex;align-items:center;gap:0.4rem;}
  .test-btn:hover{background:var(--border);color:var(--accent);}
  .test-btn-sm{padding:0.25rem 0.55rem;font-size:0.72rem;}
  .test-btn-primary{background:#0284c7;color:#fff;border-color:#0369a1;}
  .test-btn-primary:hover{background:#0ea5e9;color:#fff;}
  .test-btn-success{background:rgba(34,197,94,0.15);color:var(--built);border-color:rgba(34,197,94,0.3);}
  .test-btn-success:hover{background:rgba(34,197,94,0.25);}
  .test-btn-warning{background:rgba(245,158,11,0.15);color:var(--partial);border-color:rgba(245,158,11,0.3);}
  .test-btn-danger{background:rgba(239,68,68,0.15);color:#ef4444;border-color:rgba(239,68,68,0.3);}
  .test-output{background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:0.8rem;font-size:0.8rem;}
  .test-output-header{font-size:0.72rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--muted);margin-bottom:0.4rem;display:flex;justify-content:space-between;align-items:center;}
  .test-json{font-family:'Fira Code',monospace;font-size:0.72rem;color:#a5b4fc;overflow-x:auto;white-space:pre-wrap;background:rgba(0,0,0,0.3);padding:0.6rem;border-radius:6px;border:1px solid rgba(255,255,255,0.05);margin:0;}
  .sim-modal-overlay{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.75);backdrop-filter:blur(4px);z-index:9999;align-items:center;justify-content:center;padding:1rem;}
  .sim-modal-overlay.open{display:flex;}
  .sim-modal{background:var(--surface);border:1px solid var(--border);border-radius:12px;max-width:680px;width:100%;max-height:90vh;overflow-y:auto;padding:1.5rem;position:relative;box-shadow:0 20px 25px -5px rgba(0,0,0,0.5);}
  .sim-modal-close{position:absolute;top:1rem;right:1rem;background:transparent;border:none;color:var(--muted);font-size:1.4rem;cursor:pointer;}
  .sim-modal-close:hover{color:var(--text);}
  @media(max-width:700px){.principles,.packages,.stack-grid,.test-grid{grid-template-columns:1fr;}.layers{grid-template-columns:1fr;}.test-form-row{grid-template-columns:1fr;gap:0.3rem;}}
"""

JS = """
function switchTab(name) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  const btn = document.querySelector('[onclick="switchTab(\\'' + name + '\\')"]');
  if (btn) btn.classList.add('active');
  const panel = document.getElementById('tab-' + name);
  if (panel) panel.classList.add('active');
}

function scrollToTestModule(id) {
  switchTab('testhub');
  const el = document.getElementById('test-module-' + id);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    el.style.boxShadow = '0 0 15px rgba(56, 189, 248, 0.4)';
    setTimeout(() => { el.style.boxShadow = ''; }, 1600);
  }
}

// ----------------------------------------------------
// Track 1: Trial & Subscription Paywall Simulator
// ----------------------------------------------------
const trialState = {
  tier: 'trial_14',
  daysRemaining: 14,
  isExpired: false
};

function updateTrialBannerPreview() {
  const select = document.getElementById('trial-sim-tier');
  const val = select ? select.value : 'trial_14';
  const container = document.getElementById('trial-banner-preview');
  const badgeEl = document.getElementById('trial-banner-badge');
  if (!container) return;

  if (val === 'trial_14') {
    trialState.tier = 'free_trial';
    trialState.daysRemaining = 14;
    trialState.isExpired = false;
    container.style.background = 'rgba(56, 189, 248, 0.12)';
    container.style.border = '1px solid rgba(56, 189, 248, 0.3)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:var(--accent);">⭐ 14-Day Free Trial Active</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">14 days remaining. Explore all deterministic CAPS practice questions and worked solutions.</div>
        </div>
        <button class="test-btn test-btn-sm test-btn-primary" onclick="openSubscriptionModalPreview()">Upgrade Now</button>
      </div>`;
    badgeEl.className = 'status-badge status-built';
    badgeEl.innerText = 'Active Trial';
  } else if (val === 'trial_3') {
    trialState.tier = 'free_trial';
    trialState.daysRemaining = 3;
    trialState.isExpired = false;
    container.style.background = 'rgba(245, 158, 11, 0.12)';
    container.style.border = '1px solid rgba(245, 158, 11, 0.3)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:var(--partial);">⏳ 3 Days Left of Free Trial</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">Save your mastery pins and streak. Unlock unlimited practice exams for R149/mo.</div>
        </div>
        <button class="test-btn test-btn-sm test-btn-warning" onclick="openSubscriptionModalPreview()">Keep My Access</button>
      </div>`;
    badgeEl.className = 'status-badge status-partial';
    badgeEl.innerText = 'Ending Soon';
  } else if (val === 'trial_1') {
    trialState.tier = 'free_trial';
    trialState.daysRemaining = 1;
    trialState.isExpired = false;
    container.style.background = 'rgba(239, 68, 68, 0.15)';
    container.style.border = '1px solid rgba(239, 68, 68, 0.35)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:#ef4444;">🚨 Final Day of Free Trial!</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">Your trial expires in 12 hours. Homework and practice access will be locked.</div>
        </div>
        <button class="test-btn test-btn-sm test-btn-danger" onclick="openSubscriptionModalPreview()">Unlock Unlimited</button>
      </div>`;
    badgeEl.className = 'status-badge status-partial';
    badgeEl.innerText = 'Critical 1d';
  } else if (val === 'trial_expired') {
    trialState.tier = 'trial_expired';
    trialState.daysRemaining = 0;
    trialState.isExpired = true;
    container.style.background = 'rgba(239, 68, 68, 0.2)';
    container.style.border = '1px solid rgba(239, 68, 68, 0.5)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:#ef4444;">🔒 Free Trial Expired</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">Homework questions are locked. Your profile and mastery records are safely preserved.</div>
        </div>
        <button class="test-btn test-btn-sm test-btn-danger" onclick="openSubscriptionModalPreview()">Reactivate Access</button>
      </div>`;
    badgeEl.className = 'status-badge status-deferred';
    badgeEl.innerText = 'Paywall Locked';
  } else if (val === 'standard') {
    trialState.tier = 'standard';
    trialState.daysRemaining = 365;
    trialState.isExpired = false;
    container.style.background = 'rgba(34, 197, 94, 0.12)';
    container.style.border = '1px solid rgba(34, 197, 94, 0.3)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:var(--built);">✅ Standard Active (R149/mo)</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">Unlimited deterministic question generation & 3-tier pre-baked hints.</div>
        </div>
        <button class="test-btn test-btn-sm" onclick="mockUpgradeToPro()">Upgrade to Pro</button>
      </div>`;
    badgeEl.className = 'status-badge status-built';
    badgeEl.innerText = 'Subscribed';
  } else if (val === 'pro') {
    trialState.tier = 'pro';
    trialState.daysRemaining = 365;
    trialState.isExpired = false;
    container.style.background = 'rgba(99, 102, 241, 0.15)';
    container.style.border = '1px solid rgba(99, 102, 241, 0.35)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:#818cf8;">👑 Pro Tutor Active (R249/mo)</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">All Standard features + Live Socratic Tutor + PDF Diagnostic Reports.</div>
        </div>
        <span class="status-badge status-built">Full Access</span>
      </div>`;
    badgeEl.className = 'status-badge status-built';
    badgeEl.innerText = 'Pro Tier';
  } else if (val === 'school') {
    trialState.tier = 'school';
    trialState.daysRemaining = 365;
    trialState.isExpired = false;
    container.style.background = 'rgba(56, 189, 248, 0.15)';
    container.style.border = '1px solid rgba(56, 189, 248, 0.35)';
    container.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <span style="font-weight:700;color:var(--accent);">🏫 School Institutional License</span>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">Teacher LMS Cockpit, Class Heatmaps, Printable Assessments.</div>
        </div>
        <span class="status-badge status-built">Campus License</span>
      </div>`;
    badgeEl.className = 'status-badge status-built';
    badgeEl.innerText = 'School Tier';
  }
}

function simulateCheckTrialAccess() {
  const studentId = document.getElementById('trial-student-id').value;
  const action = document.getElementById('trial-action-test').value;
  const jsonPre = document.getElementById('trial-json-result');
  const statusEl = document.getElementById('trial-http-status');
  
  let allowed = true;
  let reason = 'Action permitted under active ' + trialState.tier + ' tier';
  let httpStatus = 'HTTP 200 OK';

  if (trialState.isExpired) {
    allowed = false;
    reason = 'Free trial expired. Subscription required to perform ' + action;
    httpStatus = 'HTTP 403 Forbidden (TRIAL_EXPIRED)';
  } else if (action === 'ask_tutor' && trialState.tier === 'standard') {
    allowed = false;
    reason = 'Live Socratic Tutor requires Pro subscription tier';
    httpStatus = 'HTTP 403 Forbidden (UPGRADE_TO_PRO)';
  } else if (action === 'view_class_heatmap' && trialState.tier !== 'school') {
    allowed = false;
    reason = 'Teacher class heatmap requires School or Teacher LMS role';
    httpStatus = 'HTTP 403 Forbidden (SCHOOL_LICENSE_REQUIRED)';
  }

  statusEl.innerText = httpStatus;
  statusEl.style.color = allowed ? 'var(--built)' : '#ef4444';

  const responsePayload = {
    endpoint: '/api/trial/check-access',
    student_id: studentId,
    action: action,
    tier: trialState.tier,
    days_remaining: trialState.daysRemaining,
    allowed: allowed,
    reason: reason,
    timestamp: new Date().toISOString()
  };

  jsonPre.innerText = JSON.stringify(responsePayload, null, 2);
}

function openSubscriptionModalPreview() {
  const modal = document.getElementById('sub-modal-sim');
  if (modal) modal.classList.add('open');
}

function closeSubscriptionModalPreview() {
  const modal = document.getElementById('sub-modal-sim');
  if (modal) modal.classList.remove('open');
}

function mockCompleteUpgrade(tier) {
  closeSubscriptionModalPreview();
  const select = document.getElementById('trial-sim-tier');
  if (select) {
    select.value = tier;
    updateTrialBannerPreview();
    simulateCheckTrialAccess();
  }
  alert('✨ Simulated Checkout Complete! Student upgraded to ' + tier.toUpperCase() + '.');
}

function mockUpgradeToPro() {
  mockCompleteUpgrade('pro');
}

// ----------------------------------------------------
// Track 2: South African Load-Shedding & Offline PWA Simulator
// ----------------------------------------------------
let isOnlineSim = true;
const offlineQueue = [];

function toggleNetworkSimulation() {
  isOnlineSim = !isOnlineSim;
  const btn = document.getElementById('pwa-toggle-net-btn');
  const badgeContainer = document.getElementById('pwa-badge-preview');
  const badgeStatus = document.getElementById('pwa-badge-status');

  if (isOnlineSim) {
    btn.className = 'test-btn test-btn-warning';
    btn.innerHTML = '🔴 Cut Power (Simulate Stage 6 Load-Shedding)';
    badgeStatus.innerText = 'Online';
    badgeStatus.style.color = 'var(--built)';
    badgeContainer.innerHTML = `
      <div style="width:10px;height:10px;border-radius:50%;background:var(--built);box-shadow:0 0 8px var(--built);"></div>
      <div>
        <strong style="font-size:0.8rem;color:var(--built);">Grid Power Online (Sync Active)</strong>
        <div style="font-size:0.72rem;color:var(--muted)">Background telemetry flush active. Auto-synced with Firestore.</div>
      </div>`;
    // If items in queue, auto-flush
    if (offlineQueue.length > 0) {
      setTimeout(flushOfflineQueue, 600);
    }
  } else {
    btn.className = 'test-btn test-btn-success';
    btn.innerHTML = '🟢 Restore Power (Simulate Eskom Grid Online)';
    badgeStatus.innerText = 'Offline';
    badgeStatus.style.color = 'var(--partial)';
    badgeContainer.innerHTML = `
      <div style="width:10px;height:10px;border-radius:50%;background:var(--partial);box-shadow:0 0 8px var(--partial);"></div>
      <div>
        <strong style="font-size:0.8rem;color:var(--partial);">Offline Mode (Load-Shedding Active)</strong>
        <div style="font-size:0.72rem;color:var(--muted)">No internet required. Workbox precache active. Answers stored in <code>localStorage</code>.</div>
      </div>`;
  }
}

function updateQueueDisplay() {
  const list = document.getElementById('pwa-queue-list');
  const count = document.getElementById('pwa-queue-count');
  if (!list || !count) return;

  count.innerText = offlineQueue.length + ' Items Pending';
  if (offlineQueue.length === 0) {
    list.innerHTML = '<span style="color:var(--muted)">No actions pending in offline buffer.</span>';
    return;
  }

  list.innerHTML = offlineQueue.map((item, idx) => `
    <div style="padding:3px 0;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;">
      <span>[#${idx+1}] <strong>${item.type}</strong>: ${item.data}</span>
      <span style="color:var(--partial)">Queued locally</span>
    </div>
  `).join('');
}

function queueOfflineAction() {
  const type = document.getElementById('pwa-action-type').value;
  const data = document.getElementById('pwa-action-data').value;
  
  offlineQueue.push({
    id: 'act_' + Date.now(),
    type: type,
    data: data,
    timestamp: new Date().toLocaleTimeString(),
    status: isOnlineSim ? 'synced' : 'pending'
  });

  updateQueueDisplay();
  if (isOnlineSim) {
    alert('Action logged directly to backend (Network is Online).');
  } else {
    alert('Action saved locally to localStorage (telemetryBuffer.js). Will auto-sync when power/network returns.');
  }
}

function flushOfflineQueue() {
  if (offlineQueue.length === 0) {
    alert('Offline queue is already empty.');
    return;
  }
  const count = offlineQueue.length;
  offlineQueue.length = 0;
  updateQueueDisplay();
  alert('🔄 Flushed ' + count + ' queued telemetry items to POST /api/session/action. Sync complete!');
}

function clearOfflineQueue() {
  offlineQueue.length = 0;
  updateQueueDisplay();
}

// ----------------------------------------------------
// Track 3: Teacher LMS Cockpit & Class Join Codes
// ----------------------------------------------------
let activeJoinCode = 'ACC9B2';
const CODE_CHARS = '23456789ABCDEFGHJKMNPQRSTUVWXYZ';

function generateRandomJoinCode() {
  let result = '';
  for (let i = 0; i < 6; i++) {
    result += CODE_CHARS.charAt(Math.floor(Math.random() * CODE_CHARS.length));
  }
  return result;
}

function simulateCreateClass() {
  const teacherId = document.getElementById('lms-teacher-id').value;
  const className = document.getElementById('lms-class-name').value;
  const grade = document.getElementById('lms-grade').value;
  const subject = document.getElementById('lms-subject').value;

  activeJoinCode = generateRandomJoinCode();
  document.getElementById('lms-active-code').innerText = activeJoinCode;
  document.getElementById('lms-student-code-input').value = activeJoinCode;

  alert('Class created successfully!\\nJoin code: ' + activeJoinCode + '\\nTeacher: ' + teacherId);
}

function copyClassCode() {
  navigator.clipboard.writeText(activeJoinCode).then(() => {
    alert('Join code ' + activeJoinCode + ' copied to clipboard!');
  }).catch(() => {
    alert('Join code: ' + activeJoinCode);
  });
}

function copyWhatsAppShare() {
  const className = document.getElementById('lms-class-name').value;
  const msg = '📚 Fundile Classroom Invite\\n\\nJoin our ' + className + ' class on Fundile!\\n1. Open https://app.fundile.co.za/join\\n2. Enter Class Code: ' + activeJoinCode + '\\n\\n100% CAPS aligned exam preparation & instant feedback.';
  navigator.clipboard.writeText(msg).then(() => {
    alert('WhatsApp classroom invite copied to clipboard! Ready to paste into teacher/parent WhatsApp group.');
  }).catch(() => {
    alert(msg);
  });
}

function simulateJoinClass() {
  const code = document.getElementById('lms-student-code-input').value.trim().toUpperCase();
  const name = document.getElementById('lms-student-name').value.trim();
  const id = document.getElementById('lms-student-id').value.trim();
  const tbody = document.getElementById('lms-roster-tbody');
  const countEl = document.getElementById('lms-roster-count');

  if (code !== activeJoinCode) {
    alert('❌ Invalid or expired join code. Expected ' + activeJoinCode);
    return;
  }
  if (!name) {
    alert('Please enter student name.');
    return;
  }

  const tr = document.createElement('tr');
  tr.innerHTML = `<td>${name}</td><td class="mono">${id}</td><td class="muted">Just now</td><td><span class="status-badge status-built">Enrolled</span></td>`;
  tbody.insertBefore(tr, tbody.firstChild);

  const currentCount = tbody.children.length;
  countEl.innerText = currentCount;

  alert('🎉 Student ' + name + ' enrolled successfully into class roster!');
}

// ----------------------------------------------------
// Option 4: Euclidean Geometry Interactive SVG Renderer
// ----------------------------------------------------
function renderGeometryTheorem() {
  const sel = document.getElementById('geom-theorem-select');
  const val = sel ? sel.value : 'tan_chord';
  const canvas = document.getElementById('geom-svg-canvas');
  const tbody = document.getElementById('geom-proof-tbody');
  if (!canvas || !tbody) return;

  if (val === 'tan_chord') {
    canvas.innerHTML = `
      <svg width="280" height="200" viewBox="0 0 280 200" style="max-width:100%;">
        <!-- Circle -->
        <circle cx="140" cy="100" r="70" stroke="#38bdf8" stroke-width="2" fill="none"/>
        <circle cx="140" cy="100" r="3" fill="#38bdf8"/>
        <text x="145" y="95" fill="#8892b0" font-size="10">O</text>
        <!-- Tangent Line at A -->
        <line x1="30" y1="170" x2="250" y2="170" stroke="#f59e0b" stroke-width="2"/>
        <text x="35" y="165" fill="#f59e0b" font-size="10">T</text>
        <text x="240" y="165" fill="#f59e0b" font-size="10">S</text>
        <!-- Triangle in Circle ABC -->
        <polygon points="140,170 85,60 195,60" stroke="#22c55e" stroke-width="2" fill="rgba(34,197,94,0.08)"/>
        <!-- Vertices -->
        <text x="135" y="185" fill="#e2e8f0" font-size="11" font-weight="bold">A</text>
        <text x="70" y="55" fill="#e2e8f0" font-size="11" font-weight="bold">B</text>
        <text x="200" y="55" fill="#e2e8f0" font-size="11" font-weight="bold">C</text>
        <!-- Angle Arc at A (tangent chord) -->
        <path d="M 140,170 L 110,170 A 30,30 0 0,1 120,140 Z" fill="rgba(245,158,11,0.3)"/>
        <!-- Angle Arc at C -->
        <path d="M 195,60 L 175,60 A 20,20 0 0,1 180,80 Z" fill="rgba(245,158,11,0.3)"/>
      </svg>
      <div style="font-size:0.75rem;color:var(--accent);margin-top:4px;">
        Theorem: Angle between tangent <em>TAS</em> and chord <em>AB</em> equals angle subtended in alternate segment (&ang;BCA).
      </div>
    `;
    tbody.innerHTML = `
      <tr><td>Draw diameter AD and join DC</td><td class="mono">Construction</td><td>[✓ M1]</td></tr>
      <tr><td>&ang;TAD = 90&deg;</td><td class="mono">rad &perp; tangent</td><td>[✓ A1]</td></tr>
      <tr><td>&ang;ACD = 90&deg;</td><td class="mono">&ang; in semi-circle</td><td>[✓ A1]</td></tr>
      <tr><td>&ang;TAB = &ang;BCA</td><td class="mono">tan chord thm</td><td>[✓ A1]</td></tr>
    `;
  } else if (val === 'centre_circum') {
    canvas.innerHTML = `
      <svg width="280" height="200" viewBox="0 0 280 200" style="max-width:100%;">
        <circle cx="140" cy="100" r="70" stroke="#38bdf8" stroke-width="2" fill="none"/>
        <circle cx="140" cy="100" r="3" fill="#38bdf8"/>
        <text x="145" y="105" fill="#38bdf8" font-size="10">O</text>
        <!-- Subtended from A and B to O and C -->
        <line x1="85" y1="145" x2="140" y2="100" stroke="#f59e0b" stroke-width="2"/>
        <line x1="195" y1="145" x2="140" y2="100" stroke="#f59e0b" stroke-width="2"/>
        <line x1="85" y1="145" x2="140" y2="30" stroke="#22c55e" stroke-width="2"/>
        <line x1="195" y1="145" x2="140" y2="30" stroke="#22c55e" stroke-width="2"/>
        <text x="75" y="155" fill="#e2e8f0" font-size="11" font-weight="bold">A</text>
        <text x="200" y="155" fill="#e2e8f0" font-size="11" font-weight="bold">B</text>
        <text x="135" y="25" fill="#e2e8f0" font-size="11" font-weight="bold">C</text>
      </svg>
      <div style="font-size:0.75rem;color:var(--accent);margin-top:4px;">
        Theorem: Angle subtended by arc AB at center O is double angle at circumference C (&ang;AOB = 2&ang;ACB).
      </div>
    `;
    tbody.innerHTML = `
      <tr><td>Join CO and produce to P</td><td class="mono">Construction</td><td>[✓ M1]</td></tr>
      <tr><td>OA = OC (radii) &rarr; &ang;A = &ang;C<sub>1</sub></td><td class="mono">&ang;s opp equal sides</td><td>[✓ A1]</td></tr>
      <tr><td>&ang;AOP = &ang;A + &ang;C<sub>1</sub> = 2&ang;C<sub>1</sub></td><td class="mono">ext &ang; of &Delta;</td><td>[✓ A1]</td></tr>
      <tr><td>&ang;AOB = 2 &ang;ACB</td><td class="mono">&ang; at centre = 2 &ang; at circ</td><td>[✓ A1]</td></tr>
    `;
  } else if (val === 'cyclic_quad') {
    canvas.innerHTML = `
      <svg width="280" height="200" viewBox="0 0 280 200" style="max-width:100%;">
        <circle cx="140" cy="100" r="70" stroke="#38bdf8" stroke-width="2" fill="none"/>
        <polygon points="110,35 195,65 170,160 80,140" stroke="#818cf8" stroke-width="2" fill="rgba(99,102,241,0.08)"/>
        <text x="105" y="28" fill="#e2e8f0" font-size="11" font-weight="bold">A</text>
        <text x="202" y="68" fill="#e2e8f0" font-size="11" font-weight="bold">B</text>
        <text x="175" y="175" fill="#e2e8f0" font-size="11" font-weight="bold">C</text>
        <text x="68" y="145" fill="#e2e8f0" font-size="11" font-weight="bold">D</text>
      </svg>
      <div style="font-size:0.75rem;color:var(--accent);margin-top:4px;">
        Theorem: Opposite angles of cyclic quad are supplementary (&ang;B + &ang;D = 180&deg;).
      </div>
    `;
    tbody.innerHTML = `
      <tr><td>Join OB and OD</td><td class="mono">Construction</td><td>[✓ M1]</td></tr>
      <tr><td>&ang;O<sub>1</sub> = 2&ang;A</td><td class="mono">&ang; at centre = 2 &ang; at circ</td><td>[✓ A1]</td></tr>
      <tr><td>&ang;O<sub>2</sub> = 2&ang;C</td><td class="mono">&ang; at centre = 2 &ang; at circ</td><td>[✓ A1]</td></tr>
      <tr><td>&ang;O<sub>1</sub> + &ang;O<sub>2</sub> = 360&deg;</td><td class="mono">&ang;s round a point</td><td>[✓ M1]</td></tr>
      <tr><td>&ang;B + &ang;D = 180&deg;</td><td class="mono">opp &ang;s cyclic quad</td><td>[✓ A1]</td></tr>
    `;
  }
}

// ----------------------------------------------------
// Option 3: Post-Exam Triage Report Simulator
// ----------------------------------------------------
function updateTriageReport() {
  const score = parseInt(document.getElementById('triage-score-slider').value);
  const box = document.getElementById('triage-report-box');
  if (!box) return;

  const marksLost = 100 - score;
  const netVsGross = Math.round(marksLost * 0.45);
  const debitCredit = Math.round(marksLost * 0.35);
  const omittedBal = marksLost - netVsGross - debitCredit;

  box.innerHTML = `
    <div style="display:flex;justify-content:space-between;margin-bottom:0.6rem;">
      <strong>Post-Mortem Diagnostic Breakdown</strong>
      <span style="color:var(--partial);">Marks Lost: ${marksLost} / 100</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:0.4rem;">
      <div style="display:flex;justify-content:space-between;padding:4px 8px;background:rgba(239,68,68,0.1);border-radius:4px;border:1px solid rgba(239,68,68,0.2);">
        <span>🏷️ <code>net_vs_gross_confusion</code> (VAT calculation error in CRJ)</span>
        <strong style="color:#ef4444;">-${netVsGross} marks</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:4px 8px;background:rgba(245,158,11,0.1);border-radius:4px;border:1px solid rgba(245,158,11,0.2);">
        <span>🏷️ <code>debit_credit_inversion</code> (Reversed Bank and Sales in Ledger)</span>
        <strong style="color:var(--partial);">-${debitCredit} marks</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:4px 8px;background:rgba(100,116,139,0.1);border-radius:4px;border:1px solid rgba(100,116,139,0.2);">
        <span>🏷️ <code>omitted_balance_b_d</code> (Missing opening balance)</span>
        <strong style="color:var(--muted);">-${omittedBal} marks</strong>
      </div>
    </div>
  `;
}

function copyParentWhatsAppReport() {
  const score = document.getElementById('triage-score-slider').value;
  const msg = '📊 Fundile Academic Progress Update\\n\\nLearner: Thabo Ndlovu\\nSubject: Grade 10 Accounting\\nRecent Exam Score: ' + score + '%\\n\\nKey Focus Area: VAT Net vs Gross Calculation (8 marks lost).\\nRecommended: 5-Minute Targeted Micro-Drill.\\n\\nView full diagnostic report: https://app.fundile.co.za/reports/std_thabo_01';
  navigator.clipboard.writeText(msg).then(() => {
    alert('Parent WhatsApp digest copied to clipboard!');
  }).catch(() => {
    alert(msg);
  });
}

// ----------------------------------------------------
// Layer B: SimuLearn Step Player Simulator
// ----------------------------------------------------
let simStep = 1;
const simSteps = [
  {
    step: 1,
    text: "Transaction: Sold merchandise for cash to K. Naidoo, R5,750 (VAT 15% inclusive). Cost of Sales R3,800.",
    analysis: "-", bank: "-", sales: "-", cos: "-"
  },
  {
    step: 2,
    text: "Step 2: Enter Receipt 001 in Analysis of Receipts (gross amount R5,750 received at till).",
    analysis: "R5 750", bank: "-", sales: "-", cos: "-"
  },
  {
    step: 3,
    text: "Step 3: End of day banking: Deposit R5,750 into Bank column. Split Net Sales (R5,000) and Output VAT (R750).",
    analysis: "R5 750", bank: "R5 750", sales: "R5 000", cos: "-"
  },
  {
    step: 4,
    text: "Step 4: Record Cost of Sales R3,800 in the memorandum Cost of Sales column for perpetual inventory tracking.",
    analysis: "R5 750", bank: "R5 750", sales: "R5 000", cos: "R3 800"
  }
];

function updateSimUI() {
  const current = simSteps[simStep - 1];
  document.getElementById('sim-step-badge').innerText = 'Step ' + current.step + ' of 4';
  document.getElementById('sim-step-text').innerText = current.text;
  document.getElementById('sim-c-analysis').innerText = current.analysis;
  document.getElementById('sim-c-bank').innerText = current.bank;
  document.getElementById('sim-c-sales').innerText = current.sales;
  document.getElementById('sim-c-cos').innerText = current.cos;

  // Highlight active cell
  ['analysis','bank','sales','cos'].forEach(k => {
    const el = document.getElementById('sim-c-' + k);
    if (el) el.style.background = 'transparent';
  });
  if (simStep === 2) document.getElementById('sim-c-analysis').style.background = 'rgba(56,189,248,0.2)';
  if (simStep === 3) {
    document.getElementById('sim-c-bank').style.background = 'rgba(34,197,94,0.2)';
    document.getElementById('sim-c-sales').style.background = 'rgba(34,197,94,0.2)';
  }
  if (simStep === 4) document.getElementById('sim-c-cos').style.background = 'rgba(245,158,11,0.2)';
}

function stepSimuLearn(delta) {
  simStep += delta;
  if (simStep < 1) simStep = 1;
  if (simStep > 4) simStep = 4;
  updateSimUI();
}

function resetSimuLearn() {
  simStep = 1;
  updateSimUI();
}

// ----------------------------------------------------
// Layer E: Gamification Simulator
// ----------------------------------------------------
let currentXP = 350;
let currentLevel = 3;

function addGamificationXP(amount) {
  currentXP += amount;
  if (currentXP >= 500) {
    currentLevel += 1;
    currentXP = currentXP - 500;
    document.getElementById('badge-trophy-status').innerText = '🏆 UNLOCKED!';
    document.getElementById('badge-trophy-status').style.color = 'var(--built)';
    alert('🎉 LEVEL UP! Reached Level ' + currentLevel + ' and unlocked Term Trophy!');
  }
  document.getElementById('game-level').innerText = currentLevel;
  document.getElementById('game-xp-text').innerText = currentXP + ' / 500 XP';
  document.getElementById('game-xp-bar').style.width = ((currentXP / 500) * 100) + '%';
}

// ----------------------------------------------------
// Layer A: Deterministic Generator Sandbox
// ----------------------------------------------------
const genQuestions = {
  acc10: {
    question: "Calculate the Output VAT (15%) included in a total cash receipt of R13,800.",
    h1: "Location: CRJ Column 4 (VAT Output / Sales split).",
    h2: "Conceptual Rule: Inclusive VAT formula is Amount × 15 / 115.",
    h3: "Calculation: R13,800 × 15 / 115 = R1,800 (Net Sales = R12,000)."
  },
  math10: {
    question: "Simplify: cos(30°) · sin(60°) - tan(45°). Leave answer in exact surd form.",
    h1: "Location: Working Pad Line 1 (Special angle exact values).",
    h2: "Conceptual Rule: cos(30°) = √3/2, sin(60°) = √3/2, tan(45°) = 1.",
    h3: "Calculation: (√3/2)(√3/2) - 1 = 3/4 - 1 = -1/4."
  },
  bs10: {
    question: "Identify the market environment component affected when a direct competitor slashes prices by 20%.",
    h1: "Location: Environmental Scan Rubric (Micro vs Market vs Macro).",
    h2: "Conceptual Rule: Competitors, customers, suppliers, intermediaries operate in Market Environment.",
    h3: "Rubric Match: Market Environment — specifically Competitors."
  },
  ems8: {
    question: "Which source document is issued when receiving cash from a customer for services rendered?",
    h1: "Location: Source Documents Identification table.",
    h2: "Conceptual Rule: Cash received for services = Receipt / Cash Register Tape.",
    h3: "Correct Answer: Duplicate Receipt (Document Number 001)."
  }
};

function runDeterministicGeneratorSandbox() {
  const subj = document.getElementById('gen-subject-select').value;
  const data = genQuestions[subj] || genQuestions['acc10'];
  document.getElementById('gen-preview-box').innerHTML = `
    <strong>Question Statement:</strong>
    <p style="margin:4px 0 0 0;color:var(--text);">${data.question}</p>
  `;
  document.getElementById('gen-hint-box').style.display = 'none';
}

function revealHint(tier) {
  const subj = document.getElementById('gen-subject-select').value;
  const data = genQuestions[subj] || genQuestions['acc10'];
  const box = document.getElementById('gen-hint-box');
  box.style.display = 'block';
  if (tier === 1) box.innerHTML = `<strong>Tier 1 (Nudge):</strong> ${data.h1}`;
  if (tier === 2) box.innerHTML = `<strong>Tier 2 (CAPS Rule):</strong> ${data.h2}`;
  if (tier === 3) box.innerHTML = `<strong>Tier 3 (Calculation):</strong> ${data.h3}`;
}

// ----------------------------------------------------
// Component Matrix Filter
// ----------------------------------------------------
function filterComponentTable() {
  const query = document.getElementById('comp-filter-input').value.toLowerCase();
  document.querySelectorAll('.comp-row').forEach(row => {
    const name = row.getAttribute('data-name') || '';
    const layer = row.getAttribute('data-layer') || '';
    const text = row.innerText.toLowerCase();
    if (text.includes(query) || name.includes(query) || layer.includes(query)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}

// Initialize test hub on page load
window.addEventListener('DOMContentLoaded', () => {
  updateTrialBannerPreview();
  toggleNetworkSimulation();
  renderGeometryTheorem();
  updateTriageReport();
  runDeterministicGeneratorSandbox();
});
"""

def build_html(data: dict) -> str:
    meta = data.get("_meta", {})
    stack = data.get("techStack", {})
    layers = data.get("layers", [])
    services = data.get("backendServices", {})
    routes = data.get("apiRoutes", {})
    generators = data.get("generators", {})
    components = data.get("frontendComponents", {})
    firestore = data.get("firestoreCollections", {})
    packages = data.get("packages", {})
    principles = data.get("designPrinciples", [])
    questions = data.get("openQuestions", [])
    workflow = data.get("_workflow", {})

    tabs = [
        ("testhub",    "🚀 Component & Feature Test Hub"),
        ("services",   "Backend Services"),
        ("routes",     "API Routes"),
        ("generators", "Generators"),
        ("frontend",   "Frontend"),
        ("firestore",  "Firestore"),
        ("stack",      "Tech Stack"),
        ("packages",   "Packages"),
        ("principles", "Principles"),
        ("oq",         "Open Questions"),
        ("workflow",   "Agent Workflow"),
    ]

    tab_buttons = "\\n".join(
        f'<div class="tab{" active" if i==0 else ""}" onclick="switchTab(\\'{key}\\')">{label}</div>'
        for i, (key, label) in enumerate(tabs)
    )

    def panel(key: str, content: str, active: bool = False) -> str:
        cls = "tab-panel active" if active else "tab-panel"
        return f'<div id="tab-{key}" class="{cls}">{content}</div>'

    panels = [
        panel("testhub", build_test_hub(data), active=True),
        panel("services", f"""<section><h2>Backend Services</h2><div class="table-wrap">
          <table><thead><tr><th>Service</th><th>Status</th><th>File</th><th>Responsibility</th></tr></thead>
          <tbody>{build_services_table(services)}</tbody></table></div></section>"""),
        panel("routes", f"""<section><h2>API Routes</h2><div class="table-wrap">
          <table><thead><tr><th>Method</th><th>Route</th><th>Status</th><th>Description</th></tr></thead>
          <tbody>{build_routes_table(routes)}</tbody></table></div></section>"""),
        panel("generators", f"""<section><h2>Question Generators</h2>
          <div class="gen-grid">{build_generators(generators)}</div></section>"""),
        panel("frontend", f"""<section><h2>Frontend Components</h2><div class="table-wrap">
          <table><thead><tr><th>Component</th><th>Status</th><th>Layer</th><th>Notes</th></tr></thead>
          <tbody>{build_frontend_table(components)}</tbody></table></div></section>"""),
        panel("firestore", f"""<section><h2>Firestore Collections</h2><div class="table-wrap">
          <table><thead><tr><th>Collection</th><th>Status</th><th>Description</th></tr></thead>
          <tbody>{build_firestore_table(firestore)}</tbody></table></div></section>"""),
        panel("stack", f"""<section><h2>Tech Stack</h2>
          <div class="stack-grid">{build_stack(stack)}</div></section>"""),
        panel("packages", f"""<section><h2>Package Tiers</h2>
          <div class="packages">{build_packages(packages)}</div></section>"""),
        panel("principles", f"""<section><h2>Design Principles</h2>
          <div class="principles">{build_principles(principles)}</div></section>"""),
        panel("oq", f"""<section><h2>Open Questions</h2>
          <div class="questions">{build_open_questions(questions)}</div></section>"""),
        panel("workflow", f"""<section><h2>Agent Workflow Protocol</h2>
          {build_workflow_panel(workflow)}</section>"""),
    ]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{h(meta.get("app","Fundile"))} — Architecture Map &amp; Feature Test Hub</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
  <header>
    <h1>&#9889; {h(meta.get("app","Fundile"))} &#8212; Architecture Map &amp; Interactive Test Hub</h1>
    <p>{h(meta.get("tagline",""))}</p>
    <div class="meta">
      <span>v{h(meta.get("version",""))}</span>
      <span>Last updated: {h(meta.get("lastUpdated",""))}</span>
      <span>Source of truth for agents: fundile-architecture.json</span>
      <span>&#9888; Edit JSON only &#8212; this file is generated</span>
    </div>
  </header>

  <div class="legend">
    <div class="legend-item"><div class="dot" style="background:var(--built)"></div> Built</div>
    <div class="legend-item"><div class="dot" style="background:var(--partial)"></div> Partial</div>
    <div class="legend-item"><div class="dot" style="background:var(--planned)"></div> Planned</div>
    <div class="legend-item"><div class="dot" style="background:var(--deferred)"></div> Deferred</div>
  </div>

  <section>
    <h2>System Layers</h2>
    <div class="layers">{build_layers(layers)}</div>
  </section>

  <div class="tabs">{tab_buttons}</div>
  {"".join(panels)}

</div>
<script>{JS}</script>
</body>
</html>"""

def main():
    if not JSON_FILE.exists():
        print(f"ERROR: {JSON_FILE} not found. Run from project root.", file=sys.stderr)
        sys.exit(1)
    data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    html = build_html(data)
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"Generated: {HTML_FILE}  ({HTML_FILE.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    main()
'''

TARGET.write_text(content, encoding="utf-8")
print(f"Updated: {TARGET} (lines: {len(content.splitlines())})")
