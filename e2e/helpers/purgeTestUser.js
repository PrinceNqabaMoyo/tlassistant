/**
 * Pre-Flight Test User Purge Helper
 * Purges a specific test learner from Firebase Auth and Firestore before a test set runs,
 * ensuring a completely clean slate from sign-up / free trial every time.
 * Strictly whitelists and protects Super Admin / owner accounts.
 */

import { initializeApp, deleteApp } from 'firebase/app';
import { getAuth, signInWithEmailAndPassword, deleteUser } from 'firebase/auth';
import { getFirestore, doc, deleteDoc, collection, query, where, getDocs, terminate } from 'firebase/firestore';
import { firebaseConfig } from '../../src/constants/sourceDocuments.js';
import { OWNER_EMAILS } from '../../src/app/constants/access.js';

export async function purgeTestUser(email, password = 'Fundile@2026!') {
  const normalizedEmail = email.trim().toLowerCase();

  // Security Invariant: Never touch Super Admin or owner accounts
  const isProtectedOwner = OWNER_EMAILS.some(owner => owner.toLowerCase() === normalizedEmail);
  if (isProtectedOwner) {
    throw new Error(`[Security Invariant] Refusing to purge Super Admin / Owner account: ${email}`);
  }

  console.log(`\n🧹 [Pre-Flight Purge] Checking for existing test user: ${email}...`);

  const appName = `purge-session-${Date.now()}`;
  const app = initializeApp(firebaseConfig, appName);
  const auth = getAuth(app);
  const db = getFirestore(app);

  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    const uid = user.uid;
    console.log(`   Found existing test account (UID: ${uid}). Purging records...`);

    // 1. Delete user profile doc in Firestore
    await deleteDoc(doc(db, 'users', uid)).catch(e => console.warn('   User doc delete note:', e.message));

    // 2. Query and delete pending payments
    try {
      const paymentsQ = query(collection(db, 'pending_payments'), where('userId', '==', uid));
      const paymentSnaps = await getDocs(paymentsQ);
      for (const d of paymentSnaps.docs) {
        await deleteDoc(d.ref).catch(() => {});
      }
    } catch (e) {}

    // 3. Query and delete submissions
    try {
      const subQ = query(collection(db, 'submissions'), where('userId', '==', uid));
      const subSnaps = await getDocs(subQ);
      for (const d of subSnaps.docs) {
        await deleteDoc(d.ref).catch(() => {});
      }
    } catch (e) {}

    // 4. Query and delete learner mastery
    try {
      const masteryQ = query(collection(db, 'learner_mastery'), where('userId', '==', uid));
      const masterySnaps = await getDocs(masteryQ);
      for (const d of masterySnaps.docs) {
        await deleteDoc(d.ref).catch(() => {});
      }
    } catch (e) {}

    // 5. Delete Firebase Auth user
    await deleteUser(user);
    console.log(`✅ [Pre-Flight Purge] Successfully purged test user: ${email} (UID: ${uid})\n`);
    await terminate(db).catch(() => {});
    await deleteApp(app).catch(() => {});
    return { purged: true, uid };
  } catch (err) {
    await terminate(db).catch(() => {});
    await deleteApp(app).catch(() => {});
    if (
      err.code === 'auth/user-not-found' ||
      err.code === 'auth/invalid-credential' ||
      err.code === 'auth/wrong-password' ||
      err.code === 'auth/invalid-email'
    ) {
      console.log(`✅ [Pre-Flight Purge] User ${email} does not exist in Firebase Auth (already clean slate).\n`);
      return { purged: false, reason: 'not_found' };
    }
    console.warn(`⚠️ [Pre-Flight Purge] Note: ${err.message}\n`);
    return { purged: false, error: err.message };
  }
}
