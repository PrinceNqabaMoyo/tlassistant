import React from 'react';

const TestThumbnail = ({ width = 80, height = 60 }) => {
    console.log('TestThumbnail rendering with:', { width, height });
    return (
        <div 
            style={{ 
                width: width, 
                height: height, 
                backgroundColor: '#FF0000', // Bright red to be very obvious
                border: '3px solid #000000',
                borderRadius: '4px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'white',
                fontSize: '12px',
                fontWeight: 'bold',
                position: 'relative'
            }}
        >
            <div style={{ position: 'absolute', top: '-20px', left: '0', fontSize: '8px', color: 'black' }}>
                THUMBNAIL
            </div>
            TEST
        </div>
    );
};

export default TestThumbnail;
