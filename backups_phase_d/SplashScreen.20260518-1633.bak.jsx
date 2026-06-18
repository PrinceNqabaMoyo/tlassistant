import React, { useState, useEffect } from 'react';
import CapRainAnimation from './CapRainAnimation';

// Netflix-style Splash Screen Component
const SplashScreen = ({ onComplete }) => {
  const [isVisible, setIsVisible] = useState(true);
  
  useEffect(() => {
    const hideTimer = setTimeout(() => {
      setIsVisible(false);
    }, 2450);

    const completeTimer = setTimeout(() => {
      onComplete();
    }, 2925);

    return () => {
      clearTimeout(hideTimer);
      clearTimeout(completeTimer);
    };
  }, [onComplete]);

  return (
    <div className={`fixed inset-0 flex items-center justify-center bg-[radial-gradient(circle_at_top,_#2B7BD8_0%,_#13519C_42%,_#0B2D57_100%)] transition-opacity duration-500 ${isVisible ? 'opacity-100' : 'opacity-0'}`}>
      <div className="relative text-center px-6">
        <div className="mx-auto h-48 w-48 sm:h-56 sm:w-56">
          <CapRainAnimation className="h-full w-full" />
        </div>
        <div className="mt-8 space-y-3">
          <h1 className="text-5xl font-bold tracking-tight text-white sm:text-6xl" style={{ fontFamily: 'Afacad, sans-serif' }}>
            fundile
          </h1>
          <p className="text-sm font-medium uppercase tracking-[0.35em] text-white/70 sm:text-base">
            CAPS learning assistant
          </p>
        </div>
      </div>
    </div>
  );
};

export default SplashScreen;
