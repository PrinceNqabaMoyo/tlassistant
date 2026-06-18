import { useState, useCallback } from 'react';

/**
 * Custom hook for caching geometry diagrams and calculations
 * Provides in-memory caching with configurable TTL and size limits
 */
const useGeometryCache = (maxSize = 50, ttl = 300000) => { // 5 minutes default TTL
    const [cache, setCache] = useState(new Map());

    // Generate cache key from parameters
    const generateKey = useCallback((type, dimension, parameters) => {
        const paramString = JSON.stringify(parameters);
        return `${type}_${dimension}_${btoa(paramString)}`;
    }, []);

    // Check if item exists and is not expired
    const get = useCallback((key) => {
        const item = cache.get(key);
        if (!item) return null;
        
        const now = Date.now();
        if (now > item.expiresAt) {
            setCache(prev => {
                const newCache = new Map(prev);
                newCache.delete(key);
                return newCache;
            });
            return null;
        }
        
        return item.data;
    }, [cache]);

    // Store item with expiration
    const set = useCallback((key, data) => {
        const now = Date.now();
        const item = {
            data,
            expiresAt: now + ttl,
            createdAt: now
        };

        setCache(prev => {
            const newCache = new Map(prev);
            
            // Remove oldest items if cache is full
            if (newCache.size >= maxSize) {
                const oldestKey = newCache.keys().next().value;
                newCache.delete(oldestKey);
            }
            
            newCache.set(key, item);
            return newCache;
        });
    }, [maxSize, ttl]);

    // Clear expired items
    const cleanup = useCallback(() => {
        const now = Date.now();
        setCache(prev => {
            const newCache = new Map();
            for (const [key, item] of prev) {
                if (now <= item.expiresAt) {
                    newCache.set(key, item);
                }
            }
            return newCache;
        });
    }, []);

    // Clear all cache
    const clear = useCallback(() => {
        setCache(new Map());
    }, []);

    // Get cache statistics
    const getStats = useCallback(() => {
        const now = Date.now();
        let validItems = 0;
        let expiredItems = 0;
        
        for (const item of cache.values()) {
            if (now <= item.expiresAt) {
                validItems++;
            } else {
                expiredItems++;
            }
        }
        
        return {
            totalItems: cache.size,
            validItems,
            expiredItems,
            maxSize,
            ttl
        };
    }, [cache, maxSize, ttl]);

    return {
        get,
        set,
        cleanup,
        clear,
        getStats,
        generateKey
    };
};

export default useGeometryCache;
