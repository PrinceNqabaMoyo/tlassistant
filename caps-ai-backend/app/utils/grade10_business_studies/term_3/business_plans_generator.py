import random


def _generate_concepts_mcq(count: int, difficulty: str) -> list:
    """Generate MCQ concept questions for Topic 17: Understanding Business Plans and Implications."""
    system_prompt = (
        "You are an expert Grade 10 Business Studies examiner in South Africa following the CAPS curriculum. "
        "Generate a JSON list of MCQ questions on 'Topic 17: Understanding Business Plans and Implications'. "
        "Focus on the importance and components of a business plan, the PESTLE analysis of the macro environment, vision/mission statements, goals and objectives, the link between business structure and forms of ownership, legal requirements of a business, the marketing plan, and financial planning. "
        "Questions must be strictly multiple-choice with 4 plausible options and a single correct answer."
    )

    prompt = (
        f"Generate {count} MCQ questions at a {difficulty} difficulty level. "
        "Return pure JSON list in this format:\n"
        "[\n"
        "  {\n"
        "    \"id\": \"unique_id\",\n"
        "    \"question_type\": \"mcq\",\n"
        "    \"prompt\": \"Question text here?\",\n"
        "    \"options\": [\"A\", \"B\", \"C\", \"D\"],\n"
        "    \"correct_option_index\": 0,\n"
        "    \"explanation\": \"Why this is the correct answer.\",\n"
        "    \"marks\": 2\n"
        "  }\n"
        "]"
    )

    return generate_questions_with_llm(system_prompt, prompt, count)


def _generate_discussion(count: int, difficulty: str) -> list:
    """Generate typed discussion/essay questions for Topic 17: Understanding Business Plans and Implications."""
    system_prompt = (
        "You are an expert Grade 10 Business Studies examiner following the CAPS curriculum. "
        "Generate a JSON list of semantic/essay/discussion questions on 'Topic 17: Understanding Business Plans and Implications'. "
        "Focus on: explaining the importance and components of a business plan, distinguishing vision/mission/goals/objectives, applying a PESTLE analysis, and discussing strategies to overcome competition in the market."
    )

    prompt = (
        f"Generate {count} discussion questions at a {difficulty} difficulty level. "
        "Return pure JSON list in this format:\n"
        "[\n"
        "  {\n"
        "    \"id\": \"unique_id\",\n"
        "    \"question_type\": \"typed\",\n"
        "    \"prompt\": \"Provide a clear prompt asking the student to discuss, explain, evaluate or outline.\",\n"
        "    \"required_points\": [\"Point 1 that must be mentioned\", \"Point 2\", \"Point 3\"],\n"
        "    \"explanation\": \"A model answer or explanation of what is expected.\",\n"
        "    \"marks\": 8\n"
        "  }\n"
        "]\n"
        "Ensure 'required_points' contains the key concepts a student must include to get full marks."
    )

    return generate_questions_with_llm(system_prompt, prompt, count)


def generate_business_plans(subskill: str, difficulty: str, count: int) -> dict:
    """Main router for Topic 17: Understanding Business Plans and Implications generation."""
    try:
        questions = []
        if subskill == 'concepts':
            questions = _generate_concepts_mcq(count, difficulty)
        elif subskill == 'discussion':
            questions = _generate_discussion(count, difficulty)
        else:
            mcq_count = max(1, count // 2)
            disc_count = count - mcq_count
            mcqs = _generate_concepts_mcq(mcq_count, difficulty)
            discs = _generate_discussion(disc_count, difficulty)
            questions = mcqs + discs
            random.shuffle(questions)

        return {"success": True, "questions": questions}
    except Exception as e:
        return {"success": False, "error": str(e)}
