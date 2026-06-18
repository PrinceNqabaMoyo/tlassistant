import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from typing import Dict, List, Any

class StatisticalEngine:
    def __init__(self):
        self.supported_analyses = {
            'descriptive': self._descriptive_statistics,
            'correlation': self._correlation_analysis,
            'regression': self._regression_analysis
        }
        
        self.supported_charts = {
            'histogram': self._generate_histogram,
            'boxplot': self._generate_boxplot,
            'scatter': self._generate_scatter,
            'line': self._generate_line_chart,
            'bar': self._generate_bar_chart
        }
    
    def analyze(self, data: List[float], analysis_type: str) -> Dict[str, Any]:
        """Perform statistical analysis"""
        if analysis_type not in self.supported_analyses:
            raise ValueError(f"Unsupported analysis type: {analysis_type}")
        
        return self.supported_analyses[analysis_type](data)
    
    def generate_chart(self, chart_type: str, data: Any, options: Dict[str, Any] = None) -> str:
        """Generate statistical chart"""
        if chart_type not in self.supported_charts:
            raise ValueError(f"Unsupported chart type: {chart_type}")
        
        # Handle both list and dict inputs
        if isinstance(data, list):
            data_dict = {'values': data}
        else:
            data_dict = data
        
        return self.supported_charts[chart_type](data_dict, options or {})
    
    def calculate_correlation(self, dataset1: List[float], dataset2: List[float]) -> Dict[str, Any]:
        """Calculate correlation between two datasets"""
        try:
            if len(dataset1) != len(dataset2):
                raise ValueError("Datasets must have the same length")
            
            correlation, p_value = stats.pearsonr(dataset1, dataset2)
            
            return {
                'correlation_coefficient': float(correlation),
                'p_value': float(p_value),
                'interpretation': self._interpret_correlation(correlation)
            }
        except Exception as e:
            raise ValueError(f"Error calculating correlation: {e}")
    
    def perform_regression(self, x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """Perform linear regression analysis"""
        try:
            if len(x_data) != len(y_data):
                raise ValueError("Datasets must have the same length")
            
            slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
            
            return {
                'slope': float(slope),
                'intercept': float(intercept),
                'r_squared': float(r_value ** 2),
                'p_value': float(p_value),
                'std_error': float(std_err),
                'equation': f"y = {slope:.4f}x + {intercept:.4f}"
            }
        except Exception as e:
            raise ValueError(f"Error performing regression: {e}")
    
    def _descriptive_statistics(self, data: List[float]) -> Dict[str, Any]:
        """Calculate descriptive statistics"""
        data_array = np.array(data)
        
        return {
            'count': len(data_array),
            'mean': float(np.mean(data_array)),
            'median': float(np.median(data_array)),
            'std': float(np.std(data_array)),
            'variance': float(np.var(data_array)),
            'min': float(np.min(data_array)),
            'max': float(np.max(data_array)),
            'q1': float(np.percentile(data_array, 25)),
            'q3': float(np.percentile(data_array, 75)),
            'skewness': float(stats.skew(data_array)),
            'kurtosis': float(stats.kurtosis(data_array))
        }
    
    def _correlation_analysis(self, data: List[float]) -> Dict[str, Any]:
        """Perform correlation analysis"""
        # This would typically work with multiple variables
        # For now, return basic correlation matrix
        return {
            'message': 'Correlation analysis requires multiple variables',
            'data_length': len(data)
        }
    
    def _regression_analysis(self, data: List[float]) -> Dict[str, Any]:
        """Perform regression analysis"""
        # This would typically work with x and y variables
        # For now, return basic info
        return {
            'message': 'Regression analysis requires x and y variables',
            'data_length': len(data)
        }
    
    def _generate_histogram(self, data: Dict[str, Any], options: Dict[str, Any]) -> str:
        """Generate histogram chart"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        values = data.get('values', [])
        bins = options.get('bins', 10)
        
        ax.hist(values, bins=bins, alpha=0.7, color='#3B82F6', edgecolor='black')
        ax.set_xlabel(data.get('xlabel', 'Values'))
        ax.set_ylabel(data.get('ylabel', 'Frequency'))
        ax.set_title(data.get('title', 'Histogram'))
        
        return self._fig_to_base64(fig)
    
    def _generate_boxplot(self, data: Dict[str, Any], options: Dict[str, Any]) -> str:
        """Generate box plot chart"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        values = data.get('values', [])
        labels = data.get('labels', ['Data'])
        
        bp = ax.boxplot(values, labels=labels, patch_artist=True)
        
        # Color the boxes
        colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax.set_title(data.get('title', 'Box Plot'))
        
        return self._fig_to_base64(fig)
    
    def _generate_scatter(self, data: Dict[str, Any], options: Dict[str, Any]) -> str:
        """Generate scatter plot chart"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x_values = data.get('x_values', [])
        y_values = data.get('y_values', [])
        
        ax.scatter(x_values, y_values, alpha=0.7, color='#3B82F6')
        ax.set_xlabel(data.get('xlabel', 'X Values'))
        ax.set_ylabel(data.get('ylabel', 'Y Values'))
        ax.set_title(data.get('title', 'Scatter Plot'))
        
        return self._fig_to_base64(fig)
    
    def _generate_line_chart(self, data: Dict[str, Any], options: Dict[str, Any]) -> str:
        """Generate line chart"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x_values = data.get('x_values', [])
        y_values = data.get('y_values', [])
        
        ax.plot(x_values, y_values, color='#3B82F6', linewidth=2)
        ax.set_xlabel(data.get('xlabel', 'X Values'))
        ax.set_ylabel(data.get('ylabel', 'Y Values'))
        ax.set_title(data.get('title', 'Line Chart'))
        
        return self._fig_to_base64(fig)
    
    def _generate_bar_chart(self, data: Dict[str, Any], options: Dict[str, Any]) -> str:
        """Generate bar chart"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        categories = data.get('categories', [])
        values = data.get('values', [])
        
        bars = ax.bar(categories, values, color='#3B82F6', alpha=0.7)
        ax.set_xlabel(data.get('xlabel', 'Categories'))
        ax.set_ylabel(data.get('ylabel', 'Values'))
        ax.set_title(data.get('title', 'Bar Chart'))
        
        return self._fig_to_base64(fig)
    
    def _fig_to_base64(self, fig) -> str:
        """Convert matplotlib figure to base64 string"""
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
        buf.seek(0)
        plt.close(fig)
        
        return base64.b64encode(buf.getvalue()).decode('utf-8')
    
    def _interpret_correlation(self, correlation: float) -> str:
        """Interpret correlation coefficient"""
        abs_corr = abs(correlation)
        if abs_corr >= 0.8:
            strength = "very strong"
        elif abs_corr >= 0.6:
            strength = "strong"
        elif abs_corr >= 0.4:
            strength = "moderate"
        elif abs_corr >= 0.2:
            strength = "weak"
        else:
            strength = "very weak"
        
        direction = "positive" if correlation > 0 else "negative"
        
        return f"{strength} {direction} correlation"
