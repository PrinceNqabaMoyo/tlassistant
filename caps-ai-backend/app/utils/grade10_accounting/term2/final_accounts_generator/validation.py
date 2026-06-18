from __future__ import annotations

from typing import Any, Dict

from .shared import _float_or_zero, _money_matches, _round_money


class _FinalAccountsScenarioValidationError(ValueError):
    pass


def _validate_final_accounts_question(*, question: Dict[str, Any], subskill: str) -> None:
    prompt = str(question.get("prompt") or "").strip()
    if not prompt:
        raise _FinalAccountsScenarioValidationError("Generated Final Accounts question is missing a prompt.")

    qt = str(question.get("question_type") or "").strip().lower()
    correct_map = question.get("correct_map") if isinstance(question.get("correct_map"), dict) else {}
    if qt == "typed" and not str(question.get("sample_answer") or "").strip():
        raise _FinalAccountsScenarioValidationError("Typed Final Accounts question is missing a sample answer.")

    if qt == "table_wordbank":
        rows = list(question.get("table", {}).get("rows") or [])
        token_ids = {str(item.get("id")) for item in list(question.get("word_bank") or []) if item.get("id") is not None}
        if not rows or not correct_map:
            raise _FinalAccountsScenarioValidationError("Table word-bank Final Accounts question is missing rows or a correct map.")
        for row_key, column_map in correct_map.items():
            row_index = int(row_key)
            if row_index < 0 or row_index >= len(rows):
                raise _FinalAccountsScenarioValidationError("Table word-bank Final Accounts question maps to an invalid row index.")
            if not isinstance(column_map, dict) or not column_map:
                raise _FinalAccountsScenarioValidationError("Table word-bank Final Accounts question has an invalid column mapping.")
            for token_id in column_map.values():
                if str(token_id) not in token_ids:
                    raise _FinalAccountsScenarioValidationError("Table word-bank Final Accounts question maps to a token that is not in the word bank.")

    if qt in {"journal", "ledger", "final_account_table", "trial_balance_table", "asset_register_table", "adjustment_analysis_table"}:
        tables = list(question.get("tables") or []) if isinstance(question.get("tables"), list) else []
        if not tables and isinstance(question.get("table"), dict):
            tables = [question.get("table")]
        if not tables or not correct_map:
            raise _FinalAccountsScenarioValidationError("Fill-in Final Accounts question is missing tables or a correct map.")
        editable_cell_ids = set()
        for table in tables:
            rows = list(table.get("rows") or []) if isinstance(table, dict) else []
            for row in rows:
                for cell in list(row or []):
                    if isinstance(cell, dict) and cell.get("cell_id") is not None:
                        editable_cell_ids.add(str(cell.get("cell_id")))
        if not editable_cell_ids:
            raise _FinalAccountsScenarioValidationError("Fill-in Final Accounts question has no editable cells.")
        for cell_id in correct_map.keys():
            if str(cell_id) not in editable_cell_ids:
                raise _FinalAccountsScenarioValidationError("Fill-in Final Accounts question maps to a cell_id that does not exist in the rendered table structure.")

    answer_part_hints = list(question.get("answer_part_hints") or []) if isinstance(question.get("answer_part_hints"), list) else []
    validation = question.get("scenario_validation") if isinstance(question.get("scenario_validation"), dict) else None
    if validation:
        family = str(validation.get("family") or "").strip().lower()
        if family == "closing_gross_profit":
            expected = _round_money(float(validation.get("sales", 0.0)) - float(validation.get("debtors_allow", 0.0)) - float(validation.get("cost_of_sales", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Closing gross profit failed recomputation.")
        elif family == "closing_net_profit":
            expected = _round_money(float(validation.get("gross_profit", 0.0)) + float(validation.get("other_income", 0.0)) - float(validation.get("total_expenses", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Closing net profit failed recomputation.")
        elif family == "closing_capital":
            expected = _round_money(float(validation.get("opening_capital", 0.0)) + float(validation.get("net_profit", 0.0)) - float(validation.get("drawings", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Closing capital failed recomputation.")
        elif family == "closing_steps_typed":
            minimum_parts = int(validation.get("minimum_parts") or 0)
            if len(answer_part_hints) < minimum_parts:
                raise _FinalAccountsScenarioValidationError("Closing transfer typed memo is too shallow.")
        elif family == "depreciation_straight_line":
            expected = _round_money(float(validation.get("cost", 0.0)) * float(validation.get("percentage", 0.0)) / 100)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Straight-line depreciation failed recomputation.")
        elif family == "depreciation_diminishing_partial":
            expected = _round_money(float(validation.get("cost", 0.0)) * float(validation.get("percentage", 0.0)) / 100 * float(validation.get("months", 0.0)) / 12)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Partial diminishing depreciation failed recomputation.")
        elif family == "depreciation_carrying_year2":
            year1 = _round_money(float(validation.get("cost", 0.0)) * float(validation.get("percentage", 0.0)) / 100 * float(validation.get("months", 0.0)) / 12)
            carrying_after_year1 = _round_money(float(validation.get("cost", 0.0)) - year1)
            expected = _round_money(carrying_after_year1 - (carrying_after_year1 * float(validation.get("percentage", 0.0)) / 100))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Year-2 carrying value failed recomputation.")
        elif family == "asset_register_carrying_year3":
            annual = _round_money(float(validation.get("cost", 0.0)) * float(validation.get("percentage", 0.0)) / 100)
            expected = _round_money(float(validation.get("cost", 0.0)) - (annual * float(validation.get("years", 0.0))))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Asset register carrying value failed recomputation.")
        elif family in {"asset_register_installation_note_fill", "adjustment_analysis_matrix_fill", "adjustment_journal_workflow_fill", "closing_transfer_workflow_fill", "closing_transfer_full_project_fill", "capital_calculation_integrated_fill", "depreciation_ledger_workflow_fill", "depreciation_core_summary_fill", "error_correction_journal_fill", "error_correction_journal_workflow_fill", "error_correction_analysis_fill", "error_correction_integrated_adjustment_journal_fill", "error_correction_ledger_fill", "error_correction_carrythrough_fill", "interest_adjustment_journal_workflow_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Expanded table workflow does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Expanded table workflow is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Expanded table workflow failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Expanded table workflow failed text cell recomputation.")
        elif family in {"adjustment_consumables_used", "consumable_stores_used_calc"}:
            expected = _round_money(float(validation.get("purchased", 0.0)) - float(validation.get("on_hand", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Consumables adjustment failed recomputation.")
        elif family == "adjustment_accrued_income":
            expected = _round_money(float(validation.get("monthly_amount", 0.0)) * float(validation.get("months", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Accrued income failed recomputation.")
        elif family == "adjustment_accrued_interest":
            expected = _round_money(float(validation.get("loan_balance", 0.0)) * float(validation.get("rate", 0.0)) / 100 * float(validation.get("months", 0.0)) / 12)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Accrued interest failed recomputation.")
        elif family == "interest_on_loan_calc":
            expected = _round_money(float(validation.get("loan_balance", 0.0)) * float(validation.get("rate", 0.0)) / 100 * float(validation.get("months", 0.0)) / 12)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Interest on loan calculation failed recomputation.")
        elif family == "adjustment_stock_difference":
            expected = _round_money(abs(float(validation.get("actual_count", 0.0)) - float(validation.get("per_records", 0.0))))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Trading stock difference failed recomputation.")
        elif family == "trading_stock_variance_calc":
            expected = _round_money(abs(float(validation.get("actual_count", 0.0)) - float(validation.get("per_records", 0.0))))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Trading stock variance calculation failed recomputation.")
        elif family == "bad_debts_net_debtors_calc":
            expected = _round_money(float(validation.get("opening_debtors", 0.0)) - float(validation.get("amount", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Bad debts adjusted debtors balance failed recomputation.")
        elif family == "adjustments_why_typed":
            minimum_parts = int(validation.get("minimum_parts") or 0)
            if len(answer_part_hints) < minimum_parts:
                raise _FinalAccountsScenarioValidationError("Year-end adjustments typed memo is too shallow.")
        elif family == "bad_debts_write_off_typed":
            minimum_parts = int(validation.get("minimum_parts") or 0)
            if len(answer_part_hints) < minimum_parts:
                raise _FinalAccountsScenarioValidationError("Bad debts typed memo is too shallow.")
        elif family == "reversals_explain_typed":
            minimum_parts = int(validation.get("minimum_parts") or 0)
            if len(answer_part_hints) < minimum_parts:
                raise _FinalAccountsScenarioValidationError("Reversals typed memo is too shallow.")
        elif family == "income_statement_net_profit":
            expected = _round_money((float(validation.get("sales", 0.0)) - float(validation.get("debtors_allowances", 0.0)) - float(validation.get("cost_of_sales", 0.0))) + float(validation.get("rent_income", 0.0)) + float(validation.get("interest_income", 0.0)) - float(validation.get("total_expenses", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Income statement net profit failed recomputation.")
        elif family == "trading_account_gross_profit_calc":
            net_sales = _round_money(float(validation.get("sales", 0.0)) - float(validation.get("debtors_allowances", 0.0)))
            net_purchases = _round_money(float(validation.get("purchases", 0.0)) - float(validation.get("returns_outwards", 0.0)))
            cost_of_sales = _round_money(float(validation.get("opening_stock", 0.0)) + net_purchases + float(validation.get("carriage_on_purchases", 0.0)) - float(validation.get("closing_stock", 0.0)))
            expected = _round_money(net_sales - cost_of_sales)
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Trading Account gross profit failed recomputation.")
        elif family == "profit_and_loss_net_profit_calc":
            expected = _round_money(float(validation.get("gross_profit", 0.0)) + float(validation.get("other_income", 0.0)) - float(validation.get("total_expenses", 0.0)))
            if not _money_matches(float(question.get("correct_answer") or 0.0), expected):
                raise _FinalAccountsScenarioValidationError("Profit and Loss net profit failed recomputation.")
        elif family == "adjustment_consumables_journal_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Adjustment journal fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            if not _money_matches(_float_or_zero(correct_map.get("adj-consumables-dr-amount")), amount) or not _money_matches(_float_or_zero(correct_map.get("adj-consumables-cr-amount")), amount):
                raise _FinalAccountsScenarioValidationError("Adjustment journal fill question failed amount recomputation.")
        elif family in {"bad_debts_write_off_journal_fill", "bad_debts_recovery_journal_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Bad debts journal fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_ids = [str(cell_id) for cell_id in list(validation.get("amount_cell_ids") or []) if str(cell_id).strip()]
            if not amount_cell_ids:
                raise _FinalAccountsScenarioValidationError("Bad debts journal fill question is missing amount-cell validation metadata.")
            for cell_id in amount_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), amount):
                    raise _FinalAccountsScenarioValidationError("Bad debts journal fill question failed amount recomputation.")
        elif family in {"interest_on_loan_journal_fill", "interest_income_journal_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Interest adjustment journal fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Interest adjustment journal fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Interest adjustment journal fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Interest adjustment journal fill question failed text cell recomputation.")
        elif family == "bad_debts_write_off_analysis_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Bad debts analysis fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_id = str(validation.get("amount_cell_id") or "").strip()
            if not amount_cell_id:
                raise _FinalAccountsScenarioValidationError("Bad debts analysis fill question is missing amount-cell validation metadata.")
            if not _money_matches(_float_or_zero(correct_map.get(amount_cell_id)), amount):
                raise _FinalAccountsScenarioValidationError("Bad debts analysis fill question failed amount recomputation.")
        elif family == "trading_stock_variance_journal_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Trading stock variance journal fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_ids = [str(cell_id) for cell_id in list(validation.get("amount_cell_ids") or []) if str(cell_id).strip()]
            if not amount_cell_ids:
                raise _FinalAccountsScenarioValidationError("Trading stock variance journal fill question is missing amount-cell validation metadata.")
            for cell_id in amount_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), amount):
                    raise _FinalAccountsScenarioValidationError("Trading stock variance journal fill question failed amount recomputation.")
        elif family == "trading_stock_variance_ledger_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Trading stock variance ledger fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_ids = [str(cell_id) for cell_id in list(validation.get("amount_cell_ids") or []) if str(cell_id).strip()]
            if not amount_cell_ids:
                raise _FinalAccountsScenarioValidationError("Trading stock variance ledger fill question is missing amount-cell validation metadata.")
            for cell_id in amount_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), amount):
                    raise _FinalAccountsScenarioValidationError("Trading stock variance ledger fill question failed amount recomputation.")
        elif family == "trading_stock_variance_carrythrough_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Trading stock variance carry-through fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            adjusted_stock = _round_money(float(validation.get("adjusted_stock", 0.0)))
            amount_cell_id = str(validation.get("amount_cell_id") or "").strip()
            adjusted_stock_cell_id = str(validation.get("adjusted_stock_cell_id") or "").strip()
            if not amount_cell_id or not adjusted_stock_cell_id:
                raise _FinalAccountsScenarioValidationError("Trading stock variance carry-through fill question is missing validation cell metadata.")
            if not _money_matches(_float_or_zero(correct_map.get(amount_cell_id)), amount):
                raise _FinalAccountsScenarioValidationError("Trading stock variance carry-through fill question failed variance recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get(adjusted_stock_cell_id)), adjusted_stock):
                raise _FinalAccountsScenarioValidationError("Trading stock variance carry-through fill question failed adjusted-stock recomputation.")
        elif family == "depreciation_ledger_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Depreciation ledger fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            if not _money_matches(_float_or_zero(correct_map.get("dep-ledger-dr-amount")), amount) or not _money_matches(_float_or_zero(correct_map.get("dep-ledger-cr-amount")), amount):
                raise _FinalAccountsScenarioValidationError("Depreciation ledger fill question failed amount recomputation.")
        elif family in {"accrued_income_reversal_ledger_fill", "accrued_expense_reversal_ledger_fill", "prepaid_expense_reversal_ledger_fill", "income_received_in_advance_reversal_ledger_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Adjustment reversal ledger fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_ids = [str(cell_id) for cell_id in list(validation.get("amount_cell_ids") or []) if str(cell_id).strip()]
            if not amount_cell_ids:
                raise _FinalAccountsScenarioValidationError("Adjustment reversal ledger fill question is missing amount-cell validation metadata.")
            for cell_id in amount_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), amount):
                    raise _FinalAccountsScenarioValidationError("Adjustment reversal ledger fill question failed amount recomputation.")
        elif family in {"accrued_income_reversal_journal_fill", "accrued_expense_reversal_journal_fill", "prepaid_expense_reversal_journal_fill", "income_received_in_advance_reversal_journal_fill", "consumable_stores_reversal_journal_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Adjustment reversal journal fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_ids = [str(cell_id) for cell_id in list(validation.get("amount_cell_ids") or []) if str(cell_id).strip()]
            if not amount_cell_ids:
                raise _FinalAccountsScenarioValidationError("Adjustment reversal journal fill question is missing amount-cell validation metadata.")
            for cell_id in amount_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), amount):
                    raise _FinalAccountsScenarioValidationError("Adjustment reversal journal fill question failed amount recomputation.")
        elif family in {"accrued_income_analysis_fill", "accrued_expense_analysis_fill", "prepaid_expense_analysis_fill", "income_received_in_advance_analysis_fill", "consumable_stores_analysis_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Adjustment analysis fill question does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_id = str(validation.get("amount_cell_id") or "").strip()
            if not amount_cell_id:
                raise _FinalAccountsScenarioValidationError("Adjustment analysis fill question is missing amount-cell validation metadata.")
            if not _money_matches(_float_or_zero(correct_map.get(amount_cell_id)), amount):
                raise _FinalAccountsScenarioValidationError("Adjustment analysis fill question failed amount recomputation.")
        elif family == "interest_income_analysis_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Interest income analysis fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Interest income analysis fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Interest income analysis fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Interest income analysis fill question failed text cell recomputation.")
        elif family == "post_closing_trial_balance_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Post-closing Trial Balance fill question does not match its expected editable-cell count.")
            total = _round_money(float(validation.get("total", 0.0)))
            if not _money_matches(_float_or_zero(correct_map.get("tb-total-debit")), total) or not _money_matches(_float_or_zero(correct_map.get("tb-total-credit")), total):
                raise _FinalAccountsScenarioValidationError("Post-closing Trial Balance totals failed recomputation.")
        elif family == "post_closing_trial_balance_expanded_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Expanded Post-closing Trial Balance fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Expanded Post-closing Trial Balance fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Expanded Post-closing Trial Balance fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Expanded Post-closing Trial Balance fill question failed text cell recomputation.")
        elif family == "post_adjustment_trial_balance_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Post-adjustment Trial Balance fill question does not match its expected editable-cell count.")
            total = _round_money(float(validation.get("total", 0.0)))
            if not _money_matches(_float_or_zero(correct_map.get("patb-total-debit")), total) or not _money_matches(_float_or_zero(correct_map.get("patb-total-credit")), total):
                raise _FinalAccountsScenarioValidationError("Post-adjustment Trial Balance totals failed recomputation.")
        elif family == "post_adjustment_trial_balance_worksheet_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Worksheet-style Post-adjustment Trial Balance question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Worksheet-style Post-adjustment Trial Balance question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Worksheet-style Post-adjustment Trial Balance question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Worksheet-style Post-adjustment Trial Balance question failed text cell recomputation.")
        elif family == "income_statement_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Final accounts fill question does not match its expected editable-cell count.")
            net_sales_expected = _round_money(float(validation.get("sales", 0.0)) - float(validation.get("debtors_allowances", 0.0)))
            gross_profit_expected = _round_money(net_sales_expected - float(validation.get("cost_of_sales", 0.0)))
            net_profit_expected = _round_money(gross_profit_expected + float(validation.get("other_income", 0.0)) - float(validation.get("total_expenses", 0.0)))
            if not _money_matches(_float_or_zero(correct_map.get("fa-net-sales")), net_sales_expected):
                raise _FinalAccountsScenarioValidationError("Final accounts fill question failed net sales recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get("fa-gross-profit")), gross_profit_expected) or not _money_matches(_float_or_zero(correct_map.get("fa-pl-gross-profit")), gross_profit_expected):
                raise _FinalAccountsScenarioValidationError("Final accounts fill question failed gross profit recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get("fa-net-profit")), net_profit_expected):
                raise _FinalAccountsScenarioValidationError("Final accounts fill question failed net profit recomputation.")
        elif family in {"trading_account_full_extract_fill", "profit_and_loss_full_extract_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Standalone final-accounts fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Standalone final-accounts fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Standalone final-accounts fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Standalone final-accounts fill question failed text cell recomputation.")
        elif family in {"accrued_income_carrythrough_fill", "accrued_expense_carrythrough_fill", "prepaid_expense_carrythrough_fill", "income_received_in_advance_carrythrough_fill", "consumable_stores_carrythrough_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Adjustment carry-through fill question does not match its expected editable-cell count.")
            adjusted_amount = _round_money(float(validation.get("adjusted_amount", 0.0)))
            carry_amount = _round_money(float(validation.get("carry_amount", 0.0)))
            adjusted_cell_id = str(validation.get("adjusted_cell_id") or "").strip()
            carry_cell_id = str(validation.get("carry_cell_id") or "").strip()
            if not adjusted_cell_id or not carry_cell_id:
                raise _FinalAccountsScenarioValidationError("Adjustment carry-through fill question is missing validation cell metadata.")
            if not _money_matches(_float_or_zero(correct_map.get(adjusted_cell_id)), adjusted_amount):
                raise _FinalAccountsScenarioValidationError("Adjustment carry-through fill question failed adjusted-balance recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get(carry_cell_id)), carry_amount):
                raise _FinalAccountsScenarioValidationError("Adjustment carry-through fill question failed Balance Sheet carry-through recomputation.")
        elif family in {"interest_on_loan_carrythrough_fill", "interest_income_carrythrough_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Interest carry-through fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Interest carry-through fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Interest carry-through fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Interest carry-through fill question failed text cell recomputation.")
        elif family in {"accrued_income_post_adjustment_tb_fill", "accrued_expense_post_adjustment_tb_fill", "prepaid_expense_post_adjustment_tb_fill", "income_received_in_advance_post_adjustment_tb_fill", "consumable_stores_post_adjustment_tb_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Adjustment post-adjustment Trial Balance fill question does not match its expected editable-cell count.")
            total = _round_money(float(validation.get("total", 0.0)))
            adjusted_amount = _round_money(float(validation.get("adjusted_amount", 0.0)))
            carry_amount = _round_money(float(validation.get("carry_amount", 0.0)))
            adjusted_cell_id = str(validation.get("adjusted_cell_id") or "").strip()
            carry_cell_id = str(validation.get("carry_cell_id") or "").strip()
            total_debit_cell_id = str(validation.get("total_debit_cell_id") or "").strip()
            total_credit_cell_id = str(validation.get("total_credit_cell_id") or "").strip()
            if not adjusted_cell_id or not carry_cell_id or not total_debit_cell_id or not total_credit_cell_id:
                raise _FinalAccountsScenarioValidationError("Adjustment post-adjustment Trial Balance fill question is missing validation cell metadata.")
            if not _money_matches(_float_or_zero(correct_map.get(adjusted_cell_id)), adjusted_amount):
                raise _FinalAccountsScenarioValidationError("Adjustment post-adjustment Trial Balance fill question failed adjusted-balance recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get(carry_cell_id)), carry_amount):
                raise _FinalAccountsScenarioValidationError("Adjustment post-adjustment Trial Balance fill question failed carry-through recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get(total_debit_cell_id)), total) or not _money_matches(_float_or_zero(correct_map.get(total_credit_cell_id)), total):
                raise _FinalAccountsScenarioValidationError("Adjustment post-adjustment Trial Balance fill question failed total recomputation.")
        elif family == "interest_adjustment_post_adjustment_tb_fill":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Interest-adjustment Post-adjustment Trial Balance fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Interest-adjustment Post-adjustment Trial Balance fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Interest-adjustment Post-adjustment Trial Balance fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Interest-adjustment Post-adjustment Trial Balance fill question failed text cell recomputation.")
        elif family in {"interest_on_loan_ledger_fill", "consumable_stores_reversal_ledger_fill", "error_correction_ledger_fill"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Ledger fill question does not match its expected editable-cell count.")
            cell_expectations = validation.get("cell_expectations") if isinstance(validation.get("cell_expectations"), dict) else {}
            if not cell_expectations:
                raise _FinalAccountsScenarioValidationError("Ledger fill question is missing cell expectation validation metadata.")
            for cell_id, expected_value in cell_expectations.items():
                actual_value = correct_map.get(cell_id)
                if isinstance(expected_value, (int, float)):
                    if not _money_matches(_float_or_zero(actual_value), float(expected_value)):
                        raise _FinalAccountsScenarioValidationError("Ledger fill question failed numeric cell recomputation.")
                else:
                    if str(actual_value or "").strip().lower() != str(expected_value or "").strip().lower():
                        raise _FinalAccountsScenarioValidationError("Ledger fill question failed text cell recomputation.")
        elif family in {"accrued_income_reversal_mini_project", "accrued_expense_reversal_mini_project", "prepaid_expense_reversal_mini_project", "income_received_in_advance_reversal_mini_project", "consumable_stores_reversal_mini_project"}:
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project does not match its expected editable-cell count.")
            amount = _round_money(float(validation.get("amount", 0.0)))
            amount_cell_ids = [str(cell_id) for cell_id in list(validation.get("amount_cell_ids") or []) if str(cell_id).strip()]
            if not amount_cell_ids:
                raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project is missing amount-cell validation metadata.")
            for cell_id in amount_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), amount):
                    raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project failed amount recomputation.")
            adjusted_amount = _round_money(float(validation.get("adjusted_amount", 0.0)))
            adjusted_cell_ids = [str(cell_id) for cell_id in list(validation.get("adjusted_cell_ids") or []) if str(cell_id).strip()]
            if not adjusted_cell_ids:
                raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project is missing adjusted-balance validation metadata.")
            for cell_id in adjusted_cell_ids:
                if not _money_matches(_float_or_zero(correct_map.get(cell_id)), adjusted_amount):
                    raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project failed adjusted-balance recomputation.")
            total = _round_money(float(validation.get("total", 0.0)))
            total_debit_cell_id = str(validation.get("total_debit_cell_id") or "").strip()
            total_credit_cell_id = str(validation.get("total_credit_cell_id") or "").strip()
            if not total_debit_cell_id or not total_credit_cell_id:
                raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project is missing total-cell validation metadata.")
            if not _money_matches(_float_or_zero(correct_map.get(total_debit_cell_id)), total) or not _money_matches(_float_or_zero(correct_map.get(total_credit_cell_id)), total):
                raise _FinalAccountsScenarioValidationError("Integrated reversal mini-project failed total recomputation.")
        elif family == "integrated_final_accounts_project":
            expected_cells = int(validation.get("expected_cells") or 0)
            if len(correct_map) != expected_cells:
                raise _FinalAccountsScenarioValidationError("Integrated final accounts project does not match its expected editable-cell count.")
            if not _money_matches(_float_or_zero(correct_map.get("int-net-sales")), _round_money(float(validation.get("net_sales", 0.0)))):
                raise _FinalAccountsScenarioValidationError("Integrated final accounts project failed net sales recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get("int-gross-profit")), _round_money(float(validation.get("gross_profit", 0.0)))):
                raise _FinalAccountsScenarioValidationError("Integrated final accounts project failed gross profit recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get("int-net-profit")), _round_money(float(validation.get("net_profit", 0.0)))):
                raise _FinalAccountsScenarioValidationError("Integrated final accounts project failed net profit recomputation.")
            if not _money_matches(_float_or_zero(correct_map.get("int-closing-capital")), _round_money(float(validation.get("closing_capital", 0.0)))):
                raise _FinalAccountsScenarioValidationError("Integrated final accounts project failed closing capital recomputation.")
            total = _round_money(float(validation.get("postclosing_total", 0.0)))
            if not _money_matches(_float_or_zero(correct_map.get("int-total-debit")), total) or not _money_matches(_float_or_zero(correct_map.get("int-total-credit")), total):
                raise _FinalAccountsScenarioValidationError("Integrated final accounts project failed post-closing Trial Balance totals recomputation.")


__all__ = ["_FinalAccountsScenarioValidationError", "_validate_final_accounts_question"]
