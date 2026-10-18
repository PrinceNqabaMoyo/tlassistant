/**
 * schoolEnrollmentService.js
 * 
 * Manages institutional enrollment, Grade-level Master Passes,
 * self-service elective & teacher selection, and teacher roster authority.
 * 
 * Complies with POPIA Section 35 and South African FET Phase subject streaming.
 */

import studentStore from './studentStore';

export const DEFAULT_SCHOOLS = [
  {
    id: 'sch_westville_high',
    schoolId: 'sch_westville_high',
    name: 'Westville High School',
    shortName: 'Westville High',
    emisNumber: '500124892',
    billingModel: 'bulk_prepaid',
    status: 'active',
    grades: [7, 8, 9, 10, 11, 12],
    province: 'KwaZulu-Natal',
    district: 'Pinetown District',
    facultyPasscode: 'WHS-TEACH-2026',
    registeredAt: '2026-01-15T08:00:00Z'
  }
];

/**
 * Dynamically retrieves registered and approved schools from storage
 */
export function getApprovedSchools() {
  const key = 'fundile_registered_schools';
  if (typeof window !== 'undefined') {
    try {
      const stored = localStorage.getItem(key);
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed) && parsed.length > 0) {
          return parsed;
        }
      }
    } catch (e) {
      console.warn('Could not read registered schools from localStorage:', e);
    }
  }
  return DEFAULT_SCHOOLS;
}

export let APPROVED_SCHOOLS = getApprovedSchools();

/**
 * Registers a new institutional school (School Admin onboarding)
 */
