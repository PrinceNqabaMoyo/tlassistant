/**
 * Independent & Homeschool Learners Registry (100 Named Students)
 * Self-paced, unlinked to any school faculty, 0 teacher homework assignments.
 * Autonomous learning paths, BKT calibrated mastery, and individual home parent links.
 */

const SA_FIRST_NAMES = [
  'Kagiso', 'Nolwazi', 'Siphamandla', 'Thandeka', 'Mbali', 'Siyabonga', 'Gugulethu',
  'Tshegofatso', 'Bokamoso', 'Keabetswe', 'Omphile', 'Lesedi', 'Kopano', 'Rethabile',
  'Oratile', 'Kamogelo', 'Phenyo', 'Amogelang', 'Mokgadi', 'Lethabo', 'Tshepo',
  'Neo', 'Tebogo', 'Kabelo', 'Thato', 'Dimpho', 'Boitumelo', 'Karabo', 'Thabiso',
  'Brandon', 'Caitlin', 'Declan', 'Emma', 'Liam', 'Megan', 'Joshua', 'Hannah',
  'Callum', 'Jessica', 'Dylan', 'Shannon', 'Aidan', 'Ashleigh', 'Matthew', 'Courtney',
  'Raeesa', 'Zubair', 'Tasneem', 'Faheem', 'Khadija', 'Bilal', 'Sumaiya', 'Hamza',
  'Devan', 'Shriya', 'Nikhil', 'Pooja', 'Kavish', 'Ananya', 'Sanjay', 'Meera',
  'Christiaan', 'Marike', 'Danie', 'Sunette', 'Tiaan', 'Inge', 'Carel', 'Elana',
  'Wian', 'Carla', 'Henco', 'Minke', 'Renier', 'Anneri', 'Stiaan', 'Lara'
];

const SA_LAST_NAMES = [
  'Molefe', 'Mokoena', 'Masango', 'Nhlapo', 'Khoza', 'Radebe', 'Mabaso', 'Shabalala',
  'Hlongwane', 'Sibeko', 'Mahlangu', 'Skosana', 'Mnguni', 'Msibi', 'Kubheka',
  'Fourie', 'Meyer', 'Nel', 'Swart', 'Basson', 'Louw', 'Theron', 'Van Niekerk',
  'Naude', 'Oosthuizen', 'Potgieter', 'Prinsloo', 'Smit', 'Viljoen', 'Visagie',
  'Govender', 'Naidoo', 'Pillay', 'Moodley', 'Chetty', 'Singh', 'Reddy', 'Padayachee',
  'Maharaj', 'Cassim', 'Moosa', 'Ebrahim', 'Saloojee', 'Vally', 'Ismail',
  'Abrahams', 'Fortune', 'Davids', 'Cupido', 'Hendricks'
];

export const MOCK_INDEPENDENT_STUDENTS = [];

for (let i = 1; i <= 100; i++) {
  const fnIndex = (i * 7 + 3) % SA_FIRST_NAMES.length;
  const lnIndex = (i * 13 + 5) % SA_LAST_NAMES.length;
  const firstName = SA_FIRST_NAMES[fnIndex];
  const lastName = SA_LAST_NAMES[lnIndex];
  const grade = 8 + (i % 5); // Grades 8, 9, 10, 11, 12

  // 80 independent parents for 100 students (20 sibling links)
  const parentIndex = ((i - 1) % 80) + 1;
  const parentId = `ind-par-${String(parentIndex).padStart(3, '0')}`;

  MOCK_INDEPENDENT_STUDENTS.push({
    id: `ind-st-${String(i).padStart(3, '0')}`,
    name: `${firstName} ${lastName}`,
    firstName,
    lastName,
    grade,
    classId: null,
    className: 'Independent Homeschool',
    schoolId: null,
    schoolName: 'Self-Paced Homeschool (Independent)',
    isIndependent: true,
    parentId,
    email: `${firstName.toLowerCase()}.${lastName.toLowerCase()}@homelearn.co.za`,
    xp: 320 + (i * 31) % 3500,
    streak: (i * 3) % 24,
    accuracyRate: 72 + (i * 2) % 25,
    masteryIndex: 70 + (i * 3) % 28,
    // INVARIANT: 0 teacher school assignments!
    assignedTasks: [],
    enrolledSubjects: grade >= 10
      ? ['accounting', 'maths', 'physics', 'business', 'lifesci', 'tech_maths', 'mathematical_literacy']
      : ['ems', 'natural_sciences', 'maths'],
    primarySubject: grade >= 10 ? 'maths' : 'ems',
    homeschoolPlatform: 'Fundile Pro Autonomous'
  });
}
