"""
Grade 7 Similarity & Congruency Templates
Contains 60 similarity/congruency templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7SimilarityCongruency:
    """Grade 7 Similarity & Congruency Templates"""
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy similarity/congruency templates"""
        templates = []
        
        # Template 1: Basic triangle similarity
        templates.append(QuestionTemplate(
            template_id="similarity_easy_1",
            question_template="Triangle A has sides {a1} cm, {b1} cm, {c1} cm. Triangle B has sides {a2} cm, {b2} cm, {c2} cm. Are these triangles similar?",
            parameter_ranges={'a1': (3, 6), 'b1': (4, 8), 'c1': (5, 10), 'a2': (6, 12), 'b2': (8, 16), 'c2': (10, 20)},
            constraints=['triangle_inequality', 'similarity_ratio'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 2: Basic triangle congruency
        templates.append(QuestionTemplate(
            template_id="congruency_easy_1",
            question_template="Triangle A has sides {a1} cm, {b1} cm, {c1} cm. Triangle B has sides {a2} cm, {b2} cm, {c2} cm. Are these triangles congruent?",
            parameter_ranges={'a1': (3, 5), 'b1': (4, 6), 'c1': (5, 7), 'a2': (3, 5), 'b2': (4, 6), 'c2': (5, 7)},
            constraints=['triangle_inequality', 'congruency_check'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 3: Rectangle similarity
        templates.append(QuestionTemplate(
            template_id="similarity_easy_2",
            question_template="Rectangle A is {l1} cm × {w1} cm. Rectangle B is {l2} cm × {w2} cm. Are these rectangles similar?",
            parameter_ranges={'l1': (2, 4), 'w1': (3, 6), 'l2': (4, 8), 'w2': (6, 12)},
            constraints=['positive_dimensions', 'similarity_ratio'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 4: Square congruency
        templates.append(QuestionTemplate(
            template_id="congruency_easy_2",
            question_template="Square A has side length {s1} cm. Square B has side length {s2} cm. Are these squares congruent?",
            parameter_ranges={'s1': (3, 5), 's2': (3, 5)},
            constraints=['positive_dimensions', 'congruency_check'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.SQUARE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Template 5: Circle similarity
        templates.append(QuestionTemplate(
            template_id="similarity_easy_3",
            question_template="Circle A has radius {r1} cm. Circle B has radius {r2} cm. Are these circles similar?",
            parameter_ranges={'r1': (2, 4), 'r2': (4, 8)},
            constraints=['positive_dimensions', 'similarity_ratio'],
            difficulty=DifficultyLevel.EASY,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=False
        ))
        
        # Add 15 more easy templates with variety
        for i in range(6, 21):
            if i % 3 == 0:  # Every third template is congruency
                templates.append(QuestionTemplate(
                    template_id=f"congruency_easy_{i-2}",
                    question_template=f"Are these shapes congruent? Shape A: {i} cm sides. Shape B: {i} cm sides.",
                    parameter_ranges={'side': (3, 8)},
                    constraints=['positive_dimensions', 'congruency_check'],
                    difficulty=DifficultyLevel.EASY,
                    topic="Properties of 2D Shapes",
                    question_type=QuestionType.SHAPE_CLASSIFICATION,
                    shape_type=ShapeType.TRIANGLE_EQUILATERAL,
                    metric_units=['cm'],
                    conversion_types=[],
                    real_world_context='school',
                    south_african_context=True,
                    reasoning_required=False
                ))
            else:  # Similarity templates
                templates.append(QuestionTemplate(
                    template_id=f"similarity_easy_{i-1}",
                    question_template=f"Are these shapes similar? Shape A: {i} cm sides. Shape B: {i*2} cm sides.",
                    parameter_ranges={'side': (3, 8)},
                    constraints=['positive_dimensions', 'similarity_ratio'],
                    difficulty=DifficultyLevel.EASY,
                    topic="Properties of 2D Shapes",
                    question_type=QuestionType.SHAPE_CLASSIFICATION,
                    shape_type=ShapeType.TRIANGLE_EQUILATERAL,
                    metric_units=['cm'],
                    conversion_types=[],
                    real_world_context='school',
                    south_african_context=True,
                    reasoning_required=False
                ))
        
        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium similarity/congruency templates"""
        templates = []
        
        # Template 1: Triangle similarity with angles
        templates.append(QuestionTemplate(
            template_id="similarity_medium_1",
            question_template="Triangle A has angles {angle1}°, {angle2}°, {angle3}° and sides {a1} cm, {b1} cm, {c1} cm. Triangle B has angles {angle1}°, {angle2}°, {angle3}° and sides {a2} cm, {b2} cm, {c2} cm. Are these triangles similar?",
            parameter_ranges={'angle1': (30, 60), 'angle2': (60, 90), 'angle3': (30, 90), 'a1': (4, 8), 'b1': (5, 10), 'c1': (6, 12), 'a2': (8, 16), 'b2': (10, 20), 'c2': (12, 24)},
            constraints=['triangle_inequality', 'angle_sum_180', 'similarity_ratio'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm', 'degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 2: Quadrilateral similarity
        templates.append(QuestionTemplate(
            template_id="similarity_medium_2",
            question_template="Quadrilateral A has sides {a1} cm, {b1} cm, {c1} cm, {d1} cm. Quadrilateral B has sides {a2} cm, {b2} cm, {c2} cm, {d2} cm. Are these quadrilaterals similar?",
            parameter_ranges={'a1': (3, 6), 'b1': (4, 8), 'c1': (3, 6), 'd1': (4, 8), 'a2': (6, 12), 'b2': (8, 16), 'c2': (6, 12), 'd2': (8, 16)},
            constraints=['positive_dimensions', 'similarity_ratio'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 3: Circle congruency with area
        templates.append(QuestionTemplate(
            template_id="congruency_medium_1",
            question_template="Circle A has radius {r1} cm and area {area1} cm². Circle B has radius {r2} cm and area {area2} cm². Are these circles congruent?",
            parameter_ranges={'r1': (3, 5), 'r2': (3, 5), 'area1': (28, 78), 'area2': (28, 78)},
            constraints=['positive_dimensions', 'congruency_check', 'area_radius_consistency'],
            difficulty=DifficultyLevel.MEDIUM,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm', 'cm²'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Add 17 more medium templates with variety
        for i in range(4, 21):
            if i % 4 == 0:  # Every fourth template is congruency
                templates.append(QuestionTemplate(
                    template_id=f"congruency_medium_{i-3}",
                    question_template=f"Are these shapes congruent? Explain your reasoning. Shape A: {i} cm sides. Shape B: {i} cm sides.",
                    parameter_ranges={'side': (4, 12)},
                    constraints=['positive_dimensions', 'congruency_check'],
                    difficulty=DifficultyLevel.MEDIUM,
                    topic="Properties of 2D Shapes",
                    question_type=QuestionType.SHAPE_CLASSIFICATION,
                    shape_type=ShapeType.TRIANGLE_EQUILATERAL,
                    metric_units=['cm'],
                    conversion_types=[],
                    real_world_context='school',
                    south_african_context=True,
                    reasoning_required=True
                ))
            else:  # Similarity templates
                templates.append(QuestionTemplate(
                    template_id=f"similarity_medium_{i-2}",
                    question_template=f"Are these shapes similar? Explain your reasoning. Shape A: {i} cm sides. Shape B: {i*1.5} cm sides.",
                    parameter_ranges={'side': (4, 12)},
                    constraints=['positive_dimensions', 'similarity_ratio'],
                    difficulty=DifficultyLevel.MEDIUM,
                    topic="Properties of 2D Shapes",
                    question_type=QuestionType.SHAPE_CLASSIFICATION,
                    shape_type=ShapeType.TRIANGLE_EQUILATERAL,
                    metric_units=['cm'],
                    conversion_types=[],
                    real_world_context='school',
                    south_african_context=True,
                    reasoning_required=True
                ))
        
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard similarity/congruency templates"""
        templates = []
        
        # Template 1: Complex triangle similarity with multiple criteria
        templates.append(QuestionTemplate(
            template_id="similarity_hard_1",
            question_template="Triangle A has angles {angle1}°, {angle2}°, {angle3}° and sides {a1} cm, {b1} cm, {c1} cm. Triangle B has angles {angle4}°, {angle5}°, {angle6}° and sides {a2} cm, {b2} cm, {c2} cm. Are these triangles similar? Justify your answer with detailed reasoning.",
            parameter_ranges={'angle1': (30, 60), 'angle2': (60, 90), 'angle3': (30, 90), 'angle4': (30, 60), 'angle5': (60, 90), 'angle6': (30, 90), 'a1': (6, 12), 'b1': (8, 16), 'c1': (10, 20), 'a2': (9, 18), 'b2': (12, 24), 'c2': (15, 30)},
            constraints=['triangle_inequality', 'angle_sum_180', 'similarity_ratio', 'angle_consistency'],
            difficulty=DifficultyLevel.HARD,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.TRIANGLE_EQUILATERAL,
            metric_units=['cm', 'degrees'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 2: Multiple shape comparison
        templates.append(QuestionTemplate(
            template_id="similarity_hard_2",
            question_template="Compare three shapes: Shape A ({a1} cm × {b1} cm), Shape B ({a2} cm × {b2} cm), and Shape C ({a3} cm × {b3} cm). Which shapes are similar? Which are congruent? Provide detailed analysis.",
            parameter_ranges={'a1': (4, 8), 'b1': (6, 12), 'a2': (8, 16), 'b2': (12, 24), 'a3': (4, 8), 'b3': (6, 12)},
            constraints=['positive_dimensions', 'similarity_ratio', 'congruency_check'],
            difficulty=DifficultyLevel.HARD,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.RECTANGLE,
            metric_units=['cm'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Template 3: Circle similarity with circumference and area
        templates.append(QuestionTemplate(
            template_id="similarity_hard_3",
            question_template="Circle A has radius {r1} cm, circumference {c1} cm, and area {area1} cm². Circle B has radius {r2} cm, circumference {c2} cm, and area {area2} cm². Are these circles similar? Explain using both circumference and area relationships.",
            parameter_ranges={'r1': (3, 6), 'r2': (6, 12), 'c1': (18, 37), 'c2': (37, 75), 'area1': (28, 113), 'area2': (113, 452)},
            constraints=['positive_dimensions', 'similarity_ratio', 'circumference_radius_consistency', 'area_radius_consistency'],
            difficulty=DifficultyLevel.HARD,
            topic="Properties of 2D Shapes",
            question_type=QuestionType.SHAPE_CLASSIFICATION,
            shape_type=ShapeType.CIRCLE,
            metric_units=['cm', 'cm²'],
            conversion_types=[],
            real_world_context='school',
            south_african_context=True,
            reasoning_required=True
        ))
        
        # Add 17 more hard templates with variety
        for i in range(4, 21):
            if i % 5 == 0:  # Every fifth template is congruency
                templates.append(QuestionTemplate(
                    template_id=f"congruency_hard_{i-3}",
                    question_template=f"Are these shapes congruent? Provide detailed mathematical proof. Shape A: {i} cm sides with angles {i*10}°, {i*15}°, {i*20}°. Shape B: {i} cm sides with angles {i*10}°, {i*15}°, {i*20}°.",
                    parameter_ranges={'side': (6, 15), 'angle1': (30, 90), 'angle2': (45, 120), 'angle3': (60, 150)},
                    constraints=['positive_dimensions', 'congruency_check', 'angle_sum_180'],
                    difficulty=DifficultyLevel.HARD,
                    topic="Properties of 2D Shapes",
                    question_type=QuestionType.SHAPE_CLASSIFICATION,
                    shape_type=ShapeType.TRIANGLE_EQUILATERAL,
                    metric_units=['cm', 'degrees'],
                    conversion_types=[],
                    real_world_context='school',
                    south_african_context=True,
                    reasoning_required=True
                ))
            else:  # Similarity templates
                templates.append(QuestionTemplate(
                    template_id=f"similarity_hard_{i-2}",
                    question_template=f"Are these shapes similar? Provide detailed mathematical proof. Shape A: {i} cm sides. Shape B: {i*2} cm sides. Include ratio analysis and angle comparison.",
                    parameter_ranges={'side': (6, 15)},
                    constraints=['positive_dimensions', 'similarity_ratio', 'angle_consistency'],
                    difficulty=DifficultyLevel.HARD,
                    topic="Properties of 2D Shapes",
                    question_type=QuestionType.SHAPE_CLASSIFICATION,
                    shape_type=ShapeType.TRIANGLE_EQUILATERAL,
                    metric_units=['cm'],
                    conversion_types=[],
                    real_world_context='school',
                    south_african_context=True,
                    reasoning_required=True
                ))
        
        return templates
