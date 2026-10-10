import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 4: Zanele Mthembu — EMS & Natural Sciences (Gr 9 Senior Phase 14-Day Free Trial Mobile Pixel 7)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 4',
    learnerName: 'Zanele Mthembu',
    grade: 9,
    email: 'zanele.mthembu@fundile.test',
    password: 'Fundile@2026!',
    plan: 'free_trial', // 14-Day Free Trial (R0 Upfront)
    isMobile: true,
    subject1: 'Economic & Management Sciences',
    subject1TabName: 'EMS',
    subject2: 'Natural Sciences',
    subject2TabName: 'Nat Sci',
    teacherCode: 'EMS903',
  });
});
