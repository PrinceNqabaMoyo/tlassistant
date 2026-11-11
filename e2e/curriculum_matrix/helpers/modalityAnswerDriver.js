import { expect } from '@playwright/test';

/**
 * Modality Answer Driver for Fundile Curriculum & Archetype Matrix
 * Enforces Rules 0d-1 through 0d-12:
 * - Zero silent skips (no `if (isVisible())` or `if (count() > 0)`)
 * - All union selectors filter by `:visible`
 * - Uses only authentic `data-testid` attributes grounded in `src/`
 */

/**
 * Resolves the active cognitive modality from a normalized question payload,
 * matching UniversalWorkspace.jsx 1-for-1.
 */
export function resolveExpectedModality(question, topic = '') {
  const topLower = String(topic || question?.topic || '').toLowerCase();

  if (
    question?.modality === 'geometric_nets' ||
    topLower.includes('geometry of 3d') ||
    topLower.includes('geometric net') ||
    topLower.includes('3d object') ||
    topLower.includes('platonic solid')
  ) return 'geometric_nets';

  if (
    question?.modality === 'electrodynamics' ||
    topLower.includes('electrodynamics') ||
    topLower.includes('ac generator') ||
    topLower.includes('dc motor') ||
    topLower.includes('armature')
  ) return 'electrodynamics';

  if (
    question?.modality === 'organic_chemistry' ||
    topLower.includes('organic chemistry') ||
    topLower.includes('isomer') ||
    topLower.includes('homologous series')
  ) return 'organic_chemistry';

  if (
    question?.modality === 'arithmetic_grid' ||
    Boolean(question?.arithmetic_grid) ||
    topLower.includes('long division')
  ) return 'arithmetic_grid';

  // Science Visual Modalities
  if (
    question?.modality === 'circuit' ||
    Boolean(question?.circuit_spec)
  ) return 'circuit';

  if (
    question?.modality === 'punnett_square' ||
    question?.modality === 'punnett' ||
    Boolean(question?.punnett_spec)
  ) return 'punnett_square';

  if (
    question?.modality === 'bio_diagram' ||
    question?.modality === 'biological_labeling'
  ) return 'bio_diagram';

  if (
    question?.modality === 'free_body_diagram' ||
    Boolean(question?.fbd_spec)
  ) return 'free_body_diagram';

  if (question?.modality === 'ledger' || question?.journal || question?.table_schema) return 'ledger';
  if (question?.options || question?.options_latex || question?.question_type === 'mcq') return 'math';
  if (question?.modality === 'diagram' || question?.question_type === 'diagram_select' || Boolean(question?.correct_edge)) return 'diagram';

  if (question?.modality === 'math') return 'math';
  if (question?.modality === 'semantic' || question?.modality === 'rubric') return 'semantic';

  if (
    ['rubric', 'essay', 'short_answer', 'conceptual'].includes(question?.question_type) ||
    Boolean(question?.content_rubric || question?.marking_points)
  ) {
    return 'semantic';
  }

  return question?.modality || 'math';
}

/**
 * Resolves the sub-type inside MathAnswerArea.jsx ('mcq' | 'diagram_select' | 'math_steps' | 'math_short')
 */
export function resolveMathSubType(question) {
  const rawType = String(question?.question_type || '').toLowerCase();
  if (
    rawType === 'mcq' ||
    (Array.isArray(question?.options) && question.options.length > 0) ||
    (Array.isArray(question?.options_latex) && question.options_latex.length > 0)
  ) {
    return 'mcq';
  }
  if (rawType === 'diagram_select' || Boolean(question?.correct_edge)) {
    return 'diagram_select';
  }
  if (rawType === 'math_steps') {
    return 'math_steps';
  }
  return 'math_short';
}

/**
 * Builds the canonical 100% answer payload for a normalized question
 * (used in Tier 1 API Grading Triad and Tier 2 Live UI Driver).
 */
