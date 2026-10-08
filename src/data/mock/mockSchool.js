/**
 * Westville High School — CAPS Institutional Blueprint
 * EMIS: 500124892 • Pinetown District, KwaZulu-Natal
 */

export const MOCK_SCHOOL = {
  id: 'westville_high',
  name: 'Westville High School',
  shortName: 'Westville High',
  emisNumber: '500124892',
  province: 'KwaZulu-Natal',
  district: 'Pinetown District',
  type: 'Public Secondary School (Section 21)',
  grades: [7, 8, 9, 10, 11, 12],
  term: 2,
  academicYear: 2026,
  totalLearners: 360,
  totalFaculty: 60,
  headmasterId: 'fac-01', // Dr. V. Naidoo
  deputyHeadId: 'fac-02', // Mrs. S. Pillay
  departments: [
    {
      id: 'dept_commerce',
      name: 'Commercial Sciences',
      hodId: 'fac-03', // Mr. N. Sithole
      subjects: ['accounting', 'business', 'ems']
    },
    {
      id: 'dept_mathematics',
      name: 'Mathematical Sciences',
      hodId: 'fac-04', // Mrs. M. Van der Merwe
      subjects: ['maths', 'tech_maths', 'mathematical_literacy']
    },
    {
      id: 'dept_sciences',
      name: 'Natural & Physical Sciences',
      hodId: 'fac-05', // Dr. K. Mthembu
      subjects: ['physics', 'lifesci', 'natural_sciences']
    }
  ],
  classes: [
    // Grade 7 (Senior Phase Entry)
    { id: 'cls-7a', name: 'Grade 7A', grade: 7, room: 'Block J-01', educatorId: 'fac-53', learnerCount: 15 },
    { id: 'cls-7b', name: 'Grade 7B', grade: 7, room: 'Block J-02', educatorId: 'fac-48', learnerCount: 15 },
    { id: 'cls-7c', name: 'Grade 7C', grade: 7, room: 'Block J-03', educatorId: 'fac-21', learnerCount: 15 },
    { id: 'cls-7d', name: 'Grade 7D', grade: 7, room: 'Block J-04', educatorId: 'fac-55', learnerCount: 15 },
    // Grade 8
    { id: 'cls-8a', name: 'Grade 8A', grade: 8, room: 'Block A-01', educatorId: 'fac-10', learnerCount: 15 },
    { id: 'cls-8b', name: 'Grade 8B', grade: 8, room: 'Block A-02', educatorId: 'fac-11', learnerCount: 15 },
    { id: 'cls-8c', name: 'Grade 8C', grade: 8, room: 'Block A-03', educatorId: 'fac-12', learnerCount: 15 },
    { id: 'cls-8d', name: 'Grade 8D', grade: 8, room: 'Block A-04', educatorId: 'fac-13', learnerCount: 15 },
    // Grade 9
    { id: 'cls-9a', name: 'Grade 9A', grade: 9, room: 'Block B-01', educatorId: 'fac-14', learnerCount: 15 },
    { id: 'cls-9b', name: 'Grade 9B', grade: 9, room: 'Block B-02', educatorId: 'fac-15', learnerCount: 15 },
    { id: 'cls-9c', name: 'Grade 9C', grade: 9, room: 'Block B-03', educatorId: 'fac-16', learnerCount: 15 },
    { id: 'cls-9d', name: 'Grade 9D', grade: 9, room: 'Block B-04', educatorId: 'fac-17', learnerCount: 15 },
    // Grade 10
    { id: 'cls-10a', name: 'Grade 10A (Commerce)', grade: 10, room: 'Block C-01', educatorId: 'fac-03', learnerCount: 15 },
    { id: 'cls-10b', name: 'Grade 10B (Sciences)', grade: 10, room: 'Block C-02', educatorId: 'fac-18', learnerCount: 15 },
    { id: 'cls-10c', name: 'Grade 10C (General)', grade: 10, room: 'Block C-03', educatorId: 'fac-19', learnerCount: 15 },
    { id: 'cls-10d', name: 'Grade 10D (Tech Maths)', grade: 10, room: 'Block C-04', educatorId: 'fac-20', learnerCount: 15 },
    // Grade 11
    { id: 'cls-11a', name: 'Grade 11A (Pure Maths)', grade: 11, room: 'Block D-01', educatorId: 'fac-02', learnerCount: 15 }, // Deputy Pillay
    { id: 'cls-11b', name: 'Grade 11B (Physical Sci)', grade: 11, room: 'Block D-02', educatorId: 'fac-21', learnerCount: 15 },
    { id: 'cls-11c', name: 'Grade 11C (Accounting)', grade: 11, room: 'Block D-03', educatorId: 'fac-22', learnerCount: 15 },
    { id: 'cls-11d', name: 'Grade 11D (Life Sciences)', grade: 11, room: 'Block D-04', educatorId: 'fac-23', learnerCount: 15 },
    // Grade 12
    { id: 'cls-12a', name: 'Grade 12A (Senior Sci)', grade: 12, room: 'Block E-01', educatorId: 'fac-01', learnerCount: 15 }, // Headmaster Naidoo
    { id: 'cls-12b', name: 'Grade 12B (Pure Maths)', grade: 12, room: 'Block E-02', educatorId: 'fac-04', learnerCount: 15 },
    { id: 'cls-12c', name: 'Grade 12C (Commerce)', grade: 12, room: 'Block E-03', educatorId: 'fac-24', learnerCount: 15 },
    { id: 'cls-12d', name: 'Grade 12D (Lit & Business)', grade: 12, room: 'Block E-04', educatorId: 'fac-25', learnerCount: 15 }
  ]
};
