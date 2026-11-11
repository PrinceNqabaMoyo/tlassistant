/**
 * offlineSemanticGrader.js
 * ------------------------
 * Client-side deterministic semantic rubric grader + offline LLM reconciliation queue.
 *
 * How Adaptive Progression Works Offline vs. Online for Semantic Answers:
 * 1. When ONLINE: `/api/evaluate` runs Tier 1 (stemmer + curriculum synonym clusters)
 *    followed by Tier 2 (`evaluate_semantic_rubric_llm` using ultra-affordable Gemini Flash-Lite /
 *    Gemma-2-2b-it at temperature=0.0, <220 tokens) whenever a learner paraphrases in their own words.
 * 2. When OFFLINE (`!navigator.onLine` or backend unreachable):
 *    - `gradeSemanticOffline(question, answer)` evaluates the learner's explanation locally using
 *      Porter-style stemming + South African curriculum synonym clusters so adaptive progression
 *      (Scaffold -> Practice -> Mastery routing) can route the learner immediately with 0ms latency.
 *    - Simultaneously, `enqueueOfflineSemanticSubmission()` saves the raw submission in
 *      `localStorage` (`fundile_offline_semantic_queue`).
 *    - As soon as `window.addEventListener('online', ...)` fires, `flushOfflineSemanticQueue()`
 *      re-grades queued semantic answers via the affordable LLM endpoint and reconciles BKT mastery.
 */

const OFFLINE_QUEUE_KEY = 'fundile_offline_semantic_queue_v1';

export const CURRICULUM_SYNONYM_CLUSTERS = [
  ['buy', 'purchase', 'acquire', 'bought', 'purchasing', 'spending'],
  ['sell', 'sale', 'sold', 'selling', 'revenue', 'income', 'turnover', 'receipts'],
  ['money', 'cash', 'capital', 'funds', 'finance', 'currency', 'rands'],
  ['worker', 'workers', 'labour', 'labor', 'employee', 'employees', 'staff', 'wages', 'salaries'],
  ['profit', 'surplus', 'gain', 'profitable', 'earnings'],
  ['loss', 'deficit', 'shortfall', 'lose', 'losing', 'overspend'],
  ['asset', 'assets', 'possessions', 'property', 'belongings', 'owned', 'equipment', 'vehicles'],
  ['liability', 'liabilities', 'debt', 'debts', 'loan', 'loans', 'owed', 'owing', 'creditors'],
  ['budget', 'plan', 'planning', 'estimate', 'forecast'],
  ['save', 'saving', 'savings', 'thrift', 'deposit', 'emergency', 'future'],
  ['entrepreneur', 'businessperson', 'owner', 'founder', 'enterprise', 'risk', 'innovator'],
  ['need', 'needs', 'essential', 'survival', 'basic', 'necessity', 'water', 'food', 'shelter'],
  ['want', 'wants', 'luxury', 'luxuries', 'desire', 'non-essential'],
  ['barter', 'swap', 'exchange', 'trading', 'trade', 'without money'],
  ['heat', 'thermal', 'warmth', 'temperature', 'hot'],
  ['insulator', 'insulation', 'prevent', 'reduce', 'stop', 'slow', 'trap', 'poor conductor'],
  ['conductor', 'conduct', 'transfer', 'transmit', 'allow', 'pass through', 'metal'],
  ['evaporate', 'evaporation', 'boil', 'boiling', 'vapor', 'vapour', 'steam', 'gas'],
  ['condense', 'condensation', 'cool', 'cooling', 'liquid', 'droplets'],
  ['filter', 'filtration', 'sieve', 'insoluble', 'residue', 'filtrate', 'separate'],
  ['acid', 'acidic', 'sour', 'corrosive', 'red litmus', 'low ph', 'vinegar', 'lemon'],
  ['base', 'basic', 'alkali', 'alkaline', 'bitter', 'slippery', 'soapy', 'blue litmus', 'bleach', 'bicarbonate'],
  ['neutral', 'water', 'salt', 'ph 7', 'neither', 'no change'],
  ['gravity', 'gravitational', 'pull', 'attract', 'attraction', 'mass', 'tides', 'orbit'],
  ['tilt', 'tilted', 'axis', '23.5', 'hemisphere', 'seasons', 'summer', 'winter', 'solstice', 'equinox'],
  ['variation', 'difference', 'differences', 'diversity', 'inherited', 'genetic', 'adapt', 'survival', 'species'],
  ['pollinate', 'pollination', 'pollen', 'anther', 'stigma', 'insect', 'wind', 'fertilisation', 'seed'],
];

