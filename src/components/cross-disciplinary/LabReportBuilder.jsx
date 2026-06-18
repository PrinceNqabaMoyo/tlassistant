import React, { useState, useEffect } from 'react';

const LabReportBuilder = ({ initialData, onChange, isSubmitted }) => {
    const [reportTitle, setReportTitle] = useState(initialData.reportTitle || 'Lab Report');
    const [studentName, setStudentName] = useState(initialData.studentName || 'Student Name');
    const [date, setDate] = useState(initialData.date || new Date().toISOString().split('T')[0]);
    const [abstract, setAbstract] = useState(initialData.abstract || '');
    const [objective, setObjective] = useState(initialData.objective || '');
    const [methods, setMethods] = useState(initialData.methods || '');
    const [results, setResults] = useState(initialData.results || '');
    const [conclusion, setConclusion] = useState(initialData.conclusion || '');

    useEffect(() => {
        const formattedData = {
            type: "lab_report_builder",
            reportTitle: reportTitle,
            studentName: studentName,
            date: date,
            abstract: abstract,
            objective: objective,
            methods: methods,
            results: results,
            conclusion: conclusion,
            results: generateReport()
        };
        onChange(formattedData);
    }, [reportTitle, studentName, date, abstract, objective, methods, results, conclusion, onChange]);

    const generateReport = () => {
        return {
            fullReport: `${reportTitle}\n\nStudent: ${studentName}\nDate: ${date}\n\nAbstract\n${abstract}\n\nObjective\n${objective}\n\nMethods\n${methods}\n\nResults\n${results}\n\nConclusion\n${conclusion}`,
            wordCount: abstract.length + objective.length + methods.length + results.length + conclusion.length
        };
    };

    const reportResults = generateReport();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <h3 className="text-lg font-semibold text-gray-800 mb-6">Lab Report Builder</h3>

            {/* Header */}
            <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                <h4 className="text-md font-medium text-blue-800 mb-3">Report Header:</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Title:</label>
                        <input 
                            type="text" 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500" 
                            value={reportTitle} 
                            onChange={(e) => !isSubmitted && setReportTitle(e.target.value)} 
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Student Name:</label>
                        <input 
                            type="text" 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500" 
                            value={studentName} 
                            onChange={(e) => !isSubmitted && setStudentName(e.target.value)} 
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Date:</label>
                        <input 
                            type="date" 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500" 
                            value={date} 
                            onChange={(e) => !isSubmitted && setDate(e.target.value)} 
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
            </div>

            {/* Abstract */}
            <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                <h4 className="text-md font-medium text-green-800 mb-3">Abstract:</h4>
                <textarea 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500" 
                    rows="4"
                    value={abstract} 
                    onChange={(e) => !isSubmitted && setAbstract(e.target.value)} 
                    disabled={isSubmitted}
                    placeholder="Write a concise summary of your experiment"
                />
            </div>

            {/* Objective */}
            <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                <h4 className="text-md font-medium text-yellow-800 mb-3">Objective:</h4>
                <textarea 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500" 
                    rows="3"
                    value={objective} 
                    onChange={(e) => !isSubmitted && setObjective(e.target.value)} 
                    disabled={isSubmitted}
                    placeholder="State the purpose of your experiment"
                />
            </div>

            {/* Methods */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Methods:</h4>
                <textarea 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500" 
                    rows="4"
                    value={methods} 
                    onChange={(e) => !isSubmitted && setMethods(e.target.value)} 
                    disabled={isSubmitted}
                    placeholder="Describe your experimental procedure"
                />
            </div>

            {/* Results */}
            <div className="mb-6 p-4 bg-indigo-50 rounded-lg border border-indigo-200">
                <h4 className="text-md font-medium text-indigo-800 mb-3">Results:</h4>
                <textarea 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500" 
                    rows="4"
                    value={results} 
                    onChange={(e) => !isSubmitted && setResults(e.target.value)} 
                    disabled={isSubmitted}
                    placeholder="Present your experimental results and data"
                />
            </div>

            {/* Conclusion */}
            <div className="mb-6 p-4 bg-pink-50 rounded-lg border border-pink-200">
                <h4 className="text-md font-medium text-pink-800 mb-3">Conclusion:</h4>
                <textarea 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-pink-500 focus:border-pink-500" 
                    rows="4"
                    value={conclusion} 
                    onChange={(e) => !isSubmitted && setConclusion(e.target.value)} 
                    disabled={isSubmitted}
                    placeholder="Summarize your findings and conclusions"
                />
            </div>

            {/* Report Summary */}
            <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                <h4 className="text-md font-medium text-gray-800 mb-3">Report Summary:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Total Words</div>
                        <div className="text-xl text-gray-700">{Math.round(reportResults.wordCount / 5)}</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Sections</div>
                        <div className="text-xl text-gray-700">6/6</div>
                    </div>
                </div>
            </div>

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Abstract should be concise and summarize key findings</li>
                    <li>• Objective should clearly state the experiment's purpose</li>
                    <li>• Methods should be detailed enough for replication</li>
                    <li>• Results should present data objectively</li>
                    <li>• Conclusion should summarize findings and significance</li>
                </ul>
            </div>
        </div>
    );
};

export default LabReportBuilder;
