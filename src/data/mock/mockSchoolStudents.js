/**
 * Westville High School — Enrolled Learners (300 Named Students)
 * Grades 8 to 12 (60 learners per grade across 4 class sections A, B, C, D).
 * Authentic South African names, real class enrollments, and dynamic teacher assignments.
 */

const SA_FIRST_NAMES = [
  'Nqobile', 'Sipho', 'Thabo', 'Lerato', 'Kagiso', 'Ayanda', 'Bongani', 'Zanele',
  'Lindiwe', 'Mpho', 'Tshepo', 'Katlego', 'Busisiwe', 'Khaya', 'Simphiwe', 'Sanele',
  'Nandi', 'Bandile', 'Sibusiso', 'Ntombi', 'Karabo', 'Tebogo', 'Nomvula', 'Dineo',
  'Lungelo', 'Mthokozisi', 'Banele', 'Nompumelelo', 'Keanu', 'Tristan', 'Chloe',
  'Liam', 'Ethan', 'Kayla', 'Devan', 'Priyanka', 'Aarav', 'Kiara', 'Rohan',
  'Fatima', 'Yusuf', 'Amina', 'Zaheer', 'Tariq', 'Anika', 'Johan', 'Anke',
  'Pieter', 'Willem', 'Lize', 'Ruan', 'Marike', 'Franco', 'Elize', 'Hendrik',
  'Siyabonga', 'Gugulethu', 'Themba', 'Zola', 'Jabulani'
];

const SA_LAST_NAMES = [
  'Dlamini', 'Khumalo', 'Sithole', 'Mthembu', 'Ndlovu', 'Zulu', 'Zwane', 'Mkhize',
  'Gumede', 'Cele', 'Buthelezi', 'Nxumalo', 'Bhengu', 'Ngcobo', 'Ntombela', 'Dube',
  'Mabena', 'Baloyi', 'Chauke', 'Maluleke', 'Van der Merwe', 'Botha', 'Du Plessis',
  'Coetzee', 'Fourie', 'Pretorius', 'Venter', 'Steyn', 'Snyman', 'De Klerk',
  'Naidoo', 'Pillay', 'Govender', 'Moodley', 'Chetty', 'Patel', 'Singh', 'Reddy',
  'Maharaj', 'Cassim', 'Moosa', 'Khan', 'Adams', 'Petersen', 'Jacobs', 'Hendricks',
  'Williams', 'Cupido', 'Abrahams', 'Smith'
];

const CLASSES = [
  // Grade 8
  { id: 'cls-8a', grade: 8, name: 'Grade 8A', educator: 'Mr. P. Dlamini', sub: 'natural_sciences' },
  { id: 'cls-8b', grade: 8, name: 'Grade 8B', educator: 'Mrs. H. Moonsamy', sub: 'ems' },
  { id: 'cls-8c', grade: 8, name: 'Grade 8C', educator: 'Mr. K. Pillay', sub: 'natural_sciences' },
  { id: 'cls-8d', grade: 8, name: 'Grade 8D', educator: 'Mrs. R. Chetty', sub: 'ems' },
  // Grade 9
  { id: 'cls-9a', grade: 9, name: 'Grade 9A', educator: 'Ms. Z. Ndlovu', sub: 'ems' },
  { id: 'cls-9b', grade: 9, name: 'Grade 9B', educator: 'Ms. T. Cele', sub: 'ems' },
  { id: 'cls-9c', grade: 9, name: 'Grade 9C', educator: 'Mr. H. Van Zyl', sub: 'natural_sciences' },
  { id: 'cls-9d', grade: 9, name: 'Grade 9D', educator: 'Mrs. N. Dube', sub: 'natural_sciences' },
  // Grade 10
  { id: 'cls-10a', grade: 10, name: 'Grade 10A (Commerce)', educator: 'Mr. N. Sithole', sub: 'accounting' },
  { id: 'cls-10b', grade: 10, name: 'Grade 10B (Sciences)', educator: 'Mr. A. Sithole', sub: 'physics' },
  { id: 'cls-10c', grade: 10, name: 'Grade 10C (General)', educator: 'Mrs. L. Botha', sub: 'mathematical_literacy' },
  { id: 'cls-10d', grade: 10, name: 'Grade 10D (Tech Maths)', educator: 'Mr. D. Govender', sub: 'tech_maths' },
  // Grade 11
  { id: 'cls-11a', grade: 11, name: 'Grade 11A (Pure Maths)', educator: 'Mrs. S. Pillay', sub: 'maths' },
  { id: 'cls-11b', grade: 11, name: 'Grade 11B (Physical Sci)', educator: 'Dr. K. Mthembu', sub: 'physics' },
  { id: 'cls-11c', grade: 11, name: 'Grade 11C (Accounting)', educator: 'Ms. K. Mkhize', sub: 'accounting' },
  { id: 'cls-11d', grade: 11, name: 'Grade 11D (Life Sciences)', educator: 'Mrs. A. Coetzee', sub: 'lifesci' },
  // Grade 12
  { id: 'cls-12a', grade: 12, name: 'Grade 12A (Senior Sci)', educator: 'Dr. V. Naidoo', sub: 'physics' },
  { id: 'cls-12b', grade: 12, name: 'Grade 12B (Pure Maths)', educator: 'Mrs. M. Van der Merwe', sub: 'maths' },
  { id: 'cls-12c', grade: 12, name: 'Grade 12C (Commerce)', educator: 'Mr. B. Khuzwayo', sub: 'accounting' },
  { id: 'cls-12d', grade: 12, name: 'Grade 12D (Lit & Business)', educator: 'Mr. T. Baloyi', sub: 'business' }
];

