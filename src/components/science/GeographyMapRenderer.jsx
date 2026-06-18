import React, { useEffect, useRef } from 'react';

const GeographyMapRenderer = ({ lat, lng, zoom, markers = [] }) => {
    const mapRef = useRef(null);
    const mapInstance = useRef(null);

    useEffect(() => {
        if (!mapRef.current || !window.L) return;

        if (!mapInstance.current) {
            mapInstance.current = window.L.map(mapRef.current).setView([lat, lng], zoom);
            window.L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap contributors'
            }).addTo(mapInstance.current);
        } else {
            mapInstance.current.setView([lat, lng], zoom);
        }

        // Clear old markers (simplistic approach for now)
        mapInstance.current.eachLayer((layer) => {
            if (layer instanceof window.L.Marker) {
                mapInstance.current.removeLayer(layer);
            }
        });

        markers.forEach(m => {
            window.L.marker([m.lat, m.lng]).addTo(mapInstance.current)
                .bindPopup(m.popupText);
        });

        return () => {
            if (mapInstance.current) {
                mapInstance.current.remove();
                mapInstance.current = null;
            }
        };
    }, [lat, lng, zoom, markers]);

    return (
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <h3 className="text-sm font-semibold text-gray-700 mb-2">Interactive Map</h3>
            <div ref={mapRef} style={{ height: '400px', width: '100%', borderRadius: '8px' }}></div>
        </div>
    );
};

export default GeographyMapRenderer;
