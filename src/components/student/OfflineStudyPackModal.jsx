import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { 
  X, 
  Download, 
  CheckCircle2, 
  AlertCircle, 
  Trash2, 
  Wifi, 
  HardDrive, 
  Calendar, 
  Layers,
  Sparkles,
  RefreshCw
} from 'lucide-react';
import offlineStorageService from '../../services/offlineStorageService';
import { getSubjectTheme } from '../../theme/subjectPalette';
import { ALL_FET_PHASE_SUBJECTS, ALL_SENIOR_PHASE_SUBJECTS } from '../curriculum/SubjectManagerModal';

/**
 * OfflineStudyPackModal
 * 
 * Provides an on-demand, user-selected 30-Day Offline Study Pack downloader
 * adhering to the Hybrid 2-Tier Balance (Zero-LLM deterministic bundles,
 * Wi-Fi only toggle, transparent MB indicator, and cryptographic lease countdown).
 */
export default function OfflineStudyPackModal({
  isOpen = false,
  onClose = () => {},
  grade = 10,
  enabledSubjects = ['accounting', 'mathematics', 'physical_sciences', 'life_sciences', 'business_studies'],
  studentId = 'local_learner',
  onPackDownloaded = () => {}
}) {
  const isSeniorPhase = Number(grade) <= 9;
  const fullPhaseList = isSeniorPhase ? ALL_SENIOR_PHASE_SUBJECTS : ALL_FET_PHASE_SUBJECTS;
  const enrolledSubjectItems = useMemo(() => {
    return fullPhaseList.filter(s => enabledSubjects.includes(s.id));
  }, [fullPhaseList, enabledSubjects]);

  const [selectedSubjects, setSelectedSubjects] = useState(() => []);
  const [selectedTerm, setSelectedTerm] = useState(1);
  const [questionsPerTopic, setQuestionsPerTopic] = useState(5);
  const [wifiOnly, setWifiOnly] = useState(true);
  
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [downloadStatusText, setDownloadStatusText] = useState('');
  const [errorMsg, setErrorMsg] = useState('');

  const [cachedPacks, setCachedPacks] = useState([]);
  const [storageUsage, setStorageUsage] = useState({ totalKb: 0, totalMb: 0, packCount: 0 });

  // Load existing cached packs and storage usage
  const loadCachedPacks = useCallback(async () => {
    try {
      const packs = await offlineStorageService.getAllPacks();
      setCachedPacks(packs);
      const usage = await offlineStorageService.getStorageUsage();
      setStorageUsage(usage);
    } catch (err) {
      console.warn('Failed to load cached packs:', err);
    }
  }, []);

  useEffect(() => {
    if (isOpen) {
      loadCachedPacks();
      setErrorMsg('');
      setDownloadProgress(0);
    }
  }, [isOpen, loadCachedPacks]);

  // Toggle subject selection
  const handleToggleSubject = (subjectId) => {
    setSelectedSubjects(prev => {
      if (prev.includes(subjectId)) {
        return prev.filter(id => id !== subjectId);
      } else {
        return [...prev, subjectId];
      }
    });
  };

  // Estimated size calculation
  // Each question is ~2.2 KB in full 6-pillar JSON with worked solution & 3-tier hints
  const estimatedKb = useMemo(() => {
    const avgTopicsPerSubject = 3.5;
    const totalQuestions = selectedSubjects.length * avgTopicsPerSubject * questionsPerTopic;
    return Math.round(totalQuestions * 2.2);
  }, [selectedSubjects.length, questionsPerTopic]);

  const estimatedMb = useMemo(() => {
    return (estimatedKb / 1024).toFixed(2);
  }, [estimatedKb]);

  // Execute download of study pack
  const handleStartDownload = async () => {
    if (selectedSubjects.length === 0) {
      setErrorMsg('Please select at least one subject to download.');
      return;
    }

    if (wifiOnly && !offlineStorageService.isWifiConnection()) {
      setErrorMsg('Wi-Fi Only is enabled, but you are currently connected via mobile cellular data. Disable "Wi-Fi Only" or connect to a Wi-Fi network to continue.');
      return;
    }

    setIsDownloading(true);
    setErrorMsg('');
    setDownloadProgress(5);
    setDownloadStatusText('Connecting to question engine...');

    try {
      const total = selectedSubjects.length;
      let completed = 0;

      for (const subjId of selectedSubjects) {
        setDownloadStatusText(`Generating 30-day pack for ${subjId.replace('_', ' ').toUpperCase()}...`);
        
        const res = await fetch('/api/offline/pack', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            subject: subjId,
            grade: String(grade),
            term: selectedTerm,
            count_per_topic: questionsPerTopic,
            student_id: studentId
          })
        });

        if (!res.ok) {
          throw new Error(`Failed to generate pack for ${subjId} (HTTP ${res.status})`);
        }

        const packData = await res.json();
        await offlineStorageService.saveQuestionPack(packData);

        completed += 1;
        setDownloadProgress(Math.round((completed / total) * 90));
      }

      setDownloadProgress(100);
      setDownloadStatusText('All packs verified and encrypted in local storage!');
      await loadCachedPacks();
      onPackDownloaded();
      setTimeout(() => {
        setIsDownloading(false);
        setDownloadProgress(0);
        setDownloadStatusText('');
      }, 1500);

    } catch (err) {
      console.error('Download error:', err);
      setErrorMsg(err.message || 'An error occurred during pack download.');
      setIsDownloading(false);
    }
  };

  // Delete individual pack
  const handleDeletePack = async (packId) => {
    try {
      await offlineStorageService.deletePack(packId);
      await loadCachedPacks();
    } catch (err) {
      console.warn('Failed to delete pack:', err);
    }
  };

  // Clear all storage
  const handleClearAll = async () => {
    if (window.confirm('Are you sure you want to delete all cached offline packs and saved drafts?')) {
      try {
        await offlineStorageService.clearAllStorage();
        await loadCachedPacks();
      } catch (err) {
        console.warn('Failed to clear storage:', err);
      }
    }
  };

  if (!isOpen) return null;

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-900/60 backdrop-blur-sm animate-fadeIn"
      data-testid="offline-study-pack-modal"
    >
      <div 
        className="bg-white rounded-2xl shadow-2xl border border-slate-200/90 w-full max-w-2xl max-h-[90vh] flex flex-col overflow-hidden font-sans"
        role="dialog"
        aria-modal="true"
      >
        {/* Modal Header */}
        <div className="px-5 py-4 border-b border-slate-200/90 flex items-center justify-between bg-slate-50/80">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-violet-600 text-white flex items-center justify-center font-bold text-lg shadow-sm">
              📦
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-900 font-display">
                30-Day Offline Study Packs
              </h3>
              <p className="text-xs text-slate-500">
                Grade {grade} • Deterministic Exam-Standard Questions & Pre-Computed Hints
              </p>
            </div>
          </div>

          <button
            type="button"
            data-testid="btn-close-offline-modal"
            onClick={onClose}
            className="w-8 h-8 rounded-full hover:bg-slate-200/80 text-slate-500 hover:text-slate-800 flex items-center justify-center transition cursor-pointer"
            title="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-5 overflow-y-auto space-y-5 flex-1">
          {/* Term Selector */}
          <div>
            <label className="text-xs font-bold text-slate-700 uppercase tracking-wider block mb-2">
              1. Select Curriculum Term
            </label>
            <div className="grid grid-cols-4 gap-2">
              {[1, 2, 3, 4].map(t => (
                <button
                  key={t}
                  type="button"
                  data-testid={`term-select-${t}`}
                  onClick={() => setSelectedTerm(t)}
                  className={`py-2 px-3 rounded-xl text-xs font-bold transition flex flex-col items-center gap-0.5 cursor-pointer border ${
                    selectedTerm === t
                      ? 'bg-violet-50 text-violet-800 border-violet-400 shadow-xs'
                      : 'bg-slate-50 hover:bg-slate-100 text-slate-600 border-slate-200'
                  }`}
                >
                  <span>Term {t}</span>
                  <span className="text-[10px] font-normal text-slate-400">
                    {t === 1 ? 'Control Test' : t === 2 ? 'Mid-Year' : t === 3 ? 'Trial Exam' : 'Final Exam'}
                  </span>
                </button>
              ))}
            </div>
          </div>

          {/* Enrolled Subjects Checkboxes */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                2. Select Enrolled Subjects
              </label>
              <button
                type="button"
                onClick={() => {
                  if (selectedSubjects.length === enrolledSubjectItems.length) {
                    setSelectedSubjects([]);
                  } else {
                    setSelectedSubjects(enrolledSubjectItems.map(s => s.id));
                  }
                }}
                className="text-[11px] font-bold text-violet-700 hover:text-violet-900 underline cursor-pointer"
              >
                {selectedSubjects.length === enrolledSubjectItems.length ? 'Deselect All' : 'Select All'}
              </button>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 max-h-48 overflow-y-auto p-1">
              {enrolledSubjectItems.map(subj => {
                const isSelected = selectedSubjects.includes(subj.id);
                const theme = getSubjectTheme(subj.id);

                return (
                  <label
                    key={subj.id}
                    className={`flex items-center justify-between p-2.5 rounded-xl border transition cursor-pointer select-none ${
                      isSelected 
                        ? 'bg-violet-50/60 border-violet-300 shadow-xs' 
                        : 'bg-white hover:bg-slate-50 border-slate-200 text-slate-600'
                    }`}
                  >
                    <div className="flex items-center gap-2.5">
                      <input
                        type="checkbox"
                        data-testid={`checkbox-subject-${subj.id}`}
                        checked={isSelected}
                        onChange={() => handleToggleSubject(subj.id)}
                        className="w-4 h-4 rounded text-violet-600 focus:ring-violet-500 cursor-pointer"
                      />
                      <span 
                        className="w-2.5 h-2.5 rounded-full shrink-0" 
                        style={{ backgroundColor: theme.base }}
                      />
                      <span className="text-xs font-bold text-slate-800">
                        {subj.name}
                      </span>
                    </div>
                    <span className="text-[10px] text-slate-400 font-mono">
                      ~4 topics
                    </span>
                  </label>
                );
              })}
            </div>
          </div>

          {/* Drill Volume & Network Controls */}
          <div className="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div>
                <label className="text-xs font-bold text-slate-800 block">
                  Questions per Topic
                </label>
                <p className="text-[11px] text-slate-500">
                  Isomorphic variants generated with seeded SymPy entropy.
                </p>
              </div>
              <div className="flex items-center gap-1.5">
                {[5, 10, 15].map(cnt => (
                  <button
                    key={cnt}
                    type="button"
                    onClick={() => setQuestionsPerTopic(cnt)}
                    className={`px-3 py-1 rounded-lg text-xs font-bold transition cursor-pointer border ${
                      questionsPerTopic === cnt
                        ? 'bg-white text-violet-800 border-violet-300 shadow-2xs'
                        : 'bg-transparent text-slate-600 border-transparent hover:bg-slate-200/60'
                    }`}
                  >
                    {cnt} Qs
                  </button>
                ))}
              </div>
            </div>

            <div className="flex items-center justify-between pt-2 border-t border-slate-200/80">
              <div className="flex items-center gap-2">
                <Wifi className="w-4 h-4 text-slate-500" />
                <span className="text-xs font-semibold text-slate-700">
                  Wi-Fi Only Download
                </span>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  data-testid="wifi-only-toggle"
                  checked={wifiOnly}
                  onChange={(e) => setWifiOnly(e.target.checked)}
                  className="sr-only peer"
                />
                <div className="w-9 h-5 bg-slate-300 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-violet-600"></div>
              </label>
            </div>
          </div>

          {/* Size & Footprint Indicator */}
          <div className="flex items-center justify-between p-3 rounded-xl bg-violet-50/70 border border-violet-200">
            <div className="flex items-center gap-2">
              <HardDrive className="w-4 h-4 text-violet-700" />
              <div>
                <span className="text-xs font-bold text-violet-900 block">
                  Estimated Download Size: ~{estimatedKb} KB ({estimatedMb} MB)
                </span>
                <span className="text-[10px] text-violet-700">
                  Lightweight JSON format • Valid offline for 30 days
                </span>
              </div>
            </div>
            <span className="text-xs font-black text-violet-900 px-2.5 py-1 rounded-lg bg-white border border-violet-200 shadow-2xs font-mono">
              {selectedSubjects.length} Subjects
            </span>
          </div>

          {/* Download Progress or Status */}
          {isDownloading && (
            <div className="space-y-2 p-3 bg-blue-50 border border-blue-200 rounded-xl animate-fadeIn">
              <div className="flex items-center justify-between text-xs font-bold text-blue-900">
                <span>{downloadStatusText}</span>
                <span>{downloadProgress}%</span>
              </div>
              <div className="w-full h-2 rounded-full bg-blue-200 overflow-hidden">
                <div 
                  className="h-full bg-blue-600 transition-all duration-300 ease-out" 
                  style={{ width: `${downloadProgress}%` }}
                />
              </div>
            </div>
          )}

          {/* Error Message */}
          {errorMsg && (
            <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-xs text-rose-800 flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0 text-rose-600" />
              <span>{errorMsg}</span>
            </div>
          )}

          {/* Download Action Button */}
          <button
            type="button"
            data-testid="btn-download-offline-pack"
            onClick={handleStartDownload}
            disabled={isDownloading || selectedSubjects.length === 0}
            className={`w-full py-3 rounded-xl text-xs font-bold transition flex items-center justify-center gap-2 cursor-pointer shadow-md ${
              isDownloading || selectedSubjects.length === 0
                ? 'bg-slate-300 text-slate-500 cursor-not-allowed'
                : 'bg-violet-600 hover:bg-violet-700 active:scale-95 text-white'
            }`}
          >
            {isDownloading ? (
              <>
                <RefreshCw className="w-4 h-4 animate-spin" />
                <span>Downloading Study Packs...</span>
              </>
            ) : (
              <>
                <Download className="w-4 h-4" />
                <span>Download 30-Day Pack ({estimatedMb} MB)</span>
              </>
            )}
          </button>

          {/* Existing Cached Packs Section */}
          <div className="pt-3 border-t border-slate-200">
            <div className="flex items-center justify-between mb-2">
              <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider">
                Locally Cached Study Packs ({cachedPacks.length})
              </h4>
              {cachedPacks.length > 0 && (
                <button
                  type="button"
                  data-testid="btn-clear-all-offline"
                  onClick={handleClearAll}
                  className="text-[11px] font-bold text-rose-600 hover:text-rose-800 transition cursor-pointer"
                >
                  Clear All Cache
                </button>
              )}
            </div>

            {cachedPacks.length === 0 ? (
              <p className="text-xs text-slate-400 italic py-2">
                No offline study packs currently downloaded. Select your subjects above to download.
              </p>
            ) : (
              <div className="space-y-2 max-h-40 overflow-y-auto p-1">
                {cachedPacks.map(pack => (
                  <div
                    key={pack.id}
                    className="flex items-center justify-between p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs"
                  >
                    <div>
                      <div className="font-bold text-slate-800 flex items-center gap-1.5">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500" />
                        <span>{pack.subject_name || pack.subject} (Term {pack.term})</span>
                      </div>
                      <div className="text-[10px] text-slate-500">
                        {pack.total_questions} questions • {pack.size_kb} KB • 
                        {pack.isExpired ? (
                          <span className="text-rose-600 font-bold ml-1">Lease Expired</span>
                        ) : (
                          <span className="text-emerald-700 ml-1">Active 30-Day Lease</span>
                        )}
                      </div>
                    </div>

                    <button
                      type="button"
                      data-testid={`btn-delete-pack-${pack.id}`}
                      onClick={() => handleDeletePack(pack.id)}
                      className="p-1.5 rounded-lg text-slate-400 hover:text-rose-600 hover:bg-rose-50 transition cursor-pointer"
                      title="Delete pack"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Modal Footer */}
        <div className="px-5 py-3 border-t border-slate-200/90 bg-slate-50 flex items-center justify-between text-xs text-slate-500">
          <span>Current Storage Footprint: {storageUsage.totalMb} MB</span>
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl text-slate-700 hover:bg-slate-200/80 font-bold transition cursor-pointer"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
