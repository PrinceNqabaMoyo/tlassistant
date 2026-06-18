/**
 * Backend health monitoring utilities
 * Provides functions to check backend status and handle failures gracefully
 */

import { getApiBaseUrl } from './apiBaseUrl';

const BACKEND_URL = getApiBaseUrl();
const HEALTH_CHECK_INTERVAL = 30000; // 30 seconds
const TIMEOUT_DURATION = 5000; // 5 seconds

/**
 * Check if the backend is healthy
 * @returns {Promise<{isHealthy: boolean, responseTime: number, error?: string}>}
 */
export const checkBackendHealth = async () => {
    const startTime = Date.now();
    
    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), TIMEOUT_DURATION);

        const response = await fetch(`${BACKEND_URL}/api/math/geometry/available-diagrams`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            signal: controller.signal
        });

        clearTimeout(timeoutId);
        const responseTime = Date.now() - startTime;

        if (response.ok) {
            return {
                isHealthy: true,
                responseTime,
                status: response.status
            };
        } else {
            return {
                isHealthy: false,
                responseTime,
                error: `HTTP ${response.status}: ${response.statusText}`,
                status: response.status
            };
        }
    } catch (error) {
        const responseTime = Date.now() - startTime;
        
        if (error.name === 'AbortError') {
            return {
                isHealthy: false,
                responseTime,
                error: 'Request timeout'
            };
        }

        return {
            isHealthy: false,
            responseTime,
            error: error.message
        };
    }
};

/**
 * Backend health monitor class
 * Continuously monitors backend health and provides status updates
 */
export class BackendHealthMonitor {
    constructor() {
        this.isHealthy = false;
        this.lastCheck = null;
        this.listeners = new Set();
        this.intervalId = null;
        this.retryCount = 0;
        this.maxRetries = 3;
    }

    /**
     * Start monitoring backend health
     */
    start() {
        if (this.intervalId) return;

        // Initial check
        this.checkHealth();
        
        // Set up interval
        this.intervalId = setInterval(() => {
            this.checkHealth();
        }, HEALTH_CHECK_INTERVAL);
    }

    /**
     * Stop monitoring
     */
    stop() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    /**
     * Add health status listener
     * @param {Function} listener - Function to call when health status changes
     */
    addListener(listener) {
        this.listeners.add(listener);
    }

    /**
     * Remove health status listener
     * @param {Function} listener - Function to remove
     */
    removeListener(listener) {
        this.listeners.delete(listener);
    }

    /**
     * Notify all listeners of health status change
     */
    notifyListeners() {
        this.listeners.forEach(listener => {
            try {
                listener({
                    isHealthy: this.isHealthy,
                    lastCheck: this.lastCheck,
                    retryCount: this.retryCount
                });
            } catch (error) {
                console.error('Error in health status listener:', error);
            }
        });
    }

    /**
     * Check backend health and update status
     */
    async checkHealth() {
        const healthStatus = await checkBackendHealth();
        const wasHealthy = this.isHealthy;
        
        this.isHealthy = healthStatus.isHealthy;
        this.lastCheck = new Date();

        if (this.isHealthy) {
            this.retryCount = 0;
        } else {
            this.retryCount++;
        }

        // Notify listeners if status changed
        if (wasHealthy !== this.isHealthy) {
            this.notifyListeners();
        }

        return healthStatus;
    }

    /**
     * Get current health status
     */
    getStatus() {
        return {
            isHealthy: this.isHealthy,
            lastCheck: this.lastCheck,
            retryCount: this.retryCount
        };
    }
}

/**
 * Global health monitor instance
 */
export const globalHealthMonitor = new BackendHealthMonitor();

/**
 * React hook for backend health status
 * Note: This should be imported in a React component file
 * @returns {Object} Health status and monitoring functions
 */
export const useBackendHealth = () => {
    // This will be implemented in a separate React hook file
    // to avoid circular dependencies
    throw new Error('useBackendHealth should be imported from hooks/useBackendHealth');
};
