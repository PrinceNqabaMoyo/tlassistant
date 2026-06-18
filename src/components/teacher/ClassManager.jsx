import React, { useState, useEffect } from 'react';
import { collection, query, where, getDocs, doc, setDoc, deleteDoc, updateDoc } from 'firebase/firestore';
import { Users, Plus, Trash2, ChevronLeft, BookOpen, GraduationCap } from 'lucide-react';

const CAPS_SUBJECTS = [
  'Accounting',
  'Business Studies',
  'Economics',
  'History',
  'Mathematics',
  'Mathematical Literacy',
  'Physical Sciences',
  'Life Sciences',
  'Geography',
  'English',
  'Afrikaans',
  'EMS',
];

const GRADES = [10, 11, 12];

const ClassManager = ({ db, currentUser, onBack }) => {
  const [classes, setClasses] = useState([]);
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [showEnrollForm, setShowEnrollForm] = useState(false);
  const [selectedClass, setSelectedClass] = useState(null);

  const [newClass, setNewClass] = useState({
    name: '',
    subject: '',
    grade: '',
    description: '',
  });

  useEffect(() => {
    const loadData = async () => {
      if (!currentUser?.uid || !db) return;
      try {
        const classesRef = collection(db, 'artifacts', 'tlassistant', 'users', currentUser.uid, 'teacher_classes');
        const classesSnap = await getDocs(classesRef);
        const classesList = [];
        classesSnap.forEach((doc) => classesList.push({ id: doc.id, ...doc.data() }));
        setClasses(classesList);

        const usersRef = collection(db, 'users');
        const studentsQuery = query(usersRef, where('role', '==', 'student'));
        const studentsSnap = await getDocs(studentsQuery);
        const studentsList = [];
        studentsSnap.forEach((doc) => studentsList.push({ id: doc.id, ...doc.data() }));
        setStudents(studentsList);
      } catch (e) {
        console.error('Error loading class data:', e);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, [currentUser, db]);

  const handleCreateClass = async () => {
    if (!newClass.name || !newClass.subject || !newClass.grade) return;
    const classId = `class-${Date.now()}`;
    const classRef = doc(db, 'artifacts', 'tlassistant', 'users', currentUser.uid, 'teacher_classes', classId);
    await setDoc(classRef, {
      ...newClass,
      teacherId: currentUser.uid,
      createdAt: new Date().toISOString(),
      enrolledStudents: [],
    });
    setClasses((prev) => [...prev, { id: classId, ...newClass, enrolledStudents: [] }]);
    setShowCreateForm(false);
    setNewClass({ name: '', subject: '', grade: '', description: '' });
  };

  const handleEnrollStudent = async (studentId) => {
    if (!selectedClass) return;
    const classRef = doc(db, 'artifacts', 'tlassistant', 'users', currentUser.uid, 'teacher_classes', selectedClass.id);
    const updated = [...(selectedClass.enrolledStudents || []), studentId];
    await updateDoc(classRef, { enrolledStudents: updated });
    setClasses((prev) => prev.map((c) => (c.id === selectedClass.id ? { ...c, enrolledStudents: updated } : c)));
    setSelectedClass((prev) => ({ ...prev, enrolledStudents: updated }));
  };

  const handleDeleteClass = async (classId) => {
    if (!window.confirm('Delete this class?')) return;
    await deleteDoc(doc(db, 'artifacts', 'tlassistant', 'users', currentUser.uid, 'teacher_classes', classId));
    setClasses((prev) => prev.filter((c) => c.id !== classId));
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-64">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600" />
      </div>
    );
  }

  return (
    <div className="p-4 sm:p-6 lg:p-8">
      <div className="flex items-center justify-between mb-6">
        <button onClick={onBack} className="flex items-center text-blue-600 hover:text-blue-800 transition-colors">
          <ChevronLeft className="h-5 w-5 mr-2" />
          Back to Dashboard
        </button>
        <h1 className="text-3xl font-bold text-gray-900">Class Management</h1>
      </div>

      <button
        onClick={() => setShowCreateForm(true)}
        className="mb-6 flex items-center bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
      >
        <Plus className="h-4 w-4 mr-2" />
        Create New Class
      </button>

      {showCreateForm && (
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <h3 className="text-lg font-semibold mb-4">Create Class</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="text"
              placeholder="Class name (e.g. Grade 10 Accounting A)"
              value={newClass.name}
              onChange={(e) => setNewClass({ ...newClass, name: e.target.value })}
              className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
            <select
              value={newClass.subject}
              onChange={(e) => setNewClass({ ...newClass, subject: e.target.value })}
              className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Subject</option>
              {CAPS_SUBJECTS.map((s) => (
                <option key={s} value={s}>{s}</option>
              ))}
            </select>
            <select
              value={newClass.grade}
              onChange={(e) => setNewClass({ ...newClass, grade: e.target.value })}
              className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Grade</option>
              {GRADES.map((g) => (
                <option key={g} value={g}>Grade {g}</option>
              ))}
            </select>
            <input
              type="text"
              placeholder="Description (optional)"
              value={newClass.description}
              onChange={(e) => setNewClass({ ...newClass, description: e.target.value })}
              className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="flex gap-3 mt-4">
            <button onClick={handleCreateClass} className="bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors">
              Save Class
            </button>
            <button onClick={() => setShowCreateForm(false)} className="bg-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-400 transition-colors">
              Cancel
            </button>
          </div>
        </div>
      )}

      {showEnrollForm && selectedClass && (
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <h3 className="text-lg font-semibold mb-4">Enroll Students into {selectedClass.name}</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-h-96 overflow-y-auto">
            {students
              .filter((s) => !(selectedClass.enrolledStudents || []).includes(s.id))
              .map((student) => (
                <div key={student.id} className="border border-gray-200 rounded-lg p-4 flex items-center justify-between">
                  <div>
                    <p className="font-medium">{student.name || student.email}</p>
                    <p className="text-sm text-gray-500">{student.email}</p>
                  </div>
                  <button
                    onClick={() => handleEnrollStudent(student.id)}
                    className="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 transition-colors"
                    title="Enroll"
                  >
                    <Plus className="h-4 w-4" />
                  </button>
                </div>
              ))}
          </div>
          <button onClick={() => setShowEnrollForm(false)} className="mt-4 bg-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-400 transition-colors">
            Done
          </button>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {classes.map((cls) => (
          <div key={cls.id} className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center justify-between mb-3">
              <BookOpen className="h-6 w-6 text-blue-600" />
              <div className="flex gap-2">
                <button
                  onClick={() => { setSelectedClass(cls); setShowEnrollForm(true); }}
                  className="p-2 text-green-600 hover:bg-green-50 rounded-lg transition-colors"
                  title="Enroll Students"
                >
                  <Users className="h-4 w-4" />
                </button>
                <button
                  onClick={() => handleDeleteClass(cls.id)}
                  className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                  title="Delete"
                >
                  <Trash2 className="h-4 w-4" />
                </button>
              </div>
            </div>
            <h3 className="text-lg font-semibold text-gray-800">{cls.name}</h3>
            <div className="flex items-center gap-2 mt-2 text-sm text-gray-600">
              <GraduationCap className="h-4 w-4" />
              <span>{cls.subject} — Grade {cls.grade}</span>
            </div>
            <p className="text-sm text-gray-500 mt-2">{cls.description}</p>
            <div className="mt-3 flex items-center gap-2 text-sm">
              <Users className="h-4 w-4 text-gray-400" />
              <span>{(cls.enrolledStudents || []).length} enrolled</span>
            </div>
          </div>
        ))}
      </div>

      {classes.length === 0 && !showCreateForm && (
        <div className="text-center py-12">
          <BookOpen className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No classes yet</h3>
          <p className="text-gray-500">Create your first class to get started.</p>
        </div>
      )}
    </div>
  );
};

export default ClassManager;
