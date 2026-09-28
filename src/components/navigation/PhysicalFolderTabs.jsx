import React, { useRef, useEffect, useState, useCallback } from 'react';
import studentStore from '../../services/studentStore';
import { 
  ClipboardList, 
  Calculator, 
  BookOpen, 
  Briefcase, 
  FlaskConical, 
  Dna, 
  Cpu, 
  Coins, 
  Leaf,
  Pin,
  ChevronLeft,
  ChevronRight
} from 'lucide-react';

/**
 * PhysicalFolderTabs
 * Skeuo-modern folder tab navigation mimicking physical manila folders and hanging file tabs.
 * 
 * Invariants:
 * - Desktop: Left-slanted lip (clip-path chamfer on top-left shoulder), 3D forward pop (z-30, translateY(-4px)), 4px top accent stripe.
 * - Mobile: Horizontally scrollable carousel (overflow-x-auto scrollbar-none) with 44px minimum touch targets and auto-scroll to active.
 * - Color Palette: 60% crisp white canvas, 30% deep navy, 10% vivid jewel-tone accents.
 */
import { SUBJECT_TABS_CONFIG } from './subjectTabsConfig';


export default function PhysicalFolderTabs({
  activeTab = 'desk',
  onSelectTab = () => {},
  currentGrade = 10,
  mode = 'desktop', // 'desktop' | 'mobile'
}) {
  const activeTabRef = useRef(null);
  const desktopShelfRef = useRef(null);
  const [canScrollLeft, setCanScrollLeft] = useState(false);
  const [canScrollRight, setCanScrollRight] = useState(false);
  const numericGrade = parseInt(String(currentGrade).replace(/\D/g, ''), 10) || 10;
  const [storeState, setStoreState] = useState(() => studentStore.getState());

  const checkDesktopScroll = useCallback(() => {
    if (desktopShelfRef.current) {
      const { scrollLeft, scrollWidth, clientWidth } = desktopShelfRef.current;
      setCanScrollLeft(scrollLeft > 6);
      setCanScrollRight(scrollLeft < scrollWidth - clientWidth - 6);
    }
  }, []);

  const handleScrollLeft = () => {
    if (desktopShelfRef.current) {
      desktopShelfRef.current.scrollBy({ left: -220, behavior: 'smooth' });
    }
  };

  const handleScrollRight = () => {
    if (desktopShelfRef.current) {
      desktopShelfRef.current.scrollBy({ left: 220, behavior: 'smooth' });
    }
  };

  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const getDynamicBadge = (tab) => {
    if (tab.isDesk) {
      const dues = storeState?.deskDues ?? 0;
      return {
        text: dues > 0 ? `${dues} Due` : '0 Due',
        color: dues > 0 ? 'bg-rose-500 text-white shadow-sm shadow-rose-500/40' : 'bg-slate-200 text-slate-700'
      };
    }
    const sub = studentStore.getSubject(tab.id);
    if (!sub || sub.status === 'diagnostic_required') {
      return {
        text: 'Diag',
        color: 'bg-amber-100 text-amber-900 border border-amber-300'
      };
    }
    const val = sub.formativeMastery ?? 0;
    return {
      text: `${val}%`,
      color: val >= 80 ? 'bg-emerald-600 text-white shadow-sm shadow-emerald-500/40' :
             val >= 60 ? 'bg-blue-600 text-white shadow-sm shadow-blue-500/40' :
             'bg-slate-200 text-slate-700'
    };
  };

  // Filter tabs strictly by student grade (Today's Desk is always visible)
  const visibleTabs = SUBJECT_TABS_CONFIG.filter(
    (tab) => tab.isDesk || (tab.grades && tab.grades.includes(numericGrade))
  );

  // Auto-scroll the active tab into center view on mobile or desktop if needed
  useEffect(() => {
    if (mode === 'mobile' && activeTabRef.current) {
      activeTabRef.current.scrollIntoView({
        behavior: 'smooth',
        inline: 'center',
        block: 'nearest',
      });
    }
  }, [activeTab, mode]);

  // Monitor desktop shelf scrollability
  useEffect(() => {
    checkDesktopScroll();
    const shelf = desktopShelfRef.current;
    if (shelf) {
      shelf.addEventListener('scroll', checkDesktopScroll, { passive: true });
      window.addEventListener('resize', checkDesktopScroll);
      return () => {
        shelf.removeEventListener('scroll', checkDesktopScroll);
        window.removeEventListener('resize', checkDesktopScroll);
      };
    }
  }, [checkDesktopScroll, visibleTabs.length]);

  if (mode === 'mobile') {
    // ═══════════════════════════════════════════════════════════════════════════
    // MOBILE SWIPEABLE HORIZONTAL CAROUSEL (44px touch targets)
    // ═══════════════════════════════════════════════════════════════════════════
    return (
      <nav 
        className="w-full bg-white border-t border-slate-200 px-3 py-2 flex items-center gap-2.5 overflow-x-auto scrollbar-none shadow-lg z-30 select-none"
        aria-label="Mobile Subject Navigation"
      >
        {visibleTabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;

          return (
            <button
              key={tab.id}
              ref={isActive ? activeTabRef : null}
              type="button"
              onClick={() => onSelectTab(tab.id)}
              className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs transition-all duration-200 shrink-0 whitespace-nowrap min-h-[44px] cursor-pointer select-none font-bold ${
                isActive
                  ? 'bg-slate-100 text-slate-900 border-2 shadow-sm scale-102'
                  : 'bg-slate-50 text-slate-600 border border-slate-200 hover:text-slate-900'
              }`}
              style={{
                borderColor: isActive ? tab.accentColor : undefined,
                color: isActive ? tab.accentColor : undefined,
              }}
            >
              <span 
                className="w-2.5 h-2.5 rounded-full shrink-0"
                style={{ backgroundColor: tab.accentColor }}
              />
              <Icon className="w-4 h-4 shrink-0" />
              <span>{tab.shortName}</span>
              {(() => {
                const b = getDynamicBadge(tab);
                return (
                  <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-extrabold ${b.color}`}>
                    {b.text}
                  </span>
                );
              })()}
            </button>
          );
        })}
      </nav>
    );
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // DESKTOP PHYSICAL FOLDER TABS (Left-slanted lip & 3D forward pop)
  // ═══════════════════════════════════════════════════════════════════════════
  return (
    <div className="tab-shelf-container relative z-20 select-none bg-[#E6EDF5] border-b border-slate-300">
      {/* Scroll Left Button */}
      {canScrollLeft && (
        <button
          type="button"
          onClick={handleScrollLeft}
          className="absolute left-1.5 top-1/2 -translate-y-1/2 z-40 w-7 h-7 rounded-full bg-white/95 text-slate-700 shadow-md border border-slate-300 flex items-center justify-center hover:bg-white hover:text-slate-900 transition-all cursor-pointer backdrop-blur-xs"
          title="Scroll tabs left"
          aria-label="Scroll tabs left"
        >
          <ChevronLeft className="w-4 h-4" />
        </button>
      )}

      {/* Scroll Right Button */}
      {canScrollRight && (
        <button
          type="button"
          onClick={handleScrollRight}
          className="absolute right-1.5 top-1/2 -translate-y-1/2 z-40 w-7 h-7 rounded-full bg-white/95 text-slate-700 shadow-md border border-slate-300 flex items-center justify-center hover:bg-white hover:text-slate-900 transition-all cursor-pointer backdrop-blur-xs"
          title="Scroll tabs right"
          aria-label="Scroll tabs right"
        >
          <ChevronRight className="w-4 h-4" />
        </button>
      )}

      {/* Slidable Desktop Shelf */}
      <div 
        ref={desktopShelfRef}
        className="tab-shelf px-2 sm:px-6 pt-3.5 overflow-x-auto scrollbar-none scroll-smooth [&::-webkit-scrollbar]:hidden"
      >
        <div className="flex items-end gap-0 min-w-max -mb-[2px]">
          {visibleTabs.map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;

            return (
              <button
                key={tab.id}
                type="button"
                onClick={() => onSelectTab(tab.id)}
                title={`${tab.name} (Grade ${numericGrade})`}
                className={`folder-tab group shrink-0 min-w-[125px] max-w-[210px] px-3.5 py-3 flex items-center justify-center gap-2 text-xs font-bold transition-all cursor-pointer relative select-none ${
                  isActive ? 'active' : 'inactive'
                }`}
                style={{
                  clipPath: 'polygon(14px 0, 100% 0, 100% 100%, 0 100%, 0 14px)',
                  WebkitClipPath: 'polygon(14px 0, 100% 0, 100% 100%, 0 100%, 0 14px)',
                  zIndex: isActive ? 30 : 10,
                  transform: isActive ? 'translateY(-4px) scale(1.01)' : 'translateY(2px)',
                  backgroundColor: isActive ? '#FFFFFF' : '#E2E8F0',
                  color: isActive ? '#0F172A' : '#475569',
                  opacity: isActive ? 1 : 0.85,
                  borderBottom: isActive ? '2px solid #FFFFFF' : '1px solid #CBD5E1',
                  boxShadow: isActive 
                    ? '0 -8px 24px -4px rgba(0, 0, 0, 0.14), -4px -2px 10px rgba(0, 0, 0, 0.06), 4px -2px 10px rgba(0, 0, 0, 0.06)' 
                    : 'none',
                }}
              >
                {/* Continuous Slanted Color Border */}
                <svg className="absolute inset-0 w-full h-full pointer-events-none overflow-visible" preserveAspectRatio="none">
                  <path 
                    d="M 0 14 L 14 0 H 1000" 
                    stroke={tab.accentColor} 
                    strokeWidth={isActive ? 4 : 3} 
                    fill="none" 
                    vectorEffect="non-scaling-stroke" 
                  />
                </svg>

                {/* Status Color Dot */}
                <span 
                  className="w-2.5 h-2.5 rounded-full shrink-0 shadow-2xs"
                  style={{ backgroundColor: tab.accentColor }}
                />

                {/* Icon & Label */}
                <Icon className="w-3.5 h-3.5 shrink-0 hidden sm:inline" />
                <span className="tracking-tight truncate">{tab.shortName}</span>

                {/* Dynamic Badge */}
                {(() => {
                  const b = getDynamicBadge(tab);
                  return (
                    <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-extrabold shrink-0 ${b.color}`}>
                      {b.text}
                    </span>
                  );
                })()}
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
}
