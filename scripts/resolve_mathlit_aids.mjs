/**
 * scripts/resolve_mathlit_aids.mjs
 * 
 * AUD-5: Evaluates Dimensions 4 & 5 under Node.js:
 *   - Runs the authentic getAvailableVisualAids from src/components/workspace/visual_aids/visualAidRegistry.js
 *   - Runs the authentic buildDynamicSimuLearnScript logic from src/components/simulearn/SimuLearnPlayer.jsx
 *   - Evaluates all 1,871 archetypes from reports/data/mathlit_audit_payloads.json
 *   - Outputs reports/data/mathlit_audit_aids.json
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

// 1. Import authentic getAvailableVisualAids
const { getAvailableVisualAids } = await import('../src/components/workspace/visual_aids/visualAidRegistry.js');

// 2. Pure JavaScript implementation of buildDynamicSimuLearnScript directly from SimuLearnPlayer.jsx
function buildDynamicSimuLearnScript(question, fallbackSubject = 'Mathematical Literacy', fallbackGrade = 10, fallbackTopic = '') {
  if (!question || typeof question !== 'object') return null;

  const subject = question.subject || fallbackSubject || 'Mathematical Literacy';
  const grade = question.grade || fallbackGrade || 10;
  const topic = question.topic || fallbackTopic || question.archetype || 'Worked Example';
  const arch = String(question.archetype || question.subskill || topic || '').toLowerCase();

  // Special interactive visual replay 1: Stem-and-Leaf Plot
  if (arch.includes('stem') && arch.includes('leaf')) {
    return {
      archetype: 'stem_and_leaf_dynamic',
      title: `SimuLearn Walkthrough • Constructing & Reading a Stem-and-Leaf Plot`,
      subject,
      grade,
      grid_type: 'stem_and_leaf_visual',
      frames: [
        { time_ms: 0, action: 'show_data' }
      ]
    };
  }

  // Dynamic synthesis from canonical_solution.steps
  const dSpec = question.diagram_spec || question.diagram || question.graph || question.function_graph || null;
  const canonicalSteps = question.canonical_solution?.steps;
  if (Array.isArray(canonicalSteps) && canonicalSteps.length > 0) {
    const frames = canonicalSteps.map((st, idx) => ({
      time_ms: idx * 2800,
      action: idx === canonicalSteps.length - 1 ? 'final_solution' : 'show_step',
      latex: st.to_latex || st.from_latex || String(st),
      narrative: `Step ${idx + 1}`
    }));
    return {
      archetype: arch || 'dynamic_canonical',
      title: `SimuLearn Walkthrough • ${topic}`,
      subject,
      grade,
      grid_type: dSpec ? 'diagram_and_steps' : 'stepwise_math',
      diagram_spec: dSpec,
      frames
    };
  }

  // Dynamic synthesis from raw worked_solution or explanation
  const rawWorked = String(question.worked_solution || question.explanation || question.sample_answer || '').trim();
  if (rawWorked) {
    const rawLines = rawWorked
      .split(/\n+/)
      .map((l) => l.replace(/^\*\*.*?\*\*:?\s*/, '').trim())
      .filter((l) => l.length > 2);

    if (rawLines.length > 0) {
      const frames = rawLines.slice(0, 6).map((line, idx) => ({
        time_ms: idx * 2800,
        action: idx === rawLines.length - 1 ? 'final_solution' : 'show_step',
        narrative: line
      }));
      return {
        archetype: arch || 'dynamic_worked_solution',
        title: `SimuLearn Walkthrough • ${topic}`,
        subject,
        grade,
        grid_type: dSpec ? 'diagram_and_steps' : 'stepwise_math',
        diagram_spec: dSpec,
        frames
      };
    }
  }

  return null;
}

// 3. Load harvested payloads
const payloadsPath = path.join(ROOT, 'reports', 'data', 'mathlit_audit_payloads.json');
if (!fs.existsSync(payloadsPath)) {
  console.error(`Missing payloads file: ${payloadsPath}. Run stage harvest first.`);
  process.exit(1);
}
const payloads = JSON.parse(fs.readFileSync(payloadsPath, 'utf-8'));

console.log('='.repeat(80));
console.log('AUD-5: Evaluating Dimensions 4 & 5 under Node.js across 1,871 Archetypes');
console.log('='.repeat(80));

const results = {};
const aidCounts = { DEDICATED: 0, GENERIC_MATH: 0, NONE: 0 };
const simuLearnSourceCounts = {
  SPECIAL_VISUAL: 0,
  DYNAMIC_CANONICAL: 0,
  DYNAMIC_WORKED: 0,
  OFF_TOPIC_FALLBACK: 0
};
const d5Counts = {
  LIVE_DIAGRAM: 0,
  STATIC_DIAGRAM: 0,
  TEXT_ONLY_REPLAY: 0,
  OFF_TOPIC_FALLBACK: 0,
  NONE: 0
};

