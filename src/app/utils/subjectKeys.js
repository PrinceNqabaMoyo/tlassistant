export const getSubjectKeyFromSelection = ({
  selectedCurriculumKey,
  selectedGrade,
  selectedSubject,
} = {}) => {
  const subjectName = typeof selectedSubject === 'string' 
    ? selectedSubject 
    : (selectedSubject?.name || selectedSubject?.id || 'all');
  return `${selectedCurriculumKey || 'all'}_${selectedGrade || 'all'}_${subjectName}`;
};
