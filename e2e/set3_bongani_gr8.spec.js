import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 3: Bongani Sithole — Mathematics & Natural Sciences (Gr 8 Senior Phase Mobile Pixel 7)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 3',
    learnerName: 'Bongani Sithole',
    grade: 8,
    email: 'bongani.sithole@fundile.test',
    password: 'Fundile@2026!',
    plan: 'monthly_pass', // R149 Monthly Pass
    isMobile: true,
    subject1: 'Mathematics',
    subject1TabName: 'Maths',
    subject2: 'Natural Sciences',
    subject2TabName: 'Nat Sci',
    teacherCode: 'SCI802',
  });
});
