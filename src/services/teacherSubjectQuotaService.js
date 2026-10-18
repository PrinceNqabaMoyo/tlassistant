/**
 * teacherSubjectQuotaService.js
 * Enforces authoritative South African faculty subject quotas:
 * - Senior Phase (Grades 7–9): Maximum 2 subjects
 * - FET Phase (Grades 10–12): Maximum 3 subjects
 */

export const SENIOR_PHASE_SUBJECTS = [
  { id: 'Mathematics', name: 'Mathematics', grades: ['7', '8', '9'] },
  { id: 'EMS', name: 'Economic & Management Sciences (EMS)', grades: ['7', '8', '9'] },
  { id: 'Natural Sciences', name: 'Natural Sciences', grades: ['7', '8', '9'] },
];

export const FET_PHASE_SUBJECTS = [
  { id: 'Accounting', name: 'Accounting', grades: ['10', '11', '12'] },
  { id: 'Mathematics', name: 'Mathematics', grades: ['10', '11', '12'] },
  { id: 'Physical Sciences', name: 'Physical Sciences', grades: ['10', '11', '12'] },
  { id: 'Business Studies', name: 'Business Studies', grades: ['10', '11', '12'] },
  { id: 'Life Sciences', name: 'Life Sciences', grades: ['10', '11', '12'] },
  { id: 'Mathematical Literacy', name: 'Mathematical Literacy', grades: ['10', '11', '12'] },
  { id: 'Technical Mathematics', name: 'Technical Mathematics', grades: ['10', '11', '12'] },
];

export const MAX_SENIOR_PHASE_SUBJECTS = 2;
export const MAX_FET_PHASE_SUBJECTS = 3;

const STORAGE_PREFIX = 'fundile_faculty_subjects_';

export function getTeacherEnrolledSubjects(teacherId = 'default_educator') {
  try {
    const raw = localStorage.getItem(`${STORAGE_PREFIX}${teacherId}`);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (parsed && Array.isArray(parsed.seniorPhase) && Array.isArray(parsed.fetPhase)) {
        return parsed;
      }
    }
  } catch (err) {
    console.warn('Could not read faculty subjects from localStorage:', err);
  }

  // Authoritative default roster allocation (Mr. N. Sithole: Accounting, Maths, PhysSci + EMS, Maths)
  return {
    seniorPhase: ['EMS', 'Mathematics'],
    fetPhase: ['Accounting', 'Mathematics', 'Physical Sciences']
  };
}

export function saveTeacherEnrolledSubjects(teacherId = 'default_educator', allocation) {
  const sanitized = {
    seniorPhase: (allocation?.seniorPhase || []).slice(0, MAX_SENIOR_PHASE_SUBJECTS),
    fetPhase: (allocation?.fetPhase || []).slice(0, MAX_FET_PHASE_SUBJECTS),
    updatedAt: new Date().toISOString()
  };

  try {
    localStorage.setItem(`${STORAGE_PREFIX}${teacherId}`, JSON.stringify(sanitized));
  } catch (err) {
    console.warn('Could not save faculty subjects to localStorage:', err);
  }

  return sanitized;
}

export function isSubjectAllowedForGrade(subjectName, grade, allocation) {
  const gNum = parseInt(grade, 10);
  if (isNaN(gNum)) return true;

  if (gNum >= 7 && gNum <= 9) {
    return (allocation?.seniorPhase || []).includes(subjectName);
  } else if (gNum >= 10 && gNum <= 12) {
    return (allocation?.fetPhase || []).includes(subjectName);
  }

  return true;
}
