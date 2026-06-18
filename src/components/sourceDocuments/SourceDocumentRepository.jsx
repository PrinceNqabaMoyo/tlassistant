import { buildApiUrl } from '../../utils/apiBaseUrl';
import React, { useState, useEffect } from 'react';
import { Loader2, X } from 'lucide-react';
import VisualToolOverlay from '../workspace/VisualToolOverlay';

const SourceDocumentRepository = ({ onSelectJournal, isVisible, selectedSubject, selectedGrade }) => {
    const [journals, setJournals] = useState({});
    const [loading, setLoading] = useState(true);
    const [isFullScreen, setIsFullScreen] = useState(false);

    // Fallback source documents in case the API doesn't have them
    const fallbackSourceDocuments = {
        CPJ: {
            name: "Cash Payments Journal",
            description: "Record all cash payments made by the business",
            columns: ["Date", "Details", "Fol.", "Amount"]
        },
        CRJ: {
            name: "Cash Receipts Journal", 
            description: "Record all cash receipts received by the business",
            columns: ["Date", "Details", "Fol.", "Amount"]
        },
        GL: {
            name: "General Ledger",
            description: "Master record of all accounts with running balances",
            columns: ["Date", "Details", "Fol.", "Debit", "Credit", "Balance"]
        },
        DL: {
            name: "Debtors Ledger",
            description: "Individual customer accounts showing amounts owed",
            columns: ["Date", "Details", "Fol.", "Debit", "Credit", "Balance"]
        },
        CL: {
            name: "Creditors Ledger", 
            description: "Individual supplier accounts showing amounts owed",
            columns: ["Date", "Details", "Fol.", "Debit", "Credit", "Balance"]
        },
        TB: {
            name: "Trial Balance",
            description: "Summary of all account balances to check for errors",
            columns: ["Account", "Fol.", "Debit", "Credit"]
        },
        DEPOSIT_SLIP: {
            name: "Deposit Slip",
            description: "Bank deposit slip for depositing cash and cheques.",
            template: {
                bankName: "",
                businessName: "",
                accountNumber: Array(10).fill(""),
                date: "",
                depositReference: "",
                detailsOfDepositor: {
                    name: "",
                    signature: "",
                    telephone: ""
                },
                chequesDeposited: [
                    { cheque: "", drawer: "1", bank: "" },
                    { cheque: "", drawer: "2", bank: "" },
                    { cheque: "", drawer: "3", bank: "" }
                ],
                cashDeposited: [
                    { label: "Note", r: "", c: "" },
                    { label: "Silver", r: "", c: "" },
                    { label: "Bronze", r: "", c: "" },
                    { label: "Money orders", r: "", c: "" },
                    { label: "sub-total", r: "", c: "" },
                    { label: "branch name/clearance code", r: "", c: "" }
                ],
                bankStamp: "",
                totalR: ""
            }
        },
        CHEQUE: {
            name: "Cheque",
            description: "Cheque/cheque counterfoil for making payments",
            template: {
                counterfoil: {
                    date: "",
                    to: "",
                    for: "",
                    balance: { main: "", cents: "" },
                    deposit: { main: "", cents: "" },
                    subtotal: { main: "", cents: "" },
                    otherDebit: { main: "", cents: "" },
                    thisCheque: { main: "", cents: "" },
                    balanceAfter: { main: "", cents: "" }
                },
                mainCheque: {
                    bankName: "",
                    branchName: "",
                    notTransferrable: true,
                    date: "",
                    payTo: "",
                    orBearer: true,
                    amountInWords: "",
                    amountNumeric: { main: "", cents: "" },
                    cents: "00",
                    accountHolderName: "",
                    businessName: ""
                }
            }
        },
        RECEIPT: {
            name: "Receipt",
            description: "Receipt for cash received from customers",
            template: {
                receiptNumber: "",
                date: "",
                receivedFrom: "",
                amount: { main: "", cents: "" },
                for: "",
                receivedBy: ""
            }
        },
        CASH_INVOICE: {
            name: "Cash Invoice",
            description: "Invoice for cash sales",
            template: {
                invoiceNumber: "",
                date: "",
                customerName: "",
                items: [
                    { description: "", quantity: "", unitPrice: "", total: "" }
                ],
                subtotal: "",
                vat: "",
                total: ""
            }
        },
        INCOME_STATEMENT: {
            name: "Income Statement",
            description: "Financial statement showing revenue and expenses",
            template: {
                period: "",
                revenue: "",
                costOfSales: "",
                grossProfit: "",
                operatingExpenses: "",
                netProfit: ""
            }
        },
        TRADING_INCOME_STATEMENT: {
            name: "Trading Income Statement",
            description: "Detailed income statement with trading account",
            template: {
                period: "",
                sales: "",
                costOfSales: "",
                grossProfit: "",
                operatingExpenses: "",
                netProfit: ""
            }
        }
    };

    useEffect(() => {
        const fetchJournals = async () => {
            setLoading(true);
            try {
                const response = await fetch(buildApiUrl('/api/source-documents'));
                if (response.ok) {
                    const data = await response.json();
                    setJournals(data);
                } else {
                    console.warn('Failed to fetch source documents, using fallback data');
                    setJournals(fallbackSourceDocuments);
                }
            } catch (error) {
                console.error('Error fetching source documents:', error);
                setJournals(fallbackSourceDocuments);
            } finally {
                setLoading(false);
            }
        };

        if (isVisible) {
            fetchJournals();
        }
    }, [isVisible]);

    const filterDocumentsBySubjectAndGrade = (documents) => {
        const subjectName = selectedSubject?.name?.toLowerCase() || '';
        const grade = parseInt(selectedGrade) || 0;
        
        // Define which documents are available for which subjects and grades
        const documentAvailability = {
            'economic and management sciences': {
                grades: [7, 8, 9],
                documents: ['CPJ', 'CRJ', 'GL', 'DL', 'CL', 'TB', 'DEPOSIT_SLIP', 'CHEQUE', 'RECEIPT', 'CASH_INVOICE']
            },
            'business studies': {
                grades: [10, 11, 12],
                documents: ['CPJ', 'CRJ', 'GL', 'DL', 'CL', 'TB', 'DEPOSIT_SLIP', 'CHEQUE', 'RECEIPT', 'CASH_INVOICE', 'INCOME_STATEMENT', 'TRADING_INCOME_STATEMENT']
            },
            'accounting': {
                grades: [10, 11, 12],
                documents: ['CPJ', 'CRJ', 'GL', 'DL', 'CL', 'TB', 'DEPOSIT_SLIP', 'CHEQUE', 'RECEIPT', 'CASH_INVOICE', 'INCOME_STATEMENT', 'TRADING_INCOME_STATEMENT']
            }
        };
        
        const availability = documentAvailability[subjectName];
        if (!availability) return {};
        
        // Check if current grade is in the allowed grades for this subject
        if (!availability.grades.includes(grade)) return {};
        
        // Filter documents to only show those available for this subject and grade
        const filteredDocs = {};
        Object.entries(documents).forEach(([key, doc]) => {
            if (availability.documents.includes(key)) {
                filteredDocs[key] = doc;
            }
        });
        
        return filteredDocs;
    };

    const filteredJournals = filterDocumentsBySubjectAndGrade(journals);

    const handleSendToWorkspace = (selectedDocument) => {
        // This will be handled by the parent component
        onSelectJournal(selectedDocument);
    };

    return (
        <VisualToolOverlay
            isVisible={isVisible}
            onClose={() => onSelectJournal(null)}
            title="Source Document Repository"
            isFullScreen={isFullScreen}
            onToggleFullScreen={() => setIsFullScreen(!isFullScreen)}
        >
            <div className="p-4">
                <div className="mb-4 p-3 bg-blue-50 rounded-lg">
                    <p className="text-sm text-blue-800">
                        <strong>Subject:</strong> {selectedSubject?.name || 'Not selected'} | 
                        <strong> Grade:</strong> {selectedGrade || 'Not selected'}
                    </p>
                </div>
                
                {loading ? (
                    <div className="flex items-center justify-center py-8">
                        <Loader2 className="animate-spin h-6 w-6 text-blue-600" />
                        <span className="ml-2 text-gray-600">Loading source documents...</span>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 gap-3">
                        {Object.keys(filteredJournals).length > 0 ? (
                            Object.entries(filteredJournals).map(([key, journal]) => (
                                <div 
                                    key={key}
                                    onClick={() => handleSendToWorkspace({ type: key, ...journal })}
                                    className="border border-gray-200 rounded-lg p-3 hover:border-blue-300 hover:shadow-md cursor-pointer transition-all duration-200"
                                >
                                    <div className="flex items-center justify-between mb-2">
                                        <h3 className="text-sm font-semibold text-gray-800">{journal.name}</h3>
                                        <span className="text-xs font-mono bg-blue-100 text-blue-800 px-2 py-1 rounded">
                                            {key}
                                        </span>
                                    </div>
                                    <p className="text-gray-600 text-xs mb-2">{journal.description}</p>
                                    <div className="text-xs text-gray-500">
                                        <span className="font-semibold">Columns:</span> {journal.columns ? journal.columns.join(', ') : 'N/A'}
                                    </div>
                                </div>
                            ))
                        ) : (
                            <div className="p-4 text-center">
                                <div className="text-gray-500">
                                    <p className="text-sm font-semibold mb-2">No source documents available</p>
                                    <p className="text-xs">
                                        Source documents are only available for:
                                    </p>
                                    <ul className="text-xs mt-2 space-y-1">
                                        <li>• Grade 7-9: Economic and Management Sciences</li>
                                        <li>• Grade 10-12: Business Studies</li>
                                        <li>• Grade 10-12: Accounting</li>
                                    </ul>
                                </div>
                            </div>
                        )}
                    </div>
                )}
                
                <div className="mt-4 p-3 bg-blue-50 rounded-lg">
                    <h4 className="font-semibold text-blue-800 mb-2 text-sm">How to use:</h4>
                    <ul className="text-xs text-blue-700 space-y-1">
                        <li>• Select a source document to add it to your workspace</li>
                        <li>• Fill in the document according to the question</li>
                        <li>• Submit your completed document for AI marking</li>
                    </ul>
                </div>
            </div>
        </VisualToolOverlay>
    );
};

export default SourceDocumentRepository;
