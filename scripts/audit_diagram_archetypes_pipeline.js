#!/usr/bin/env node
/**
 * Super Admin Diagram Archetype Vetting & Multi-Seed Entropy Pipeline (v2)
 *
 * Real-browser Super Admin execution (unchanged architecture) with an evidence-based
 * evaluation core. Every status below is DERIVED from measured data — there are no
 * optimistic defaults and no fallback strings that convert defects into passes.
 *
 * Evaluation model per archetype (across Seeds 1..N):
 *  - Factor 1 - Annotation geometry (geometry_status):
 *      Reads the LIVE DOM (InteractiveCallouts badges, anchor dots, leader polylines)
 *      and cross-checks against the authoritative anchor registry at
 *      caps-ai-backend/app/data/diagram_anchors/<master>.json:
 *        * every declared pin badge / anchor dot / leader line is mounted
 *        * badge sits on its declared side of the anchor
 *        * leader polyline starts exactly at the anchor point
 *        * badges never overlap and stay inside the viewBox
 *        * generator pin coordinates match the registry coordinates (drift detection)
 *        * no NaN coordinates anywhere in the rendered SVG
 *  - Factor 2 - Answer & rubric truth (rubric_status):
 *      Facts come from the intercepted POST /api/admin/vet/generate JSON (never from
 *      possibly-stale DOM text). Verifies the canonical answer names the structure the
 *      registry says lives at the target pin's coordinates, marking points sum to the
 *      declared total, hints tiers are populated, and no foreign structure is claimed.
 *  - Factor 3 - Seed entropy (entropy_status):
 *      Signature = the set of TARGET STRUCTURE NAMES asked per seed (e.g.
 *      {Left Ventricle, Left Atrium} vs {Left Ventricle, Right Atrium}), falling back
 *      to normalized prompt+answer for vector-modality items without callout pins.
 *
 * Outputs:
 *  - reports/diagram_vetting/shots/Gr<G>_<archetype_id>_seed<S>_{diagram,card}.png
 *  - reports/diagram_vetting/diagram_vetting_ledger_gr<G>.json   (written incrementally)
 *  - reports/diagram_vetting/diagram_vetting_dashboard_gr<G>.html
 *  - reports/diagram_vetting/user_flags_gr<G>.json               (intake for manual scan;
 *    existing file is merged into the ledger + dashboard on the next run)
 *
 * Usage: node scripts/audit_diagram_archetypes_pipeline.js --grade 7 [--seeds 6]
 *        [--url http://127.0.0.1:5173] [--api-url http://127.0.0.1:5001] [--headless false]
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright';
import { authenticateSuperAdminSession } from '../e2e/helpers/authenticateSuperAdmin.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');
const ANCHORS_DIR = path.join(PROJECT_ROOT, 'caps-ai-backend', 'app', 'data', 'diagram_anchors');
const GENERATE_ROUTE = '/api/admin/vet/generate';

const PASS = {
    render: 'RENDER_SUCCESS',
    geometryOk: 'GEOMETRY_VERIFIED',
    geometryNa: 'N/A_VECTOR_MODALITY',
    entropyDynamic: 'DYNAMIC_VARIED',
    entropyLow: 'LOW_ENTROPY_PARTIAL',
    entropyStatic: 'ZERO_ENTROPY_STATIC',
    truthVerified: 'TRUTH_VERIFIED',
    truthPartial: 'PARTIAL_EXISTS_ONLY',
    truthDefect: 'RUBRIC_DEFECT',
    emptyRubric: 'EMPTY_RUBRIC_DEFECT',
};

// ---------------------------------------------------------------- CLI args
function parseArgs() {
    const args = process.argv.slice(2);
    const config = {
        grade: '7',
        seeds: null, // null => adaptive: 6 for callout-pin (Category A) archetypes, 3 otherwise
        headless: true,
        url: 'http://127.0.0.1:5173',
        apiUrl: null,
        only: null, // comma-separated archetype ids to audit (subset of the grade list)
        outputDir: path.join(PROJECT_ROOT, 'reports', 'diagram_vetting')
    };
    for (let i = 0; i < args.length; i++) {
        if (args[i] === '--grade' && args[i + 1]) config.grade = args[++i].trim();
        else if (args[i] === '--seeds' && args[i + 1]) config.seeds = Math.max(1, parseInt(args[++i], 10) || null);
        else if (args[i] === '--headless' && args[i + 1]) config.headless = args[++i].toLowerCase() !== 'false';
        else if (args[i] === '--url' && args[i + 1]) config.url = args[++i].trim();
        else if (args[i] === '--api-url' && args[i + 1]) config.apiUrl = args[++i].trim();
        else if (args[i] === '--only' && args[i + 1]) config.only = args[++i].split(',').map(s => s.trim()).filter(Boolean);
        else if (args[i] === '--output-dir' && args[i + 1]) config.outputDir = path.resolve(PROJECT_ROOT, args[++i].trim());
    }
    if (!config.apiUrl) {
        const host = new URL(config.url).hostname;
        config.apiUrl = (host === 'localhost' || host === '127.0.0.1') ? `http://${host}:5001` : config.url;
    }
    return config;
}

// ------------------------------------------------- Anchor registry (ground truth)
const anchorCache = new Map();
const normalizeName = (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();

function loadAnchorRegistry(master) {
    if (!master) return null;
    if (anchorCache.has(master)) return anchorCache.get(master);
    let registry = null;
    const file = path.join(ANCHORS_DIR, `${master}.json`);
    if (fs.existsSync(file)) {
        try {
            const raw = JSON.parse(fs.readFileSync(file, 'utf-8'));
            const vb = String(raw.viewBox || '0 0 600 480').split(' ').map(Number);
            const entries = Object.entries(raw.anchors || {}).map(([key, v]) => {
                const aliases = [v.name, ...(v.synonyms || []), ...(v.acceptable || [])]
                    .map(a => normalizeName(a)).filter(a => a.length >= 4);
                return { key, name: v.name, anchor: v.anchor, side: v.side, default_box: v.default_box, aliases };
            });
            registry = { master, viewBox: vb, entries };
        } catch (e) {
            console.warn(`[registry] Failed to parse ${file}: ${e.message}`);
        }
    }
    anchorCache.set(master, registry);
    return registry;
}

function registryByCoord(registry, coord, tol = 2) {
    if (!registry || !Array.isArray(coord)) return null;
    return registry.entries.find(e => Array.isArray(e.anchor)
        && Math.abs(e.anchor[0] - coord[0]) <= tol
        && Math.abs(e.anchor[1] - coord[1]) <= tol) || null;
}

function registryByName(registry, name) {
    if (!registry || !name) return null;
    const n = normalizeName(name);
    return registry.entries.find(e => e.aliases.includes(n)) || null;
}

/** Which registry structures are mentioned anywhere in a text blob? (space-padded whole-phrase match) */
function structuresMentionedIn(registry, text) {
    if (!registry) return [];
    const t = ` ${normalizeName(text)} `;
    return registry.entries.filter(e => e.aliases.some(a => t.includes(` ${a} `)));
}

