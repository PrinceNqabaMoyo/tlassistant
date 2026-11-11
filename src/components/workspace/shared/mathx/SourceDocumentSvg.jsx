import React from 'react';

/**
 * Publication-Grade Vector South African Source Document Plates (GP-16 / Rule 0d-11).
 * Renders authentic vector SVG representations of primary accounting source documents:
 *  - receipt (Duplicate Receipt with official seal)
 *  - cheque_counterfoil (Perforated counterfoil with payee & allocations)
 *  - deposit_slip (Bank deposit slip with PASA double-ring teller stamp)
 *  - bank_statement (Official bank statement excerpt with audit trail)
 *  - cash_register_tape (Till slip / cash register roll with VAT breakdown)
 */

export default function SourceDocumentSvg({ spec }) {
    if (!spec) return null;
    const docType = String(spec.document_type || 'receipt').toLowerCase();

    return (
        <div
            data-testid="source-document-svg"
            className="w-full rounded-xl border border-slate-300 bg-white shadow-sm overflow-hidden my-3"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-100 border-b border-slate-300 text-xs">
                <div className="flex items-center gap-2">
                    <span className="inline-block w-2.5 h-2.5 rounded-full bg-emerald-600" />
                    <span className="font-semibold text-slate-800 uppercase tracking-wider">
                        Accounting Source Document • {spec.title || docType.replace(/_/g, ' ').toUpperCase()}
                    </span>
                </div>
                <span className="font-mono text-slate-600 font-medium text-[11px]">
                    Authentic Vector Plate
                </span>
            </div>

            <div
                data-testid={`source-doc-${docType.replace(/_/g, '-')}`}
                className="p-3 sm:p-4 flex flex-col items-center bg-slate-50"
            >
                {docType === 'receipt' && <ReceiptPlate spec={spec} />}
                {docType === 'cheque_counterfoil' && <ChequeCounterfoilPlate spec={spec} />}
                {docType === 'deposit_slip' && <DepositSlipPlate spec={spec} />}
                {docType === 'bank_statement' && <BankStatementPlate spec={spec} />}
                {docType === 'cash_register_tape' && <CashRegisterTapePlate spec={spec} />}
            </div>
        </div>
    );
}

