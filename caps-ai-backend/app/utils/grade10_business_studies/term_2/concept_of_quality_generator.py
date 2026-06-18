import random

def _generate_concepts_mcq(count: int, difficulty: str) -> list:
    """Generate MCQ concept questions for Concept of quality."""
    system_prompt = (
        "You are an expert Grade 10 Business Studies examiner in South Africa. "
        "Generate a JSON list of MCQ questions on 'Topic 11: Concept of quality'. "
        "Focus on defining quality, quality control vs quality assurance, total quality management (TQM), "
        "quality circles, and the importance of quality for a business (e.g., customer satisfaction, reduced costs)."
        "Questions should be strictly multiple-choice with 4 options. Include the correct option index."
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
    """Generate typed discussion questions for Concept of quality."""
    system_prompt = (
        "You are an expert Grade 10 Business Studies examiner. "
        "Generate a JSON list of semantic/essay/discussion questions on 'Topic 11: Concept of quality'. "
        "Focus on: distinguishing between quality control and quality assurance, "
        "explaining how various business functions contribute to quality (e.g., HR, Production, Marketing), "
        "and evaluating the impact of poor quality on a business."
    )
    
    prompt = (
        f"Generate {count} discussion questions at a {difficulty} difficulty level. "
        "Return pure JSON list in this format:\n"
        "[\n"
        "  {\n"
        "    \"id\": \"unique_id\",\n"
        "    \"question_type\": \"typed\",\n"
        "    \"prompt\": \"Provide a clear prompt asking the student to discuss, explain, or outline.\",\n"
        "    \"required_points\": [\"Point 1 that must be mentioned\", \"Point 2\", \"Point 3\"],\n"
        "    \"explanation\": \"A model answer or explanation of what is expected.\",\n"
        "    \"marks\": 8\n"
        "  }\n"
        "]\n"
        "Ensure 'required_points' contains the key concepts a student must include to get full marks."
    )
    
    return generate_questions_with_llm(system_prompt, prompt, count)

def generate_concept_of_quality(subskill: str, difficulty: str, count: int) -> dict:
    """
    Main router for Concept of quality generation.
    """
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
            
        return {
            "success": True,
            "questions": questions
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
