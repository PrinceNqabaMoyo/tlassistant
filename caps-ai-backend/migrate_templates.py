#!/usr/bin/env python3
"""
Template Migration Script
Extracts templates from the old monolithic file and migrates them to the modular structure
"""

import sys
import os
import re
from typing import List, Dict, Any

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.utils.quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType

def extract_templates_from_file(file_path: str) -> Dict[str, List[QuestionTemplate]]:
    """Extract all templates from the old monolithic file"""
    templates = {
        'triangle_easy': [],
        'triangle_medium': [],
        'triangle_hard': [],
        'quadrilateral_easy': [],
        'quadrilateral_medium': [],
        'quadrilateral_hard': [],
        'circle_easy': [],
        'circle_medium': [],
        'circle_hard': [],
        'angle_easy': [],
        'angle_medium': [],
        'angle_hard': [],
        'composite_area_easy': [],
        'composite_area_medium': [],
        'composite_area_hard': [],
        'classification_easy': [],
        'classification_medium': [],
        'classification_hard': [],
        'similarity_congruency_easy': [],
        'similarity_congruency_medium': [],
        'similarity_congruency_hard': []
    }
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract triangle easy templates
    triangle_easy_match = re.search(r'def _create_triangle_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if triangle_easy_match:
        triangle_easy_code = triangle_easy_match.group(0)
        templates['triangle_easy'] = extract_templates_from_code(triangle_easy_code)
    
    # Extract triangle medium templates
    triangle_medium_match = re.search(r'def _create_triangle_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if triangle_medium_match:
        triangle_medium_code = triangle_medium_match.group(0)
        templates['triangle_medium'] = extract_templates_from_code(triangle_medium_code)
    
    # Extract triangle hard templates
    triangle_hard_match = re.search(r'def _create_triangle_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if triangle_hard_match:
        triangle_hard_code = triangle_hard_match.group(0)
        templates['triangle_hard'] = extract_templates_from_code(triangle_hard_code)
    
    # Extract quadrilateral templates
    quadrilateral_easy_match = re.search(r'def _create_quadrilateral_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if quadrilateral_easy_match:
        quadrilateral_easy_code = quadrilateral_easy_match.group(0)
        templates['quadrilateral_easy'] = extract_templates_from_code(quadrilateral_easy_code)
    
    quadrilateral_medium_match = re.search(r'def _create_quadrilateral_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if quadrilateral_medium_match:
        quadrilateral_medium_code = quadrilateral_medium_match.group(0)
        templates['quadrilateral_medium'] = extract_templates_from_code(quadrilateral_medium_code)
    
    quadrilateral_hard_match = re.search(r'def _create_quadrilateral_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if quadrilateral_hard_match:
        quadrilateral_hard_code = quadrilateral_hard_match.group(0)
        templates['quadrilateral_hard'] = extract_templates_from_code(quadrilateral_hard_code)
    
    # Extract circle templates
    circle_easy_match = re.search(r'def _create_circle_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if circle_easy_match:
        circle_easy_code = circle_easy_match.group(0)
        templates['circle_easy'] = extract_templates_from_code(circle_easy_code)
    
    circle_medium_match = re.search(r'def _create_circle_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if circle_medium_match:
        circle_medium_code = circle_medium_match.group(0)
        templates['circle_medium'] = extract_templates_from_code(circle_medium_code)
    
    circle_hard_match = re.search(r'def _create_circle_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if circle_hard_match:
        circle_hard_code = circle_hard_match.group(0)
        templates['circle_hard'] = extract_templates_from_code(circle_hard_code)
    
    # Extract angle templates
    angle_easy_match = re.search(r'def _create_angle_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if angle_easy_match:
        angle_easy_code = angle_easy_match.group(0)
        templates['angle_easy'] = extract_templates_from_code(angle_easy_code)
    
    angle_medium_match = re.search(r'def _create_angle_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if angle_medium_match:
        angle_medium_code = angle_medium_match.group(0)
        templates['angle_medium'] = extract_templates_from_code(angle_medium_code)
    
    angle_hard_match = re.search(r'def _create_angle_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if angle_hard_match:
        angle_hard_code = angle_hard_match.group(0)
        templates['angle_hard'] = extract_templates_from_code(angle_hard_code)
    
    # Extract composite area templates
    composite_easy_match = re.search(r'def _create_composite_area_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if composite_easy_match:
        composite_easy_code = composite_easy_match.group(0)
        templates['composite_area_easy'] = extract_templates_from_code(composite_easy_code)
    
    composite_medium_match = re.search(r'def _create_composite_area_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if composite_medium_match:
        composite_medium_code = composite_medium_match.group(0)
        templates['composite_area_medium'] = extract_templates_from_code(composite_medium_code)
    
    composite_hard_match = re.search(r'def _create_composite_area_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if composite_hard_match:
        composite_hard_code = composite_hard_match.group(0)
        templates['composite_area_hard'] = extract_templates_from_code(composite_hard_code)
    
    # Extract classification templates
    classification_easy_match = re.search(r'def _create_quadrilateral_classification_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if classification_easy_match:
        classification_easy_code = classification_easy_match.group(0)
        templates['classification_easy'] = extract_templates_from_code(classification_easy_code)
    
    classification_medium_match = re.search(r'def _create_quadrilateral_classification_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if classification_medium_match:
        classification_medium_code = classification_medium_match.group(0)
        templates['classification_medium'] = extract_templates_from_code(classification_medium_code)
    
    classification_hard_match = re.search(r'def _create_quadrilateral_classification_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if classification_hard_match:
        classification_hard_code = classification_hard_match.group(0)
        templates['classification_hard'] = extract_templates_from_code(classification_hard_code)
    
    # Extract similarity/congruency templates
    similarity_easy_match = re.search(r'def _create_similarity_congruency_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if similarity_easy_match:
        similarity_easy_code = similarity_easy_match.group(0)
        templates['similarity_congruency_easy'] = extract_templates_from_code(similarity_easy_code)
    
    similarity_medium_match = re.search(r'def _create_similarity_congruency_medium_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if similarity_medium_match:
        similarity_medium_code = similarity_medium_match.group(0)
        templates['similarity_congruency_medium'] = extract_templates_from_code(similarity_medium_code)
    
    similarity_hard_match = re.search(r'def _create_similarity_congruency_hard_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if similarity_hard_match:
        similarity_hard_code = similarity_hard_match.group(0)
        templates['similarity_congruency_hard'] = extract_templates_from_code(similarity_hard_code)
    
    return templates

def extract_templates_from_code(code: str) -> List[QuestionTemplate]:
    """Extract QuestionTemplate objects from code string"""
    templates = []
    
    # Find all QuestionTemplate constructor calls
    template_pattern = r'QuestionTemplate\(\s*template_id="([^"]+)",\s*question_template="([^"]+)",\s*parameter_ranges=([^,]+),\s*constraints=([^,]+),\s*difficulty=([^,]+),\s*topic="([^"]+)",\s*question_type=([^,]+),\s*shape_type=([^,]+),\s*metric_units=([^,]+),\s*conversion_types=([^,]+),\s*real_world_context=\'([^\']+)\',\s*south_african_context=([^,]+),\s*reasoning_required=([^)]+)\)'
    
    matches = re.findall(template_pattern, code, re.DOTALL)
    
    for match in matches:
        try:
            template_id, question_template, parameter_ranges, constraints, difficulty, topic, question_type, shape_type, metric_units, conversion_types, real_world_context, south_african_context, reasoning_required = match
            
            # Parse the values
            parameter_ranges_dict = eval(parameter_ranges.strip())
            constraints_list = eval(constraints.strip())
            difficulty_enum = getattr(DifficultyLevel, difficulty.strip().split('.')[-1])
            question_type_enum = getattr(QuestionType, question_type.strip().split('.')[-1])
            shape_type_enum = getattr(ShapeType, shape_type.strip().split('.')[-1])
            metric_units_list = eval(metric_units.strip())
            conversion_types_list = eval(conversion_types.strip())
            south_african_context_bool = eval(south_african_context.strip())
            reasoning_required_bool = eval(reasoning_required.strip())
            
            template = QuestionTemplate(
                template_id=template_id,
                question_template=question_template,
                parameter_ranges=parameter_ranges_dict,
                constraints=constraints_list,
                difficulty=difficulty_enum,
                topic=topic,
                question_type=question_type_enum,
                shape_type=shape_type_enum,
                metric_units=metric_units_list,
                conversion_types=conversion_types_list,
                real_world_context=real_world_context,
                south_african_context=south_african_context_bool,
                reasoning_required=reasoning_required_bool
            )
            
            templates.append(template)
            
        except Exception as e:
            print(f"Error parsing template: {e}")
            continue
    
    return templates

def generate_triangle_file(templates: Dict[str, List[QuestionTemplate]]) -> str:
    """Generate the triangles.py file content"""
    content = '''"""
Grade 7 Triangle Templates
Contains 60 triangle templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Triangles:
    """
    Grade 7 Triangle Templates
    Provides triangle-specific templates for Grade 7
    """
    
    def get_easy_templates(self) -> List[QuestionTemplate]:
        """Get 20 easy triangle templates"""
        templates = []
        
'''
    
    # Add easy templates
    for template in templates['triangle_easy']:
        content += f'''        templates.append(QuestionTemplate(
            template_id="{template.template_id}",
            question_template="{template.question_template}",
            parameter_ranges={template.parameter_ranges},
            constraints={template.constraints},
            difficulty=DifficultyLevel.{template.difficulty.name},
            topic="{template.topic}",
            question_type=QuestionType.{template.question_type.name},
            shape_type=ShapeType.{template.shape_type.name},
            metric_units={template.metric_units},
            conversion_types={template.conversion_types},
            real_world_context='{template.real_world_context}',
            south_african_context={template.south_african_context},
            reasoning_required={template.reasoning_required}
        ))
        
'''
    
    content += '''        return templates
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium triangle templates"""
        templates = []
        
'''
    
    # Add medium templates
    for template in templates['triangle_medium']:
        content += f'''        templates.append(QuestionTemplate(
            template_id="{template.template_id}",
            question_template="{template.question_template}",
            parameter_ranges={template.parameter_ranges},
            constraints={template.constraints},
            difficulty=DifficultyLevel.{template.difficulty.name},
            topic="{template.topic}",
            question_type=QuestionType.{template.question_type.name},
            shape_type=ShapeType.{template.shape_type.name},
            metric_units={template.metric_units},
            conversion_types={template.conversion_types},
            real_world_context='{template.real_world_context}',
            south_african_context={template.south_african_context},
            reasoning_required={template.reasoning_required}
        ))
        
'''
    
    content += '''        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard triangle templates"""
        templates = []
        
'''
    
    # Add hard templates
    for template in templates['triangle_hard']:
        content += f'''        templates.append(QuestionTemplate(
            template_id="{template.template_id}",
            question_template="{template.question_template}",
            parameter_ranges={template.parameter_ranges},
            constraints={template.constraints},
            difficulty=DifficultyLevel.{template.difficulty.name},
            topic="{template.topic}",
            question_type=QuestionType.{template.question_type.name},
            shape_type=ShapeType.{template.shape_type.name},
            metric_units={template.metric_units},
            conversion_types={template.conversion_types},
            real_world_context='{template.real_world_context}',
            south_african_context={template.south_african_context},
            reasoning_required={template.reasoning_required}
        ))
        
'''
    
    content += '''        return templates
'''
    
    return content

def main():
    """Main migration function"""
    print("Starting template migration...")
    
    # Extract templates from old file
    old_file_path = "app/utils/question_templates.py"
    templates = extract_templates_from_file(old_file_path)
    
    print(f"Extracted templates:")
    for key, template_list in templates.items():
        print(f"  {key}: {len(template_list)} templates")
    
    # Generate triangle file
    triangle_content = generate_triangle_file(templates)
    
    # Write triangle file
    triangle_file_path = "app/utils/templates/grade7/triangles.py"
    with open(triangle_file_path, 'w', encoding='utf-8') as f:
        f.write(triangle_content)
    
    print(f"Generated {triangle_file_path}")
    print("Migration completed!")

if __name__ == "__main__":
    main()
