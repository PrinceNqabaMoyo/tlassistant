import React, { useState, useEffect } from 'react';
import { query, collection, where, getDocs } from 'firebase/firestore';
import { ChevronLeft, Loader2 } from 'lucide-react';

const SubmissionsDashboard = ({ db, currentUser, setView }) => {
    const [assessments, setAssessments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAssessments = async () => {
            if (!db || !currentUser) return;
            try {
                const q = query(collection(db, "assessments"), where("teacherId", "==", currentUser.uid));
                const querySnapshot = await getDocs(q);
                const fetchedAssessments = querySnapshot.docs.map(doc => ({
                    id: doc.id,
                    ...doc.data()
                }));
                setAssessments(fetchedAssessments);
            } catch (err) {
                console.error("Error fetching assessments: ", err);
                setError("Could not load your assessments. Please try again later.");
            } finally {
                setLoading(false);
            }
        };

        fetchAssessments();
    }, [db, currentUser]);

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <button onClick={() => setView('dashboard')} className="flex items-center text-gray-600 hover:text-blue-600 font-medium mb-6 group">
                <ChevronLeft className="h-5 w-5 mr-2 transition-transform group-hover:-translate-x-1" />
                Back to Dashboard
            </button>
            <h1 className="text-3xl font-bold text-gray-800 mb-2">View Submissions</h1>
            <p className="text-gray-600 mb-8">Select an assignment to view student submissions.</p>
            
            {loading && <div className="flex justify-center items-center p-8"><Loader2 className="h-8 w-8 animate-spin text-blue-600" /></div>}
            {error && <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded-md" role="alert"><p>{error}</p></div>}
            
            {!loading && !error && (
                <div className="space-y-4">
                    {assessments.length > 0 ? (
                        assessments.map(assessment => (
                            <button key={assessment.id} onClick={() => alert(`Navigating to submissions for ${assessment.topic}`)} className="w-full text-left p-4 bg-white rounded-lg shadow-md hover:shadow-lg hover:border-blue-500 border-2 border-transparent transition-all">
                                <h3 className="font-bold text-lg text-gray-800">{assessment.topic}</h3>
                                <p className="text-sm text-gray-600">{assessment.subject} - Grade {assessment.grade}</p>
                                <p className="text-xs text-gray-400 mt-2">Created on: {assessment.createdAt?.toDate().toLocaleDateString()}</p>
                            </button>
                        ))
                    ) : (
                        <p className="text-center text-gray-500 py-8">You have not created any assignments yet.</p>
                    )}
                </div>
            )}
        </div>
    );
};

export default SubmissionsDashboard;