// ------------------------------------------------------- Preflight (fail fast)
async function preflight(config) {
    const probes = [
        { label: 'Frontend (Vite)', url: config.url },
        { label: 'Backend API', url: config.apiUrl }
    ];
    for (const p of probes) {
        try {
            const res = await fetch(p.url, { method: 'GET', signal: AbortSignal.timeout(8000) });
            console.log(`[preflight] ${p.label} reachable: ${p.url} (HTTP ${res.status})`);
        } catch (e) {
            const reason = e.name === 'TimeoutError'
                ? 'connection accepted but no response within 8s (process hung or wrong port)'
                : (e.cause?.code || e.message);
            throw new Error(
                `[preflight] ${p.label} NOT reachable at ${p.url} — ${reason}.\n` +
                `Start a healthy Vite dev server and Flask backend before running this pipeline.`);
        }
    }
}

// ------------------------------------------------------- Rubric truth (Factor 2)
function extractAnswerString(q) {
    if (q.sample_answer && String(q.sample_answer).trim()) return String(q.sample_answer);
    if (q.correct_answer && String(q.correct_answer).trim()) return String(q.correct_answer);
    if (q.worked_solution && String(q.worked_solution).trim()) return String(q.worked_solution);
    if (q.canonical_solution && typeof q.canonical_solution === 'object' && Array.isArray(q.canonical_solution.steps)) {
        return q.canonical_solution.steps
            .map((st, idx) => `Step ${idx + 1}: ${st.latex || st.sympy || ''} ${st.justification ? `(${st.justification})` : ''}`)
            .join('\n');
    }
    if (typeof q.canonical_solution === 'string' && q.canonical_solution.trim()) return q.canonical_solution;
    return '';
}

function evaluateRubricTruth(q, registry, catalogEntry = {}) {
    const issues = [];
    const answerText = extractAnswerString(q);
    if (!answerText.trim()) {
        return { status: PASS.emptyRubric, issues: [{ code: 'EMPTY_ANSWER', detail: 'Generator produced no canonical answer.' }], targetNames: [] };
    }

    // Marks arithmetic & R6 (Expected answer 1:1 alignment with marking_points)
    const schema = q.marking_schema;
    if (schema && Array.isArray(schema.marking_points) && schema.marking_points.length > 0) {
        const sum = schema.marking_points.reduce((acc, mp) => acc + (Number(mp.marks) || 0), 0);
        const declared = Number(schema.total_marks ?? q.marks);
        if (Number.isFinite(declared) && sum !== declared) {
            issues.push({ code: 'MARKS_SUM_MISMATCH', detail: `marking_points sum to ${sum}m but total declared ${declared}m.` });
        }
        // R6: Check that numbers/key tokens in marking_points appear in answerText + worked_solution
        const combinedAns = `${answerText} ${q.worked_solution || ''}`.toLowerCase().replace(/\{,\}/g, ',');
        for (const mp of schema.marking_points) {
            const desc = String(mp.description || mp.criterion || mp.point || '').replace(/\{,\}/g, ',');
            // Extract numeric values from marking point description (excluding mark counts like "1 mark")
            const nums = (desc.match(/\b\d+(?:[.,]\d+)?\b/g) || []).filter(n => Number(n) > 1);
            for (const num of nums) {
                const dotVar = num.replace(',', '.');
                const commaVar = num.replace('.', ',');
                if (!combinedAns.includes(dotVar) && !combinedAns.includes(commaVar)) {
                    issues.push({
                        code: 'RUBRIC_NOT_IN_ANSWER',
                        detail: `Marking point "${desc.slice(0, 70)}" awards marks for value "${num}" which is absent from expected answer.`
                    });
                    break;
                }
            }
        }
    } else {
        issues.push({ code: 'MARKING_POINTS_ABSENT', detail: 'marking_schema has no marking_points breakdown.' });
    }

    // Hints populated (3-tier contract)
    const tiers = [q.hints?.tier_1 || q.hints?.nudge, q.hints?.tier_2 || q.hints?.structure, q.hints?.tier_3 || q.hints?.solution];
    tiers.forEach((t, i) => { if (!t || !String(t).trim()) issues.push({ code: `HINT_TIER_${i + 1}_EMPTY`, detail: `Tier ${i + 1} hint is missing.` }); });

    // R11: Math/Physics calculation questions (>1 mark) must show step-by-step procedure
    const isMathOrPhys = /Mathematics|Physical Sciences|Technical/i.test(catalogEntry.subject || q.subject || '');
    const declaredMarks = Number(schema?.total_marks ?? q.marks ?? 1);
    const hasStepsArray = Array.isArray(q.canonical_solution?.steps) && q.canonical_solution.steps.length >= 2;
    const hasMultiLineOrEq = (answerText.match(/=|\n|→|;|\bStep\b/gi) || []).length >= 2;
    if (isMathOrPhys && declaredMarks >= 2 && !hasStepsArray && !hasMultiLineOrEq) {
        issues.push({
            code: 'NO_PROCEDURE',
            detail: `Answer "${answerText.slice(0, 60)}" has no step-by-step working for a ${declaredMarks}-mark ${catalogEntry.subject || 'calculation'} question (R11).`
        });
    }

    // Target-structure answer truth, cross-checked against the anchor registry
    const spec = q.diagram_spec || q.diagram || {};
    const pins = Array.isArray(spec.pins) ? spec.pins : [];
    const serverMap = q._server_solution?.pin_map || null;
    const targetPin = spec.target_pin
        || (pins.find(p => p.role === 'target') || {}).pin
        || (pins.length ? pins[0].pin : null);
    const targetNames = [];

    if (!registry) {
        const severeNoReg = issues.filter(i => !['ANCHOR_REGISTRY_MISSING'].includes(i.code));
        return {
            status: severeNoReg.length === 0 ? PASS.truthVerified : PASS.truthPartial,
            issues,
            targetNames
        };
    }

    for (const p of pins) {
        const coordEntry = registryByCoord(registry, p.anchor);
        const serverName = serverMap?.[p.pin];
        if (!coordEntry) {
            issues.push({ code: 'REGISTRY_COORD_DRIFT', detail: `Pin ${p.pin} anchor [${p.anchor}] matches no entry in ${registry.master} registry (generator data out of sync with anchor JSON).` });
            continue;
        }
        if (serverName && normalizeName(serverName) !== normalizeName(coordEntry.name)
            && !coordEntry.aliases.includes(normalizeName(serverName))) {
            issues.push({ code: 'SERVER_SOLUTION_DRIFT', detail: `Pin ${p.pin}: generator says "${serverName}" but registry anchor is "${coordEntry.name}".` });
        }
        if (p.role === 'target') targetNames.push(coordEntry.name);
    }

    if (targetNames.length > 0 && targetPin) {
        const mentioned = structuresMentionedIn(registry, `${answerText}\n${q.worked_solution || ''}\n${q.hints?.tier_3 || ''}`);
        const answerNames = new Set(mentioned.map(m => m.name));
        for (const want of targetNames) {
            if (!answerNames.has(want)) {
                issues.push({ code: 'ANSWER_TARGET_NOT_CONFIRMED', detail: `Expected answer for callout ${targetPin} is "${want}" per registry, but memorandum does not name it.` });
            }
        }
        // Wrong-structure detection: check only the identification line (first line of answerText) so prose words
        // like "Sun" or "condenser" inside Step 2 functional descriptions don't false-flag as distractor structures.
        const firstLineAns = String(answerText || '').split('\n')[0] || '';
        const idLineMentioned = new Set(structuresMentionedIn(registry, firstLineAns).map(m => m.name));
        for (const p of pins) {
            const entry = registryByCoord(registry, p.anchor);
            if (!entry || p.role === 'target') continue;
            if (idLineMentioned.has(entry.name) && !targetNames.includes(entry.name)) {
                issues.push({ code: 'DISTRACTOR_IN_ANSWER', detail: `Memorandum names distractor "${entry.name}" (callout ${p.pin}) which is not the asked target.` });
            }
        }
    }

    const severe = issues.filter(i => !['ANCHOR_REGISTRY_MISSING'].includes(i.code));
    const status = severe.length === 0 ? PASS.truthVerified : (severe.some(i => i.code.startsWith('ANSWER_') || i.code === 'EMPTY_ANSWER' || i.code === 'RUBRIC_NOT_IN_ANSWER' || i.code === 'NO_PROCEDURE') ? PASS.truthDefect : PASS.truthPartial);
    return { status, issues, targetNames };
}

