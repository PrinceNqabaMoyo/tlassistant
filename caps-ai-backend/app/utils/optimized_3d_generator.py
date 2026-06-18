"""
Optimized 3D Diagram Generator
Performance-optimized version of 3D diagram generation with reduced data transfer
"""

import numpy as np
import plotly.graph_objects as go
import json
from typing import Dict, Any, Tuple
import math

class Optimized3DGenerator:
    """Optimized 3D diagram generator with performance improvements"""
    
    def __init__(self):
        self.cache = {}  # Simple in-memory cache for frequently used diagrams
        self.max_cache_size = 100  # Limit cache size to prevent memory issues
    
    def _get_cache_key(self, shape_type: str, dimensions: Dict[str, float]) -> str:
        """Generate a cache key for the given parameters"""
        # Round dimensions to 2 decimal places to increase cache hits
        rounded_dims = {k: round(v, 2) for k, v in dimensions.items()}
        return f"{shape_type}_{json.dumps(rounded_dims, sort_keys=True)}"
    
    def _clean_cache(self):
        """Remove oldest entries if cache is too large"""
        if len(self.cache) > self.max_cache_size:
            # Remove oldest 20% of entries
            items_to_remove = len(self.cache) // 5
            keys_to_remove = list(self.cache.keys())[:items_to_remove]
            for key in keys_to_remove:
                del self.cache[key]
    
    def generate_optimized_cube(self, side_length: float, center: Tuple[float, float, float] = (0, 0, 0)) -> Dict[str, Any]:
        """Generate an optimized cube diagram with reduced data transfer"""
        cache_key = self._get_cache_key('cube', {'side_length': side_length})
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Pre-calculate vertices (more efficient than array operations)
        half_side = side_length / 2
        cx, cy, cz = center
        
        # Define vertices more efficiently
        vertices = np.array([
            [cx - half_side, cy - half_side, cz - half_side],  # 0
            [cx + half_side, cy - half_side, cz - half_side],  # 1
            [cx + half_side, cy + half_side, cz - half_side],  # 2
            [cx - half_side, cy + half_side, cz - half_side],  # 3
            [cx - half_side, cy - half_side, cz + half_side],  # 4
            [cx + half_side, cy - half_side, cz + half_side],  # 5
            [cx + half_side, cy + half_side, cz + half_side],  # 6
            [cx - half_side, cy + half_side, cz + half_side]   # 7
        ])
        
        # Pre-define faces (static)
        faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], 
                [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]
        
        # Create optimized mesh data
        mesh_data = {
            'x': vertices[:, 0].tolist(),
            'y': vertices[:, 1].tolist(), 
            'z': vertices[:, 2].tolist(),
            'i': [face[0] for face in faces],
            'j': [face[1] for face in faces],
            'k': [face[2] for face in faces],
            'opacity': 0.7,
            'color': 'lightblue',
            'name': 'Cube',
            'type': 'mesh3d'
        }
        
        # Add dimension labels (simplified)
        dimension_data = {
            'x': [vertices[0, 0], vertices[1, 0]],
            'y': [vertices[0, 1], vertices[1, 1]],
            'z': [vertices[0, 2], vertices[1, 2]],
            'mode': 'lines+markers+text',
            'line': {'color': 'red', 'width': 4},
            'text': [f'{side_length}cm', f'{side_length}cm'],
            'textposition': 'top center',
            'name': 'Side Length',
            'showlegend': False,
            'type': 'scatter3d'
        }
        
        # Optimized layout (reduced template data)
        layout = {
            'scene': {
                'camera': {'eye': {'x': 1.5, 'y': 1.5, 'z': 1.5}},
                'xaxis': {'title': 'X (cm)'},
                'yaxis': {'title': 'Y (cm)'},
                'zaxis': {'title': 'Z (cm)'},
                'aspectmode': 'cube'
            },
            'title': {
                'text': f'3D Cube (Side: {side_length}cm)',
                'x': 0.5,
                'font': {'size': 14}
            },
            'width': 600,
            'height': 500,
            'margin': {'l': 0, 'r': 0, 't': 40, 'b': 0}  # Reduced margins
        }
        
        result = {
            'data': [mesh_data, dimension_data],
            'layout': layout
        }
        
        # Cache the result
        self.cache[cache_key] = result
        self._clean_cache()
        
        return result
    
    def generate_optimized_rectangular_prism(self, length: float, breadth: float, height: float, 
                                           center: Tuple[float, float, float] = (0, 0, 0)) -> Dict[str, Any]:
        """Generate an optimized rectangular prism diagram"""
        cache_key = self._get_cache_key('rectangular_prism', {
            'length': length, 'breadth': breadth, 'height': height
        })
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Pre-calculate vertices
        half_l, half_b, half_h = length / 2, breadth / 2, height / 2
        cx, cy, cz = center
        
        vertices = np.array([
            [cx - half_l, cy - half_b, cz - half_h],  # 0
            [cx + half_l, cy - half_b, cz - half_h],  # 1
            [cx + half_l, cy + half_b, cz - half_h],  # 2
            [cx - half_l, cy + half_b, cz - half_h],  # 3
            [cx - half_l, cy - half_b, cz + half_h],  # 4
            [cx + half_l, cy - half_b, cz + half_h],  # 5
            [cx + half_l, cy + half_b, cz + half_h],  # 6
            [cx - half_l, cy + half_b, cz + half_h]   # 7
        ])
        
        faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], 
                [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]
        
        mesh_data = {
            'x': vertices[:, 0].tolist(),
            'y': vertices[:, 1].tolist(),
            'z': vertices[:, 2].tolist(),
            'i': [face[0] for face in faces],
            'j': [face[1] for face in faces],
            'k': [face[2] for face in faces],
            'opacity': 0.7,
            'color': 'lightgreen',
            'name': 'Rectangular Prism',
            'type': 'mesh3d'
        }
        
        # Add dimension labels
        dimension_data = {
            'x': [vertices[0, 0], vertices[1, 0]],
            'y': [vertices[0, 1], vertices[1, 1]],
            'z': [vertices[0, 2], vertices[1, 2]],
            'mode': 'lines+markers+text',
            'line': {'color': 'red', 'width': 4},
            'text': [f'{length}cm', f'{length}cm'],
            'textposition': 'top center',
            'name': 'Length',
            'showlegend': False,
            'type': 'scatter3d'
        }
        
        layout = {
            'scene': {
                'camera': {'eye': {'x': 1.5, 'y': 1.5, 'z': 1.5}},
                'xaxis': {'title': 'X (cm)'},
                'yaxis': {'title': 'Y (cm)'},
                'zaxis': {'title': 'Z (cm)'},
                'aspectmode': 'cube'
            },
            'title': {
                'text': f'3D Rectangular Prism ({length}×{breadth}×{height}cm)',
                'x': 0.5,
                'font': {'size': 14}
            },
            'width': 600,
            'height': 500,
            'margin': {'l': 0, 'r': 0, 't': 40, 'b': 0}
        }
        
        result = {
            'data': [mesh_data, dimension_data],
            'layout': layout
        }
        
        self.cache[cache_key] = result
        self._clean_cache()
        
        return result
    
    def generate_optimized_cylinder(self, radius: float, height: float, 
                                  center: Tuple[float, float, float] = (0, 0, 0)) -> Dict[str, Any]:
        """Generate an optimized cylinder diagram"""
        cache_key = self._get_cache_key('cylinder', {'radius': radius, 'height': height})
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Generate cylinder vertices more efficiently
        cx, cy, cz = center
        half_h = height / 2
        
        # Create cylinder using parametric equations (more efficient than meshgrid)
        theta = np.linspace(0, 2 * np.pi, 20)  # Reduced resolution for performance
        z_bottom = np.full_like(theta, cz - half_h)
        z_top = np.full_like(theta, cz + half_h)
        
        x_bottom = cx + radius * np.cos(theta)
        y_bottom = cy + radius * np.sin(theta)
        x_top = cx + radius * np.cos(theta)
        y_top = cy + radius * np.sin(theta)
        
        # Create cylinder mesh data
        cylinder_data = {
            'x': np.concatenate([x_bottom, x_top]).tolist(),
            'y': np.concatenate([y_bottom, y_top]).tolist(),
            'z': np.concatenate([z_bottom, z_top]).tolist(),
            'type': 'scatter3d',
            'mode': 'markers',
            'marker': {'size': 3, 'color': 'lightblue'},
            'name': 'Cylinder',
            'opacity': 0.7
        }
        
        # Add radius dimension
        radius_data = {
            'x': [cx, cx + radius],
            'y': [cy, cy],
            'z': [cz - half_h, cz - half_h],
            'mode': 'lines+markers+text',
            'line': {'color': 'red', 'width': 4},
            'text': [f'{radius}cm', f'{radius}cm'],
            'textposition': 'top center',
            'name': 'Radius',
            'showlegend': False,
            'type': 'scatter3d'
        }
        
        layout = {
            'scene': {
                'camera': {'eye': {'x': 1.5, 'y': 1.5, 'z': 1.5}},
                'xaxis': {'title': 'X (cm)'},
                'yaxis': {'title': 'Y (cm)'},
                'zaxis': {'title': 'Z (cm)'},
                'aspectmode': 'cube'
            },
            'title': {
                'text': f'3D Cylinder (r={radius}cm, h={height}cm)',
                'x': 0.5,
                'font': {'size': 14}
            },
            'width': 600,
            'height': 500,
            'margin': {'l': 0, 'r': 0, 't': 40, 'b': 0}
        }
        
        result = {
            'data': [cylinder_data, radius_data],
            'layout': layout
        }
        
        self.cache[cache_key] = result
        self._clean_cache()
        
        return result
    
    def generate_optimized_sphere(self, radius: float, center: Tuple[float, float, float] = (0, 0, 0)) -> Dict[str, Any]:
        """Generate an optimized sphere diagram"""
        cache_key = self._get_cache_key('sphere', {'radius': radius})
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Generate sphere vertices more efficiently
        cx, cy, cz = center
        
        # Use spherical coordinates with reduced resolution
        phi = np.linspace(0, np.pi, 15)  # Reduced from 20
        theta = np.linspace(0, 2 * np.pi, 15)  # Reduced from 20
        
        phi_grid, theta_grid = np.meshgrid(phi, theta)
        
        x = cx + radius * np.sin(phi_grid) * np.cos(theta_grid)
        y = cy + radius * np.sin(phi_grid) * np.sin(theta_grid)
        z = cz + radius * np.cos(phi_grid)
        
        sphere_data = {
            'x': x.flatten().tolist(),
            'y': y.flatten().tolist(),
            'z': z.flatten().tolist(),
            'type': 'scatter3d',
            'mode': 'markers',
            'marker': {'size': 2, 'color': 'lightcoral'},  # Smaller markers for performance
            'name': 'Sphere',
            'opacity': 0.7
        }
        
        # Add radius dimension
        radius_data = {
            'x': [cx, cx + radius],
            'y': [cy, cy],
            'z': [cz, cz],
            'mode': 'lines+markers+text',
            'line': {'color': 'red', 'width': 4},
            'text': [f'{radius}cm', f'{radius}cm'],
            'textposition': 'top center',
            'name': 'Radius',
            'showlegend': False,
            'type': 'scatter3d'
        }
        
        layout = {
            'scene': {
                'camera': {'eye': {'x': 1.5, 'y': 1.5, 'z': 1.5}},
                'xaxis': {'title': 'X (cm)'},
                'yaxis': {'title': 'Y (cm)'},
                'zaxis': {'title': 'Z (cm)'},
                'aspectmode': 'cube'
            },
            'title': {
                'text': f'3D Sphere (r={radius}cm)',
                'x': 0.5,
                'font': {'size': 14}
            },
            'width': 600,
            'height': 500,
            'margin': {'l': 0, 'r': 0, 't': 40, 'b': 0}
        }
        
        result = {
            'data': [sphere_data, radius_data],
            'layout': layout
        }
        
        self.cache[cache_key] = result
        self._clean_cache()
        
        return result
    
    def clear_cache(self):
        """Clear the diagram cache"""
        self.cache.clear()
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        return {
            'cache_size': len(self.cache),
            'max_cache_size': self.max_cache_size,
            'cache_usage_percent': (len(self.cache) / self.max_cache_size) * 100
        }
