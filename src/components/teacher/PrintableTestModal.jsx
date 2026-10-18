import React, { useState } from 'react';
import { Printer, Copy, Check, X, FileText, CheckCircle2 } from 'lucide-react';

export default function PrintableTestModal({
  isOpen = false,
  onClose,
  testTitle = 'Classroom Diagnostic Assessment',
  subject = 'Mathematics',
  grade = '10',
  term = 1,
  durationMins = 45,
  questions = []
}) {
  const [activeTab, setActiveTab] = useState('paper'); // 'paper' | 'memo'
  const [copied, setCopied] = useState(false);

  if (!isOpen) return null;

  const totalMarks = questions.reduce((sum, q) => {
    const marks = q.marks || (q.marking_scheme ? q.marking_scheme.reduce((s, p) => s + (p.marks || 1), 0) : 5);
    return sum + marks;
  }, 0) || 30;

  const handlePrint = () => {
    const printWindow = window.open('', '_blank');
    if (!printWindow) {
      alert('Please allow popups to generate the printable test document.');
      return;
    }

    const questionsHtml = questions.map((q, idx) => {
      const optionsBlock = (q.options && q.options.length > 0)
        ? `<div style="margin: 8px 0 14px 8px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            ${q.options.map((opt, oIdx) => `
              <div style="padding: 6px 10px; border: 1px solid #e2e8f0; border-radius: 4px; font-size: 9.5pt; background: #fff;">
                <strong>${String.fromCharCode(65 + oIdx)}.</strong> ${opt}
              </div>
            `).join('')}
          </div>`
        : '';

      const workingBox = (q.options && q.options.length > 0)
        ? `<div style="border: 1px dashed #cbd5e0; border-radius: 4px; padding: 6px 12px; font-size: 9pt; color: #4a5568; background: #f7fafc; margin-top: 6px;">
            Learner Selected Choice: &nbsp; <strong>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</strong>
          </div>`
        : `<div style="border: 1px solid #e2e8f0; border-radius: 4px; padding: 10px; min-height: 120px;">
            <div style="font-size: 8pt; color: #a0aec0; margin-bottom: 8px;">Working Space:</div>
            <div style="border-bottom: 1px dashed #edf2f7; height: 26px;"></div>
            <div style="border-bottom: 1px dashed #edf2f7; height: 26px;"></div>
            <div style="border-bottom: 1px dashed #edf2f7; height: 26px;"></div>
          </div>`;

      return `
        <div style="margin-bottom: 24px; page-break-inside: avoid;">
          <div style="display: flex; justify-content: space-between; font-weight: bold; border-bottom: 1px solid #cbd5e0; padding-bottom: 4px; margin-bottom: 8px;">
            <span>QUESTION ${idx + 1} ${q.question_type === 'mcq' ? '(Diagnostic MCQ)' : ''}</span>
            <span>[${q.marks || 5} marks]</span>
          </div>
          <p style="margin: 0 0 12px 0;">${q.question_text || q.text || 'Solve the following problem.'}</p>
          ${optionsBlock}
          ${workingBox}
        </div>
      `;
    }).join('');

    const memoHtml = questions.map((q, idx) => {
      const scheme = q.marking_scheme || [{ point: 'Correct final calculated value with method', marks: q.marks || 5 }];
      const schemeRows = scheme.map(mp => `
        <tr>
          <td style="border: 1px solid #cbd5e0; padding: 6px 8px;">${mp.point || mp.desc}</td>
          <td style="border: 1px solid #cbd5e0; padding: 6px 8px; color: #2b6cb0; font-weight: bold;">✓ (${mp.marks || 1}M/A)</td>
          <td style="border: 1px solid #cbd5e0; padding: 6px 8px; text-align: right; font-weight: bold;">${mp.marks || 1}</td>
        </tr>
      `).join('');

      const correctKeyText = (q.options && q.options.length > 0)
        ? `<div style="margin-bottom: 6px; color: #276749; font-weight: bold; font-size: 9pt;">
            Key: Option ${String.fromCharCode(65 + (parseInt(q.correct_index, 10) || 0))}
          </div>`
        : '';

      return `
        <div style="margin-bottom: 20px; padding: 12px; border: 1px solid #cbd5e0; border-radius: 6px; background: #f7fafc; page-break-inside: avoid;">
          <div style="display: flex; justify-content: space-between; font-weight: bold; color: #2b6cb0; margin-bottom: 8px;">
            <span>QUESTION ${idx + 1} MEMORANDUM</span>
            <span>[${q.marks || 5} marks]</span>
          </div>
          ${correctKeyText}
          <div style="margin-bottom: 8px;"><strong>Worked Solution:</strong> ${q.solution || 'Follow canonical procedure.'}</div>
          <table style="width: 100%; border-collapse: collapse; font-size: 9.5pt; background: #fff;">
            <thead>
              <tr style="background: #edf2f7;">
                <th style="border: 1px solid #cbd5e0; padding: 6px 8px; text-align: left;">Marking Criteria</th>
                <th style="border: 1px solid #cbd5e0; padding: 6px 8px; text-align: left; width: 90px;">Tick Type</th>
                <th style="border: 1px solid #cbd5e0; padding: 6px 8px; text-align: right; width: 50px;">Marks</th>
              </tr>
            </thead>
            <tbody>
              ${schemeRows}
            </tbody>
          </table>
        </div>
      `;
    }).join('');

    const instructionsHtml = `
      <div style="border: 1px solid #cbd5e0; background: #f8fafc; border-radius: 6px; padding: 10px 14px; margin-bottom: 20px; font-size: 8.5pt; color: #334155; line-height: 1.45;">
        <div style="font-weight: bold; text-transform: uppercase; margin-bottom: 4px; color: #1e293b; letter-spacing: 0.5px;">INSTRUCTIONS AND INFORMATION</div>
        <ol style="margin: 0; padding-left: 18px;">
          <li>This question paper consists of <strong>${questions.length}</strong> questions.</li>
          <li>Answer <strong>ALL</strong> the questions in the designated spaces provided.</li>
          <li>Clearly show <strong>ALL</strong> calculations, diagrams, and formulas used in determining your answers.</li>
          <li>Answers only will <strong>NOT</strong> necessarily be awarded full marks.</li>
          <li>An approved scientific calculator (non-programmable and non-graphical) may be used unless stated otherwise.</li>
          <li>Round off final numerical answers to <strong>TWO</strong> decimal places unless stated otherwise.</li>
          <li>Write neatly and legibly.</li>
        </ol>
      </div>
    `;

    const docHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>${testTitle} - ${subject} Gr ${grade}</title>
        <style>
          @page { size: A4; margin: 18mm; }
          body { font-family: 'Segoe UI', Tahoma, Helvetica, sans-serif; color: #1a202c; line-height: 1.5; margin: 0; padding: 0; }
          .page-break { page-break-before: always; break-before: page; }
        </style>
      </head>
      <body>
        <div style="border-bottom: 2px solid #1e293b; padding-bottom: 8px; margin-bottom: 14px; text-align: center;">
          <div style="font-size: 14pt; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">CURRICULUM ASSESSMENT</div>
          <div style="font-size: 11pt; color: #334155; font-weight: 600;">${testTitle}</div>
          <div style="display: flex; justify-content: space-around; margin-top: 8px; padding: 6px 12px; background: #f1f5f9; font-size: 8.5pt; font-weight: bold; border-radius: 4px; border: 1px solid #e2e8f0;">
            <div>Subject: ${subject}</div>
            <div>Grade: ${grade}</div>
            <div>Term: ${term}</div>
            <div>Marks: ${totalMarks} | Time: ${durationMins} min</div>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 12px; margin-bottom: 16px; font-size: 9pt;">
          <div style="border-bottom: 1px dotted #64748b; padding-bottom: 2px;">Learner Name: </div>
          <div style="border-bottom: 1px dotted #64748b; padding-bottom: 2px;">Class: Grade ${grade}___</div>
          <div style="border-bottom: 1px dotted #64748b; padding-bottom: 2px;">Date: ____________</div>
        </div>

        ${instructionsHtml}

        ${questionsHtml}

        <div class="page-break"></div>

        <div style="background: #1e3a8a; color: #fff; text-align: center; padding: 8px; font-size: 11pt; font-weight: 800; margin-bottom: 16px; border-radius: 4px; letter-spacing: 0.5px;">
          TEACHER MARKING MEMORANDUM — STRICTLY CONFIDENTIAL
        </div>

        <div style="display: flex; justify-content: space-between; margin-bottom: 14px; font-size: 8.5pt; color: #64748b; border-bottom: 1px solid #cbd5e0; padding-bottom: 4px;">
          <span>Subject: ${subject} Grade ${grade}</span>
          <span>Term ${term} Assessment</span>
          <span>Total: ${totalMarks} Marks</span>
        </div>

        ${memoHtml}

        <script>
          window.onload = function() {
            window.print();
          };
        </script>
      </body>
      </html>
    `;

    printWindow.document.open();
    printWindow.document.write(docHtml);
    printWindow.document.close();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/80 backdrop-blur-md animate-fade-in text-slate-100">
      <div className="bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl max-w-4xl w-full flex flex-col max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-slate-950/60 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-blue-500/20 text-blue-300 flex items-center justify-center text-xl border border-blue-500/30">
              <FileText className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-100">{testTitle}</h3>
              <div className="flex items-center gap-2 flex-wrap">
                <p className="text-xs text-slate-400">
                  {subject} • Grade {grade} • Term {term} • {totalMarks} Marks • {durationMins} mins
                </p>
                {term === 1 && (
                  <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-blue-500/20 text-blue-300 text-[10px] font-semibold border border-blue-400/30">
                    🏛️ Provincial March Common Scope
                  </span>
                )}
              </div>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrint}
              data-testid="btn-print-save-pdf"
              className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs transition-colors flex items-center gap-1.5 shadow-lg shadow-blue-900/30"
            >
              <Printer className="w-4 h-4" />
              <span>Print / Save PDF</span>
            </button>
            <button
              onClick={onClose}
              data-testid="btn-close-printable-test-x"
              className="p-1.5 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Tab Toggle */}
        <div className="flex items-center gap-2 px-6 pt-3 pb-2 border-b border-slate-800 bg-slate-950/30 text-xs">
          <button
            onClick={() => setActiveTab('paper')}
            data-testid="tab-learner-paper"
            className={`px-4 py-1.5 rounded-lg font-medium transition-colors ${
              activeTab === 'paper'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
            }`}
          >
            📄 Learner Question Paper
          </button>
          <button
            onClick={() => setActiveTab('memo')}
            data-testid="tab-marking-memo"
            className={`px-4 py-1.5 rounded-lg font-medium transition-colors ${
              activeTab === 'memo'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
            }`}
          >
            📝 Teacher Marking Memorandum
          </button>
        </div>

        {/* Document Preview Stage */}
        <div className="p-6 overflow-y-auto flex-1 bg-slate-950/80">
          <div className="max-w-3xl mx-auto bg-white text-slate-900 p-8 rounded-xl shadow-xl font-sans text-xs">
            {/* Paper Header */}
            <div className="border-b-2 border-slate-800 pb-3 mb-4 text-center">
              <div className="text-sm font-bold uppercase tracking-wider text-slate-900">
                FUNDILE CURRICULUM ASSESSMENT
              </div>
              <div className="text-base font-bold text-slate-700 mt-1">{testTitle}</div>
              <div className="grid grid-cols-4 gap-2 mt-3 p-2 bg-slate-100 rounded text-[11px] font-semibold text-slate-700">
                <div>Subject: {subject}</div>
                <div>Grade: {grade}</div>
                <div>Term: {term}</div>
                <div>Marks: {totalMarks}</div>
              </div>
            </div>

            {activeTab === 'paper' ? (
              <div className="space-y-5">
                <div className="grid grid-cols-3 gap-3 pb-2 text-[11px] text-slate-600 border-b border-dotted border-slate-400">
                  <div>Learner Name: ____________________</div>
                  <div>Class: Grade {grade}___</div>
                  <div>Date: ____________</div>
                </div>

                {/* Instructions and Information */}
                <div className="border border-slate-200 bg-slate-50/80 rounded-lg p-3 text-[11px] text-slate-700 leading-relaxed space-y-1">
                  <div className="font-bold uppercase tracking-wider text-slate-900 text-[10px]">
                    Instructions and Information
                  </div>
                  <ol className="list-decimal pl-4 space-y-0.5 text-[10.5px]">
                    <li>This question paper consists of <strong>{questions.length}</strong> questions.</li>
                    <li>Answer <strong>ALL</strong> questions in the designated spaces.</li>
                    <li>Clearly show <strong>ALL</strong> calculations and intermediate steps where applicable.</li>
                    <li>Answers only will <strong>NOT</strong> necessarily be awarded full marks.</li>
                    <li>Round off numerical answers to <strong>TWO</strong> decimal places unless stated otherwise.</li>
                    <li>Write neatly and legibly.</li>
                  </ol>
                </div>

                {questions.map((q, idx) => (
                  <div key={idx} className="space-y-2 pt-1">
                    <div className="flex justify-between font-bold text-slate-800 border-b border-slate-200 pb-1">
                      <span>QUESTION {idx + 1} {q.question_type === 'mcq' ? '(Diagnostic MCQ)' : ''}</span>
                      <span>[{q.marks || 5} marks]</span>
                    </div>
                    <p className="text-slate-800 leading-relaxed font-serif text-xs">
                      {q.question_text || q.text || 'Solve the following problem.'}
                    </p>

                    {/* MCQ Options Display */}
                    {q.options && q.options.length > 0 ? (
                      <div className="space-y-2">
                        <div className="grid grid-cols-2 gap-2 my-2">
                          {q.options.map((opt, oIdx) => (
                            <div key={oIdx} className="p-2 border border-slate-200 rounded text-xs bg-slate-50/60 font-sans">
                              <strong>{String.fromCharCode(65 + oIdx)}.</strong> {opt}
                            </div>
                          ))}
                        </div>
                        <div className="border border-dashed border-slate-300 rounded p-2 text-[11px] text-slate-600 bg-slate-50">
                          Learner Selected Choice: &nbsp; <strong>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</strong>
                        </div>
                      </div>
                    ) : (
                      <div className="border border-slate-200 rounded p-3 min-h-[90px] bg-slate-50/50">
                        <div className="text-[10px] text-slate-400 mb-2">Working Space:</div>
                        <div className="border-b border-dashed border-slate-200 h-6"></div>
                        <div className="border-b border-dashed border-slate-200 h-6"></div>
                        <div className="border-b border-dashed border-slate-200 h-6"></div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              <div className="space-y-6">
                <div className="bg-blue-700 text-white font-bold p-2.5 rounded text-center text-sm uppercase tracking-wide">
                  Teacher Marking Memorandum — Confidential
                </div>

                {questions.map((q, idx) => (
                  <div key={idx} className="p-4 bg-slate-50 rounded-lg border border-slate-200 space-y-3">
                    <div className="flex justify-between font-bold text-blue-800 border-b border-slate-200 pb-1">
                      <span>QUESTION {idx + 1} MEMORANDUM</span>
                      <span>[{q.marks || 5} marks]</span>
                    </div>
                    <div className="text-slate-700">
                      <strong>Worked Solution:</strong> {q.solution || 'Full canonical algebraic solution.'}
                    </div>
                    <table className="w-full border-collapse text-[11px]">
                      <thead>
                        <tr className="bg-slate-200 text-slate-800">
                          <th className="border border-slate-300 p-1.5 text-left">Marking Point</th>
                          <th className="border border-slate-300 p-1.5 text-left w-24">Tick</th>
                          <th className="border border-slate-300 p-1.5 text-right w-16">Marks</th>
                        </tr>
                      </thead>
                      <tbody>
                        {(q.marking_scheme || [{ point: 'Correct method and final substitution', marks: q.marks || 5 }]).map((mp, pIdx) => (
                          <tr key={pIdx} className="bg-white">
                            <td className="border border-slate-300 p-1.5 text-slate-700">{mp.point || mp.desc}</td>
                            <td className="border border-slate-300 p-1.5 text-blue-700 font-bold">✓ ({mp.marks || 1}M/A)</td>
                            <td className="border border-slate-300 p-1.5 text-right font-bold text-slate-800">{mp.marks || 1}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 bg-slate-950/80 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
          <span>Formatted for standard A4 duplex printing with automatic page break separation.</span>
          <button
            onClick={onClose}
            data-testid="btn-close-printable-test"
            className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition-colors"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
