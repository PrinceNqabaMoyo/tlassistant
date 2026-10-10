import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 8: Prince Mthembu — Mathematics Calculus & Physical Sciences (Gr 12 Matric Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 8',
    learnerName: 'Prince Mthembu',
    grade: 12,
    email: 'prince.mthembu@fundile.test',
    password: 'Fundile@2026!',
    plan: 'annual_pass', // R999 Annual Distinction Pass
    isMobile: false,
    subject1: 'Mathematics',
    subject1TabName: 'Maths',
    subject2: 'Physical Sciences',
    subject2TabName: 'Physics',
  });
});
