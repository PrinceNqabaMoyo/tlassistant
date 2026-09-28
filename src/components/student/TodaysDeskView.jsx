import React, { useState, useEffect } from 'react';
import studentStore from '../../services/studentStore';
import { 
  ClipboardCheck, 
  Calendar, 
  Clock, 
  ArrowRight, 
  BookOpen, 
  Calculator, 
  Flame, 
  Zap, 
  WifiOff, 
  CheckCircle2, 
  TrendingUp,
  AlertCircle
} from 'lucide-react';

/**
 * TodaysDeskView
 * Action Dashboard rendered when the learner is on Tab 0 ("Today's Desk").
 * Eliminates redundant card drilling: learners immediately see teacher tasks,
 * autonomous quick-resumes, and diagnostic benchmarks.
 */

export default function TodaysDeskView({
  studentName = 'Nqobile Dlamini',
  grade = 10,
  schoolName = 'Westville High School',
  streakDays = 5,
  xp = 1420,
  onOpenSubject = () => {},
  onStartBenchmark = () => {},
}) {
  const [storeState, setStoreState] = useState(() => studentStore.getState());
  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const deskDues = storeState.deskDues ?? 0;
  const physSub = studentStore.getSubject('physical_sciences');
  const busSub = studentStore.getSubject('business_studies');
  const lifeSub = studentStore.getSubject('life_sciences');
  return (
    <div className="p-4 sm:p-8 bg-slate-50 min-h-[560px] space-y-6 animate-fadeIn font-sans">
      
      {/* 1. Welcome & Pacing Banner */}
      <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight font-display">
            Good afternoon, {studentName}. {deskDues > 0 ? `You have ${deskDues} assignments due this week.` : 'All assignments are up to date! Select a subject folder above for practice or diagnostic evaluation.'}
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 mt-1">
            Complete your scheduled classwork below, or click any subject folder above for autonomous practice.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs font-bold text-slate-700 bg-slate-100 px-3 py-1.5 rounded-xl border border-slate-200 flex items-center gap-1.5">
            <Calendar className="w-3.5 h-3.5 text-[#13519C]" />
            <span>Term 1 Benchmark Week</span>
          </span>
        </div>
      </div>

      {/* 2. Urgent Teacher Assignments Grid */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>
            <span>Teacher Assignments &amp; Classwork</span>
          </h3>
          <span className="text-xs text-rose-600 font-bold bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">
            Action Required
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          {/* Assignment 1: Accounting */}
          <div className="bg-white border-2 border-emerald-400 p-5 rounded-2xl shadow-xs hover:shadow-md transition-all space-y-3">
            <div className="flex items-center justify-between text-xs font-bold">
              <span className="bg-emerald-600 text-white px-2.5 py-1 rounded-full text-[11px] font-extrabold shadow-sm shadow-emerald-500/30 flex items-center gap-1.5">
                <BookOpen className="w-3.5 h-3.5" />
                <span>ACCOUNTING • DUE TODAY</span>
              </span>
              <span className="bg-rose-500 text-white px-2.5 py-0.5 rounded-full text-[11px] font-extrabold shadow-sm shadow-rose-500/30">
                17:00
              </span>
            </div>

            <div>
              <h4 className="text-base font-bold text-slate-900 font-display">
                General Journal: Debtors Allowance &amp; Bad Debts
              </h4>
              <p className="text-xs text-slate-600 mt-1">
                Assigned by Mrs. Khumalo • 12 Marks • Record credit note #402 and insolvent debtor final dividend.
              </p>
            </div>

            <div className="pt-2 flex items-center justify-between border-t border-slate-100">
              <span className="text-xs font-semibold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-md">
                Estimated: 15 mins
              </span>
              <button
                type="button"
                onClick={() => onOpenSubject('accounting', 'General Journal')}
                className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold rounded-xl shadow-sm shadow-emerald-600/30 flex items-center gap-1.5 transition cursor-pointer"
              >
                <span>Open in Accounting</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Assignment 2: Mathematics */}
          <div className="bg-white border-2 border-blue-400 p-5 rounded-2xl shadow-xs hover:shadow-md transition-all space-y-3">
            <div className="flex items-center justify-between text-xs font-bold">
              <span className="bg-blue-600 text-white px-2.5 py-1 rounded-full text-[11px] font-extrabold shadow-sm shadow-blue-500/30 flex items-center gap-1.5">
                <Calculator className="w-3.5 h-3.5" />
                <span>MATHEMATICS • DUE FRIDAY</span>
              </span>
              <span className="bg-amber-500 text-white px-2.5 py-0.5 rounded-full text-[11px] font-extrabold shadow-sm shadow-amber-500/30">
                08:00
              </span>
            </div>

            <div>
              <h4 className="text-base font-bold text-slate-900 font-display">
                Algebraic Trinomial Factorisation Drill
              </h4>
              <p className="text-xs text-slate-600 mt-1">
                Assigned by Mr. Botha • 10 Marks • Practice quadratic factor splitting with positive and negative constant terms.
              </p>
            </div>

            <div className="pt-2 flex items-center justify-between border-t border-slate-100">
              <span className="text-xs font-semibold text-blue-800 bg-blue-50 px-2 py-0.5 rounded-md">
                Estimated: 12 mins
              </span>
              <button
                type="button"
                onClick={() => onOpenSubject('mathematics', 'Algebraic Expressions')}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold rounded-xl shadow-sm shadow-blue-600/30 flex items-center gap-1.5 transition cursor-pointer"
              >
                <span>Open in Mathematics</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

        </div>
      </div>

      {/* 3. Autonomous Mastery & Quick Pickups */}
      <div>
        <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-2">
          <TrendingUp className="w-3.5 h-3.5 text-[#13519C]" />
          <span>Autonomous Practice &amp; Mastery Dials</span>
        </h3>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          
          <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-slate-800">Physical Sciences</span>
              <span className="text-cyan-700 bg-cyan-50 font-bold px-1.5 py-0.5 rounded text-[11px]">
                {physSub.status === 'diagnostic_required' ? 'Diagnostic Due' : `${physSub.formativeMastery}% BKT`}
              </span>
            </div>
            <p className="text-xs text-slate-600">Motion in 1D: Constant acceleration calculations.</p>
            <button
              type="button"
              onClick={() => onOpenSubject('physical_sciences', 'Motion in 1D')}
              className="w-full mt-2 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold rounded-lg transition cursor-pointer"
            >
              Resume Drill &rarr;
            </button>
          </div>

          <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-slate-800">Business Studies</span>
              <span className="text-amber-700 bg-amber-50 font-bold px-1.5 py-0.5 rounded text-[11px]">
                {busSub.status === 'diagnostic_required' ? 'Diagnostic Due' : `${busSub.formativeMastery}% BKT`}
              </span>
            </div>
            <p className="text-xs text-slate-600">Micro vs Market vs Macro Environments.</p>
            <button
              type="button"
              onClick={() => onOpenSubject('business_studies', 'Business Environments')}
              className="w-full mt-2 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold rounded-lg transition cursor-pointer"
            >
              Resume Drill &rarr;
            </button>
          </div>

          <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-slate-800">Life Sciences</span>
              <span className="text-teal-700 bg-teal-50 font-bold px-1.5 py-0.5 rounded text-[11px]">
                {lifeSub.status === 'diagnostic_required' ? 'Diagnostic Due' : `${lifeSub.formativeMastery}% BKT`}
              </span>
            </div>
            <p className="text-xs text-slate-600">Mitosis: Identifying cell division stages from diagrams.</p>
            <button
              type="button"
              onClick={() => onOpenSubject('life_sciences', 'Cell Division & Mitosis')}
              className="w-full mt-2 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold rounded-lg transition cursor-pointer"
            >
              Resume Drill &rarr;
            </button>
          </div>

        </div>
      </div>

      {/* 4. Offline WebAPK / PWA Health & Data Saver Card */}
      <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs flex flex-wrap items-center justify-between gap-3 text-xs">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center font-bold">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
          </div>
          <div>
            <span className="font-bold text-slate-800 block">Offline Cache Active (Service Worker Ready)</span>
            <span className="text-slate-500 text-[11px]">18 questions cached locally • Submissions sync automatically when reconnected</span>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-[11px] font-bold text-emerald-800 bg-emerald-50 px-2.5 py-1 rounded-lg border border-emerald-200">
            ⚡ Data Saver &lt; 2 MB
          </span>
        </div>
      </div>

    </div>
  );
}
