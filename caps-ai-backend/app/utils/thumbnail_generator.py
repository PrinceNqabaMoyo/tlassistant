import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle
import numpy as np
from io import BytesIO
import math
import matplotlib.font_manager as fm
try:
    from matplotlib_venn import venn2
except ImportError:
    # Fallback if matplotlib-venn is not available
    venn2 = None

class ThumbnailGenerator:
    def __init__(self):
        plt.style.use('default')
        
        # Set up font configuration
        self._setup_fonts()
        
    def _setup_fonts(self):
        """Configure fonts for the application"""
        # Use Windows-friendly fonts with fallbacks
        font_families = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'sans-serif']
        
        # Configure matplotlib to use our preferred fonts
        plt.rcParams['font.family'] = font_families
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.titlesize'] = 12
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['ytick.labelsize'] = 8
        plt.rcParams['legend.fontsize'] = 8
        self.supported_types = {
            'linear_function': self._generate_linear_function,
            'quadratic_function': self._generate_quadratic_function,
            'cubic_function': self._generate_cubic_function,
            'exponential_function': self._generate_exponential_function,
            'logarithmic_function': self._generate_logarithmic_function,
            'box_whisker_plot': self._generate_box_whisker_plot,
            'coordinate_plane': self._generate_coordinate_plane,
            'histogram': self._generate_histogram,
            'scatter_plot': self._generate_scatter_plot,
            'venn_diagram': self._generate_venn_diagram,
            'tree_diagram': self._generate_tree_diagram,
            'bar_chart': self._generate_bar_chart,
            'line_graph': self._generate_line_graph,
            'pie_chart': self._generate_pie_chart
        }
    
    def generate(self, component_type: str, params: dict) -> bytes:
        """Generate thumbnail for specified component type"""
        if component_type not in self.supported_types:
            raise ValueError(f"Unsupported component type: {component_type}")
        
        try:
            return self.supported_types[component_type](params)
        except Exception as e:
            # Fallback to a simple error thumbnail
            return self._generate_error_thumbnail(str(e))
    
    def _generate_linear_function(self, params: dict) -> bytes:
        """Generate linear function thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        m = params.get('m', 2)
        c = params.get('c', 3)
        x_range = params.get('x_range', [-10, 10])
        
        # Generate data
        x = np.linspace(x_range[0], x_range[1], 100)
        y = m * x + c
        
        # Plot
        ax.plot(x, y, color='#3B82F6', linewidth=2)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(x_range)
        ax.set_ylim([-20, 20])
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_quadratic_function(self, params: dict) -> bytes:
        """Generate quadratic function thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        a = params.get('a', 1)
        b = params.get('b', 0)
        c = params.get('c', 0)
        x_range = params.get('x_range', [-10, 10])
        
        # Generate data
        x = np.linspace(x_range[0], x_range[1], 100)
        y = a * x**2 + b * x + c
        
        # Plot
        ax.plot(x, y, color='#3B82F6', linewidth=2)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(x_range)
        ax.set_ylim([-10, 10])
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_cubic_function(self, params: dict) -> bytes:
        """Generate cubic function thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        a = params.get('a', 1)
        b = params.get('b', 0)
        c = params.get('c', -4)
        d = params.get('d', 0)
        x_range = params.get('x_range', [-10, 10])
        
        # Generate data
        x = np.linspace(x_range[0], x_range[1], 100)
        y = a * x**3 + b * x**2 + c * x + d
        
        # Plot
        ax.plot(x, y, color='#3B82F6', linewidth=2)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(x_range)
        ax.set_ylim([-20, 20])
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_exponential_function(self, params: dict) -> bytes:
        """Generate exponential function thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        a = params.get('a', 1)
        b = params.get('b', 2)
        c = params.get('c', 0)
        d = params.get('d', 0)
        x_range = params.get('x_range', [-5, 5])
        
        # Generate data
        x = np.linspace(x_range[0], x_range[1], 100)
        y = a * b**x + c + d
        
        # Plot
        ax.plot(x, y, color='#3B82F6', linewidth=2)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(x_range)
        ax.set_ylim([0, 10])
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_logarithmic_function(self, params: dict) -> bytes:
        """Generate logarithmic function thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        a = params.get('a', 1)
        b = params.get('b', 1)
        c = params.get('c', 0)
        d = params.get('d', 0)
        base = params.get('base', 'e')
        x_range = params.get('x_range', [0.1, 10])
        
        # Generate data
        x = np.linspace(x_range[0], x_range[1], 100)
        if base == 'e':
            y = a * np.log(x) + c + d
        else:
            y = a * np.log(x) / np.log(float(base)) + c + d
        
        # Plot
        ax.plot(x, y, color='#3B82F6', linewidth=2)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(x_range)
        ax.set_ylim([-5, 5])
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_box_whisker_plot(self, params: dict) -> bytes:
        """Generate box and whisker plot thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters - two groups
        data = params.get('data', [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        ])
        labels = params.get('labels', ['Group A', 'Group B'])
        
        # Create box plot
        bp = ax.boxplot(data, labels=labels, patch_artist=True)
        
        # Color the boxes
        colors = ['#3B82F6', '#10B981']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_coordinate_plane(self, params: dict) -> bytes:
        """Generate coordinate plane thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Set up coordinate plane
        x_range = params.get('x_range', [-10, 10])
        y_range = params.get('y_range', [-10, 10])
        
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        ax.grid(True, alpha=0.3)
        
        # Draw axes
        ax.axhline(y=0, color='black', linewidth=1)
        ax.axvline(x=0, color='black', linewidth=1)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_histogram(self, params: dict) -> bytes:
        """Generate histogram thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters - use fixed seed for reproducible results
        if 'data' not in params:
            np.random.seed(42)  # Fixed seed for consistent thumbnails
            data = np.random.normal(0, 1, 100)
        else:
            data = params.get('data')
        bins = params.get('bins', 10)
        color = params.get('color', '#3B82F6')
        
        # Plot histogram
        ax.hist(data, bins=bins, color=color, alpha=0.7)
        ax.grid(True, alpha=0.3)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_scatter_plot(self, params: dict) -> bytes:
        """Generate scatter plot thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters - use fixed seed for reproducible results
        if 'x_data' not in params or 'y_data' not in params:
            np.random.seed(42)  # Fixed seed for consistent thumbnails
            x_data = np.random.normal(0, 1, 100)
            y_data = x_data + np.random.normal(0, 0.3, 100)  # Correlated data
        else:
            x_data = params.get('x_data')
            y_data = params.get('y_data')
        color = params.get('color', '#3B82F6')
        marker = params.get('marker', 'o')
        s = params.get('s', 50)
        
        # Plot scatter plot
        ax.scatter(x_data, y_data, color=color, marker=marker, s=s, alpha=0.7)
        ax.grid(True, alpha=0.3)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_venn_diagram(self, params: dict) -> bytes:
        """Generate venn diagram thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        sets = params.get('sets', ['A', 'B'])
        sizes = params.get('sizes', [10, 15])
        colors = params.get('colors', ['#3B82F6', '#10B981'])
        
        if venn2 is not None:
            # Use matplotlib-venn if available
            venn2(subsets=(sizes[0], sizes[1]), set_labels=sets, ax=ax, alpha=0.7)
        else:
            # Fallback: draw simple overlapping circles
            
            # Calculate positions for overlapping circles
            center1 = (0.3, 0.5)
            center2 = (0.7, 0.5)
            radius = 0.3
            
            # Draw circles
            circle1 = Circle(center1, radius, color=colors[0], alpha=0.7)
            circle2 = Circle(center2, radius, color=colors[1], alpha=0.7)
            
            ax.add_patch(circle1)
            ax.add_patch(circle2)
            
            # Add labels
            ax.text(center1[0], center1[1], sets[0], ha='center', va='center', fontsize=8, fontweight='bold')
            ax.text(center2[0], center2[1], sets[1], ha='center', va='center', fontsize=8, fontweight='bold')
            
            # Set limits
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_tree_diagram(self, params: dict) -> bytes:
        """Generate tree diagram thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        labels = params.get('labels', ['Root', 'Child 1', 'Child 2'])
        colors = params.get('colors', ['#3B82F6', '#10B981', '#F59E0B'])
        
        # Draw simple tree structure
        # Root node
        ax.scatter(0.5, 0.8, s=200, color=colors[0], alpha=0.7, zorder=3)
        ax.text(0.5, 0.8, labels[0], ha='center', va='center', fontsize=8, fontweight='bold')
        
        # Child nodes
        ax.scatter(0.3, 0.4, s=150, color=colors[1], alpha=0.7, zorder=3)
        ax.text(0.3, 0.4, labels[1], ha='center', va='center', fontsize=7, fontweight='bold')
        
        ax.scatter(0.7, 0.4, s=150, color=colors[2], alpha=0.7, zorder=3)
        ax.text(0.7, 0.4, labels[2], ha='center', va='center', fontsize=7, fontweight='bold')
        
        # Draw connections
        ax.plot([0.5, 0.3], [0.75, 0.45], 'k-', linewidth=1, alpha=0.5)
        ax.plot([0.5, 0.7], [0.75, 0.45], 'k-', linewidth=1, alpha=0.5)
        
        # Set limits
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_bar_chart(self, params: dict) -> bytes:
        """Generate bar chart thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        x_data = params.get('x_data', ['A', 'B', 'C'])
        y_data = params.get('y_data', [10, 20, 15])
        color = params.get('color', '#3B82F6')
        width = params.get('width', 0.6)
        
        # Plot bar chart
        ax.bar(x_data, y_data, color=color, width=width, alpha=0.7)
        ax.grid(True, alpha=0.3)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_line_graph(self, params: dict) -> bytes:
        """Generate line graph thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters - use fixed seed for reproducible results
        if 'x_data' not in params or 'y_data' not in params:
            np.random.seed(42)  # Fixed seed for consistent thumbnails
            x_data = np.linspace(0, 10, 100)
            y_data = np.sin(x_data) + np.random.normal(0, 0.3, 100)
        else:
            x_data = params.get('x_data')
            y_data = params.get('y_data')
        color = params.get('color', '#3B82F6')
        linewidth = params.get('linewidth', 2)
        
        # Plot line graph
        ax.plot(x_data, y_data, color=color, linewidth=linewidth, alpha=0.7)
        ax.grid(True, alpha=0.3)
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_pie_chart(self, params: dict) -> bytes:
        """Generate pie chart thumbnail"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Default parameters
        labels = params.get('labels', ['A', 'B', 'C'])
        sizes = params.get('sizes', [10, 20, 30])
        colors = params.get('colors', ['#3B82F6', '#10B981', '#F59E0B'])
        explode = params.get('explode', [0, 0, 0])
        autopct = params.get('autopct', '%1.1f%%')
        startangle = params.get('startangle', 90)
        pctdistance = params.get('pctdistance', 0.8)
        
        # Draw pie chart
        ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct=autopct, startangle=startangle, pctdistance=pctdistance)
        
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis('equal')
        
        # Remove axes labels for thumbnail
        ax.set_xticks([])
        ax.set_yticks([])
        
        return self._fig_to_bytes(fig)
    
    def _generate_error_thumbnail(self, error_msg: str) -> bytes:
        """Generate error thumbnail when generation fails"""
        fig, ax = plt.subplots(figsize=(1.5, 1), dpi=80)
        
        # Create a simple error display
        ax.text(0.5, 0.5, 'Error', ha='center', va='center', fontsize=10, 
                fontweight='bold', color='red')
        ax.text(0.5, 0.3, error_msg[:20] + '...' if len(error_msg) > 20 else error_msg, 
                ha='center', va='center', fontsize=6, color='gray')
        
        # Set limits
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        # Remove axes
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        return self._fig_to_bytes(fig)
    
    def _fig_to_bytes(self, fig) -> bytes:
        """Convert matplotlib figure to bytes"""
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=80)
        buf.seek(0)
        plt.close(fig)
        return buf.getvalue()