export function buildCanonicalAnswer(question) {
  if (!question) return '';

  const qType = String(question.question_type || '').toLowerCase();
  const modality = question.modality || '';

  // 1. Arithmetic Grid (Long Division)
  if (modality === 'arithmetic_grid' || Boolean(question.arithmetic_grid)) {
    const grid = question.arithmetic_grid || {};
    return {
      quotient: String(grid.quotient ?? question.correct_quotient ?? question.expected_answer ?? 169),
      remainder: String(grid.remainder ?? question.correct_remainder ?? 0)
    };
  }

  // 2. MCQ
  if (qType === 'mcq' || (Array.isArray(question.options) && question.options.length > 0)) {
    if (typeof question.correct_index === 'number') {
      return question.correct_index;
    }
    const target = String(question.expected_answer ?? question.correct_answer ?? question.sample_answer ?? '').trim();
    const idx = (question.options || []).findIndex((o) => String(o).trim() === target);
    return idx >= 0 ? idx : (target || 0);
  }

  // 3. Diagram Select
  if (qType === 'diagram_select' || modality === 'diagram' || Boolean(question.correct_edge)) {
    return String(question.correct_edge || question.expected_answer || question.correct_answer || 'AB');
  }

  // 4. Ledger / Table
  if (modality === 'ledger' || question.table_schema || question.journal || ['table', 'ledger', 'tabular_fill', 'table_completion'].includes(qType)) {
    const srcMap = (question.correct_map && typeof question.correct_map === 'object' && Object.keys(question.correct_map).length > 0)
      ? question.correct_map
      : (question.expected_answer && typeof question.expected_answer === 'object' ? question.expected_answer : null);
    if (srcMap) {
      const cleaned = {};
      for (const [k, v] of Object.entries(srcMap)) {
        cleaned[k] = Array.isArray(v) ? String(v[0] ?? '') : v;
      }
      return cleaned;
    }
  }

  // 5. Semantic / Rubric
  if (modality === 'semantic' || modality === 'rubric' || ['rubric', 'essay', 'short_answer', 'conceptual'].includes(qType)) {
    const explanation = String(
      question.model_answer ||
      question.ideal_answer ||
      question.sample_answer ||
      question.expected_answer ||
      question.worked_solution ||
      question.explanation ||
      ''
    );
    const keywords = Array.isArray(question.keywords)
      ? question.keywords
      : Array.isArray(question.key_concepts)
        ? question.key_concepts
        : [];
    return {
      keywords,
      explanation
    };
  }

  // 6. Math Steps
  if (qType === 'math_steps') {
    const steps = question.canonical_solution?.steps || [];
    if (steps.length > 0) {
      return steps.map((st) => String(st.to_latex || st.step || question.expected_answer || '')).filter(Boolean);
    }
  }

  // 6b. Multi-Part Questions (sub_parts)
  if (Array.isArray(question.sub_parts) && question.sub_parts.length > 1) {
    return {
      parts: question.sub_parts.map((p) => String(p.expected_answer || p.answer_latex || '')),
      value: question.sub_parts.map((p) => String(p.expected_answer || p.answer_latex || '')).join('; ')
    };
  }

  // 7. Standard Math / Typed / Calculation
  const rawAns =
    question.expected_answer ??
    question.correct_answer ??
    question.canonical_solution?.final_latex ??
    question.sample_answer ??
    question.final_answer ??
    question.answer_latex ??
    question.model_answer ??
    '';
  if (typeof rawAns === 'object' && rawAns !== null) {
    return JSON.stringify(rawAns);
  }
  return String(rawAns);
}

/**
 * Builds a partial-credit answer payload for questions with marks >= 2
 * (awarding method marks: 0 < score < max_score).
 */
