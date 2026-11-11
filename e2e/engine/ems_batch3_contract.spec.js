import { test, expect } from '@playwright/test';

/**
 * EMS Batch 3 Contract Verification (GP-16)
 *
 * Strict Compliance:
 * - Rule 0d-1: Zero-theater end-to-end verification. Live application components only.
 * - Rule 0d-4: Grounded in live JSX components (UniversalWorkspace, QuestionSurface, SourceDocumentSvg).
 * - Rule 0d-6: Zero silent skips with explicit assertions.
 * - GP-16: Source documents with vector images and routing to journals/ledgers mount in DOM.
 */

test.describe('Batch 3 EMS Contract (GP-16)', () => {
  const targetBaseUrl = process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:5173';

  test('GP-16: Source document plates mount inside question surface and are absent from memo', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${targetBaseUrl}/`, { waitUntil: 'domcontentloaded' });
    await page.waitForFunction(() => typeof window.__FUNDILE_SWITCH_PERSONA__ === 'function', { timeout: 15000 });

    await page.evaluate(() => {
      window.__FUNDILE_SWITCH_PERSONA__({
        id: 'sch-gr8-01',
        name: 'Kagiso Molefe',
        role: 'student',
        type: 'student',
        grade: 8,
        school: 'Sandton Secondary School',
        assignedTasks: []
      });
      if (window.studentStore) {
        window.studentStore.setEnabledSubjects(['economic_and_management_sciences']);
        window.studentStore.completeDiagnostic('economic_and_management_sciences', 80);
      }
    });

    const openSubjectBtn = page.locator('[data-testid="btn-open-subject-session"]').first();
    await expect(openSubjectBtn).toBeVisible({ timeout: 15000 });
    await openSubjectBtn.click();

    await page.waitForFunction(() => typeof window.__FUNDILE_LOAD_QUESTION__ === 'function', { timeout: 15000 });

    const sourceDocArchetypes = [
      {
        id: 'gp16_receipt',
        subject: 'economic_and_management_sciences',
        grade: 8,
        topic: 'Source documents',
        subskill: 'visual_documents',
        mode: 'practice',
        question_type: 'typed',
        question: 'Examine the duplicate receipt below and identify the subsidiary journal.',
        prompt: 'Examine the duplicate receipt below and identify the subsidiary journal.',
        correct_answer: 'Cash Receipts Journal (CRJ)',
        diagram_spec: {
          kind: 'source_document',
          document_type: 'receipt',
          diagram_role: 'context',
          title: 'DUPLICATE RECEIPT',
          doc_number: '082',
          date: '14 June 2024',
          business_name: 'Nqaba Professional Services',
          received_from: 'M. Ndlovu',
          amount: 2500,
          description: 'Rent of storeroom',
          received_by: 'Nqaba'
        }
      },
      {
        id: 'gp16_deposit_slip',
        subject: 'economic_and_management_sciences',
        grade: 8,
        topic: 'Source documents',
        subskill: 'visual_documents',
        mode: 'practice',
        question_type: 'typed',
        question: 'Examine the bank deposit slip and state the total deposited amount.',
        prompt: 'Examine the bank deposit slip and state the total deposited amount.',
        correct_answer: 'R 3900.00',
        diagram_spec: {
          kind: 'source_document',
          document_type: 'deposit_slip',
          diagram_role: 'context',
          title: 'BANK DEPOSIT SLIP',
          bank_name: 'Standard Bank',
          date: '05 June 2024',
          account_name: 'Nqaba Services',
          account_number: '104829104',
          cash_amount: 2400,
          cheque_amount: 1500,
          total_amount: 3900
        }
      },
      {
        id: 'gp16_cheque_counterfoil',
        subject: 'economic_and_management_sciences',
        grade: 8,
        topic: 'Source documents',
        subskill: 'visual_documents',
        mode: 'practice',
        question_type: 'typed',
        question: 'Examine the cheque counterfoil and identify the payee.',
        prompt: 'Examine the cheque counterfoil and identify the payee.',
        correct_answer: 'Waltons Stationers',
        diagram_spec: {
          kind: 'source_document',
          document_type: 'cheque_counterfoil',
          diagram_role: 'context',
          title: 'CHEQUE COUNTERFOIL',
          doc_number: '204',
          date: '22 June 2024',
          payee: 'Waltons Stationers',
          amount: 650,
          description: 'Office stationery'
        }
      },
      {
        id: 'gp16_bank_statement',
        subject: 'economic_and_management_sciences',
        grade: 8,
        topic: 'Source documents',
        subskill: 'visual_documents',
        mode: 'practice',
        question_type: 'typed',
        question: 'Examine the bank statement and identify the debit amount.',
        prompt: 'Examine the bank statement and identify the debit amount.',
        correct_answer: 'R 245.00',
        diagram_spec: {
          kind: 'source_document',
          document_type: 'bank_statement',
          diagram_role: 'context',
          title: 'BANK STATEMENT EXCERPT',
          bank_name: 'Nedbank',
          date: '30 June 2024',
          description: 'Monthly Service Fees',
          amount: 245,
          entry_type: 'debit'
        }
      },
      {
        id: 'gp16_cash_register_tape',
        subject: 'economic_and_management_sciences',
        grade: 8,
        topic: 'Source documents',
        subskill: 'visual_documents',
        mode: 'practice',
        question_type: 'typed',
        question: 'Examine the cash register roll (CRR) and state the cash total.',
        prompt: 'Examine the cash register roll (CRR) and state the cash total.',
        correct_answer: 'R 1200.00',
        diagram_spec: {
          kind: 'source_document',
          document_type: 'cash_register_tape',
          diagram_role: 'context',
          title: 'CASH REGISTER ROLL (CRR)',
          business_name: 'Nqaba Services',
          date: '18 June 2024',
          crr_number: 'CRR 01',
          amount: 1200
        }
      }
    ];

    for (const q of sourceDocArchetypes) {
      await page.evaluate((question) => {
        window.__FUNDILE_LOAD_QUESTION__(question);
      }, q);

      // 1. Verify question surface has mounted
      const questionSurface = page.locator('[data-testid="question-surface"]:visible').first();
      await expect(questionSurface).toBeVisible({ timeout: 10000 });

      // 2. Verify source document SVG element has mounted inside the question surface
      const docSvg = questionSurface.locator('[data-testid="source-document-svg"]:visible').first();
      await expect(docSvg).toBeVisible({ timeout: 10000 });

      // 3. Verify the specific document plate has rendered
      const plate = docSvg.locator(`[data-testid="source-doc-${q.diagram_spec.document_type.replace(/_/g, '-')}"]`).first();
      await expect(plate).toBeVisible({ timeout: 5000 });

      // 4. Verify diagram is absent from the full-memo panel
      const memoPanel = page.locator('[data-testid="panel-full-memo"]');
      const memoDiagramCount = await memoPanel.locator('[data-testid="source-document-svg"]').count();
      expect(memoDiagramCount).toBe(0);
    }
  });
});
