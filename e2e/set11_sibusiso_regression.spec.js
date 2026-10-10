import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 11: Sibusiso Zulu — Cross-Grade Adaptive Descent (Gr 12 Optimization -> Gr 10 Trinomials -> Gr 8 HCF Factorisation)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 11',
    learnerName: 'Sibusiso Zulu',
    grade: 12,
    email: 'sibusiso.zulu@fundile.test',
    password: 'Fundile@2026!',
    plan: 'free_trial', // Zero payment friction for license sync simulation
    isMobile: false,
    subject1: 'Mathematics',
    subject1TabName: 'Maths',
    subject2: null,
  });
});
