import { spawn } from 'child_process';
import readline from 'readline';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');
const bridgeFile = path.resolve(projectRoot, '.pause_signal.json');

// Purge any stale pause signal on startup
try {
  if (fs.existsSync(bridgeFile)) fs.unlinkSync(bridgeFile);
} catch {}

const specArg = process.argv[2] || 'e2e/set1_interactive_side_by_side.spec.js';

console.log(`\n================================================================================`);
console.log(`🚀 Fundile TLAssistant Autonomous Autopilot [Continuous + On-Demand Pause]`);
console.log(`   Spec: ${specArg}`);
console.log(`   Headed Execution: Strictly 1 browser window active at a time (~250 MB RAM cap)`);
console.log(`   Mode: Continuous Auto-Run (Runs from start to finish without forced stops)`);
console.log(`   💡 To Pause: Type 'p' + Enter in this PowerShell terminal OR click [⏸️ Pause] on the browser.`);
console.log(`================================================================================\n`);

let execBinary = process.execPath;
let pwArgs = [];
const spawnOpts = {
  cwd: projectRoot,
  stdio: ['ignore', 'inherit', 'inherit'],
  env: {
    ...process.env,
    PLAYWRIGHT_WORKERS: '1'
  }
};

try {
  const playwrightCli = require.resolve('@playwright/test/cli');
  pwArgs = [playwrightCli, 'test', specArg, '--headed'];
} catch {
  execBinary = process.platform === 'win32' ? 'npx.cmd' : 'npx';
  pwArgs = ['playwright', 'test', specArg, '--headed'];
  spawnOpts.shell = process.platform === 'win32';
}

const pwProcess = spawn(execBinary, pwArgs, spawnOpts);

let isPaused = false;

function triggerPause() {
  if (!isPaused) {
    isPaused = true;
    try {
      fs.writeFileSync(bridgeFile, JSON.stringify({ status: 'pause', timestamp: Date.now() }), 'utf8');
    } catch (err) {
      console.error('[Pause Signal Error]', err.message);
    }
    console.log(`\n================================================================================`);
    console.log(`⏸️  [PAUSED BY USER]`);
    console.log(`   The test is paused for inspection. The browser window is live on screen.`);
    console.log(`   👉 Press [ENTER] in this terminal (or click [▶️ Resume] in browser) to resume...`);
    console.log(`================================================================================\n`);
  }
}

function triggerResume() {
  if (isPaused || fs.existsSync(bridgeFile)) {
    isPaused = false;
    try {
      if (fs.existsSync(bridgeFile)) fs.unlinkSync(bridgeFile);
    } catch {}
    console.log(`\n   ▶️ [RESUMED] Advancing user journey...\n`);
  }
}

// Setup readline interface connected DIRECTLY to PowerShell console standard input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: true
});

rl.on('line', (line) => {
  const str = String(line || '').trim().toLowerCase();
  if (str === 'p' || str === 'pause') {
    triggerPause();
  } else {
    triggerResume();
  }
});

// Also listen for raw stdin data / keypress
try {
  process.stdin.setEncoding?.('utf8');
  process.stdin.resume?.();
  process.stdin.on?.('data', (chunk) => {
    const str = String(chunk || '').trim().toLowerCase();
    if (str === 'p' || str === 'pause') {
      triggerPause();
    } else if (isPaused && (chunk.includes('\r') || chunk.includes('\n'))) {
      triggerResume();
    }
  });
} catch {}

// Poll to sync if the user resumed via the on-screen browser button
const pollInterval = setInterval(() => {
  if (isPaused && !fs.existsSync(bridgeFile)) {
    isPaused = false;
    console.log(`\n   ▶️ [RESUMED FROM BROWSER] Continuing user journey...\n`);
  }
}, 300);

pwProcess.on('exit', (code, signal) => {
  clearInterval(pollInterval);
  try {
    rl.close();
  } catch {}
  try {
    if (fs.existsSync(bridgeFile)) fs.unlinkSync(bridgeFile);
  } catch {}
  process.exit(code ?? (signal ? 1 : 0));
});

pwProcess.on('error', (err) => {
  clearInterval(pollInterval);
  try {
    rl.close();
  } catch {}
  try {
    if (fs.existsSync(bridgeFile)) fs.unlinkSync(bridgeFile);
  } catch {}
  console.error(`[Playwright Launcher Error]`, err);
  process.exit(1);
});
