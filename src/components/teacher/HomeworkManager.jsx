import React, { useState, useEffect } from 'react';
import { collection, getDocs, doc, setDoc } from 'firebase/firestore';
import { FileText, ChevronLeft, Send, CalendarDays } from 'lucide-react';

const HomeworkManager = ({ db, currentUser, onBack }) => {
  const [classes, setClasses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedClassId, setSelectedClassId] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [showMarksImmediately, setShowMarksImmediately] = useState(false);
  const [sending, setSending] = useState(false);

  useEffect(() => {
    const loadClasses = async () => {
      if (!currentUser?.uid || !db) return;
      try {
        const ref = collection(db, 'artifacts', 'tlassistant', 'users', currentUser.uid, 'teacher_classes');
        const snap = await getDocs(ref);
        const list = [];
        snap.forEach((doc) => list.push({ id: doc.id, ...doc.data() }));
        setClasses(list);
      } catch (e) {
        console.error(e);
      } finally {
        setLoading(false);
      }
    };
    loadClasses();
  }, [currentUser, db]);

  const handleSend = async () => {
    if (!selectedClassId || !title || !dueDate) return;
    setSending(true);
    try {
      const homeworkId = `hw-${Date.now()}`;
      const ref = doc(db, 'artifacts', 'tlassistant', 'users', currentUser.uid, 'teacher_homework', homeworkId);
      await setDoc(ref, {
        classId: selectedClassId,
        title,
        description,
        dueDate,
        showMarksImmediately,
        teacherId: currentUser.uid,
        createdAt: new Date().toISOString(),
        status: 'active',
      });
      setTitle('');
      setDescription('');
      setDueDate('');
      setShowMarksImmediately(false);
      setSelectedClassId('');
      alert('Homework sent successfully.');
    } catch (e) {
      console.error(e);
      alert('Failed to send homework.');
    } finally {
      setSending(false);
    }
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
        <h1 className="text-3xl font-bold text-gray-900">Homework</h1>
      </div>

      <div className="bg-white rounded-lg shadow-md p-6 max-w-2xl">
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Select Class</label>
            <select
              value={selectedClassId}
              onChange={(e) => setSelectedClassId(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Choose a class</option>
              {classes.map((c) => (
                <option key={c.id} value={c.id}>{c.name} ({c.subject} — Grade {c.grade})</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Cash Journals Exercise 3"
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Description / Instructions</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              rows={4}
              placeholder="Enter homework instructions..."
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Due Date</label>
            <input
              type="date"
              value={dueDate}
              onChange={(e) => setDueDate(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg">
            <input
              type="checkbox"
              id="showMarks"
              checked={showMarksImmediately}
              onChange={(e) => setShowMarksImmediately(e.target.checked)}
              className="h-4 w-4 text-blue-600"
            />
            <label htmlFor="showMarks" className="text-sm text-gray-700">
              Allow students to see their marks immediately after submission
            </label>
          </div>

          <button
            onClick={handleSend}
            disabled={!selectedClassId || !title || !dueDate || sending}
            className="w-full bg-green-600 text-white py-3 px-4 rounded-lg hover:bg-green-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors flex items-center justify-center"
          >
            {sending ? (
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white" />
            ) : (
              <>
                <Send className="h-4 w-4 mr-2" />
                Send Homework
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};

export default HomeworkManager;
