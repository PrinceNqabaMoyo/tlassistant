from flask import request, jsonify
from . import curriculum_bp
from ...utils.curriculum_service import CurriculumService
from ...utils.cache import cache
from datetime import datetime

curriculum_service = CurriculumService()

@curriculum_bp.route('/data', methods=['GET'])
@cache.memoize(timeout=600)  # Cache for 10 minutes
def get_curriculum_data():
    """Get curriculum data from ChromaDB"""
    try:
        curriculum_data = curriculum_service.get_curriculum_data()
        return jsonify({
            'success': True,
            'curricula': curriculum_data,
            'lastUpdated': datetime.now().isoformat(),
            'version': '2.1'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@curriculum_bp.route('/topics/<subject>/<grade>', methods=['GET'])
@cache.memoize(timeout=3600)  # Cache for 1 hour
def get_topics_by_subject_grade(subject, grade):
    """Get topics for specific subject and grade"""
    try:
        topics = curriculum_service.get_topics_by_subject_grade(subject, grade)
        return jsonify({
            'success': True,
            'topics': topics,
            'subject': subject,
            'grade': grade
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@curriculum_bp.route('/search', methods=['POST'])
def search_curriculum():
    """Search curriculum content"""
    data = request.get_json()
    query = data.get('query', '')
    filters = data.get('filters', {})
    
    try:
        results = curriculum_service.search_curriculum(query, filters)
        return jsonify({
            'success': True,
            'results': results,
            'query': query
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