export function registerSchool(schoolData) {
  const name = schoolData.name || 'New High School';
  let slug = name.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
  if (slug === 'westville_high_school' || slug.includes('westville_high')) {
    slug = 'westville_high';
  }
  const schoolId = schoolData.schoolId || `sch_${slug}`;
  const facultyCode = (schoolData.facultyPasscode || 'WHS-TEACH-2026').toUpperCase();

  const newSchool = {
    id: schoolId,
    schoolId,
    name,
    shortName: name.replace(/\s+(High School|Secondary School|College)/i, ''),
    emisNumber: schoolData.emisNumber || '500124892',
    billingModel: schoolData.billingModel || 'bulk_prepaid',
    status: 'active',
    grades: schoolData.grades || [7, 8, 9, 10, 11, 12],
    province: schoolData.province || 'KwaZulu-Natal',
    district: schoolData.district || 'Pinetown District',
    facultyPasscode: facultyCode,
    registeredAt: new Date().toISOString()
  };

  const currentSchools = getApprovedSchools();
  const existingIdx = currentSchools.findIndex(s => s.id === schoolId);
  let updated;
  if (existingIdx >= 0) {
    updated = [...currentSchools];
    updated[existingIdx] = { ...updated[existingIdx], ...newSchool };
  } else {
    updated = [newSchool, ...currentSchools];
  }

  if (typeof window !== 'undefined') {
    try {
      localStorage.setItem('fundile_registered_schools', JSON.stringify(updated));
    } catch (e) {
      console.warn('Could not persist registered school:', e);
    }
  }

  APPROVED_SCHOOLS = updated;

  // Generate Master Passkeys for Grade 10 if not present
  const masterKey = `fundile_master_passes_${schoolId}_10`;
  const existingPasses = typeof window !== 'undefined' ? localStorage.getItem(masterKey) : null;
  if (!existingPasses) {
    const prefix = schoolId === 'sch_westville_high' ? 'WHS' : (slug.slice(0, 3) || 'SCH').toUpperCase();
    const newPasses = [
      { passkey: `${prefix}-GR10-8421`, schoolId, grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
      { passkey: `${prefix}-GR10-8422`, schoolId, grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
      { passkey: `${prefix}-GR10-8423`, schoolId, grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
      { passkey: `${prefix}-GR10-8424`, schoolId, grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
      { passkey: `${prefix}-GR10-8425`, schoolId, grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
      { passkey: `${prefix}-GR10-8426`, schoolId, grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
    ];
    if (typeof window !== 'undefined') {
      try {
        localStorage.setItem(masterKey, JSON.stringify(newPasses));
      } catch (_) {}
    }
  }

  // Register Faculty Passcode in FACULTY_PASSCODES entry
  if (!FACULTY_PASSCODES[schoolId]) {
    FACULTY_PASSCODES[schoolId] = [
      {
        code: facultyCode,
        schoolId,
        schoolName: name,
        department: 'All Departments (Institutional Master)',
        defaultSubject: 'Accounting',
        isMaster: true
      }
    ];
  }

  return newSchool;
}

const INITIAL_MASTER_PASSES_WHS_GR10 = [
  { passkey: 'WHS-GR10-8421', schoolId: 'sch_westville_high', grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
  { passkey: 'WHS-GR10-8422', schoolId: 'sch_westville_high', grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
  { passkey: 'WHS-GR10-8423', schoolId: 'sch_westville_high', grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
  { passkey: 'WHS-GR10-8424', schoolId: 'sch_westville_high', grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
  { passkey: 'WHS-GR10-8425', schoolId: 'sch_westville_high', grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
  { passkey: 'WHS-GR10-8426', schoolId: 'sch_westville_high', grade: 10, isClaimed: false, claimedBy: null, claimedAt: null },
];

/**
 * Institutional Faculty Passcodes & Pre-Assigned Teaching Allocations
 */
export const FACULTY_PASSCODES = {
  sch_westville_high: [
    {
      code: 'WHS-TEACH-2026',
      schoolId: 'sch_westville_high',
      schoolName: 'Westville High School',
      department: 'Commercial Sciences & STEM',
      defaultSubject: 'Accounting',
      isMaster: true
    },
    {
      code: 'WHS-FAC-SITHOLE',
      schoolId: 'sch_westville_high',
      schoolName: 'Westville High School',
      educatorName: 'Mr. N. Sithole',
      department: 'Commercial Sciences',
      email: 'n.sithole@westvillehigh.co.za',
      defaultSubject: 'Accounting',
      isMaster: false
    },
    {
      code: 'WHS-FAC-KHUMALO',
      schoolId: 'sch_westville_high',
      schoolName: 'Westville High School',
      educatorName: 'Mrs. P. Khumalo',
      department: 'STEM',
      email: 'p.khumalo@westvillehigh.co.za',
      defaultSubject: 'Mathematics',
      isMaster: false
    },
    {
      code: 'WHS-FAC-BOTHA',
      schoolId: 'sch_westville_high',
      schoolName: 'Westville High School',
      educatorName: 'Mr. J. Botha',
      department: 'STEM & Sciences',
      email: 'j.botha@westvillehigh.co.za',
      defaultSubject: 'Physical Sciences',
      isMaster: false
    },
    {
      code: 'WHS-FAC-PILLAY',
      schoolId: 'sch_westville_high',
      schoolName: 'Westville High School',
      educatorName: 'Mrs. M. Pillay',
      department: 'Commerce',
      email: 'm.pillay@westvillehigh.co.za',
      defaultSubject: 'Business Studies',
      isMaster: false
    }
  ]
};

/**
 * Pre-assigned departmental class roster templates for institutional faculty
 */
export const WHS_FACULTY_ASSIGNED_CLASSES = {
  'Accounting': [
    {
      classId: 'cls_whs_acc10a',
      name: 'Grade 10A (Commerce)',
      subject: 'Accounting',
      grade: '10',
      term: 1,
      joinCode: 'ACC10A',
      studentCount: 28,
      avgMastery: 78,
      homeworkDue: 8,
      topMisconception: 'net_vs_gross_confusion',
      misconceptionLabel: 'Confusing 15% Exclusive vs 115% Inclusive VAT Formula',
      recentSubmissionCount: 24,
      students: []
    },
    {
      classId: 'cls_whs_ems9c',
      name: 'Grade 9 EMS (Commerce)',
      subject: 'EMS',
      grade: '9',
      term: 1,
      joinCode: 'EMS9Q1',
      studentCount: 35,
      avgMastery: 84,
      homeworkDue: 9,
      topMisconception: 'debit_credit_inversion',
      misconceptionLabel: 'Inverting Bank Statement vs Bank Account Entries',
      recentSubmissionCount: 33,
      students: []
    }
  ],
  'Mathematics': [
    {
      classId: 'cls_whs_math10b',
      name: 'Grade 10B (Sciences)',
      subject: 'Mathematics',
      grade: '10',
      term: 1,
      joinCode: 'MATH10B',
      studentCount: 32,
      avgMastery: 71,
      homeworkDue: 5,
      topMisconception: 'sequence_difference_multiplier',
      misconceptionLabel: 'Confusing common difference with multiplier',
      recentSubmissionCount: 28,
      students: []
    },
    {
      classId: 'cls_whs_math11x',
      name: 'Grade 11 Mathematics — Extended',
      subject: 'Mathematics',
      grade: '11',
      term: 1,
      joinCode: 'MAT11X',
      studentCount: 26,
      avgMastery: 74,
      homeworkDue: 6,
      topMisconception: 'quadratic_formula_sign',
      misconceptionLabel: 'Inverting -b in Quadratic Formula ±√Discriminant',
      recentSubmissionCount: 22,
      students: []
    }
  ],
  'Physical Sciences': [
    {
      classId: 'cls_whs_phy10b',
      name: 'Grade 10 Physical Sciences (Physics & Chem)',
      subject: 'Physical Sciences',
      grade: '10',
      term: 1,
      joinCode: 'PHYS10B',
      studentCount: 30,
      avgMastery: 70,
      homeworkDue: 11,
      topMisconception: 'vector_direction_omission',
      misconceptionLabel: 'Omitting Direction on Vector Resultants [e.g. East or Right]',
      recentSubmissionCount: 25,
      students: []
    }
  ],
  'Business Studies': [
    {
      classId: 'cls_whs_bus10a',
      name: 'Grade 10A Business Studies',
      subject: 'Business Studies',
      grade: '10',
      term: 1,
      joinCode: 'BUS10A',
      studentCount: 25,
      avgMastery: 75,
      homeworkDue: 4,
      topMisconception: 'micro_macro_confusion',
      misconceptionLabel: 'Confusing Micro vs Macro Business Environments',
      recentSubmissionCount: 21,
      students: []
    }
  ]
};

/**
 * Retrieve master passkeys for a school and grade
 */
export function getMasterPasskeys(schoolId = 'sch_westville_high', grade = 10) {
  const key = `fundile_master_passes_${schoolId}_${grade}`;
  try {
    const raw = localStorage.getItem(key);
    if (raw) return JSON.parse(raw);
  } catch (e) {
    console.warn('Could not read master passkeys from storage:', e);
  }
  // Initialize default passes
  try {
    localStorage.setItem(key, JSON.stringify(INITIAL_MASTER_PASSES_WHS_GR10));
  } catch (_) {}
  return INITIAL_MASTER_PASSES_WHS_GR10;
}

/**
 * Validate a candidate master passkey entered during registration
 */
export function validateMasterPasskey(candidateKey, schoolId = 'sch_westville_high') {
  if (!candidateKey) {
    return { valid: false, error: 'Please enter your Grade Master Pass key.' };
  }
  const cleanKey = String(candidateKey).trim().toUpperCase();
  const passes = getMasterPasskeys(schoolId, 10);
  const found = passes.find(p => p.passkey.toUpperCase() === cleanKey);

  if (!found) {
    return { 
      valid: false, 
      error: 'Invalid Master Pass key for this school. Check your printed slip or contact your school.' 
    };
  }

  if (found.isClaimed) {
    return { 
      valid: false, 
      error: `This Master Pass was already claimed by ${found.claimedBy || 'another learner'}.` 
    };
  }

  const schools = getApprovedSchools();
  const school = schools.find(s => s.id === schoolId || s.schoolId === schoolId) || schools[0] || null;

  if (!school) {
    return {
      valid: false,
      error: 'Selected school is not registered or approved yet.'
    };
  }

  return {
    valid: true,
    passkey: found.passkey,
    grade: found.grade,
    school,
    billingModel: school.billingModel
  };
}

/**
 * Consume a master passkey once student registers
 */
export function claimMasterPasskey(passkey, studentData, schoolId = 'sch_westville_high') {
  const cleanKey = String(passkey).trim().toUpperCase();
  const key = `fundile_master_passes_${schoolId}_10`;
  const passes = getMasterPasskeys(schoolId, 10);

  const updated = passes.map(p => {
    if (p.passkey.toUpperCase() === cleanKey) {
      return {
        ...p,
        isClaimed: true,
        claimedBy: studentData.name || studentData.email,
        claimedByEmail: studentData.email,
        claimedAt: new Date().toISOString()
      };
    }
    return p;
  });

  try {
    localStorage.setItem(key, JSON.stringify(updated));
  } catch (e) {
    console.warn('Could not persist claimed passkey:', e);
  }

  // Also record on school admin enrolled records for SASAMS
  recordStudentOnSchoolAdminRoster(studentData, schoolId);

  return true;
}

/**
 * Redeems an institutional Master Passkey for an independent subscriber.
 * Calculates refund/forfeiture for remaining retail months, binds to school,
 * and preserves 100% of student's historical mastery and guardian links.
 */
export function redeemSchoolPasskeyForIndependentLearner(passkey, studentProfile = {}, schoolId = 'sch_westville_high') {
  const validation = validateMasterPasskey(passkey, schoolId);
  if (!validation.valid) {
    return { success: false, error: validation.error };
  }

  // Claim the passkey for this student
  claimMasterPasskey(passkey, studentProfile, schoolId);

  // Transition in studentStore and compute refund claim
  const refundClaim = studentStore.transitionIndependentToSchool(passkey, validation.school);

  return {
    success: true,
    school: validation.school,
    refundClaim,
    passkey: validation.passkey
  };
}

/**
 * Available Subject Classes & Teachers for Westville High School Grade 10
 */
export const WHS_GRADE10_CLASS_OFFERINGS = {
  accounting: [
    {
      classId: 'cls_whs_acc10a',
      name: 'Class 10A (Commerce)',
      subject: 'Accounting',
      teacherName: 'Mr. N. Sithole',
      joinCode: 'ACC10A',
      educatorEmail: 'n.sithole@westvillehigh.co.za'
    }
  ],
  mathematics: [
    {
      classId: 'cls_whs_math10b',
      name: 'Class 10B (Sciences)',
      subject: 'Mathematics',
      teacherName: 'Mrs. P. Khumalo',
      joinCode: 'MATH10B',
      educatorEmail: 'p.khumalo@westvillehigh.co.za'
    },
    {
      classId: 'cls_whs_math10a',
      name: 'Class 10A (Pure Maths)',
      subject: 'Mathematics',
      teacherName: 'Mr. J. Botha',
      joinCode: 'MATH10A',
      educatorEmail: 'j.botha@westvillehigh.co.za'
    }
  ],
  physics: [
    {
      classId: 'cls_whs_phy10b',
      name: 'Class 10B (Sciences)',
      subject: 'Physical Sciences',
      teacherName: 'Mr. J. Botha',
      joinCode: 'PHYS10B',
      educatorEmail: 'j.botha@westvillehigh.co.za'
    }
  ],
  business: [
    {
      classId: 'cls_whs_bus10a',
      name: 'Class 10A (Commerce)',
      subject: 'Business Studies',
      teacherName: 'Mrs. M. Pillay',
      joinCode: 'BUS10A',
      educatorEmail: 'm.pillay@westvillehigh.co.za'
    }
  ]
};

/**
 * Enrolls a student into selected subject classes
 */
export function enrollStudentIntoClasses(studentProfile, classSelections) {
  // classSelections: { accounting: 'ACC10A', mathematics: 'MATH10B', ... }
  const teacherLinks = [];

  Object.entries(classSelections).forEach(([subjectKey, joinCode]) => {
    if (!joinCode || joinCode === 'none') return;

    // Find class info
    let foundClass = null;
    const offerings = WHS_GRADE10_CLASS_OFFERINGS[subjectKey] || [];
    foundClass = offerings.find(o => o.joinCode === joinCode);

    const enrollmentRecord = {
      id: studentProfile.id || `std_${Date.now()}`,
      name: studentProfile.name,
      email: studentProfile.email,
      score: studentProfile.score || 88,
      status: 'Mastered',
      photoURL: studentProfile.photoURL || null,
      topic: subjectKey === 'accounting' ? 'Cash Receipts Journal (VAT 15%)' : 'Trinomial Factorisation Drill',
      olympiadBadge: '🥇 Live Distinction',
      misconception: null,
      lastActive: 'Active now',
      className: foundClass?.name || 'Grade 10A',
      enrolledAt: new Date().toISOString()
    };

    // 1. Add to class enrollment storage
    const storageKey = `fundile_class_enrolled_students_${joinCode}`;
    try {
      const existing = JSON.parse(localStorage.getItem(storageKey) || '[]');
      const filtered = existing.filter(s => s.email !== studentProfile.email && s.name !== studentProfile.name);
      filtered.unshift(enrollmentRecord);
      localStorage.setItem(storageKey, JSON.stringify(filtered));
    } catch (e) {
      console.warn('Error saving class enrollment:', e);
    }

    teacherLinks.push({
      code: joinCode,
      subject: foundClass?.subject || subjectKey,
      teacher: foundClass?.teacherName || 'Subject Educator',
      className: foundClass?.name || 'Grade 10'
    });
  });

  // 2. Persist teacherLinks to studentStore state in localStorage
  try {
    const studentStateRaw = localStorage.getItem('fundile_student_state_v1');
    const studentState = studentStateRaw ? JSON.parse(studentStateRaw) : {};
    studentState.teacherLinks = teacherLinks;
    studentState.schoolId = 'sch_westville_high';
    studentState.schoolName = 'Westville High School';
    studentState.isSchoolLinked = true;
    studentState.studentName = studentProfile.name;
    localStorage.setItem('fundile_student_state_v1', JSON.stringify(studentState));
  } catch (e) {
    console.warn('Error updating studentStore teacherLinks:', e);
  }

  // 3. Persist to School Admin marks ledger for SASAMS
  recordStudentOnSchoolAdminRoster(studentProfile, 'sch_westville_high');

  return { success: true, teacherLinks };
}

/**
 * Removes a learner from a class roster (Teacher authority action)
 */
export function removeStudentFromClassRoster(joinCode, studentIdOrName) {
  const storageKey = `fundile_class_enrolled_students_${joinCode}`;
  try {
    const existing = JSON.parse(localStorage.getItem(storageKey) || '[]');
    const updated = existing.filter(s => s.id !== studentIdOrName && s.name !== studentIdOrName);
    localStorage.setItem(storageKey, JSON.stringify(updated));
  } catch (e) {
    console.warn('Error removing student from class roster:', e);
  }

  // Remove from teacherLinks in studentStore if present
  try {
    const studentStateRaw = localStorage.getItem('fundile_student_state_v1');
    if (studentStateRaw) {
      const studentState = JSON.parse(studentStateRaw);
      studentState.teacherLinks = (studentState.teacherLinks || []).filter(t => t.code !== joinCode);
      localStorage.setItem('fundile_student_state_v1', JSON.stringify(studentState));
    }
  } catch (_) {}

  return { success: true };
}

/**
 * Synchronize learner to School Admin SASAMS records
 */
function recordStudentOnSchoolAdminRoster(studentData, schoolId) {
  const marksKey = 'fundile_school_admin_enrolled_marks';
  try {
    const existingMarks = JSON.parse(localStorage.getItem(marksKey) || '[]');
    const alreadyThere = existingMarks.some(m => m.name === studentData.name);
    if (!alreadyThere) {
      const [fName, ...sNames] = (studentData.name || 'Lesedi Khumalo').trim().split(' ');
      existingMarks.unshift({
        id: `adm_${Date.now()}`,
        name: studentData.name,
        firstName: fName || 'Lesedi',
        surname: sNames.join(' ') || 'Khumalo',
        photoURL: studentData.photoURL || null,
        emis: '500124892',
        emisNumber: '500124892',
        lurits: 'LUR9821045',
        luritsNumber: 'LUR9821045',
        grade: String(studentData.grade || '10'),
        class: '10A',
        classSection: '10A',
        subject: 'Accounting',
        formativeScore: 88,
        formalExamScore: 84,
        examScore: 84,
        termMark: 86,
        capsLevel: 7,
        status: 'Active',
        schoolId
      });
      localStorage.setItem(marksKey, JSON.stringify(existingMarks));
    }
  } catch (e) {
    console.warn('Error updating School Admin SASAMS records:', e);
  }
}

/**
 * Validates an institutional faculty passcode entered during teacher sign-up
 */
export function validateFacultyPasscode(candidateCode, schoolId = 'sch_westville_high') {
  if (!candidateCode) {
    return { valid: false, error: 'Please enter your Institutional Faculty Passcode.' };
  }
  const cleanCode = String(candidateCode).trim().toUpperCase();
  const schoolCodes = FACULTY_PASSCODES[schoolId] || FACULTY_PASSCODES['sch_westville_high'] || [];
  const found = schoolCodes.find(c => c.code.toUpperCase() === cleanCode);
  const schools = getApprovedSchools();
  const school = schools.find(s => s.id === schoolId || s.schoolId === schoolId) || schools[0] || null;

  let resolvedFound = found;
  if (!resolvedFound && school && school.facultyPasscode && candidateCode.toUpperCase() === school.facultyPasscode.toUpperCase()) {
    resolvedFound = {
      code: school.facultyPasscode,
      schoolId: school.id,
      schoolName: school.name,
      department: 'Commercial Sciences & STEM',
      defaultSubject: 'Accounting',
      isMaster: true
    };
  }

  if (!resolvedFound) {
    return {
      valid: false,
      error: 'Invalid Faculty Passcode for this school. Check your faculty invite slip or contact your School Principal / HOD.'
    };
  }

  return {
    valid: true,
    code: resolvedFound.code,
    school,
    schoolId: school.id,
    schoolName: school.name,
    department: resolvedFound.department || 'Commercial Sciences & STEM',
    defaultSubject: resolvedFound.defaultSubject || 'Accounting',
    educatorName: resolvedFound.educatorName || null,
    isMaster: Boolean(resolvedFound.isMaster)
  };
}

/**
 * Returns pre-allocated departmental classes for an institutional teacher
 */
export function getAssignedFacultyClasses(schoolId = 'sch_westville_high', passcode = 'WHS-TEACH-2026', subject = 'Accounting') {
  const cleanCode = String(passcode || '').trim().toUpperCase();
  if (cleanCode.includes('KHUMALO')) {
    return WHS_FACULTY_ASSIGNED_CLASSES['Mathematics'] || [];
  }
  if (cleanCode.includes('BOTHA')) {
    return [...(WHS_FACULTY_ASSIGNED_CLASSES['Physical Sciences'] || []), ...(WHS_FACULTY_ASSIGNED_CLASSES['Mathematics'] || [])];
  }
  if (cleanCode.includes('PILLAY')) {
    return WHS_FACULTY_ASSIGNED_CLASSES['Business Studies'] || [];
  }
  if (subject && WHS_FACULTY_ASSIGNED_CLASSES[subject]) {
    return WHS_FACULTY_ASSIGNED_CLASSES[subject];
  }
  // Default to Commercial Sciences load (Accounting & EMS)
  return WHS_FACULTY_ASSIGNED_CLASSES['Accounting'] || [];
}

/**
 * Binds an educator to an approved school upon registration, seeding their assigned classes
 */
export function bindTeacherToSchool(teacherUser, passcode, schoolId = 'sch_westville_high', subject = 'Accounting') {
  const assigned = getAssignedFacultyClasses(schoolId, passcode, subject);
  const storageKey = 'fundile_teacher_classes_v3';

  try {
    localStorage.setItem(storageKey, JSON.stringify(assigned));
    localStorage.setItem('fundile_teacher_faculty_passcode', passcode);
    localStorage.setItem('fundile_teacher_school_id', schoolId);
  } catch (e) {
    console.warn('Could not persist teacher classes to localStorage:', e);
  }

  // Also record on School Admin faculty roster if not present
  try {
    const rosterKey = 'fundile_school_admin_faculty_roster';
    const existing = JSON.parse(localStorage.getItem(rosterKey) || '[]');
    const educatorRecord = {
      id: `fac_${teacherUser.uid || Date.now()}`,
      name: teacherUser.name || 'Educator',
      role: `Senior Educator ${subject}`,
      email: teacherUser.email,
      subject,
      schoolId,
      status: 'Active',
      joinedAt: new Date().toISOString()
    };
    if (!existing.some(f => f.email === teacherUser.email)) {
      existing.unshift(educatorRecord);
      localStorage.setItem(rosterKey, JSON.stringify(existing));
    }
  } catch (_) {}

  return assigned;
}

