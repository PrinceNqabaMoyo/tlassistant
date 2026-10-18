import { execSync } from 'child_process';

console.log('\n======================================================================');
console.log('   FUNDILE HOLISTIC PRE-FLIGHT AUDIT PIPELINE (RULE 0d-8)             ');
console.log('======================================================================\n');

function runStep(name, command) {
  console.log(`[*] [STEP: ${name}] Running: ${command}...`);
  const start = Date.now();
  try {
    const output = execSync(command, { stdio: 'inherit', encoding: 'utf-8' });
    const elapsed = ((Date.now() - start) / 1000).toFixed(1);
    console.log(`[PASS] ${name} succeeded (${elapsed}s).\n`);
  } catch (err) {
    const elapsed = ((Date.now() - start) / 1000).toFixed(1);
    console.error(`\n[FAIL] ${name} FAILED after ${elapsed}s!`);
    process.exit(1);
  }
}

// 0. Generator Preservation & Inventory Audit (Rule 2 & Generator Preservation Law)
runStep('0. Generator Preservation & Inventory Audit', 'python scripts/audit_generators_preservation.py');

// 1. Selector purity and Anti-Hollywood verification
runStep('1. E2E Mechanical Selector & Skip Audit', 'python scripts/audit_e2e_specs.py');

// 2. Cross-spec import and syntax discovery
runStep('2. Playwright Multi-Suite Test Discovery', 'npx playwright test --list');

// 3. Live browser connectivity and Vite rendering check
runStep('3. Live Browser DOM Smoke Check', 'node scripts/smoke_check.js');

console.log('======================================================================');
console.log('   [SUCCESS] ALL PRE-FLIGHT GATES PASSED (Codebase is 100% healthy)   ');
console.log('======================================================================\n');