export function buildPartialAnswer(question) {
  if (!question) return '';
  const modality = question.modality || '';
  const qType = String(question.question_type || '').toLowerCase();

  // 1. Ledger: fill half the cells accurately
  if (modality === 'ledger' && question.correct_map && typeof question.correct_map === 'object') {
    const entries = Object.entries(question.correct_map);
    if (entries.length >= 2) {
      const half = Math.max(1, Math.floor(entries.length / 2));
      return { ...Object.fromEntries(entries.slice(0, half)), __partial_method__: true };
    }
  }

  // 2. Arithmetic Grid: provide intermediate sub-step product or quotient only with wrong remainder
  if (modality === 'arithmetic_grid' || question.arithmetic_grid) {
    const grid = question.arithmetic_grid || {};
    return {
      quotient: String(grid.quotient ?? question.correct_quotient ?? 169),
      remainder: '999',
      __partial_method__: true
    };
  }

  // 3. Semantic / Rubric: include half of the keywords or first sentence of explanation
  if (modality === 'semantic' || modality === 'rubric' || ['rubric', 'essay', 'short_answer', 'conceptual'].includes(qType)) {
    const kws = Array.isArray(question.keywords) ? question.keywords : [];
    if (kws.length >= 2) {
      return {
        keywords: kws.slice(0, Math.max(1, Math.floor(kws.length / 2))),
        explanation: kws.slice(0, Math.max(1, Math.floor(kws.length / 2))).join(' '),
        __partial_method__: true
      };
    }
    const modelText = String(question.sample_answer || question.model_answer || question.expected_answer || '');
    const words = modelText.split(/\s+/).filter(Boolean);
    return {
      keywords: [],
      explanation: words.slice(0, Math.max(2, Math.floor(words.length / 3))).join(' '),
      __partial_method__: true
    };
  }

  // 3b. Multi-Part Questions (sub_parts): fill half the parts accurately, half wrong
  if (Array.isArray(question.sub_parts) && question.sub_parts.length > 1) {
    const half = Math.max(1, Math.floor(question.sub_parts.length / 2));
    const parts = question.sub_parts.map((p, idx) => (idx < half ? String(p.expected_answer || p.answer_latex || '') : '-999999'));
    return {
      parts,
      value: parts.join('; '),
      __partial_method__: true
    };
  }

  // 4. Math / Typed with intermediate steps: provide the first intermediate step
  const steps = question.canonical_solution?.steps || [];
  if (steps.length >= 2) {
    const firstStep = steps[0].to_latex || steps[0].step || '';
    if (firstStep && firstStep !== String(question.expected_answer)) {
      return '__PARTIAL_METHOD_STEP__';
    }
  }

  return '__PARTIAL_METHOD_STEP__';
}

/**
 * Builds a known distractor / wrong answer payload (expected 0 marks + misconception_tag).
 */
export function buildWrongAnswer(question) {
  if (!question) return 'incorrect_response_xyz';
  const modality = question.modality || '';
  const qType = String(question.question_type || '').toLowerCase();

  if (Array.isArray(question.sub_parts) && question.sub_parts.length > 1) {
    const parts = question.sub_parts.map(() => '-999999');
    return {
      parts,
      value: parts.join('; ')
    };
  }

  if (modality === 'arithmetic_grid' || question.arithmetic_grid) {
    return { quotient: '999999', remainder: '888' };
  }

  if (qType === 'mcq' || (Array.isArray(question.options) && question.options.length > 0)) {
    const correctIdx = typeof question.correct_index === 'number' ? question.correct_index : 0;
    return (correctIdx + 1) % Math.max(2, (question.options || []).length);
  }

  if (qType === 'diagram_select' || modality === 'diagram' || Boolean(question.correct_edge)) {
    const rightEdge = String(question.correct_edge || 'AB');
    return rightEdge === 'AB' ? 'BC' : 'AB';
  }

  if (modality === 'ledger') {
    const cmap = question.correct_map || {};
    const wrongMap = {};
    for (const k of Object.keys(cmap)) {
      wrongMap[k] = '999999.99';
    }
    return Object.keys(wrongMap).length > 0 ? wrongMap : { cell_0: '999999.99' };
  }

  if (modality === 'semantic' || modality === 'rubric') {
    return {
      keywords: [],
      explanation: 'Completely unrelated incorrect distractor statement with zero target concepts.'
    };
  }

  // Check if common_errors has a known distractor value
  const commonErrors = question.common_errors || [];
  if (Array.isArray(commonErrors) && commonErrors.length > 0 && commonErrors[0]?.value !== undefined) {
    return String(commonErrors[0].value);
  }

  return '-999999.876';
}

/**
 * Enters either the canonical (100%) or wrong (0%) answer directly into the live
 * browser DOM for the currently rendered question in UniversalWorkspace, clicks
 * Check, and returns the question and user input used.
 */
