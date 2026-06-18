export const getSubjectKeyFromSelection = ({
  selectedCurriculumKey,
  selectedGrade,
  selectedSubject,
} = {}) => {
  const subjectName = selectedSubject?.name || 'all';
  return `${selectedCurriculumKey || 'all'}_${selectedGrade || 'all'}_${subjectName}`;
};