export function stemWord(word) {
  const w = String(word || '').toLowerCase().replace(/[^a-z0-9-]/g, '');
  if (w.length <= 4) return w;
  const suffixes = ['ation', 'ition', 'ment', 'ness', 'able', 'ible', 'ingly', 'edly', 'ing', 'ies', 'es', 'ed', 'ly', 'er', 'or', 's'];
  for (const sfx of suffixes) {
    if (w.endsWith(sfx) && w.length - sfx.length >= 3) {
      const base = w.slice(0, -sfx.length);
      return sfx === 'ies' ? `${base}y` : base;
    }
  }
  return w;
}

export function conceptMatchesCorpus(concept, studentCorpus, studentStems) {
  const cClean = String(concept || '').toLowerCase().replace(/^[.,;:!?]+|[.,;:!?]+$/g, '').trim();
  if (!cClean) return false;
  if (studentCorpus.includes(cClean)) return true;
  const cStem = stemWord(cClean);
  if (cStem && cStem.length >= 3 && studentStems.has(cStem)) return true;
  for (const cluster of CURRICULUM_SYNONYM_CLUSTERS) {
    if (cluster.includes(cClean) || cluster.some((t) => stemWord(t) === cStem)) {
      for (const syn of cluster) {
        if (studentCorpus.includes(syn) || studentStems.has(stemWord(syn))) {
          return true;
        }
      }
    }
  }
  return false;
}

export function gradeSemanticOffline(question, answer) {
  const maxScore = Math.max(1, Number(question?.marks || 4));
  const expectedKeywords = question?.key_concepts || question?.keywords || [];
  const misconception = (question?.misconception_tags || ['incomplete_conceptual_elaboration'])[0];

  let selected = [];
  let explanation = '';
  if (answer && typeof answer === 'object' && !Array.isArray(answer)) {
    selected = Array.isArray(answer.keywords) ? answer.keywords : [];
    if (Array.isArray(answer.parts)) {
      explanation = answer.parts.filter(Boolean).join(' ');
    } else {
      explanation = String(answer.explanation || answer.value || '');
    }
  } else if (Array.isArray(answer)) {
    selected = answer;
    explanation = answer.filter(Boolean).join(' ');
  } else {
    explanation = String(answer || '');
  }

  const studentCorpus = `${selected.join(' ')} ${explanation}`.toLowerCase().trim();
  if (!studentCorpus) {
    return {
      is_correct: false,
      score: 0,
      max_score: maxScore,
      feedback: 'No answer provided.',
      awarded_points: [],
      matched_concepts: [],
      misconception_tag: misconception,
      graded_by: 'offline_concept_stemmer',
      queued_for_online_llm: false,
    };
  }

  const studentWords = studentCorpus.match(/[a-z0-9_-]+/g) || [];
  const studentStems = new Set(studentWords.filter((w) => w.length >= 3).map(stemWord));

  const rawMarkingPoints =
    question?.marking_schema?.marking_points ||
    question?.marking_points ||
    question?.content_rubric ||
    [];

  const awardedPoints = [];
  let earnedScore = 0;

  if (Array.isArray(rawMarkingPoints) && rawMarkingPoints.length > 0) {
    rawMarkingPoints.forEach((mp, idx) => {
      const pId = typeof mp === 'object' ? (mp.id || `mp_${idx + 1}`) : `mp_${idx + 1}`;
      const pDesc = typeof mp === 'object' ? (mp.desc || mp.point || mp.criterion || '') : String(mp);
      const pMarks = typeof mp === 'object' ? Number(mp.marks || mp.max_marks || 2) : 1;
      const pConcepts = typeof mp === 'object' ? (mp.concepts || mp.target_concepts || mp.key_concepts || []) : [];

      let achieved = false;
      if (pConcepts.length > 0) {
        const matchedC = pConcepts.filter((c) => conceptMatchesCorpus(c, studentCorpus, studentStems));
        if (matchedC.length >= Math.max(1, Math.floor(pConcepts.length / 2))) {
          achieved = true;
        }
      }
      if (!achieved && pDesc) {
        const stopWords = new Set(['explain', 'discuss', 'outline', 'state', 'describe', 'impact', 'marks', 'point', 'correct', 'target', 'value', 'learner', 'student', 'identifies', 'mentions', 'states']);
        const meaningful = (pDesc.toLowerCase().match(/[a-z0-9_-]+/g) || []).filter((w) => w.length > 3 && !stopWords.has(w));
        if (meaningful.length > 0) {
          const matchedW = meaningful.filter((w) => conceptMatchesCorpus(w, studentCorpus, studentStems));
          if (matchedW.length >= Math.max(1, Math.ceil(meaningful.length / 3))) {
            achieved = true;
          }
        }
      }
      if (achieved) {
        earnedScore += pMarks;
        awardedPoints.push({ id: pId, marks: pMarks, desc: pDesc });
      }
    });
  } else if (expectedKeywords.length > 0) {
    const matched = expectedKeywords.filter((k) => conceptMatchesCorpus(k, studentCorpus, studentStems));
    earnedScore = Math.min(maxScore, matched.length * 2);
  }

  earnedScore = Math.min(earnedScore, maxScore);
  const isCorrect = earnedScore >= maxScore * 0.6;
  const queued = earnedScore < maxScore && studentWords.length >= 4;
  if (queued) {
    enqueueOfflineSemanticSubmission({ question, answer, provisionalScore: earnedScore, timestamp: Date.now() });
  }

  return {
    is_correct: isCorrect,
    score: earnedScore,
    max_score: maxScore,
    feedback: queued
      ? `Provisional offline rubric score: ${earnedScore} / ${maxScore} marks (queued for AI semantic verification when online).`
      : `Awarded ${earnedScore} / ${maxScore} marks (offline concept & synonym rubric).`,
    awarded_points: awardedPoints,
    matched_concepts: expectedKeywords.filter((k) => conceptMatchesCorpus(k, studentCorpus, studentStems)),
    misconception_tag: isCorrect ? undefined : misconception,
    graded_by: 'offline_concept_stemmer',
    queued_for_online_llm: queued,
  };
}