export async function enterAndSubmitLiveAnswer(page, { answerType = 'canonical', topic = '' } = {}) {
  const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
  await expect(questionSurface).toBeVisible({ timeout: 15000 });

  // Wait for active question to be hydrated on window
  await page.waitForFunction(() => Boolean(window.__FUNDILE_ACTIVE_QUESTION__), { timeout: 15000 });
  const question = await page.evaluate(() => window.__FUNDILE_ACTIVE_QUESTION__);
  expect(question, 'Live UniversalWorkspace question must be mounted').toBeTruthy();

  const domModality = (await questionSurface.getAttribute('data-modality')) || resolveExpectedModality(question, topic);
  let submittedValue = null;

  if (domModality === 'arithmetic_grid') {
    const payload = answerType === 'canonical' ? buildCanonicalAnswer(question) : buildWrongAnswer(question);
    submittedValue = payload;

    const quotientInput = page.locator('[data-testid="input-quotient"]:visible').first();
    const remainderInput = page.locator('[data-testid="input-remainder"]:visible').first();
    await expect(quotientInput).toBeVisible({ timeout: 10000 });
    await expect(remainderInput).toBeVisible({ timeout: 10000 });

    await quotientInput.fill(String(payload.quotient));
    await remainderInput.fill(String(payload.remainder));
  } else if (domModality === 'ledger') {
    // Extract editable cell IDs from question payload (including statement header titleFields)
    const editableCells = extractEditableLedgerCells(question);
    const cellPayload = {};

    const cellsToInteract = answerType === 'canonical'
      ? editableCells.filter(({ expected }) => String(expected ?? '').trim() !== '')
      : editableCells.slice(0, Math.min(3, editableCells.length));

    for (const { cellId, expected } of cellsToInteract) {
      const valToFill = answerType === 'canonical' ? String(expected) : '999999';
      cellPayload[cellId] = valToFill;
      const cellInput = page.locator(`[data-testid="ledger-cell-${cellId}"]:visible`).first();
      await expect(cellInput).toBeVisible({ timeout: 10000 });
      await cellInput.fill(valToFill);
    }
    submittedValue = cellPayload;
  } else if (domModality === 'diagram') {
    const targetEdge = answerType === 'canonical'
      ? String(question.correct_edge || question.expected_answer || question.correct_answer || 'AB')
      : (String(question.correct_edge || 'AB') === 'AB' ? 'BC' : 'AB');
    submittedValue = targetEdge;

    const edgeBtn = page.locator(`[data-testid="btn-diagram-edge-${targetEdge}"]:visible`).first();
    await expect(edgeBtn).toBeVisible({ timeout: 10000 });
    await edgeBtn.click();
  } else if (domModality === 'semantic' || domModality === 'rubric') {
    const payload = answerType === 'canonical' ? buildCanonicalAnswer(question) : buildWrongAnswer(question);
    submittedValue = payload;

    const explanationTextarea = page.locator('[data-testid="input-rubric-explanation"]:visible').first();
    await expect(explanationTextarea).toBeVisible({ timeout: 10000 });

    const textToFill = typeof payload === 'object' ? String(payload.explanation || '') : String(payload);
    await explanationTextarea.fill(textToFill || String(question.sample_answer || question.expected_answer || 'Canonical concept analysis'));
  } else {
    // 'math', 'geometric_nets', 'electrodynamics', 'organic_chemistry'
    const mathSubType = resolveMathSubType(question);

    if (mathSubType === 'mcq') {
      const options = question.options || question.options_latex || [];
      let targetIdx = 0;
      if (typeof question.correct_index === 'number') {
        targetIdx = question.correct_index;
      } else {
        const expectedStr = String(question.expected_answer ?? question.correct_answer ?? question.sample_answer ?? '').trim();
        const found = options.findIndex((o) => String(o).trim() === expectedStr);
        targetIdx = found >= 0 ? found : 0;
      }
      if (answerType === 'wrong') {
        targetIdx = (targetIdx + 1) % Math.max(2, options.length);
      }
      submittedValue = targetIdx;

      const optBtn = page.locator(`[data-testid="btn-math-option-${targetIdx}"]:visible`).first();
      await expect(optBtn).toBeVisible({ timeout: 10000 });
      await optBtn.click();
    } else if (mathSubType === 'diagram_select') {
      const targetEdge = answerType === 'canonical'
        ? String(question.correct_edge || question.expected_answer || 'AB')
        : (String(question.correct_edge || 'AB') === 'AB' ? 'BC' : 'AB');
      submittedValue = targetEdge;

      const edgeBtn = page.locator(`[data-testid="btn-diagram-edge-${targetEdge}"]:visible`).first();
      await expect(edgeBtn).toBeVisible({ timeout: 10000 });
      await edgeBtn.click();
    } else if (mathSubType === 'math_steps') {
      const stepVal = answerType === 'canonical'
        ? String(question.expected_answer ?? question.correct_answer ?? question.canonical_solution?.final_latex ?? question.sample_answer ?? '1')
        : '-999999';
      submittedValue = [stepVal];

      const stepInput = page.locator('[data-testid="input-math-step-0"]:visible').first();
      await expect(stepInput).toBeVisible({ timeout: 10000 });
      await stepInput.fill(stepVal);
    } else {
      const shortVal = answerType === 'canonical'
        ? String(question.expected_answer ?? question.correct_answer ?? question.canonical_solution?.final_latex ?? question.sample_answer ?? question.final_answer ?? '1')
        : '-999999.876';
      submittedValue = shortVal;

      const partInputs = page.locator('[data-testid^="input-math-answer-part-"]:visible');
      const partCount = await partInputs.count();
      if (partCount > 1) {
        const subParts = question.sub_parts || [];
        const filledParts = [];
        for (let pIdx = 0; pIdx < partCount; pIdx++) {
          const pExp = subParts[pIdx]?.expected_answer || subParts[pIdx]?.answer_latex || `part_${pIdx + 1}`;
          const pVal = answerType === 'canonical' ? String(pExp) : '-999999';
          await partInputs.nth(pIdx).fill(pVal);
          filledParts.push(pVal);
        }
        submittedValue = filledParts.join('; ');
      } else {
        const mathInput = page.locator('[data-testid="input-math-answer"]:visible, [data-testid="input-math-answer-part-0"]:visible').first();
        await expect(mathInput).toBeVisible({ timeout: 10000 });
        await mathInput.fill(shortVal);
      }
    }
  }

  const checkBtn = page.locator('[data-testid="btn-check-answer"]:visible').first();
  await expect(checkBtn).toBeVisible({ timeout: 10000 });
  await expect(checkBtn).toBeEnabled({ timeout: 10000 });
  await checkBtn.click();

  await expect(page.locator('[data-testid="banner-marks-awarded"]:visible').first()).toBeVisible({ timeout: 15000 });

  return {
    question,
    domModality,
    submittedValue
  };
}

