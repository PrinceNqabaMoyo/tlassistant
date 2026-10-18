import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '../..');

/**
 * Authentic Super Admin Session Authenticator (Rule 0d-2 & 0d-5)
 *
 * Strictly adheres to The Super Admin Law:
 * 1. Derives genuine identity for platform owner (princenqaba@gmail.com / UID: yUHv5COBcCdOFy6brXnOoBhfaTc2).
 * 2. Generates a valid Firebase Auth custom token signed by the Firebase Admin service account.
 * 3. Signs into Firebase Auth client-side via signInWithCustomToken().
 * 4. Produces authentic Firebase ID tokens with email_verified: true.
 * 5. Zero mock personas (never MOCK_SUPER_ADMIN) and zero URL query spoofing (never ?persona=admin).
 */
export async function authenticateSuperAdminSession(page, targetBaseUrl = 'http://localhost:5173') {
  // 1. Generate authentic custom token from Firebase Admin SDK
  const cmd = `python -c "import sys; sys.path.append('caps-ai-backend'); from app.utils.firebase_admin_client import get_firebase_app, auth; print(auth.create_custom_token('yUHv5COBcCdOFy6brXnOoBhfaTc2', app=get_firebase_app()).decode('utf-8'))"`;
  const customToken = execSync(cmd, { cwd: projectRoot, encoding: 'utf-8' }).trim();

  if (!customToken) {
    throw new Error('[SuperAdmin Auth] Failed to generate custom auth token from Firebase Admin SDK');
  }

  // 2. Navigate to base URL with admin hash
  await page.goto(`${targetBaseUrl}/#admin`, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof window.__FUNDILE_SIGN_IN_CUSTOM_TOKEN__ === 'function', { timeout: 20000 });

  // 3. Authenticate via genuine Firebase client SDK
  const authSuccess = await page.evaluate(async (token) => {
    try {
      await window.__FUNDILE_SIGN_IN_CUSTOM_TOKEN__(token);
      return true;
    } catch (e) {
      console.error('Failed to sign in with custom token:', e);
      return false;
    }
  }, customToken);

  if (!authSuccess) {
    throw new Error('[SuperAdmin Auth] Client-side Firebase custom token sign-in failed');
  }

  // 4. Wait for auth observer and real-time user doc to resolve
  await page.waitForTimeout(1500);

  // 5. Switch to admin perspective for governance and clearance desk
  await page.evaluate(() => {
    window.location.hash = '#admin';
    window.dispatchEvent(new HashChangeEvent('hashchange'));
    if (typeof window.__FUNDILE_SET_SUPER_ADMIN_MODE__ === 'function') {
      window.__FUNDILE_SET_SUPER_ADMIN_MODE__('admin');
    }
  });
  await page.waitForTimeout(600);
}
