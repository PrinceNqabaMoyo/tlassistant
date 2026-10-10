import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 10: Lerato Khanyile — Technical Mathematics & Maths Literacy SARS Brackets (Gr 12 Technical Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 10',
    learnerName: 'Lerato Khanyile',
    grade: 12,
    email: 'lerato.khanyile@fundile.test',
    password: 'Fundile@2026!',
    plan: 'monthly_pass', // R149 Monthly Pass
    isMobile: false,
    subject1: 'Technical Mathematics',
    subject1TabName: 'Tech Maths',
    subject2: 'Mathematical Literacy',
    subject2TabName: 'Maths Lit',
  });
});
