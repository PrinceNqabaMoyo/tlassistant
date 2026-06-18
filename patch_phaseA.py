import sys

scaffold_path = r'C:\Users\princ\fundile-tlassistant-vite\src\components\workspace\grade11\accounting\Grade11AccountingScaffold.jsx'

with open(scaffold_path, 'r', encoding='utf-8') as f:
    s_content = f.read()

# 1. Remove sample_answer and correct_value from hints
# Current hint code looks like:
#                             {renderQuestion?.sample_answer && (
#                                 <div className="mt-3 text-xs opacity-90">
#                                     <strong>Sample Answer:</strong>
#                                     <div className="text-sm text-slate-700 mt-1">{renderQuestion.sample_answer}</div>
#                                 </div>
#                             )}
s_content = s_content.replace(
"""                            {renderQuestion?.sample_answer && (
                                <div className="mt-3 text-xs opacity-90">
                                    <strong>Sample Answer:</strong>
                                    <div className="text-sm text-slate-700 mt-1">{renderQuestion.sample_answer}</div>
                                </div>
                            )}""",
"")

s_content = s_content.replace(
"""                            {renderQuestion?.correct_value && (
                                <div className="mt-3 text-xs opacity-90">
                                    <strong>Expected Answer:</strong> {renderQuestion.correct_value}
                                </div>
                            )}""",
"")


# 2. Add compare/memo for calc and journal (as well as typed)
# Current: {g11AcctScaffoldFeedback && question?.question_type === 'typed' && (
s_content = s_content.replace(
    "{g11AcctScaffoldFeedback && question?.question_type === 'typed' && (",
    "{g11AcctScaffoldFeedback && ['typed', 'calc', 'journal', 'ledger'].includes(question?.question_type) && (question?.sample_answer || question?.guidelines?.length > 0) && ("
)
s_content = s_content.replace(
    "{showMemo && question?.question_type === 'typed' && (",
    "{showMemo && ['typed', 'calc', 'journal', 'ledger'].includes(question?.question_type) && (question?.sample_answer || question?.guidelines?.length > 0) && ("
)

# 3. Change hardcoded feedback statements
s_content = s_content.replace(
    "setPartFeedback({ kind: 'info', message: 'Compare your answer to the sample answer / visual aids.' });",
    "setPartFeedback({ kind: 'info', message: 'Answer saved.' });"
)
s_content = s_content.replace(
    "setG11AcctScaffoldFeedback({ kind: 'info', message: 'Compare your answer to the sample answer / visual aids.' });",
    "setG11AcctScaffoldFeedback({ kind: 'info', message: 'Answer saved.' });"
)

with open(scaffold_path, 'w', encoding='utf-8') as f:
    f.write(s_content)


practice_path = r'C:\Users\princ\fundile-tlassistant-vite\src\components\workspace\grade11\accounting\Grade11AccountingPractice.jsx'

with open(practice_path, 'r', encoding='utf-8') as f:
    p_content = f.read()

# 2. Add compare/memo for calc and journal
p_content = p_content.replace(
    "{fb && part.question_type === 'typed' && (",
    "{fb && ['typed', 'calc', 'journal', 'ledger'].includes(part.question_type) && (part.sample_answer || part.guidelines?.length > 0) && ("
)
p_content = p_content.replace(
    "{memoOpenById[part.id] && part.question_type === 'typed' && (",
    "{memoOpenById[part.id] && ['typed', 'calc', 'journal', 'ledger'].includes(part.question_type) && (part.sample_answer || part.guidelines?.length > 0) && ("
)
p_content = p_content.replace(
    "{displayFeedback && q.question_type === 'typed' && (",
    "{displayFeedback && ['typed', 'calc', 'journal', 'ledger'].includes(q.question_type) && (q.sample_answer || q.guidelines?.length > 0) && ("
)
p_content = p_content.replace(
    "{memoOpenById[q.id] && q.question_type === 'typed' && (",
    "{memoOpenById[q.id] && ['typed', 'calc', 'journal', 'ledger'].includes(q.question_type) && (q.sample_answer || q.guidelines?.length > 0) && ("
)

# 3. Change hardcoded feedback statements
p_content = p_content.replace(
    "{ kind: 'info', message: 'Saved. Compare your answer to the sample answer / visual aids.' }",
    "{ kind: 'info', message: 'Answer saved.' }"
)

with open(practice_path, 'w', encoding='utf-8') as f:
    f.write(p_content)

print("Patched Phase A UI")
