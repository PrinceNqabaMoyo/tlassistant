import React, { useState, useMemo } from 'react';
import { 
  Users, Search, X, Check, School, GraduationCap, 
  Briefcase, Heart, Shield, Sparkles, ArrowRight 
} from 'lucide-react';
import { searchPersonas, MOCK_SCHOOL_STUDENTS } from '../../data/mock/mockEnvironment';

export default function PersonaSwitcherModal({
  isOpen,
  onClose,
  currentUser,
  onSwitchPersona
}) {
  const [activeTab, setActiveTab] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');

  const filteredPersonas = useMemo(() => {
    return searchPersonas(searchQuery, activeTab);
  }, [searchQuery, activeTab]);

  if (!isOpen) return null;

  const handleSelect = (persona) => {
    if (onSwitchPersona) {
      onSwitchPersona(persona);
    }
    onClose();
  };

  const tabs = [
    { id: 'all', label: 'All Personas' },
    { id: 'school_students', label: `School Students (${MOCK_SCHOOL_STUDENTS.length})` },
    { id: 'independent_students', label: 'Independent (100)' },
    { id: 'teachers', label: 'Faculty & HODs (60)' },
    { id: 'parents', label: 'Parents (330)' },
    { id: 'school_admin', label: 'School Admin' }
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/70 backdrop-blur-xs p-4 animate-in fade-in duration-150">
      <div 
        className="w-full max-w-3xl bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col max-h-[90vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header Ribbon */}
        <div className="bg-gradient-to-r from-[#13519C] to-[#0d3669] text-white p-5 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white/10 backdrop-blur-md flex items-center justify-center border border-white/20">
              <Users className="w-5 h-5 text-[#FFD166]" />
            </div>
            <div>
              <h3 className="text-xl font-bold" style={{ fontFamily: 'Afacad, sans-serif' }}>
                Testing Persona Switcher &amp; Oversight Cockpit
              </h3>
              <p className="text-xs text-blue-100/90">
                Instantly sign in as any Westville High student, independent homeschooler, teacher, or parent.
              </p>
            </div>
          </div>
          <button 
            type="button" 
            onClick={onClose} 
            className="p-2 text-white/80 hover:text-white hover:bg-white/10 rounded-full transition cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Search & Tabs */}
        <div className="p-4 bg-slate-50 border-b border-slate-200 space-y-3">
          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
            <input 
              type="text"
              placeholder="Search by name, grade, subject, class code, or parent ID..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-10 pr-4 py-2 bg-white border border-slate-200 rounded-xl text-sm focus:outline-hidden focus:ring-2 focus:ring-[#13519C] focus:border-transparent transition"
              autoFocus
            />
            {searchQuery && (
              <button 
                type="button"
                onClick={() => setSearchQuery('')}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-slate-600"
              >
                Clear
              </button>
            )}
          </div>

          <div className="flex items-center gap-1.5 overflow-x-auto scrollbar-none pb-1">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                type="button"
                onClick={() => setActiveTab(tab.id)}
                className={`px-3 py-1.5 text-xs font-bold rounded-lg shrink-0 transition cursor-pointer ${
                  activeTab === tab.id
                    ? 'bg-[#13519C] text-white shadow-xs'
                    : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200/80'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>

        {/* Persona List */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2 divide-y divide-slate-100">
          {filteredPersonas.length === 0 ? (
            <div className="text-center py-12 text-slate-400">
              <Users className="w-10 h-10 mx-auto text-slate-300 mb-2" />
              <p className="text-sm font-semibold">No personas match your search query.</p>
              <p className="text-xs text-slate-400">Try clearing the search or switching categories.</p>
            </div>
          ) : (
            filteredPersonas.map((persona) => {
              const isCurrent = currentUser?.id === persona.id;

              let icon = <GraduationCap className="w-4 h-4 text-blue-600" />;
              let badgeBg = 'bg-blue-50 text-blue-800 border-blue-200';

              if (persona.type === 'independent_student') {
                icon = <Sparkles className="w-4 h-4 text-purple-600" />;
                badgeBg = 'bg-purple-50 text-purple-800 border-purple-200';
              } else if (persona.type === 'teacher') {
                icon = <Briefcase className="w-4 h-4 text-emerald-600" />;
                badgeBg = 'bg-emerald-50 text-emerald-800 border-emerald-200';
              } else if (persona.type === 'parent') {
                icon = <Heart className="w-4 h-4 text-rose-600" />;
                badgeBg = 'bg-rose-50 text-rose-800 border-rose-200';
              } else if (persona.type === 'school_admin') {
                icon = <Shield className="w-4 h-4 text-amber-600" />;
                badgeBg = 'bg-amber-50 text-amber-800 border-amber-200';
              }

              return (
                <div
                  key={persona.id}
                  onClick={() => handleSelect(persona)}
                  className={`p-3 rounded-2xl flex items-center justify-between gap-3 hover:bg-slate-50 transition cursor-pointer ${
                    isCurrent ? 'bg-blue-50/60 ring-2 ring-[#13519C]' : ''
                  }`}
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <div className="w-10 h-10 rounded-xl bg-slate-100 flex items-center justify-center shrink-0 border border-slate-200">
                      {icon}
                    </div>
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="text-sm font-bold text-slate-900 truncate">
                          {persona.name}
                        </span>
                        <span className={`px-2 py-0.5 text-[10px] font-extrabold rounded-md border ${badgeBg}`}>
                          {persona.badge}
                        </span>
                        {isCurrent && (
                          <span className="bg-[#13519C] text-white text-[9px] font-extrabold px-1.5 py-0.5 rounded-full flex items-center gap-0.5">
                            <Check className="w-2.5 h-2.5" /> Active
                          </span>
                        )}
                      </div>
                      <p className="text-xs text-slate-500 truncate mt-0.5">
                        {persona.subtitle}
                      </p>
                    </div>
                  </div>

                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      handleSelect(persona);
                    }}
                    className={`px-3 py-1.5 text-xs font-bold rounded-xl flex items-center gap-1 transition shrink-0 cursor-pointer ${
                      isCurrent
                        ? 'bg-slate-200 text-slate-700'
                        : 'bg-[#13519C] text-white hover:bg-[#0e3e78] shadow-xs'
                    }`}
                  >
                    <span>{isCurrent ? 'Active' : 'Sign In'}</span>
                    {!isCurrent && <ArrowRight className="w-3.5 h-3.5" />}
                  </button>
                </div>
              );
            })
          )}
        </div>

        {/* Footer info */}
        <div className="p-3 bg-slate-50 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500">
          <span>Showing {filteredPersonas.length} test personas</span>
          <span className="font-mono">Westville High (300) • Homeschool (100) • Faculty (60) • Parents (330)</span>
        </div>
      </div>
    </div>
  );
}
