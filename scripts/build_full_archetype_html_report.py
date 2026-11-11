#!/usr/bin/env python3
"""
scripts/build_full_archetype_html_report.py

Builds interactive HTML galleries and remediation dashboards for the Full Archetype Audit.
Outputs:
  reports/full_archetype_audit/grade_<G>.html
  reports/full_archetype_audit/index.html
"""

import argparse
import html
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = ROOT / "reports" / "full_archetype_audit"


def generate_grade_html(grade: str) -> None:
    ledger_path = AUDIT_DIR / f"ledger_gr{grade}.json"
    if not ledger_path.is_file():
        print(f"Warning: Ledger not found at {ledger_path}", file=sys.stderr)
        return

    data = json.loads(ledger_path.read_text(encoding="utf-8"))
    archetypes = data.get("archetypes", [])
    remediations = data.get("remediations", [])

    total_archs = len(archetypes)
    pass_count = sum(1 for a in archetypes if len(a.get("unresolved_defects", [])) == 0)
    flagged_count = total_archs - pass_count

    total_shots = sum(
        len(a.get("pre_scroll_screenshots", [])) + len(a.get("memo_scroll_screenshots", []))
        for a in archetypes
    )

    subjects = sorted(list(set(a.get("subject", "General") for a in archetypes)))

    cards_html = []
    for idx, a in enumerate(archetypes, 1):
        subj = html.escape(str(a.get("subject", "")))
        topic = html.escape(str(a.get("topic", "")))
        arch_id = html.escape(str(a.get("archetype_id", "")))
        modality = html.escape(str(a.get("modality", "semantic")))
        marks = a.get("marks", 1)
        term = a.get("term", 1)
        defects = a.get("unresolved_defects", [])
        is_pass = len(defects) == 0

        status_badge = (
            '<span class="badge badge-pass">✓ PASS</span>'
            if is_pass
            else f'<span class="badge badge-fail">⚠️ FLAGGED ({len(defects)})</span>'
        )

        # Pre-attempt screenshots
        pre_shots_html = []
        for s_idx, rel_p in enumerate(a.get("pre_scroll_screenshots", []), 1):
            s_name = "Full Stitch" if "full" in rel_p else f"Scroll {s_idx}"
            pre_shots_html.append(f"""
                <div class="shot-card">
                  <a href="../../{rel_p}" target="_blank">
                    <img src="../../{rel_p}" alt="{arch_id} pre {s_idx}" loading="lazy" />
                  </a>
                  <div class="shot-caption">{s_name}</div>
                </div>
            """)

        # Memo screenshots
        memo_shots_html = []
        for s_idx, rel_p in enumerate(a.get("memo_scroll_screenshots", []), 1):
            s_name = "Full Memo Stitch" if "full" in rel_p else f"Memo Scroll {s_idx}"
            memo_shots_html.append(f"""
                <div class="shot-card">
                  <a href="../../{rel_p}" target="_blank">
                    <img src="../../{rel_p}" alt="{arch_id} memo {s_idx}" loading="lazy" />
                  </a>
                  <div class="shot-caption">{s_name}</div>
                </div>
            """)

        defects_html = ""
        if defects:
            items = "".join(f"<li>{html.escape(d)}</li>" for d in defects)
            defects_html = f'<div class="defects-box"><strong>Identified Issues:</strong><ul>{items}</ul></div>'

        cards_html.append(f"""
        <div class="archetype-card" data-subject="{subj}" data-status="{'pass' if is_pass else 'flagged'}">
          <div class="card-header">
            <div class="card-title-group">
              <span class="index-num">#{idx}</span>
              <span class="subj-tag">{subj}</span>
              <span class="topic-tag">Term {term} • {topic}</span>
              <h3 class="arch-title">{arch_id}</h3>
            </div>
            <div class="card-meta">
              <span class="meta-pill">{modality}</span>
              <span class="meta-pill">{marks} Marks</span>
              {status_badge}
            </div>
          </div>

          {defects_html}

          <div class="shots-section">
            <div class="shots-col">
              <div class="shots-header">
                <strong>Pre-Attempt Student UI View (Before Answering)</strong>
                <span class="shots-count">{len(a.get("pre_scroll_screenshots", []))} slice(s)</span>
              </div>
              <div class="shots-grid">
                {"".join(pre_shots_html)}
              </div>
            </div>

            <div class="shots-col">
              <div class="shots-header">
                <strong>Revealed Memorandum & Step-by-Step Procedure View</strong>
                <span class="shots-count">{len(a.get("memo_scroll_screenshots", []))} slice(s)</span>
              </div>
              <div class="shots-grid">
                {"".join(memo_shots_html)}
              </div>
            </div>
          </div>
        </div>
        """)

    remediations_html = ""
    if remediations:
        rem_rows = []
        for r in remediations:
            rem_rows.append(f"""
            <tr>
              <td><code>{html.escape(r.get('archetype_id', ''))}</code></td>
              <td>{html.escape(r.get('description', ''))}</td>
              <td><code>{html.escape(r.get('curriculum_doc_path', ''))}</code></td>
              <td>{f"<a href='../../{r['before_shot']}' target='_blank'>Before</a>" if r.get('before_shot') else '-'}</td>
              <td>{f"<a href='../../{r['after_shot']}' target='_blank'>After</a>" if r.get('after_shot') else '-'}</td>
            </tr>
            """)
        remediations_html = f"""
        <section class="remediations-panel">
          <h2>🛠️ Grounded Curriculum Remediations (Grounded in <code>curriculum_docs_auto/</code>)</h2>
          <table>
            <thead>
              <tr>
                <th>Archetype ID</th>
                <th>Remediation Summary</th>
                <th>Authoritative Curriculum Doc</th>
                <th>Before Fix</th>
                <th>After Fix</th>
              </tr>
            </thead>
            <tbody>
              {"".join(rem_rows)}
            </tbody>
          </table>
        </section>
        """

    subj_filter_buttons = "".join(
        f'<button class="filter-btn" onclick="filterSubject(\'{html.escape(s)}\')">{html.escape(s)}</button>'
        for s in subjects
    )

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Grade {grade} Archetype Quality & Multi-Scroll Gallery | Fundile</title>
  <style>
    :root {{
      --primary: #13519C;
      --primary-light: #EBF3FC;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --border: #E2E8F0;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --emerald: #10B981;
      --rose: #E11D48;
      --amber: #F59E0B;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--text-main);
      padding-bottom: 60px;
    }}
    header {{
      background: var(--primary);
      color: #fff;
      padding: 24px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}
    header h1 {{ font-size: 22px; font-weight: 700; }}
    header p {{ font-size: 13px; opacity: 0.9; margin-top: 4px; }}
    .kpi-bar {{
      display: flex;
      gap: 16px;
      padding: 20px 32px;
      background: #fff;
      border-bottom: 1px solid var(--border);
      flex-wrap: wrap;
    }}
    .kpi-card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 20px;
      min-width: 150px;
    }}
    .kpi-card .val {{ font-size: 20px; font-weight: 700; color: var(--primary); }}
    .kpi-card .lbl {{ font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 600; margin-top: 2px; }}
    .filters {{
      padding: 16px 32px;
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .filter-btn {{
      padding: 6px 14px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #fff;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
    }}
    .filter-btn.active {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }}
    .container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 32px;
    }}
    .archetype-card {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 24px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      overflow: hidden;
    }}
    .card-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .card-title-group {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .index-num {{ font-size: 12px; font-weight: 700; color: var(--primary); }}
    .subj-tag {{ font-size: 11px; font-weight: 700; background: var(--primary-light); color: var(--primary); padding: 2px 8px; border-radius: 4px; }}
    .topic-tag {{ font-size: 12px; color: var(--text-muted); font-weight: 500; }}
    .arch-title {{ font-size: 14px; font-weight: 700; color: var(--text-main); font-family: monospace; }}
    .card-meta {{ display: flex; align-items: center; gap: 8px; }}
    .meta-pill {{ font-size: 11px; background: #F1F5F9; color: #475569; padding: 2px 8px; border-radius: 4px; font-weight: 600; }}
    .badge {{ font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 4px; }}
    .badge-pass {{ background: #ECFDF5; color: var(--emerald); border: 1px solid #A7F3D0; }}
    .badge-fail {{ background: #FFF1F2; color: var(--rose); border: 1px solid #FECDD3; }}
    .defects-box {{
      background: #FFFBEB;
      border-bottom: 1px solid #FDE68A;
      padding: 12px 20px;
      color: #92400E;
      font-size: 12px;
    }}
    .defects-box ul {{ margin-left: 18px; margin-top: 4px; }}
    .shots-section {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      padding: 16px 20px;
      background: #FAFAFA;
    }}
    @media (max-width: 900px) {{
      .shots-section {{ grid-template-columns: 1fr; }}
    }}
    .shots-col {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
    }}
    .shots-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 10px;
      padding-bottom: 6px;
      border-bottom: 1px solid #F1F5F9;
    }}
    .shots-count {{ font-size: 10px; font-family: monospace; font-weight: 600; }}
    .shots-grid {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 6px;
    }}
    .shot-card {{
      min-width: 220px;
      max-width: 260px;
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
      background: #fff;
      flex-shrink: 0;
    }}
    .shot-card img {{
      width: 100%;
      height: 140px;
      object-fit: cover;
      display: block;
      transition: transform 0.2s;
    }}
    .shot-card:hover img {{ transform: scale(1.02); }}
    .shot-caption {{
      font-size: 10px;
      padding: 4px 6px;
      text-align: center;
      color: var(--text-muted);
      font-weight: 600;
      background: #F8FAFC;
    }}
    .remediations-panel {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 24px;
    }}
    .remediations-panel h2 {{ font-size: 16px; margin-bottom: 12px; color: var(--primary); }}
    table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
    th, td {{ padding: 8px 12px; border-bottom: 1px solid var(--border); text-align: left; }}
    th {{ background: #F8FAFC; color: var(--text-muted); font-size: 11px; text-transform: uppercase; }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Grade {grade} Archetype Quality, Anti-Leak & Multi-Scroll Gallery</h1>
      <p>100% Student Workspace UI Capture • All Subskill Archetypes • Zero-Token Deterministic Audit</p>
    </div>
    <div>
      <a href="index.html" style="color: #fff; font-size: 12px; text-decoration: underline;">← Back to Index</a>
    </div>
  </header>

  <div class="kpi-bar">
    <div class="kpi-card">
      <div class="val">{data.get('total_topics', 0)}</div>
      <div class="lbl">Curriculum Topics</div>
    </div>
    <div class="kpi-card">
      <div class="val">{total_archs}</div>
      <div class="lbl">Audited Archetypes</div>
    </div>
    <div class="kpi-card">
      <div class="val">{total_shots}</div>
      <div class="lbl">Screenshots on Disk</div>
    </div>
    <div class="kpi-card">
      <div class="val" style="color: {'var(--emerald)' if flagged_count == 0 else 'var(--rose)'};">
        {pass_count} / {total_archs} ({round((pass_count / total_archs * 100) if total_archs else 0)}%)
      </div>
      <div class="lbl">Pass Rate</div>
    </div>
    <div class="kpi-card">
      <div class="val" style="color: var(--amber);">{flagged_count}</div>
      <div class="lbl">Flagged Items</div>
    </div>
  </div>

  <div class="filters">
    <button class="filter-btn active" onclick="filterSubject('ALL')">All Subjects</button>
    {subj_filter_buttons}
    <span style="margin: 0 12px; color: #CBD5E1;">|</span>
    <button class="filter-btn" onclick="filterStatus('all')">All Status</button>
    <button class="filter-btn" onclick="filterStatus('pass')">Pass Only</button>
    <button class="filter-btn" onclick="filterStatus('flagged')">Flagged Only</button>
  </div>

  <div class="container">
    {remediations_html}
    {"".join(cards_html)}
  </div>

  <script>
    let activeSubject = 'ALL';
    let activeStatus = 'all';

    function filterSubject(subj) {{
      activeSubject = subj;
      document.querySelectorAll('.filters .filter-btn').forEach(b => {{
        if (b.innerText === subj || (subj === 'ALL' && b.innerText === 'All Subjects')) {{
          b.classList.add('active');
        }} else if (!['All Status', 'Pass Only', 'Flagged Only'].includes(b.innerText)) {{
          b.classList.remove('active');
        }}
      }});
      applyFilters();
    }}

    function filterStatus(status) {{
      activeStatus = status;
      applyFilters();
    }}

    function applyFilters() {{
      document.querySelectorAll('.archetype-card').forEach(card => {{
        const cardSubj = card.getAttribute('data-subject');
        const cardStatus = card.getAttribute('data-status');
        const matchSubj = activeSubject === 'ALL' || cardSubj === activeSubject;
        const matchStatus = activeStatus === 'all' || cardStatus === activeStatus;
        card.style.display = (matchSubj && matchStatus) ? 'block' : 'none';
      }});
    }}
  </script>
</body>
</html>
"""
    out_file = AUDIT_DIR / f"grade_{grade}.html"
    out_file.write_text(page_html, encoding="utf-8")
    print(f"Generated HTML report: {out_file}")


def generate_index_html() -> None:
    grades = ["7", "8", "9", "10", "11", "12"]
    rows = []
    total_archs_all = 0
    total_shots_all = 0
    total_pass_all = 0

    for g in grades:
        ledger_path = AUDIT_DIR / f"ledger_gr{g}.json"
        if ledger_path.is_file():
            data = json.loads(ledger_path.read_text(encoding="utf-8"))
            archs = data.get("archetypes", [])
            passes = sum(1 for a in archs if len(a.get("unresolved_defects", [])) == 0)
            shots = sum(
                len(a.get("pre_scroll_screenshots", [])) + len(a.get("memo_scroll_screenshots", []))
                for a in archs
            )
            total_archs_all += len(archs)
            total_shots_all += shots
            total_pass_all += passes
            pct = round(passes / len(archs) * 100) if archs else 0
            rows.append(f"""
            <tr>
              <td><strong>Grade {g}</strong></td>
              <td>{data.get('total_topics', 0)}</td>
              <td>{len(archs)}</td>
              <td>{shots}</td>
              <td><span style="color: {'#10B981' if passes == len(archs) else '#E11D48'}; font-weight: bold;">{passes} / {len(archs)} ({pct}%)</span></td>
              <td><a href="grade_{g}.html" style="color: #13519C; font-weight: bold;">Open Gallery →</a></td>
            </tr>
            """)
        else:
            rows.append(f"""
            <tr>
              <td><strong>Grade {g}</strong></td>
              <td colspan="4" style="color: #94A3B8;">Pending audit execution</td>
              <td>-</td>
            </tr>
            """)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Master Archetype Quality & Multi-Scroll Gallery (Grades 7–12) | Fundile</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #F8FAFC;
      color: #0F172A;
      padding: 40px;
    }}
    .header {{
      background: #13519C;
      color: #fff;
      padding: 32px;
      border-radius: 12px;
      margin-bottom: 24px;
    }}
    .table-card {{
      background: #fff;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{ padding: 14px 20px; border-bottom: 1px solid #E2E8F0; text-align: left; }}
    th {{ background: #F1F5F9; font-size: 11px; text-transform: uppercase; color: #64748B; }}
  </style>
</head>
<body>
  <div class="header">
    <h1>Platform Full-Archetype Quality & Multi-Scroll Screenshot Gallery</h1>
    <p>Comprehensive audit of all 2,550 subskill archetypes across 476 curriculum topics (Grades 7–12).</p>
  </div>
  <div class="table-card">
    <table>
      <thead>
        <tr>
          <th>Grade</th>
          <th>Curriculum Topics</th>
          <th>Subskill Archetypes</th>
          <th>Screenshots on Disk</th>
          <th>Pass Rate</th>
          <th>Interactive Gallery</th>
        </tr>
      </thead>
      <tbody>
        {"".join(rows)}
      </tbody>
    </table>
  </div>
</body>
</html>
"""
    out_file = AUDIT_DIR / "index.html"
    out_file.write_text(index_html, encoding="utf-8")
    print(f"Generated master index: {out_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Full Archetype HTML Report")
    parser.add_argument("--grade", type=str, help="Grade to build report for (7..12)")
    parser.add_argument("--all", action="store_true", help="Build reports for all grades")
    args = parser.parse_args()

    if args.all:
        for g in ["7", "8", "9", "10", "11", "12"]:
            generate_grade_html(g)
        generate_index_html()
    elif args.grade:
        generate_grade_html(args.grade)
        generate_index_html()
    else:
        generate_index_html()


if __name__ == "__main__":
    main()
