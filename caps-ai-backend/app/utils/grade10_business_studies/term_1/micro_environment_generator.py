import random

def generate_concepts(difficulty="medium", count=1, **kwargs):
    questions = []
    
    # Pool of MCQ questions based on the curriculum
    concept_pool = [
        {
            "prompt": "Which of the following components belongs to the micro environment?",
            "options": ["Suppliers", "Competitors", "Vision and Mission", "Economic factors"],
            "correct_index": 2,
            "explanation": "The vision and mission statement are internal components managed by the business itself, falling under the micro environment."
        },
        {
            "prompt": "What does a business's 'Mission Statement' primarily describe?",
            "options": [
                "Its long-term dream or goal for the future",
                "What the business provides, produces, and why it exists",
                "The way employees communicate with each other",
                "The exact steps taken to advertise products"
            ],
            "correct_index": 1,
            "explanation": "The mission statement describes what the business provides or produces, and why the business exists."
        },
        {
            "prompt": "Which resource category do raw materials, machinery, and vehicles fall under?",
            "options": ["Human resources", "Technological resources", "Physical resources", "Financial resources"],
            "correct_index": 2,
            "explanation": "Physical resources are tangible items like raw materials, buildings, machinery, and vehicles."
        },
        {
            "prompt": "Which of the following statements best describes 'Organisational Culture'?",
            "options": [
                "The hierarchy of managers and subordinates",
                "The physical assets owned by the business",
                "The way things are done, including values, beliefs, and dress code",
                "The long-term plans the business wants to accomplish"
            ],
            "correct_index": 2,
            "explanation": "Organisational culture refers to how things are done, including norms, values, beliefs, and dress code shared among employees."
        },
        {
            "prompt": "Which function is responsible for changing/processing raw materials into finished or semi-finished products?",
            "options": ["Purchasing function", "Production function", "Administration function", "Marketing function"],
            "correct_index": 1,
            "explanation": "The production function is responsible for changing raw materials into finished products."
        }
    ]

    selected = random.sample(concept_pool, min(count, len(concept_pool)))
    
    for q in selected:
        questions.append({
            "id": f"mcq_{random.randint(1000, 9999)}",
            "question_type": "mcq",
            "prompt": q["prompt"],
            "options": q["options"],
            "correct_index": str(q["correct_index"]),
            "explanation": q["explanation"],
            "marks": 1
        })
        
    return questions

def generate_discussion(difficulty="medium", count=1, **kwargs):
    questions = []
    
    # Essay / Semantic Questions
    discussion_pool = [
        {
            "prompt": "Outline the purpose of organisational culture in a business. (4 marks)",
            "marking_points": [
                "Defines the business' internal and external identity and core values.",
                "Has the power to turn employees into ambassadors of the business.",
                "Helps the business to retain its employees and clients.",
                "Breaks down boundaries between teams, guides decision-making, and improves productivity."
            ],
            "sample_answer": "The purpose of organisational culture is to define the core values and identity of the business. A strong culture turns employees into ambassadors and helps retain both staff and clients. Furthermore, it guides decision-making, breaks down team boundaries, and ultimately improves overall productivity.",
            "marks": 4
        },
        {
            "prompt": "Explain the purpose of an organisational structure (organogram). (6 marks)",
            "marking_points": [
                "Helps ensure the smooth and efficient functioning of the business.",
                "Ensures work happens with precise co-ordination and minimum resource wastage.",
                "Helps the business work towards its goals.",
                "Shows the connections between various positions and tasks.",
                "Describes the coordination between various departments in the business."
            ],
            "sample_answer": "An organisational structure, or organogram, shows the connections between various positions and tasks. It ensures the smooth and efficient functioning of the business by coordinating departments. This allows work to happen with minimal wastage of resources and helps the business achieve its goals.",
            "marks": 6
        },
        {
            "prompt": "Differentiate between Management and Leadership. (4 marks)",
            "marking_points": [
                "Management is the process of guiding and directing the organisation to achieve goals.",
                "Managers plan, organise, lead, and control resources.",
                "Leadership is the ability to inspire, influence, or motivate subordinates.",
                "Leaders focus on influencing behaviour towards achieving objectives."
            ],
            "sample_answer": "Management is the process where individuals guide and direct the organisation by planning, organising, and controlling resources to achieve goals. In contrast, leadership focuses on the ability to inspire, influence, or motivate subordinates' behaviour towards achieving the business's objectives.",
            "marks": 4
        }
    ]

    selected = random.sample(discussion_pool, min(count, len(discussion_pool)))
    
    for q in selected:
        questions.append({
            "id": f"typed_{random.randint(1000, 9999)}",
            "question_type": "typed",
            "prompt": q["prompt"],
            "marking_points": q["marking_points"],
            "sample_answer": q["sample_answer"],
            "marks": q["marks"]
        })
        
    return questions

def generate(subskill="concepts", difficulty="medium", count=1, **kwargs):
    if subskill == "discussion":
        return generate_discussion(difficulty=difficulty, count=count, **kwargs)
    else:
        return generate_concepts(difficulty=difficulty, count=count, **kwargs)
