import { waitIfPaused } from './autopilotHud.js';

/**
 * Milestone Reporter for Playwright E2E Tests
 * - Logs verified milestones cleanly to the terminal without blocking or pausing.
 * - Executes continuously from start to finish by default.
 * - Honors on-demand user pause if triggered.
 */

export async function waitForStep(phaseName, description, page) {
  console.log(`\n================================================================================`);
  console.log(`🎯 [MILESTONE: ${phaseName}]`);
  console.log(`   ${description}`);
  console.log(`================================================================================\n`);

  if (page) {
    await waitIfPaused(page);
  }
}
