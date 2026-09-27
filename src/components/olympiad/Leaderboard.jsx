import React, { useState } from 'react';
import { 
  Trophy, Medal, ShieldCheck, Filter, Globe, School, 
  Sparkles, Check, Eye, EyeOff, Award, ChevronDown, Flame
} from 'lucide-react';

/**
 * Leaderboard Component (Layer F — SAMO Olympiad Track)
 * The ONLY competitive ranking surface in the Fundile platform.
 * Strictly opt-in, preserving student psychological safety on standard CAPS syllabus.
 */
export default function Leaderboard({
  currentUser = { name: 'Thabo Ndlovu', grade: '10', school: 'Pretoria Boys High', province: 'Gauteng' },
  userScore = 85,
  userRank = 14,
  onBackToArena = () => {},
}) {
  const [isOptedIn, setIsOptedIn] = useState(true);
  const [selectedDivision, setSelectedDivision] = useState('all'); // 'all' | 'junior' | 'senior'
  const [selectedDomain, setSelectedDomain] = useState('all'); // 'all' | 'number_theory' | 'combinatorics' | 'geometry' | 'algebra'
  const [selectedProvince, setSelectedProvince] = useState('all');

  const LEADERBOARD_DATA = [
    { rank: 1, initials: 'SZ', name: 'Sipho Z.', school: 'Maritzburg College', province: 'KwaZulu-Natal', division: 'Senior', solved: 64, score: 98, tier: 'Top 1%' },
    { rank: 2, initials: 'LD', name: 'Lerato D.', school: 'Westerford High', province: 'Western Cape', division: 'Senior', solved: 59, score: 95, tier: 'Top 2%' },
    { rank: 3, initials: 'KM', name: 'Kagiso M.', school: 'St. Albans College', province: 'Gauteng', division: 'Junior', solved: 55, score: 92, tier: 'Top 3%' },
    { rank: 4, initials: 'AM', name: 'Andile M.', school: 'Hilton College', province: 'KwaZulu-Natal', division: 'Senior', solved: 51, score: 90, tier: 'Top 5%' },
    { rank: 5, initials: 'ZK', name: 'Zanele K.', school: 'Bishops Diocesan', province: 'Western Cape', division: 'Junior', solved: 48, score: 88, tier: 'Top 5%' },
    { rank: 6, initials: 'BN', name: 'Bongani N.', school: 'King Edward VII (KES)', province: 'Gauteng', division: 'Senior', solved: 46, score: 87, tier: 'Top 10%' },
    { rank: 7, initials: 'PM', name: 'Precious M.', school: 'Clarendon High', province: 'Eastern Cape', division: 'Junior', solved: 42, score: 86, tier: 'Top 10%' },
    { rank: 14, initials: 'TN', name: 'Thabo N. (You)', school: 'Pretoria Boys High', province: 'Gauteng', division: 'Senior', solved: 38, score: userScore, tier: 'Top 15%', isCurrentUser: true },
  ];

  const filteredData = LEADERBOARD_DATA.filter((entry) => {
    if (selectedDivision === 'junior' && entry.division !== 'Junior') return false;
    if (selectedDivision === 'senior' && entry.division !== 'Senior') return false;
    if (selectedProvince !== 'all' && entry.province !== selectedProvince) return false;
    return true;
  });

  return (
    <div className="w-full max-w-5xl mx-auto space-y-6 text-slate-100 animate-in fade-in duration-300">
      
      {/* 1. TOP BANNER & OPT-IN PRIVACY SHIELD */}
      <div className="bg-gradient-to-r from-amber-950/40 via-slate-900 to-indigo-950/40 border border-amber-500/30 rounded-2xl p-5 md:p-6 shadow-xl flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 rounded-xl bg-amber-500/20 border border-amber-400/40 flex items-center justify-center text-amber-400 shadow-inner">
            <Trophy className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl md:text-2xl font-bold text-white tracking-tight">SAMO National Leaderboard</h1>
              <span className="bg-amber-500/20 border border-amber-400/30 text-amber-300 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase">
                Competition Arena Only
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Opt-in non-routine mathematical rankings across South African independent &amp; public schools.
            </p>
          </div>
        </div>

        {/* Opt-in Toggle */}
        <div className="bg-slate-950/80 border border-slate-800 rounded-xl p-3 flex items-center gap-3 w-full md:w-auto justify-between">
          <div className="flex items-center gap-2 text-xs">
            {isOptedIn ? <Eye className="w-4 h-4 text-emerald-400" /> : <EyeOff className="w-4 h-4 text-slate-500" />}
            <span className={isOptedIn ? "text-slate-200 font-semibold" : "text-slate-500"}>
              {isOptedIn ? "Visible on Leaderboard" : "Private (Hidden)"}
            </span>
          </div>
          <button
            onClick={() => setIsOptedIn(!isOptedIn)}
            className={`px-3 py-1 rounded-lg text-xs font-bold transition-all ${
              isOptedIn 
                ? 'bg-emerald-950 border border-emerald-500/40 text-emerald-300 hover:bg-emerald-900' 
                : 'bg-slate-800 border border-slate-700 text-slate-300 hover:bg-slate-700'
            }`}
          >
            {isOptedIn ? "Opt Out" : "Opt In"}
          </button>
        </div>
      </div>

      {/* 2. NATIONAL PERCENTILE TIERS */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-slate-900/80 border border-amber-500/30 rounded-2xl p-4 flex items-center gap-3 shadow-lg">
          <div className="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-lg">
            🥇
          </div>
          <div>
            <div className="text-xs text-slate-400 font-semibold uppercase">Gold Distinction</div>
            <div className="text-base font-bold text-white">Top 5% National</div>
            <div className="text-[11px] text-amber-400">Score &ge; 90% (Round 1)</div>
          </div>
        </div>

        <div className="bg-slate-900/80 border border-slate-700/60 rounded-2xl p-4 flex items-center gap-3 shadow-lg">
          <div className="w-10 h-10 rounded-xl bg-slate-700/40 text-slate-300 flex items-center justify-center font-bold text-lg">
            🥈
          </div>
          <div>
            <div className="text-xs text-slate-400 font-semibold uppercase">Silver Distinction</div>
            <div className="text-base font-bold text-white">Top 15% National</div>
            <div className="text-[11px] text-sky-400">Score &ge; 75% (Round 1)</div>
          </div>
        </div>

        <div className="bg-slate-900/80 border border-amber-900/30 rounded-2xl p-4 flex items-center gap-3 shadow-lg">
          <div className="w-10 h-10 rounded-xl bg-amber-900/20 text-amber-600 flex items-center justify-center font-bold text-lg">
            🥉
          </div>
          <div>
            <div className="text-xs text-slate-400 font-semibold uppercase">Bronze Distinction</div>
            <div className="text-base font-bold text-white">Top 30% National</div>
            <div className="text-[11px] text-amber-600">Score &ge; 60% (Round 1)</div>
          </div>
        </div>
      </div>

      {/* 3. FILTERS BAR */}
      <div className="flex flex-wrap items-center justify-between gap-3 bg-slate-900/60 border border-slate-800 rounded-xl p-3">
        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs text-slate-400 font-semibold flex items-center gap-1 mr-1">
            <Filter className="w-3.5 h-3.5" /> Division:
          </span>
          {[
            { id: 'all', label: 'All Grades' },
            { id: 'junior', label: 'Junior (Gr 8–9)' },
            { id: 'senior', label: 'Senior (Gr 10–12)' },
          ].map((div) => (
            <button
              key={div.id}
              onClick={() => setSelectedDivision(div.id)}
              className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                selectedDivision === div.id
                  ? 'bg-amber-500/20 border border-amber-400/40 text-amber-300'
                  : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              {div.label}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-2">
          <span className="text-xs text-slate-400 font-semibold">Province:</span>
          <select
            value={selectedProvince}
            onChange={(e) => setSelectedProvince(e.target.value)}
            className="bg-slate-950 border border-slate-700 text-slate-200 text-xs rounded-lg px-2.5 py-1 focus:outline-none focus:border-amber-400"
          >
            <option value="all">All Provinces</option>
            <option value="Gauteng">Gauteng</option>
            <option value="Western Cape">Western Cape</option>
            <option value="KwaZulu-Natal">KwaZulu-Natal</option>
            <option value="Eastern Cape">Eastern Cape</option>
          </select>
        </div>
      </div>

      {/* 4. LEADERBOARD TABLE */}
      <div className="bg-slate-900/90 border border-slate-800 rounded-2xl shadow-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950/80 text-slate-400 uppercase tracking-wider text-[10px] border-b border-slate-800">
              <tr>
                <th className="py-3.5 px-4">Rank</th>
                <th className="py-3.5 px-4">Problem Solver</th>
                <th className="py-3.5 px-4">School &amp; Province</th>
                <th className="py-3.5 px-4">Division</th>
                <th className="py-3.5 px-4">Solved</th>
                <th className="py-3.5 px-4">Best Score</th>
                <th className="py-3.5 px-4 text-right">Standing</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {filteredData.map((row) => (
                <tr 
                  key={row.rank}
                  className={`transition-colors ${
                    row.isCurrentUser 
                      ? 'bg-amber-500/10 hover:bg-amber-500/15 border-l-4 border-l-amber-400 font-medium' 
                      : 'hover:bg-slate-800/30'
                  }`}
                >
                  <td className="py-3.5 px-4">
                    {row.rank === 1 && <span className="font-black text-amber-400 text-sm">🥇 #1</span>}
                    {row.rank === 2 && <span className="font-black text-slate-300 text-sm">🥈 #2</span>}
                    {row.rank === 3 && <span className="font-black text-amber-600 text-sm">🥉 #3</span>}
                    {row.rank > 3 && <span className="font-mono text-slate-400 font-bold">#{row.rank}</span>}
                  </td>
                  <td className="py-3.5 px-4">
                    <div className="flex items-center gap-2.5">
                      <div className="w-7 h-7 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-white text-xs">
                        {row.initials}
                      </div>
                      <span className={row.isCurrentUser ? "text-amber-300 font-bold" : "text-white font-semibold"}>
                        {row.name}
                      </span>
                    </div>
                  </td>
                  <td className="py-3.5 px-4">
                    <div className="text-slate-300">{row.school}</div>
                    <div className="text-[10px] text-slate-500">{row.province}</div>
                  </td>
                  <td className="py-3.5 px-4">
                    <span className="bg-slate-800 text-slate-300 text-[10px] font-semibold px-2 py-0.5 rounded">
                      {row.division}
                    </span>
                  </td>
                  <td className="py-3.5 px-4 font-mono font-semibold text-slate-200">
                    {row.solved}
                  </td>
                  <td className="py-3.5 px-4 font-mono font-bold text-amber-400">
                    {row.score}%
                  </td>
                  <td className="py-3.5 px-4 text-right">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      row.tier.includes('1%') || row.tier.includes('2%') || row.tier.includes('3%') || row.tier.includes('5%')
                        ? 'bg-amber-950 text-amber-300 border border-amber-800'
                        : 'bg-slate-800 text-slate-300 border border-slate-700'
                    }`}>
                      {row.tier}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
