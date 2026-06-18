from flask import request, jsonify
from . import stats_bp
from ...utils.statistical_engine import StatisticalEngine
from ...utils.cache import cache

stats_engine = StatisticalEngine()

@stats_bp.route('/analyze', methods=['POST'])
@cache.memoize(timeout=600)  # Cache for 10 minutes
def analyze_data():
    """Perform statistical analysis on data"""
    data = request.get_json()
    dataset = data.get('data')
    analysis_type = data.get('type', 'descriptive')
    
    try:
        result = stats_engine.analyze(dataset, analysis_type)
        return jsonify({
            'success': True,
            'analysis': result,
            'type': analysis_type
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@stats_bp.route('/generate-chart', methods=['POST'])
def generate_chart():
    """Generate statistical charts"""
    data = request.get_json()
    chart_type = data.get('type')
    chart_data = data.get('data')
    options = data.get('options', {})
    
    try:
        chart_image = stats_engine.generate_chart(chart_type, chart_data, options)
        return jsonify({
            'success': True,
            'chart': chart_image
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@stats_bp.route('/correlation', methods=['POST'])
def calculate_correlation():
    """Calculate correlation between two datasets"""
    data = request.get_json()
    dataset1 = data.get('dataset1')
    dataset2 = data.get('dataset2')
    
    try:
        result = stats_engine.calculate_correlation(dataset1, dataset2)
        return jsonify({
            'success': True,
            'correlation': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@stats_bp.route('/regression', methods=['POST'])
def perform_regression():
    """Perform linear regression analysis"""
    data = request.get_json()
    x_data = data.get('x_data')
    y_data = data.get('y_data')
    
    try:
        result = stats_engine.perform_regression(x_data, y_data)
        return jsonify({
            'success': True,
            'regression': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
