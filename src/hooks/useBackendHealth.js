import { useState, useEffect } from 'react';
import { globalHealthMonitor } from '../utils/backendHealth';

/**
 * React hook for backend health status
 * @returns {Object} Health status and monitoring functions
 */
export const useBackendHealth = () => {
    const [healthStatus, setHealthStatus] = useState({
        isHealthy: false,
        lastCheck: null,
        retryCount: 0
    });

    useEffect(() => {
        const updateStatus = (status) => {
            setHealthStatus(status);
        };

        globalHealthMonitor.addListener(updateStatus);
        
        // Get initial status
        setHealthStatus(globalHealthMonitor.getStatus());

        return () => {
            globalHealthMonitor.removeListener(updateStatus);
        };
    }, []);

    return {
        ...healthStatus,
        checkHealth: () => globalHealthMonitor.checkHealth(),
        startMonitoring: () => globalHealthMonitor.start(),
        stopMonitoring: () => globalHealthMonitor.stop()
    };
};
