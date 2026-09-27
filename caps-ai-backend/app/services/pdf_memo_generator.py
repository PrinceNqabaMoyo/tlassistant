"""
Teacher Printable PDF Test & Marking Memo Engine (Layer D)
Generates authentic South African CAPS-aligned printable test papers and marking memorandums.
Produces clean HTML/CSS formatted documents with page breaks, mark allocations, method ticks,
and teacher rubric notes.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


def generate_printable_html(
    school_name: str,
    subject: str,
    grade: str,
    term: int,
    test_title: str,
    duration_mins: int,
    total_marks: int,
    questions: List[Dict[str, Any]]
) -> str:
    """
    Generates a complete standalone printable HTML document with two distinct sections:
    1. Section A: Learner Question Paper (with answer lines and tables)
    2. Section B: Teacher Marking Memorandum (with method ticks, accuracy ticks, and rubrics)
    """
    date_str = datetime.now().strftime("%B %Y")
    
    # Generate Questions HTML
    questions_html = ""
    for idx, q in enumerate(questions, start=1):
        q_text = q.get("question_text", "")
        q_marks = q.get("marks", 0)
        q_schema = q.get("marking_schema", {})
        if not q_marks and "marking_points" in q_schema:
            q_marks = sum(mp.get("marks", 1) for mp in q_schema["marking_points"])
        
        questions_html += f"""
        <div class="question-block">
            <div class="question-header">
                <span class="question-num">QUESTION {idx}</span>
                <span class="question-marks">[{q_marks} marks]</span>
            </div>
            <div class="question-body">
                <p>{q_text}</p>
            </div>
            <div class="working-space">
                <div class="space-label">Working Space:</div>
                <div class="ruled-lines">
                    <div class="line"></div>
                    <div class="line"></div>
                    <div class="line"></div>
                    <div class="line"></div>
                </div>
            </div>
        </div>
        """

    # Generate Memorandum HTML
    memo_html = ""
    for idx, q in enumerate(questions, start=1):
        q_marks = q.get("marks", 0)
        q_solution = q.get("solution", "See marking points below.")
        q_schema = q.get("marking_schema", {})
        marking_points = q_schema.get("marking_points", [])
        
        mp_rows = ""
        for mp in marking_points:
            mp_desc = mp.get("desc", mp.get("point", ""))
            mp_mark = mp.get("marks", 1)
            mp_rows += f"""
            <tr>
                <td class="mp-desc">{mp_desc}</td>
                <td class="mp-tick">✓ ({mp_mark}M/A)</td>
                <td class="mp-marks">{mp_mark}</td>
            </tr>
            """
            
        memo_html += f"""
        <div class="memo-block">
            <div class="memo-header">
                <span class="memo-num">QUESTION {idx} MEMORANDUM</span>
                <span class="memo-marks">[{q_marks} marks]</span>
            </div>
            <div class="memo-solution">
                <strong>Worked Solution:</strong>
                <p>{q_solution}</p>
            </div>
            {f'''
            <table class="memo-table">
                <thead>
                    <tr>
                        <th>Marking Criteria / Step</th>
                        <th>Tick Type</th>
                        <th>Marks</th>
                    </tr>
                </thead>
                <tbody>
                    {mp_rows}
                </tbody>
            </table>
            ''' if marking_points else ''}
            <div class="memo-note">
                <em>* Consequential marking applies: award method marks if learner followed correct procedure with carried-over calculation error.</em>
            </div>
        </div>
        """

    # Assemble complete HTML template
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{test_title} - {subject} Grade {grade}</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #1a202c;
            background: #fff;
            line-height: 1.5;
            margin: 0;
            padding: 0;
        }}
        .page-header {{
            border-bottom: 2px solid #2d3748;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }}
        .school-title {{
            font-size: 18pt;
            font-weight: bold;
            text-transform: uppercase;
            text-align: center;
            margin-bottom: 4px;
        }}
        .exam-title {{
            font-size: 14pt;
            font-weight: 600;
            text-align: center;
            color: #4a5568;
        }}
        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
            margin-top: 15px;
            padding: 8px;
            background: #edf2f7;
            font-size: 10pt;
            font-weight: 600;
            border-radius: 4px;
        }}
        .student-fields {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 15px;
            margin: 15px 0;
            font-size: 11pt;
        }}
        .field-box {{
            border-bottom: 1px dotted #4a5568;
            padding-bottom: 2px;
        }}
        .instructions {{
            background: #fffaf0;
            border-left: 4px solid #dd6b20;
            padding: 10px;
            font-size: 9.5pt;
            margin-bottom: 25px;
        }}
        .question-block {{
            margin-bottom: 30px;
            page-break-inside: avoid;
        }}
        .question-header {{
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            font-size: 11pt;
            border-bottom: 1px solid #cbd5e0;
            padding-bottom: 4px;
            margin-bottom: 8px;
        }}
        .working-space {{
            margin-top: 12px;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            padding: 8px;
            min-height: 120px;
        }}
        .space-label {{
            font-size: 8.5pt;
            color: #a0aec0;
            margin-bottom: 8px;
        }}
        .ruled-lines .line {{
            border-bottom: 1px dashed #edf2f7;
            height: 24px;
        }}
        .page-break {{
            page-break-before: always;
            break-before: page;
        }}
        .memo-banner {{
            background: #2b6cb0;
            color: #fff;
            text-align: center;
            padding: 12px;
            font-size: 14pt;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 20px;
            border-radius: 4px;
        }}
        .memo-block {{
            margin-bottom: 25px;
            padding: 12px;
            border: 1px solid #cbd5e0;
            border-radius: 6px;
            background: #f7fafc;
            page-break-inside: avoid;
        }}
        .memo-header {{
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            font-size: 11pt;
            color: #2b6cb0;
            margin-bottom: 8px;
        }}
        .memo-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 9.5pt;
            margin: 10px 0;
            background: #fff;
        }}
        .memo-table th, .memo-table td {{
            border: 1px solid #cbd5e0;
            padding: 6px 8px;
            text-align: left;
        }}
        .memo-table th {{
            background: #edf2f7;
            font-weight: 600;
        }}
        .mp-tick {{
            color: #2b6cb0;
            font-weight: bold;
            width: 90px;
        }}
        .mp-marks {{
            width: 50px;
            text-align: right;
            font-weight: bold;
        }}
        .memo-note {{
            font-size: 8.5pt;
            color: #718096;
            margin-top: 6px;
        }}
        @media print {{
            .no-print {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <!-- SECTION 1: QUESTION PAPER -->
    <div class="page-header">
        <div class="school-title">{school_name}</div>
        <div class="exam-title">{test_title}</div>
        <div class="meta-grid">
            <div>Subject: {subject}</div>
            <div>Grade: {grade}</div>
            <div>Term: {term}</div>
            <div>Marks: {total_marks} | Time: {duration_mins} mins</div>
        </div>
    </div>

    <div class="student-fields">
        <div class="field-box">Learner Name & Surname: </div>
        <div class="field-box">Date: {date_str}</div>
    </div>

    <div class="instructions">
        <strong>INSTRUCTIONS AND INFORMATION:</strong>
        <ol style="margin: 4px 0 0 16px; padding: 0;">
            <li>Answer ALL questions in the spaces provided.</li>
            <li>Clearly show ALL calculations, diagrams, and formulas where applicable.</li>
            <li>Units must be indicated where required. Round off answers to TWO decimal places unless stated otherwise.</li>
        </ol>
    </div>

    {questions_html}

    <!-- SECTION 2: MARKING MEMORANDUM (NEW PAGE) -->
    <div class="page-break"></div>
    <div class="memo-banner">
        TEACHER MARKING MEMORANDUM — CONFIDENTIAL
    </div>
    <div class="meta-grid" style="margin-bottom: 20px;">
        <div>Subject: {subject}</div>
        <div>Grade: {grade}</div>
        <div>Term: {term}</div>
        <div>Total: {total_marks} Marks</div>
    </div>

    {memo_html}
</body>
</html>
"""
    return html_content