export function enqueueOfflineSemanticSubmission(item) {
  if (typeof window === 'undefined' || !window.localStorage) return;
  try {
    const raw = window.localStorage.getItem(OFFLINE_QUEUE_KEY);
    const list = raw ? JSON.parse(raw) : [];
    list.push({
      id: `${item.question?.id || 'q'}_${Date.now()}`,
      question: item.question,
      answer: item.answer,
      provisionalScore: item.provisionalScore,
      timestamp: item.timestamp || Date.now(),
    });
    window.localStorage.setItem(OFFLINE_QUEUE_KEY, JSON.stringify(list.slice(-50)));
  } catch {
    // Ignore storage quota errors
  }
}

export function getOfflineSemanticQueue() {
  if (typeof window === 'undefined' || !window.localStorage) return [];
  try {
    const raw = window.localStorage.getItem(OFFLINE_QUEUE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

export async function flushOfflineSemanticQueue(apiUrl = 'http://localhost:5001', onReconciled = null) {
  if (typeof window === 'undefined' || (typeof navigator !== 'undefined' && !navigator.onLine)) {
    return { flushed: 0 };
  }
  const queue = getOfflineSemanticQueue();
  if (!queue.length) return { flushed: 0 };

  let flushed = 0;
  const remaining = [];
  for (const entry of queue) {
    try {
      const resp = await fetch(`${apiUrl}/api/evaluate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          questions: [entry.question],
          answers: { [entry.question?.id || 'q1']: entry.answer },
        }),
      });
      if (resp.ok) {
        const data = await resp.json();
        const res = data?.results?.[entry.question?.id || 'q1'];
        flushed += 1;
        if (res && typeof onReconciled === 'function') {
          onReconciled(entry, res);
        }
      } else {
        remaining.push(entry);
      }
    } catch {
      remaining.push(entry);
    }
  }
  try {
    window.localStorage.setItem(OFFLINE_QUEUE_KEY, JSON.stringify(remaining));
  } catch {
    // ignore
  }
  return { flushed, remaining: remaining.length };
}