// Build 300 deterministic learners (15 learners per class across 20 classes)
export const MOCK_SCHOOL_STUDENTS = [];

let studentCounter = 1;
CLASSES.forEach((cls, clsIndex) => {
  for (let seat = 0; seat < 15; seat++) {
    const fnIndex = (clsIndex * 3 + seat * 7) % SA_FIRST_NAMES.length;
    const lnIndex = (clsIndex * 5 + seat * 11 + 3) % SA_LAST_NAMES.length;
    const firstName = SA_FIRST_NAMES[fnIndex];
    const lastName = SA_LAST_NAMES[lnIndex];
    const studentId = `sch-st-${String(studentCounter).padStart(3, '0')}`;
    
    // Assign 1 or 2 authentic homework tasks from the class educator
    const assignedTasks = [];
    if (cls.grade >= 10) {
      if (cls.sub === 'accounting') {
        assignedTasks.push({
          id: `task-${studentCounter}-1`,
          subject: 'accounting',
          subjectName: 'Accounting',
          title: 'Cash Receipts Journal: VAT 15% Calculation',
          assignedBy: cls.educator,
          dueText: 'DUE TODAY',
          dueTime: '17:00',
          marks: 12,
          estimatedMins: 15,
          topic: 'Cash Receipts Journal'
        });
      } else if (cls.sub === 'maths') {
        assignedTasks.push({
          id: `task-${studentCounter}-1`,
          subject: 'maths',
          subjectName: 'Mathematics',
          title: 'Algebraic Expressions & Factorisation Drill',
          assignedBy: cls.educator,
          dueText: 'DUE FRIDAY',
          dueTime: '08:00',
          marks: 10,
          estimatedMins: 12,
          topic: 'Algebraic Expressions'
        });
      } else if (cls.sub === 'physics') {
        assignedTasks.push({
          id: `task-${studentCounter}-1`,
          subject: 'physics',
          subjectName: 'Physical Sciences',
          title: 'Newtonian Forces & Vectors on an Incline',
          assignedBy: cls.educator,
          dueText: 'DUE TOMORROW',
          dueTime: '16:00',
          marks: 15,
          estimatedMins: 20,
          topic: "Newton's Laws of Motion"
        });
      } else if (cls.sub === 'lifesci') {
        assignedTasks.push({
          id: `task-${studentCounter}-1`,
          subject: 'lifesci',
          subjectName: 'Life Sciences',
          title: 'Meiosis Stages & Non-Disjunction Analysis',
          assignedBy: cls.educator,
          dueText: 'DUE THURSDAY',
          dueTime: '17:00',
          marks: 12,
          estimatedMins: 18,
          topic: 'Meiosis'
        });
      } else {
        assignedTasks.push({
          id: `task-${studentCounter}-1`,
          subject: cls.sub,
          subjectName: cls.sub.toUpperCase(),
          title: `${cls.name} Term 2 Diagnostic Review`,
          assignedBy: cls.educator,
          dueText: 'DUE FRIDAY',
          dueTime: '12:00',
          marks: 10,
          estimatedMins: 15,
          topic: 'Curriculum Review'
        });
      }
    } else {
      // Junior Phase (Grades 8-9)
      assignedTasks.push({
        id: `task-${studentCounter}-1`,
        subject: cls.sub === 'ems' ? 'ems' : 'natural_sciences',
        subjectName: cls.sub === 'ems' ? 'EMS' : 'Natural Sciences',
        title: cls.sub === 'ems' ? 'The Accounting Equation (A = O + L)' : 'Photosynthesis & Respiration',
        assignedBy: cls.educator,
        dueText: 'DUE TODAY',
        dueTime: '16:30',
        marks: 10,
        estimatedMins: 15,
        topic: cls.sub === 'ems' ? 'Accounting Equation' : 'Photosynthesis'
      });
    }

    // Assign parent ID (with some shared parents for sibling links)
    // Parent index wraps so 250 parents cover 300 students (50 sibling pairs)
    const parentIndex = ((studentCounter - 1) % 250) + 1;
    const parentId = `sch-par-${String(parentIndex).padStart(3, '0')}`;

    MOCK_SCHOOL_STUDENTS.push({
      id: studentId,
      name: `${firstName} ${lastName}`,
      firstName,
      lastName,
      grade: cls.grade,
      classId: cls.id,
      className: cls.name,
      schoolId: 'westville_high',
      schoolName: 'Westville High School',
      isIndependent: false,
      parentId,
      email: `${firstName.toLowerCase()}.${lastName.toLowerCase()}${studentCounter}@westvillehigh.co.za`,
      xp: 450 + (studentCounter * 23) % 2800,
      streak: 1 + (studentCounter * 7) % 18,
      accuracyRate: 68 + (studentCounter * 3) % 28,
      masteryIndex: 65 + (studentCounter * 4) % 32,
      assignedTasks,
      enrolledSubjects: cls.grade >= 10
        ? ['accounting', 'maths', 'physics', 'business', 'lifesci', 'tech_maths', 'mathematical_literacy']
        : ['ems', 'natural_sciences', 'maths'],
      primarySubject: cls.sub
    });

    studentCounter++;
  }
});