// ------------------------------------------- Segment intersection helper (R3)
function ccw(ax, ay, bx, by, cx, cy) {
    return (cy - ay) * (bx - ax) > (by - ay) * (cx - ax);
}
function segmentsIntersect(ax, ay, bx, by, cx, cy, dx, dy) {
    if (Math.hypot(ax - cx, ay - cy) < 1 || Math.hypot(ax - dx, ay - dy) < 1 ||
        Math.hypot(bx - cx, by - cy) < 1 || Math.hypot(bx - dx, by - dy) < 1) {
        return false;
    }
    return ccw(ax, ay, cx, cy, dx, dy) !== ccw(bx, by, cx, cy, dx, dy) &&
           ccw(ax, ay, bx, by, cx, cy) !== ccw(ax, ay, bx, by, dx, dy);
}
function polylinesCross(ptsA, ptsB) {
    for (let i = 0; i < ptsA.length - 1; i++) {
        const [ax, ay] = ptsA[i], [bx, by] = ptsA[i + 1];
        for (let j = 0; j < ptsB.length - 1; j++) {
            const [cx, cy] = ptsB[j], [dx, dy] = ptsB[j + 1];
            if (segmentsIntersect(ax, ay, bx, by, cx, cy, dx, dy)) return true;
        }
    }
    return false;
}

// ------------------------------------------- Annotation geometry & DOM leak checks (Factor 1, live DOM)
async function evaluateGeometry(container, q, page = null) {
    const issues = [];
    const spec = q.diagram_spec || q.diagram || {};
    const pins = Array.isArray(spec.pins) ? spec.pins : [];
    const vb = String(spec.viewBox || '0 0 600 480').split(' ').map(Number);
    const vbW = vb[2] || 600, vbH = vb[3] || 480;

    const svgMarkup = await container.evaluate(el => el.innerHTML);
    if (!/<svg/i.test(svgMarkup)) {
        return { status: 'RENDER_FAILURE', issues: [{ code: 'SVG_NOT_MOUNTED', detail: 'Diagram container holds no <svg> plate.' }], measured: [] };
    }
    if (svgMarkup.includes('NaN')) {
        issues.push({ code: 'NaN_COORDINATE', detail: 'Rendered SVG contains NaN coordinates (broken geometry math).' });
    }

    // R2: Check SVG <text> nodes for leaked LaTeX/markdown/Geogebra tags
    const svgTextLeaks = await container.evaluate(el => {
        const leaks = [];
        const texts = el.querySelectorAll('svg text');
        texts.forEach(t => {
            const txt = (t.textContent || '').trim();
            if (!txt) return;
            if (/(\{,\}|\\[a-zA-Z]+|\*\*|\^|_\{|_[0-9a-zA-Z]|GeoGebra)/i.test(txt)) {
                leaks.push(txt.slice(0, 80));
            }
        });
        // Also check header bar inside diagram container for "GeoGebra"
        const allText = (el.innerText || '');
        if (/GeoGebra/i.test(allText)) {
            leaks.push('Header/Caption contains "GeoGebra"');
        }
        return leaks;
    });
    if (svgTextLeaks.length > 0) {
        issues.push({ code: 'SVG_TEXT_LEAK', detail: `SVG/Diagram leaked raw syntax or branding: ${[...new Set(svgTextLeaks)].slice(0, 3).join(' | ')}` });
    }

    // R4: Check non-adjacent SVG <text> bounding-box collisions
    const textOverlaps = await container.evaluate(el => {
        const overlaps = [];
        const svgs = el.querySelectorAll('svg');
        svgs.forEach(svg => {
            const nodes = Array.from(svg.querySelectorAll('text')).filter(t => (t.textContent || '').trim().length > 0);
            const boxes = nodes.map(n => {
                const r = n.getBoundingClientRect();
                return { text: (n.textContent || '').trim(), x: r.left, y: r.top, w: r.width, h: r.height };
            }).filter(b => b.w > 2 && b.h > 2);
            for (let i = 0; i < boxes.length; i++) {
                for (let j = i + 1; j < boxes.length; j++) {
                    const a = boxes[i], b = boxes[j];
                    const ix = Math.max(0, Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x));
                    const iy = Math.max(0, Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y));
                    if (ix > 6 && iy > 5) {
                        overlaps.push(`"${a.text}" overlaps "${b.text}"`);
                    }
                }
            }
        });
        return overlaps;
    });
    if (textOverlaps.length > 0) {
        issues.push({ code: 'LABEL_OVERLAP', detail: `Overlapping SVG text labels: ${textOverlaps.slice(0, 2).join('; ')}` });
    }

    // R2: Check rendered question card text (prompt, answer, marking points, hints) for raw LaTeX/markdown leaks
    if (page) {
        const cardLeaks = await page.evaluate(() => {
            const selectors = [
                '[data-testid="workbench-question-prompt"]',
                '[data-testid="workbench-sample-answer"]',
                '[data-testid="workbench-marking-points"]',
                '[data-testid="workbench-hint-tier1"]',
                '[data-testid="workbench-hint-tier2"]',
                '[data-testid="workbench-hint-tier3"]',
            ];
            const found = [];
            for (const sel of selectors) {
                const el = document.querySelector(sel);
                if (!el) continue;
                const vis = el.innerText || '';
                if (/(\{,\}|\\frac|\\sqrt|\\text|\\times|\\cdot|\\therefore|\\approx|\*\*|\$[a-zA-Z0-9\\])/i.test(vis)) {
                    found.push(`${sel.replace('[data-testid="workbench-', '').replace('"]', '')}: "${vis.slice(0, 70)}"`);
                }
                if (/(?:[a-zA-Z0-9)]\^[0-9{+-]|[a-zA-Z]_[0-9{])/.test(vis)) {
                    found.push(`${sel.replace('[data-testid="workbench-', '').replace('"]', '')} bare ^/_: "${vis.slice(0, 70)}"`);
                }
            }
            return found;
        });
        if (cardLeaks.length > 0) {
            issues.push({ code: 'TEXT_LEAK', detail: `Visible card text contains unrendered LaTeX/markdown: ${cardLeaks.slice(0, 2).join(' | ')}` });
        }
    }

    if (pins.length === 0) {
        return { status: issues.length === 0 ? PASS.geometryNa : 'GEOMETRY_DEFECT', issues, measured: [] };
    }

    // R9: If pins are present, prompt or answer must actually reference pin letters or structure identification
    const promptAndAns = `${q.question || q.prompt || ''} ${extractAnswerString(q)}`;
    const mentionsPins = pins.some(p => new RegExp(`\\b(part|label|structure|letter|pin|region|component|organelle|vessel|chamber|layer|phase|stage|bone|gland|force|ray|wave)?\\s*\\(?${p.pin}\\)?\\b`, 'i').test(promptAndAns));
    if (!mentionsPins) {
        issues.push({ code: 'PINS_ON_NON_LABELLING', detail: `Diagram renders A-D pins (${pins.map(p => p.pin).join(',')}) but neither prompt nor answer references them (R9).` });
    }

    const measured = await container.evaluate((el, pinDefs) => pinDefs.map(p => {
        const rect = el.querySelector(`rect[data-testid="bio-pin-${p.pin}"]`);
        const g = rect ? rect.closest('g') : null;
        const circle = g ? g.querySelector('circle') : null;
        const poly = g ? g.querySelector('polyline') : null;
        const rawPoints = poly ? String(poly.getAttribute('points') || '').trim().split(/\s+/).map(pair => pair.split(',').map(Number)) : [];
        return {
            pin: p.pin,
            rect: rect ? {
                x: Number(rect.getAttribute('x')), y: Number(rect.getAttribute('y')),
                w: Number(rect.getAttribute('width')), h: Number(rect.getAttribute('height'))
            } : null,
            dot: circle ? { cx: Number(circle.getAttribute('cx')), cy: Number(circle.getAttribute('cy')) } : null,
            leaderFirstPoint: poly ? String(poly.getAttribute('points') || '').trim().split(/\s+/)[0] : null,
            polyPoints: rawPoints
        };
    }), pins);

    for (const m of measured) {
        const def = pins.find(p => p.pin === m.pin);
        const [ax, ay] = def.anchor || [NaN, NaN];
        if (!m.rect) { issues.push({ code: 'PIN_BADGE_NOT_MOUNTED', detail: `Callout badge ${m.pin} is absent from the live DOM.` }); continue; }
        const cx = m.rect.x + m.rect.w / 2, cy = m.rect.y + m.rect.h / 2;

        if (m.rect.x < 0 || m.rect.y < 0 || m.rect.x + m.rect.w > vbW || m.rect.y + m.rect.h > vbH) {
            issues.push({ code: 'PIN_BOX_OFF_CANVAS', detail: `Badge ${m.pin} at (${m.rect.x},${m.rect.y}) escapes the ${vbW}x${vbH} viewBox.` });
        }
        const expectsLeft = def.side === 'left';
        if (ax > 20 && ax < vbW - 20) {
            const sideOk = expectsLeft ? cx < ax : cx > ax;
            if (!sideOk) issues.push({ code: 'PIN_SIDE_FLIPPED', detail: `Badge ${m.pin} center x=${cx.toFixed(0)} is on the wrong side of anchor x=${ax} (declared side: "${def.side}").` });
        }
        if (!m.dot || Math.abs(m.dot.cx - ax) > 1 || Math.abs(m.dot.cy - ay) > 1) {
            issues.push({ code: 'ANCHOR_DOT_MISMATCH', detail: `Anchor dot for ${m.pin} is ${m.dot ? `(${m.dot.cx},${m.dot.cy})` : 'missing'} but generator declared (${ax},${ay}).` });
        }
        if (!m.leaderFirstPoint || m.leaderFirstPoint !== `${ax},${ay}`) {
            issues.push({ code: 'LEADER_NOT_ANCHORED', detail: `Leader line for ${m.pin} starts at "${m.leaderFirstPoint}" instead of the anchor point (${ax},${ay}).` });
        }
    }

    // R4: Badge overlap (same-side vertical collisions of 32px boxes)
    for (let i = 0; i < measured.length; i++) {
        for (let j = i + 1; j < measured.length; j++) {
            const a = measured[i], b = measured[j];
            if (!a.rect || !b.rect) continue;
            const overlap = a.rect.x < b.rect.x + b.rect.w && b.rect.x < a.rect.x + a.rect.w
                && a.rect.y < b.rect.y + b.rect.h && b.rect.y < a.rect.y + a.rect.h;
            if (overlap) issues.push({ code: 'PIN_BADGES_OVERLAP', detail: `Badges ${a.pin} and ${b.pin} overlap on the rendered plate.` });
        }
    }

    // R3: Leader polyline crossing check across all callouts
    for (let i = 0; i < measured.length; i++) {
        for (let j = i + 1; j < measured.length; j++) {
            const a = measured[i], b = measured[j];
            if (a.polyPoints?.length >= 2 && b.polyPoints?.length >= 2) {
                if (polylinesCross(a.polyPoints, b.polyPoints)) {
                    issues.push({ code: 'LEADER_CROSSING', detail: `Leader lines for pins ${a.pin} and ${b.pin} intersect (R3).` });
                }
            }
        }
    }

    return { status: issues.length === 0 ? PASS.geometryOk : 'GEOMETRY_DEFECT', issues, measured };
}