function ReceiptPlate({ spec }) {
    const docNo = spec.doc_number || '082';
    const date = spec.date || '14 June 2024';
    const businessName = spec.business_name || 'Service Enterprise';
    const receivedFrom = spec.received_from || spec.party || 'M. Ndlovu';
    const amount = Number(spec.amount || 2500);
    const description = spec.description || 'Rent of storeroom';
    const receivedBy = spec.received_by || spec.signatory || 'Owner';

    return (
        <svg
            viewBox="0 0 540 220"
            className="w-full max-w-[540px] h-auto block bg-amber-50/40 rounded-lg border-2 border-slate-400 font-sans shadow-xs"
            data-testid="source-doc-receipt"
        >
            {/* Outer Decorative Frame */}
            <rect x="6" y="6" width="528" height="208" rx="4" fill="none" stroke="#64748b" strokeWidth="1" strokeDasharray="4,2" />

            {/* Header */}
            <text x="24" y="32" fontSize="13" fontWeight="800" fill="#0f172a" letterSpacing="0.5">
                {businessName.toUpperCase()}
            </text>
            <text x="24" y="47" fontSize="10" fill="#475569">
                Professional Services • South Africa
            </text>

            <rect x="360" y="16" width="154" height="32" rx="4" fill="#f1f5f9" stroke="#cbd5e1" strokeWidth="1" />
            <text x="370" y="30" fontSize="10" fontWeight="700" fill="#334155">
                DUPLICATE RECEIPT
            </text>
            <text x="370" y="43" fontSize="11" fontWeight="800" fill="#0f172a" fontFamily="monospace">
                No. {docNo}
            </text>

            {/* Content Rows */}
            <line x1="24" y1="60" x2="516" y2="60" stroke="#94a3b8" strokeWidth="1" />

            <text x="24" y="80" fontSize="11" fill="#475569">Date:</text>
            <text x="70" y="80" fontSize="11" fontWeight="700" fill="#0f172a">{date}</text>

            <text x="24" y="105" fontSize="11" fill="#475569">Received from:</text>
            <text x="120" y="105" fontSize="12" fontWeight="700" fill="#0f172a">{receivedFrom}</text>
            <line x1="120" y1="110" x2="516" y2="110" stroke="#cbd5e1" strokeWidth="1" />

            <text x="24" y="132" fontSize="11" fill="#475569">The sum of:</text>
            <text x="120" y="132" fontSize="11" fontStyle="italic" fill="#0f172a">
                R{amount.toLocaleString()} Rand only
            </text>
            <line x1="120" y1="137" x2="350" y2="137" stroke="#cbd5e1" strokeWidth="1" />

            {/* Amount Box */}
            <rect x="365" y="118" width="150" height="30" rx="4" fill="#ffffff" stroke="#0f172a" strokeWidth="1.5" />
            <text x="375" y="138" fontSize="14" fontWeight="800" fill="#0f172a" fontFamily="monospace">
                R {amount.toLocaleString()}.00
            </text>

            <text x="24" y="158" fontSize="11" fill="#475569">For:</text>
            <text x="70" y="158" fontSize="11" fontWeight="600" fill="#0f172a">{description}</text>
            <line x1="70" y1="163" x2="350" y2="163" stroke="#cbd5e1" strokeWidth="1" />

            {/* Signature & Stamp */}
            <text x="24" y="195" fontSize="10" fill="#475569">Received by:</text>
            <text x="95" y="195" fontSize="11" fontWeight="700" fontStyle="italic" fill="#1e3a8a">{receivedBy}</text>
            <line x1="95" y1="198" x2="230" y2="198" stroke="#64748b" strokeWidth="1" />

            {/* Double-ring Paid Stamp */}
            <g transform="translate(430, 180) rotate(-12)">
                <circle cx="0" cy="0" r="22" fill="none" stroke="#dc2626" strokeWidth="1.5" strokeDasharray="3,2" />
                <circle cx="0" cy="0" r="18" fill="none" stroke="#dc2626" strokeWidth="1" />
                <text x="0" y="-3" textAnchor="middle" fontSize="7" fontWeight="900" fill="#dc2626" letterSpacing="1">
                    PAID
                </text>
                <text x="0" y="7" textAnchor="middle" fontSize="6.5" fontWeight="700" fill="#dc2626">
                    OFFICIAL
                </text>
            </g>
        </svg>
    );
}

function ChequeCounterfoilPlate({ spec }) {
    const docNo = spec.doc_number || '204';
    const date = spec.date || '22 June 2024';
    const payee = spec.payee || spec.party || 'Waltons Stationers';
    const amount = Number(spec.amount || 750);
    const description = spec.description || 'Office stationery';

    return (
        <svg
            viewBox="0 0 540 180"
            className="w-full max-w-[540px] h-auto block bg-slate-50 rounded-lg border-2 border-slate-400 font-sans shadow-xs"
            data-testid="source-doc-cheque-counterfoil"
        >
            {/* Left Perforation (tear line from chequebook) */}
            <line x1="20" y1="8" x2="20" y2="172" stroke="#94a3b8" strokeWidth="2" strokeDasharray="4,4" />
            <text x="12" y="95" fontSize="8" fill="#94a3b8" transform="rotate(-90, 12, 95)" textAnchor="middle">
                PERFORATION
            </text>

            <rect x="28" y="10" width="496" height="160" rx="4" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />

            {/* Header */}
            <text x="44" y="32" fontSize="12" fontWeight="800" fill="#1e293b" letterSpacing="0.5">
                CHEQUE COUNTERFOIL
            </text>
            <text x="440" y="32" fontSize="12" fontWeight="800" fill="#0f172a" fontFamily="monospace">
                No. {docNo}
            </text>
            <line x1="44" y1="42" x2="508" y2="42" stroke="#cbd5e1" strokeWidth="1" />

            {/* Fields */}
            <text x="44" y="65" fontSize="11" fill="#475569">Date:</text>
            <text x="110" y="65" fontSize="11" fontWeight="700" fill="#0f172a">{date}</text>
            <line x1="110" y1="70" x2="508" y2="70" stroke="#e2e8f0" strokeWidth="1" />

            <text x="44" y="95" fontSize="11" fill="#475569">To (Payee):</text>
            <text x="110" y="95" fontSize="11.5" fontWeight="700" fill="#0f172a">{payee}</text>
            <line x1="110" y1="100" x2="508" y2="100" stroke="#e2e8f0" strokeWidth="1" />

            <text x="44" y="125" fontSize="11" fill="#475569">For:</text>
            <text x="110" y="125" fontSize="11" fill="#0f172a">{description}</text>
            <line x1="110" y1="130" x2="330" y2="130" stroke="#e2e8f0" strokeWidth="1" />

            {/* Amount Box */}
            <rect x="345" y="110" width="163" height="34" rx="4" fill="#f8fafc" stroke="#334155" strokeWidth="1.5" />
            <text x="355" y="132" fontSize="13" fontWeight="800" fill="#0f172a" fontFamily="monospace">
                R {amount.toLocaleString()}.00
            </text>

            <text x="44" y="155" fontSize="9" fill="#94a3b8" fontStyle="italic">
                Primary source document for Cash Payments Journal (CPJ) entry.
            </text>
        </svg>
    );
}

