import React, { useRef, useEffect } from 'react';
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
  Pin
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

export const SUBJECT_TABS_CONFIG = [
  {
    id: 'desk',
    name: "Today's Desk",
    shortName: 'Desk',
    icon: ClipboardList,
    accentColor: '#13519C',
    badge: '2 Due',
    badgeColor: 'bg-rose-500 text-white shadow-sm shadow-rose-500/40',
    grades: [7, 8, 9, 10, 11, 12],
    isDesk: true,
  },
  {
    id: 'accounting',
    name: 'Accounting',
    shortName: 'Accounting',
    icon: BookOpen,
    accentColor: '#059669',
    badge: '84%',
    badgeColor: 'bg-emerald-600 text-white shadow-sm shadow-emerald-500/40',
    grades: [10, 11, 12],
  },
  {
    id: 'mathematics',
    name: 'Mathematics',
    shortName: 'Maths',
    icon: Calculator,
    accentColor: '#2563EB',
    badge: '82%',
    badgeColor: 'bg-blue-600 text-white shadow-sm shadow-blue-500/40',
    grades: [7, 8, 9, 10, 11, 12],
  },
  {
    id: 'physical_sciences',
    name: 'Physical Sciences',
    shortName: 'Physics',
    icon: FlaskConical,
    accentColor: '#0891B2',
    badge: '68%',
    badgeColor: 'bg-cyan-600 text-white shadow-sm shadow-cyan-500/40',
    grades: [10, 11, 12],
  },
  {
    id: 'business_studies',
    name: 'Business Studies',
    shortName: 'Business',
    icon: Briefcase,
    accentColor: '#EA580C',
    badge: '75%',
    badgeColor: 'bg-[#FF9100] text-white shadow-sm shadow-orange-500/40',
    grades: [10, 11, 12],
  },
  {
    id: 'life_sciences',
    name: 'Life Sciences',
    shortName: 'Life Sci',
    icon: Dna,
    accentColor: '#0D9488',
    badge: '80%',
    badgeColor: 'bg-teal-600 text-white shadow-sm shadow-teal-500/40',
    grades: [10, 11, 12],
  },
  {
    id: 'technical_mathematics',
    name: 'Technical Mathematics',
    shortName: 'Tech Maths',
    icon: Cpu,
    accentColor: '#7C3AED',
    badge: '70%',
    badgeColor: 'bg-indigo-600 text-white shadow-sm shadow-indigo-500/40',
    grades: [10, 11, 12],
  },
  {
    id: 'ems',
    name: 'EMS',
    shortName: 'EMS',
    icon: Coins,
    accentColor: '#D97706',
    badge: '80%',
    badgeColor: 'bg-amber-600 text-white shadow-sm shadow-amber-500/40',
    grades: [7, 8, 9],
  },
  {
    id: 'natural_sciences',
    name: 'Natural Sciences',
    shortName: 'Nat Sci',
    icon: Leaf,
    accentColor: '#059669',
    badge: '75%',
    badgeColor: 'bg-emerald-600 text-white shadow-sm shadow-emerald-500/40',
    grades: [7, 8, 9],
  }
];

export default function PhysicalFolderTabs({
  activeTab = 'desk',
  onSelectTab = () => {},
  currentGrade = 10,
  mode = 'desktop', // 'desktop' | 'mobile'
}) {
  const activeTabRef = useRef(null);
  const numericGrade = parseInt(String(currentGrade).replace(/\D/g, ''), 10) || 10;

  // Filter tabs strictly by student grade (Today's Desk is always visible)
  const visibleTabs = SUBJECT_TABS_CONFIG.filter(
    (tab) => tab.isDesk || (tab.grades && tab.grades.includes(numericGrade))
  );

  // Auto-scroll the active tab into center view on mobile
  useEffect(() => {
    if (mode === 'mobile' && activeTabRef.current) {
      activeTabRef.current.scrollIntoView({
        behavior: 'smooth',
        inline: 'center',
        block: 'nearest',
      });
    }
  }, [activeTab, mode]);

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
              {tab.badge && (
                <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-extrabold ${tab.badgeColor}`}>
                  {tab.badge}
                </span>
              )}
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
    <div className="tab-shelf bg-[#E6EDF5] px-2 sm:px-6 pt-3.5 border-b border-slate-300 relative z-20 select-none overflow-x-auto lg:overflow-visible scrollbar-none [&::-webkit-scrollbar]:hidden">
      <div className="flex items-end gap-0 w-full -mb-[2px]">
        {visibleTabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;

          return (
            <button
              key={tab.id}
              type="button"
              onClick={() => onSelectTab(tab.id)}
              title={`${tab.name} (Grade ${numericGrade})`}
              className={`folder-tab group flex-1 min-w-[120px] max-w-[200px] px-3 py-3 flex items-center justify-center gap-2 text-xs font-bold transition-all cursor-pointer relative select-none ${
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
              {/* Top Accent Stripe */}
              <span 
                className="absolute top-0 left-0 right-0 h-[4px] transition-all"
                style={{ backgroundColor: tab.accentColor }}
              />

              {/* Status Color Dot */}
              <span 
                className="w-2.5 h-2.5 rounded-full shrink-0 shadow-2xs"
                style={{ backgroundColor: tab.accentColor }}
              />

              {/* Icon & Label */}
              <Icon className="w-3.5 h-3.5 shrink-0 hidden sm:inline" />
              <span className="tracking-tight truncate">{tab.shortName}</span>

              {/* Badge */}
              {tab.badge && (
                <span className={`text-[10px] px-1.5 py-0.5 rounded-full font-extrabold shrink-0 ${tab.badgeColor}`}>
                  {tab.badge}
                </span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
