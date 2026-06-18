import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\concepts_generator.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix missing context in Gross Profit / Net Profit question
content = content.replace(
    'prompt=f"#### REQUIRED:\\nExplain the difference between gross profit and net profit to {scenario1[\'owner\']}.",',
    'prompt=f"{scenario1[\'intro\']}\\n\\n#### REQUIRED:\\nExplain the difference between gross profit and net profit to {scenario1[\'owner\']}.",',
)

# 2. Add new templates to ethics_pool
# Let's insert the new templates right after the existing ethics_pool appends.
new_ethics_code = """    ethics_pool.append(
        _make_table_wordbank(
            prompt="Match the ethics and internal control definitions with the correct term.",
            headers=["#", "Definition", "Term", ""],
            rows=[
                ["1", "Taking responsibility for what you say and do; being able to justify your actions.", "", ""],
                ["2", "Behaviour must be such that it is clear that you have nothing to hide.", "", ""],
                ["3", "Can be defined as honesty and upholding values and norms.", "", ""],
                ["4", "The ability to maintain economic, social and environmental resources.", "", ""]
            ],
            word_bank=[
                {"id": "t0", "label": "Accountability"},
                {"id": "t1", "label": "Transparency"},
                {"id": "t2", "label": "Integrity"},
                {"id": "t3", "label": "Sustainability"},
                {"id": "t4", "label": "Fairness"},
                {"id": "t5", "label": "Objectivity"}
            ],
            correct_map={
                "0": {"2": "t0", "3": None},
                "1": {"2": "t1", "3": None},
                "2": {"2": "t2", "3": None},
                "3": {"2": "t3", "3": None}
            },
            guidelines=[
                "Read each definition carefully.",
                "Choose one term from the word bank for each row."
            ]
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario1['intro']}\\n\\nThe coach of the local soccer team has selected his nephew for the team despite a string of poor performances by the player.\\n\\n#### REQUIRED:\\nExplain which ethical principle is being violated here, and why it is important for the coach to be objective.",
            sample_answer="The ethical principle being violated is objectivity / transparency. The coach is showing bias (favouritism). It is important to be objective so that players are selected on merit, ensuring the team performs at its best and public trust is maintained.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario2['intro']}\\n\\nAn employee of {scenario2['business']} has been using the company delivery vehicle to transport personal goods on weekends without permission.\\n\\n#### REQUIRED:\\nIdentify the internal control risk in this scenario, and suggest TWO internal control measures {scenario2['owner']} can implement to prevent this.",
            sample_answer="Risk: Unauthorised use of business assets (vehicle misuse) leading to wear and tear, and fuel theft.\\nInternal controls: \\n1. Keep vehicle keys locked in a safe and require sign-out logs.\\n2. Compare vehicle mileage logs to authorised delivery routes.",
            mode=mode_norm,
        )
    )

    ethics_pool.append(
        _make_typed(
            prompt=f"{scenario1['intro']}\\n\\n{scenario1['owner']} noticed that the cashier does not always deposit the cash received on the same day. She sometimes 'borrows' the cash for personal expenses and 'pays it back' at the end of the month.\\n\\n#### REQUIRED:\\nExplain why this behaviour is unethical and state ONE internal control measure that should be put in place regarding cash deposits.",
            sample_answer="This is unethical because it is essentially theft/fraud (rolling of cash); she is using business funds for personal use without authorisation. Internal control: Cash must be deposited daily, and duties should be divided so the person collecting cash is not the same person depositing and recording it (segregation of duties).",
            mode=mode_norm,
        )
    )

"""

# Insert it before matching_items
content = content.replace("    matching_items = [", new_ethics_code + "    matching_items = [")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched concepts_generator.py')
