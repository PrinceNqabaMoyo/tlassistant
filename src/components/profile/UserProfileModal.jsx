import React, { useState, useEffect, useRef } from 'react';
import { 
  X, 
  Camera, 
  Upload, 
  LogOut, 
  Users, 
  UserPlus, 
  Trash2, 
  Check, 
  Shield, 
  School, 
  GraduationCap, 
  Link2, 
  AlertCircle,
  RotateCcw,
  Sparkles
} from 'lucide-react';
import studentStore from '../../services/studentStore';

/**
 * UserProfileModal
 * Comprehensive user profile dialog for all devices (Web, Desktop PWA, Mobile WebAPK).
 * 
 * Features:
 * - Profile photo snap (live camera 3-2-1 flash) or file upload
 * - Full name, Grade (7–12), Phase (Senior Phase vs FET Phase)
 * - School Name with toggle for Independent Account / Homeschool
 * - Teacher links (Class join code input & connected teachers list)
 * - Parent links (Allowance of up to 2 parental links)
 * - Prominent "Log Out" button (Item 2: Log off on installed apps)
 * - Super Admin controls (Item 15: Clean 5-role switcher, Tier toggle, Mock Tester)
 */
export default function UserProfileModal({
  isOpen = false,
  onClose = () => {},
  currentUser = null,
  onLogout = () => {},
  superAdminMode = 'student',
  setSuperAdminMode = null,
  superAdminTier = 'standard',
  setSuperAdminTier = null,
  onOpenPersonaSwitcher = null,
}) {
  const [storeState, setStoreState] = useState(() => studentStore.getState());
  const [photoMode, setPhotoMode] = useState(null); // null | 'camera' | 'upload'
  const [capturedPhoto, setCapturedPhoto] = useState(null);
  const [countdown, setCountdown] = useState(null);
  const [cameraError, setCameraError] = useState(null);
  const [isFlashing, setIsFlashing] = useState(false);

  // Profile editable form fields
  const [name, setName] = useState('');
  const [grade, setGrade] = useState(10);
  const [school, setSchool] = useState('');
  const [isIndependent, setIsIndependent] = useState(false);

  // New parent link form
  const [showAddParent, setShowAddParent] = useState(false);
  const [parentName, setParentName] = useState('');
  const [parentContact, setParentContact] = useState('');
  const [parentRelation, setParentRelation] = useState('Mother');

  // Teacher join code
  const [teacherCode, setTeacherCode] = useState('');
  const [teacherJoinMessage, setTeacherJoinMessage] = useState(null);

  const videoRef = useRef(null);
  const streamRef = useRef(null);
  const fileInputRef = useRef(null);
  const countdownIntervalRef = useRef(null);

  // Subscribe to studentStore updates
  useEffect(() => {
    const unsub = studentStore.subscribe((next) => {
      setStoreState({ ...next });
    });
    return unsub;
  }, []);

  // Sync form state on open
  useEffect(() => {
    if (isOpen) {
      const state = studentStore.getState();
      setName(state.studentName || currentUser?.name || 'Nqobile Dlamini');
      setGrade(state.grade || currentUser?.grade || 10);
      setSchool(state.school || currentUser?.schoolName || 'Westville High School');
      setIsIndependent(Boolean(state.isIndependent || currentUser?.isIndependent));
      setPhotoMode(null);
      setCapturedPhoto(null);
      setShowAddParent(false);
      setTeacherCode('');
      setTeacherJoinMessage(null);
    }
  }, [isOpen, currentUser]);

  // Clean up camera stream
  const stopCamera = () => {
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
  };

  useEffect(() => {
    if (!isOpen || photoMode !== 'camera') {
      stopCamera();
    }
  }, [isOpen, photoMode]);

  // Start camera for selfie capture
  const startCamera = async () => {
    setCameraError(null);
    stopCamera();
    try {
      if (!navigator?.mediaDevices?.getUserMedia) {
        throw new Error('Camera is not supported on this device/browser.');
      }
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'user', width: { ideal: 640 }, height: { ideal: 640 } },
        audio: false,
      });
      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.play().catch(() => {});
      }
    } catch (err) {
      console.warn('Camera error:', err);
      setCameraError('Camera access unavailable. Please upload a photo from your device.');
    }
  };

  const handleSnapPhoto = () => {
    if (countdown !== null || !videoRef.current) return;
    setCountdown(3);
    let count = 3;
    countdownIntervalRef.current = setInterval(() => {
      count -= 1;
      if (count > 0) {
        setCountdown(count);
      } else {
        clearInterval(countdownIntervalRef.current);
        countdownIntervalRef.current = null;
        setCountdown(null);

        setIsFlashing(true);
        setTimeout(() => setIsFlashing(false), 200);

        try {
          const video = videoRef.current;
          if (!video) return;
          const canvas = document.createElement('canvas');
          canvas.width = 400;
          canvas.height = 400;
          const ctx = canvas.getContext('2d');
          const minDim = Math.min(video.videoWidth || 640, video.videoHeight || 640);
          const startX = ((video.videoWidth || 640) - minDim) / 2;
          const startY = ((video.videoHeight || 640) - minDim) / 2;
          ctx.translate(canvas.width, 0);
          ctx.scale(-1, 1);
          ctx.drawImage(video, startX, startY, minDim, minDim, 0, 0, 400, 400);
          const dataUrl = canvas.toDataURL('image/jpeg', 0.88);
          setCapturedPhoto(dataUrl);
          stopCamera();
        } catch (err) {
          console.error('Snap error:', err);
          setCameraError('Failed to capture photo from camera.');
        }
      }
    }, 1000);
  };

  const handleFileChange = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
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
      };
      img.src = event.target.result;
    };
    reader.readAsDataURL(file);
  };

  const handleSavePhoto = () => {
    if (!capturedPhoto) return;
    studentStore.updateProfilePhoto(capturedPhoto);
    setPhotoMode(null);
    setCapturedPhoto(null);
  };

  const handleSaveProfileDetails = () => {
    studentStore.updateProfileDetails({
      studentName: name.trim(),
      grade: Number(grade),
      school: isIndependent ? 'Independent Account' : school.trim(),
      isIndependent,
    });
    onClose();
  };

  const handleAddParentSubmit = (e) => {
    e.preventDefault();
    if (!parentName.trim()) return;
    try {
      studentStore.addParentLink({
        name: parentName.trim(),
        contact: parentContact.trim(),
        relationship: parentRelation,
      });
      setParentName('');
      setParentContact('');
      setShowAddParent(false);
    } catch (err) {
      alert(err.message);
    }
  };

  const handleTeacherJoin = (e) => {
    e.preventDefault();
    if (!teacherCode.trim()) return;
    const success = studentStore.joinTeacherClass(teacherCode);
    if (success) {
      setTeacherJoinMessage('Class joined successfully!');
      setTeacherCode('');
      setTimeout(() => setTeacherJoinMessage(null), 3000);
    }
  };

  if (!isOpen) return null;

  const currentPhoto = capturedPhoto || storeState.photoURL || currentUser?.photoURL;
  const isSuperAdmin = Boolean(
    currentUser?.isSuperAdmin || 
    (currentUser?.email && (currentUser.email.includes('princ') || currentUser.email.includes('admin')))
  );

  const phaseLabel = Number(grade) >= 10 ? 'FET Phase (Gr 10–12)' : 'Senior Phase (Gr 7–9)';
  const parentLinks = storeState.parentLinks || [];
  const teacherLinks = storeState.teacherLinks || [];

  return (
    <div 
      className="fixed inset-0 z-[120] flex items-center justify-center bg-black/60 backdrop-blur-xs p-3 sm:p-4 select-none animate-in fade-in duration-150 overflow-y-auto"
      onClick={onClose}
    >
      <div 
        className="w-full max-w-xl bg-white rounded-3xl border border-slate-200 shadow-2xl overflow-hidden flex flex-col max-h-[92vh] my-auto"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header Ribbon */}
        <div className="bg-[#13519C] text-white px-6 py-4 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white/10 flex items-center justify-center border border-white/20">
              <GraduationCap className="w-6 h-6 text-[#FF9100]" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-white leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                Learner Profile &amp; Settings
              </h3>
              <p className="text-xs text-blue-200">
                Manage your credentials, parent linkages, and school settings
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="p-1.5 rounded-full text-white/80 hover:text-white hover:bg-white/10 transition cursor-pointer"
            title="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Scrollable Body */}
        <div className="p-6 overflow-y-auto space-y-6 font-sans">
          
          {/* 1. Avatar & Photo Manager */}
          <div className="flex flex-col sm:flex-row items-center gap-5 p-4 rounded-2xl bg-slate-50 border border-slate-200/90">
            <div className="relative group shrink-0">
              <div className="w-20 h-20 rounded-full overflow-hidden border-3 border-[#13519C] shadow-md bg-white flex items-center justify-center">
                {currentPhoto ? (
                  <img src={currentPhoto} alt={name} className="w-full h-full object-cover" />
                ) : (
                  <span className="text-xl font-extrabold text-[#13519C]">
                    {(name || 'FL').split(' ').map((n) => n[0]).slice(0, 2).join('')}
                  </span>
                )}
              </div>
              <button
                type="button"
                onClick={() => {
                  setPhotoMode('camera');
                  startCamera();
                }}
                className="absolute bottom-0 right-0 p-1.5 rounded-full bg-[#13519C] text-white shadow-md hover:bg-[#0b376b] transition cursor-pointer"
                title="Change Photo"
              >
                <Camera className="w-3.5 h-3.5" />
              </button>
            </div>

            <div className="flex-1 text-center sm:text-left space-y-1">
              <h4 className="font-bold text-slate-900 text-base" style={{ fontFamily: 'Afacad, sans-serif' }}>
                {name || 'Learner Name'}
              </h4>
              <p className="text-xs text-slate-500 font-medium">
                {isIndependent ? 'Independent Account' : school} • Grade {grade} • {phaseLabel}
              </p>
              <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2 pt-1">
                <button
                  type="button"
                  onClick={() => {
                    setPhotoMode('camera');
                    startCamera();
                  }}
                  className="px-3 py-1 rounded-xl bg-blue-50 text-[#13519C] border border-blue-200 text-xs font-bold hover:bg-blue-100 transition cursor-pointer flex items-center gap-1.5"
                >
                  <Camera className="w-3 h-3" />
                  <span>Take Selfie</span>
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setPhotoMode('upload');
                    fileInputRef.current?.click();
                  }}
                  className="px-3 py-1 rounded-xl bg-slate-100 text-slate-700 border border-slate-200 text-xs font-bold hover:bg-slate-200 transition cursor-pointer flex items-center gap-1.5"
                >
                  <Upload className="w-3 h-3" />
                  <span>Upload Image</span>
                </button>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept="image/*"
                  className="hidden"
                  onChange={handleFileChange}
                />
              </div>
            </div>
          </div>

          {/* Photo Capture Modal / Drawer (if photoMode is active) */}
          {photoMode && (
            <div className="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-3 animate-in fade-in duration-200">
              <div className="flex items-center justify-between text-xs font-bold text-[#13519C]">
                <span>{capturedPhoto ? 'Preview New Photo' : photoMode === 'camera' ? 'Live Camera Capture' : 'Upload Image'}</span>
                <button 
                  type="button" 
                  onClick={() => {
                    stopCamera();
                    setPhotoMode(null);
                    setCapturedPhoto(null);
                  }}
                  className="text-slate-500 hover:text-slate-800"
                >
                  Cancel
                </button>
              </div>

              {capturedPhoto ? (
                <div className="flex items-center gap-4">
                  <div className="w-20 h-20 rounded-full overflow-hidden border-2 border-emerald-500 shadow-sm shrink-0">
                    <img src={capturedPhoto} alt="New preview" className="w-full h-full object-cover" />
                  </div>
                  <div className="flex items-center gap-2">
                    <button
                      type="button"
                      onClick={handleSavePhoto}
                      className="px-4 py-2 rounded-xl bg-emerald-600 text-white font-bold text-xs shadow-xs hover:bg-emerald-700 transition cursor-pointer flex items-center gap-1.5"
                    >
                      <Check className="w-3.5 h-3.5" />
                      <span>Confirm &amp; Save</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => setCapturedPhoto(null)}
                      className="px-3 py-2 rounded-xl bg-white border border-slate-200 text-slate-700 font-bold text-xs hover:bg-slate-50 transition cursor-pointer"
                    >
                      Retake
                    </button>
                  </div>
                </div>
              ) : photoMode === 'camera' ? (
                <div className="flex flex-col items-center gap-3">
                  {cameraError ? (
                    <div className="text-xs text-rose-700 bg-rose-50 p-3 rounded-xl border border-rose-200 flex items-center gap-2">
                      <AlertCircle className="w-4 h-4 shrink-0" />
                      <span>{cameraError}</span>
                    </div>
                  ) : (
                    <div className="relative w-44 h-44 rounded-full overflow-hidden border-4 border-[#13519C] shadow-inner bg-black flex items-center justify-center">
                      <video ref={videoRef} autoPlay playsInline muted className="w-full h-full object-cover scale-x-[-1]" />
                      {countdown !== null && (
                        <div className="absolute inset-0 bg-black/40 flex items-center justify-center text-4xl font-extrabold text-white animate-ping">
                          {countdown}
                        </div>
                      )}
                      {isFlashing && <div className="absolute inset-0 bg-white" />}
                    </div>
                  )}
                  <button
                    type="button"
                    onClick={handleSnapPhoto}
                    disabled={countdown !== null || Boolean(cameraError)}
                    className="px-5 py-2 rounded-xl bg-[#13519C] text-white font-bold text-xs shadow-md hover:bg-[#0b376b] transition cursor-pointer disabled:opacity-50 flex items-center gap-1.5"
                  >
                    <Camera className="w-3.5 h-3.5" />
                    <span>{countdown ? `Snapping in ${countdown}...` : '📸 Snap Photo'}</span>
                  </button>
                </div>
              ) : null}
            </div>
          )}

          {/* 2. Basic Profile Info */}
          <div className="space-y-4">
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500">
              Personal Information
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Full Name</label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:outline-hidden focus:ring-2 focus:ring-[#13519C]"
                  placeholder="e.g. Nqobile Dlamini"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">Grade</label>
                <select
                  value={grade}
                  onChange={(e) => setGrade(Number(e.target.value))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm bg-white focus:outline-hidden focus:ring-2 focus:ring-[#13519C]"
                >
                  <option value={7}>Grade 7</option>
                  <option value={8}>Grade 8</option>
                  <option value={9}>Grade 9</option>
                  <option value={10}>Grade 10</option>
                  <option value={11}>Grade 11</option>
                  <option value={12}>Grade 12</option>
                </select>
              </div>

              <div className="sm:col-span-2">
                <div className="flex items-center justify-between mb-1">
                  <label className="text-xs font-semibold text-slate-700">School Affiliation</label>
                  <label className="flex items-center gap-2 cursor-pointer text-xs font-bold text-[#13519C]">
                    <input
                      type="checkbox"
                      checked={isIndependent}
                      onChange={(e) => setIsIndependent(e.target.checked)}
                      className="rounded text-[#13519C] focus:ring-[#13519C]"
                    />
                    <span>Independent Account / Homeschool</span>
                  </label>
                </div>
                {!isIndependent ? (
                  <input
                    type="text"
                    value={school}
                    onChange={(e) => setSchool(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:outline-hidden focus:ring-2 focus:ring-[#13519C]"
                    placeholder="e.g. Westville High School"
                  />
                ) : (
                  <div className="p-2.5 rounded-xl bg-purple-50 border border-purple-200 text-xs text-purple-900 font-medium">
                    🏡 Independent Account active: you receive self-paced study with zero school homework deadlines.
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* 3. Parent / Guardian Links (Allowance of up to 2 links - Item 5) */}
          <div className="space-y-3 pt-2 border-t border-slate-100">
            <div className="flex items-center justify-between">
              <div>
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500">
                  Parent / Guardian Links ({parentLinks.length}/2)
                </h4>
                <p className="text-[11px] text-slate-400">
                  Weekly Sunday Academic Pulse sent via WhatsApp / SMS (POPIA Section 35 verified)
                </p>
              </div>
              {parentLinks.length < 2 && !showAddParent && (
                <button
                  type="button"
                  onClick={() => setShowAddParent(true)}
                  className="px-3 py-1 rounded-xl bg-blue-50 text-[#13519C] hover:bg-blue-100 border border-blue-200 text-xs font-bold transition cursor-pointer flex items-center gap-1"
                >
                  <UserPlus className="w-3 h-3" />
                  <span>Add Parent</span>
                </button>
              )}
            </div>

            {/* Existing Parent Links */}
            <div className="space-y-2">
              {parentLinks.map((parent) => (
                <div 
                  key={parent.id}
                  className="p-3 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-between text-xs"
                >
                  <div className="space-y-0.5">
                    <div className="flex items-center gap-2">
                      <span className="font-bold text-slate-900">{parent.name}</span>
                      <span className="px-2 py-0.2 rounded-full bg-blue-100 text-[#13519C] text-[10px] font-extrabold">
                        {parent.relationship || 'Guardian'}
                      </span>
                      <span className="px-1.5 py-0.2 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-bold">
                        ✓ Linked
                      </span>
                    </div>
                    <span className="text-[11px] text-slate-500 block">{parent.contact || 'No phone recorded'}</span>
                  </div>
                  <button
                    type="button"
                    onClick={() => studentStore.removeParentLink(parent.id)}
                    className="p-1.5 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition cursor-pointer"
                    title="Remove Parent Link"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              ))}
            </div>

            {/* Add Parent Form */}
            {showAddParent && (
              <form onSubmit={handleAddParentSubmit} className="p-3.5 rounded-2xl bg-blue-50/70 border border-blue-200 space-y-2 text-xs">
                <span className="font-bold text-[#13519C] block">Link Additional Parent or Guardian</span>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
                  <input
                    type="text"
                    value={parentName}
                    onChange={(e) => setParentName(e.target.value)}
                    placeholder="Parent Full Name"
                    required
                    className="px-2.5 py-1.5 rounded-lg border border-slate-300 bg-white text-xs"
                  />
                  <input
                    type="text"
                    value={parentContact}
                    onChange={(e) => setParentContact(e.target.value)}
                    placeholder="WhatsApp / Cell Number"
                    required
                    className="px-2.5 py-1.5 rounded-lg border border-slate-300 bg-white text-xs"
                  />
                  <select
                    value={parentRelation}
                    onChange={(e) => setParentRelation(e.target.value)}
                    className="px-2.5 py-1.5 rounded-lg border border-slate-300 bg-white text-xs"
                  >
                    <option value="Mother">Mother</option>
                    <option value="Father">Father</option>
                    <option value="Legal Guardian">Legal Guardian</option>
                    <option value="Sponsor">Sponsor</option>
                  </select>
                </div>
                <div className="flex items-center justify-end gap-2 pt-1">
                  <button
                    type="button"
                    onClick={() => setShowAddParent(false)}
                    className="px-3 py-1 rounded-lg text-slate-600 hover:bg-slate-200 font-bold transition cursor-pointer"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-3 py-1 rounded-lg bg-[#13519C] text-white font-bold hover:bg-[#0b376b] transition cursor-pointer"
                  >
                    Save Parent Link
                  </button>
                </div>
              </form>
            )}
          </div>

          {/* 4. Teacher Links & Class Join Code */}
          <div className="space-y-3 pt-2 border-t border-slate-100">
            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500">
                Connected Teachers &amp; Classes
              </h4>
              <p className="text-[11px] text-slate-400">
                Enter your educator's 6-character class code to receive authentic school tasks
              </p>
            </div>

            <form onSubmit={handleTeacherJoin} className="flex items-center gap-2">
              <input
                type="text"
                value={teacherCode}
                onChange={(e) => setTeacherCode(e.target.value.toUpperCase())}
                placeholder="Join Code (e.g. ACC10A)"
                maxLength={8}
                className="flex-1 px-3 py-2 rounded-xl border border-slate-300 text-xs font-mono uppercase font-bold focus:outline-hidden focus:ring-2 focus:ring-[#13519C]"
              />
              <button
                type="submit"
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-bold text-xs transition cursor-pointer shrink-0"
              >
                Join Class
              </button>
            </form>

            {teacherJoinMessage && (
              <span className="text-xs text-emerald-700 font-bold block">{teacherJoinMessage}</span>
            )}

            <div className="space-y-1.5">
              {teacherLinks.map((t) => (
                <div 
                  key={t.id}
                  className="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-between text-xs"
                >
                  <div>
                    <span className="font-bold text-slate-800">{t.name}</span>
                    <span className="text-slate-500 text-[11px] block">{t.subject} • Code: {t.code}</span>
                  </div>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200">
                    Connected ✓
                  </span>
                </div>
              ))}
            </div>
          </div>

          {/* 5. Super Admin Switcher (Item 15 - Hidden inside Profile to keep UI clean) */}
          {isSuperAdmin && (
            <div className="p-4 rounded-2xl bg-amber-50/80 border border-amber-300/80 space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2 text-amber-950 font-bold text-xs">
                  <Shield className="w-4 h-4 text-amber-600" />
                  <span>Super Admin Control Center</span>
                </div>
                <span className="text-[10px] bg-amber-200/80 text-amber-900 font-mono font-bold px-2 py-0.5 rounded-full">
                  Privileged
                </span>
              </div>
              <p className="text-[11px] text-amber-800 leading-snug">
                Switch perspective without cluttering the main student ribbon.
              </p>

              {/* 5 Roles */}
              {setSuperAdminMode && (
                <div className="space-y-1">
                  <span className="text-[10px] font-bold text-amber-900 uppercase tracking-wider block">Perspective Switcher:</span>
                  <div className="grid grid-cols-3 sm:grid-cols-5 gap-1.5">
                    {[
                      { role: 'student', label: 'Student' },
                      { role: 'parent', label: 'Parent' },
                      { role: 'teacher', label: 'Teacher' },
                      { role: 'school', label: 'School' },
                      { role: 'admin', label: 'Super Admin' },
                    ].map((item) => (
                      <button
                        key={item.role}
                        type="button"
                        data-testid={`btn-admin-role-${item.role}`}
                        onClick={() => {
                          setSuperAdminMode(item.role);
                          if (onClose) onClose();
                        }}
                        className={`px-2 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer text-center ${
                          superAdminMode === item.role
                            ? 'bg-[#13519C] text-white shadow-xs'
                            : 'bg-white text-slate-700 hover:bg-amber-100 border border-amber-200'
                        }`}
                      >
                        {item.label}
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* Tier Switcher & Mock School */}
              <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-amber-200/60 text-xs">
                {setSuperAdminTier && (
                  <div className="flex items-center gap-1.5">
                    <span className="font-bold text-amber-900 text-[11px]">Tutoring Tier:</span>
                    <button
                      type="button"
                      onClick={() => setSuperAdminTier('standard')}
                      className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${
                        superAdminTier === 'standard'
                          ? 'bg-purple-700 text-white shadow-xs'
                          : 'bg-white text-slate-700 border border-amber-200'
                      }`}
                    >
                      Standard
                    </button>
                    <button
                      type="button"
                      onClick={() => setSuperAdminTier('pro')}
                      className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${
                        superAdminTier === 'pro'
                          ? 'bg-purple-700 text-white shadow-xs'
                          : 'bg-white text-slate-700 border border-amber-200'
                      }`}
                    >
                      Pro Socratic
                    </button>
                  </div>
                )}

                {onOpenPersonaSwitcher && (
                  <button
                    type="button"
                    onClick={() => {
                      onClose();
                      onOpenPersonaSwitcher();
                    }}
                    className="px-3 py-1 rounded-lg bg-amber-600 text-white font-bold text-xs hover:bg-amber-700 transition cursor-pointer flex items-center gap-1 shadow-xs"
                  >
                    <Users className="w-3.5 h-3.5" />
                    <span>Mock School Tester</span>
                  </button>
                )}
              </div>
            </div>
          )}

        </div>

        {/* Footer Actions: Save Profile + Log Out Button (Item 2) */}
        <div className="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between gap-3 shrink-0">
          {/* Prominent Log Out Button (Item 2) */}
          <button
            type="button"
            onClick={() => {
              onClose();
              if (typeof onLogout === 'function') {
                onLogout();
              }
            }}
            className="px-4 py-2.5 rounded-xl border border-rose-300 text-rose-700 hover:bg-rose-50 active:bg-rose-100 font-bold text-xs sm:text-sm flex items-center gap-2 transition cursor-pointer"
            title="Log out of Fundile on this device"
          >
            <LogOut className="w-4 h-4" />
            <span>Sign Out</span>
          </button>

          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2.5 rounded-xl border border-slate-300 text-slate-700 hover:bg-slate-100 font-bold text-xs sm:text-sm transition cursor-pointer"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={handleSaveProfileDetails}
              className="px-5 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0b376b] text-white font-bold text-xs sm:text-sm shadow-md shadow-blue-900/20 transition cursor-pointer"
              style={{ fontFamily: 'Afacad, sans-serif' }}
            >
              Save Profile
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
