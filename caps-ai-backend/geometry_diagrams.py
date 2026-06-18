"""
Geometry Diagram Generation Module
Generates precise 2D and 3D geometric diagrams using matplotlib and plotly
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arc
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import io
import base64
from typing import Dict, List, Tuple, Optional, Any
import math
import json

class GeometryDiagramGenerator:
    """Generates precise geometric diagrams for the Geometry Studio"""
    
    def __init__(self):
        # Set matplotlib style for professional diagrams
        plt.style.use('default')
        plt.rcParams['figure.facecolor'] = 'white'
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.linewidth'] = 1.5
        # Use a more reliable font that's available on most systems
        plt.rcParams['font.family'] = 'DejaVu Sans'
        
    def generate_2d_diagram(self, diagram_type: str, parameters: Dict[str, Any]) -> str:
        """
        Generate a 2D geometric diagram and return as base64 encoded image
        
        Args:
            diagram_type: Type of diagram (point, line, ray, segment, angle, circle, etc.)
            parameters: Dictionary containing diagram parameters
            
        Returns:
            Base64 encoded PNG image string
        """
        try:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            
            # Generate diagram based on type
            if diagram_type == 'point':
                self._draw_point(ax, parameters)
            elif diagram_type == 'line':
                self._draw_line(ax, parameters)
            elif diagram_type == 'ray':
                self._draw_ray(ax, parameters)
            elif diagram_type == 'segment':
                self._draw_segment(ax, parameters)
            elif diagram_type == 'parallel_lines':
                self._draw_parallel_lines(ax, parameters)
            elif diagram_type == 'perpendicular_lines':
                self._draw_perpendicular_lines(ax, parameters)
            elif diagram_type == 'angle':
                self._draw_angle(ax, parameters)
            elif diagram_type == 'circle':
                self._draw_circle(ax, parameters)
            elif diagram_type == 'triangle':
                self._draw_triangle(ax, parameters)
            elif diagram_type == 'quadrilateral':
                self._draw_quadrilateral(ax, parameters)
            else:
                raise ValueError(f"Unsupported diagram type: {diagram_type}")
            
            # Convert to base64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
            plt.close(fig)
            
            return image_base64
            
        except Exception as e:
            plt.close('all')
            raise Exception(f"Error generating 2D diagram: {str(e)}")
    
    def generate_3d_diagram(self, diagram_type: str, parameters: Dict[str, Any]) -> str:
        """
        Generate a 3D geometric diagram and return as JSON for plotly
        
        Args:
            diagram_type: Type of 3D diagram (cube, sphere, cylinder, etc.)
            parameters: Dictionary containing diagram parameters
            
        Returns:
            JSON string of plotly figure
        """
        try:
            if diagram_type == 'cube':
                fig = self._create_cube(parameters)
            elif diagram_type == 'sphere':
                fig = self._create_sphere(parameters)
            elif diagram_type == 'cylinder':
                fig = self._create_cylinder(parameters)
            elif diagram_type == 'pyramid':
                fig = self._create_pyramid(parameters)
            else:
                raise ValueError(f"Unsupported 3D diagram type: {diagram_type}")
            
            return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            
        except Exception as e:
            raise Exception(f"Error generating 3D diagram: {str(e)}")
    
    # 2D Drawing Methods
    def _draw_point(self, ax, params):
        """Draw a point with label"""
        x, y = params.get('x', 0), params.get('y', 0)
        label = params.get('label', 'P')
        color = params.get('color', 'red')
        
        ax.plot(x, y, 'o', color=color, markersize=8, markeredgecolor='black', markeredgewidth=1)
        ax.annotate(label, (x, y), xytext=(5, 5), textcoords='offset points', 
                   fontsize=12, fontweight='bold')
    
    def _draw_line(self, ax, params):
        """Draw a line with arrows on both ends"""
        x1, y1 = params.get('start', [0, 0])
        x2, y2 = params.get('end', [5, 0])
        label = params.get('label', 'AB')
        color = params.get('color', 'blue')
        
        # Draw line with arrows
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='<->', color=color, lw=2))
        
        # Add labels
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.annotate(label, (mid_x, mid_y), xytext=(0, 10), 
                   textcoords='offset points', ha='center', fontsize=12, fontweight='bold')
    
    def _draw_ray(self, ax, params):
        """Draw a ray with starting point and arrow"""
        x1, y1 = params.get('start', [0, 0])
        x2, y2 = params.get('end', [5, 0])
        label = params.get('label', 'AB')
        color = params.get('color', 'green')
        
        # Draw starting point
        ax.plot(x1, y1, 'o', color=color, markersize=6, markeredgecolor='black', markeredgewidth=1)
        
        # Draw ray with arrow
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=color, lw=2))
        
        # Add labels
        ax.annotate(label.split()[0] if ' ' in label else label[0], (x1, y1), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        ax.annotate(label.split()[1] if ' ' in label else label[1], (x2, y2), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    
    def _draw_segment(self, ax, params):
        """Draw a line segment with endpoints"""
        x1, y1 = params.get('start', [0, 0])
        x2, y2 = params.get('end', [5, 0])
        label = params.get('label', 'AB')
        color = params.get('color', 'purple')
        
        # Draw endpoints
        ax.plot(x1, y1, 'o', color=color, markersize=6, markeredgecolor='black', markeredgewidth=1)
        ax.plot(x2, y2, 'o', color=color, markersize=6, markeredgecolor='black', markeredgewidth=1)
        
        # Draw segment
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2)
        
        # Add labels
        ax.annotate(label.split()[0] if ' ' in label else label[0], (x1, y1), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        ax.annotate(label.split()[1] if ' ' in label else label[1], (x2, y2), 
                   xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    
    def _draw_parallel_lines(self, ax, params):
        """Draw two parallel lines"""
        line1 = params.get('line1', {'start': [0, 0], 'end': [5, 0]})
        line2 = params.get('line2', {'start': [0, 2], 'end': [5, 2]})
        color = params.get('color', 'orange')
        
        # Draw first line
        ax.plot([line1['start'][0], line1['end'][0]], 
                [line1['start'][1], line1['end'][1]], color=color, linewidth=2)
        
        # Draw second line
        ax.plot([line2['start'][0], line2['end'][0]], 
                [line2['start'][1], line2['end'][1]], color=color, linewidth=2)
        
        # Add parallel symbol
        mid1_x, mid1_y = (line1['start'][0] + line1['end'][0]) / 2, (line1['start'][1] + line1['end'][1]) / 2
        mid2_x, mid2_y = (line2['start'][0] + line2['end'][0]) / 2, (line2['start'][1] + line2['end'][1]) / 2
        
        ax.annotate('∥', (mid1_x, mid1_y), xytext=(0, 10), textcoords='offset points', 
                   ha='center', fontsize=14, fontweight='bold')
        ax.annotate('∥', (mid2_x, mid2_y), xytext=(0, -15), textcoords='offset points', 
                   ha='center', fontsize=14, fontweight='bold')
    
    def _draw_perpendicular_lines(self, ax, params):
        """Draw two perpendicular lines"""
        line1 = params.get('line1', {'start': [0, 0], 'end': [5, 0]})
        line2 = params.get('line2', {'start': [2.5, 0], 'end': [2.5, 3]})
        color = params.get('color', 'red')
        
        # Draw lines
        ax.plot([line1['start'][0], line1['end'][0]], 
                [line1['start'][1], line1['end'][1]], color=color, linewidth=2)
        ax.plot([line2['start'][0], line2['end'][0]], 
                [line2['start'][1], line2['end'][1]], color=color, linewidth=2)
        
        # Draw right angle symbol
        intersection = params.get('intersection', [2.5, 0])
        size = 0.3
        square = patches.Rectangle((intersection[0] - size/2, intersection[1] - size/2), 
                                 size, size, fill=False, edgecolor=color, linewidth=1.5)
        ax.add_patch(square)
    
    def _draw_angle(self, ax, params):
        """Draw an angle with proper arc"""
        vertex = params.get('vertex', [0, 0])
        arm1 = params.get('arm1', [2, 0])
        arm2 = params.get('arm2', [1, 1.5])
        angle_type = params.get('type', 'acute')  # acute, right, obtuse, straight, reflex
        color = params.get('color', 'blue')
        
        # Draw arms
        ax.plot([vertex[0], arm1[0]], [vertex[1], arm1[1]], color=color, linewidth=2)
        ax.plot([vertex[0], arm2[0]], [vertex[1], arm2[1]], color=color, linewidth=2)
        
        # Draw vertex
        ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Draw angle arc
        self._draw_angle_arc(ax, vertex, arm1, arm2, angle_type, color)
        
        # Add labels
        ax.annotate('B', vertex, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10, fontweight='bold')
        ax.annotate('A', arm1, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10, fontweight='bold')
        ax.annotate('C', arm2, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10, fontweight='bold')
    
    def _draw_angle_arc(self, ax, vertex, arm1, arm2, angle_type, color):
        """Draw the arc for an angle"""
        # Calculate angle between arms
        v1 = np.array(arm1) - np.array(vertex)
        v2 = np.array(arm2) - np.array(vertex)
        
        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])
        
        # Determine arc parameters based on angle type
        radius = 0.5
        
        if angle_type == 'right':
            # Draw square for right angle
            square = patches.Rectangle((vertex[0] - radius/2, vertex[1] - radius/2), 
                                     radius, radius, fill=False, edgecolor=color, linewidth=1.5)
            ax.add_patch(square)
        elif angle_type == 'straight':
            # Draw a straight line for 180° angle
            ax.plot([vertex[0] - radius, vertex[0] + radius], [vertex[1], vertex[1]], 
                   color=color, linewidth=1.5)
        elif angle_type == 'revolution':
            # Draw a full circle for 360° angle
            circle = Circle(vertex, radius, fill=False, edgecolor=color, linewidth=1.5)
            ax.add_patch(circle)
        elif angle_type == 'reflex':
            # Draw a large arc for reflex angle (180° < θ < 360°)
            # Calculate the smaller angle and draw the larger arc
            angle_diff = abs(angle2 - angle1)
            if angle_diff > np.pi:
                angle_diff = 2 * np.pi - angle_diff
            if angle_diff < np.pi:
                # Draw the larger arc
                arc = Arc(vertex, 2*radius, 2*radius, angle=0, 
                         theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                         color=color, linewidth=1.5)
                ax.add_patch(arc)
            else:
                # Draw arc in the opposite direction
                arc = Arc(vertex, 2*radius, 2*radius, angle=0, 
                         theta1=np.degrees(angle2), theta2=np.degrees(angle1),
                         color=color, linewidth=1.5)
                ax.add_patch(arc)
        else:
            # Draw normal arc for acute, obtuse angles
            arc = Arc(vertex, 2*radius, 2*radius, angle=0, 
                     theta1=np.degrees(angle1), theta2=np.degrees(angle2),
                     color=color, linewidth=1.5)
            ax.add_patch(arc)
    
    def _draw_circle(self, ax, params):
        """Draw a circle with center and radius"""
        center = params.get('center', [0, 0])
        radius = params.get('radius', 2)
        color = params.get('color', 'blue')
        
        # Draw circle
        circle = Circle(center, radius, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        
        # Draw center
        ax.plot(center[0], center[1], 'o', color=color, markersize=6, 
               markeredgecolor='black', markeredgewidth=1)
        
        # Add labels
        ax.annotate('O', center, xytext=(5, 5), textcoords='offset points', 
                   fontsize=10, fontweight='bold')
    
    def _draw_triangle(self, ax, params):
        """Draw a triangle"""
        vertices = params.get('vertices', [[0, 0], [3, 0], [1.5, 2.5]])
        color = params.get('color', 'green')
        
        # Draw triangle
        triangle = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(triangle)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10, fontweight='bold')
    
    def _draw_quadrilateral(self, ax, params):
        """Draw a quadrilateral"""
        vertices = params.get('vertices', [[0, 0], [3, 0], [3, 2], [0, 2]])
        color = params.get('color', 'purple')
        
        # Draw quadrilateral
        quad = patches.Polygon(vertices, fill=False, edgecolor=color, linewidth=2)
        ax.add_patch(quad)
        
        # Draw vertices
        for i, vertex in enumerate(vertices):
            ax.plot(vertex[0], vertex[1], 'o', color=color, markersize=6, 
                   markeredgecolor='black', markeredgewidth=1)
            ax.annotate(chr(65 + i), vertex, xytext=(5, 5), textcoords='offset points', 
                       fontsize=10, fontweight='bold')
    
    # 3D Drawing Methods
    def _create_cube(self, params):
        """Create a 3D cube using plotly"""
        size = params.get('size', 2)
        center = params.get('center', [0, 0, 0])
        
        # Define cube vertices
        vertices = np.array([
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # bottom face
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # top face
        ]) * size / 2 + np.array(center)
        
        # Define faces
        faces = [
            [0, 1, 2, 3],  # bottom
            [4, 5, 6, 7],  # top
            [0, 1, 5, 4],  # front
            [2, 3, 7, 6],  # back
            [0, 3, 7, 4],  # left
            [1, 2, 6, 5]   # right
        ]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=[face[0] for face in faces],
                j=[face[1] for face in faces],
                k=[face[2] for face in faces],
                opacity=0.7,
                color='lightblue'
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Cube'
        )
        
        return fig
    
    def _create_sphere(self, params):
        """Create a 3D sphere using plotly"""
        radius = params.get('radius', 1)
        center = params.get('center', [0, 0, 0])
        
        # Generate sphere coordinates
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
        y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
        
        fig = go.Figure(data=[
            go.Surface(x=x, y=y, z=z, opacity=0.7, colorscale='Blues')
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Sphere'
        )
        
        return fig
    
    def _create_cylinder(self, params):
        """Create a 3D cylinder using plotly"""
        radius = params.get('radius', 1)
        height = params.get('height', 3)
        center = params.get('center', [0, 0, 0])
        
        # Generate cylinder coordinates
        theta = np.linspace(0, 2 * np.pi, 20)
        z = np.linspace(0, height, 20)
        theta_grid, z_grid = np.meshgrid(theta, z)
        
        x = radius * np.cos(theta_grid) + center[0]
        y = radius * np.sin(theta_grid) + center[1]
        z = z_grid + center[2]
        
        fig = go.Figure(data=[
            go.Surface(x=x, y=y, z=z, opacity=0.7, colorscale='Greens')
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Cylinder'
        )
        
        return fig
    
    def _create_pyramid(self, params):
        """Create a 3D pyramid using plotly"""
        base_size = params.get('base_size', 2)
        height = params.get('height', 3)
        center = params.get('center', [0, 0, 0])
        
        # Define pyramid vertices
        base_vertices = np.array([
            [-1, -1, 0], [1, -1, 0], [1, 1, 0], [-1, 1, 0]
        ]) * base_size / 2 + np.array(center[:2] + [0])
        
        apex = np.array([center[0], center[1], height])
        
        vertices = np.vstack([base_vertices, apex])
        
        # Define faces
        faces = [
            [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4],  # sides
            [0, 1, 2, 3]  # base
        ]
        
        fig = go.Figure(data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=[face[0] for face in faces],
                j=[face[1] for face in faces],
                k=[face[2] for face in faces],
                opacity=0.7,
                color='orange'
            )
        ])
        
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='3D Pyramid'
        )
        
        return fig

# Global instance for use in API endpoints
geometry_generator = GeometryDiagramGenerator()



