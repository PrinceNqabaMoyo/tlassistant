import React, { useState, useMemo, useEffect } from 'react';
import { 
  X, 
  Search, 
  BookOpen, 
  CheckCircle2, 
  AlertCircle, 
  Clock, 
  GraduationCap, 
  Sparkles,
  ChevronRight,
  Filter
} from 'lucide-react';
import studentStore from '../../services/studentStore';
import { curriculumData } from '../../curriculumData';

/**
 * Normalizes subject names across various formats (id, title, abbreviation)
 * to match keys in curriculumData.js
 */
const normalizeSubjectName = (subject) => {
  const s = String(subject || '').toLowerCase().replace(/[\s_-]+/g, '');
  if (s.includes('acc')) return 'Accounting';
  if (s.includes('bus')) return 'Business Studies';
  if (s.includes('ems') || s.includes('economic')) return 'Economic and Management Sciences';
  if (s.includes('lit') || s.includes('mathslit')) return 'Mathematical Literacy';
  if (s.includes('tech')) return 'Technical Mathematics';
  if (s.includes('math')) return 'Mathematics';
  if (s.includes('phys')) return 'Physical Sciences';
  if (s.includes('life') || s.includes('bio')) return 'Life Sciences';
  if (s.includes('nat')) return 'Natural Sciences';
  return 'Mathematics';
};

/**
 * South African CAPS Term topic distribution rules.
 * Assigns topics to Terms 1, 2, 3, or 4 based on CAPS syllabus.
 */
const getTermForTopic = (subjectName, topicName, index, totalTopics) => {
  const t = topicName.toLowerCase();

  // Term 1 Rules
  if (
    t.includes('algebra') || t.includes('expression') || t.includes('exponent') || 
    t.includes('pattern') || t.includes('number') || t.includes('principle') ||
    t.includes('crj') || t.includes('cash receipt') || t.includes('tariff') ||
    t.includes('vector') || t.includes('kinematic') || t.includes('motion in 1d') ||
    t.includes('matter') || t.includes('cell') || t.includes('mitosis') ||
    t.includes('environment') || t.includes('micro') || t.includes('vat')
  ) {
    return 1;
  }

  // Term 2 Rules
  if (
    t.includes('function') || t.includes('linear') || t.includes('analytical') ||
    t.includes('newton') || t.includes('momentum') || t.includes('chemical bonding') ||
    t.includes('reconciliation') || t.includes('bank') || t.includes('sole trader') ||
    t.includes('tax') || t.includes('paye') || t.includes('conversion') ||
    t.includes('map') || t.includes('plan') || t.includes('creative thinking') ||
    t.includes('photosynthesis') || t.includes('nutrition') || t.includes('ownership')
  ) {
    return 2;
  }

  // Term 3 Rules
  if (
    t.includes('euclidean') || t.includes('geometry') || t.includes('trigonometr') ||
    t.includes('measurement') || t.includes('mensuration') || t.includes('cost accounting') ||
    t.includes('manufacturing') || t.includes('adjustment') || t.includes('electric') ||
    t.includes('circuit') || t.includes('energy') || t.includes('power') ||
    t.includes('human resources') || t.includes('respiration') || t.includes('gas exchange') ||
    t.includes('nervous') || t.includes('volume') || t.includes('interest') ||
    t.includes('loan') || t.includes('banking') || t.includes('data handling')
  ) {
    return 3;
  }

  // Term 4 Rules
  if (
    t.includes('statistic') || t.includes('probabilit') || t.includes('budget') ||
    t.includes('interpretation') || t.includes('ratio') || t.includes('wave') ||
    t.includes('sound') || t.includes('light') || t.includes('operation') ||
    t.includes('quality') || t.includes('evolution') || t.includes('genetics') ||
    t.includes('ecology') || t.includes('exam') || t.includes('revision')
  ) {
    return 4;
  }

  // Default balanced quadrant distribution
  if (totalTopics > 0) {
    const quadrant = Math.floor((index / totalTopics) * 4) + 1;
    return Math.min(4, Math.max(1, quadrant));
  }
  return 1;
};

