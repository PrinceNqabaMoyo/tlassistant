import React, { useState } from 'react';
import { useEmsMarking } from './useEmsMarking';

const EmsAssessment = ({ onBack, buildApiUrl }) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [assessmentData, setAssessmentData] = useState(null);
    const [answers, setAnswers] = useState({});
    const [submitted, setSubmitted] = useState(false);
    const [score, setScore] = useState(0);
    const [totalMarks, setTotalMarks] = useState(0);

    const marking = useEmsMarking();

    const generateAssessment = async () => {
        setLoading(true);
        setError(null);
        try {
            const endpoint = buildApiUrl('/api/grade7_ems/assessment');
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    term: 1, // Defaulting to term 1 for now, or we can add a selector
                    difficulty: 'medium'
                }),
            });

            if (!res.ok) throw new Error(`Assessment request failed: HTTP ${res.status}`);
            const data = await res.json();
            if (!data?.success) throw new Error(data?.error || 'Generation failed');

            setAssessmentData(data.paper);
            setAnswers({});
            setSubmitted(false);
        } catch (err) {
            setError(err.message || String(err));
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = () => {
        // Simple mock submission logic until we wire in full marking
        setSubmitted(true);
        setScore(Math.floor(Math.random() * 50)); // Mock score
        setTotalMarks(50);
    };

    return (
        <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
            <div className="bg-white p-6 rounded-xl shadow-xl">
                <div className="flex items-center justify-between mb-6">
                    <div>
                        <h2 className="text-2xl font-bold text-gray-900">Grade 7 EMS • Assessment Mode</h2>
                        <p className="text-sm text-gray-600">Exam condition testing.</p>
                    </div>
                    <button
                        onClick={onBack}
                        className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-medium"
                    >
                        Back
                    </button>
                </div>

                {!assessmentData ? (
                    <div className="text-center py-12">
                        <button
                            onClick={generateAssessment}
                            disabled={loading}
                            className="px-6 py-3 bg-blue-600 text-white rounded-lg font-bold text-lg hover:bg-blue-700 disabled:bg-gray-400"
                        >
                            {loading ? 'Generating Exam...' : 'Start Assessment'}
                        </button>
                        {error && <p className="text-red-500 mt-4">{error}</p>}
                    </div>
                ) : (
                    <div>
                        <div className="mb-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                            <h3 className="font-bold text-yellow-800">Assessment in Progress</h3>
                            <p className="text-sm text-yellow-700">Answer all questions below. No hints are available.</p>
                        </div>

                        {assessmentData.questions.map((q, idx) => (
                            <div key={idx} className="mb-8 p-4 border border-gray-200 rounded-lg">
                                <h4 className="font-bold mb-2">Question {idx + 1}</h4>
                                <p>{q.prompt}</p>
                                {/* Placeholder for rendering specific question inputs based on type */}
                                <textarea 
                                    className="w-full mt-2 p-2 border border-gray-300 rounded"
                                    rows="3"
                                    placeholder="Type your answer here..."
                                    disabled={submitted}
                                />
                            </div>
                        ))}

                        {!submitted ? (
                            <button
                                onClick={handleSubmit}
                                className="px-6 py-3 bg-green-600 text-white rounded-lg font-bold hover:bg-green-700"
                            >
                                Submit Exam
                            </button>
                        ) : (
                            <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg text-center">
                                <h3 className="text-xl font-bold text-blue-900">Final Score: {score} / {totalMarks}</h3>
                            </div>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
};

export default EmsAssessment;
