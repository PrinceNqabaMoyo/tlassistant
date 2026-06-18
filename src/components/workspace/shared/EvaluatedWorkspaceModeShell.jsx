import React, { useEffect } from 'react';
import WorkspaceModeShell from './WorkspaceModeShell';
import { useEvaluationCheck } from '../../../hooks/useEvaluationCheck';
import EvaluationOverlay, { EvaluationScoreBanner } from './EvaluationOverlay';

/**
 * EvaluatedWorkspaceModeShell — drop-in replacement for WorkspaceModeShell
 * that automatically wires the Check/Compare evaluation system.
 *
 * Usage (in registry):
 *   h(EvaluatedWorkspaceModeShell, {
 *       ...shellProps,
 *       question: controller.scaffoldQuestion,
 *       userAnswersCells: controller.scaffoldAnswer?.cells || {},
 *   }, h(ScaffoldComponent, {...}))
 *
 * When `question` has a `correct_map`, Check/Compare buttons appear automatically.
 * When `question` changes, evaluation state resets.
 */
const EvaluatedWorkspaceModeShell = ({
    question,
    userAnswersCells,
    children,
    ...shellProps
}) => {
    const {
        checkResults,
        isChecked,
        isComparing,
        selectedCell,
        summary,
        handleCheck,
        handleCompare,
        handleCellClick,
        closeOverlay,
        resetEvaluation,
        getCellStatus,
    } = useEvaluationCheck({
        question,
        userAnswers: userAnswersCells || {},
    });

    // Reset evaluation when question changes
    useEffect(() => {
        resetEvaluation();
    }, [question]);

    // Determine if evaluation is available (question has correct_map)
    const hasCorrectMap = question?.correct_map && typeof question.correct_map === 'object'
        && Object.keys(question.correct_map).length > 0;

    // Clone children to inject evaluation props
    const enhancedChildren = React.Children.map(children, (child) => {
        if (!React.isValidElement(child)) return child;
        return React.cloneElement(child, {
            evaluationState: hasCorrectMap ? {
                isChecked,
                isComparing,
                checkResults,
                getCellStatus,
                handleCellClick,
            } : null,
        });
    });

    return (
        <WorkspaceModeShell
            {...shellProps}
            onCheck={hasCorrectMap ? handleCheck : undefined}
            onCompare={hasCorrectMap ? handleCompare : undefined}
            isChecked={isChecked}
            isComparing={isComparing}
        >
            {/* Score Banner (appears after Check) */}
            {isChecked && summary && (
                <div className="mb-4">
                    <EvaluationScoreBanner summary={summary} />
                </div>
            )}

            {/* Scaffold content with injected evaluation state */}
            {enhancedChildren}

            {/* Rubric overlay for clicked incorrect cell */}
            {selectedCell && checkResults?.[selectedCell] && (
                <EvaluationOverlay
                    cellId={selectedCell}
                    result={checkResults[selectedCell]}
                    onClose={closeOverlay}
                />
            )}
        </WorkspaceModeShell>
    );
};

export default EvaluatedWorkspaceModeShell;