/**
 * Fallback CAPS topics when curriculumData does not have entries
 */
const FALLBACK_CAPS_TOPICS = {
  'Mathematical Literacy': {
    10: [
      { name: 'Tariffs and Break-even Analysis', term: 1 },
      { name: 'Numbers and Calculations with Money', term: 1 },
      { name: 'Financial Documents & Invoices', term: 1 },
      { name: 'Measurement: Perimeter & Area', term: 2 },
      { name: 'Conversions and Scale Ratios', term: 2 },
      { name: 'Taxation: VAT & Income Tax (PAYE)', term: 2 },
      { name: 'Maps, Floor Plans and Direction', term: 3 },
      { name: 'Measurement: Volume & Packaging', term: 3 },
      { name: 'Finance: Banking & Loan Interest', term: 3 },
      { name: 'Data Handling and Summaries', term: 4 },
      { name: 'Probability and Risk Estimation', term: 4 },
      { name: 'Integrated Exam Case Studies', term: 4 },
    ]
  }
};

export default function TopicScopeModal({
  isOpen,
  onClose,
  subject = 'mathematics',
  grade = 10,
  currentTopic = '',
  onSelectTopic = () => {}
}) {
  const [selectedTerm, setSelectedTerm] = useState(1);
  const [searchQuery, setSearchQuery] = useState('');
  const [storeState, setStoreState] = useState(() => studentStore.getState());

  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  // Close on Escape key press
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  const normalizedSubject = normalizeSubjectName(subject);
  const numericGrade = parseInt(String(grade).replace(/\D/g, ''), 10) || 10;
  const subjectId = String(subject || '').toLowerCase().replace(/[\s-]+/g, '_');
  const subData = storeState?.subjects?.[subjectId] || studentStore.getSubject(subjectId);

  // Load and enrich CAPS topics for this subject & grade
  const allTopics = useMemo(() => {
    const rawList = curriculumData[normalizedSubject]?.[String(numericGrade)]?.topics;
    
    if (Array.isArray(rawList) && rawList.length > 0) {
      return rawList.map((topicName, idx) => {
        const term = getTermForTopic(normalizedSubject, topicName, idx, rawList.length);
        return {
          name: topicName,
          term,
        };
      });
    }

    // Check fallback catalog
    const fallback = FALLBACK_CAPS_TOPICS[normalizedSubject]?.[numericGrade];
    if (fallback) {
      return fallback;
    }

    // Generic CAPS syllabus fallbacks
    return [
      { name: 'Core Foundations and Algebraic Concepts', term: 1 },
      { name: 'Analytical Relations and Core Methods', term: 2 },
      { name: 'Calculations, Applications and Mensuration', term: 3 },
      { name: 'Statistical Evaluation and Final Exam Prep', term: 4 },
    ];
  }, [normalizedSubject, numericGrade]);

  // Compute status badge for each topic
  const getTopicStatus = (topic) => {
    const mastery = subData?.formativeMastery ?? 0;
    const isTopicCurrent = currentTopic && currentTopic.toLowerCase() === topic.name.toLowerCase();

    if (isTopicCurrent) {
      if (mastery >= 80) {
        return { label: 'Exam Ready', color: 'bg-emerald-50 text-emerald-800 border-emerald-300', dot: 'bg-emerald-500' };
      }
      return { label: 'Practice Active', color: 'bg-blue-50 text-blue-800 border-blue-300', dot: 'bg-blue-500' };
    }

    if (subData?.status === 'diagnostic_required' || (mastery === 0 && (subData?.questionsAttempted || 0) === 0)) {
      return { label: 'Diagnostic Needed', color: 'bg-amber-50 text-amber-800 border-amber-300', dot: 'bg-amber-500' };
    }

    if (mastery >= 80) {
      return { label: 'Exam Ready', color: 'bg-emerald-50 text-emerald-800 border-emerald-300', dot: 'bg-emerald-500' };
    }

    if (topic.term < selectedTerm) {
      return { label: 'Exam Ready', color: 'bg-emerald-50 text-emerald-800 border-emerald-300', dot: 'bg-emerald-500' };
    }

    return { label: 'Practice Active', color: 'bg-blue-50 text-blue-800 border-blue-300', dot: 'bg-blue-500' };
  };

  // Filtered topics based on search query or term tab
  const filteredTopics = useMemo(() => {
    const query = searchQuery.trim().toLowerCase();
    if (query) {
      return allTopics.filter((t) => t.name.toLowerCase().includes(query));
    }
    return allTopics.filter((t) => t.term === selectedTerm);
  }, [allTopics, searchQuery, selectedTerm]);

  if (!isOpen) return null;

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-900/60 backdrop-blur-xs select-none animate-in fade-in duration-150"
      onClick={onClose}
    >
      <div 
        className="w-full max-w-2xl bg-white rounded-2xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col max-h-[90vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-[#13519C] text-white px-5 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-white/10 flex items-center justify-center border border-white/20">
              <BookOpen className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-[11px] font-bold uppercase tracking-wider text-blue-200 font-mono">
                  CAPS Curriculum Alignment
                </span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-white/20 text-white font-bold">
                  Grade {numericGrade}
                </span>
              </div>
              <h3 className="text-base sm:text-lg font-bold text-white mt-0.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
                {normalizedSubject} • Topic &amp; Exam Scope
              </h3>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition cursor-pointer"
            aria-label="Close Topic Scope Modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Selection & Search Bar */}
        <div className="p-4 bg-slate-50 border-b border-slate-200 space-y-3">
          {/* Consecutive Ordered Dropdown Selector */}
          <div>
            <label className="text-[11px] font-bold uppercase tracking-wider text-slate-500 mb-1 flex items-center justify-between">
              <span>Consecutive Syllabus Topics:</span>
              <span className="text-[10px] text-[#13519C] font-semibold">Term 1 → Term 4</span>
            </label>
            <select
              value={allTopics.some(t => t.name.toLowerCase() === (currentTopic || '').toLowerCase()) ? currentTopic : ''}
              onChange={(e) => {
                if (e.target.value) {
                  onSelectTopic(e.target.value);
                  onClose();
                }
              }}
              className="w-full px-3 py-2 rounded-xl bg-white border border-slate-300 text-slate-800 text-xs sm:text-sm font-semibold focus:outline-hidden focus:border-[#13519C] focus:ring-2 focus:ring-[#13519C]/15 transition font-sans cursor-pointer shadow-2xs"
            >
              <option value="" disabled>-- Select a topic from consecutive syllabus --</option>
              {[1, 2, 3, 4].map((termNum) => {
                const termTopics = allTopics.filter(t => t.term === termNum);
                if (termTopics.length === 0) return null;
                return (
                  <optgroup key={termNum} label={`Term ${termNum}`}>
                    {termTopics.map((t, idx) => (
                      <option key={`${t.name}-${idx}`} value={t.name}>
                        {`T${t.term}: ${t.name}`}
                      </option>
                    ))}
                  </optgroup>
                );
              })}
            </select>
          </div>

          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder='Or search topics by name (e.g. "Trig", "VAT", "Newton")...'
              className="w-full pl-9 pr-9 py-2 rounded-xl bg-white border border-slate-200 text-slate-800 placeholder:text-slate-400 text-xs sm:text-sm focus:outline-hidden focus:border-[#13519C] focus:ring-2 focus:ring-[#13519C]/15 transition font-sans"
            />
            {searchQuery && (
              <button
                type="button"
                onClick={() => setSearchQuery('')}
                className="w-5 h-5 rounded-full bg-slate-200 hover:bg-slate-300 text-slate-600 flex items-center justify-center absolute right-3 top-1/2 -translate-y-1/2 text-xs transition cursor-pointer"
                title="Clear search"
              >
                ✕
              </button>
            )}
          </div>

          {/* CAPS Term Selector Tabs (hidden during active search) */}
          {!searchQuery && (
            <div className="grid grid-cols-4 gap-1.5 mt-3 bg-slate-200/80 p-1 rounded-xl">
              {[
                { term: 1, label: 'Term 1', desc: 'Foundation' },
                { term: 2, label: 'Term 2', desc: 'Mid-Year' },
                { term: 3, label: 'Term 3', desc: 'Trial Scope' },
                { term: 4, label: 'Term 4', desc: 'Final Exam' },
              ].map((item) => {
                const isSelected = selectedTerm === item.term;
                return (
                  <button
                    key={item.term}
                    type="button"
                    onClick={() => setSelectedTerm(item.term)}
                    className={`px-2 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer text-center ${
                      isSelected
                        ? 'bg-white text-[#13519C] shadow-xs'
                        : 'text-slate-600 hover:text-slate-900 hover:bg-white/50'
                    }`}
                  >
                    <div className="font-extrabold">{item.label}</div>
                    <div className="text-[10px] opacity-75 font-normal truncate hidden sm:block">
                      {item.desc}
                    </div>
                  </button>
                );
              })}
            </div>
          )}
        </div>

        {/* Topics List Surface */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2.5 max-h-[420px]">
          {searchQuery && (
            <div className="text-xs text-slate-500 font-semibold mb-2 flex items-center justify-between">
              <span>Found {filteredTopics.length} topic{filteredTopics.length === 1 ? '' : 's'} matching "{searchQuery}"</span>
              <button
                type="button"
                onClick={() => setSearchQuery('')}
                className="text-[#13519C] hover:underline font-bold"
              >
                Show all Terms
              </button>
            </div>
          )}

          {filteredTopics.length === 0 ? (
            <div className="py-12 text-center text-slate-500 space-y-2">
              <Filter className="w-8 h-8 text-slate-300 mx-auto" />
              <p className="text-sm font-semibold text-slate-700">No CAPS topics found</p>
              <p className="text-xs text-slate-500">Try typing a different keyword or clear the search filter.</p>
            </div>
          ) : (
            filteredTopics.map((topic, index) => {
              const status = getTopicStatus(topic);
              const isCurrent = currentTopic && currentTopic.toLowerCase() === topic.name.toLowerCase();

              return (
                <div
                  key={`${topic.name}-${index}`}
                  onClick={() => {
                    onSelectTopic(topic.name);
                    onClose();
                  }}
                  className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between gap-3 group ${
                    isCurrent
                      ? 'bg-blue-50/70 border-[#13519C] shadow-xs ring-1 ring-[#13519C]'
                      : 'bg-white border-slate-200 hover:border-slate-300 hover:bg-slate-50'
                  }`}
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <span className="w-7 h-7 rounded-lg bg-slate-100 group-hover:bg-[#13519C]/10 text-slate-500 group-hover:text-[#13519C] flex items-center justify-center text-xs font-mono font-bold shrink-0 transition">
                      {topic.term ? `T${topic.term}` : '•'}
                    </span>
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="text-xs sm:text-sm font-bold text-slate-900 truncate">
                          {topic.name}
                        </span>
                        {isCurrent && (
                          <span className="text-[10px] px-2 py-0.5 rounded-full bg-[#13519C] text-white font-extrabold shrink-0">
                            Current Scope
                          </span>
                        )}
                      </div>
                      <div className="flex items-center gap-2 mt-0.5 text-[11px] text-slate-500">
                        <span>CAPS Term {topic.term}</span>
                        <span>•</span>
                        <span>Grade {numericGrade}</span>
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-2 shrink-0">
                    <span className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold border ${status.color}`}>
                      <span className={`w-1.5 h-1.5 rounded-full ${status.dot}`} />
                      <span>{status.label}</span>
                    </span>
                    <ChevronRight className="w-4 h-4 text-slate-300 group-hover:text-slate-600 group-hover:translate-x-0.5 transition" />
                  </div>
                </div>
              );
            })
          )}
        </div>

        {/* Footer Note */}
        <div className="bg-slate-50 px-5 py-3 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500">
          <div className="flex items-center gap-1.5">
            <GraduationCap className="w-4 h-4 text-[#13519C]" />
            <span>100% Aligned with South African Curriculum Standards (CAPS)</span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="px-3 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-100 text-slate-700 text-xs font-semibold transition cursor-pointer"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
}
