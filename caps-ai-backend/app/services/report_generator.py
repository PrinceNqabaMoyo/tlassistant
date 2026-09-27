"""
Diagnostic Progress Report Engine (Phase D3)
Generates authentic South African CAPS-aligned diagnostic progress reports for students, parents, and teachers.
Outputs print-optimized A4 HTML reports with visual diagnostic dials, grade level benchmarks (1-7),
misconception triage debriefs, and forward-looking remedial action plans.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


def calculate_caps_level(percentage: float) -> Dict[str, Any]:
    """Maps percentage to official South African CAPS achievement levels (1 to 7)."""
    if percentage >= 80:
        return {"level": 7, "rating": "Outstanding Achievement", "color": "#22c55e"}
    elif percentage >= 70:
        return {"level": 6, "rating": "Meritorious Achievement", "color": "#10b981"}
    elif percentage >= 60:
        return {"level": 5, "rating": "Substantial Achievement", "color": "#3b82f6"}
    elif percentage >= 50:
        return {"level": 4, "rating": "Adequate Achievement", "color": "#f59e0b"}
    elif percentage >= 40:
        return {"level": 3, "rating": "Moderate Achievement", "color": "#ea580c"}
    elif percentage >= 30:
        return {"level": 2, "rating": "Elementary Achievement", "color": "#ef4444"}
    else:
        return {"level": 1, "rating": "Not Achieved", "color": "#dc2626"}


def generate_parent_report_html(
    student_name: str,
    grade: str,
    report_period: str,
    subject_mastery: Dict[str, float],
    streak_days: int,
    total_xp: int,
    earned_badges: List[Dict[str, Any]],
    diagnosed_misconceptions: List[Dict[str, Any]],
    tutor_feedback: Optional[str] = None
) -> str:
    """
    Generates a complete standalone printable A4 HTML progress report.
    """
    date_str = datetime.now().strftime("%d %B %Y")
    avg_score = sum(subject_mastery.values()) / max(1, len(subject_mastery))
    caps_band = calculate_caps_level(avg_score)

    # Subject Mastery Breakdown rows
    subject_rows = ""
    for subj, score in subject_mastery.items():
        band = calculate_caps_level(score)
        subject_rows += f"""
        <tr>
            <td style="font-weight: 600; padding: 10px; border-bottom: 1px solid #e2e8f0;">{subj}</td>
            <td style="text-align: center; font-family: monospace; font-weight: bold; padding: 10px; border-bottom: 1px solid #e2e8f0;">{round(score)}%</td>
            <td style="text-align: center; padding: 10px; border-bottom: 1px solid #e2e8f0;">
                <span style="background: {band['color']}20; color: {band['color']}; padding: 3px 8px; border-radius: 9999px; font-weight: bold; font-size: 8.5pt;">
                    Level {band['level']} • {band['rating']}
                </span>
            </td>
        </tr>
        """

    # Misconceptions Triage Cards
    misconception_cards = ""
    if diagnosed_misconceptions:
        for m in diagnosed_misconceptions:
            tag = m.get("tag", "conceptual_barrier")
            label = m.get("label", "Concept Confusion")
            subject = m.get("subject", "General")
            lost_marks = m.get("marks_lost", 5)
            remedial = m.get("remedial_action", "Review foundational prerequisite rules.")
            misconception_cards += f"""
            <div style="background: #fff5f5; border-left: 4px solid #f87171; padding: 12px; margin-bottom: 10px; border-radius: 4px;">
                <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 10pt; color: #991b1b; margin-bottom: 4px;">
                    <span>{subject}: {label}</span>
                    <span>~{lost_marks} Marks Lost/Exam</span>
                </div>
                <div style="font-size: 9pt; color: #4b5563;">
                    <strong>Recommended Action:</strong> {remedial}
                </div>
            </div>
            """
    else:
        misconception_cards = "<p style='color: #10b981; font-weight: 600;'>No systemic conceptual bottlenecks identified across recent sessions.</p>"

    feedback_text = tutor_feedback or (
        f"{student_name} demonstrates consistent academic commitment with a {streak_days}-day study streak. "
        f"Mastery across core subjects averages {round(avg_score)}% (CAPS Level {caps_band['level']}). "
        f"Prioritizing the targeted remedial micro-drills above will optimize performance for upcoming term examinations."
    )

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fundile Academic Progress Report - {student_name}</title>
    <style>
        @page {{
            size: A4;
            margin: 18mm;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #1e293b;
            line-height: 1.5;
            background: #fff;
            margin: 0;
            padding: 0;
        }}
        .report-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #0f172a;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }}
        .logo-text {{
            font-size: 20pt;
            font-weight: 900;
            letter-spacing: -0.5px;
            color: #4338ca;
        }}
        .report-title {{
            font-size: 13pt;
            font-weight: 700;
            color: #475569;
        }}
        .student-hero {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 24px;
            text-align: center;
        }}
        .hero-metric {{
            font-size: 16pt;
            font-weight: 800;
            font-family: monospace;
            color: #0f172a;
        }}
        .hero-label {{
            font-size: 8.5pt;
            text-transform: uppercase;
            color: #64748b;
            font-weight: 600;
        }}
        .section-title {{
            font-size: 12pt;
            font-weight: 800;
            color: #0f172a;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 6px;
            margin-bottom: 12px;
            margin-top: 20px;
        }}
        .mastery-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 9.5pt;
            margin-bottom: 20px;
        }}
        .mastery-table th {{
            background: #f1f5f9;
            padding: 8px 10px;
            text-align: left;
            font-weight: 700;
            border-bottom: 2px solid #cbd5e1;
        }}
        .feedback-box {{
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 8px;
            padding: 14px;
            font-size: 9.5pt;
            color: #166534;
            line-height: 1.6;
        }}
        .footer {{
            margin-top: 30px;
            border-top: 1px solid #e2e8f0;
            padding-top: 10px;
            font-size: 8.5pt;
            color: #94a3b8;
            display: flex;
            justify-content: space-between;
        }}
    </style>
</head>
<body>
    <div class="report-header">
        <div>
            <div class="logo-text">FUNDILE</div>
            <div style="font-size: 9pt; color: #64748b;">Adaptive Learning & Cognitive Diagnostic Engine</div>
        </div>
        <div style="text-align: right;">
            <div class="report-title">Academic Diagnostic Progress Report</div>
            <div style="font-size: 9pt; color: #64748b;">Period: {report_period} • Issued: {date_str}</div>
        </div>
    </div>

    <div class="student-hero">
        <div>
            <div class="hero-label">Learner</div>
            <div class="hero-metric" style="font-family: inherit; font-size: 13pt;">{student_name}</div>
            <div style="font-size: 8.5pt; color: #64748b;">Grade {grade}</div>
        </div>
        <div>
            <div class="hero-label">Curriculum Standing</div>
            <div class="hero-metric" style="color: {caps_band['color']};">Level {caps_band['level']}</div>
            <div style="font-size: 8.5pt; color: {caps_band['color']}; font-weight: bold;">{round(avg_score)}% Overall</div>
        </div>
        <div>
            <div class="hero-label">Ungameable XP</div>
            <div class="hero-metric" style="color: #4338ca;">{total_xp:,}</div>
            <div style="font-size: 8.5pt; color: #64748b;">{len(earned_badges)} Badges Earned</div>
        </div>
        <div>
            <div class="hero-label">Consistency</div>
            <div class="hero-metric" style="color: #d97706;">🔥 {streak_days}d</div>
            <div style="font-size: 8.5pt; color: #64748b;">Active Study Streak</div>
        </div>
    </div>

    <div class="section-title">1. Subject Mastery & CAPS Achievement Ratings</div>
    <table class="mastery-table">
        <thead>
            <tr>
                <th>Subject</th>
                <th style="text-align: center; width: 100px;">Mastery %</th>
                <th style="text-align: center; width: 220px;">Official CAPS Scale</th>
            </tr>
        </thead>
        <tbody>
            {subject_rows}
        </tbody>
    </table>

    <div class="section-title">2. Post-Exam Triage & Conceptual Bottlenecks</div>
    {misconception_cards}

    <div class="section-title">3. Personalized Socratic Tutor Observation</div>
    <div class="feedback-box">
        {feedback_text}
    </div>

    <div class="footer">
        <span>Verified by Fundile Diagnostic Engine • Strictly Aligned with South African Curriculum Standards (CAPS)</span>
        <span>Confidential • For Parent & Guardian Review</span>
    </div>
</body>
</html>
"""
    return html_content