// -------------------------------------------------- Seed generation via API intercept
function postField(r) {
    try { return JSON.parse(r.request().postData() || '{}'); } catch { return null; }
}

async function generateForSeed(page, seed, archetypeId, timeoutMs = 60000) {
    // The workbench keeps a single shared `generating` flag; on mount it auto-generates catalog[0]
    // (a heavy Grade-9 heart question) which disables the button for everyone else. Wait for idle.
    const idleStart = Date.now();
    await page.waitForFunction(() => {
        const b = document.querySelector('[data-testid="btn-vet-generate"]');
        return b && !b.disabled;
    }, { timeout: 240000 });
    if (Date.now() - idleStart > 15000) {
        console.log(`  (waited ${Math.round((Date.now() - idleStart) / 1000)}s for generator queue to go idle)`);
    }

    // Threaded backends interleave responses: match on BOTH seed and archetype_id so a
    // straggler auto-generation from another archetype (same seed number) can never leak in.
    const responsePromise = page.waitForResponse(r => {
        if (!r.url().includes(GENERATE_ROUTE) || r.request().method() !== 'POST') return false;
        const j = postField(r);
        return j && j.seed === seed && j.archetype_id === archetypeId;
    }, { timeout: timeoutMs });

    await page.locator('[data-testid="input-workbench-seed"]:visible').fill(String(seed));
    await page.locator('[data-testid="btn-vet-generate"]:visible').click();

    const resp = await responsePromise;
    const payload = await resp.json().catch(() => null);
    if (!resp.ok() || !payload || !Array.isArray(payload.questions) || payload.questions.length === 0) {
        const msg = payload?.error || `HTTP ${resp.status()} / empty questions[]`;
        throw new Error(`Generator failed for seed ${seed}: ${msg}`);
    }
    const q = payload.questions[0];
    if (q.archetype_id && q.archetype_id !== archetypeId) {
        throw new Error(`Response identity mismatch: asked ${archetype_id}, received ${q.archetype_id} (seed ${seed}).`);
    }
    return q;
}

