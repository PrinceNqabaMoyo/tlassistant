from flask import request, jsonify
from . import thumbnails_bp
from ...utils.thumbnail_generator import ThumbnailGenerator
from ...utils.cache import cache
import base64

thumbnail_gen = ThumbnailGenerator()

@thumbnails_bp.route('/generate', methods=['POST'])
@cache.memoize(timeout=3600)  # Cache for 1 hour
def generate_thumbnail():
    """Generate mathematical component thumbnails"""
    data = request.get_json()
    component_type = data.get('type')
    params = data.get('params', {})
    width = params.get('width', 120)
    height = params.get('height', 80)
    
    try:
        # Generate thumbnail
        image_data = thumbnail_gen.generate(component_type, params)
        
        # Convert to base64 for frontend
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        return jsonify({
            'success': True,
            'thumbnail': f'data:image/png;base64,{image_base64}',
            'type': component_type,
            'dimensions': {'width': width, 'height': height}
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@thumbnails_bp.route('/batch', methods=['POST'])
def generate_batch_thumbnails():
    """Generate multiple thumbnails at once"""
    data = request.get_json()
    components = data.get('components', [])
    
    results = []
    for component in components:
        try:
            result = thumbnail_gen.generate(
                component['type'], 
                component.get('params', {})
            )
            results.append({
                'type': component['type'],
                'success': True,
                'thumbnail': base64.b64encode(result).decode('utf-8')
            })
        except Exception as e:
            results.append({
                'type': component['type'],
                'success': False,
                'error': str(e)
            })
    
    return jsonify({'results': results})
