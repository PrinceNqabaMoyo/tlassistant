#!/usr/bin/env python3
"""
3D Net Visualization Generator
Generates 2D nets that fold into 3D shapes for educational purposes
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np
from typing import Dict, List, Tuple, Any
import base64
from io import BytesIO

class NetGenerator:
    """
    Generates 2D nets for 3D shapes that can be folded
    """
    
    def __init__(self):
        self.fig_size = (12, 8)
        self.face_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink', 'lightgray']
        self.edge_color = 'black'
        self.line_width = 2
        
    def generate_cube_net(self, side_length: float) -> str:
        """
        Generate a 2D net for a cube in cross pattern
        
        Pattern:
        [ ][ ][ ]
        [ ][ ][ ]
        [ ][ ][ ]
        
        Returns base64 encoded image
        """
        fig, ax = plt.subplots(1, 1, figsize=self.fig_size)
        ax.set_xlim(-2, 4)
        ax.set_ylim(-2, 4)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Define the 6 faces of the cube net
        faces = [
            # Row 1
            {'pos': (0, 1), 'label': 'Top'},
            {'pos': (1, 1), 'label': 'Front'},
            {'pos': (2, 1), 'label': 'Right'},
            # Row 2
            {'pos': (0, 0), 'label': 'Left'},
            {'pos': (1, 0), 'label': 'Bottom'},
            {'pos': (2, 0), 'label': 'Back'}
        ]
        
        # Draw each face
        for i, face in enumerate(faces):
            x, y = face['pos']
            rect = Rectangle(
                (x, y), side_length, side_length,
                facecolor=self.face_colors[i % len(self.face_colors)],
                edgecolor=self.edge_color,
                linewidth=self.line_width
            )
            ax.add_patch(rect)
            
            # Add face label
            ax.text(x + side_length/2, y + side_length/2, face['label'], 
                   ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Add dimensions
            ax.text(x + side_length/2, y - 0.2, f'{side_length}cm', 
                   ha='center', va='center', fontsize=8)
        
        # Add fold lines (dashed)
        fold_lines = [
            # Vertical fold lines
            ((1, 0), (1, 2)),
            ((2, 0), (2, 2)),
            # Horizontal fold lines
            ((0, 1), (3, 1))
        ]
        
        for start, end in fold_lines:
            ax.plot([start[0], end[0]], [start[1], end[1]], 
                   'k--', linewidth=1, alpha=0.7)
        
        # Add title
        ax.set_title(f'Cube Net (Side Length: {side_length}cm)', fontsize=14, fontweight='bold')
        
        # Add instructions
        ax.text(1.5, -1.5, 'Cut along the outer edges and fold along the dashed lines', 
               ha='center', va='center', fontsize=10, style='italic')
        
        return self._fig_to_base64(fig)
    
    def generate_rectangular_prism_net(self, length: float, breadth: float, height: float) -> str:
        """
        Generate a 2D net for a rectangular prism
        
        Pattern:
        [  ][  ][  ]
        [  ][  ][  ]
        [  ][  ][  ]
        [  ][  ][  ]
        
        Returns base64 encoded image
        """
        fig, ax = plt.subplots(1, 1, figsize=self.fig_size)
        ax.set_xlim(-1, 5)
        ax.set_ylim(-1, 5)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Define the 6 faces of the rectangular prism net
        faces = [
            # Row 1
            {'pos': (0, 2), 'label': 'Top', 'width': length, 'height': breadth},
            {'pos': (1, 2), 'label': 'Front', 'width': length, 'height': height},
            {'pos': (2, 2), 'label': 'Right', 'width': breadth, 'height': height},
            # Row 2
            {'pos': (0, 1), 'label': 'Left', 'width': breadth, 'height': height},
            {'pos': (1, 1), 'label': 'Bottom', 'width': length, 'height': breadth},
            {'pos': (2, 1), 'label': 'Back', 'width': length, 'height': height}
        ]
        
        # Draw each face
        for i, face in enumerate(faces):
            x, y = face['pos']
            rect = Rectangle(
                (x, y), face['width'], face['height'],
                facecolor=self.face_colors[i % len(self.face_colors)],
                edgecolor=self.edge_color,
                linewidth=self.line_width
            )
            ax.add_patch(rect)
            
            # Add face label
            ax.text(x + face['width']/2, y + face['height']/2, face['label'], 
                   ha='center', va='center', fontsize=10, fontweight='bold')
            
            # Add dimensions
            ax.text(x + face['width']/2, y - 0.2, f'{face["width"]}×{face["height"]}cm', 
                   ha='center', va='center', fontsize=8)
        
        # Add fold lines (dashed)
        fold_lines = [
            # Vertical fold lines
            ((1, 1), (1, 3)),
            ((2, 1), (2, 3)),
            # Horizontal fold lines
            ((0, 1.5), (3, 1.5))
        ]
        
        for start, end in fold_lines:
            ax.plot([start[0], end[0]], [start[1], end[1]], 
                   'k--', linewidth=1, alpha=0.7)
        
        # Add title
        ax.set_title(f'Rectangular Prism Net (L:{length}cm, B:{breadth}cm, H:{height}cm)', 
                    fontsize=14, fontweight='bold')
        
        # Add instructions
        ax.text(1.5, 0.5, 'Cut along the outer edges and fold along the dashed lines', 
               ha='center', va='center', fontsize=10, style='italic')
        
        return self._fig_to_base64(fig)
    
    def _fig_to_base64(self, fig) -> str:
        """Convert matplotlib figure to base64 string"""
        buffer = BytesIO()
        fig.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        plt.close(fig)
        return image_base64

# Test the net generator
if __name__ == "__main__":
    generator = NetGenerator()
    
    # Test cube net
    cube_net = generator.generate_cube_net(3.0)
    print("Cube net generated successfully!")
    
    # Test rectangular prism net
    prism_net = generator.generate_rectangular_prism_net(4.0, 3.0, 2.0)
    print("Rectangular prism net generated successfully!")