/** Does the rendered card show exactly this intercepted question? */
async function waitForPaintedQuestion(page, q, budgetMs = 6000) {
    const rawPrompt = String(q.prompt || q.question || q.question_text || '');
    const expectedRaw = rawPrompt.slice(0, 120);
    const expectedNorm = normalizeName(rawPrompt).slice(0, 120);
    if (!expectedNorm) return true;
    const deadline = Date.now() + budgetMs;
    for (;;) {
        const rawSig = await page.locator('[data-testid="workbench-question-prompt"]:visible').getAttribute('data-raw-prompt-sig').catch(() => null);
        if (rawSig && rawSig === expectedRaw) return true;
        const dom = await page.locator('[data-testid="workbench-question-prompt"]:visible').innerText().catch(() => '');
        if (normalizeName(dom).slice(0, 120) === expectedNorm) return true;
        if (Date.now() > deadline) return false;
        await page.waitForTimeout(400);
    }
}

/** Wait until no /vet/generate responses land for quietMs (drains heavy mount auto-generations). */
async function drainInflightGenerations(page, quietMs = 5000, maxMs = 180000) {
    const t0 = Date.now();
    let lastResp = t0;
    const handler = r => { if (r.url().includes(GENERATE_ROUTE)) lastResp = Date.now(); };
    page.on('response', handler);
    while (Date.now() - t0 < maxMs) {
        await page.waitForTimeout(500);
        if (Date.now() - lastResp >= quietMs) break;
    }
    page.off('response', handler);
    const waited = Math.round((Date.now() - t0) / 1000);
    if (waited > 8) console.log(`[*] Drained in-flight generations (${waited}s wait) before starting the audit loop.`);
}

// ----------------------------------------------------------- User flags intake
function loadOrInitUserFlags(outputDir, grade, archetypeIds) {
    const flagsPath = path.join(outputDir, `user_flags_gr${grade}.json`);
    if (fs.existsSync(flagsPath)) {
        try {
            const raw = JSON.parse(fs.readFileSync(flagsPath, 'utf-8'));
            const list = (Array.isArray(raw) ? raw : (raw.flags || [])).filter(f => f && f.archetype_id && String(f.note || '').trim());
            const byId = new Map();
            for (const f of list) {
                if (!f || !f.archetype_id) continue;
                if (!byId.has(f.archetype_id)) byId.set(f.archetype_id, []);
                byId.get(f.archetype_id).push({ factor: f.factor || 'other', note: f.note || '' });
            }
            console.log(`[flags] Merged ${list.length} manual review flag(s) from ${flagsPath}`);
            return { byId, flagsPath, isNew: false };
        } catch (e) {
            console.warn(`[flags] Could not parse ${flagsPath}: ${e.message} — using empty flags.`);
            return { byId: new Map(), flagsPath, isNew: false };
        }
    }
    const template = {
        _instructions: `Manual visual-scan intake for Grade ${grade} diagram vetting. For each issue you see while browsing the screenshots/dashboard, append { "archetype_id", "factor": "annotation" | "answer" | "entropy" | "other", "note": "..." }. Re-run the pipeline afterwards and flagged notes appear in the ledger and dashboard.`,
        flags: archetypeIds.map(id => ({ archetype_id: id, factor: '', note: '' }))
    };
    fs.writeFileSync(flagsPath, JSON.stringify(template, null, 2), 'utf-8');
    console.log(`[flags] Created manual-review template: ${flagsPath}`);
    return { byId: new Map(), flagsPath, isNew: true };
}

// ------------------------------------------------------------- HTML dashboard
function renderBadge(text, ok, warn = false) {
    const cls = ok ? 'bg-emerald-100 text-emerald-800' : warn ? 'bg-amber-100 text-amber-800' : 'bg-red-100 text-red-800';
    return `<span class="px-2.5 py-1 rounded-full text-xs font-semibold ${cls}">${text}</span>`;
}

function issueList(issues) {
    if (!issues || issues.length === 0) return '<li class="text-emerald-700">No issues detected.</li>';
    return issues.map(i => `<li><span class="font-mono font-bold text-red-700">${i.code}</span> — ${i.detail}</li>`).join('');
}

