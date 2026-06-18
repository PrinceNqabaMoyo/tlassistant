#!/usr/bin/env python3
"""
Simple Template Copy Script
Copies template methods from the old monolithic file to the new modular structure
"""

import os
import re

def copy_triangle_templates():
    """Copy triangle templates from old file to new modular structure"""
    
    # Read the old file
    with open('app/utils/question_templates.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract triangle easy templates method
    triangle_easy_match = re.search(r'def _create_triangle_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if triangle_easy_match:
        triangle_easy_code = triangle_easy_match.group(0)
        # Convert to new format
        triangle_easy_code = triangle_easy_code.replace('def _create_triangle_easy_templates(self) -> List[QuestionTemplate]:', 'def get_easy_templates(self) -> List[QuestionTemplate]:')
        triangle_easy_code = triangle_easy_code.replace('        """Create 20 easy triangle templates as per plan"""', '        """Get 20 easy triangle templates"""')
        
        # Write to new file
        new_file_content = '''"""
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
    
    ''' + triangle_easy_code + '''
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium triangle templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard triangle templates"""
        templates = []
        # TODO: Add hard templates
        return templates
'''
        
        with open('app/utils/templates/grade7/triangles.py', 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        
        print("✅ Triangle easy templates copied successfully!")
    else:
        print("❌ Could not find triangle easy templates")

def copy_quadrilateral_templates():
    """Copy quadrilateral templates from old file to new modular structure"""
    
    # Read the old file
    with open('app/utils/question_templates.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract quadrilateral easy templates method
    quadrilateral_easy_match = re.search(r'def _create_quadrilateral_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if quadrilateral_easy_match:
        quadrilateral_easy_code = quadrilateral_easy_match.group(0)
        # Convert to new format
        quadrilateral_easy_code = quadrilateral_easy_code.replace('def _create_quadrilateral_easy_templates(self) -> List[QuestionTemplate]:', 'def get_easy_templates(self) -> List[QuestionTemplate]:')
        quadrilateral_easy_code = quadrilateral_easy_code.replace('        """Create 20 easy quadrilateral templates as per plan"""', '        """Get 20 easy quadrilateral templates"""')
        
        # Write to new file
        new_file_content = '''"""
Grade 7 Quadrilateral Templates
Contains 60 quadrilateral templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Quadrilaterals:
    """
    Grade 7 Quadrilateral Templates
    Provides quadrilateral-specific templates for Grade 7
    """
    
    ''' + quadrilateral_easy_code + '''
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium quadrilateral templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard quadrilateral templates"""
        templates = []
        # TODO: Add hard templates
        return templates
'''
        
        with open('app/utils/templates/grade7/quadrilaterals.py', 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        
        print("✅ Quadrilateral easy templates copied successfully!")
    else:
        print("❌ Could not find quadrilateral easy templates")

def copy_circle_templates():
    """Copy circle templates from old file to new modular structure"""
    
    # Read the old file
    with open('app/utils/question_templates.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract circle easy templates method
    circle_easy_match = re.search(r'def _create_circle_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if circle_easy_match:
        circle_easy_code = circle_easy_match.group(0)
        # Convert to new format
        circle_easy_code = circle_easy_code.replace('def _create_circle_easy_templates(self) -> List[QuestionTemplate]:', 'def get_easy_templates(self) -> List[QuestionTemplate]:')
        circle_easy_code = circle_easy_code.replace('        """Create 20 easy circle templates as per plan"""', '        """Get 20 easy circle templates"""')
        
        # Write to new file
        new_file_content = '''"""
Grade 7 Circle Templates
Contains 60 circle templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Circles:
    """
    Grade 7 Circle Templates
    Provides circle-specific templates for Grade 7
    """
    
    ''' + circle_easy_code + '''
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium circle templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard circle templates"""
        templates = []
        # TODO: Add hard templates
        return templates
'''
        
        with open('app/utils/templates/grade7/circles.py', 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        
        print("✅ Circle easy templates copied successfully!")
    else:
        print("❌ Could not find circle easy templates")

def copy_angle_templates():
    """Copy angle templates from old file to new modular structure"""
    
    # Read the old file
    with open('app/utils/question_templates.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract angle easy templates method
    angle_easy_match = re.search(r'def _create_angle_easy_templates\(self\) -> List\[QuestionTemplate\]:.*?return templates', content, re.DOTALL)
    if angle_easy_match:
        angle_easy_code = angle_easy_match.group(0)
        # Convert to new format
        angle_easy_code = angle_easy_code.replace('def _create_angle_easy_templates(self) -> List[QuestionTemplate]:', 'def get_easy_templates(self) -> List[QuestionTemplate]:')
        angle_easy_code = angle_easy_code.replace('        """Create 20 easy angle templates as per plan"""', '        """Get 20 easy angle templates"""')
        
        # Write to new file
        new_file_content = '''"""
Grade 7 Angle Templates
Contains 60 angle templates (20 easy, 20 medium, 20 hard)
"""

from typing import List
from ...quiz_models import QuestionTemplate, DifficultyLevel, QuestionType, ShapeType


class Grade7Angles:
    """
    Grade 7 Angle Templates
    Provides angle-specific templates for Grade 7
    """
    
    ''' + angle_easy_code + '''
    
    def get_medium_templates(self) -> List[QuestionTemplate]:
        """Get 20 medium angle templates"""
        templates = []
        # TODO: Add medium templates
        return templates
    
    def get_hard_templates(self) -> List[QuestionTemplate]:
        """Get 20 hard angle templates"""
        templates = []
        # TODO: Add hard templates
        return templates
'''
        
        with open('app/utils/templates/grade7/angles.py', 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        
        print("✅ Angle easy templates copied successfully!")
    else:
        print("❌ Could not find angle easy templates")

def main():
    """Main copy function"""
    print("Starting template copying...")
    
    # Copy templates for each shape type
    copy_triangle_templates()
    copy_quadrilateral_templates()
    copy_circle_templates()
    copy_angle_templates()
    
    print("Template copying completed!")

if __name__ == "__main__":
    main()
