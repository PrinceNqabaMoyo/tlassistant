import React, { useState, useRef, useEffect, useCallback } from 'react';
import { Camera, Upload, X, RotateCcw, Check, AlertCircle } from 'lucide-react';
import studentStore from '../../services/studentStore';

/**
 * ProfilePhotoModal
 * Allows any subscriber (Learner, Teacher, Parent, School Admin) to take or upload a profile picture.
 * - Live Camera Capture with 3-2-1 flash countdown & circular guideline
 * - File Upload / Pick from Device with drag-and-drop support
 * - Circular crop preview & Save to studentStore / localStorage
 */
export default function ProfilePhotoModal({
  isOpen = false,
  onClose = () => {},
  onSavePhoto = null,
}) {
  const [activeTab, setActiveTab] = useState('camera'); // 'camera' | 'upload'
  const [capturedPhoto, setCapturedPhoto] = useState(null);
  const [cameraError, setCameraError] = useState(null);
  const [countdown, setCountdown] = useState(null);
  const [isFlashing, setIsFlashing] = useState(false);
  const [isDragOver, setIsDragOver] = useState(false);

  const videoRef = useRef(null);
  const streamRef = useRef(null);
  const fileInputRef = useRef(null);
  const countdownIntervalRef = useRef(null);

  // Stop camera tracks cleanly
  const stopCamera = useCallback(() => {
    if (countdownIntervalRef.current) {
      clearInterval(countdownIntervalRef.current);
      countdownIntervalRef.current = null;
    }
    setCountdown(null);
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => track.stop());
      streamRef.current = null;
    }
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
  }, []);

  // Start camera stream
  const startCamera = useCallback(async () => {
    setCameraError(null);
    stopCamera();

    try {
      if (!navigator?.mediaDevices?.getUserMedia) {
        throw new Error('Camera is not supported on this browser or device.');
      }

      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          facingMode: 'user',
          width: { ideal: 640 },
          height: { ideal: 640 },
        },
        audio: false,
      });

      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.play().catch((err) => {
          console.warn('Video playback notice:', err);
        });
      }
    } catch (err) {
      console.warn('Camera access unavailable:', err);
      const msg = err.name === 'NotAllowedError' || err.name === 'PermissionDeniedError'
        ? 'Camera permission denied. Please allow camera access in your browser or upload a photo instead.'
        : 'Unable to access camera. You can upload an image from your device.';
      setCameraError(msg);
    }
  }, [stopCamera]);

  // Manage camera lifecycle based on isOpen, tab, and captured status
  useEffect(() => {
    if (isOpen && activeTab === 'camera' && !capturedPhoto) {
      startCamera();
    } else {
      stopCamera();
    }

    return () => {
      stopCamera();
    };
  }, [isOpen, activeTab, capturedPhoto, startCamera, stopCamera]);

  // Reset modal state when closed
  const handleModalClose = useCallback(() => {
    stopCamera();
    setCapturedPhoto(null);
    setCameraError(null);
    setCountdown(null);
    setIsFlashing(false);
    onClose();
  }, [stopCamera, onClose]);

  // Close on Escape key
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') {
        handleModalClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, handleModalClose]);

  // Process image file to base64 square crop
  const processImageFile = useCallback((file) => {
    if (!file || !file.type.startsWith('image/')) {
      setCameraError('Please select a valid image file (JPEG, PNG, WebP).');
      return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = 400;
        canvas.height = 400;
        const ctx = canvas.getContext('2d');

        const minDim = Math.min(img.width, img.height);
        const startX = (img.width - minDim) / 2;
        const startY = (img.height - minDim) / 2;

        ctx.drawImage(img, startX, startY, minDim, minDim, 0, 0, 400, 400);
        const dataUrl = canvas.toDataURL('image/jpeg', 0.88);
        setCapturedPhoto(dataUrl);
        setCameraError(null);
      };
      img.onerror = () => {
        setCameraError('Failed to read image. Please try another file.');
      };
      img.src = e.target.result;
    };
    reader.onerror = () => {
      setCameraError('Failed to read image file.');
    };
    reader.readAsDataURL(file);
  }, []);

  // Trigger camera snap with 3-2-1 countdown & flash effect
  const handleSnapPhoto = () => {
    if (countdown !== null || !videoRef.current) return;

    setCountdown(3);
    let current = 3;

    countdownIntervalRef.current = setInterval(() => {
      current -= 1;
      if (current > 0) {
        setCountdown(current);
      } else {
        clearInterval(countdownIntervalRef.current);
        countdownIntervalRef.current = null;
        setCountdown(null);

        // Visual flash effect
        setIsFlashing(true);
        setTimeout(() => setIsFlashing(false), 220);

        // Draw video frame to 400x400 square canvas
        try {
          const video = videoRef.current;
          if (!video) return;

          const canvas = document.createElement('canvas');
          canvas.width = 400;
          canvas.height = 400;
          const ctx = canvas.getContext('2d');

          const vWidth = video.videoWidth || 640;
          const vHeight = video.videoHeight || 640;
          const minDim = Math.min(vWidth, vHeight);
          const startX = (vWidth - minDim) / 2;
          const startY = (vHeight - minDim) / 2;

          // Mirror horizontally for natural selfie perspective
          ctx.translate(canvas.width, 0);
          ctx.scale(-1, 1);
          ctx.drawImage(video, startX, startY, minDim, minDim, 0, 0, 400, 400);

          const dataUrl = canvas.toDataURL('image/jpeg', 0.88);
          setCapturedPhoto(dataUrl);
          stopCamera();
        } catch (err) {
          console.error('Canvas capture error:', err);
          setCameraError('Failed to capture photo from video feed.');
        }
      }
    }, 1000);
  };

  // Save profile photo across studentStore, localStorage, and callback
  const handleSavePhoto = () => {
    if (!capturedPhoto) return;

    studentStore.updateProfilePhoto(capturedPhoto);

    try {
      localStorage.setItem('fundile_user_photoURL', capturedPhoto);
    } catch (e) {
      console.warn('LocalStorage save error:', e);
    }

    if (typeof onSavePhoto === 'function') {
      onSavePhoto(capturedPhoto);
    }

    handleModalClose();
  };

  // Retake or pick another image
  const handleRetake = () => {
    setCapturedPhoto(null);
    setCameraError(null);
    if (activeTab === 'camera') {
      startCamera();
    }
  };

  // File input change handler
  const handleFileInputChange = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      processImageFile(file);
    }
  };

  // Drag and drop handlers
  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragOver(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragOver(false);
    const file = e.dataTransfer.files?.[0];
    if (file) {
      processImageFile(file);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[120] flex items-center justify-center bg-black/60 backdrop-blur-xs p-4 animate-in fade-in duration-200">
      <div 
        className="w-full max-w-md bg-white rounded-2xl border border-slate-200 shadow-2xl overflow-hidden flex flex-col transition-all"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Modal Header */}
        <div className="px-5 py-4 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-[#13519C]/10 text-[#13519C] flex items-center justify-center font-bold">
              📸
            </div>
            <div>
              <h3 className="font-bold text-base text-slate-900 leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                Update Profile Picture
              </h3>
              <p className="text-[11px] text-slate-500">Take a live photo or upload from your device</p>
            </div>
          </div>
          <button
            type="button"
            onClick={handleModalClose}
            className="p-1.5 rounded-full text-slate-400 hover:text-slate-700 hover:bg-slate-200 transition cursor-pointer"
            title="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Content */}
        <div className="p-5 flex flex-col items-center">
          {/* Tab Switcher (When not in preview) */}
          {!capturedPhoto && (
            <div className="w-full grid grid-cols-2 p-1 bg-slate-100 rounded-xl mb-4 text-xs font-semibold">
              <button
                type="button"
                onClick={() => {
                  setActiveTab('camera');
                  setCameraError(null);
                }}
                className={`py-2 rounded-lg flex items-center justify-center gap-1.5 transition cursor-pointer ${
                  activeTab === 'camera'
                    ? 'bg-white text-[#13519C] shadow-xs font-bold'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                <Camera className="w-4 h-4" />
                <span>Live Camera</span>
              </button>
              <button
                type="button"
                onClick={() => {
                  setActiveTab('upload');
                  setCameraError(null);
                  stopCamera();
                }}
                className={`py-2 rounded-lg flex items-center justify-center gap-1.5 transition cursor-pointer ${
                  activeTab === 'upload'
                    ? 'bg-white text-[#13519C] shadow-xs font-bold'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                <Upload className="w-4 h-4" />
                <span>Upload File</span>
              </button>
            </div>
          )}

          {/* PREVIEW MODE: Captured / Uploaded Photo */}
          {capturedPhoto ? (
            <div className="flex flex-col items-center w-full py-2 animate-in zoom-in-95 duration-200">
              <div className="relative mb-4">
                <div className="w-44 h-44 rounded-full overflow-hidden border-4 border-[#13519C] shadow-lg ring-4 ring-blue-100 flex items-center justify-center bg-slate-100">
                  <img
                    src={capturedPhoto}
                    alt="Profile preview"
                    className="w-full h-full object-cover"
                  />
                </div>
                <div className="absolute bottom-1 right-2 w-8 h-8 rounded-full bg-emerald-500 text-white flex items-center justify-center shadow-md ring-2 ring-white">
                  <Check className="w-4 h-4" />
                </div>
              </div>

              <p className="text-xs text-slate-600 mb-5 text-center font-medium">
                Photo ready! Confirm to save this as your profile picture.
              </p>

              <div className="flex items-center gap-3 w-full">
                <button
                  type="button"
                  onClick={handleRetake}
                  className="flex-1 py-2.5 px-4 rounded-xl border border-slate-300 hover:bg-slate-100 text-slate-700 text-xs font-bold flex items-center justify-center gap-1.5 transition cursor-pointer"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>Retake / Change</span>
                </button>
                <button
                  type="button"
                  onClick={handleSavePhoto}
                  className="flex-1 py-2.5 px-4 rounded-xl bg-[#13519C] hover:bg-[#0e3c73] text-white text-xs font-bold shadow-md shadow-blue-900/20 flex items-center justify-center gap-1.5 transition hover:scale-[1.02] cursor-pointer"
                  style={{ fontFamily: 'Afacad, sans-serif' }}
                >
                  <Check className="w-4 h-4" />
                  <span>Save Profile Photo</span>
                </button>
              </div>
            </div>
          ) : activeTab === 'camera' ? (
            /* CAMERA CAPTURE MODE */
            <div className="flex flex-col items-center w-full">
              {cameraError ? (
                <div className="w-full p-4 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs space-y-3 text-center my-4">
                  <AlertCircle className="w-6 h-6 text-amber-600 mx-auto" />
                  <p>{cameraError}</p>
                  <button
                    type="button"
                    onClick={() => {
                      setActiveTab('upload');
                      setCameraError(null);
                    }}
                    className="inline-flex items-center gap-1.5 px-4 py-2 bg-[#13519C] text-white rounded-xl font-bold text-xs shadow-xs hover:bg-[#0e3c73] transition cursor-pointer"
                  >
                    <Upload className="w-3.5 h-3.5" />
                    <span>Switch to File Upload</span>
                  </button>
                </div>
              ) : (
                <div className="flex flex-col items-center w-full">
                  {/* Circular Viewfinder Container */}
                  <div className="relative w-56 h-56 rounded-full overflow-hidden border-4 border-slate-300 shadow-inner bg-slate-950 flex items-center justify-center mb-4">
                    <video
                      ref={videoRef}
                      autoPlay
                      playsInline
                      muted
                      className="w-full h-full object-cover scale-x-[-1]"
                    />

                    {/* Circular Guideline Overlay */}
                    <div className="absolute inset-0 rounded-full border-2 border-white/60 pointer-events-none" />

                    {/* Countdown Flash Overlay */}
                    {countdown !== null && (
                      <div className="absolute inset-0 bg-black/40 flex items-center justify-center backdrop-blur-2xs">
                        <span className="text-6xl font-black text-white animate-ping">
                          {countdown}
                        </span>
                      </div>
                    )}

                    {/* Flash Animation on Snap */}
                    {isFlashing && (
                      <div className="absolute inset-0 bg-white transition-opacity duration-150" />
                    )}
                  </div>

                  <p className="text-[11px] text-slate-500 mb-4 text-center">
                    Center your face inside the circle and press Snap Photo.
                  </p>

                  <button
                    type="button"
                    onClick={handleSnapPhoto}
                    disabled={countdown !== null}
                    className="w-full py-2.5 px-4 rounded-xl bg-[#13519C] hover:bg-[#0e3c73] text-white text-xs font-bold shadow-md shadow-blue-900/20 flex items-center justify-center gap-2 transition hover:scale-[1.02] cursor-pointer disabled:opacity-50"
                    style={{ fontFamily: 'Afacad, sans-serif' }}
                  >
                    <Camera className="w-4 h-4" />
                    <span>{countdown !== null ? `Snapping in ${countdown}...` : '📸 Snap Photo'}</span>
                  </button>
                </div>
              )}
            </div>
          ) : (
            /* FILE UPLOAD MODE */
            <div className="flex flex-col items-center w-full">
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                capture="user"
                className="hidden"
                onChange={handleFileInputChange}
              />

              <div
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}
                onClick={() => fileInputRef.current?.click()}
                className={`w-full py-8 px-4 rounded-2xl border-2 border-dashed flex flex-col items-center justify-center gap-2 transition cursor-pointer text-center ${
                  isDragOver
                    ? 'border-[#13519C] bg-blue-50/70'
                    : 'border-slate-300 hover:border-slate-400 bg-slate-50/80 hover:bg-slate-50'
                }`}
              >
                <div className="w-12 h-12 rounded-full bg-blue-100 text-[#13519C] flex items-center justify-center mb-1">
                  <Upload className="w-6 h-6" />
                </div>
                <span className="text-xs font-bold text-slate-800">
                  Click to browse or drag and drop
                </span>
                <span className="text-[11px] text-slate-500">
                  Supports JPG, PNG, WebP (Max 5MB)
                </span>
              </div>

              {cameraError && (
                <div className="w-full mt-3 p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-rose-800 text-xs flex items-center gap-2">
                  <AlertCircle className="w-4 h-4 shrink-0 text-rose-600" />
                  <span>{cameraError}</span>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
