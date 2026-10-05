import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

import {
  MOCK_SCHOOL,
  MOCK_FACULTY,
  MOCK_SCHOOL_STUDENTS,
  MOCK_INDEPENDENT_STUDENTS,
  MOCK_SCHOOL_PARENTS,
  MOCK_INDEPENDENT_PARENTS,
} from '../src/data/mock/mockEnvironment.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const outputFile = path.join(rootDir, 'mockschool.md');

console.log('Generating mockschool.md...');

let md = `# WESTVILLE HIGH SCHOOL & INDEPENDENT HOMESCHOOL REGISTRY (MOCK ENVIRONMENT)
**Document Generated:** 2026-10-05  
**Institutional Blueprint:** South African National Curriculum Standards (CAPS) • Grades 8–12  
**Purpose:** Authoritative reference, audit roster, ability grouping baseline, and agent test simulation ledger.

---

## TABLE OF CONTENTS
1. [Executive Summary & School Administrative Profile](#1-executive-summary--school-administrative-profile)
2. [Academic Departments & Leadership](#2-academic-departments--leadership)
3. [Faculty & Educator Roster (60 Teachers)](#3-faculty--educator-roster-60-teachers)
4. [Westville High Enrolled Students by Grade & Class (300 Learners)](#4-westville-high-enrolled-students-by-grade--class-300-learners)
   - [Grade 8 Classes (8A, 8B, 8C, 8D - 60 Learners)](#grade-8-classes)
   - [Grade 9 Classes (9A, 9B, 9C, 9D - 60 Learners)](#grade-9-classes)
   - [Grade 10 Classes (10A, 10B, 10C, 10D - 60 Learners)](#grade-10-classes)
   - [Grade 11 Classes (11A, 11B, 11C, 11D - 60 Learners)](#grade-11-classes)
   - [Grade 12 Classes (12A, 12B, 12C, 12D - 60 Learners)](#grade-12-classes)
5. [Independent & Homeschool Learners (100 Students)](#5-independent--homeschool-learners-100-students)
6. [Parents & Guardians Directory (330 Total Parents)](#6-parents--guardians-directory-330-total-parents)
   - [Westville High School Parents (250 Parents)](#westville-high-school-parents)
   - [Independent Homeschool Parents (80 Parents)](#independent-homeschool-parents)
7. [Cross-Reference & Ability Grouping Schema](#7-cross-reference--ability-grouping-schema)

---

## 1. Executive Summary & School Administrative Profile

| Field | Detail |
| :--- | :--- |
| **School Name** | **${MOCK_SCHOOL.name}** |
| **Short Name** | ${MOCK_SCHOOL.shortName} |
| **EMIS Number** | \`${MOCK_SCHOOL.emisNumber}\` |
| **Province / District** | ${MOCK_SCHOOL.province} • ${MOCK_SCHOOL.district} |
| **School Classification** | ${MOCK_SCHOOL.type} |
| **Grades Offered** | Grades 8, 9, 10, 11, 12 |
| **Current Term & Academic Year** | Term ${MOCK_SCHOOL.term}, Academic Year ${MOCK_SCHOOL.academicYear} |
| **Total Enrolled Learners** | **${MOCK_SCHOOL.totalLearners} Learners** (60 per grade across 20 class sections) |
| **Total Teaching Faculty** | **${MOCK_SCHOOL.totalFaculty} Educators** (1 Headmaster, 1 Deputy, 9 HODs, 49 Subject Educators) |
| **Total Associated Parents** | **${MOCK_SCHOOL_PARENTS.length} School Parents** (covering 300 students with 50 sibling pairs) |
| **Independent Homeschool Pool** | **${MOCK_INDEPENDENT_STUDENTS.length} Learners** & **${MOCK_INDEPENDENT_PARENTS.length} Parents** |
| **Grand Total User Profiles** | **790 Complete Traceable Personas** (400 Learners, 60 Teachers, 330 Parents) |

---

## 2. Academic Departments & Leadership

`;

MOCK_SCHOOL.departments.forEach((dept, idx) => {
  const hod = MOCK_FACULTY.find(f => f.id === dept.hodId) || { name: 'Unknown HOD', title: 'HOD' };
  md += `### Department ${idx + 1}: ${dept.name}\n`;
  md += `- **Department ID:** \`${dept.id}\`\n`;
  md += `- **Head of Department (HOD):** **${hod.name}** (\`${dept.hodId}\` - ${hod.title})\n`;
  md += `- **Curriculum Subjects Covered:** ${dept.subjects.map(s => `\`${s}\``).join(', ')}\n\n`;
});

md += `---

## 3. Faculty & Educator Roster (60 Teachers)

| ID | Name | Role & Title | Department | Primary Subject | Grades | Class Assignment | Join Code | Email | Phone | Enrolled Learners | Class Avg |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
`;

MOCK_FACULTY.forEach(t => {
  const gradesStr = t.grades.join(', ');
  md += `| \`${t.id}\` | **${t.name}** | ${t.title} | \`${t.department}\` | ${t.subject} | Gr ${gradesStr} | ${t.assignedClassName} | \`${t.joinCode}\` | ${t.email} | \`${t.phone}\` | ${t.totalLearners} | **${t.classAverage}%** |\n`;
});

md += `\n---\n\n## 4. Westville High Enrolled Students by Grade & Class (300 Learners)\n\n`;

// Group students by grade and class
const grades = [8, 9, 10, 11, 12];

