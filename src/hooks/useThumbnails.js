import { useState, useCallback } from 'react';
import { apiService } from '../services/api';

/**
 * React hook for thumbnail generation using backend API
 */
export const useThumbnails = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [thumbnails, setThumbnails] = useState({});

    /**
     * Generate single thumbnail
     */
    const generateThumbnail = useCallback(async (componentType, params = {}) => {
        setLoading(true);
        setError(null);
        
        try {
            const result = await apiService.generateThumbnail(componentType, params);
            
            // Cache the thumbnail
            setThumbnails(prev => ({
                ...prev,
                [componentType]: result.thumbnail
            }));
            
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    /**
     * Generate multiple thumbnails at once
     */
    const generateBatchThumbnails = useCallback(async (components) => {
        setLoading(true);
        setError(null);
        
        try {
            const result = await apiService.generateBatchThumbnails(components);
            
            // Cache all thumbnails
            const newThumbnails = {};
            result.results.forEach(item => {
                if (item.success) {
                    newThumbnails[item.type] = item.thumbnail;
                }
            });
            
            setThumbnails(prev => ({
                ...prev,
                ...newThumbnails
            }));
            
            return result;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    /**
     * Get cached thumbnail
     */
    const getThumbnail = useCallback((componentType) => {
        return thumbnails[componentType] || null;
    }, [thumbnails]);

    /**
     * Clear thumbnail cache
     */
    const clearCache = useCallback(() => {
        setThumbnails({});
    }, []);

    return {
        generateThumbnail,
        generateBatchThumbnails,
        getThumbnail,
        clearCache,
        thumbnails,
        loading,
        error
    };
};
