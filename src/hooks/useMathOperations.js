import { useState, useCallback } from 'react';
import { apiService } from '../services/api';

/**
 * React hook for mathematical operations using backend API
 */
export const useMathOperations = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    /**
     * Calculate mathematical operations
     */
    const calculate = useCallback(async (operation, expression, params = {}) => {
        setLoading(true);
        setError(null);
        
        try {
            const result = await apiService.calculateMath(operation, expression, params);
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    /**
     * Validate mathematical expressions
     */
    const validate = useCallback(async (expression) => {
        setLoading(true);
        setError(null);
        
        try {
            const result = await apiService.validateExpression(expression);
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    /**
     * Solve mathematical equations
     */
    const solve = useCallback(async (equation) => {
        setLoading(true);
        setError(null);
        
        try {
            const result = await apiService.solveEquation(equation);
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    /**
     * Evaluate mathematical expressions with substitutions
     */
    const evaluate = useCallback(async (expression, substitutions = {}) => {
        setLoading(true);
        setError(null);
        
        try {
            const result = await apiService.evaluateExpression(expression, substitutions);
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    return {
        calculate,
        validate,
        solve,
        evaluate,
        loading,
        error
    };
};
