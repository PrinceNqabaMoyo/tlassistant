import React, { useState, useEffect } from 'react';
import { collection, query, where, getDocs } from 'firebase/firestore';
import { BookCopy, Users, BarChart3, FileText, Plus, Edit, Trash2, Eye, CheckCircle, XCircle, School, Send, ClipboardList, ChevronLeft } from 'lucide-react';

// Teacher Dashboard Component
export const TeacherDashboard = ({ currentUser, db, onSelect }) => {
    const [students, setStudents] = useState([]);
    const [assignments, setAssignments] = useState([]);
    const [performanceData, setPerformanceData] = useState({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadTeacherData = async () => {
            if (!currentUser || !db) return;
            
            try {
                // Load students
                const studentsRef = collection(db, 'users');
                const studentsQuery = query(studentsRef, where('role', '==', 'student'), where('teacherId', '==', currentUser.uid));
                const studentsSnapshot = await getDocs(studentsQuery);
                
                const studentsList = [];
                studentsSnapshot.forEach((doc) => {
                    studentsList.push({ id: doc.id, ...doc.data() });
                });
                setStudents(studentsList);

                // Load assignments
                const assignmentsRef = collection(db, 'assignments');
                const assignmentsQuery = query(assignmentsRef, where('teacherId', '==', currentUser.uid));
                const assignmentsSnapshot = await getDocs(assignmentsQuery);
                
                const assignmentsList = [];
                assignmentsSnapshot.forEach((doc) => {
                    assignmentsList.push({ id: doc.id, ...doc.data() });
                });
                setAssignments(assignmentsList);

                // Load performance data
                const performanceRef = collection(db, 'performance');
                const performanceQuery = query(performanceRef, where('teacherId', '==', currentUser.uid));
                const performanceSnapshot = await getDocs(performanceQuery);
                
                const performance = {};
                performanceSnapshot.forEach((doc) => {
                    const data = doc.data();
                    if (!performance[data.studentId]) {
                        performance[data.studentId] = [];
                    }
                    performance[data.studentId].push(data);
                });
                setPerformanceData(performance);

                setLoading(false);
            } catch (error) {
                console.error('Error loading teacher data:', error);
                setLoading(false);
            }
        };

        loadTeacherData();
    }, [currentUser, db]);

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <h1 className="text-3xl font-bold text-gray-900 mb-8">Teacher Dashboard</h1>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {/* Student Management */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Student Management</h3>
                        <Users className="h-6 w-6 text-blue-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Manage your students and track their progress</p>
                    <button
                        onClick={() => onSelect('studentManagement')}
                        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
                    >
                        Manage Students
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        {students.length} active students
                    </div>
                </div>

                {/* Assignment Management */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Assignments</h3>
                        <FileText className="h-6 w-6 text-green-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Create and manage assignments for your students</p>
                    <button
                        onClick={() => onSelect('assignmentManagement')}
                        className="w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors"
                    >
                        Manage Assignments
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        {assignments.length} active assignments
                    </div>
                </div>

                {/* Performance Analytics */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Analytics</h3>
                        <BarChart3 className="h-6 w-6 text-purple-600" />
                    </div>
                    <p className="text-gray-600 mb-4">View detailed performance analytics and reports</p>
                    <button
                        onClick={() => onSelect('analytics')}
                        className="w-full bg-purple-600 text-white py-2 px-4 rounded-lg hover:bg-purple-700 transition-colors"
                    >
                        View Analytics
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Performance tracking enabled
                    </div>
                </div>

                {/* Question Generation */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Question Bank</h3>
                        <BookCopy className="h-6 w-6 text-orange-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Generate custom questions and practice materials</p>
                    <button
                        onClick={() => onSelect('questionGeneration')}
                        className="w-full bg-orange-600 text-white py-2 px-4 rounded-lg hover:bg-orange-700 transition-colors"
                    >
                        Generate Questions
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        AI-powered generation
                    </div>
                </div>

                {/* Curriculum Management */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Curriculum</h3>
                        <BookCopy className="h-6 w-6 text-indigo-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Manage curriculum content and learning paths</p>
                    <button
                        onClick={() => onSelect('curriculumManagement')}
                        className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors"
                    >
                        Manage Curriculum
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Content management tools
                    </div>
                </div>

                {/* Reports */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Reports</h3>
                        <FileText className="h-6 w-6 text-red-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Generate comprehensive reports and insights</p>
                    <button
                        onClick={() => onSelect('reports')}
                        className="w-full bg-red-600 text-white py-2 px-4 rounded-lg hover:bg-red-700 transition-colors"
                    >
                        Generate Reports
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Export and sharing tools
                    </div>
                </div>

                {/* Class Management */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Classes</h3>
                        <School className="h-6 w-6 text-teal-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Create classes, set subjects/grades, and enroll students</p>
                    <button
                        onClick={() => onSelect('classManagement')}
                        className="w-full bg-teal-600 text-white py-2 px-4 rounded-lg hover:bg-teal-700 transition-colors"
                    >
                        Manage Classes
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Up to 3 subjects &amp; 3 grades
                    </div>
                </div>

                {/* Homework */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Homework</h3>
                        <Send className="h-6 w-6 text-sky-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Create and send homework to enrolled classes</p>
                    <button
                        onClick={() => onSelect('homework')}
                        className="w-full bg-sky-600 text-white py-2 px-4 rounded-lg hover:bg-sky-700 transition-colors"
                    >
                        Create Homework
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Linked to classes
                    </div>
                </div>

                {/* Assessments */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Assessments</h3>
                        <ClipboardList className="h-6 w-6 text-amber-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Set timed assessments with mark visibility controls</p>
                    <button
                        onClick={() => onSelect('assessments')}
                        className="w-full bg-amber-600 text-white py-2 px-4 rounded-lg hover:bg-amber-700 transition-colors"
                    >
                        Create Assessment
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Timed &amp; scheduled
                    </div>
                </div>
            </div>
        </div>
    );
};

// Student Management Component
export const StudentManagement = ({ currentUser, db, onBack }) => {
    const [students, setStudents] = useState([]);
    const [selectedStudent, setSelectedStudent] = useState(null);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        const loadStudents = async () => {
            if (!currentUser || !db) return;
            
            try {
                const studentsRef = collection(db, 'users');
                const studentsQuery = query(studentsRef, where('role', '==', 'student'), where('teacherId', '==', currentUser.uid));
                const studentsSnapshot = await getDocs(studentsQuery);
                
                const studentsList = [];
                studentsSnapshot.forEach((doc) => {
                    studentsList.push({ id: doc.id, ...doc.data() });
                });
                setStudents(studentsList);
                setLoading(false);
            } catch (error) {
                console.error('Error loading students:', error);
                setLoading(false);
            }
        };

        loadStudents();
    }, [currentUser, db]);

    const filteredStudents = students.filter(student =>
        student.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        student.email?.toLowerCase().includes(searchTerm.toLowerCase())
    );

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <div className="flex items-center justify-between mb-6">
                <button
                    onClick={onBack}
                    className="flex items-center text-blue-600 hover:text-blue-800 transition-colors"
                >
                    <ChevronLeft className="h-5 w-5 mr-2" />
                    Back to Dashboard
                </button>
                <h1 className="text-3xl font-bold text-gray-900">Student Management</h1>
            </div>

            {/* Search Bar */}
            <div className="mb-6">
                <input
                    type="text"
                    placeholder="Search students by name or email..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
            </div>

            {/* Students List */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {filteredStudents.map(student => (
                    <div key={student.id} className="bg-white rounded-lg shadow-md p-6">
                        <div className="flex items-center justify-between mb-4">
                            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                                <span className="text-blue-600 font-semibold text-lg">
                                    {student.name?.charAt(0) || 'S'}
                </span>
                            </div>
                            <div className="flex space-x-2">
                                <button
                                    onClick={() => setSelectedStudent(student)}
                                    className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                                    title="View Details"
                                >
                                    <Eye className="h-4 w-4" />
                                </button>
                                <button
                                    onClick={() => {/* Edit student */}}
                                    className="p-2 text-green-600 hover:bg-green-50 rounded-lg transition-colors"
                                    title="Edit Student"
                                >
                                    <Edit className="h-4 w-4" />
                                </button>
                            </div>
                        </div>
                        
                        <h3 className="text-lg font-semibold text-gray-800 mb-2">{student.name || 'Unnamed Student'}</h3>
                        <p className="text-gray-600 text-sm mb-3">{student.email}</p>
                        
                        <div className="space-y-2">
                            <div className="flex justify-between text-sm">
                                <span className="text-gray-500">Curriculum:</span>
                                <span className="font-medium">{student.curriculum || 'Not set'}</span>
                            </div>
                            <div className="flex justify-between text-sm">
                                <span className="text-gray-500">Grade:</span>
                                <span className="font-medium">{student.grade || 'Not set'}</span>
                            </div>
                            <div className="flex justify-between text-sm">
                                <span className="text-gray-500">Status:</span>
                                <span className={`px-2 py-1 rounded-full text-xs ${
                                    student.status === 'active' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                                }`}>
                                    {student.status || 'inactive'}
                                </span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {filteredStudents.length === 0 && (
                <div className="text-center py-12">
                    <Users className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-gray-900 mb-2">No students found</h3>
                    <p className="text-gray-500">
                        {searchTerm ? 'Try adjusting your search terms.' : 'Start by adding students to your class.'}
                    </p>
                </div>
            )}
        </div>
    );
};

// Question Generation Component
export const QuestionGeneration = ({ currentUser, db, onBack }) => {
    const [topics, setTopics] = useState([]);
    const [selectedTopic, setSelectedTopic] = useState('');
    const [questionCount, setQuestionCount] = useState(5);
    const [difficulty, setDifficulty] = useState('medium');
    const [generatedQuestions, setGeneratedQuestions] = useState([]);
    const [loading, setLoading] = useState(false);

    const difficulties = [
        { value: 'easy', label: 'Easy', color: 'bg-green-100 text-green-800' },
        { value: 'medium', label: 'Medium', color: 'bg-yellow-100 text-yellow-800' },
        { value: 'hard', label: 'Hard', color: 'bg-red-100 text-red-800' }
    ];

    const handleGenerateQuestions = async () => {
        if (!selectedTopic || questionCount < 1) return;
        
        setLoading(true);
        try {
            // Simulate AI question generation
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            const questions = Array.from({ length: questionCount }, (_, i) => ({
                id: Date.now() + i,
                question: `Sample question ${i + 1} for ${selectedTopic}`,
                answer: `Sample answer ${i + 1}`,
                difficulty: difficulty,
                topic: selectedTopic,
                type: 'multiple_choice'
            }));
            
            setGeneratedQuestions(questions);
        } catch (error) {
            console.error('Error generating questions:', error);
            alert(error.message || "Connection failed. Please check your internet connection and try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <div className="flex items-center justify-between mb-6">
                <button
                    onClick={onBack}
                    className="flex items-center text-blue-600 hover:text-blue-800 transition-colors"
                >
                    <ChevronLeft className="h-5 w-5 mr-2" />
                    Back to Dashboard
                </button>
                <h1 className="text-3xl font-bold text-gray-900">Question Generation</h1>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                {/* Generation Form */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">Generate Questions</h2>
                    
                    <div className="space-y-4">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Topic</label>
                            <select
                                value={selectedTopic}
                                onChange={(e) => setSelectedTopic(e.target.value)}
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                            >
                                <option value="">Select a topic</option>
                                <option value="cash_receipts">Cash Receipts</option>
                                <option value="cash_payments">Cash Payments</option>
                                <option value="general_ledger">General Ledger</option>
                                <option value="trial_balance">Trial Balance</option>
                            </select>
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Number of Questions</label>
                            <input
                                type="number"
                                min="1"
                                max="20"
                                value={questionCount}
                                onChange={(e) => setQuestionCount(parseInt(e.target.value))}
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Difficulty Level</label>
                            <div className="flex space-x-3">
                                {difficulties.map((diff) => (
                                    <button
                                        key={diff.value}
                                        onClick={() => setDifficulty(diff.value)}
                                        className={`px-4 py-2 rounded-lg transition-colors ${
                                            difficulty === diff.value 
                                                ? diff.color 
                                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                                        }`}
                                    >
                                        {diff.label}
                                    </button>
                                ))}
                            </div>
                        </div>

                        <button
                            onClick={handleGenerateQuestions}
                            disabled={!selectedTopic || loading}
                            className="w-full bg-blue-600 text-white py-3 px-4 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
                        >
                            {loading ? (
                                <div className="flex items-center justify-center">
                                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                                    Generating...
                                </div>
                            ) : (
                                'Generate Questions'
                            )}
                        </button>
                    </div>
                </div>

                {/* Generated Questions */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">Generated Questions</h2>
                    
                    {generatedQuestions.length === 0 ? (
                        <div className="text-center py-12">
                            <FileText className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                            <p className="text-gray-500">No questions generated yet. Use the form to create questions.</p>
                        </div>
                    ) : (
                        <div className="space-y-4">
                            {generatedQuestions.map((question, index) => (
                                <div key={question.id} className="border border-gray-200 rounded-lg p-4">
                                    <div className="flex items-center justify-between mb-2">
                                        <span className="text-sm font-medium text-gray-600">Question {index + 1}</span>
                                        <span className={`px-2 py-1 rounded-full text-xs ${
                                            difficulties.find(d => d.value === question.difficulty)?.color || 'bg-gray-100 text-gray-800'
                                        }`}>
                                            {question.difficulty}
                                        </span>
                                    </div>
                                    <p className="text-gray-800 mb-2">{question.question}</p>
                                    <p className="text-sm text-gray-600">Answer: {question.answer}</p>
                                </div>
                            ))}
                            
                            <div className="flex space-x-3 pt-4">
                                <button className="flex-1 bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors">
                                    Save Questions
                                </button>
                                <button className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors">
                                    Export
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};