function DepositSlipPlate({ spec }) {
    const bankName = spec.bank_name || 'STANDARD BANK';
    const date = spec.date || '05 June 2024';
    const accountName = spec.account_name || spec.entity_name || 'Service Enterprise';
    const accountNo = spec.account_number || '104829104';
    const cashNotes = Number(spec.cash_amount || spec.cash_notes || 2400);
    const cheques = Number(spec.cheque_amount || spec.cheques || 1500);
    const total = Number(spec.total_amount || spec.total || (cashNotes + cheques));

    return (
        <svg
            viewBox="0 0 540 220"
            className="w-full max-w-[540px] h-auto block bg-white rounded-lg border-2 border-blue-400 font-sans shadow-xs"
            data-testid="source-doc-deposit-slip"
        >
            {/* Header Bar */}
            <rect x="0" y="0" width="540" height="36" fill="#1e3a8a" />
            <text x="18" y="24" fontSize="13" fontWeight="800" fill="#ffffff" letterSpacing="0.8">
                {bankName.toUpperCase()}
            </text>
            <text x="522" y="23" textAnchor="end" fontSize="10.5" fontWeight="700" fill="#bfdbfe">
                DEPOSIT SLIP / TELLER RECEIPT
            </text>

            {/* Details Grid */}
            <text x="20" y="55" fontSize="10" fill="#475569">Account Name:</text>
            <text x="110" y="55" fontSize="11" fontWeight="700" fill="#0f172a">{accountName}</text>

            <text x="330" y="55" fontSize="10" fill="#475569">Date:</text>
            <text x="375" y="55" fontSize="11" fontWeight="700" fill="#0f172a">{date}</text>

            <text x="20" y="75" fontSize="10" fill="#475569">Account No:</text>
            <text x="110" y="75" fontSize="11" fontWeight="700" fill="#0f172a" fontFamily="monospace">{accountNo}</text>

            <line x1="20" y1="85" x2="520" y2="85" stroke="#cbd5e1" strokeWidth="1" />

            {/* Breakdown Table */}
            <rect x="20" y="92" width="310" height="96" fill="#f8fafc" stroke="#cbd5e1" strokeWidth="1" />
            <text x="30" y="112" fontSize="10.5" fill="#334155">Bank Notes &amp; Coins:</text>
            <text x="315" y="112" textAnchor="end" fontSize="11" fontWeight="700" fill="#0f172a" fontFamily="monospace">
                R {cashNotes.toLocaleString()}.00
            </text>

            <text x="30" y="138" fontSize="10.5" fill="#334155">Cheques deposited:</text>
            <text x="315" y="138" textAnchor="end" fontSize="11" fontWeight="700" fill="#0f172a" fontFamily="monospace">
                R {cheques.toLocaleString()}.00
            </text>

            <line x1="20" y1="150" x2="330" y2="150" stroke="#94a3b8" strokeWidth="1" />

            <text x="30" y="174" fontSize="11" fontWeight="800" fill="#0f172a">TOTAL DEPOSITED:</text>
            <text x="315" y="174" textAnchor="end" fontSize="13" fontWeight="900" fill="#1e3a8a" fontFamily="monospace">
                R {total.toLocaleString()}.00
            </text>

            {/* Authentic PASA Bank Teller Stamp */}
            <g transform="translate(425, 142) rotate(4)">
                <circle cx="0" cy="0" r="38" fill="#eff6ff" stroke="#2563eb" strokeWidth="1.8" />
                <circle cx="0" cy="0" r="34" fill="none" stroke="#2563eb" strokeWidth="1" strokeDasharray="3,1.5" />
                <text x="0" y="-18" textAnchor="middle" fontSize="6.5" fontWeight="800" fill="#1d4ed8" letterSpacing="0.5">
                    RECEIVED BY TELLER
                </text>
                <text x="0" y="-3" textAnchor="middle" fontSize="8" fontWeight="800" fill="#0f172a" fontFamily="monospace">
                    {date}
                </text>
                <text x="0" y="12" textAnchor="middle" fontSize="6.5" fontWeight="700" fill="#1d4ed8">
                    STAMPED &amp; VERIFIED
                </text>
                <text x="0" y="24" textAnchor="middle" fontSize="6" fontWeight="700" fill="#2563eb">
                    {bankName}
                </text>
            </g>

            <text x="20" y="206" fontSize="9" fill="#64748b" fontStyle="italic">
                Stamped deposit slip serves as audit proof verifying the Bank column total in the Cash Receipts Journal (CRJ).
            </text>
        </svg>
    );
}

