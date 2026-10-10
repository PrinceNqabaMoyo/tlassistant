import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 7: Kelebogile Dlamini — Life Sciences & Asset Accounting (Gr 11 FET Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 7',
    learnerName: 'Kelebogile Dlamini',
    grade: 11,
    email: 'kelebogile.dlamini@fundile.test',
    password: 'Fundile@2026!',
    plan: 'term_pass', // R349 Term Pass
    isMobile: false,
    subject1: 'Life Sciences',
    subject1TabName: 'Life Sciences',
    subject2: 'Accounting',
    subject2TabName: 'Accounting',
  });
});
