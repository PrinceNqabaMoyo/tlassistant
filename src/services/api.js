/**
 * API Service Layer for Backend Communication
 * Handles all HTTP requests to the backend services
 */

import { getApiBaseUrl } from '../utils/apiBaseUrl';

class APIService {
    constructor(baseURL = getApiBaseUrl()) {
        this.baseURL = baseURL;
    }

    /**
     * Generic request method
     */
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        };

        try {
            const response = await fetch(url, config);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }

    // ===== MATH OPERATIONS =====
    
    /**
     * Calculate mathematical operations
     */
    async calculateMath(operation, expression, params = {}) {
        return this.request('/api/math/calculate', {
            method: 'POST',
            body: JSON.stringify({
                operation,
                expression,
                params
            })
        });
    }

    /**
     * Validate mathematical expressions
     */
    async validateExpression(expression) {
        return this.request('/api/math/validate', {
            method: 'POST',
            body: JSON.stringify({ expression })
        });
    }

    /**
     * Solve mathematical equations
     */
    async solveEquation(equation) {
        return this.request('/api/math/solve', {
            method: 'POST',
            body: JSON.stringify({ equation })
        });
    }

    /**
     * Evaluate mathematical expressions with substitutions
     */
    async evaluateExpression(expression, substitutions = {}) {
        return this.request('/api/math/evaluate', {
            method: 'POST',
            body: JSON.stringify({
                expression,
                substitutions
            })
        });
    }

    // ===== THUMBNAIL GENERATION =====
    
    /**
     * Generate single thumbnail
     */
    async generateThumbnail(componentType, params = {}) {
        return this.request('/api/thumbnails/generate', {
            method: 'POST',
            body: JSON.stringify({
                type: componentType,
                params
            })
        });
    }

    /**
     * Generate multiple thumbnails at once
     */
    async generateBatchThumbnails(components) {
        return this.request('/api/thumbnails/batch', {
            method: 'POST',
            body: JSON.stringify({ components })
        });
    }

    // ===== CURRICULUM DATA =====
    
    /**
     * Get curriculum data
     */
    async getCurriculumData() {
        return this.request('/api/curriculum/data', {
            method: 'GET'
        });
    }

    /**
     * Get topics by subject and grade
     */
    async getTopicsBySubjectGrade(subject, grade) {
        return this.request(`/api/curriculum/topics/${subject}/${grade}`, {
            method: 'GET'
        });
    }

    /**
     * Search curriculum content
     */
    async searchCurriculum(query, filters = {}) {
        return this.request('/api/curriculum/search', {
            method: 'POST',
            body: JSON.stringify({
                query,
                filters
            })
        });
    }

    // ===== STATISTICAL ANALYSIS =====
    
    /**
     * Perform statistical analysis
     */
    async analyzeData(data, analysisType = 'descriptive') {
        return this.request('/api/statistics/analyze', {
            method: 'POST',
            body: JSON.stringify({
                data,
                type: analysisType
            })
        });
    }

    /**
     * Generate statistical charts
     */
    async generateChart(chartType, data, options = {}) {
        return this.request('/api/statistics/generate-chart', {
            method: 'POST',
            body: JSON.stringify({
                type: chartType,
                data,
                options
            })
        });
    }

    /**
     * Calculate correlation between datasets
     */
    async calculateCorrelation(dataset1, dataset2) {
        return this.request('/api/statistics/correlation', {
            method: 'POST',
            body: JSON.stringify({
                dataset1,
                dataset2
            })
        });
    }

    /**
     * Perform linear regression
     */
    async performRegression(xData, yData) {
        return this.request('/api/statistics/regression', {
            method: 'POST',
            body: JSON.stringify({
                x_data: xData,
                y_data: yData
            })
        });
    }
}

// Export singleton instance
export const apiService = new APIService();

// Export the class for testing or custom instances
export default APIService;
