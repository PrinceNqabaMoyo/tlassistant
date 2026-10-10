import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 1: Lesedi Khumalo — Accounting & Mathematics (Gr 10 FET Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 1',
    learnerName: 'Lesedi Khumalo',
    grade: 10,
    email: 'lesedi.khumalo@fundile.test',
    password: 'Fundile@2026!',
    plan: 'term_pass', // R349 School Term Pass
    isMobile: false,
    subject1: 'Accounting',
    subject1TabName: 'Accounting',
    subject2: 'Mathematics',
    subject2TabName: 'Mathematics',
  });
});
