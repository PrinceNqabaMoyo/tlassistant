/**
 * Parents & Guardians Registry
 * 250 School Parents (linked to 300 Westville High learners, 50 sibling pairs)
 * 80 Independent Parents (linked to 100 Homeschool learners, 20 sibling pairs)
 * Sibling linking, WhatsApp notification numbers, focus times, and data savings.
 */

import { MOCK_SCHOOL_STUDENTS } from './mockSchoolStudents.js';
import { MOCK_INDEPENDENT_STUDENTS } from './mockIndependentStudents.js';

const PARENT_TITLES = ['Mr.', 'Mrs.', 'Dr.', 'Ms.', 'Prof.'];

const PARENT_FIRST_NAMES = [
  'Bongani', 'Nomusa', 'Sizwe', 'Thandiwe', 'Mandla', 'Zandile', 'Zweli', 'Nokuthula',
  'David', 'Sarah', 'Michael', 'Jennifer', 'Mark', 'Lisa', 'Robert', 'Karen',
  'Rajesh', 'Sunita', 'Vikram', 'Pooja', 'Anand', 'Kavitha', 'Dinesh', 'Preetha',
  'Ahmed', 'Fatima', 'Mohamed', 'Zainab', 'Rashid', 'Amina', 'Ibrahim', 'Mariam',
  'Johannes', 'Maria', 'Willem', 'Anna', 'Petrus', 'Susanna', 'Cornelis', 'Elisabeth',
  'Vusi', 'Dudu', 'Themba', 'Gugu', 'Kabelo', 'Nthabiseng', 'Tshepo', 'Mpho'
];

// Group school students by parentId
const schoolStudentsByParent = {};
MOCK_SCHOOL_STUDENTS.forEach(student => {
  if (!schoolStudentsByParent[student.parentId]) {
    schoolStudentsByParent[student.parentId] = [];
  }
  schoolStudentsByParent[student.parentId].push(student);
});

// Group independent students by parentId
const indStudentsByParent = {};
MOCK_INDEPENDENT_STUDENTS.forEach(student => {
  if (!indStudentsByParent[student.parentId]) {
    indStudentsByParent[student.parentId] = [];
  }
  indStudentsByParent[student.parentId].push(student);
});

// ── 250 School Parents ──
export const MOCK_SCHOOL_PARENTS = [];
for (let p = 1; p <= 250; p++) {
  const pId = `sch-par-${String(p).padStart(3, '0')}`;
  const children = schoolStudentsByParent[pId] || [];
  const primaryChild = children[0] || { lastName: 'Dlamini', firstName: 'Child' };
  
  const title = PARENT_TITLES[p % PARENT_TITLES.length];
  const firstName = PARENT_FIRST_NAMES[p % PARENT_FIRST_NAMES.length];
  const lastName = primaryChild.lastName;
  const phone = `+27 8${p % 4} ${String(200 + p * 3).padStart(3, '0')} ${String(1000 + p * 29).padStart(4, '0')}`;

  MOCK_SCHOOL_PARENTS.push({
    id: pId,
    name: `${title} ${firstName} ${lastName}`,
    title,
    firstName,
    lastName,
    phone,
    whatsappPhone: phone,
    email: `${firstName.toLowerCase()}.${lastName.toLowerCase()}@guardianmail.co.za`,
    schoolId: 'westville_high',
    isIndependent: false,
    childrenIds: children.map(c => c.id),
    childrenCount: children.length,
    childrenSummary: children.map(c => `${c.name} (${c.className})`).join(', '),
    weeklyFocusHours: (2.5 + (p % 15) * 0.4).toFixed(1),
    questionsMastered: 35 + (p % 40) * 2,
    dataSavedMB: 440 + (p % 20) * 12, // Saved vs streaming video tutoring
    activeSubscription: 'Standard Institutional (Covered by School SGB)',
    renewalDate: '2026-12-31'
  });
}

// ── 80 Independent Parents ──
export const MOCK_INDEPENDENT_PARENTS = [];
for (let p = 1; p <= 80; p++) {
  const pId = `ind-par-${String(p).padStart(3, '0')}`;
  const children = indStudentsByParent[pId] || [];
  const primaryChild = children[0] || { lastName: 'Molefe', firstName: 'Child' };
  
  const title = PARENT_TITLES[(p + 2) % PARENT_TITLES.length];
  const firstName = PARENT_FIRST_NAMES[(p + 5) % PARENT_FIRST_NAMES.length];
  const lastName = primaryChild.lastName;
  const phone = `+27 7${p % 5} ${String(300 + p * 5).padStart(3, '0')} ${String(2000 + p * 41).padStart(4, '0')}`;

  MOCK_INDEPENDENT_PARENTS.push({
    id: pId,
    name: `${title} ${firstName} ${lastName}`,
    title,
    firstName,
    lastName,
    phone,
    whatsappPhone: phone,
    email: `${firstName.toLowerCase()}.${lastName.toLowerCase()}@homefamily.co.za`,
    schoolId: null,
    isIndependent: true,
    childrenIds: children.map(c => c.id),
    childrenCount: children.length,
    childrenSummary: children.map(c => `${c.name} (Grade ${c.grade})`).join(', '),
    weeklyFocusHours: (3.0 + (p % 12) * 0.5).toFixed(1),
    questionsMastered: 48 + (p % 35) * 2,
    dataSavedMB: 510 + (p % 15) * 15,
    activeSubscription: 'Fundile Pro Family Annual (R149/mo)',
    renewalDate: '2027-02-15'
  });
}

export const MOCK_ALL_PARENTS = [...MOCK_SCHOOL_PARENTS, ...MOCK_INDEPENDENT_PARENTS];
