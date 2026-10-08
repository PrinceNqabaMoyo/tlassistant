/**
 * Central Mock Environment Orchestrator
 * Integrates Westville High School (360 learners across Grades 7–12, 60 faculty, 250 parents)
 * and Independent Homeschool (100 learners, 80 parents).
 */

import { MOCK_SCHOOL } from './mockSchool.js';
import { MOCK_FACULTY } from './mockFaculty.js';
import { MOCK_SCHOOL_STUDENTS } from './mockSchoolStudents.js';
import { MOCK_INDEPENDENT_STUDENTS } from './mockIndependentStudents.js';
import { MOCK_SCHOOL_PARENTS, MOCK_INDEPENDENT_PARENTS, MOCK_ALL_PARENTS } from './mockParents.js';

export {
  MOCK_SCHOOL,
  MOCK_FACULTY,
  MOCK_SCHOOL_STUDENTS,
  MOCK_INDEPENDENT_STUDENTS,
  MOCK_SCHOOL_PARENTS,
  MOCK_INDEPENDENT_PARENTS,
  MOCK_ALL_PARENTS
};

export const MOCK_ALL_STUDENTS = [
  ...MOCK_SCHOOL_STUDENTS,
  ...MOCK_INDEPENDENT_STUDENTS
];

export function getStudentById(studentId) {
  return MOCK_ALL_STUDENTS.find(s => s.id === studentId) || null;
}

export function getTeacherById(teacherId) {
  return MOCK_FACULTY.find(t => t.id === teacherId) || null;
}

export function getParentById(parentId) {
  return MOCK_ALL_PARENTS.find(p => p.id === parentId) || null;
}

export function getClassById(classId) {
  return MOCK_SCHOOL.classes.find(c => c.id === classId) || null;
}

export function getStudentsByClass(classId) {
  return MOCK_SCHOOL_STUDENTS.filter(s => s.classId === classId);
}

export function getChildrenForParent(parentId) {
  const parent = getParentById(parentId);
  if (!parent) return [];
  return parent.childrenIds.map(id => getStudentById(id)).filter(Boolean);
}

/**
 * Filter personas for the quick persona switcher modal.
 */
export function searchPersonas(query = '', filterRole = 'all') {
  const q = String(query).toLowerCase().trim();

  let pool = [];

  if (filterRole === 'all' || filterRole === 'school_students') {
    pool.push(...MOCK_SCHOOL_STUDENTS.map(s => ({
      ...s,
      type: 'school_student',
      badge: `Gr ${s.grade} • ${s.className}`,
      subtitle: `${s.schoolName} • Tasks: ${s.assignedTasks.length}`
    })));
  }

  if (filterRole === 'all' || filterRole === 'independent_students') {
    pool.push(...MOCK_INDEPENDENT_STUDENTS.map(s => ({
      ...s,
      type: 'independent_student',
      badge: `Gr ${s.grade} • Independent`,
      subtitle: `Homeschool • Self-Paced • 0 School Tasks`
    })));
  }

  if (filterRole === 'all' || filterRole === 'teachers') {
    pool.push(...MOCK_FACULTY.map(t => ({
      ...t,
      type: 'teacher',
      badge: t.title,
      subtitle: `${t.subject} • Class: ${t.assignedClassName} • Code: ${t.joinCode}`
    })));
  }

  if (filterRole === 'all' || filterRole === 'parents') {
    pool.push(...MOCK_ALL_PARENTS.map(p => ({
      ...p,
      type: 'parent',
      badge: p.isIndependent ? 'Independent Parent' : 'School Parent',
      subtitle: `Children (${p.childrenCount}): ${p.childrenSummary}`
    })));
  }

  if (filterRole === 'all' || filterRole === 'school_admin') {
    pool.push({
      id: 'admin-westville',
      name: 'Westville High School Administration',
      title: 'Principal Dr. V. Naidoo & SGB Executive',
      type: 'school_admin',
      badge: 'School Admin Cockpit',
      subtitle: 'SASAMS EMIS: 500124892 • 300 Learners • 60 Teachers'
    });
  }

  if (!q) return pool.slice(0, 50);

  return pool.filter(p => 
    p.name.toLowerCase().includes(q) ||
    (p.badge && p.badge.toLowerCase().includes(q)) ||
    (p.subtitle && p.subtitle.toLowerCase().includes(q)) ||
    (p.email && p.email.toLowerCase().includes(q)) ||
    (p.id && p.id.toLowerCase().includes(q))
  ).slice(0, 50);
}
