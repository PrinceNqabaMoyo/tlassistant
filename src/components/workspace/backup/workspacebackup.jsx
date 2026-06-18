import React, { useState, useEffect, useRef } from 'react';
import { FunctionSquare, FileText, BrainCircuit, Target, BookOpen, X, Loader2, Compass, ChevronLeft, ChevronRight } from 'lucide-react';

// Import repositories
import MathComponentsRepository from '../math/MathComponentsRepository';
import ChemistryComponentsRepository from '../chemistry/ChemistryComponentsRepository';
import PhysicsComponentsRepository from '../physics/PhysicsComponentsRepository';
import CrossDisciplinaryComponentsRepository from '../cross-disciplinary/CrossDisciplinaryComponentsRepository';
import ThumbnailRenderer from '../math/ThumbnailRenderer';
import ComponentOverlay from '../shared/ComponentOverlay';

// Import math components
import AlgebraicExpressionBuilder from '../math/AlgebraicExpressionBuilder';
import ComplexNumbersInput from '../math/ComplexNumbersInput';
import GeometryStudio from '../math/GeometryStudio';

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

const Workspace = ({
    db,
    subject,
    grade,
    topic,
    practiceQuestions, setPracticeQuestions,
    setIsCurriculumPageVisible, workspaceMode, setWorkspaceMode,
    freeformWorkAreaRef, setActiveEditableRef, currentUser,
    isKeypadVisible, setIsKeypadVisible, getAgentResponse,
    handleAttempt, handleAnswerInput, handleSubmit,
    setNavigationStack, setView, activeAssignment,
    handleAssignmentSubmit, handleToggleMathStructure,
    loading, setLoading,
    selectedSubject,
    selectedGrade,
    chatHistory, addQuestionToChat,
    updateAnswerInChat, handleSendFreeformQuery,
    freeformAnswer,
    setFreeformAnswer,
    applyAllTextFormatting,
    currentProblemThreadId,
    handleStrugglingProblem, setSelectedFreeformTopic,
}) => {
    // Reference to the bottom of the chat area for auto-scrolling
    const chatEndRef = useRef(null);

    // State for managing available topics and the currently selected topic in the dropdown
    const [availableTopics, setAvailableTopics] = useState([]);
    const [selectedTopic, setSelectedTopic] = useState('');
    
    // State for source document repository functionality
    const [showSourceDocumentRepository, setShowSourceDocumentRepository] = useState(false);
    const [showMathComponentsRepository, setShowMathComponentsRepository] = useState(false);
    const [showChemistryComponentsRepository, setShowChemistryComponentsRepository] = useState(false);
    const [showPhysicsComponentsRepository, setShowPhysicsComponentsRepository] = useState(false);
    const [showCrossDisciplinaryComponentsRepository, setShowCrossDisciplinaryComponentsRepository] = useState(false);
    const [selectedSourceDocument, setSelectedSourceDocument] = useState(null);
    const [sourceDocumentData, setSourceDocumentData] = useState(null);
    const [isSourceDocumentSubmitted, setIsSourceDocumentSubmitted] = useState(false);
    
    // State for ordered answer sequence
    const [answerSequence, setAnswerSequence] = useState([]); // Each item: { type: 'text'|'journal', value, journalType? }

    // State for visual tools pane visibility
    const [isVisualToolsPaneVisible, setIsVisualToolsPaneVisible] = useState(true);
    
    // State for visual tool data that can be sent to workspace
    const [visualToolData, setVisualToolData] = useState(null);

    // State for expanded repositories
    const [expandedRepositories, setExpandedRepositories] = useState([]);

    // State for component overlay
    const [selectedComponent, setSelectedComponent] = useState(null);
    const [isComponentOverlayVisible, setIsComponentOverlayVisible] = useState(false);
    const [isComponentFullscreen, setIsComponentFullscreen] = useState(false);



    // Function to determine which repositories should be available based on subject and grade
    const getAvailableRepositories = () => {
        if (!selectedSubject || !selectedGrade) return [];
        
        const subjectName = selectedSubject.name?.toLowerCase() || '';
        const gradeNum = parseInt(selectedGrade);
        
        console.log('🔍 getAvailableRepositories called with:', { subjectName, gradeNum, selectedSubject: selectedSubject?.name });
        
        const repositories = [];
        
        // Math components for math subjects
        if (['mathematics', 'mathematical literacy', 'technical mathematics'].includes(subjectName)) {
            repositories.push({
                key: 'math',
                name: 'Mathematical Visual Aids',
                color: 'bg-green-500 hover:bg-green-600',
                icon: FunctionSquare,
                onClick: () => setShowMathComponentsRepository(true)
            });
        }
        
        // Chemistry and Physics components for Physical Science (Gr 10-12)
        if (subjectName === 'physical science' && gradeNum >= 10 && gradeNum <= 12) {
            repositories.push(
                {
                    key: 'chemistry',
                    name: 'Chemistry Visual Aids',
                    color: 'bg-purple-500 hover:bg-purple-600',
                    icon: FileText,
                    onClick: () => setShowChemistryComponentsRepository(true)
                },
                {
                    key: 'physics',
                    name: 'Physics Visual Aids',
                    color: 'bg-orange-500 hover:bg-orange-600',
                    icon: Target,
                    onClick: () => setShowPhysicsComponentsRepository(true)
                }
            );
        }
        
        // Source documents for business subjects
        if (['accounting', 'economic and management sciences', 'business studies'].includes(subjectName)) {
            repositories.push({
                key: 'source-documents',
                name: 'Source Documents',
                color: 'bg-blue-500 hover:bg-blue-600',
                icon: FileText,
                onClick: () => setShowSourceDocumentRepository(true)
            });
        }
        
        // Cross-disciplinary components available for all subjects
        repositories.push({
            key: 'cross-disciplinary',
            name: 'Cross-Disciplinary Tools',
            color: 'bg-indigo-500 hover:bg-indigo-600',
            icon: BrainCircuit,
            onClick: () => setShowCrossDisciplinaryComponentsRepository(true)
        });
        
        console.log('🔍 Available repositories:', repositories);
        return repositories;
    };

    // Function to handle visual tool data being sent to workspace
    const handleVisualToolDataToWorkspace = (data) => {
        setVisualToolData(data);
        
        // Open the appropriate tool overlay based on the data
        if (data.category === 'Number Systems' || data.category === 'Algebra' || data.category === 'Geometry' || data.category === 'Statistics' || data.category === 'Probability' || data.category === 'Algebra & Geometry') {
            setShowMathComponentsRepository(true);
        } else if (data.category === 'Fundamentals' || data.category === 'Molecular' || data.category === 'Reactions') {
            setShowChemistryComponentsRepository(true);
        } else if (data.category === 'Mechanics' || data.category === 'Waves' || data.category === 'Electricity') {
            setShowPhysicsComponentsRepository(true);
        } else if (data.category === 'Organization') {
            setShowCrossDisciplinaryComponentsRepository(true);
        }
        
        // Add the visual tool data to the freeform work area
        if (freeformWorkAreaRef.current) {
            const currentContent = freeformWorkAreaRef.current.innerText;
            const visualToolDescription = `[Visual Tool: ${data.name || 'Mathematical Component'}]\n${data.description || ''}\n\n`;
            
            freeformWorkAreaRef.current.innerText = visualToolDescription + currentContent;
            setFreeformAnswer(visualToolDescription + currentContent);
        }
    };

    // Function to handle component selection and show overlay
    const handleComponentSelect = (component) => {
        setSelectedComponent(component);
        setIsComponentOverlayVisible(true);
        setIsComponentFullscreen(false);
    };

    // Function to close component overlay
    const closeComponentOverlay = () => {
        setIsComponentOverlayVisible(false);
        setSelectedComponent(null);
        setIsComponentFullscreen(false);
    };

    // Function to toggle fullscreen mode
    const toggleFullscreen = () => {
        setIsComponentFullscreen(!isComponentFullscreen);
    };

    // Dynamically derive available topics whenever selectedSubject or selectedGrade changes.
    useEffect(() => {
        if (selectedSubject && selectedGrade) {
            // This would need to be passed as a prop or imported
            const topicsForGrade = []; // Placeholder - needs curriculumData
            setAvailableTopics(topicsForGrade);

            if (topicsForGrade.length > 0) {
                setSelectedTopic(topicsForGrade[0]);
                setSelectedFreeformTopic(topicsForGrade[0]);
            } else {
                setSelectedTopic('');
                setSelectedFreeformTopic(null);
            }
        } else {
            setAvailableTopics([]);
            setSelectedTopic('');
            setSelectedFreeformTopic(null);
        }
    }, [selectedSubject, selectedGrade, setSelectedFreeformTopic]);

    // Automatically scroll to the bottom of the chat whenever chatHistory changes
    useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [chatHistory]);

    // Effect to clear contentEditable div when freeformAnswer state changes
    useEffect(() => {
        if (freeformWorkAreaRef.current && freeformAnswer === '') {
            freeformWorkAreaRef.current.innerText = '';
        }
    }, [freeformAnswer, freeformWorkAreaRef]);

    // Debug effect to log repository states
    useEffect(() => {
        console.log('🔍 Repository visibility states:', {
            showMathComponentsRepository,
            showChemistryComponentsRepository,
            showPhysicsComponentsRepository,
            showCrossDisciplinaryComponentsRepository,
            showSourceDocumentRepository
        });
    }, [showMathComponentsRepository, showChemistryComponentsRepository, showPhysicsComponentsRepository, showCrossDisciplinaryComponentsRepository, showSourceDocumentRepository]);

    // Function to handle sending freeform queries with selected topic context
    const handleSendWithTopic = () => {
        const combinedQuery = `Topic: ${selectedTopic}\nProblem and Solution:\n${freeformAnswer}`;
        handleSendFreeformQuery(combinedQuery);
    };

    // Source document handling functions
    const handleSelectSourceDocument = (doc) => {
        if (doc) {
            setSelectedSourceDocument(doc);
            setSourceDocumentData(doc.template);
            setIsSourceDocumentSubmitted(false);
            
            // Add source document info to the workspace
            if (freeformWorkAreaRef.current) {
                const currentContent = freeformWorkAreaRef.current.innerText;
                const sourceDocDescription = `[Source Document: ${doc.name}]\n${doc.description}\n\n`;
                
                freeformWorkAreaRef.current.innerText = sourceDocDescription + currentContent;
                setFreeformAnswer(sourceDocDescription + currentContent);
            }
        }
        setShowSourceDocumentRepository(false);
    };

    const handleMathComponentSelect = (component) => {
        setShowMathComponentsRepository(false);
        console.log('Selected math component:', component);
    };

    const handleChemistryComponentSelect = (component) => {
        setShowChemistryComponentsRepository(false);
        console.log('Selected chemistry component:', component);
    };

    const handlePhysicsComponentSelect = (component) => {
        setShowPhysicsComponentsRepository(false);
        console.log('Selected physics component:', component);
    };

    const handleCrossDisciplinaryComponentSelect = (component) => {
        setShowCrossDisciplinaryComponentsRepository(false);
        console.log('Selected cross-disciplinary component:', component);
    };

    const handleSourceDocumentDataChange = (newData) => {
        setSourceDocumentData(newData);
    };

    const handleSourceDocumentSubmit = async () => {
        if (!sourceDocumentData || !selectedSourceDocument) return;
        setLoading(true);
        try {
            // Validate the source document first
            const validationResponse = await fetch('http://127.0.0.1:5001/api/source-documents/validate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    document_data: sourceDocumentData,
                    document_type: selectedSourceDocument.type
                })
            });
            if (validationResponse.ok) {
                const validationResult = await validationResponse.json();
                // Send to AI for marking/feedback
                const aiResponse = await getAgentResponse(
                    `Please review this ${selectedSourceDocument.name} submission and provide detailed feedback:\n\n${validationResult.validation_result}`,
                    []
                );
                // Add the document submission to chat history
                addQuestionToChat(`Submitted ${selectedSourceDocument.name} for review`);
                updateAnswerInChat(
                    chatHistory[chatHistory.length - 1]?.id,
                    `Source Document Validation:\n${validationResult.validation_result}\n\nAI Feedback:\n${aiResponse}`,
                    true
                );
                setIsSourceDocumentSubmitted(true);
            }
        } catch (error) {
            console.error('Error submitting source document:', error);
        } finally {
            setLoading(false);
        }
    };

    // Check if the last message in the chat history is an AI response that is not successful
    const lastMessage = chatHistory[chatHistory.length - 1];
    const isLastMessageUnsuccessful = lastMessage && lastMessage.answer && !lastMessage.isSuccessful && !lastMessage.loading;

    // Hide body scrollbar when component overlay is visible
    useEffect(() => {
        if (isComponentOverlayVisible) {
            const previous = document.body.style.overflow;
            document.body.style.overflow = 'hidden';
            return () => {
                document.body.style.overflow = previous || '';
            };
        }
    }, [isComponentOverlayVisible]);

    return (
        <div className="bg-gray-50 min-h-screen">

            {/* --- Freeform Work Area (Visible when workspaceMode is 'freeform') --- */}
            {workspaceMode === 'freeform' && (
                <div className="flex h-screen bg-white">
                    {/* Main Work Area */}
                    <div className="flex-1 flex flex-col">
                        {/* Single Header Line */}
                        <div className="flex items-center justify-between p-4 border-b border-gray-200 bg-white">
                            <h1 className="text-lg font-semibold text-gray-800">
                                Personal Study: Freeform Work Area - {selectedSubject?.name || '...'} [Grade {selectedGrade || '...'}]
                            </h1>
                            {/* Show toggle button only when sidebar is hidden */}
                            {!isVisualToolsPaneVisible && (
                                <button
                                    onClick={() => setIsVisualToolsPaneVisible(true)}
                                    className="flex items-center space-x-1 px-3 py-1 text-sm bg-gray-100 hover:bg-gray-200 rounded-md transition-colors"
                                    title="Show Visual Tools"
                                >
                                    <ChevronLeft className="h-4 w-4" />
                                    <span className="hidden sm:inline">Visual Tools</span>
                                </button>
                            )}
                        </div>

                        {/* Topic Dropdown + Send Button Row */}
                        <div className="p-4 border-b border-gray-100 flex items-center justify-between">
                            <select
                                value={selectedTopic}
                                onChange={(e) => {
                                    setSelectedTopic(e.target.value);
                                    setSelectedFreeformTopic(e.target.value);
                                }}
                                className="w-full max-w-xs px-3 py-2 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                disabled={!availableTopics || availableTopics.length === 0}
                            >
                                <option value="">Select Topic for AI Context</option>
                                {availableTopics && availableTopics.length > 0 ? (
                                    availableTopics.map(topicName => (
                                        <option key={topicName} value={topicName}>{topicName}</option>
                                    ))
                                ) : (
                                    <option value="">No topics available</option>
                                )}
                            </select>

                            <button
                                onClick={handleSendWithTopic}
                                disabled={!freeformAnswer.trim() || !selectedTopic}
                                className="ml-4 bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed text-sm font-medium"
                                title="Send Problem to AI Tutor"
                            >
                                Send Problem to AI Tutor
                            </button>
                        </div>

                        {/* Selected Source Document Display - Compact */}
                        {selectedSourceDocument && (
                            <div className="p-4 border-b border-gray-100 bg-blue-50">
                                <div className="flex justify-between items-center">
                                    <h4 className="text-sm font-semibold text-blue-800">
                                        {selectedSourceDocument.name}
                                    </h4>
                                    <button
                                        onClick={() => {
                                            setSelectedSourceDocument(null);
                                            setSourceDocumentData(null);
                                            setIsSourceDocumentSubmitted(false);
                                        }}
                                        className="text-blue-600 hover:text-blue-800"
                                    >
                                        <X className="h-4 w-4" />
                                    </button>
                                </div>
                                
                                {/* Render the correct form for each source document type */}
                                {selectedSourceDocument.name === 'Deposit Slip' && (
                                    <DepositSlipInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Cash Receipts Journal' && (
                                    <CashReceiptsJournalInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Cash Payments Journal' && (
                                    <CashPaymentsJournalInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Cheque' && (
                                    <ChequeInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Receipt' && (
                                    <ReceiptInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Cash Invoice' && (
                                    <CashInvoiceInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Income Statement' && ['Business Studies', 'Accounting'].includes(selectedSubject?.name) && parseInt(selectedGrade) >= 10 && (
                                    <IncomeStatementInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Trading Income Statement' && ['Business Studies', 'Accounting'].includes(selectedSubject?.name) && parseInt(selectedGrade) >= 10 && (
                                    <TradingIncomeStatementInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Debtors Journal' && (
                                    <DebtorsJournalInput
                                        data={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Creditors Journal' && (
                                    <CreditorsJournalInput
                                        data={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                    />
                                )}
                                {selectedSourceDocument.name === 'General Ledger' && (
                                    <GeneralLedgerInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                {selectedSourceDocument.name === 'Debtors Ledger' && (
                                    <DebtorsLedgerInput
                                        initialData={sourceDocumentData}
                                        onChange={handleSourceDocumentDataChange}
                                        isSubmitted={isSourceDocumentSubmitted}
                                    />
                                )}
                                
                                {/* Submit Button */}
                                <button
                                    onClick={handleSourceDocumentSubmit}
                                    disabled={loading}
                                    className="mt-2 bg-blue-600 text-white px-3 py-1 rounded text-sm hover:bg-blue-700 disabled:bg-gray-400"
                                >
                                    {loading ? <Loader2 className="animate-spin h-3 w-3" /> : 'Submit for Review'}
                                </button>
                            </div>
                        )}

                        {/* Main Work Area - Maximized */}
                        <div className="flex-1 p-4">
                            <div
                                ref={freeformWorkAreaRef}
                                contentEditable
                                className="w-full h-full p-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none overflow-hidden bg-white"
                                style={{ scrollbarWidth: 'none' }}
                                placeholder="Type your problem here..."
                                onInput={(e) => setFreeformAnswer(e.currentTarget.innerText)}
                            />
                        </div>
                    </div>

                    {/* Visual Tools Pane - Collapsible */}
                    {isVisualToolsPaneVisible && (
                        <div className="w-80 bg-gray-50 border-l border-gray-200 overflow-y-auto">
                            <div className="p-4">
                                <div className="flex items-center justify-between mb-4">
                                    <h3 className="text-lg font-semibold text-gray-800">Visual Tools</h3>
                                    <button
                                        onClick={() => setIsVisualToolsPaneVisible(false)}
                                        className="flex items-center space-x-1 px-2 py-1 text-sm bg-gray-100 hover:bg-gray-200 rounded-md transition-colors"
                                        title="Hide Visual Tools"
                                    >
                                        <ChevronRight className="h-4 w-4" />
                                        <span className="hidden sm:inline">Hide</span>
                                    </button>
                                </div>
                                
                                {/* Available Tools with Expandable Sections */}
                                <div className="space-y-3">
                                    {getAvailableRepositories().map((repo) => {
                                        const Icon = repo.icon;
                                        return (
                                            <div key={repo.key} className="bg-white border border-gray-200 rounded-lg overflow-hidden">
                                                <button
                                                    onClick={() => {
                                                        // Toggle the expanded state for this repository
                                                        if (expandedRepositories.includes(repo.key)) {
                                                            setExpandedRepositories(expandedRepositories.filter(key => key !== repo.key));
                                                        } else {
                                                            setExpandedRepositories([...expandedRepositories, repo.key]);
                                                        }
                                                    }}
                                                    className="w-full flex items-center justify-between p-3 hover:bg-gray-50 transition-colors duration-200"
                                                >
                                                    <div className="flex items-center space-x-3">
                                                        <Icon className="h-5 w-5 text-gray-600" />
                                                        <span className="text-sm font-medium text-gray-700">{repo.name}</span>
                                                    </div>
                                                    <ChevronRight 
                                                        className={`h-4 w-4 text-gray-500 transition-transform duration-200 ${
                                                            expandedRepositories.includes(repo.key) ? 'rotate-90' : ''
                                                        }`} 
                                                    />
                                                </button>
                                                
                                                {/* Expanded Content - Show Component Previews */}
                                                {expandedRepositories.includes(repo.key) && (
                                                    <div className="border-t border-gray-100 bg-gray-50">
                                                        {repo.key === 'math' && (
                                                            <div className="p-3 space-y-4">
                                                                {/* Number Systems */}
                                                                <div>
                                                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">Number Systems</h4>
                                                                    <div className="grid grid-cols-2 gap-2">
                                                                                                                                                                                                                         <div 
                                                                            className="cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Number Line', 
                                                                                category: 'Number Systems', 
                                                                                type: 'number_line',
                                                                                component: 'NumberLineInput'
                                                                            })}
                                                                        >
                                                                            <ThumbnailRenderer 
                                                                                componentId="number_line"
                                                                                width={120}
                                                                                height={64}
                                                                                fallbackData={{
                                                                                    gradient: 'from-gray-100 to-gray-200',
                                                                                    textColor: 'text-gray-800',
                                                                                    title: 'Number Line',
                                                                                    description: 'Interactive number line'
                                                                                }}
                                                                            />
                                                                        </div>

                                                                        <div 
                                                                            className="cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Complex Numbers', 
                                                                                category: 'Number Systems', 
                                                                                type: 'complex_numbers',
                                                                                component: 'ComplexNumbersInput'
                                                                            })}
                                                                        >
                                                                            <ThumbnailRenderer 
                                                                                componentId="complex_numbers"
                                                                                width={120}
                                                                                height={64}
                                                                                fallbackData={{
                                                                                    gradient: 'from-purple-100 to-purple-200',
                                                                                    textColor: 'text-purple-800',
                                                                                    title: 'Complex Numbers',
                                                                                    description: 'Calculator & Argand diagram'
                                                                                }}
                                                                            />
                                                                        </div>
                                                                        
                                                                        <div 
                                                                            className="cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Fraction Visualizer', 
                                                                                category: 'Number Systems', 
                                                                                type: 'fraction_visualizer',
                                                                                component: 'FractionVisualizer'
                                                                            })}
                                                                        >
                                                                            <ThumbnailRenderer 
                                                                                componentId="fraction_visualizer"
                                                                                width={120}
                                                                                height={64}
                                                                                fallbackData={{
                                                                                    gradient: 'from-green-100 to-green-200',
                                                                                    textColor: 'text-green-800',
                                                                                    title: 'Fractions',
                                                                                    description: 'Visual fraction representation'
                                                                                }}
                                                                            />
                                                                        </div>
                                                                    </div>
                                                                </div>

                                                                {/* Algebra */}
                                                                <div>
                                                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">Algebra</h4>
                                                                    <div className="grid grid-cols-2 gap-2">
                                                                        <div 
                                                                            className="cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Coordinate Plane', 
                                                                                category: 'Algebra', 
                                                                                type: 'coordinate_plane',
                                                                                component: 'CoordinatePlaneInput'
                                                                            })}
                                                                        >
                                                                            <ThumbnailRenderer 
                                                                                componentId="coordinate_plane"
                                                                                width={120}
                                                                                height={64}
                                                                                fallbackData={{
                                                                                    gradient: 'from-purple-100 to-purple-200',
                                                                                    textColor: 'text-purple-800',
                                                                                    title: 'Coordinate Plane',
                                                                                    description: 'Plot points and functions'
                                                                                }}
                                                                            />
                                                                        </div>
                                                                        
                                                                        <div 
                                                                            className="cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Algebraic Expressions', 
                                                                                category: 'Algebra', 
                                                                                type: 'algebraic_expression_builder',
                                                                                component: 'AlgebraicExpressionBuilder'
                                                                            })}
                                                                        >
                                                                            <ThumbnailRenderer 
                                                                                componentId="algebraic_expression_builder"
                                                                                width={120}
                                                                                height={64}
                                                                                fallbackData={{
                                                                                    gradient: 'from-orange-100 to-orange-200',
                                                                                    textColor: 'text-orange-800',
                                                                                    title: 'Expressions',
                                                                                    description: 'Build and simplify expressions'
                                                                                }}
                                                                            />
                                                                        </div>

                                                                        







                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Matrix Calculator', 
                                                                                category: 'Algebra', 
                                                                                type: 'matrix_calculator',
                                                                                component: 'MatrixCalculator'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-emerald-100 to-emerald-200 rounded flex items-center justify-center text-xs text-emerald-800 font-medium">
                                                                                Matrix Calculator
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Matrix operations</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Vector Calculator', 
                                                                                category: 'Algebra', 
                                                                                type: 'vector_calculator',
                                                                                component: 'VectorCalculator'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-rose-100 to-rose-200 rounded flex items-center justify-center text-xs text-rose-800 font-medium">
                                                                                Vector Calculator
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Vector operations</p>
                                                                        </div>
                                                                    </div>
                                                                </div>

                                                                {/* Geometry */}
                                                                <div>
                                                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">Geometry</h4>
                                                                    <div className="grid grid-cols-2 gap-2">
                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Geometric Construction', 
                                                                                category: 'Geometry', 
                                                                                type: 'geometric_construction',
                                                                                component: 'GeometricConstructionInput'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-red-100 to-red-200 rounded flex items-center justify-center text-xs text-red-800 font-medium">
                                                                                Construction
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Geometric constructions</p>
                                                                        </div>
                                                                        
                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Mathematical Instruments', 
                                                                                category: 'Geometry', 
                                                                                type: 'mathematical_instruments',
                                                                                component: 'MathematicalInstruments'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-indigo-100 to-indigo-200 rounded flex items-center justify-center text-xs text-indigo-800 font-medium">
                                                                                Instruments
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Protractor, compass, ruler</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Circle Input', 
                                                                                category: 'Geometry', 
                                                                                type: 'circle_input',
                                                                                component: 'CircleInput'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-blue-100 to-blue-200 rounded flex items-center justify-center text-xs text-blue-800 font-medium">
                                                                                Circle Input
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Circle properties</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Conic Sections', 
                                                                                category: 'Geometry', 
                                                                                type: 'conic_sections',
                                                                                component: 'ConicSections'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-green-100 to-green-200 rounded flex items-center justify-center text-xs text-green-800 font-medium">
                                                                                Conic Sections
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Ellipse, parabola, hyperbola</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Geometry Studio', 
                                                                                category: 'Geometry', 
                                                                                type: 'geometry_studio',
                                                                                component: 'GeometryStudio'
                                                                            })}
                                                                        >
                                                                            <ThumbnailRenderer 
                                                                                componentId="geometry_studio"
                                                                                width={120}
                                                                                height={64}
                                                                                fallbackData={{
                                                                                    gradient: 'from-blue-100 to-indigo-200',
                                                                                    textColor: 'text-blue-800',
                                                                                    title: 'Geometry Studio',
                                                                                    description: '2D • 3D • Advanced'
                                                                                }}
                                                                            />
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: '3D Coordinate System', 
                                                                                category: 'Geometry', 
                                                                                type: 'three_d_coordinate_system',
                                                                                component: 'ThreeDCoordinateSystem'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-purple-100 to-purple-200 rounded flex items-center justify-center text-xs text-purple-800 font-medium">
                                                                                3D Coordinates
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">3D space visualization</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Polar Coordinates', 
                                                                                category: 'Geometry', 
                                                                                type: 'polar_coordinate_system',
                                                                                component: 'PolarCoordinateSystem'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-orange-100 to-orange-200 rounded flex items-center justify-center text-xs text-orange-800 font-medium">
                                                                                Polar Coordinates
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">r and θ coordinates</p>
                                                                        </div>
                                                                    </div>
                                                                </div>

                                                                {/* Statistics & Probability */}
                                                                <div>
                                                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">Statistics & Probability</h4>
                                                                    <div className="grid grid-cols-2 gap-2">
                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Statistical Analysis', 
                                                                                category: 'Statistics', 
                                                                                type: 'statistical_analysis',
                                                                                component: 'StatisticalAnalysisInput'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-teal-100 to-teal-200 rounded flex items-center justify-center text-xs text-teal-800 font-medium">
                                                                                Statistics
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Data analysis tools</p>
                                                                        </div>
                                                                        
                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Probability Simulator', 
                                                                                category: 'Probability', 
                                                                                type: 'probability_simulator',
                                                                                component: 'ProbabilitySimulator'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-pink-100 to-pink-200 rounded flex items-center justify-center text-xs text-pink-800 font-medium">
                                                                                Probability
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Probability experiments</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Bar Chart', 
                                                                                category: 'Statistics', 
                                                                                type: 'bar_chart_input',
                                                                                component: 'BarChartInput'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-yellow-100 to-yellow-200 rounded flex items-center justify-center text-xs text-yellow-800 font-medium">
                                                                                Bar Chart
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Bar chart creation</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Line Graph', 
                                                                                category: 'Statistics', 
                                                                                type: 'line_graph_input',
                                                                                component: 'LineGraphInput'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-indigo-100 to-indigo-200 rounded flex items-center justify-center text-xs text-indigo-800 font-medium">
                                                                                Line Graph
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Line graph creation</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Pie Chart', 
                                                                                category: 'Statistics', 
                                                                                type: 'pie_chart_input',
                                                                                component: 'PieChartInput'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-red-100 to-red-200 rounded flex items-center justify-center text-xs text-red-800 font-medium">
                                                                                Pie Chart
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Pie chart creation</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Histogram', 
                                                                                category: 'Statistics', 
                                                                                type: 'histogram',
                                                                                component: 'Histogram'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-green-100 to-green-200 rounded flex items-center justify-center text-xs text-green-800 font-medium">
                                                                                Histogram
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Frequency distribution</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Scatter Plot', 
                                                                                category: 'Statistics', 
                                                                                type: 'scatter_plot',
                                                                                component: 'ScatterPlot'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-blue-100 to-blue-200 rounded flex items-center justify-center text-xs text-blue-800 font-medium">
                                                                                Scatter Plot
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Correlation analysis</p>
                                                                        </div>

                                                                                                                                                                                                                          <div 
                                                                             className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                             onClick={() => handleComponentSelect({ 
                                                                                 name: 'Box & Whisker Plot', 
                                                                                 category: 'Statistics', 
                                                                                 type: 'box_whisker_plot',
                                                                                 component: 'BoxWhiskerPlot'
                                                                             })}
                                                                         >
                                                                             <div className="h-16 bg-gradient-to-r from-blue-100 to-blue-200 rounded flex items-center justify-center text-xs text-blue-800 font-medium">
                                                                                 Box & Whisker
                                                                             </div>
                                                                             <p className="text-xs text-gray-600 mt-1 text-center">Box and Whisker Plot</p>
                                                                         </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Stem & Leaf Plot', 
                                                                                category: 'Statistics', 
                                                                                type: 'stem_and_leaf_plot',
                                                                                component: 'StemAndLeafPlot'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-cyan-100 to-cyan-200 rounded flex items-center justify-center text-xs text-cyan-800 font-medium">
                                                                                Stem & Leaf
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Data organization</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Frequency Polygon', 
                                                                                category: 'Statistics', 
                                                                                type: 'frequency_polygon',
                                                                                component: 'FrequencyPolygon'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-amber-100 to-amber-200 rounded flex items-center justify-center text-xs text-amber-800 font-medium">
                                                                                Frequency Polygon
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Frequency distribution</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Cumulative Frequency', 
                                                                                category: 'Statistics', 
                                                                                type: 'cumulative_frequency_curve',
                                                                                component: 'CumulativeFrequencyCurve'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-violet-100 to-violet-200 rounded flex items-center justify-center text-xs text-violet-800 font-medium">
                                                                                Cumulative Freq
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Running totals</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Normal Distribution', 
                                                                                category: 'Statistics', 
                                                                                type: 'normal_distribution',
                                                                                component: 'NormalDistribution'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-emerald-100 to-emerald-200 rounded flex items-center justify-center text-xs text-emerald-800 font-medium">
                                                                                Normal Distribution
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Bell curve</p>
                                                                        </div>
                                                                    </div>
                                                                </div>

                                                                {/* Advanced Mathematics */}
                                                                <div>
                                                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">Advanced Mathematics</h4>
                                                                    <div className="grid grid-cols-2 gap-2">
                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Calculus Tools', 
                                                                                category: 'Calculus', 
                                                                                type: 'calculus_tools',
                                                                                component: 'CalculusTools'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-rose-100 to-rose-200 rounded flex items-center justify-center text-xs text-rose-800 font-medium">
                                                                                Calculus Tools
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Derivatives & integrals</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Tree Diagram', 
                                                                                category: 'Probability', 
                                                                                type: 'tree_diagram',
                                                                                component: 'TreeDiagram'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-sky-100 to-sky-200 rounded flex items-center justify-center text-xs text-sky-800 font-medium">
                                                                                Tree Diagram
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Probability trees</p>
                                                                        </div>

                                                                        <div 
                                                                            className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                            onClick={() => handleComponentSelect({ 
                                                                                name: 'Venn Diagram', 
                                                                                category: 'Set Theory', 
                                                                                type: 'venn_diagram',
                                                                                component: 'VennDiagram'
                                                                            })}
                                                                        >
                                                                            <div className="h-16 bg-gradient-to-r from-lime-100 to-lime-200 rounded flex items-center justify-center text-xs text-lime-800 font-medium">
                                                                                Venn Diagram
                                                                            </div>
                                                                            <p className="text-xs text-gray-600 mt-1 text-center">Set relationships</p>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        )}
                                                        
                                                        {repo.key === 'chemistry' && (
                                                            <div className="p-3 space-y-3">
                                                                <div className="grid grid-cols-2 gap-2">
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Periodic Table', category: 'Fundamentals', type: 'periodic-table' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-blue-100 to-blue-200 rounded flex items-center justify-center text-xs text-blue-800 font-medium">
                                                                            Periodic Table
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Element properties</p>
                                                                    </div>
                                                                    
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Molecular Builder', category: 'Molecular', type: 'molecular-builder' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-green-100 to-green-200 rounded flex items-center justify-center text-xs text-green-800 font-medium">
                                                                            Molecules
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Build molecules</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        )}
                                                        
                                                        {repo.key === 'physics' && (
                                                            <div className="p-3 space-y-3">
                                                                <div className="grid grid-cols-2 gap-2">
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Force Diagram', category: 'Mechanics', type: 'force-diagram' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-red-100 to-red-200 rounded flex items-center justify-center text-xs text-red-800 font-medium">
                                                                            Forces
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Force vectors</p>
                                                                    </div>
                                                                    
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Wave Simulator', category: 'Waves', type: 'wave-simulator' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-purple-100 to-purple-200 rounded flex items-center justify-center text-xs text-purple-800 font-medium">
                                                                            Waves
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Wave properties</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        )}
                                                        
                                                        {repo.key === 'source-documents' && (
                                                            <div className="p-3 space-y-3">
                                                                <div className="grid grid-cols-2 gap-2">
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Deposit Slip', category: 'Source Documents', type: 'deposit-slip' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-blue-100 to-blue-200 rounded flex items-center justify-center text-xs text-blue-800 font-medium">
                                                                            Deposit Slip
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Bank deposit form</p>
                                                                    </div>
                                                                    
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Cash Receipts Journal', category: 'Source Documents', type: 'cash-receipts' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-green-100 to-green-200 rounded flex items-center justify-center text-xs text-green-800 font-medium">
                                                                            Cash Receipts
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Cash receipts log</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        )}
                                                        
                                                        {repo.key === 'cross-disciplinary' && (
                                                            <div className="p-3 space-y-3">
                                                                <div className="grid grid-cols-2 gap-2">
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Mind Map', category: 'Organization', type: 'mind-map' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-indigo-100 to-indigo-200 rounded flex items-center justify-center text-xs text-indigo-800 font-medium">
                                                                            Mind Map
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Visual organization</p>
                                                                    </div>
                                                                    
                                                                    <div 
                                                                        className="bg-white p-2 rounded border border-gray-200 cursor-pointer hover:bg-blue-50 hover:border-blue-300 transition-colors"
                                                                        onClick={() => handleComponentSelect({ name: 'Flow Chart', category: 'Organization', type: 'flow-chart' })}
                                                                    >
                                                                        <div className="h-16 bg-gradient-to-r from-teal-100 to-teal-200 rounded flex items-center justify-center text-xs text-teal-800 font-medium">
                                                                            Flow Chart
                                                                        </div>
                                                                        <p className="text-xs text-gray-600 mt-1 text-center">Process flow</p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        )}
                                                    </div>
                                                )}
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        </div>
                    )}
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
                                        <span className={`px-3 py-1 text-sm rounded-full ${
                                            question.isSubmitted ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
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
                                            {getAvailableRepositories().length > 0 && (
                                                <div className="mb-3 p-2 bg-gray-50 rounded border border-gray-200">
                                                    <p className="text-xs text-gray-600 mb-1 font-medium">Available Tools:</p>
                                                    <div className="flex flex-wrap gap-1">
                                                        {getAvailableRepositories().map((repo) => {
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

            {/* Math Components Repository Modal */}
            <MathComponentsRepository 
                isVisible={showMathComponentsRepository}
                onSelectComponent={handleVisualToolDataToWorkspace}
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
            />

            {/* Chemistry Components Repository Modal */}
            <ChemistryComponentsRepository 
                isVisible={showChemistryComponentsRepository}
                onSelectComponent={handleVisualToolDataToWorkspace}
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
            />

            {/* Physics Components Repository Modal */}
            <PhysicsComponentsRepository 
                isVisible={showPhysicsComponentsRepository}
                onSelectComponent={handleVisualToolDataToWorkspace}
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
            />

            {/* Cross-Disciplinary Components Repository Modal */}
            <CrossDisciplinaryComponentsRepository 
                isVisible={showCrossDisciplinaryComponentsRepository}
                onSelectComponent={handleVisualToolDataToWorkspace}
                selectedSubject={selectedSubject}
                selectedGrade={selectedGrade}
            />

            {/* Component Overlay */}
            <ComponentOverlay
                selectedComponent={selectedComponent}
                isVisible={isComponentOverlayVisible}
                isFullscreen={isComponentFullscreen}
                onClose={closeComponentOverlay}
                onToggleFullscreen={toggleFullscreen}
            />
            {/* Old component overlay code removed - now using shared ComponentOverlay */}
            {false && false && isComponentOverlayVisible && selectedComponent && (
                <div className={`fixed inset-0 z-50 flex items-center justify-center ${(selectedComponent.type === 'algebraic_expression_builder' || selectedComponent.type === 'complex_numbers') ? 'bg-white' : (isComponentFullscreen ? 'bg-white' : 'bg-black bg-opacity-50')}`}>
                    <div className={`relative ${(selectedComponent.type === 'algebraic_expression_builder' || selectedComponent.type === 'complex_numbers') ? 'w-full h-full' : (isComponentFullscreen ? 'w-full h-full' : 'w-11/12 max-w-4xl h-5/6')} bg-white rounded-lg shadow-2xl flex flex-col`}>
                                                {/* Header */}
                         <div className="flex items-center justify-between p-2 border-b border-gray-200 bg-gray-50">
                             <h3 className="text-lg font-semibold text-gray-800">
                                 {selectedComponent.name}
                             </h3>
                             <div className="flex items-center space-x-2">
                                                                   {(selectedComponent.type !== 'algebraic_expression_builder' && selectedComponent.type !== 'complex_numbers') && (
                                     <button
                                         onClick={toggleFullscreen}
                                         className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-md transition-colors"
                                         title={isComponentFullscreen ? 'Exit Fullscreen' : 'Fullscreen'}
                                     >
                                         {isComponentFullscreen ? (
                                             <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                                             </svg>
                                         ) : (
                                             <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
                                             </svg>
                                         )}
                                     </button>
                                 )}
                                 <button
                                     onClick={closeComponentOverlay}
                                     className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-md transition-colors"
                                     title="Close"
                                 >
                                     <X className="w-5 h-5" />
                                 </button>
                             </div>
                         </div>

                        {/* Component Content */}
                        <div className={`flex-1 ${(selectedComponent.type === 'algebraic_expression_builder' || selectedComponent.type === 'complex_numbers') ? 'px-6 pb-6 pt-[18px]' : 'p-6'} overflow-y-auto`}>
                            {/* Render actual math components based on type */}
                            {selectedComponent.type === 'algebraic_expression_builder' && (
                                <AlgebraicExpressionBuilder 
                                    initialData={{
                                        title: "Algebraic Expression",
                                        expression: "2x + 3y",
                                        variables: ["x", "y"],
                                        showSteps: true
                                    }}
                                    onChange={() => {}}
                                    isSubmitted={false}
                                    aiInput={{
                                        expression: "2x + 3y",
                                        operation: "simplify",
                                        instructions: "Simplify the expression step by step",
                                        steps: "First, identify the terms in the expression. Then, combine like terms. Finally, write the simplified result."
                                    }}
                                />
                            )}

                            {selectedComponent.type === 'complex_numbers' && (
                                <ComplexNumbersInput 
                                    initialData={{
                                        title: "Complex Numbers Calculator",
                                        operation: 'add',
                                        viewMode: 'calculator',
                                        z1_real: 3,
                                        z1_imag: 2,
                                        z2_real: 1,
                                        z2_imag: -1,
                                        simplifyExpression: 'sqrt(-16) + sqrt(-4) - sqrt(-1)',
                                        equationInput: '2x - 15i = 3 + 5yi',
                                        showGrid: true,
                                        showAxes: true,
                                        showUnitCircle: false,
                                        showPolarForm: false
                                    }}
                                    onChange={() => {}}
                                    isSubmitted={false}
                                />
                            )}

                            {selectedComponent.type === 'geometry_studio' && (
                                <GeometryStudio 
                                    initialData={{
                                        title: "Geometry Studio",
                                        mode: '2d',
                                        viewMode: 'construction',
                                        showGrid: true,
                                        showAxes: true,
                                        showLabels: true,
                                        gridSize: 20,
                                        unitScale: 1,
                                        backgroundColor: '#ffffff',
                                        gridColor: '#e5e7eb',
                                        axisColor: '#374151',
                                        shapeColor: '#3B82F6',
                                        pointColor: '#EF4444',
                                        lineColor: '#10B981',
                                        points: [],
                                        lines: [],
                                        shapes: [],
                                        shapes3D: [],
                                        circles: [],
                                        angles: [],
                                        sectors: []
                                    }}
                                    onChange={() => {}}
                                    isSubmitted={false}
                                />
                            )}

                            {/* More components can be added here */}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Workspace;
