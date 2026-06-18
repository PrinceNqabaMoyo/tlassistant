# Enhanced Geometry Quiz System - Phase 1

## Overview

This is the Phase 1 implementation of the comprehensive geometry quiz enhancement system for the Fundile AI Learning Assistant. The system provides a robust, curriculum-aligned, multi-level question generation framework for Grade 7 Geometry.

## Features Implemented

### ✅ Phase 1 Complete

1. **Quiz System Architecture**
   - `QuizQuestion` dataclass with comprehensive metadata
   - `QuizGenerator` abstract base class
   - `GeometricConstraintValidator` for mathematical accuracy
   - `QuestionTemplate` system for pre-defined patterns

2. **Curriculum Mapping**
   - 11 main question categories mapped to Grade 7 requirements
   - 3 difficulty levels (Easy, Medium, Hard) with clear characteristics
   - Shape coverage for triangles, quadrilaterals, circles, and angles
   - South African curriculum alignment (CAPS)

3. **Geometric Constraint Validation**
   - Triangle inequality validation
   - Quadrilateral angle sum validation
   - Circle parameter validation
   - Metric unit conversion validation
   - Composite area calculation validation

4. **Dual Fail-Safe Generation System**
   - **Primary**: Constraint-based generation using geometric rules
   - **Fallback**: Template-based generation using pre-defined patterns
   - **Emergency**: Basic fallback questions

5. **Enhanced API Endpoints**
   - `POST /api/math/geometry/generate-quiz-question` - Enhanced quiz generation
   - `GET /api/math/geometry/quiz-templates/{topic}/{difficulty}` - Get templates
   - `POST /api/math/geometry/validate-parameters` - Validate parameters
   - `GET /api/math/geometry/curriculum-topics` - Get curriculum info
   - `GET /api/math/geometry/quiz-stats` - Get system statistics

## File Structure

```
caps-ai-backend/
├── app/
│   ├── models/
│   │   └── quiz_models.py              # Core data structures
│   ├── utils/
│   │   ├── geometric_validators.py    # Mathematical validation
│   │   ├── quiz_generators.py         # Question generation logic
│   │   └── curriculum_mapping.py      # Curriculum mapping
│   └── api/math/
│       └── quiz_routes.py             # Enhanced API endpoints
├── test_quiz_system.py                # Test script
└── QUIZ_SYSTEM_README.md             # This file
```

## Usage

### Backend Testing

1. **Start the Flask server:**
   ```bash
   cd caps-ai-backend
   python run.py
   ```

2. **Run the test script:**
   ```bash
   python test_quiz_system.py
   ```

### API Usage

#### Generate Quiz Questions

```bash
curl -X POST http://localhost:5001/api/math/geometry/generate-quiz-question \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Calculations involving 2D Shapes",
    "difficulty": "easy",
    "question_type": "area_calculation",
    "shape_type": "triangle_equilateral",
    "count": 3,
    "south_african_context": true
  }'
```

#### Get Curriculum Topics

```bash
curl http://localhost:5001/api/math/geometry/curriculum-topics
```

#### Validate Parameters

```bash
curl -X POST http://localhost:5001/api/math/geometry/validate-parameters \
  -H "Content-Type: application/json" \
  -d '{
    "shape_type": "triangle_equilateral",
    "parameters": {"sides": [3, 4, 5]}
  }'
```

## Question Categories

1. **Shape Classification** - Identify and classify geometric shapes
2. **Area & Perimeter Calculations** - Calculate areas and perimeters
3. **Composite Area Calculations** - Complex area problems with multiple shapes
4. **Angle Calculations** - Calculate and classify angles
5. **Unit Conversions** - Convert between metric units
6. **Quadrilateral Sorting & Grouping** - Classify quadrilaterals
7. **Similarity & Congruency** - Compare shapes for similarity/congruency
8. **Equation Solving by Inspection** - Solve geometric equations
9. **Triangle Height Concepts** - Work with triangle heights and bases
10. **Problem Solving** - Complex multi-step problems
11. **Real-world Applications** - South African context problems

## Difficulty Levels

### Easy
- Simple, single-step calculations
- Whole numbers only
- Basic shape recognition
- Direct formula application

### Medium
- Multi-step calculations
- Decimal numbers (1-2 decimal places)
- Real-world contexts
- Formula manipulation

### Hard
- Complex problem solving
- Multiple decimal places
- Advanced reasoning required
- Challenging real-world scenarios

## Metric System Integration

- **Length Units**: mm, cm, m, km
- **Area Units**: mm², cm², m², km²
- **Conversion Focus**: mm ↔ cm, cm ↔ m, mm² ↔ cm², cm² ↔ m²
- **South African Contexts**: Garden plots, construction, school projects

## South African Real-World Contexts

- **Garden & Landscaping**: Garden plots, flower beds, lawn areas
- **Construction & Home**: Room floors, wall areas, roof sections
- **School Projects**: Classroom floors, sports fields, art rooms
- **Home Applications**: Living rooms, bedrooms, kitchens

## Technical Specifications

### Performance Targets
- Question generation: < 2 seconds
- Parameter validation: < 0.5 seconds
- Template selection: < 0.1 seconds
- System availability: > 99.5%

### Data Structures
- `QuizQuestion`: Complete question with metadata
- `QuestionTemplate`: Reusable question patterns
- `ValidationResult`: Validation feedback
- `GeometricConstraints`: Shape-specific rules

## Next Steps (Phase 2)

1. **Enhanced Parameter Generators** - More sophisticated parameter generation
2. **Advanced Question Templates** - 240+ question templates
3. **Composite Area Calculations** - Shaded/unshaded area problems
4. **Quadrilateral Classification** - Advanced sorting and grouping
5. **Similarity & Congruency** - Shape comparison questions
6. **Equation Solving** - Formula reversal problems
7. **Triangle Height Concepts** - Advanced height calculations

## Error Handling

The system includes comprehensive error handling:
- **Constraint Validation**: Mathematical accuracy checks
- **Parameter Validation**: Input validation and correction
- **Fallback Systems**: Multiple generation methods
- **Error Logging**: Detailed error tracking
- **Graceful Degradation**: System continues working even with errors

## Testing

Run the test script to verify all components:

```bash
python test_quiz_system.py
```

This will test:
- Quiz generation for different question types
- Difficulty level progression
- Geometric constraint validation
- Curriculum mapping
- Shape coverage
- Metric system requirements
- South African contexts

## Contributing

When adding new features:
1. Follow the existing code structure
2. Add comprehensive tests
3. Update the curriculum mapping
4. Ensure geometric accuracy
5. Maintain South African context relevance

## Support

For issues or questions about the quiz system:
1. Check the test script output
2. Review the API endpoint responses
3. Check the Flask server logs
4. Verify geometric constraint validation
