export const OWNER_EMAILS = ['princenqaba@gmail.com', 'princenqabamoyo@outlook.com'];

export const LIVE_SIGNUP_GRADES = [7, 8, 9, 10, 11, 12];

export const LIVE_SUBJECT_MATRIX = {
  CAPS: {
    7: ['Economic and Management Sciences', 'EMS', 'Mathematics', 'Natural Sciences'],
    8: ['Economic and Management Sciences', 'EMS', 'Mathematics', 'Natural Sciences'],
    9: ['Economic and Management Sciences', 'EMS', 'Mathematics', 'Natural Sciences'],
    10: [
      'Accounting',
      'Mathematics',
      'Business Studies',
      'Physical Sciences',
      'Life Sciences',
      'Mathematical Literacy',
      'Technical Mathematics',
    ],
    11: [
      'Accounting',
      'Mathematics',
      'Business Studies',
      'Physical Sciences',
      'Life Sciences',
      'Mathematical Literacy',
      'Technical Mathematics',
    ],
    12: [
      'Accounting',
      'Mathematics',
      'Business Studies',
      'Physical Sciences',
      'Life Sciences',
      'Mathematical Literacy',
      'Technical Mathematics',
    ],
  },
};

export const COMING_SOON_SUBJECT_MESSAGE = 'This topic or elective is currently being updated to latest exam guidelines. Standard practice is live across all core national curriculum subjects.';

export const CLASS_ASSIGNMENTS_BLOCKED_MESSAGE = 'This facility is not yet available in South Africa.';

export const SAVED_PROBLEMS_PRO_MESSAGE = 'My Saved Problems is only available in the Pro package. Pro is coming soon and not yet available in South Africa.';

export const FREEFORM_PRO_MESSAGE = 'AI Tutor and Freeform Q&A are only available in the Pro package. Pro is coming soon and not yet available in South Africa.';

export const isOwnerEmail = (email = '') => OWNER_EMAILS.includes(String(email).trim().toLowerCase());

export const canBypassSignupGradeRestriction = (email = '') => isOwnerEmail(email);

export const canBypassComingSoon = (currentUser) => {
  if (!currentUser) return false;
  return Boolean(currentUser.isOwner || currentUser.isSuperAdmin);
};

const normalizeSubjectName = (subject) => {
  if (typeof subject === 'string') {
    return subject;
  }

  return subject?.name || '';
};

export const isLiveLaunchSubject = ({ curriculumKey, grade, subject }) => {
  const normalizedGrade = Number(grade);
  const subjectName = normalizeSubjectName(subject);

  if (!curriculumKey || !normalizedGrade || !subjectName) {
    return false;
  }

  return LIVE_SUBJECT_MATRIX[curriculumKey]?.[normalizedGrade]?.includes(subjectName) === true;
};

export const canAccessSavedProblems = (currentUser) => {
  if (!currentUser) {
    return false;
  }

  return currentUser.isOwner || currentUser.isSuperAdmin || currentUser.tier === 'pro';
};
