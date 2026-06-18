import { buildApiUrl } from '../../utils/apiBaseUrl';
import React, { useState } from 'react';
import { collection, addDoc, serverTimestamp } from 'firebase/firestore';
import { ChevronLeft, Loader2, FilePlus, AlertTriangle, Trash2, PlusCircle } from 'lucide-react';
import AssignClassModal from '../admin/AssignClassModal';

const AssessmentGenerator = ({ db, currentUser, setView }) => {
    const [subject, setSubject] = useState('Mathematics');
    const [grade, setGrade] = useState('10');
    const [selectedTopic, setSelectedTopic] = useState('');
    const [selectedSubtopic, setSelectedSubtopic] = useState('');
    const [numQuestions, setNumQuestions] = useState('3');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [assessmentData, setAssessmentData] = useState(null);
    const [feedbackMode, setFeedbackMode] = useState('instant');

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedClassId, setSelectedClassId] = useState('');
    const [assignmentStatus, setAssignmentStatus] = useState('');

    const teacherClasses = [
        { id: 'class_10a', name: 'Grade 10A Maths' },
        { id: 'class_10b', name: 'Grade 10B Maths' },
        { id: 'class_11c', name: 'Grade 11C Maths Lit' },
    ];

    // Mock CAPS topics - you'll need to import the actual data
    const capsTopics = {
        'Mathematics': {
            '10': [
                { name: 'Algebra', subtopics: ['Linear equations', 'Quadratic equations'] },
                { name: 'Geometry', subtopics: ['Circles', 'Triangles'] }
            ]
        }
    };

    const availableTopics = capsTopics[subject]?.[grade] || [];
    const availableSubtopics = availableTopics.find(t => t.name === selectedTopic)?.subtopics || [];

    const handleSubjectChange = (e) => { setSubject(e.target.value); setSelectedTopic(''); setSelectedSubtopic(''); };
    const handleGradeChange = (e) => { setGrade(e.target.value); setSelectedTopic(''); setSelectedSubtopic(''); };
    const handleTopicChange = (e) => { setSelectedTopic(e.target.value); setSelectedSubtopic(''); };

    const handleGenerateAssessment = async (e) => {
        e.preventDefault();
        if (!selectedTopic) { setError("Please select a main topic."); return; }
        setLoading(true);
        setError(null);
        setAssessmentData(null);
        setAssignmentStatus('');
        const topicForAPI = selectedSubtopic && selectedSubtopic !== 'all' ? `${selectedTopic}: ${selectedSubtopic}` : selectedTopic;
        try {
            const response = await fetch(buildApiUrl('/api/teacher/create-assessment'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: topicForAPI, grade, num_questions: parseInt(numQuestions, 10) }),
            });
            if (!response.ok) { const errorData = await response.json(); throw new Error(errorData.error || 'An unknown error occurred.'); }
            const data = await response.json();
            setAssessmentData(data.assessment);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    const handleApproveAndAssign = () => {
        if (!assessmentData) return;
        setAssignmentStatus('');
        setIsModalOpen(true);
    };

    const handleConfirmAssignment = async () => {
        if (!selectedClassId) {
            alert("Please select a class.");
            return;
        }
        setLoading(true);
        try {
            const assessmentRef = collection(db, "assessments");
            await addDoc(assessmentRef, {
                teacherId: currentUser.uid,
                classId: selectedClassId,
                subject: subject,
                grade: grade,
                topic: selectedTopic,
                subtopic: selectedSubtopic,
                questions: assessmentData,
                createdAt: serverTimestamp(),
                feedbackMode: feedbackMode,
            });
            setAssignmentStatus(`Assessment successfully assigned to class ${selectedClassId}!`);
        } catch (e) {
            console.error("Error adding document: ", e);
            setAssignmentStatus('Failed to assign assessment. Please try again.');
            setError(e.message);
        } finally {
            setLoading(false);
            setIsModalOpen(false);
        }
    };

    const handleQuestionTextChange = (qIndex, newText) => { const updatedData = [...assessmentData]; updatedData[qIndex].question_text = newText; setAssessmentData(updatedData); };
    const handleMarkingPointChange = (qIndex, pIndex, newPoint) => { const updatedData = [...assessmentData]; updatedData[qIndex].marking_scheme[pIndex].point = newPoint; setAssessmentData(updatedData); };
    const handleMarksChange = (qIndex, pIndex, newMarks) => { const updatedData = [...assessmentData]; updatedData[qIndex].marking_scheme[pIndex].marks = parseInt(newMarks, 10); setAssessmentData(updatedData); };
    const handleAddMarkingPoint = (qIndex) => { const updatedData = [...assessmentData]; updatedData[qIndex].marking_scheme.push({ point: 'New marking point', marks: 1 }); setAssessmentData(updatedData); };
    const handleRemoveMarkingPoint = (qIndex, pIndex) => { const updatedData = [...assessmentData]; updatedData[qIndex].marking_scheme.splice(pIndex, 1); setAssessmentData(updatedData); };
    const handleSolutionChange = (qIndex, newSolution) => { const updatedData = [...assessmentData]; updatedData[qIndex].solution = newSolution; setAssessmentData(updatedData); };

    return (
        <>
            <AssignClassModal
                isOpen={isModalOpen}
                onClose={() => setIsModalOpen(false)}
                onConfirm={handleConfirmAssignment}
                classes={teacherClasses}
                setSelectedClassId={setSelectedClassId}
            />
            <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
                <div className="max-w-4xl mx-auto">
                    <button onClick={() => setView('dashboard')} className="flex items-center text-gray-600 hover:text-blue-600 font-medium mb-6 group">
                        <ChevronLeft className="h-5 w-5 mr-2 transition-transform group-hover:-translate-x-1" />
                        Back to Dashboard
                    </button>
                    <h1 className="text-3xl font-bold text-gray-800 mb-2">Assessment Generator</h1>
                    <p className="text-gray-600 mb-8">Create a draft assessment with a detailed marking scheme using AI.</p>
                    <form onSubmit={handleGenerateAssessment} className="bg-white p-6 rounded-xl shadow-md border border-gray-200 mb-8">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label htmlFor="subject" className="block text-sm font-medium text-gray-700 mb-1">Subject</label>
                                <select id="subject" value={subject} onChange={handleSubjectChange} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">{Object.keys(capsTopics).map(s => <option key={s} value={s}>{s}</option>)}</select>
                            </div>
                            <div>
                                <label htmlFor="grade" className="block text-sm font-medium text-gray-700 mb-1">Grade</label>
                                <select id="grade" value={grade} onChange={handleGradeChange} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">{[7, 8, 9, 10, 11, 12].map(g => <option key={g} value={g}>Grade {g}</option>)}</select>
                            </div>
                            <div className="md:col-span-2">
                                <label htmlFor="topic" className="block text-sm font-medium text-gray-700 mb-1">Topic</label>
                                <select id="topic" value={selectedTopic} onChange={handleTopicChange} required className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"><option value="" disabled>-- Select a Topic --</option>{availableTopics.map(t => <option key={t.name} value={t.name}>{t.name}</option>)}</select>
                            </div>
                            <div className="md:col-span-2">
                                <label htmlFor="subtopic" className="block text-sm font-medium text-gray-700 mb-1">Subtopic (Optional)</label>
                                <select id="subtopic" value={selectedSubtopic} onChange={e => setSelectedSubtopic(e.target.value)} disabled={!selectedTopic || availableSubtopics.length === 0} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100"><option value="all">All Subtopics</option>{availableSubtopics.map(st => <option key={st} value={st}>{st}</option>)}</select>
                            </div>
                            <div>
                                <label htmlFor="numQuestions" className="block text-sm font-medium text-gray-700 mb-1">Number of Questions</label>
                                <select id="numQuestions" value={numQuestions} onChange={e => setNumQuestions(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">{[1, 2, 3, 5, 10].map(n => <option key={n} value={n}>{n}</option>)}</select>
                            </div>
                            <div>
                                <label htmlFor="feedbackMode" className="block text-sm font-medium text-gray-700 mb-1">Feedback Mode</label>
                                <select id="feedbackMode" value={feedbackMode} onChange={e => setFeedbackMode(e.target.value)} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
                                    <option value="instant">Instant Feedback</option>
                                    <option value="on_submission">Feedback on Final Submission</option>
                                    <option value="teacher_only">Teacher Marked Only</option>
                                </select>
                            </div>
                        </div>
                        <div className="mt-6 text-right">
                            <button type="submit" disabled={loading} className="inline-flex items-center px-6 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-gray-400">{loading ? <Loader2 className="mr-2 h-5 w-5 animate-spin" /> : <FilePlus className="mr-2 h-5 w-5" />}{loading ? 'Generating...' : 'Generate Draft'}</button>
                        </div>
                    </form>
                    {assignmentStatus && (<div className={`p-4 mb-4 text-sm rounded-lg ${error ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`} role="alert"><span className="font-medium">{assignmentStatus}</span></div>)}
                    {error && !assignmentStatus && (<div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded-md mb-8" role="alert"><div className="flex"><AlertTriangle className="h-5 w-5 text-red-500 mr-3" /><div><p className="font-bold">Error</p><p>{error}</p></div></div></div>)}
                    {assessmentData && (
                      <div className="space-y-6">
                        <h2 className="text-2xl font-bold text-gray-800">Review & Edit Draft</h2>
                        {assessmentData.map((question, qIndex) => (
                          <div key={qIndex} className="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                            <h3 className="text-lg font-semibold text-gray-700 mb-4">Question {qIndex + 1}</h3>
                            <textarea value={question.question_text} onChange={(e) => handleQuestionTextChange(qIndex, e.target.value)} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 mb-4" rows="3" />
                            <h4 className="text-md font-semibold text-gray-600 mb-2">Marking Scheme</h4>
                            <div className="space-y-3 mb-4">
                              {question.marking_scheme.map((point, pIndex) => (
                                <div key={pIndex} className="flex items-center gap-3 bg-gray-50 p-3 rounded-md">
                                  <input type="text" value={point.point} onChange={(e) => handleMarkingPointChange(qIndex, pIndex, e.target.value)} className="flex-grow p-2 border border-gray-200 rounded-md" />
                                  <input type="number" value={point.marks} onChange={(e) => handleMarksChange(qIndex, pIndex, e.target.value)} className="w-20 p-2 border border-gray-200 rounded-md" min="0" />
                                  <button onClick={() => handleRemoveMarkingPoint(qIndex, pIndex)} className="text-red-500 hover:text-red-700 p-2 rounded-full hover:bg-red-100"><Trash2 className="h-5 w-5" /></button>
                                </div>
                              ))}
                              <button onClick={() => handleAddMarkingPoint(qIndex)} className="flex items-center gap-2 text-sm font-medium text-blue-600 hover:text-blue-800 mt-2"><PlusCircle className="h-4 w-4" /> Add Marking Point</button>
                            </div>
                            <h4 className="text-md font-semibold text-gray-600 mb-2">Worked Solution</h4>
                            <textarea value={question.solution} onChange={(e) => handleSolutionChange(qIndex, e.target.value)} className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500" rows="4" />
                          </div>
                        ))}
                        <div className="mt-8 flex justify-end space-x-4">
                            <button className="px-6 py-2 border border-gray-300 text-base font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">Save Draft</button>
                            <button onClick={handleApproveAndAssign} className="px-6 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700">Approve & Assign</button>
                        </div>
                      </div>
                    )}
                </div>
            </div>
        </>
    );
};

export default AssessmentGenerator;
