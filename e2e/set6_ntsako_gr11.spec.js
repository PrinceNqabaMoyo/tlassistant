import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 6: Ntsako Baloyi — Physical Sciences & Tech Mathematics (Gr 11 FET Desktop)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 6',
    learnerName: 'Ntsako Baloyi',
    grade: 11,
    email: 'ntsako.baloyi@fundile.test',
    password: 'Fundile@2026!',
    plan: 'term_pass', // R349 Term Pass
    isMobile: false,
    subject1: 'Physical Sciences',
    subject1TabName: 'Physics',
    subject2: 'Technical Mathematics',
    subject2TabName: 'Tech Maths',
    teacherCode: 'PHY110',
  });
});
