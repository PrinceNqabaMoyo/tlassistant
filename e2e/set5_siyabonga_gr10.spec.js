import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 5: Siyabonga Cele — Business Studies & Maths Literacy (Gr 10 FET Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 5',
    learnerName: 'Siyabonga Cele',
    grade: 10,
    email: 'siyabonga.cele@fundile.test',
    password: 'Fundile@2026!',
    plan: 'monthly_pass', // R149 Monthly Pass
    isMobile: false,
    subject1: 'Business Studies',
    subject1TabName: 'Business',
    subject2: 'Mathematical Literacy',
    subject2TabName: 'Maths Lit',
  });
});
