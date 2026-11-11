import React, { useState } from 'react';
import {
  Landmark,
  Scale,
  TrendingUp,
  Layers,
  Sliders,
  DollarSign,
  PieChart,
  ArrowRight,
  ShieldCheck,
  Building,
  Users,
  Briefcase,
  CheckCircle2,
  AlertCircle,
} from 'lucide-react';

/**
 * CommerceAndAccountingAtlasAid — Dedicated Cognitive Sidecar Visual Aid for:
 * - Economic and Management Sciences (Grades 7–9)
 * - Accounting (Grades 10–12)
 * - Business Studies (Grades 10–12)
 *
 * Implements Rule 0d-14 & Diagram Doctrine:
 * - Dual-tab architecture:
 *   * Tab 1: Annotated Master Atlas (Accounting Cycle, T-Accounts Architecture & PESTLE Macro Environments)
 *   * Tab 2: Interactive Dynamic Exploration Lab (Accounting Equation A = O + L, SA VAT 15% Converter & Break-Even Chart)
 */
export default function CommerceAndAccountingAtlasAid() {
  const [activeTab, setActiveTab] = useState('atlas'); // 'atlas' | 'interactive'
  const [activeAtlasSection, setActiveAtlasSection] = useState('cycle'); // 'cycle' | 't_accounts' | 'environments'

  // Interactive Lab State:
  // 1. Accounting Equation: A = O + L
  const [assetVal, setAssetVal] = useState(150000);
  const [equityVal, setEquityVal] = useState(90000);
  const [liabVal, setLiabVal] = useState(60000);

  // 2. VAT 15% Calculator
  const [vatExcl, setVatExcl] = useState(1000);
  const vatRate = 0.15;
  const vatAmount = vatExcl * vatRate;
  const vatIncl = vatExcl * (1 + vatRate);

  // 3. Break-Even Analysis
  const [fixedCosts, setFixedCosts] = useState(25000);
  const [unitSellingPrice, setUnitSellingPrice] = useState(150);
  const [unitVariableCost, setUnitVariableCost] = useState(70);
  const [unitsSold, setUnitsSold] = useState(350);

  const contributionPerUnit = Math.max(1, unitSellingPrice - unitVariableCost);
  const breakEvenUnits = Math.ceil(fixedCosts / contributionPerUnit);
  const totalRevenue = unitsSold * unitSellingPrice;
  const totalCost = fixedCosts + unitsSold * unitVariableCost;
  const netProfitOrLoss = totalRevenue - totalCost;

  // Accounting equation balance test
  const equationBalanced = Math.abs(assetVal - (equityVal + liabVal)) < 1;

  return (
    <div data-testid="commerce-accounting-atlas-aid" className="flex flex-col h-full bg-slate-50 text-slate-800 font-sans">
      {/* Top Header */}
      <div className="p-4 bg-white border-b border-slate-200 shadow-2xs">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="p-2 bg-emerald-50 text-emerald-700 rounded-xl border border-emerald-200">
              <Landmark className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-sm font-bold text-slate-900 leading-tight">
                Commerce & Financial Accounting Atlas
              </h2>
              <p className="text-[11px] text-slate-500">
                Accounting Cycle, T-Accounts, Accounting Equation & Break-Even Models
              </p>
            </div>
          </div>
          {/* Dual Tab Switcher */}
          <div className="flex p-0.5 bg-slate-100 rounded-xl border border-slate-200 text-xs font-semibold">
            <button
              onClick={() => setActiveTab('atlas')}
              className={`px-3 py-1 rounded-lg transition-all ${
                activeTab === 'atlas' ? 'bg-white text-emerald-700 shadow-2xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <span className="flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5" /> Annotated Atlas
              </span>
            </button>
            <button
              onClick={() => setActiveTab('interactive')}
              className={`px-3 py-1 rounded-lg transition-all ${
                activeTab === 'interactive' ? 'bg-white text-emerald-700 shadow-2xs' : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <span className="flex items-center gap-1.5">
                <Sliders className="w-3.5 h-3.5" /> Interactive Lab
              </span>
            </button>
          </div>
        </div>
      </div>

      {/* Tab 1: Annotated Master Atlas */}
      {activeTab === 'atlas' && (
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {/* Sub-navigation pills */}
          <div className="flex gap-2">
            {[
              { id: 'cycle', label: '1. Accounting Cycle Flow' },
              { id: 't_accounts', label: '2. Ledger T-Account Architecture' },
              { id: 'environments', label: '3. Business Environments (PESTLE)' },
            ].map((sec) => (
              <button
                key={sec.id}
                onClick={() => setActiveAtlasSection(sec.id)}
                className={`text-xs px-3 py-1.5 rounded-lg border font-medium transition-all ${
                  activeAtlasSection === sec.id
                    ? 'bg-emerald-600 text-white border-emerald-600 shadow-2xs'
                    : 'bg-white text-slate-600 border-slate-200 hover:border-slate-300'
                }`}
              >
                {sec.label}
              </button>
            ))}
          </div>

          {/* Section: Accounting Cycle Flow */}
          {activeAtlasSection === 'cycle' && (
            <div className="space-y-4">
              <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <Layers className="w-4 h-4 text-emerald-600" /> Standard 8-Step Accounting Cycle
                </h3>
                <p className="text-xs text-slate-600 mb-4">
                  Every financial transaction moves systematically from authentic source document to final audited statements.
                </p>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-2">
                  {[
                    { step: '1', title: 'Transaction Occurs', desc: 'Commercial exchange between entities' },
                    { step: '2', title: 'Source Document', desc: 'Receipt, Invoice, Cheque Counterfoil, Deposit Slip' },
                    { step: '3', title: 'Subsidiary Journals', desc: 'CRJ, CPJ, DJ, DAJ, CJ, CAJ, General Journal' },
                    { step: '4', title: 'General Ledger', desc: 'Double-entry posting to debit/credit T-accounts' },
                    { step: '5', title: 'Trial Balance', desc: 'Verification of total debits = total credits' },
                    { step: '6', title: 'Adjustments', desc: 'Depreciation, Accruals, Prepayments, Bad Debts' },
                    { step: '7', title: 'Financial Statements', desc: 'Statement of Comprehensive Income, Financial Position' },
                    { step: '8', title: 'Closing Entries', desc: 'Transfer nominal accounts to Trading & P&L' },
                  ].map((s) => (
                    <div key={s.step} className="p-3 bg-slate-50 rounded-lg border border-slate-200">
                      <div className="flex items-center gap-2 mb-1">
                        <span className="w-5 h-5 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-bold flex items-center justify-center">
                          {s.step}
                        </span>
                        <h4 className="text-xs font-bold text-slate-900">{s.title}</h4>
                      </div>
                      <p className="text-[11px] text-slate-500 leading-snug">{s.desc}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* Section: T-Accounts Architecture */}
          {activeAtlasSection === 't_accounts' && (
            <div className="space-y-4">
              <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-1.5">
                  <Scale className="w-4 h-4 text-emerald-600" /> Double-Entry Rule Matrix (DEAD CLIC)
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Debit Normal Balances */}
                  <div className="p-4 bg-emerald-50/50 rounded-xl border border-emerald-200">
                    <h4 className="text-xs font-bold text-emerald-900 mb-2">Debit Increases (+) / Credit Decreases (-)</h4>
                    <ul className="text-xs text-slate-700 space-y-1.5">
                      <li className="flex items-start gap-1.5">
                        <span className="font-bold text-emerald-700">• Assets:</span> Vehicles, Equipment, Land & Buildings, Trading Stock, Debtors Control, Bank, Cash Float.
                      </li>
                      <li className="flex items-start gap-1.5">
                        <span className="font-bold text-emerald-700">• Expenses:</span> Salaries, Rent Expense, Water & Electricity, Stationery, Cost of Sales, Depreciation.
                      </li>
                      <li className="flex items-start gap-1.5">
                        <span className="font-bold text-emerald-700">• Drawings:</span> Withdrawals by owner decrease Owner's Equity (recorded on Debit side).
                      </li>
                    </ul>
                  </div>

                  {/* Credit Normal Balances */}
                  <div className="p-4 bg-blue-50/50 rounded-xl border border-blue-200">
                    <h4 className="text-xs font-bold text-blue-900 mb-2">Credit Increases (+) / Debit Decreases (-)</h4>
                    <ul className="text-xs text-slate-700 space-y-1.5">
                      <li className="flex items-start gap-1.5">
                        <span className="font-bold text-blue-700">• Liabilities:</span> Creditors Control, Bank Overdraft, Mortgage Bond, Long-Term Loans.
                      </li>
                      <li className="flex items-start gap-1.5">
                        <span className="font-bold text-blue-700">• Income:</span> Sales, Current Income, Rent Income, Interest Income, Commission Income.
                      </li>
                      <li className="flex items-start gap-1.5">
                        <span className="font-bold text-blue-700">• Capital:</span> Direct contribution by owner increases Owner's Equity (recorded on Credit side).
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Section: Business Environments */}
          {activeAtlasSection === 'environments' && (
            <div className="space-y-4">
              <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
                <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-1.5">
                  <Building className="w-4 h-4 text-emerald-600" /> Three Business Environments (Senior Phase EMS & Business Studies)
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                  <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                    <div className="flex items-center gap-2 mb-2">
                      <div className="p-1.5 bg-blue-100 text-blue-700 rounded-lg">
                        <Users className="w-4 h-4" />
                      </div>
                      <h4 className="text-xs font-bold text-slate-900">Micro Environment</h4>
                    </div>
                    <p className="text-[11px] text-slate-600 mb-2">Full Management Control</p>
                    <ul className="text-[11px] text-slate-500 space-y-1">
                      <li>• Mission & Objectives</li>
                      <li>• Business Functions (8 functions)</li>
                      <li>• Organizational Structure</li>
                      <li>• Resources & Employees</li>
                    </ul>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                    <div className="flex items-center gap-2 mb-2">
                      <div className="p-1.5 bg-amber-100 text-amber-700 rounded-lg">
                        <Briefcase className="w-4 h-4" />
                      </div>
                      <h4 className="text-xs font-bold text-slate-900">Market Environment</h4>
                    </div>
                    <p className="text-[11px] text-slate-600 mb-2">Partial Influence / No Control</p>
                    <ul className="text-[11px] text-slate-500 space-y-1">
                      <li>• Consumers / Target Market</li>
                      <li>• Suppliers & Supply Chain</li>
                      <li>• Competitors (Porters 5 Forces)</li>
                      <li>• Intermediaries & Regulators</li>
                    </ul>
                  </div>

                  <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                    <div className="flex items-center gap-2 mb-2">
                      <div className="p-1.5 bg-purple-100 text-purple-700 rounded-lg">
                        <Building className="w-4 h-4" />
                      </div>
                      <h4 className="text-xs font-bold text-slate-900">Macro Environment</h4>
                    </div>
                    <p className="text-[11px] text-slate-600 mb-2">Zero Control (PESTLE Analysis)</p>
                    <ul className="text-[11px] text-slate-500 space-y-1">
                      <li>• Political & Legal (B-BBEE, BCEA)</li>
                      <li>• Economic (Inflation, Repo Rate)</li>
                      <li>• Social (Demographics, HIV/AIDS)</li>
                      <li>• Technological & Environmental</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Tab 2: Interactive Dynamic Exploration Lab */}
      {activeTab === 'interactive' && (
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {/* Tool 1: Accounting Equation Lab */}
          <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
            <div className="flex items-center justify-between mb-3">
              <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                <Scale className="w-4 h-4 text-emerald-600" /> Interactive Accounting Equation: Assets = Owner's Equity + Liabilities
              </h3>
              {equationBalanced ? (
                <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Balanced
                </span>
              ) : (
                <span className="flex items-center gap-1 text-[11px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">
                  <AlertCircle className="w-3.5 h-3.5" /> Out of Balance (Diff: R {Math.abs(assetVal - (equityVal + liabVal)).toLocaleString()})
                </span>
              )}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <label className="text-[11px] font-bold text-slate-700 flex justify-between">
                  <span>Assets (A):</span>
                  <span className="text-emerald-700 font-mono">R {assetVal.toLocaleString()}</span>
                </label>
                <input
                  type="range"
                  min="10000"
                  max="500000"
                  step="5000"
                  value={assetVal}
                  onChange={(e) => setAssetVal(Number(e.target.value))}
                  className="w-full h-1.5 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-600 mt-2"
                />
              </div>

              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <label className="text-[11px] font-bold text-slate-700 flex justify-between">
                  <span>Owner's Equity (OE):</span>
                  <span className="text-blue-700 font-mono">R {equityVal.toLocaleString()}</span>
                </label>
                <input
                  type="range"
                  min="0"
                  max="500000"
                  step="5000"
                  value={equityVal}
                  onChange={(e) => setEquityVal(Number(e.target.value))}
                  className="w-full h-1.5 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-blue-600 mt-2"
                />
              </div>

              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <label className="text-[11px] font-bold text-slate-700 flex justify-between">
                  <span>Liabilities (L):</span>
                  <span className="text-purple-700 font-mono">R {liabVal.toLocaleString()}</span>
                </label>
                <input
                  type="range"
                  min="0"
                  max="500000"
                  step="5000"
                  value={liabVal}
                  onChange={(e) => setLiabVal(Number(e.target.value))}
                  className="w-full h-1.5 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-purple-600 mt-2"
                />
              </div>
            </div>

            <button
              onClick={() => {
                setEquityVal(Math.round(assetVal * 0.6));
                setLiabVal(Math.round(assetVal * 0.4));
              }}
              className="text-xs px-3 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg border border-slate-300 font-medium transition-all"
            >
              Auto-Rebalance (60% Equity / 40% Debt)
            </button>
          </div>

          {/* Tool 2: South African VAT 15% Converter */}
          <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
            <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-1.5">
              <DollarSign className="w-4 h-4 text-emerald-600" /> South African Standard VAT Calculator (15%)
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <label className="text-[11px] font-bold text-slate-600 block mb-1">Exclusive of VAT (100%)</label>
                <div className="flex items-center gap-1 text-sm font-mono font-bold text-slate-900">
                  <span>R</span>
                  <input
                    type="number"
                    value={vatExcl}
                    onChange={(e) => setVatExcl(Math.max(0, Number(e.target.value)))}
                    className="w-full p-1 bg-white border border-slate-300 rounded font-mono text-sm"
                  />
                </div>
              </div>

              <div className="p-3 bg-emerald-50 rounded-xl border border-emerald-200">
                <label className="text-[11px] font-bold text-emerald-800 block mb-1">Output / Input VAT (15%)</label>
                <div className="text-base font-mono font-bold text-emerald-700">
                  R {vatAmount.toFixed(2)}
                </div>
                <p className="text-[10px] text-emerald-600 mt-1">Excl × 0.15 or Incl × 15/115</p>
              </div>

              <div className="p-3 bg-blue-50 rounded-xl border border-blue-200">
                <label className="text-[11px] font-bold text-blue-800 block mb-1">Inclusive of VAT (115%)</label>
                <div className="text-base font-mono font-bold text-blue-700">
                  R {vatIncl.toFixed(2)}
                </div>
                <p className="text-[10px] text-blue-600 mt-1">Total invoice amount</p>
              </div>
            </div>
          </div>

          {/* Tool 3: Break-Even & Cost-Volume-Profit Live Model */}
          <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
            <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-3 flex items-center gap-1.5">
              <TrendingUp className="w-4 h-4 text-emerald-600" /> Break-Even & Cost-Volume-Profit Live Model
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-3 mb-4">
              <div>
                <label className="text-[11px] font-bold text-slate-600 block">Fixed Costs (FC):</label>
                <input
                  type="number"
                  value={fixedCosts}
                  onChange={(e) => setFixedCosts(Math.max(1000, Number(e.target.value)))}
                  className="w-full p-1 bg-slate-50 border border-slate-300 rounded text-xs font-mono mt-1"
                />
              </div>
              <div>
                <label className="text-[11px] font-bold text-slate-600 block">Selling Price/Unit (P):</label>
                <input
                  type="number"
                  value={unitSellingPrice}
                  onChange={(e) => setUnitSellingPrice(Math.max(1, Number(e.target.value)))}
                  className="w-full p-1 bg-slate-50 border border-slate-300 rounded text-xs font-mono mt-1"
                />
              </div>
              <div>
                <label className="text-[11px] font-bold text-slate-600 block">Variable Cost/Unit (VC):</label>
                <input
                  type="number"
                  value={unitVariableCost}
                  onChange={(e) => setUnitVariableCost(Math.max(0, Number(e.target.value)))}
                  className="w-full p-1 bg-slate-50 border border-slate-300 rounded text-xs font-mono mt-1"
                />
              </div>
              <div>
                <label className="text-[11px] font-bold text-slate-600 block">Actual Sales (Units):</label>
                <input
                  type="number"
                  value={unitsSold}
                  onChange={(e) => setUnitsSold(Math.max(0, Number(e.target.value)))}
                  className="w-full p-1 bg-slate-50 border border-slate-300 rounded text-xs font-mono mt-1"
                />
              </div>
            </div>

            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <span className="text-[11px] text-slate-500 block">Contribution per unit (P - VC):</span>
                <span className="text-sm font-bold font-mono text-slate-800">R {contributionPerUnit}</span>
              </div>
              <div>
                <span className="text-[11px] text-slate-500 block">Break-Even Point (FC ÷ CPU):</span>
                <span className="text-sm font-bold font-mono text-blue-700">{breakEvenUnits} units</span>
              </div>
              <div>
                <span className="text-[11px] text-slate-500 block">Net Profit / (Loss):</span>
                <span
                  className={`text-sm font-bold font-mono ${
                    netProfitOrLoss >= 0 ? 'text-emerald-700' : 'text-rose-600'
                  }`}
                >
                  R {netProfitOrLoss.toLocaleString()}
                </span>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
