/**
 * getEvalCellStyle — returns inline style overrides for a cell based on evaluation state.
 *
 * Usage:
 *   const evalStyle = getEvalCellStyle(evaluationState, cellId);
 *   <td style={{ ...baseStyle, ...evalStyle.td }}>
 *       <input style={{ ...baseInputStyle, ...evalStyle.input }} ... />
 *   </td>
 *
 * Returns { td: {}, input: {}, displayValue: null, onClick: null }
 */
export const getEvalCellStyle = (evaluationState, cellId) => {
    const base = { td: {}, input: {}, displayValue: null, onClick: null };

    if (!evaluationState || !evaluationState.isChecked) return base;

    const status = evaluationState.getCellStatus(cellId);
    if (!status) return base;

    if (status.isCorrect) {
        base.td = { borderColor: '#22c55e', borderWidth: '2px' }; // green-500
        if (evaluationState.isComparing && status.displayValue != null) {
            base.input = { backgroundColor: '#f0fdf4', color: '#166534' }; // green-50, green-800
            base.displayValue = String(status.displayValue);
        }
    } else if (status.isIncorrect) {
        base.td = { borderColor: '#ef4444', borderWidth: '2px' }; // red-500
        if (evaluationState.isComparing && status.displayValue != null) {
            base.input = { backgroundColor: '#fef2f2', color: '#991b1b' }; // red-50, red-800
            base.displayValue = String(status.displayValue);
        }
        if (status.hasRubric && evaluationState.handleCellClick) {
            base.td.cursor = 'pointer';
            base.onClick = () => evaluationState.handleCellClick(cellId);
        }
    }

    return base;
};