function BankStatementPlate({ spec }) {
    const bankName = spec.bank_name || 'NEDBANK';
    const date = spec.date || '30 June 2024';
    const accountName = spec.account_name || 'Service Enterprise';
    const description = spec.description || 'Monthly Service Fees & Electronic Levy';
    const amount = Number(spec.amount || 245);
    const isDebit = String(spec.entry_type || 'debit').toLowerCase() === 'debit';

    return (
        <svg
            viewBox="0 0 540 200"
            className="w-full max-w-[540px] h-auto block bg-white rounded-lg border-2 border-emerald-500 font-sans shadow-xs"
            data-testid="source-doc-bank-statement"
        >
            {/* Header */}
            <rect x="0" y="0" width="540" height="34" fill="#065f46" />
            <text x="18" y="22" fontSize="13" fontWeight="800" fill="#ffffff" letterSpacing="0.8">
                {bankName.toUpperCase()}
            </text>
            <text x="522" y="22" textAnchor="end" fontSize="10.5" fontWeight="700" fill="#a7f3d0">
                OFFICIAL STATEMENT EXCERPT
            </text>

            <text x="20" y="54" fontSize="10" fill="#475569">Account:</text>
            <text x="80" y="54" fontSize="11" fontWeight="700" fill="#0f172a">{accountName}</text>
            <text x="350" y="54" fontSize="10" fill="#475569">Statement Date:</text>
            <text x="445" y="54" fontSize="11" fontWeight="700" fill="#0f172a">{date}</text>

            {/* Table Header */}
            <rect x="20" y="68" width="500" height="24" fill="#f1f5f9" stroke="#cbd5e1" strokeWidth="1" />
            <text x="30" y="84" fontSize="9.5" fontWeight="700" fill="#475569">DATE</text>
            <text x="100" y="84" fontSize="9.5" fontWeight="700" fill="#475569">TRANSACTION DETAILS</text>
            <text x="360" y="84" textAnchor="end" fontSize="9.5" fontWeight="700" fill="#475569">DEBIT (OUT)</text>
            <text x="435" y="84" textAnchor="end" fontSize="9.5" fontWeight="700" fill="#475569">CREDIT (IN)</text>
            <text x="510" y="84" textAnchor="end" fontSize="9.5" fontWeight="700" fill="#475569">BALANCE</text>

            {/* Table Row */}
            <rect x="20" y="92" width="500" height="36" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />
            <text x="30" y="114" fontSize="10.5" fill="#334155" fontFamily="monospace">{date.split(' ')[0]} {date.split(' ')[1].slice(0, 3)}</text>
            <text x="100" y="114" fontSize="10.5" fontWeight="600" fill="#0f172a">{description}</text>

            <text x="360" y="114" textAnchor="end" fontSize="11" fontWeight="700" fill={isDebit ? '#dc2626' : '#64748b'} fontFamily="monospace">
                {isDebit ? `R ${amount.toLocaleString()}.00` : '-'}
            </text>
            <text x="435" y="114" textAnchor="end" fontSize="11" fontWeight="700" fill={!isDebit ? '#059669' : '#64748b'} fontFamily="monospace">
                {!isDebit ? `R ${amount.toLocaleString()}.00` : '-'}
            </text>
            <text x="510" y="114" textAnchor="end" fontSize="11" fontWeight="700" fill="#0f172a" fontFamily="monospace">
                R 38,420.00
            </text>

            <rect x="20" y="136" width="500" height="28" fill="#f8fafc" stroke="#cbd5e1" strokeWidth="1" />
            <text x="30" y="154" fontSize="9.5" fill="#334155">
                PASA Interbank Electronic Settlement Reference: <tspan fontWeight="700" fontFamily="monospace">ZA-EFT-9482103</tspan>
            </text>

            <text x="20" y="186" fontSize="9" fill="#64748b" fontStyle="italic">
                Direct bank charges appear on the bank statement and must be recorded in the Cash Payments Journal (CPJ).
            </text>
        </svg>
    );
}

