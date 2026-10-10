import { test } from '@playwright/test';
import { runParticipantSet } from './helpers/runParticipantSet.js';

test('Set 2: Ayanda Ndlovu — Mathematics & EMS (Gr 7 Senior Phase Mobile Pixel 7)', async () => {
  test.setTimeout(3600000);
  await runParticipantSet({
    setName: 'SET 2',
    learnerName: 'Ayanda Ndlovu',
    grade: 7,
    email: 'ayanda.ndlovu@fundile.test',
    password: 'Fundile@2026!',
    plan: 'term_pass', // R349 School Term Pass
    isMobile: true,
    subject1: 'Mathematics',
    subject1TabName: 'Maths',
    subject2: 'Economic & Management Sciences',
    subject2TabName: 'EMS',
    teacherCode: 'MTH701',
  });
});