function extractEditableLedgerCells(question) {
  const result = [];
  const seenIds = new Set();
  const rows = question?.journal?.rows || question?.rows || question?.table_schema?.rows || [];
  const titleFields = question?.journal?.title_fields || question?.title_fields || [];
  const correctMap = question?.correct_map || question?.expected_cells || question?.expected_values || {};

  const unwrapExpected = (val) => {
    if (Array.isArray(val)) return String(val[0] ?? '');
    if (val === undefined || val === null) return '';
    return String(val);
  };

  // 1. Statement Header Bar title_fields
  if (Array.isArray(titleFields)) {
    for (const field of titleFields) {
      if (field && field.cell_id && field.editable !== false) {
        const cellId = field.cell_id;
        const rawExp = correctMap[cellId] !== undefined ? correctMap[cellId] : (field.expected ?? field.value ?? '');
        seenIds.add(cellId);
        result.push({ cellId, expected: unwrapExpected(rawExp) });
      }
    }
  }

  // 2. 2D Tabular Grid rows
  if (Array.isArray(rows) && rows.length > 0) {
    rows.forEach((row, rIdx) => {
      const cells = Array.isArray(row) ? row : (row?.cells || []);
      cells.forEach((cell, cIdx) => {
        if (cell && typeof cell === 'object') {
          const cellId = cell.cell_id || cell.id || cell.coordinate || `r${rIdx}_c${cIdx}`;
          const isEditable = Boolean(
            cell.editable ||
            cell.type === 'required' ||
            cell.type === 'input' ||
            cell.is_input ||
            (correctMap && cellId in correctMap)
          );
          if (isEditable && !seenIds.has(cellId)) {
            const rawExp =
              correctMap[cellId] !== undefined
                ? correctMap[cellId]
                : (cell.expected !== undefined && String(cell.expected) !== ''
                    ? cell.expected
                    : (cell.solution ?? cell.answer ?? cell.value ?? ''));
            seenIds.add(cellId);
            result.push({ cellId, expected: unwrapExpected(rawExp) });
          }
        }
      });
    });
  }

  if (result.length === 0 && Object.keys(correctMap).length > 0) {
    for (const [cellId, rawExp] of Object.entries(correctMap)) {
      result.push({ cellId, expected: unwrapExpected(rawExp) });
    }
  }

  return result;
}