function CashRegisterTapePlate({ spec }) {
    const businessName = spec.business_name || 'Service Enterprise';
    const date = spec.date || '18 June 2024';
    const docNo = spec.crr_number || 'CRR 01';
    const amount = Number(spec.amount || 650);

    return (
        <svg
            viewBox="0 0 540 210"
            className="w-full max-w-[540px] h-auto block bg-slate-100 rounded-lg border-2 border-slate-400 font-sans shadow-xs"
            data-testid="source-doc-cash-register-tape"
        >
            {/* Center Slip (White Paper Tape) */}
            <g transform="translate(145, 10)">
                <rect x="0" y="0" width="250" height="190" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />

                <text x="125" y="24" textAnchor="middle" fontSize="11" fontWeight="800" fill="#0f172a">
                    {businessName.toUpperCase()}
                </text>
                <text x="125" y="38" textAnchor="middle" fontSize="9" fill="#475569">
                    CASH REGISTER TILL ROLL
                </text>
                <text x="125" y="52" textAnchor="middle" fontSize="9.5" fontWeight="700" fill="#334155" fontFamily="monospace">
                    {docNo} • {date}
                </text>

                <line x1="15" y1="60" x2="235" y2="60" stroke="#0f172a" strokeWidth="1" strokeDasharray="3,2" />

                <text x="20" y="80" fontSize="10" fill="#334155">Service Rendered</text>
                <text x="230" y="80" textAnchor="end" fontSize="10.5" fontWeight="700" fill="#0f172a" fontFamily="monospace">
                    R {amount.toLocaleString()}.00
                </text>

                <line x1="15" y1="105" x2="235" y2="105" stroke="#cbd5e1" strokeWidth="1" />

                <text x="20" y="125" fontSize="11" fontWeight="800" fill="#0f172a">TOTAL CASH:</text>
                <text x="230" y="125" textAnchor="end" fontSize="13" fontWeight="900" fill="#0f172a" fontFamily="monospace">
                    R {amount.toLocaleString()}.00
                </text>

                <line x1="15" y1="140" x2="235" y2="140" stroke="#0f172a" strokeWidth="1" strokeDasharray="3,2" />

                <text x="125" y="160" textAnchor="middle" fontSize="8.5" fill="#475569">
                    THANK YOU FOR YOUR SUPPORT
                </text>
                <text x="125" y="174" textAnchor="middle" fontSize="7.5" fill="#94a3b8">
                    South African Tax Invoice / Till Slip
                </text>
            </g>

            {/* Left/Right Guidance Notes */}
            <text x="30" y="105" fontSize="10" fontWeight="700" fill="#1e3a8a">
                CRR Source Document
            </text>
            <text x="30" y="120" fontSize="8.5" fill="#64748b">
                Proof of daily cash sales
            </text>
            <text x="30" y="132" fontSize="8.5" fill="#64748b">
                recorded in CRJ Analysis
            </text>

            <text x="420" y="105" fontSize="10" fontWeight="700" fill="#1e3a8a">
                CRJ Routing
            </text>
            <text x="420" y="120" fontSize="8.5" fill="#64748b">
                Credit: Current Income
            </text>
            <text x="420" y="132" fontSize="8.5" fill="#64748b">
                Debit: Bank
            </text>
        </svg>
    );
}
