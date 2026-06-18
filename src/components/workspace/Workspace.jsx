import React, { useState, useEffect } from 'react';
import { FileText, X, Loader2, ChevronLeft, ChevronRight } from 'lucide-react';

// Import source document components
import SourceDocumentRepository from '../sourceDocuments/SourceDocumentRepository';
import DepositSlipInput from '../sourceDocuments/DepositSlipInput';
import CashReceiptsJournalInput from '../sourceDocuments/CashReceiptsJournalInput';
import CashPaymentsJournalInput from '../sourceDocuments/CashPaymentsJournalInput';
import ChequeInput from '../sourceDocuments/ChequeInput';
import ReceiptInput from '../sourceDocuments/ReceiptInput';
import CashInvoiceInput from '../sourceDocuments/CashInvoiceInput';
import IncomeStatementInput from '../sourceDocuments/IncomeStatementInput';
import TradingIncomeStatementInput from '../sourceDocuments/TradingIncomeStatementInput';
import DebtorsJournalInput from '../sourceDocuments/DebtorsJournalInput';
import CreditorsJournalInput from '../sourceDocuments/CreditorsJournalInput';
import GeneralLedgerInput from '../sourceDocuments/GeneralLedgerInput';
import DebtorsLedgerInput from '../sourceDocuments/DebtorsLedgerInput';

import { buildApiUrl } from '../../utils/apiBaseUrl';
import { renderFromRegistry } from './workspaceRegistry';
import FeatureGatePanel from '../ui/FeatureGatePanel';
import { FREEFORM_PRO_MESSAGE } from '../../app/constants/access';