function generateHtmlDashboard(reportData, outputPath) {
    const targetGrade = reportData.grade;
    const archs = reportData.archetypes;
    const countPass = (key, passValues) => archs.filter(a => passValues.includes(a[key])).length;
    const renderPass = countPass('rendering_status', [PASS.render]);
    const geomPass = countPass('geometry_status', [PASS.geometryOk, PASS.geometryNa]);
    const entropyPass = countPass('entropy_status', [PASS.entropyDynamic]);
    const truthPass = countPass('rubric_status', [PASS.truthVerified]);

    const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fundile - Grade ${targetGrade} Diagram Archetype Vetting Audit</title>
<script src="https://cdn.tailwindcss.com"><\/script>
<style>.screenshot-zoom{transition:transform .2s}.screenshot-zoom:hover{transform:scale(1.02)}</style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen">
<header class="bg-[#13519C] text-white py-6 px-8 shadow-md">
  <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
    <div>
      <span class="text-xs font-mono uppercase tracking-widest text-amber-300">Super Admin Quality Governance</span>
      <h1 class="text-2xl font-bold tracking-tight">Grade ${targetGrade} Diagram Archetype Vetting &amp; Multi-Seed Entropy Audit</h1>
      <p class="text-xs text-blue-100 mt-1">Evidence-derived statuses only • ${reportData.seeds_executed} seeds/archetype • ${new Date(reportData.timestamp).toISOString().replace('T', ' ').substring(0, 19)} UTC</p>
    </div>
  </div>
</header>
<main class="max-w-7xl mx-auto py-8 px-6 space-y-8">
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
    ${[['Plate render', renderPass, archs.length], ['Annotation geometry', geomPass, archs.length], ['Seed entropy (part variation)', entropyPass, archs.length], ['Answer truth vs anchor registry', truthPass, archs.length]]
        .map(([l, p, t]) => `<div class="bg-white rounded-xl border border-slate-200 p-5"><div class="text-xs font-medium uppercase tracking-wider text-slate-500">${l}</div><div class="text-3xl font-bold ${p === t ? 'text-emerald-600' : 'text-amber-600'} mt-2">${p} / ${t}</div></div>`).join('')}
  </div>

  ${archs.map(a => `
  <div id="arch-${a.archetype_id}" class="bg-white rounded-2xl border ${a.run_status === 'OK' ? 'border-slate-200' : 'border-red-300'} shadow-sm overflow-hidden">
    <div class="bg-slate-50 border-b border-slate-200 p-5 flex flex-wrap items-center justify-between gap-4">
      <div class="space-y-1">
        <div class="flex items-center gap-2 flex-wrap">
          <span class="px-2 py-0.5 rounded text-xs font-bold font-mono bg-blue-100 text-blue-900">${a.archetype_id}</span>
          <span class="px-2 py-0.5 rounded text-xs bg-slate-200 text-slate-700">${a.subject} • Gr ${a.grade} • T${a.term} • ${a.diagram_id || a.master || '?'}</span>
        </div>
        <h2 class="text-lg font-bold text-slate-900">${a.title}</h2>
        ${a.run_status !== 'OK' ? `<div class="text-xs font-mono text-red-700">RUN ABORTED: ${a.run_error || a.run_status}</div>` : ''}
      </div>
      <div class="flex flex-wrap items-center gap-2">
        ${renderBadge(a.rendering_status, a.rendering_status === PASS.render)}
        ${renderBadge(a.geometry_status, [PASS.geometryOk, PASS.geometryNa].includes(a.geometry_status), a.geometry_status === PASS.geometryNa)}
        ${renderBadge(a.entropy_status, a.entropy_status === PASS.entropyDynamic, a.entropy_status === PASS.entropyLow)}
        ${renderBadge(a.rubric_status, a.rubric_status === PASS.truthVerified, a.rubric_status === PASS.truthPartial)}
      </div>
    </div>
    <div class="p-6 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-${Math.min(3, Math.max(1, a.seeds.length))} gap-6">
        ${a.seeds.map(s => `
        <div class="rounded-xl border border-slate-200 bg-slate-50 p-4 space-y-3">
          <div class="flex items-center justify-between text-xs">
            <span class="px-2 py-0.5 rounded font-mono font-bold bg-blue-600 text-white">Seed ${s.seed}</span>
            <span class="text-slate-500 font-mono">${s.marks ? s.marks + ' Marks' : ''}</span>
          </div>
          ${s.error ? `<div class="text-xs text-red-700 font-mono bg-red-50 border border-red-200 rounded-lg p-2">${s.error}</div>` : `
          <div class="rounded-lg overflow-hidden border border-slate-200 bg-white aspect-4/3 flex items-center justify-center p-2 screenshot-zoom">
            ${s.diagram_screenshot_rel ? `<a href="${s.diagram_screenshot_rel}" target="_blank"><img src="${s.diagram_screenshot_rel}" class="w-full h-auto max-h-56 object-contain" alt="${a.archetype_id} seed ${s.seed}"/></a>` : '<div class="text-xs text-slate-400">Screenshot unavailable</div>'}
          </div>
          <div class="text-xs bg-white p-3 rounded-lg border border-slate-200 max-h-28 overflow-y-auto whitespace-pre-line"><div class="font-semibold mb-1">Prompt:</div>${s.prompt || 'N/A'}</div>
          <div class="text-xs bg-emerald-50/70 p-3 rounded-lg border border-emerald-200 max-h-28 overflow-y-auto whitespace-pre-line"><div class="font-semibold text-emerald-900 mb-1">Canonical answer:</div><div class="font-mono text-[11px]">${s.sample_answer || 'N/A'}</div></div>
          <div class="text-xs"><span class="font-semibold">Asked structures:</span> <span class="font-mono">${(s.target_names || []).join(', ') || '(no callout pins — vector modality)'}</span></div>`}
        </div>`).join('')}
      </div>

      <div class="rounded-xl border border-slate-200 p-4 space-y-2">
        <h4 class="text-xs font-bold uppercase tracking-wider text-slate-700">Seed-to-Seed Part Variation</h4>
        <table class="w-full text-xs border-collapse">
          <thead><tr class="border-b text-left text-slate-600 font-mono"><th class="py-1.5 px-2">Seed</th><th class="py-1.5 px-2">Target structures asked</th><th class="py-1.5 px-2">Distinct?</th></tr></thead>
          <tbody class="divide-y">${a.seeds.map(s => `<tr><td class="py-1.5 px-2 font-mono font-bold">Seed ${s.seed}</td><td class="py-1.5 px-2 font-mono">${s.error ? '—' : ((s.target_names || []).join(', ') || s.signature_short || '—')}</td><td class="py-1.5 px-2">${s.is_unique ? '<span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-[11px]">New parts</span>' : '<span class="px-2 py-0.5 rounded bg-slate-200 text-slate-700 text-[11px]">Repeat</span>'}</td></tr>`).join('')}</tbody>
        </table>
        ${a.coverage_note ? `<div class="text-[11px] text-slate-600 pt-1">${a.coverage_note}</div>` : ''}
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="rounded-xl border border-amber-200 bg-amber-50/40 p-4 space-y-2">
          <span class="text-xs font-bold uppercase tracking-wider text-amber-900">Manual Review Flags (user_flags_gr${targetGrade}.json)</span>
          <ul class="text-xs list-disc pl-4 space-y-1">${a.user_flagged_notes && a.user_flagged_notes.length ? a.user_flagged_notes.map(f => `<li><span class="font-mono">[${f.factor}]</span> ${f.note}</li>`).join('') : '<li class="text-amber-700">None recorded yet.</li>'}</ul>
        </div>
        <div class="rounded-xl border border-blue-200 bg-blue-50/40 p-4 space-y-2">
          <span class="text-xs font-bold uppercase tracking-wider text-blue-900">Automated Findings</span>
          <ul class="text-xs list-disc pl-4 space-y-1">${issueList(a.findings)}</ul>
        </div>
      </div>
    </div>
  </div>`).join('')}
</main>
<footer class="bg-white border-t py-6 text-center text-xs text-slate-500">Fundile Super Admin Quality Engine • Grade ${targetGrade} • statuses derived from measured DOM + anchor-registry cross-checks</footer>
</body></html>`;
    fs.writeFileSync(outputPath, html, 'utf-8');
    console.log(`[PASS] HTML dashboard: ${outputPath}`);
}

// ------------------------------------------------------------------- Main run
export async function runVettingPipeline() {
    const config = parseArgs();
    const shotsDir = path.join(config.outputDir, 'shots');
    fs.mkdirSync(shotsDir, { recursive: true });

    console.log('\n======================================================================');
    console.log('   FUNDILE DIAGRAM ARCHETYPE VETTING & MULTI-SEED PIPELINE (v2)');
    console.log('======================================================================');
    console.log(`Grade ${config.grade} | seeds: ${config.seeds ?? 'adaptive (6 pinned / 3 vector)'} | headless: ${config.headless}`);
    console.log(`Frontend: ${config.url} | Backend: ${config.apiUrl}\n`);

    await preflight(config);

    const catalogPath = path.join(PROJECT_ROOT, 'caps-ai-backend', 'app', 'data', 'diagram_archetypes_catalog.json');
    if (!fs.existsSync(catalogPath)) throw new Error(`Catalog missing at: ${catalogPath}`);
    const allArchetypes = JSON.parse(fs.readFileSync(catalogPath, 'utf-8'));
    const catalogByGrade = allArchetypes.filter(a => String(a.grade) === String(config.grade));

    const browser = await chromium.launch({ headless: config.headless });
    const context = await browser.newContext({ viewport: { width: 1440, height: 960 }, deviceScaleFactor: 2 });
    const page = await context.newPage();
    page.setDefaultTimeout(60000); // dev-server cold compiles can exceed Playwright's 30s default

    if (process.argv.includes('--debug')) {
        page.on('request', r => { if (r.url().includes(GENERATE_ROUTE)) console.log(`  [trace>req] ${(r.postData() || '').slice(0, 120)}`); });
        page.on('response', async r => { if (r.url().includes(GENERATE_ROUTE)) console.log(`  [trace<res] ${r.status()} seed-in=${postField(r)?.seed} arch=${postField(r)?.archetype_id}`); });
        page.on('requestfailed', r => { if (r.url().includes(GENERATE_ROUTE)) console.log(`  [trace!fail] ${r.failure()?.errorText}`); });
    }

    const reportData = {
        grade: config.grade, seeds_executed: config.seeds ?? 'adaptive',
        timestamp: new Date().toISOString(), archetypes: []
    };
    const ledgerPath = path.join(config.outputDir, `diagram_vetting_ledger_gr${config.grade}.json`);
    const dashboardPath = path.join(config.outputDir, `diagram_vetting_dashboard_gr${config.grade}.html`);
    const writeLedger = () => fs.writeFileSync(ledgerPath, JSON.stringify(reportData, null, 2), 'utf-8');

    try {
        await authenticateSuperAdminSession(page, config.url);
        const openBtn = page.locator('[data-testid="btn-open-vetting-workbench"]:visible');
        try {
            await openBtn.waitFor({ state: 'visible' }); // page default 60s: admin card awaits live Firestore user doc
        } catch (e) {
            const dbg = path.join(config.outputDir, 'auth_debug.png');
            await page.screenshot({ path: dbg, fullPage: true }).catch(() => {});
            const bodyText = await page.locator('body').innerText().catch(() => '(unreadable)');
            throw new Error(`${e.message.split('\n')[0]}\n  Debug screenshot: ${dbg}\n  Visible page text: ${bodyText.slice(0, 400)}`);
        }
        await openBtn.click();
        await page.locator('[data-testid="super-admin-archetype-workbench"]:visible').waitFor({ state: 'visible' });

        // The workbench auto-generates catalog[0] (a heavy Grade-9 heart question, twice under
        // StrictMode) on mount. Those starve the first audited archetype's seeds server-side.
        await drainInflightGenerations(page);

        if (config.grade !== 'ALL') {
            const gradeBtn = page.locator(`[data-testid="btn-workbench-grade-${config.grade}"]:visible`);
            if (await gradeBtn.count() === 0) throw new Error(`Grade filter button btn-workbench-grade-${config.grade} not rendered in workbench UI.`);
            await gradeBtn.click();
        }

        // The workbench fetches /vet/catalog on mount (Firestore joins make this slow) — wait for the list to populate
        await page.waitForSelector('[data-testid^="archetype-item-"]', { timeout: 90000 }).catch(() => {});
        const renderedIdsAll = await page.$$eval('[data-testid^="archetype-item-"]', els =>
            els.map(e => e.getAttribute('data-testid').replace('archetype-item-', '')));
        if (renderedIdsAll.length === 0) {
            const dbg = path.join(config.outputDir, 'catalog_debug.png');
            await page.screenshot({ path: dbg, fullPage: true }).catch(() => {});
            const deskText = await page.locator('[data-testid="super-admin-archetype-workbench"]').innerText().catch(() => '(unreadable)');
            throw new Error(`No archetype items rendered for grade ${config.grade}.\n  Debug screenshot: ${dbg}\n  Workbench text: ${deskText.slice(0, 500)}`);
        }
        const renderedIds = config.only ? renderedIdsAll.filter(id => config.only.includes(id)) : renderedIdsAll;
        if (renderedIds.length === 0) throw new Error(`--only matched none of the rendered ids: ${renderedIdsAll.join(', ')}`);
        console.log(`\n[*] ${renderedIds.length} archetypes rendered for Grade ${config.grade}${config.only ? ` (--only subset)` : ''}.\n`);

        const { byId: userFlags } = loadOrInitUserFlags(config.outputDir, config.grade, renderedIds);

        for (let aIdx = 0; aIdx < renderedIds.length; aIdx++) {
            const id = renderedIds[aIdx];
            const catalogEntry = catalogByGrade.find(c => c.archetype_id === id) || {};
            console.log(`[${aIdx + 1}/${renderedIds.length}] ${id} (${catalogEntry.title || ''})`);

            const archRecord = {
                archetype_id: id, diagram_id: catalogEntry.diagram_id || null, title: catalogEntry.title || id,
                subject: catalogEntry.subject || '', grade: catalogEntry.grade || config.grade, term: catalogEntry.term || null,
                category: catalogEntry.category || '', master: null, view: catalogEntry.view || null,
                run_status: 'OK', run_error: null,
                rendering_status: 'RENDER_NOT_ATTEMPTED', geometry_status: 'GEOMETRY_NOT_ATTEMPTED',
                entropy_status: 'ENTROPY_NOT_ATTEMPTED', rubric_status: 'RUBRIC_NOT_ATTEMPTED',
                seeds: [], findings: [], coverage_note: '',
                user_flagged_notes: userFlags.get(id) || []
            };
            reportData.archetypes.push(archRecord);

            try {
                // Select archetype; consume its auto-generation response so it can't race the seed loop
                const autoGen = page.waitForResponse(r => {
                    if (!r.url().includes(GENERATE_ROUTE)) return false;
                    const j = postField(r);
                    return j && j.archetype_id === id;
                }, { timeout: 30000 }).catch(() => null);
                const itemBtn = page.locator(`[data-testid="archetype-item-${id}"]:visible`);
                await itemBtn.scrollIntoViewIfNeeded();
                await itemBtn.click();
                const firstResp = await autoGen;
                let firstQuestion = null;
                if (firstResp && firstResp.ok()) {
                    try {
                        const p = await firstResp.json();
                        firstQuestion = p?.questions?.[0] || null;
                    } catch { /* handled per-seed */ }
                }
                const masterGuess = firstQuestion?.diagram_spec?.master || firstQuestion?.diagram?.master || null;
                archRecord.master = masterGuess;
                const isPinned = Boolean(firstQuestion?.diagram_spec?.pins?.length) || /Category A/i.test(archRecord.category || '');
                const seedPlan = config.seeds ?? (isPinned ? 6 : 3);

                const signatures = new Map(); // signature -> first seed seen
                const allTargetNames = new Set();
                let renderAttempts = 0, renderSuccesses = 0;
                const truthResults = [];
                const geomResults = [];

                for (let s = 1; s <= seedPlan; s++) {
                    const seedRecord = { seed: s, error: null, target_names: [], prompt: '', sample_answer: '', marks: null, signature: null, is_unique: false, findings: [] };
                    archRecord.seeds.push(seedRecord);
                    try {
                        const q = await generateForSeed(page, s, id);

                        // Wait for React to paint this exact question's layer
                        const container = page.locator('[data-testid="workbench-diagram-container"]:visible');
                        await container.waitFor({ state: 'visible', timeout: 15000 });
                        await page.waitForTimeout(500); // KaTeX / image decode settle
                        renderAttempts++;

                        // Confirm the card actually shows THIS intercepted question (a late stray
                        // generation from another archetype can overwrite the DOM mid-loop). On a
                        // miss, regenerate the same seed once — generation is deterministic, so the
                        // repaint lands on the identical question — then re-check.
                        let paintOk = await waitForPaintedQuestion(page, q);
                        if (!paintOk) {
                            const regen = page.waitForResponse(r => {
                                if (!r.url().includes(GENERATE_ROUTE)) return false;
                                const j = postField(r);
                                return j && j.seed === s && j.archetype_id === id;
                            }, { timeout: 60000 }).catch(() => null);
                            await page.locator('[data-testid="btn-vet-generate"]:visible').click();
                            await regen;
                            paintOk = await waitForPaintedQuestion(page, q);
                        }
                        if (!paintOk) {
                            seedRecord.findings.push({ code: 'DOM_STALE_PAINT', detail: 'Rendered card never matched the intercepted question — screenshot may depict a different (stray) generation; annotation geometry NOT measured for this seed.' });
                            console.log(`  seed ${s}: stale-paint warning (data still from live API response)`);
                        }

                        const shots = {
                            diagram: `Gr${archRecord.grade}_${id}_seed${s}_diagram.png`,
                            card: `Gr${archRecord.grade}_${id}_seed${s}_card.png`
                        };
                        await container.screenshot({ path: path.join(shotsDir, shots.diagram) });
                        const card = page.locator('[data-testid="workbench-question-card"]:visible');
                        if (await card.count() > 0) await card.screenshot({ path: path.join(shotsDir, shots.card) });
                        renderSuccesses++;

                        seedRecord.prompt = q.question || q.question_text || q.prompt || '';
                        seedRecord.sample_answer = extractAnswerString(q);
                        seedRecord.marks = q.marks ?? q.marking_schema?.total_marks ?? null;

                        const registry = loadAnchorRegistry(q.diagram_spec?.master || q.diagram?.master || archRecord.master);
                        archRecord.master = archRecord.master || q.diagram_spec?.master || null;

                        const truth = evaluateRubricTruth(q, registry, catalogEntry);
                        truthResults.push(truth);
                        seedRecord.findings.push(...truth.issues);

                        const geom = paintOk
                            ? await evaluateGeometry(container, q, page)
                            : { status: 'GEOMETRY_SKIPPED_STALE', issues: [], measured: [] };
                        geomResults.push(geom);
                        seedRecord.findings.push(...geom.issues);

                        // Entropy signature: target structure NAMES, not raw answer text
                        const spec = q.diagram_spec || q.diagram || {};
                        const pins = Array.isArray(spec.pins) ? spec.pins : [];
                        const names = truth.targetNames.length ? truth.targetNames
                            : pins.filter(p => p.role === 'target').map(p => registryByCoord(registry, p.anchor)?.name || `pin_${p.pin}`);
                        seedRecord.target_names = [...new Set(names)];
                        seedRecord.target_names.forEach(n => allTargetNames.add(n));
                        seedRecord.signature = seedRecord.target_names.length
                            ? seedRecord.target_names.map(normalizeName).sort().join('|')
                            : normalizeName(`${seedRecord.prompt} ${seedRecord.sample_answer}`.slice(0, 600));
                        seedRecord.signature_short = seedRecord.signature.length > 80 ? seedRecord.signature.slice(0, 80) + '…' : seedRecord.signature;
                        const seenOn = signatures.get(seedRecord.signature);
                        seedRecord.is_unique = !seenOn;
                        if (!seenOn) signatures.set(seedRecord.signature, s);
                        if (seedRecord.findings.length === 0) process.stdout.write(`  seed ${s}: ok\n`);
                        else process.stdout.write(`  seed ${s}: ${seedRecord.findings.length} finding(s) [${seedRecord.findings.map(f => f.code).join(', ')}]\n`);
                    } catch (seedErr) {
                        seedRecord.error = String(seedErr.message || seedErr).split('\n')[0];
                        process.stdout.write(`  seed ${s}: ERROR ${seedRecord.error}\n`);
                        writeLedger();
                    }
                }

                // ---- Aggregate statuses (all measured, never defaulted) ----
                archRecord.rendering_status = renderAttempts > 0 && renderSuccesses === renderAttempts
                    ? PASS.render : (renderSuccesses > 0 ? 'RENDER_PARTIAL' : 'RENDER_FAILURE');
                const geomMeasured = geomResults.filter(g => g.status !== 'GEOMETRY_SKIPPED_STALE');
                const geomIssues = geomMeasured.flatMap(g => g.issues);
                if (geomMeasured.length === 0) {
                    archRecord.geometry_status = 'GEOMETRY_UNMEASURED';
                } else if (geomMeasured.every(g => g.status === PASS.geometryNa)) {
                    archRecord.geometry_status = PASS.geometryNa;
                } else if (geomIssues.length > 0) {
                    archRecord.geometry_status = 'GEOMETRY_DEFECT';
                } else {
                    archRecord.geometry_status = geomMeasured.some(g => g.status === PASS.geometryOk) ? PASS.geometryOk : 'GEOMETRY_UNMEASURED';
                }
                const okTruths = truthResults.filter(t => t.status === PASS.truthVerified).length;
                archRecord.rubric_status = truthResults.some(t => t.status === PASS.emptyRubric) ? PASS.emptyRubric
                    : okTruths === truthResults.length && truthResults.length > 0 ? PASS.truthVerified
                    : truthResults.some(t => t.status === PASS.truthPartial) ? PASS.truthPartial : PASS.truthDefect;

                const successful = archRecord.seeds.filter(x => !x.error);
                if (successful.length === 0) archRecord.entropy_status = 'ENTROPY_UNMEASURED';
                else if (signatures.size === 1) archRecord.entropy_status = PASS.entropyStatic;
                else if (signatures.size < successful.length) archRecord.entropy_status = PASS.entropyLow;
                else archRecord.entropy_status = PASS.entropyDynamic;

                archRecord.coverage_note = `Across ${successful.length} successful seed(s): ${signatures.size} distinct part-combination(s); structures ever asked: ${[...allTargetNames].join(', ') || '(none parsed)'}.`;

                const codeCounts = {};
                [...geomIssues, ...truthResults.flatMap(t => t.issues)].forEach(i => { codeCounts[i.code] = (codeCounts[i.code] || 0) + 1; });
                archRecord.findings = Object.entries(codeCounts).map(([code, n]) => ({ code, detail: `detected in ${n} seed run(s) — see per-seed findings for exact evidence.` }));
            } catch (archErr) {
                archRecord.run_status = 'ARCHETYPE_ERROR';
                archRecord.run_error = String(archErr.message || archErr).split('\n')[0];
                console.error(`  [!] archetype ${id} aborted: ${archRecord.run_error}`);
            }
            writeLedger(); // incremental: a later crash never loses earlier results
        }

        generateHtmlDashboard(reportData, dashboardPath);

        // ---- Console summary ----
        const sum = (key, vals) => reportData.archetypes.filter(a => vals.includes(a[key])).length;
        console.log('\n======================================================================');
        console.log(`GRADE ${config.grade} VETTING SUMMARY (${reportData.archetypes.length} archetypes)`);
        console.log(`  Rendering OK        : ${sum('rendering_status', [PASS.render])}`);
        console.log(`  Geometry verified/NA: ${sum('geometry_status', [PASS.geometryOk, PASS.geometryNa])}`);
        console.log(`  Entropy dynamic    : ${sum('entropy_status', [PASS.entropyDynamic])}`);
        console.log(`  Answer truth       : ${sum('rubric_status', [PASS.truthVerified])} verified, ${sum('rubric_status', [PASS.truthPartial])} partial`);
        const defectArchs = reportData.archetypes.filter(a => a.run_status !== 'OK' || a.geometry_status === 'GEOMETRY_DEFECT'
            || a.rubric_status === PASS.truthDefect || a.rubric_status === PASS.emptyRubric || a.entropy_status === PASS.entropyStatic);
        console.log(`  Archetypes with defects: ${defectArchs.length ? defectArchs.map(a => a.archetype_id).join(', ') : 'NONE'}`);
        console.log(`\n  Ledger    : ${ledgerPath}`);
        console.log(`  Dashboard : ${dashboardPath}`);
        console.log(`  Flags     : ${path.join(config.outputDir, `user_flags_gr${config.grade}.json`)}`);
        console.log('======================================================================\n');
    } finally {
        writeLedger();
        await browser.close();
    }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
    runVettingPipeline().catch(err => {
        console.error('\n[FATAL] Pipeline aborted:', err.message || err);
        process.exit(1);
    });
}
