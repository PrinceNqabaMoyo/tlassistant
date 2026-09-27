import React, { useState, useEffect } from 'react';
import { Users, Plus, Copy, Check, X, Share2, School, BookOpen, Sparkles, ExternalLink } from 'lucide-react';

/**
 * ClassManagerModal Component (Layer D — Phase D4)
 * Allows teachers and solo tutors to create classes, generate 6-character join codes,
 * inspect student rosters, and dispatch diagnostics.
 */
export default function ClassManagerModal({
  isOpen = false,
  onClose = () => {},
  teacherId = 'tch_demo_101',
  teacherName = 'Mr. Sithole',
}) {
  const [classes, setClasses] = useState([]);
  const [activeTab, setActiveTab] = useState('list'); // 'list' | 'create'
  const [selectedClass, setSelectedClass] = useState(null);
  const [copiedCode, setCopiedCode] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  // New Class Form State
  const [className, setClassName] = useState('');
  const [subject, setSubject] = useState('Mathematics');
  const [grade, setGrade] = useState('10');
  const [createSuccess, setCreateSuccess] = useState(null);

  // Load teacher classes on open
  useEffect(() => {
    if (isOpen) {
      fetchTeacherClasses();
    }
  }, [isOpen, teacherId]);

  const fetchTeacherClasses = async () => {
    setIsLoading(true);
    try {
      const res = await fetch(`/api/classes/teacher/${teacherId}`);
      if (res.ok) {
        const data = await res.json();
        setClasses(data.classes || []);
        if (data.classes && data.classes.length > 0 && !selectedClass) {
          setSelectedClass(data.classes[0]);
        }
      } else {
        // Fallback mock class for demo/testing
        const mockClasses = [
          {
            classId: 'cls_10_math_demo',
            name: 'Grade 10 Mathematics — Alpha',
            subject: 'Mathematics',
            grade: '10',
            joinCode: 'MATH8X',
            studentCount: 3,
            students: [
              { studentId: 's1', studentName: 'Lerato Dlamini', joinedAt: '2026-09-18' },
              { studentId: 's2', studentName: 'Thabo Mokoena', joinedAt: '2026-09-19' },
              { studentId: 's3', studentName: 'Sipho Zulu', joinedAt: '2026-09-20' },
            ],
            createdAt: new Date().toISOString(),
          },
        ];
        setClasses(mockClasses);
        setSelectedClass(mockClasses[0]);
      }
    } catch {
      // Fallback mock
      const mockClasses = [
        {
          classId: 'cls_10_math_demo',
          name: 'Grade 10 Mathematics — Alpha',
          subject: 'Mathematics',
          grade: '10',
          joinCode: 'MATH8X',
          studentCount: 3,
          students: [
            { studentId: 's1', studentName: 'Lerato Dlamini', joinedAt: '2026-09-18' },
            { studentId: 's2', studentName: 'Thabo Mokoena', joinedAt: '2026-09-19' },
            { studentId: 's3', studentName: 'Sipho Zulu', joinedAt: '2026-09-20' },
          ],
          createdAt: new Date().toISOString(),
        },
      ];
      setClasses(mockClasses);
      setSelectedClass(mockClasses[0]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreateClass = async (e) => {
    e.preventDefault();
    if (!className.trim()) return;

    setIsLoading(true);
    try {
      const res = await fetch('/api/classes/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          teacherId,
          teacherName,
          className: className.trim(),
          subject,
          grade,
        }),
      });

      if (res.ok) {
        const data = await res.json();
        setCreateSuccess(data.class);
        setClasses(prev => [data.class, ...prev]);
        setSelectedClass(data.class);
        setClassName('');
        setActiveTab('list');
      } else {
        // Fallback local creation
        const randomCode = Math.random().toString(36).substring(2, 8).toUpperCase();
        const fallbackClass = {
          classId: `cls_${grade}_${Date.now()}`,
          name: className.trim(),
          subject,
          grade,
          joinCode: randomCode,
          studentCount: 0,
          students: [],
          createdAt: new Date().toISOString(),
        };
        setCreateSuccess(fallbackClass);
        setClasses(prev => [fallbackClass, ...prev]);
        setSelectedClass(fallbackClass);
        setClassName('');
        setActiveTab('list');
      }
    } catch {
      const randomCode = Math.random().toString(36).substring(2, 8).toUpperCase();
      const fallbackClass = {
        classId: `cls_${grade}_${Date.now()}`,
        name: className.trim(),
        subject,
        grade,
        joinCode: randomCode,
        studentCount: 0,
        students: [],
        createdAt: new Date().toISOString(),
      };
      setCreateSuccess(fallbackClass);
      setClasses(prev => [fallbackClass, ...prev]);
      setSelectedClass(fallbackClass);
      setClassName('');
      setActiveTab('list');
    } finally {
      setIsLoading(false);
    }
  };

  const copyJoinCode = (code) => {
    navigator.clipboard.writeText(code);
    setCopiedCode(code);
    setTimeout(() => setCopiedCode(null), 2500);
  };

  const shareWhatsApp = (classItem) => {
    const text = `Join our ${classItem.name} class on Fundile! Go to the student profile, click "Join Class" and enter code: *${classItem.joinCode}*`;
    window.open(`https://wa.me/?text=${encodeURIComponent(text)}`, '_blank');
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fadeIn">
      <div className="relative w-full max-w-4xl bg-slate-900 border border-slate-700 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[85vh]">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-950/70">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
              <School className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-lg font-bold text-white">Teacher LMS Cockpit — Class Roster</h2>
              <p className="text-xs text-slate-400">Manage classes, generate 6-char join codes, and track learner enrollments</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Switcher */}
        <div className="flex items-center justify-between px-6 py-3 border-b border-slate-800 bg-slate-900/50">
          <div className="flex gap-2">
            <button
              onClick={() => setActiveTab('list')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition cursor-pointer ${
                activeTab === 'list'
                  ? 'bg-cyan-600 text-white shadow-sm'
                  : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              My Classes ({classes.length})
            </button>
            <button
              onClick={() => setActiveTab('create')}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition flex items-center gap-1.5 cursor-pointer ${
                activeTab === 'create'
                  ? 'bg-cyan-600 text-white shadow-sm'
                  : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              <Plus className="w-3.5 h-3.5" />
              Create Class
            </button>
          </div>

          <span className="text-xs text-slate-400 font-mono">Teacher: {teacherName}</span>
        </div>

        {/* Main Body */}
        <div className="flex-1 overflow-y-auto p-6">
          {activeTab === 'create' ? (
            /* Create Class Form */
            <form onSubmit={handleCreateClass} className="max-w-xl mx-auto space-y-4 py-4">
              <div className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/60 space-y-4">
                <h3 className="text-sm font-bold text-white flex items-center gap-2">
                  <Sparkles className="w-4 h-4 text-cyan-400" />
                  Create New Subject Class
                </h3>

                <div>
                  <label className="block text-xs font-medium text-slate-300 mb-1">Class Name</label>
                  <input
                    type="text"
                    value={className}
                    onChange={e => setClassName(e.target.value)}
                    placeholder="e.g. Grade 10 Mathematics Set A"
                    className="w-full px-3.5 py-2 rounded-lg bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-cyan-500"
                    required
                  />
                </div>

                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-medium text-slate-300 mb-1">Subject</label>
                    <select
                      value={subject}
                      onChange={e => setSubject(e.target.value)}
                      className="w-full px-3.5 py-2 rounded-lg bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-cyan-500 cursor-pointer"
                    >
                      <option value="Mathematics">Mathematics</option>
                      <option value="Accounting">Accounting</option>
                      <option value="EMS">EMS</option>
                      <option value="Business Studies">Business Studies</option>
                      <option value="Physical Sciences">Physical Sciences</option>
                      <option value="Life Sciences">Life Sciences</option>
                      <option value="Mathematical Literacy">Mathematical Literacy</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs font-medium text-slate-300 mb-1">Grade</label>
                    <select
                      value={grade}
                      onChange={e => setGrade(e.target.value)}
                      className="w-full px-3.5 py-2 rounded-lg bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-cyan-500 cursor-pointer"
                    >
                      <option value="7">Grade 7</option>
                      <option value="8">Grade 8</option>
                      <option value="9">Grade 9</option>
                      <option value="10">Grade 10</option>
                      <option value="11">Grade 11</option>
                      <option value="12">Grade 12</option>
                    </select>
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={isLoading || !className.trim()}
                  className="w-full py-2.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow-md cursor-pointer disabled:opacity-50"
                >
                  {isLoading ? 'Creating...' : 'Generate Class & 6-Char Join Code'}
                </button>
              </div>
            </form>
          ) : (
            /* Class List & Roster View */
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Left sidebar: class list */}
              <div className="space-y-3">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">Your Classes</h4>
                {classes.length === 0 ? (
                  <div className="p-4 rounded-xl bg-slate-800/40 border border-slate-800 text-center text-xs text-slate-400">
                    No classes created yet. Click "Create Class" above!
                  </div>
                ) : (
                  classes.map(c => (
                    <div
                      key={c.classId}
                      onClick={() => setSelectedClass(c)}
                      className={`p-3.5 rounded-xl border transition cursor-pointer ${
                        selectedClass?.classId === c.classId
                          ? 'bg-slate-800 border-cyan-500/80 shadow-md'
                          : 'bg-slate-800/40 border-slate-700/60 hover:bg-slate-800/70'
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <span className="text-xs font-bold text-white truncate max-w-[140px]">{c.name}</span>
                        <span className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-cyan-950/60 text-cyan-300 border border-cyan-800/60">
                          {c.studentCount} {c.studentCount === 1 ? 'Learner' : 'Learners'}
                        </span>
                      </div>
                      <div className="flex items-center justify-between mt-2 text-[11px] text-slate-400">
                        <span>{c.subject} · Gr {c.grade}</span>
                        <span className="font-mono font-bold text-amber-300">{c.joinCode}</span>
                      </div>
                    </div>
                  ))
                )}
              </div>

              {/* Right area: Selected class details & student roster */}
              <div className="md:col-span-2 space-y-4">
                {selectedClass ? (
                  <div className="p-5 rounded-xl bg-slate-800/50 border border-slate-700/80 space-y-5">
                    {/* Class Banner & Join Code Card */}
                    <div className="flex flex-wrap items-center justify-between gap-4 p-4 rounded-xl bg-slate-950/70 border border-slate-800">
                      <div>
                        <h3 className="text-base font-bold text-white">{selectedClass.name}</h3>
                        <p className="text-xs text-slate-400 mt-0.5">
                          {selectedClass.subject} · Grade {selectedClass.grade} · Created by {selectedClass.teacherName}
                        </p>
                      </div>

                      {/* 6-Char Join Code Pill */}
                      <div className="flex items-center gap-2 bg-slate-900 px-3.5 py-2 rounded-xl border border-amber-500/50 shadow-inner">
                        <div>
                          <div className="text-[10px] font-bold uppercase tracking-wider text-slate-400">Join Code</div>
                          <div className="text-lg font-black tracking-widest text-amber-400 font-mono">
                            {selectedClass.joinCode}
                          </div>
                        </div>

                        <div className="flex items-center gap-1 ml-2">
                          <button
                            onClick={() => copyJoinCode(selectedClass.joinCode)}
                            className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition cursor-pointer"
                            title="Copy code"
                          >
                            {copiedCode === selectedClass.joinCode ? (
                              <Check className="w-4 h-4 text-emerald-400" />
                            ) : (
                              <Copy className="w-4 h-4" />
                            )}
                          </button>
                          <button
                            onClick={() => shareWhatsApp(selectedClass)}
                            className="p-1.5 rounded-lg bg-emerald-950/60 hover:bg-emerald-900 text-emerald-400 transition cursor-pointer"
                            title="Share via WhatsApp"
                          >
                            <Share2 className="w-4 h-4" />
                          </button>
                        </div>
                      </div>
                    </div>

                    {/* Student Roster Table */}
                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <h4 className="text-xs font-bold uppercase tracking-wider text-slate-300 flex items-center gap-1.5">
                          <Users className="w-3.5 h-3.5 text-cyan-400" />
                          Enrolled Learners ({selectedClass.studentCount || 0})
                        </h4>
                        <span className="text-[11px] text-slate-400">Auto-synced from student profiles</span>
                      </div>

                      {!selectedClass.students || selectedClass.students.length === 0 ? (
                        <div className="py-8 text-center text-xs text-slate-400 border border-dashed border-slate-800 rounded-xl">
                          No students have joined yet. Share join code <strong className="text-amber-400 font-mono">{selectedClass.joinCode}</strong> with your class!
                        </div>
                      ) : (
                        <div className="border border-slate-800 rounded-xl overflow-hidden">
                          <table className="w-full text-left text-xs text-slate-300">
                            <thead className="bg-slate-950/60 text-slate-400 border-b border-slate-800 text-[11px]">
                              <tr>
                                <th className="py-2.5 px-4 font-semibold">Learner Name</th>
                                <th className="py-2.5 px-4 font-semibold">Student ID</th>
                                <th className="py-2.5 px-4 font-semibold">Date Joined</th>
                                <th className="py-2.5 px-4 font-semibold text-right">Status</th>
                              </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-800/60">
                              {selectedClass.students.map((std, idx) => (
                                <tr key={std.studentId || idx} className="hover:bg-slate-800/30">
                                  <td className="py-2.5 px-4 font-semibold text-white">{std.studentName}</td>
                                  <td className="py-2.5 px-4 font-mono text-slate-400">{std.studentId}</td>
                                  <td className="py-2.5 px-4 text-slate-400">
                                    {std.joinedAt ? std.joinedAt.split('T')[0] : 'Recent'}
                                  </td>
                                  <td className="py-2.5 px-4 text-right">
                                    <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-950/60 text-emerald-300 border border-emerald-800/40">
                                      Active
                                    </span>
                                  </td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>
                      )}
                    </div>
                  </div>
                ) : (
                  <div className="p-12 text-center text-xs text-slate-500">
                    Select a class on the left to inspect its student roster.
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