const Workspace = ({
    topic,
    practiceQuestions, workspaceMode, setWorkspaceMode,
    freeformWorkAreaRef, currentUser, getAgentResponse,
    handleAnswerInput, handleSubmit,
    setView, activeAssignment,
    handleAssignmentSubmit,
    handleExplainMistake,
    loading, setLoading,
    selectedSubject,
    selectedGrade,
    addQuestionToChat,
    updateAnswerInChat, handleSendFreeformQuery,
    freeformAnswer,
    setFreeformAnswer,
    currentProblemThreadId,
    setSelectedFreeformTopic,
}) => {
    // State for managing available topics and the currently selected topic in the dropdown
    const [availableTopics, setAvailableTopics] = useState([]);
    const [selectedTopic, setSelectedTopic] = useState('');

    // State for source document repository functionality
    const [showSourceDocumentRepository, setShowSourceDocumentRepository] = useState(false);
    const [selectedSourceDocument, setSelectedSourceDocument] = useState(null);
    const [sourceDocumentData, setSourceDocumentData] = useState(null);
    const [isSourceDocumentSubmitted, setIsSourceDocumentSubmitted] = useState(false);

    // State for visual tools pane visibility
    const [isVisualToolsPaneVisible, setIsVisualToolsPaneVisible] = useState(true);
    const [freeformLandingDismissed, setFreeformLandingDismissed] = useState(false);

    const onBack = () => {
        if (typeof setView === 'function') {
            setView('curriculum_helper');
        }
    };

    const availableRepositories = [];

    const normalizeWholeNumberAnswer = (value) => {
        if (value === null || value === undefined) return '';
        return String(value)
            .trim()
            .replace(/\s+/g, '')
            .replace(/,/g, '');
    };

    const normalizeTextAnswer = (value) => {
        if (value === null || value === undefined) return '';
        return String(value)
            .trim()
            .replace(/\s+/g, ' ');
    };

    const formatExponentCarets = (value) => {
        if (value === null || value === undefined) return '';
        const s = String(value);
        const map = {
            '0': '⁰',
            '1': '¹',
            '2': '²',
            '3': '³',
            '4': '⁴',
            '5': '⁵',
            '6': '⁶',
            '7': '⁷',
            '8': '⁸',
            '9': '⁹',
            '+': '⁺',
            '-': '⁻'
        };

        return s.replace(/\^([+-]?\d+)/g, (_, exp) => {
            const out = String(exp).split('').map((ch) => map[ch] || ch).join('');
            return out;
        });
    };

    const handleSendWithTopic = () => {
        const combinedQuery = `Topic: ${selectedTopic}\nProblem and Solution:\n${freeformAnswer}`;
        handleSendFreeformQuery(combinedQuery);
    };

    const handleTopicSelect = (nextTopic) => {
        setSelectedTopic(nextTopic);
        setSelectedFreeformTopic(nextTopic || null);
    };

    const handleSelectSourceDocument = (doc) => {
        if (doc) {
            setSelectedSourceDocument(doc);
            setSourceDocumentData(doc.template);
            setIsSourceDocumentSubmitted(false);

            if (freeformWorkAreaRef?.current) {
                const currentContent = freeformWorkAreaRef.current.innerText;
                const sourceDocDescription = `[Source Document: ${doc.name}]\n${doc.description}\n\n`;

                freeformWorkAreaRef.current.innerText = sourceDocDescription + currentContent;
                setFreeformAnswer(sourceDocDescription + currentContent);
            }
        }
        setShowSourceDocumentRepository(false);
    };

    const handleSourceDocumentDataChange = (newData) => {
        setSourceDocumentData(newData);
    };

    const handleSourceDocumentSubmit = async () => {
        if (!sourceDocumentData || !selectedSourceDocument) return;
        setLoading(true);

        try {
            const validationResponse = await fetch(buildApiUrl('/api/source-documents/validate'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    document_data: sourceDocumentData,
                    document_type: selectedSourceDocument.type,
                }),
            });

            if (!validationResponse.ok) {
                throw new Error(`Source document validation failed with status ${validationResponse.status}`);
            }

            const validationResult = await validationResponse.json();
            let feedbackText = `Source Document Validation:\n${validationResult.validation_result}`;

            if (typeof getAgentResponse === 'function') {
                const aiResponse = await getAgentResponse(
                    `Please review this ${selectedSourceDocument.name} submission and provide detailed feedback:\n\n${validationResult.validation_result}`,
                    []
                );
                feedbackText = `${feedbackText}\n\nAI Feedback:\n${aiResponse}`;
            }

            const questionId = typeof addQuestionToChat === 'function'
                ? addQuestionToChat(`Submitted ${selectedSourceDocument.name} for review`)
                : null;

            if (questionId && typeof updateAnswerInChat === 'function') {
                updateAnswerInChat(questionId, feedbackText, true);
            }

            setIsSourceDocumentSubmitted(true);
        } catch (error) {
            console.error('Error submitting source document:', error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        const topicsForGrade = (selectedSubject?.topicsByGrade?.[selectedGrade]?.topics || [])
            .map((entry) => (typeof entry === 'string' ? entry : entry?.name))
            .filter(Boolean);

        setAvailableTopics(topicsForGrade);

        const activeTopicName = typeof topic === 'string' ? topic : topic?.name;
        const nextTopic = activeTopicName || (topicsForGrade.includes(selectedTopic) ? selectedTopic : topicsForGrade[0] || '');

        setSelectedTopic(nextTopic);
        setSelectedFreeformTopic(nextTopic || null);
    }, [selectedSubject, selectedGrade, topic, selectedTopic, setSelectedFreeformTopic]);

    useEffect(() => {
        if (workspaceMode !== 'freeform') return;
        if (currentProblemThreadId || freeformAnswer.trim() || selectedSourceDocument) {
            setFreeformLandingDismissed(true);
            return;
        }
        setFreeformLandingDismissed(false);
    }, [workspaceMode, selectedSubject, selectedGrade, currentProblemThreadId, freeformAnswer, selectedSourceDocument]);

    useEffect(() => {
        if (freeformWorkAreaRef?.current && freeformAnswer === '') {
            freeformWorkAreaRef.current.innerText = '';
        }
    }, [freeformAnswer, freeformWorkAreaRef]);

    const showFreeformLanding = false;

    const isPro = currentUser?.tier === 'pro' || currentUser?.isOwner || currentUser?.isSuperAdmin;

    return (
        <div className="bg-gray-50 min-h-screen">

            {workspaceMode === 'freeform' && !isPro && (
                <div className="p-4 sm:p-6 lg:p-8">
                    <FeatureGatePanel
                        title="AI Tutor & Workspace"
                        description={FREEFORM_PRO_MESSAGE}
                        badge="Pro package only"
                    />
                </div>
            )}

            {workspaceMode === 'freeform' && isPro && (
                <div className="flex h-screen items-center justify-center bg-gray-50 p-6">
                    <div className="bg-white p-8 rounded-xl shadow-lg text-center max-w-md w-full border border-gray-100">
                        <div className="mb-6 flex justify-center">
                            <div className="bg-blue-50 p-4 rounded-full text-blue-500">
                                <FileText size={48} />
                            </div>
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 mb-4">No Workspace Selected</h2>
                        <p className="text-gray-600 mb-8 leading-relaxed">
                            Please select a topic and mode from the Curriculum section to begin your learning session.
                        </p>
                        <button
                            onClick={() => {
                                if (typeof setView === 'function') {
                                    setView('curriculum_helper');
                                }
                            }}
                            className="w-full bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-sm hover:shadow-md"
                        >
                            Go to Curriculum
                        </button>
                    </div>
                </div>
            )}

            {/* --- Practice Mode (Visible when workspaceMode is 'practice') --- */}
            {workspaceMode === 'practice' && (
                <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
                    <div className="bg-white p-6 rounded-xl shadow-xl">
                        <div className="mb-6">
                            <h2 className="text-2xl font-bold text-gray-800">
                                {activeAssignment ? 'Class Assignment' : 'Personal Study Workspace'}
                            </h2>
                            <p className="text-gray-600">
                                Subject: <span className="font-semibold text-gray-700">{selectedSubject?.name || '...'}</span> |
                                Grade: <span className="font-semibold text-gray-700">{selectedGrade || '...'}</span>
                            </p>
                            {activeAssignment && <p className="text-gray-600">Topic: <span className="font-semibold text-gray-700">{activeAssignment.topic}</span></p>}
                        </div>

                        <div className="space-y-6">
                            {practiceQuestions.map((question, index) => (
                                <div key={question.id} className="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                                    <div className="flex justify-between items-start mb-4">
                                        <h3 className="text-lg font-semibold text-gray-800">Question {index + 1}</h3>
                                        <span className={`px-3 py-1 text-sm rounded-full ${question.isSubmitted ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
                                            }`}>
                                            {question.isSubmitted ? 'Submitted' : 'Not Submitted'}
                                        </span>
                                    </div>

                                    <p className="text-gray-700 mb-4">{question.text}</p>

                                    {/* Question Input Area */}
                                    {!question.isSubmitted && (
                                        <div className="mb-4">
                                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                                Your Answer:
                                            </label>

                                            {/* Small, unobtrusive repository buttons - only show if available */}
                                            {availableRepositories.length > 0 && (
                                                <div className="mb-3 p-2 bg-gray-50 rounded border border-gray-200">
                                                    <p className="text-xs text-gray-600 mb-1 font-medium">Available Tools:</p>
                                                    <div className="flex flex-wrap gap-1">
                                                        {availableRepositories.map((repo) => {
                                                            const Icon = repo.icon;
                                                            return (
                                                                <button
                                                                    key={repo.key}
                                                                    onClick={repo.onClick}
                                                                    className="flex items-center space-x-1 bg-white text-gray-700 px-2 py-1 rounded border border-gray-300 hover:bg-gray-100 hover:border-gray-400 transition-colors duration-200 text-xs"
                                                                    title={`Open ${repo.name}`}
                                                                >
                                                                    <Icon className="h-3 w-3" />
                                                                    <span>{repo.name}</span>
                                                                </button>
                                                            );
                                                        })}
                                                    </div>
                                                </div>
                                            )}

                                            <textarea
                                                value={question.answer || ''}
                                                onChange={(e) => handleAnswerInput(question.id, e.target.value)}
                                                className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                rows={4}
                                                placeholder="Type your answer here..."
                                            />
                                        </div>
                                    )}

                                    {/* Submit Button */}
                                    {!question.isSubmitted && (
                                        <button
                                            onClick={() => handleSubmit(question.id, question.text, question.expected_answer_type, question.answer, question.solution)}
                                            className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700 transition-colors duration-200"
                                        >
                                            Submit Answer
                                        </button>
                                    )}

                                    {/* Feedback Display */}
                                    {question.feedback && (
                                        <div className="mt-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                                            <h4 className="font-semibold text-blue-800 mb-2">Feedback:</h4>
                                            <div className="text-blue-700" dangerouslySetInnerHTML={{ __html: question.feedback.processedContent || question.feedback.content }} />
                                            {question.feedback.is_correct === false && (
                                                <button
                                                    type="button"
                                                    onClick={() => handleExplainMistake && handleExplainMistake(question)}
                                                    className="mt-3 text-sm bg-amber-100 text-amber-800 px-3 py-1.5 rounded-md hover:bg-amber-200 transition-colors font-medium"
                                                >
                                                    Explain my mistake
                                                </button>
                                            )}
                                        </div>
                                    )}
                                </div>
                            ))}

                            {/* Assignment Submit Button */}
                            {activeAssignment && practiceQuestions.every(q => q.isSubmitted) && (
                                <div className="text-center">
                                    <button
                                        onClick={handleAssignmentSubmit}
                                        className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition-colors duration-200 text-lg font-medium"
                                    >
                                        Submit Assignment
                                    </button>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            )}


            {/* Source Document Repository Modal */}
            <SourceDocumentRepository
                isVisible={showSourceDocumentRepository}
                onSelectJournal={handleSelectSourceDocument}
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
            />

            {renderFromRegistry({
                workspaceMode,
                ctx: {
                    onBack,
                    buildApiUrl,
                    normalizeWholeNumberAnswer,
                    normalizeTextAnswer,
                    formatExponentCarets,
                    currentUser,
                    subscriptionTier: currentUser?.tier || 'standard',
                    setWorkspaceMode,
                    selectedSubject,
                    selectedGrade,
                    topic,
                }
            })}

        </div>
    );
};

export default Workspace;