let count = 0;
for (const [subId, data] of Object.entries(payloads)) {
  count++;
  const { grade, topic, subskill } = data;
  const s101 = data.seeds?.['101'] || {};

  // Form question payload for evaluation
  const questionPayload = {
    grade: Number(grade),
    subject: 'Mathematical Literacy',
    topic,
    subskill,
    modality: s101.modality || '',
    diagram_spec: s101.diagram_spec_raw || null,
    canonical_solution: s101.has_canonical_steps ? { steps: [{ step: 'Step 1' }] } : null,
    worked_solution: s101.has_worked_solution ? 'Step 1: Calculate\nStep 2: Answer' : null,
  };

  // Evaluate Dimension 4 (Visual Aid in Cognitive Sidecar)
  // Normalized subject string used by UniversalWorkspace.jsx line 547
  const normalizedSubId = 'mathematical_literacy';
  const availableAids = getAvailableVisualAids(normalizedSubId, topic, s101.modality, questionPayload);

  let aidClass = 'NONE';
  let matchedAidId = null;
  if (availableAids && availableAids.length > 0) {
    matchedAidId = availableAids[0].id;
    // Check if matched aid was dedicated to Math Lit or generic math
    const aidTitle = (availableAids[0].title || '').toLowerCase();
    if (aidTitle.includes('literacy')) {
      aidClass = 'DEDICATED';
    } else {
      aidClass = 'GENERIC_MATH';
    }
  }
  aidCounts[aidClass]++;

  // Evaluate Dimension 4 & 5 (SimuLearn Script & Behavior)
  const dynamicScript = buildDynamicSimuLearnScript(questionPayload, 'Mathematical Literacy', Number(grade), topic);

  let simuLearnSource = 'OFF_TOPIC_FALLBACK';
  let d5Behavior = 'OFF_TOPIC_FALLBACK';

  if (dynamicScript) {
    if (dynamicScript.grid_type === 'stem_and_leaf_visual') {
      simuLearnSource = 'SPECIAL_VISUAL';
      d5Behavior = 'LIVE_DIAGRAM';
    } else if (dynamicScript.grid_type === 'diagram_and_steps') {
      simuLearnSource = dynamicScript.archetype === 'dynamic_canonical' ? 'DYNAMIC_CANONICAL' : 'DYNAMIC_WORKED';
      d5Behavior = 'STATIC_DIAGRAM';
    } else if (dynamicScript.archetype === 'dynamic_canonical') {
      simuLearnSource = 'DYNAMIC_CANONICAL';
      d5Behavior = 'TEXT_ONLY_REPLAY';
    } else {
      simuLearnSource = 'DYNAMIC_WORKED';
      d5Behavior = 'TEXT_ONLY_REPLAY';
    }
  } else {
    simuLearnSource = 'OFF_TOPIC_FALLBACK'; // falls through to math_quadratic_trinomial
    d5Behavior = 'OFF_TOPIC_FALLBACK';
  }

  simuLearnSourceCounts[simuLearnSource]++;
  d5Counts[d5Behavior]++;

  results[subId] = {
    sub_id: subId,
    grade,
    term: data.term,
    topic,
    subskill,
    d4_visual_aid_class: aidClass,
    matched_aid_id: matchedAidId,
    d4_simulearn_source: simuLearnSource,
    d5_behavior: d5Behavior
  };
}

const outPath = path.join(ROOT, 'reports', 'data', 'mathlit_audit_aids.json');
fs.writeFileSync(outPath, JSON.stringify(results, null, 2), 'utf-8');

console.log(`\nProcessed ${count} archetypes.`);
console.log('\nDimension 4: Visual Aid Presence (Cognitive Sidecar):');
for (const [k, v] of Object.entries(aidCounts)) {
  console.log(`  ${k.padEnd(16)}: ${String(v).padStart(5)} (${((v / count) * 100).toFixed(1)}%)`);
}
console.log('\nDimension 4: SimuLearn Script Source:');
for (const [k, v] of Object.entries(simuLearnSourceCounts)) {
  console.log(`  ${k.padEnd(20)}: ${String(v).padStart(5)} (${((v / count) * 100).toFixed(1)}%)`);
}
console.log('\nDimension 5: Visual Aid / SimuLearn Diagram Behavior:');
for (const [k, v] of Object.entries(d5Counts)) {
  console.log(`  ${k.padEnd(20)}: ${String(v).padStart(5)} (${((v / count) * 100).toFixed(1)}%)`);
}

console.log(`\nWrote aids and SimuLearn resolution data to: ${outPath}`);
process.exit(0);
