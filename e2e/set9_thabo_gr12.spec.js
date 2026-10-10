import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 9: Thabo Molefe — Accounting Corporate Statements & Business Studies King IV (Gr 12 Matric Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 9',
    learnerName: 'Thabo Molefe',
    grade: 12,
    email: 'thabo.molefe@fundile.test',
    password: 'Fundile@2026!',
    plan: 'term_pass', // R349 Term Pass
    isMobile: false,
    subject1: 'Accounting',
    subject1TabName: 'Accounting',
    subject2: 'Business Studies',
    subject2TabName: 'Business',
    teacherCode: 'ACC12B',
  });
});