grades.forEach(g => {
  md += `### Grade ${g} Classes\n\n`;
  const gradeStudents = MOCK_SCHOOL_STUDENTS.filter(s => s.grade === g);
  
  // Group by classId
  const classesInGrade = [...new Set(gradeStudents.map(s => s.classId))];
  
  classesInGrade.forEach(clsId => {
    const classStudents = gradeStudents.filter(s => s.classId === clsId);
    const clsMeta = MOCK_SCHOOL.classes.find(c => c.id === clsId) || { name: clsId, room: 'N/A' };
    const classTeacher = MOCK_FACULTY.find(f => f.assignedClassId === clsId) || { name: 'Faculty Staff', subject: 'Core' };

    md += `#### ${clsMeta.name} (\`${clsId}\` • Room: ${clsMeta.room})\n`;
    md += `- **Class Educator:** **${classTeacher.name}** (${classTeacher.title}) • Join Code: \`${classTeacher.joinCode}\`\n`;
    md += `- **Enrolled Learners:** ${classStudents.length} Students\n\n`;

    md += `| Seat | Student ID | Student Name | Parent ID | Primary Subject | Enrolled Subjects | Mastery Index | Accuracy | XP | Streak | Current Homework Task |\n`;
    md += `| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |\n`;

    classStudents.forEach((st, seatIdx) => {
      const task = st.assignedTasks[0] || { title: 'Self-Paced Practice', dueText: 'None' };
      const subjectsStr = st.enrolledSubjects.map(sub => `\`${sub}\``).join(', ');
      md += `| ${seatIdx + 1} | \`${st.id}\` | **${st.name}** | \`${st.parentId}\` | \`${st.primarySubject}\` | ${subjectsStr} | **${st.masteryIndex}%** | ${st.accuracyRate}% | ${st.xp} | 🔥 ${st.streak}d | *${task.title}* (${task.dueText}) |\n`;
    });
    md += `\n`;
  });
});

md += `---\n\n## 5. Independent & Homeschool Learners (100 Students)\n\n`;
md += `These learners study independently on the self-paced curriculum, unlinked to any school faculty or homework tasks.\n\n`;
md += `| # | Student ID | Student Name | Grade | Parent ID | Primary Subject | Enrolled Subjects | Mastery Index | Accuracy | XP | Streak | Email |\n`;
md += `| :---: | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |\n`;

MOCK_INDEPENDENT_STUDENTS.forEach((st, idx) => {
  const subjectsStr = st.enrolledSubjects.map(sub => `\`${sub}\``).join(', ');
  md += `| ${idx + 1} | \`${st.id}\` | **${st.name}** | Gr ${st.grade} | \`${st.parentId}\` | \`${st.primarySubject}\` | ${subjectsStr} | **${st.masteryIndex}%** | ${st.accuracyRate}% | ${st.xp} | 🔥 ${st.streak}d | ${st.email} |\n`;
});

md += `\n---\n\n## 6. Parents & Guardians Directory (330 Total Parents)\n\n`;

md += `### Westville High School Parents (250 Parents)\n\n`;
md += `| Parent ID | Parent / Guardian Name | Phone / WhatsApp | Email | Children Count | Linked Children & Class | Focus Time/Wk | Questions Mastered | Mobile Data Saved |\n`;
md += `| :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: |\n`;

MOCK_SCHOOL_PARENTS.forEach(p => {
  md += `| \`${p.id}\` | **${p.name}** | \`${p.phone}\` | ${p.email} | **${p.childrenCount}** | ${p.childrenSummary} | ${p.weeklyFocusHours}h | ${p.questionsMastered} | **${p.dataSavedMB} MB** |\n`;
});

md += `\n### Independent Homeschool Parents (80 Parents)\n\n`;
md += `| Parent ID | Parent / Guardian Name | Phone / WhatsApp | Email | Children Count | Linked Children & Grade | Focus Time/Wk | Questions Mastered | Mobile Data Saved |\n`;
md += `| :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: |\n`;

MOCK_INDEPENDENT_PARENTS.forEach(p => {
  md += `| \`${p.id}\` | **${p.name}** | \`${p.phone}\` | ${p.email} | **${p.childrenCount}** | ${p.childrenSummary} | ${p.weeklyFocusHours}h | ${p.questionsMastered} | **${p.dataSavedMB} MB** |\n`;
});

md += `\n---\n\n## 7. Cross-Reference & Ability Grouping Schema\n\n`;
md += `### Proposed Ability Grouping Tiers (Automated Classification):\n`;
md += `1. **Remedial / At-Risk Tier (\`masteryIndex < 50%\`):**\n`;
md += `   - Target: Diagnostic baseline incomplete or recurring misconception tags.\n`;
md += `   - System Intervention: Automatic 5-minute atomic micro-drills (e.g. VAT net vs gross, sign distribution).\n`;
md += `2. **Core Competency Tier (\`50% <= masteryIndex < 75%\`):**\n`;
md += `   - Target: Autonomous practice unlocked, working through assigned class drills.\n`;
md += `   - System Intervention: Stepwise procedure tracker with method marks \`[M]\` and carry-over accuracy.\n`;
md += `3. **Distinction Track (\`masteryIndex >= 75%\`):**\n`;
md += `   - Target: Level 7 Distinction candidates prepping for cycle tests and prelims.\n`;
md += `   - System Intervention: Timed assessment mode, past-exam papers, and advanced multi-concept questions.\n\n`;

md += `### Stream Classifications:\n`;
md += `- **Commercial Sciences Stream:** Grade 10A, 11C, 12C (Accounting, Business Studies, EMS).\n`;
md += `- **STEM Stream:** Grade 10B, 11A, 11B, 11D, 12A, 12B (Mathematics, Physical Sciences, Life Sciences).\n`;
md += `- **General & Technical Stream:** Grade 10C, 10D, 12D (Mathematical Literacy, Technical Mathematics, Business Studies).\n`;

fs.writeFileSync(outputFile, md, 'utf-8');
console.log('Successfully wrote mockschool.md! Size:', md.length, 'bytes');
