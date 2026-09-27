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

    const questionsHtml = questions.map((q, idx) => `
      <div style="margin-bottom: 24px; page-break-inside: avoid;">
        <div style="display: flex; justify-content: space-between; font-weight: bold; border-bottom: 1px solid #cbd5e0; padding-bottom: 4px; margin-bottom: 8px;">
          <span>QUESTION ${idx + 1}</span>
          <span>[${q.marks || 5} marks]</span>
        </div>
        <p style="margin: 0 0 12px 0;">${q.question_text || q.text || 'Solve the following problem.'}</p>
        <div style="border: 1px solid #e2e8f0; border-radius: 4px; padding: 10px; min-height: 120px;">
          <div style="font-size: 8pt; color: #a0aec0; margin-bottom: 8px;">Working Space:</div>
          <div style="border-bottom: 1px dashed #edf2f7; height: 26px;"></div>
          <div style="border-bottom: 1px dashed #edf2f7; height: 26px;"></div>
          <div style="border-bottom: 1px dashed #edf2f7; height: 26px;"></div>
        </div>
      </div>
    `).join('');

    const memoHtml = questions.map((q, idx) => {
      const scheme = q.marking_scheme || [{ point: 'Correct final calculated value with method', marks: q.marks || 5 }];
      const schemeRows = scheme.map(mp => `
        <tr>
          <td style="border: 1px solid #cbd5e0; padding: 6px 8px;">${mp.point || mp.desc}</td>
          <td style="border: 1px solid #cbd5e0; padding: 6px 8px; color: #2b6cb0; font-weight: bold;">✓ (${mp.marks || 1}M/A)</td>
          <td style="border: 1px solid #cbd5e0; padding: 6px 8px; text-align: right; font-weight: bold;">${mp.marks || 1}</td>
        </tr>
      `).join('');

      return `
        <div style="margin-bottom: 20px; padding: 12px; border: 1px solid #cbd5e0; border-radius: 6px; background: #f7fafc; page-break-inside: avoid;">
          <div style="display: flex; justify-content: space-between; font-weight: bold; color: #2b6cb0; margin-bottom: 8px;">
            <span>QUESTION ${idx + 1} MEMORANDUM</span>
            <span>[${q.marks || 5} marks]</span>
          </div>
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

    const docHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>${testTitle} - ${subject} Gr ${grade}</title>
        <style>
          @page { size: A4; margin: 18mm; }
          body { font-family: 'Segoe UI', Tahoma, sans-serif; color: #1a202c; line-height: 1.5; margin: 0; padding: 0; }
          .page-break { page-break-before: always; break-before: page; }
        </style>
      </head>
      <body>
        <div style="border-bottom: 2px solid #2d3748; padding-bottom: 10px; margin-bottom: 16px; text-align: center;">
          <div style="font-size: 16pt; font-weight: bold; text-transform: uppercase;">FUNDILE CURRICULUM ASSESSMENT</div>
          <div style="font-size: 12pt; color: #4a5568; font-weight: 600;">${testTitle}</div>
          <div style="display: flex; justify-content: space-around; margin-top: 10px; padding: 6px; background: #edf2f7; font-size: 9pt; font-weight: bold; border-radius: 4px;">
            <div>Subject: ${subject}</div>
            <div>Grade: ${grade}</div>
            <div>Term: ${term}</div>
            <div>Marks: ${totalMarks} | Time: ${durationMins}m</div>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-bottom: 16px; font-size: 10pt;">
          <div style="border-bottom: 1px dotted #4a5568; width: 60%;">Learner Name: </div>
          <div style="border-bottom: 1px dotted #4a5568; width: 30%;">Date: </div>
        </div>

        ${questionsHtml}

        <div class="page-break"></div>

        <div style="background: #2b6cb0; color: #fff; text-align: center; padding: 10px; font-size: 13pt; font-weight: bold; margin-bottom: 16px; border-radius: 4px;">
          TEACHER MARKING MEMORANDUM — CONFIDENTIAL
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
              <p className="text-xs text-slate-400">
                {subject} • Grade {grade} • Term {term} • {totalMarks} Marks • {durationMins} mins
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={handlePrint}
              className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-xs transition-colors flex items-center gap-1.5 shadow-lg shadow-blue-900/30"
            >
              <Printer className="w-4 h-4" />
              <span>Print / Save PDF</span>
            </button>
            <button
              onClick={onClose}
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
              <div className="space-y-6">
                <div className="grid grid-cols-2 gap-4 pb-2 text-[11px] text-slate-600 border-b border-dotted border-slate-400">
                  <div>Learner Name: __________________________</div>
                  <div>Date: ____________________</div>
                </div>

                {questions.map((q, idx) => (
                  <div key={idx} className="space-y-2">
                    <div className="flex justify-between font-bold text-slate-800 border-b border-slate-200 pb-1">
                      <span>QUESTION {idx + 1}</span>
                      <span>[{q.marks || 5} marks]</span>
                    </div>
                    <p className="text-slate-700 leading-relaxed font-serif text-sm">
                      {q.question_text || q.text || 'Solve the following equation and justify each step.'}
                    </p>
                    <div className="border border-slate-200 rounded p-3 min-h-[90px] bg-slate-50/50">
                      <div className="text-[10px] text-slate-400 mb-2">Working Space:</div>
                      <div className="border-b border-dashed border-slate-200 h-6"></div>
                      <div className="border-b border-dashed border-slate-200 h-6"></div>
                    </div>
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
            className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition-colors"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
