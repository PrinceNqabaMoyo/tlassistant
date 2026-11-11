#!/usr/bin/env node
/**
 * scripts/audit_all_archetypes_pipeline.js
 *
 * Full-Platform Archetype Quality, Anti-Leak & Multi-Scroll Screenshot Pipeline
 * Implements Rule 0d and Rule 30 (.agents/AGENTS.md).
 *
 * Usage:
 *   node scripts/audit_all_archetypes_pipeline.js --grade 7
 *   node scripts/audit_all_archetypes_pipeline.js --grade 7 --only "Whole Numbers"
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright';
import { spawnSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');
const OUTPUT_DIR = path.join(PROJECT_ROOT, 'reports', 'full_archetype_audit');
const SHOTS_DIR = path.join(OUTPUT_DIR, 'shots');

if (!fs.existsSync(SHOTS_DIR)) {
  fs.mkdirSync(SHOTS_DIR, { recursive: true });
}

function parseArgs() {
  const args = process.argv.slice(2);
  const cfg = {
    grade: '7',
    url: 'http://localhost:5173',
    only: null,
  };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--grade' && args[i + 1]) cfg.grade = args[++i].trim();
    else if (args[i] === '--url' && args[i + 1]) cfg.url = args[++i].trim();
    else if (args[i] === '--only' && args[i + 1]) cfg.only = args[++i].trim();
  }
  return cfg;
}

// Helper to query python backend for curriculum catalog and question variants
function getCatalogForGrade(grade) {
  const pyCode = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.caps_term_curriculum_registry import _ALL_TOPIC_RECORDS
from app.services.generator_registry import get_topic_archetypes

records = [r for r in _ALL_TOPIC_RECORDS if str(r.get('grade')) == '${grade}']
catalog = []
for r in records:
    subj = r['subject']
    top = r['name']
    term = r.get('term', 1)
    info = get_topic_archetypes(top, '${grade}', subj)
    archs = info.get('archetypes') or []
    catalog.append({
        'subject': subj,
        'topic': top,
        'term': term,
        'archetypes': archs,
        'modalities': info.get('modalities', ['math']),
    })
print(json.dumps(catalog))
`;
  const res = spawnSync('.\\caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', pyCode], {
    cwd: PROJECT_ROOT,
    encoding: 'utf-8',
    maxBuffer: 32 * 1024 * 1024,
  });
  if (res.error || res.status !== 0) {
    throw new Error('Failed to fetch catalog: ' + (res.stderr || res.stdout));
  }
  return JSON.parse(res.stdout.trim());
}

function generateArchetypesPayload(topic, grade, subject, archetypes) {
  const pyCode = `
import sys, json
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import generate_variant

topic = ${JSON.stringify(topic)}
subject = ${JSON.stringify(subject)}
grade = '${grade}'
archs = ${JSON.stringify(archetypes)}

def gen_batch(seed):
    out = []
    for a in archs:
        try:
            res = generate_variant(topic=topic, subskill=a, grade=grade, subject=subject, seed=seed, count=1)
            out.append(res[0] if res else {})
        except Exception as e:
            out.append({'prompt': f'Error generating archetype {a}: {e}', 'archetype_error': str(e)})
    return out

print(json.dumps({
    's101': gen_batch(101),
    's202': gen_batch(202),
    's303': gen_batch(303)
}))
`;
  const res = spawnSync('.\\caps-ai-backend\\venv\\Scripts\\python.exe', ['-c', pyCode], {
    cwd: PROJECT_ROOT,
    encoding: 'utf-8',
    maxBuffer: 32 * 1024 * 1024,
  });
  if (res.error || res.status !== 0) {
    throw new Error(`Failed to generate ${subject} Gr${grade} ${topic}: ` + (res.stderr || res.stdout));
  }
  return JSON.parse(res.stdout.trim());
}

function sanitizeSlug(str) {
  return String(str || '').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
}

async function captureMultiScroll(page, baseFilename, fullPage = false) {
  let retries = 2;
  while (retries >= 0) {
    try {
      const scrollInfo = await page.evaluate(() => {
        return {
          scrollHeight: document.documentElement.scrollHeight,
          clientHeight: window.innerHeight,
        };
      });

      const relativePaths = [];
      const vpHeight = scrollInfo.clientHeight;
      const totalHeight = scrollInfo.scrollHeight;

      // First scroll shot at top
      await page.evaluate(() => {
        const el = document.getElementById('harness-scroll-step-badge');
        if (el) el.innerText = 'SCROLL_1_TOP';
        window.scrollTo(0, 0);
      });
      await page.waitForTimeout(100);
      const shot1Rel = path.relative(PROJECT_ROOT, path.join(SHOTS_DIR, `${baseFilename}_scroll_1.png`)).replace(/\\/g, '/');
      await page.screenshot({ path: path.join(PROJECT_ROOT, shot1Rel) });
      relativePaths.push(shot1Rel);

      // If page is taller than viewport + 60px, scroll down step-by-step
      if (totalHeight > vpHeight + 60) {
        let currentTop = 0;
        let step = 1;
        const stepIncrement = 750;
        while (currentTop + vpHeight < totalHeight) {
          currentTop = Math.min(currentTop + stepIncrement, totalHeight - vpHeight);
          step++;
          await page.evaluate(({ s, top }) => {
            const el = document.getElementById('harness-scroll-step-badge');
            if (el) el.innerText = `SCROLL_${s}_Y${top}`;
            window.scrollTo(0, top);
          }, { s: step, top: currentTop });
          await page.waitForTimeout(100);
          const shotStepRel = path.relative(PROJECT_ROOT, path.join(SHOTS_DIR, `${baseFilename}_scroll_${step}.png`)).replace(/\\/g, '/');
          await page.screenshot({ path: path.join(PROJECT_ROOT, shotStepRel) });
          relativePaths.push(shotStepRel);
          if (currentTop + vpHeight >= totalHeight) break;
        }
      }

      // Also take fullPage stitch if requested
      if (fullPage) {
        await page.evaluate(() => {
          const el = document.getElementById('harness-scroll-step-badge');
          if (el) el.innerText = 'SCROLL_FULL';
          window.scrollTo(0, 0);
        });
        await page.waitForTimeout(50);
        const fullRel = path.relative(PROJECT_ROOT, path.join(SHOTS_DIR, `${baseFilename}_full.png`)).replace(/\\/g, '/');
        await page.screenshot({ path: path.join(PROJECT_ROOT, fullRel), fullPage: true });
      }

      // Reset scroll position back to top
      await page.evaluate(() => {
        window.scrollTo(0, 0);
      });

      return {
        relativePaths,
        shots: relativePaths,
        totalHeight,
        viewportHeight: vpHeight,
        vpHeight,
        scrollSteps: relativePaths.length,
        stepCount: relativePaths.length,
      };
    } catch (err) {
      if (err.message && err.message.includes('Execution context was destroyed') && retries > 0) {
        retries--;
        await page.waitForLoadState('domcontentloaded');
        await page.waitForTimeout(300);
        continue;
      }
      throw err;
    }
  }
}

async function runPipeline() {
  const cfg = parseArgs();
  console.log(`\n======================================================`);
  console.log(`🚀 Full-Archetype Quality & Multi-Scroll Screenshot Pipeline`);
  console.log(`   Grade: ${cfg.grade} | URL: ${cfg.url}`);
  console.log(`======================================================\n`);

  const catalog = getCatalogForGrade(cfg.grade);
  console.log(`Loaded ${catalog.length} topics for Grade ${cfg.grade}.`);

  const ledgerPath = path.join(OUTPUT_DIR, `ledger_gr${cfg.grade}.json`);
  const ledger = {
    grade: cfg.grade,
    timestamp: new Date().toISOString(),
    total_topics: catalog.length,
    archetypes: [],
    remediations: [],
  };

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  page.on('console', msg => {
    if (msg.type() === 'error') console.log(`  [UI Console Error]:`, msg.text());
  });

  const harnessUrl = `${cfg.url}/?harness=universal_workspace`;
  console.log(`Mounting UniversalWorkspace harness at ${harnessUrl}...`);
  await page.goto(harnessUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForSelector('[data-testid="universal-workspace-harness-ready"]', { timeout: 15000 });
  console.log(`UniversalWorkspace harness ready in browser!\n`);

  let archetypeIndex = 0;
  for (const topicRecord of catalog) {
    const { subject, topic, term, archetypes } = topicRecord;

    if (cfg.only && !topic.toLowerCase().includes(cfg.only.toLowerCase())) {
      continue;
    }

    console.log(`\n📘 [Topic ${subject} | Gr${cfg.grade} | ${topic}] (${archetypes.length} archetypes)`);

    // Generate questions for seeds 101, 202, 303 for every archetype explicitly
    let batches;
    try {
      batches = generateArchetypesPayload(topic, cfg.grade, subject, archetypes);
    } catch (err) {
      console.error(`  ❌ Generator failure for ${topic}:`, err.message);
      ledger.archetypes.push({
        subject, topic, archetype_id: 'generator_crash',
        unresolved_defects: [`Generator crashed: ${err.message}`]
      });
      continue;
    }

    for (let aIdx = 0; aIdx < archetypes.length; aIdx++) {
      const archName = archetypes[aIdx];
      archetypeIndex++;
      const q101 = batches.s101[aIdx] || {};
      const q202 = batches.s202[aIdx] || {};
      const q303 = batches.s303[aIdx] || {};

      // Explicitly stamp active subskill/archetype on question objects
      q101.subskill = archName;
      q101.archetype = archName;
      q202.subskill = archName;
      q202.archetype = archName;
      q303.subskill = archName;
      q303.archetype = archName;

      const topicSlug = sanitizeSlug(topic);
      const subjSlug = sanitizeSlug(subject);
      const archSlug = sanitizeSlug(archName);
      const basePrefix = `gr${cfg.grade}_${subjSlug}_${topicSlug}_${archSlug}`;

      process.stdout.write(`  [${archetypeIndex}] Archetype '${archName}' ... `);

      // 1. Mount question into live React UniversalWorkspace
      await page.evaluate(({ q, grade, subject, topic }) => {
        return window.__SET_WORKSPACE_QUESTION__(q, { grade, subject, topic, mode: 'practice' });
      }, { q: q101, grade: cfg.grade, subject, topic });

      await page.waitForSelector('[data-testid="question-surface"]', { state: 'visible', timeout: 10000 });
      await page.waitForTimeout(150); // allow KaTeX & diagrams to settle

      // 2. Capture Pre-Attempt Multi-Scroll Screenshots
      const preCapture = await captureMultiScroll(page, `${basePrefix}_pre`, true);

      // 3. Run Deterministic Quality Checks on Pre-Attempt DOM (0 LLM Tokens)
      const defects = [];
      const preDomText = await page.locator('[data-testid="question-surface"]').innerText();

      // Check 1: Anti-Leak (Ensure answer is not given away in prompt text)
      const ansRaw = String(q101.correct_answer || q101.sample_answer || '').trim();
      if (ansRaw.length >= 3 && !/^(true|false|[a-d]|yes|no)$/i.test(ansRaw)) {
        const promptOnly = String(q101.question || q101.prompt || q101.question_text || '');
        if (promptOnly.includes(ansRaw)) {
          defects.push(`[ANSWER_LEAK] Final answer '${ansRaw}' appears verbatim in question prompt.`);
        }
      }

      // Check 2: Aesthetic / Code / LaTeX leaks
      if (/\\(frac|sqrt|text|begin|right|left)\{/.test(preDomText) || /\$\$/.test(preDomText)) {
        defects.push(`[RAW_LATEX_LEAK] Raw LaTeX tokens found in rendered student prompt.`);
      }
      if (/\b(undefined|NaN)\b|\[object Object\]/.test(preDomText)) {
        defects.push(`[JS_TOKEN_LEAK] Page contains undefined/NaN/[object Object].`);
      }
      if (/\bCAPS\b/.test(preDomText)) {
        defects.push(`[BANNED_CAPS_ACRONYM] Prompt displays banned 'CAPS' acronym.`);
      }

      // 4. Trigger Memorandum & Worked Procedure Reveal
      await page.evaluate(() => {
        if (typeof window.__TRIGGER_WORKSPACE_MEMO__ === 'function') {
          window.__TRIGGER_WORKSPACE_MEMO__();
        }
      });
      await page.waitForSelector('[data-testid="panel-full-memo"]', { state: 'visible', timeout: 5000 });
      await page.waitForTimeout(200);

      // 5. Capture Post-Attempt / Sample Answer Multi-Scroll Screenshots
      const memoCapture = await captureMultiScroll(page, `${basePrefix}_memo`, true);

      // Check 4: Informative Worked Procedure Depth for questions >= 2 marks
      const marks = intOr(q101.marks || q101.total_marks, 1);
      const memoText = String(q101.worked_solution || q101.canonical_solution || q101.explanation || q101.sample_answer || q101.solution || '');
      if (marks >= 2 && memoText.length < 30 && !q101.sub_questions && !q101.parts) {
        defects.push(`[THIN_PROCEDURE] ${marks}-mark question has thin worked solution (${memoText.length} chars).`);
      }

      // Check 5: Multi-Seed Variety
      const p101 = String(q101.question || q101.prompt || q101.question_text || '');
      const p202 = String(q202.question || q202.prompt || q202.question_text || '');
      const p303 = String(q303.question || q303.prompt || q303.question_text || '');
      if (p101 === p202 && p202 === p303 && p101.length > 20) {
        defects.push(`[ZERO_ENTROPY_STATIC] Question prompt is identical across seeds 101, 202, 303.`);
      }

      // Record to ledger
      const entry = {
        subject,
        grade: cfg.grade,
        topic,
        term,
        archetype_id: archName,
        modality: q101.modality || 'semantic',
        marks,
        mounted_in_universal_workspace: true,
        viewport_width: 1440,
        viewport_height: 900,
        pre_scroll_height: preCapture.totalHeight,
        pre_scroll_screenshots: preCapture.relativePaths,
        memo_scroll_height: memoCapture.totalHeight,
        memo_scroll_screenshots: memoCapture.relativePaths,
        unresolved_defects: defects,
        status: defects.length === 0 ? 'PASS' : 'FLAGGED',
      };
      ledger.archetypes.push(entry);

      if (defects.length === 0) {
        console.log(`✅ PASS (${preCapture.relativePaths.length} pre-shots, ${memoCapture.relativePaths.length} memo-shots)`);
      } else {
        console.log(`⚠️ FLAGGED (${defects.length} defect(s)): ${defects[0]}`);
      }
    }
  }

  await browser.close();

  // Load known grounded curriculum remediations
  const knownRemPath = path.join(PROJECT_ROOT, 'scripts', 'known_remediations.json');
  if (fs.existsSync(knownRemPath)) {
    try {
      const allRem = JSON.parse(fs.readFileSync(knownRemPath, 'utf-8'));
      if (allRem[cfg.grade]) {
        ledger.remediations = allRem[cfg.grade];
      }
    } catch (e) {
      console.warn('Could not load known remediations:', e.message);
    }
  }

  // Write ledger to disk
  fs.writeFileSync(ledgerPath, JSON.stringify(ledger, null, 2), 'utf-8');
  console.log(`\nSaved ledger: ${ledgerPath}`);

  // Build HTML report
  console.log(`Building interactive HTML report...`);
  spawnSync('.\\caps-ai-backend\\venv\\Scripts\\python.exe', ['scripts/build_full_archetype_html_report.py', '--grade', cfg.grade], {
    cwd: PROJECT_ROOT,
    stdio: 'inherit',
  });

  console.log(`\nAudit completed for Grade ${cfg.grade}.`);
}

function intOr(val, fallback) {
  const n = parseInt(val, 10);
  return isNaN(n) ? fallback : n;
}

runPipeline().catch(err => {
  console.error('\nPipeline Error:', err);
  process.exit(1);
});
