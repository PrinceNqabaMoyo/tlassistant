import { useState, useCallback, useEffect } from 'react';
import useGeometryCache from './useGeometryCache';
import { buildApiUrl } from '../utils/apiBaseUrl';

/**
 * Custom hook for interacting with the geometry backend
 * Provides functions for generating diagrams and calculating properties
 * Includes caching for improved performance
 */
export const useGeometryBackend = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const cache = useGeometryCache(50, 300000); // 50 items, 5 minutes TTL

    const generateDiagram = useCallback(async (diagramType, dimension = '2d', parameters = {}) => {
        // Check cache first
        const cacheKey = cache.generateKey(diagramType, dimension, parameters);
        const cachedResult = cache.get(cacheKey);
        
        if (cachedResult) {
            return cachedResult;
        }

        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/generate-diagram'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    diagram_type: diagramType,
                    dimension: dimension,
                    parameters: parameters
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                // Cache the result
                cache.set(cacheKey, data);
                return data;
            } else {
                throw new Error(data.error || 'Failed to generate diagram');
            }
        } catch (err) {
            console.error('Error generating diagram:', err);
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, [cache]);

    const calculateProperties = useCallback(async (shape, parameters = {}, includeDiagram = true) => {
        // Check cache first
        const cacheKey = cache.generateKey(`calc_${shape}`, '2d', { ...parameters, includeDiagram });
        const cachedResult = cache.get(cacheKey);
        
        if (cachedResult) {
            return cachedResult;
        }

        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/calculate-properties'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    shape: shape,
                    parameters: parameters,
                    include_diagram: includeDiagram
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                // Cache the result
                cache.set(cacheKey, data);
                return data;
            } else {
                throw new Error(data.error || 'Failed to calculate properties');
            }
        } catch (err) {
            console.error('Error calculating properties:', err);
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, [cache]);

    const getAvailableDiagrams = useCallback(async () => {
        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch(buildApiUrl('/api/math/geometry/available-diagrams'), {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                return data.available_diagrams;
            } else {
                throw new Error(data.error || 'Failed to get available diagrams');
            }
        } catch (err) {
            console.error('Error getting available diagrams:', err);
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    // Cleanup expired cache items periodically
    useEffect(() => {
        const interval = setInterval(() => {
            cache.cleanup();
        }, 60000); // Cleanup every minute

        return () => clearInterval(interval);
    }, [cache]);

    return {
        generateDiagram,
        calculateProperties,
        getAvailableDiagrams,
        loading,
        error,
        setError,
        // Cache management
        clearCache: cache.clear,
        getCacheStats: cache.getStats
    };
};
