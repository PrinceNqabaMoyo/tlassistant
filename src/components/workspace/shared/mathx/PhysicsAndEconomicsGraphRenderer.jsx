import React from 'react';
import SvgRichLabel, { cleanSvgText } from './SvgRichLabel';
import SourceDocumentSvg from './SourceDocumentSvg';

/**
 * Physics Graphs & EMS / Business Studies Vector Schematics (Milestone 13)
 * Supports:
 *  - motion_graph (x-t, v-t, a-t projectile / kinematics graph)
 *  - reaction_energy_profile (Exothermic / Endothermic ΔH potential energy diagram)
 *  - kc_equilibrium_graph / maxwell_boltzmann
 *  - supply_demand (EMS Market Equilibrium Supply & Demand curves)
 *  - circular_flow / organogram / porters_five_forces
 */

function MotionGraphSvg({ spec }) {
    const v0 = Number(spec.v0 ?? 19.6);
    const tApex = Number(spec.t_apex ?? 2.0);
    const tTotal = Number(spec.t_total ?? tApex * 2);
    const direction = spec.upward_positive !== false ? 'Upward (+)' : 'Downward (+)';

    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Kinematics Velocity–Time (v–t) Graph ({direction})
                </span>
                <span className="font-mono text-blue-700 font-semibold">
                    vᵢ = {v0} m·s⁻¹ | t(apex) = {tApex} s
                </span>
            </div>
            <svg viewBox="0 0 560 320" className="w-full h-auto block bg-white">
                {/* Axes */}
                <line x1="65" y1="160" x2="510" y2="160" stroke="#334155" strokeWidth="2" />
                <line x1="65" y1="30" x2="65" y2="290" stroke="#334155" strokeWidth="2" />
                <text x="518" y="164" fontSize="12" fontWeight="700" fill="#0f172a">t (s)</text>
                <SvgRichLabel x={55} y={24} textAnchor="end" fontSize={11.5} fontWeight="700" fill="#0f172a" text="v (m·s^{-1})" />

                {/* Shaded upward & downward displacement triangles */}
                <polygon points="65,160 65,45 270,160" fill="#dbeafe" fillOpacity="0.55" />
                <polygon points="270,160 475,275 475,160" fill="#fee2e2" fillOpacity="0.45" />

                {/* Velocity line */}
                <line x1="65" y1="45" x2="475" y2="275" stroke="#2563eb" strokeWidth="3" />
                <line x1="475" y1="160" x2="475" y2="275" stroke="#64748b" strokeWidth="1.6" strokeDasharray="5,4" />

                {/* Labels */}
                <circle cx="65" cy="45" r="4.5" fill="#1d4ed8" />
                <text x="56" y="49" textAnchor="end" fontSize="11" fontWeight="700" fill="#1d4ed8">+{v0}</text>

                <circle cx="270" cy="160" r="5" fill="#dc2626" />
                <text
                    x="282"
                    y="146"
                    textAnchor="start"
                    fontSize="11"
                    fontWeight="700"
                    fill="#dc2626"
                    style={{ paintOrder: 'stroke', stroke: '#ffffff', strokeWidth: '3.5px', strokeLinejoin: 'round' }}
                >
                    Apex ({tApex} s; 0)
                </text>

                <circle cx="475" cy="275" r="4.5" fill="#dc2626" />
                <text x="56" y="278" textAnchor="end" fontSize="11" fontWeight="700" fill="#dc2626">-{v0}</text>
                <text x="475" y="148" textAnchor="middle" fontSize="11" fontWeight="700" fill="#334155">
                    {tTotal} s
                </text>
                <SvgRichLabel x={145} y={135} textAnchor="middle" fontSize={10.5} fontWeight="700" fill="#1e3a8a" text="Area = Δy_{max}" />
            </svg>
        </div>
    );
}

function ReactionEnergyProfileSvg({ spec }) {
    const isExo = spec.reaction_type !== 'endothermic';
    const rE = isExo ? 165 : 225;
    const pE = isExo ? 245 : 145;
    const peakY = 55;

    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Potential Energy (Eₚ) Reaction Profile ({isExo ? 'Exothermic ΔH < 0' : 'Endothermic ΔH > 0'})
                </span>
            </div>
            <svg viewBox="0 0 560 320" className="w-full h-auto block bg-white">
                <line x1="65" y1="280" x2="515" y2="280" stroke="#334155" strokeWidth="2" />
                <line x1="65" y1="25" x2="65" y2="280" stroke="#334155" strokeWidth="2" />
                <text x="290" y="305" textAnchor="middle" fontSize="11.5" fontWeight="700" fill="#334155">
                    Reaction Coordinate (Progress of Reaction)
                </text>

                {/* Uncatalysed curve */}
                <path
                    d={`M 75 ${rE} L 165 ${rE} C 215 ${rE}, 235 ${peakY}, 275 ${peakY} C 315 ${peakY}, 345 ${pE}, 395 ${pE} L 490 ${pE}`}
                    fill="none"
                    stroke="#2563eb"
                    strokeWidth="3"
                />
                {/* Catalysed curve (dashed) */}
                <path
                    d={`M 165 ${rE} C 215 ${rE}, 235 ${peakY + 48}, 275 ${peakY + 48} C 315 ${peakY + 48}, 345 ${pE}, 395 ${pE}`}
                    fill="none"
                    stroke="#059669"
                    strokeWidth="2.2"
                    strokeDasharray="6,4"
                />

                {/* Reference dashed lines */}
                <line x1="65" y1={rE} x2="360" y2={rE} stroke="#94a3b8" strokeWidth="1.4" strokeDasharray="4,4" />
                <line x1="275" y1={peakY} x2="275" y2={rE} stroke="#dc2626" strokeWidth="1.8" />
                <g style={{ paintOrder: 'stroke', stroke: '#ffffff', strokeWidth: '4px', strokeLinejoin: 'round' }}>
                    <SvgRichLabel x={283} y={(peakY + rE) / 2 + 18} fontSize={11} fontWeight="700" fill="#dc2626" text="E_a (uncatalysed)" />
                </g>
                <text x="120" y={rE - 8} textAnchor="middle" fontSize="11" fontWeight="700" fill="#0f172a">Reactants</text>
                <text x="440" y={pE - 8} textAnchor="middle" fontSize="11" fontWeight="700" fill="#0f172a">Products</text>
                <text x="275" y={peakY - 10} textAnchor="middle" fontSize="11" fontWeight="700" fill="#1d4ed8">
                    Activated Complex
                </text>
            </svg>
        </div>
    );
}

function SupplyDemandSvg({ spec }) {
    const pEq = cleanSvgText(spec.equilibrium_price || 'R 45');
    const qEq = cleanSvgText(spec.equilibrium_qty || '300');

    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Market Supply & Demand Equilibrium
                </span>
                <span className="font-mono text-blue-700 font-semibold">
                    Equilibrium E({qEq} units; {pEq})
                </span>
            </div>
            <svg viewBox="0 0 560 320" className="w-full h-auto block bg-white">
                <line x1="70" y1="270" x2="500" y2="270" stroke="#334155" strokeWidth="2" />
                <line x1="70" y1="30" x2="70" y2="270" stroke="#334155" strokeWidth="2" />
                <text x="285" y="298" textAnchor="middle" fontSize="11.5" fontWeight="700" fill="#334155">
                    Quantity (Q)
                </text>
                <text x="58" y="34" textAnchor="end" fontSize="11.5" fontWeight="700" fill="#334155">
                    Price (P)
                </text>

                {/* Demand curve D */}
                <line x1="110" y1="55" x2="450" y2="245" stroke="#2563eb" strokeWidth="3" />
                <text x="462" y="248" fontSize="12.5" fontWeight="800" fill="#1d4ed8">D</text>

                {/* Supply curve S */}
                <line x1="110" y1="245" x2="450" y2="55" stroke="#059669" strokeWidth="3" />
                <text x="462" y="58" fontSize="12.5" fontWeight="800" fill="#047857">S</text>

                {/* Equilibrium E(280, 150) */}
                <line x1="70" y1="150" x2="280" y2="150" stroke="#dc2626" strokeWidth="1.8" strokeDasharray="5,4" />
                <line x1="280" y1="150" x2="280" y2="270" stroke="#dc2626" strokeWidth="1.8" strokeDasharray="5,4" />
                <circle cx="280" cy="150" r="6" fill="#dc2626" stroke="#ffffff" strokeWidth="2" />
                <text x="294" y="154" fontSize="12" fontWeight="700" fill="#dc2626">
                    E ({qEq}; {pEq})
                </text>
                <text x="62" y="154" textAnchor="end" fontSize="11" fontWeight="700" fill="#dc2626">{pEq}</text>
                <text x="280" y="286" textAnchor="middle" fontSize="11" fontWeight="700" fill="#dc2626">{qEq}</text>
            </svg>
        </div>
    );
}

function CircularFlowSvg({ spec }) {
    const title = spec.title || 'Two-Sector Economic Circular Flow (Households & Businesses)';
    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {title}
                </span>
                <span className="font-mono text-emerald-700 font-semibold">
                    Goods Market ⇄ Factor Market
                </span>
            </div>
            <svg viewBox="0 0 580 340" className="w-full h-auto block bg-white">
                <defs>
                    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
                    </marker>
                    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
                    </marker>
                    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
                    </marker>
                    <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#7c3aed" />
                    </marker>
                </defs>

                {/* Top Center: Goods & Services Market */}
                <rect x="180" y="20" width="220" height="42" rx="8" fill="#eff6ff" stroke="#3b82f6" strokeWidth="2" />
                <text x="290" y="45" textAnchor="middle" fontSize="12.5" fontWeight="700" fill="#1e40af">
                    Goods & Services Market
                </text>

                {/* Left: Households Box */}
                <rect x="25" y="125" width="150" height="85" rx="10" fill="#f8fafc" stroke="#475569" strokeWidth="2.5" />
                <text x="100" y="152" textAnchor="middle" fontSize="13.5" fontWeight="800" fill="#0f172a">
                    HOUSEHOLDS
                </text>
                <text x="100" y="172" textAnchor="middle" fontSize="10.5" fill="#475569">
                    • Consumers of goods
                </text>
                <text x="100" y="190" textAnchor="middle" fontSize="10.5" fill="#475569">
                    • Owners of factors
                </text>

                {/* Right: Businesses Box */}
                <rect x="405" y="125" width="150" height="85" rx="10" fill="#f8fafc" stroke="#475569" strokeWidth="2.5" />
                <text x="480" y="152" textAnchor="middle" fontSize="13.5" fontWeight="800" fill="#0f172a">
                    BUSINESSES
                </text>
                <text x="480" y="172" textAnchor="middle" fontSize="10.5" fill="#475569">
                    • Producers of goods
                </text>
                <text x="480" y="190" textAnchor="middle" fontSize="10.5" fill="#475569">
                    • Employers of labour
                </text>

                {/* Bottom Center: Factor Market */}
                <rect x="180" y="275" width="220" height="42" rx="8" fill="#f0fdf4" stroke="#10b981" strokeWidth="2" />
                <text x="290" y="300" textAnchor="middle" fontSize="12.5" fontWeight="700" fill="#065f46">
                    Factor Market (Labour, Land, Capital)
                </text>

                {/* Flows: Upper Loop (Goods Market) */}
                {/* Blue arrow: Goods flow from Market to Households */}
                <path d="M 230 62 L 110 62 L 110 120" fill="none" stroke="#2563eb" strokeWidth="2.2" markerEnd="url(#arrow-blue)" />
                <text x="160" y="80" textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#2563eb">
                    Flow of Goods & Services
                </text>

                {/* Amber arrow: Consumer spending from Households to Businesses */}
                <path d="M 125 125 L 125 40 L 175 40" fill="none" stroke="#d97706" strokeWidth="2.2" markerEnd="url(#arrow-amber)" />
                <path d="M 405 40 L 465 40 L 465 120" fill="none" stroke="#d97706" strokeWidth="2.2" markerEnd="url(#arrow-amber)" />
                <text x="435" y="80" textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#d97706">
                    Consumer Spending (Revenue)
                </text>

                {/* Flows: Lower Loop (Factor Market) */}
                {/* Purple arrow: Factors of production (labour) from Households to Market */}
                <path d="M 100 215 L 100 295 L 175 295" fill="none" stroke="#7c3aed" strokeWidth="2.2" markerEnd="url(#arrow-purple)" />
                <path d="M 405 295 L 470 295 L 470 215" fill="none" stroke="#7c3aed" strokeWidth="2.2" markerEnd="url(#arrow-purple)" />
                <text x="145" y="260" textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#7c3aed">
                    Factors (Labour, Skills)
                </text>

                {/* Green arrow: Factor remuneration (Wages, Salaries, Profits) */}
                <path d="M 455 210 L 455 275 L 405 275" fill="none" stroke="#059669" strokeWidth="2.2" markerEnd="url(#arrow-green)" />
                <path d="M 180 315 L 85 315 L 85 215" fill="none" stroke="#059669" strokeWidth="2.2" markerEnd="url(#arrow-green)" />
                <text x="435" y="260" textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#059669">
                    Income (Wages & Salaries)
                </text>
            </svg>
        </div>
    );
}

function ProductionChainSvg({ spec }) {
    const raw = spec.raw || 'Raw Natural Resource';
    const primary = spec.primary || 'Primary Extraction (Farming / Mining)';
    const secondary = spec.secondary || 'Secondary Processing (Manufacturing Factory)';
    const tertiary = spec.tertiary || 'Tertiary Distribution (Retail / Services)';
    const product = spec.product || 'Finished Consumer Good';

    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Sectors of Production: Supply Chain Flow
                </span>
                <span className="font-mono text-blue-700 font-semibold">
                    Primary → Secondary → Tertiary
                </span>
            </div>
            <svg viewBox="0 0 580 200" className="w-full h-auto block bg-white">
                <defs>
                    <marker id="arrow-chain" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7" />
                    </marker>
                </defs>

                {/* Primary Sector Box */}
                <rect x="20" y="35" width="150" height="110" rx="8" fill="#f0fdf4" stroke="#16a34a" strokeWidth="2" />
                <text x="95" y="60" textAnchor="middle" fontSize="12" fontWeight="800" fill="#15803d">
                    PRIMARY SECTOR
                </text>
                <text x="95" y="80" textAnchor="middle" fontSize="10" fill="#334155">
                    Extraction / Harvesting
                </text>
                <text x="95" y="105" textAnchor="middle" fontSize="10" fontWeight="700" fill="#0f172a">
                    {primary.slice(0, 24)}
                </text>
                <text x="95" y="125" textAnchor="middle" fontSize="9.5" fill="#15803d">
                    Input: {raw}
                </text>

                {/* Connecting Arrow 1 */}
                <line x1="172" y1="90" x2="210" y2="90" stroke="#0284c7" strokeWidth="2.5" markerEnd="url(#arrow-chain)" />

                {/* Secondary Sector Box */}
                <rect x="215" y="35" width="150" height="110" rx="8" fill="#eff6ff" stroke="#2563eb" strokeWidth="2" />
                <text x="290" y="60" textAnchor="middle" fontSize="12" fontWeight="800" fill="#1d4ed8">
                    SECONDARY SECTOR
                </text>
                <text x="290" y="80" textAnchor="middle" fontSize="10" fill="#334155">
                    Manufacturing & Processing
                </text>
                <text x="290" y="105" textAnchor="middle" fontSize="10" fontWeight="700" fill="#0f172a">
                    {secondary.slice(0, 24)}
                </text>
                <text x="290" y="125" textAnchor="middle" fontSize="9.5" fill="#1d4ed8">
                    Transforms: {raw}
                </text>

                {/* Connecting Arrow 2 */}
                <line x1="367" y1="90" x2="405" y2="90" stroke="#0284c7" strokeWidth="2.5" markerEnd="url(#arrow-chain)" />

                {/* Tertiary Sector Box */}
                <rect x="410" y="35" width="150" height="110" rx="8" fill="#faf5ff" stroke="#9333ea" strokeWidth="2" />
                <text x="485" y="60" textAnchor="middle" fontSize="12" fontWeight="800" fill="#7e22ce">
                    TERTIARY SECTOR
                </text>
                <text x="485" y="80" textAnchor="middle" fontSize="10" fill="#334155">
                    Retail & Final Services
                </text>
                <text x="485" y="105" textAnchor="middle" fontSize="10" fontWeight="700" fill="#0f172a">
                    {tertiary.slice(0, 24)}
                </text>
                <text x="485" y="125" textAnchor="middle" fontSize="9.5" fill="#7e22ce">
                    Final: {product.slice(0, 22)}
                </text>

                {/* Bottom caption */}
                <text x="290" y="175" textAnchor="middle" fontSize="11" fontWeight="700" fill="#475569">
                    Goods Flow: Raw Materials → Industrial Processing → Consumer Purchase
                </text>
            </svg>
        </div>
    );
}

function PromissoryNoteSvg({ spec }) {
    const amount = spec.amount || '100';
    const merchant = spec.merchant || 'A. Khumalo';
    const city = spec.city || 'Cape Town';
    const date = spec.date || '14 March 1785';

    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-amber-200 bg-amber-50/40 shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-amber-100/60 border-b border-amber-200 text-xs">
                <span className="font-semibold text-amber-900 uppercase tracking-wider font-serif">
                    Historical Promissory Note & Deposit Receipt (Source Document)
                </span>
                <span className="font-mono text-amber-800 font-bold">
                    Value: {amount} Gold Guilders / Coins
                </span>
            </div>
            <div className="p-4 flex justify-center">
                <svg viewBox="0 0 540 230" className="w-full max-w-xl h-auto block bg-[#fefce8] border-4 border-double border-amber-800/60 rounded-lg shadow-inner">
                    {/* Security corner decorative marks */}
                    <rect x="8" y="8" width="12" height="12" fill="none" stroke="#92400e" strokeWidth="1.5" />
                    <rect x="520" y="8" width="12" height="12" fill="none" stroke="#92400e" strokeWidth="1.5" />
                    <rect x="8" y="210" width="12" height="12" fill="none" stroke="#92400e" strokeWidth="1.5" />
                    <rect x="520" y="210" width="12" height="12" fill="none" stroke="#92400e" strokeWidth="1.5" />

                    {/* Header */}
                    <text x="270" y="38" textAnchor="middle" fontSize="15" fontWeight="900" fontFamily="serif" fill="#78350f" letterSpacing="1.5">
                        GOLDSMITH PROMISSORY RECEIPT
                    </text>
                    <line x1="140" y1="46" x2="400" y2="46" stroke="#92400e" strokeWidth="1.2" />

                    {/* Date and Location */}
                    <text x="40" y="70" fontSize="11" fontFamily="serif" fill="#78350f">
                        Location: <tspan fontWeight="700">{city}</tspan>
                    </text>
                    <text x="420" y="70" textAnchor="end" fontSize="11" fontFamily="serif" fill="#78350f">
                        Date: <tspan fontWeight="700">{date}</tspan>
                    </text>

                    {/* Body Text */}
                    <text x="40" y="105" fontSize="12" fontFamily="serif" fill="#451a03">
                        I, the undersigned Master Goldsmith &amp; Bailee, acknowledge receipt of:
                    </text>
                    <text x="40" y="132" fontSize="13.5" fontWeight="800" fontFamily="serif" fill="#78350f">
                        {amount} Gold Coins of Standard Weight and Assay
                    </text>
                    <text x="40" y="160" fontSize="11.5" fontFamily="serif" fill="#451a03">
                        deposited by <tspan fontWeight="700">{merchant}</tspan>. I PROMISE TO PAY the Bearer hereof
                    </text>
                    <text x="40" y="180" fontSize="11.5" fontFamily="serif" fill="#451a03">
                        the full sum of {amount} Gold Coins upon presentation and demand.
                    </text>

                    {/* Signature Seal */}
                    <circle cx="450" cy="170" r="28" fill="#fde68a" stroke="#b45309" strokeWidth="1.8" strokeDasharray="3,2" />
                    <text x="450" y="166" textAnchor="middle" fontSize="9" fontWeight="800" fontFamily="serif" fill="#78350f">
                        GOLDSMITH
                    </text>
                    <text x="450" y="178" textAnchor="middle" fontSize="8" fontWeight="700" fontFamily="serif" fill="#92400e">
                        OFFICIAL SEAL
                    </text>

                    <line x1="330" y1="202" x2="500" y2="202" stroke="#78350f" strokeWidth="1" />
                    <text x="415" y="216" textAnchor="middle" fontSize="9.5" fontStyle="italic" fontFamily="serif" fill="#78350f">
                        Authorised Goldsmith Signatory
                    </text>
                </svg>
            </div>
        </div>
    );
}


function SankeyEnergySvg({ spec }) {
    const inputJ = Number(spec.input_j ?? 100);
    const usefulJ = Number(spec.useful_j ?? 20);
    const wastedJ = Number(spec.wasted_j ?? (inputJ - usefulJ));
    const appliance = spec.appliance || 'Appliance';
    const usefulName = spec.useful_name || 'Useful Energy';
    const wastedName = spec.wasted_name || 'Wasted Heat Energy';

    const usefulPct = Math.round((usefulJ / inputJ) * 100);
    const wastedPct = 100 - usefulPct;

    // Strict invariant: usefulWidth + wastedWidth strictly equals totalWidth
    const totalWidth = 90;
    const usefulWidth = Math.max(16, Math.min(74, Math.round(totalWidth * (usefulJ / inputJ))));
    const wastedWidth = totalWidth - usefulWidth;

    return (
        <div data-testid="sankey-energy-svg" className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2">
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Sankey Diagram — Energy Conservation & Efficiency
                </span>
                <span className="font-mono text-emerald-700 font-bold">
                    Efficiency: {usefulPct}% | Loss: {wastedPct}%
                </span>
            </div>
            <div className="p-4 flex flex-col items-center">
                <svg viewBox="0 0 540 280" className="w-full max-w-[540px] h-auto block bg-white">
                    <defs>
                        <linearGradient id="sankeyInput" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stopColor="#3b82f6" />
                            <stop offset="100%" stopColor="#2563eb" />
                        </linearGradient>
                        <linearGradient id="sankeyUseful" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stopColor="#10b981" />
                            <stop offset="100%" stopColor="#059669" />
                        </linearGradient>
                        <linearGradient id="sankeyWasted" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" stopColor="#f59e0b" />
                            <stop offset="100%" stopColor="#dc2626" />
                        </linearGradient>
                    </defs>

                    {/* Input Trunk */}
                    <rect x="30" y={130 - totalWidth / 2} width="160" height={totalWidth} rx="6" fill="url(#sankeyInput)" />
                    <text x="110" y="125" textAnchor="middle" fontSize="13" fontWeight="bold" fill="#ffffff">
                        Input: {inputJ} J
                    </text>
                    <text x="110" y="143" textAnchor="middle" fontSize="10.5" fill="#dbeafe">
                        (100% Total Energy)
                    </text>

                    {/* Useful Horizontal Stream */}
                    <path
                        d={`M 190 ${130 - totalWidth / 2} L 390 ${130 - totalWidth / 2} L 390 ${130 - totalWidth / 2 - 10} L 450 ${130 - totalWidth / 2 + usefulWidth / 2} L 390 ${130 - totalWidth / 2 + usefulWidth + 10} L 390 ${130 - totalWidth / 2 + usefulWidth} L 190 ${130 - totalWidth / 2 + usefulWidth} Z`}
                        fill="url(#sankeyUseful)"
                    />
                    <text x="310" y={130 - totalWidth / 2 + usefulWidth / 2 - 2} textAnchor="middle" fontSize="12" fontWeight="bold" fill="#ffffff">
                        {usefulJ} J ({usefulPct}%)
                    </text>
                    <text x="310" y={130 - totalWidth / 2 + usefulWidth / 2 + 14} textAnchor="middle" fontSize="10" fill="#d1fae5">
                        {usefulName}
                    </text>

                    {/* Wasted Downward Stream */}
                    <path
                        d={`M 190 ${130 - totalWidth / 2 + usefulWidth} Q 250 ${130 - totalWidth / 2 + usefulWidth} 260 190 L 245 190 L 260 + wastedWidth/2 245 L 275 + wastedWidth 190 L 260 + wastedWidth 190 Q 250 + wastedWidth ${130 + totalWidth / 2} 190 ${130 + totalWidth / 2} Z`}
                        fill="url(#sankeyWasted)"
                    />
                    <rect x="215" y="200" width="130" height="48" rx="6" fill="url(#sankeyWasted)" />
                    <text x="280" y="220" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#ffffff">
                        Wasted: {wastedJ} J ({wastedPct}%)
                    </text>
                    <text x="280" y="236" textAnchor="middle" fontSize="10" fill="#fef3c7">
                        {wastedName}
                    </text>

                    {/* Input Label on top */}
                    <text x="110" y="70" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#1e40af">
                        {appliance} Energy In
                    </text>
                </svg>
                <p className="mt-2 text-xs text-slate-500 text-center font-mono">
                    Conservation Law: Total Input ({inputJ} J) = Useful ({usefulJ} J) + Wasted ({wastedJ} J)
                </p>
            </div>
        </div>
    );
}

function GridPaperSvg({ spec }) {
    const length = Number(spec.length ?? 6);
    const width = Number(spec.width ?? 4);
    const unit = spec.unit || 'cm';
    const caption = spec.caption || `Rectangle on 1 ${unit} × 1 ${unit} grid (${length} × ${width})`;

    const cols = Math.max(10, length + 4);
    const rows = Math.max(8, width + 4);
    const cellSize = 22;
    const padX = 35;
    const padY = 35;
    const totalW = cols * cellSize + padX * 2;
    const totalH = rows * cellSize + padY * 2;

    const startC = Math.floor((cols - length) / 2);
    const startR = Math.floor((rows - width) / 2);
    const rectX = padX + startC * cellSize;
    const rectY = padY + startR * cellSize;
    const rectW = length * cellSize;
    const rectH = width * cellSize;

    return (
        <div data-testid="grid-paper-svg" className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2">
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Grid Paper (1 {unit} × 1 {unit} Square Grid)
                </span>
                <span className="font-mono text-blue-700 font-bold">
                    P = {2 * (length + width)} {unit} | A = {length * width} {unit}²
                </span>
            </div>
            <div className="p-3 flex flex-col items-center">
                <svg viewBox={`0 0 ${totalW} ${totalH}`} className="w-full max-w-[480px] h-auto block bg-white">
                    {/* Grid lines */}
                    {Array.from({ length: cols + 1 }).map((_, c) => (
                        <line key={`c-${c}`} x1={padX + c * cellSize} y1={padY} x2={padX + c * cellSize} y2={padY + rows * cellSize} stroke="#e2e8f0" strokeWidth="1" />
                    ))}
                    {Array.from({ length: rows + 1 }).map((_, r) => (
                        <line key={`r-${r}`} x1={padX} y1={padY + r * cellSize} x2={padX + cols * cellSize} y2={padY + r * cellSize} stroke="#e2e8f0" strokeWidth="1" />
                    ))}

                    {/* Highlighted Rectangle */}
                    <rect x={rectX} y={rectY} width={rectW} height={rectH} fill="#bfdbfe" fillOpacity="0.65" stroke="#2563eb" strokeWidth="2.5" />

                    {/* Dimension callouts */}
                    <text x={rectX + rectW / 2} y={rectY - 8} textAnchor="middle" fontSize="12" fontWeight="bold" fill="#1e3a8a">
                        {length} {unit} ({length} squares)
                    </text>
                    <text x={rectX + rectW + 10} y={rectY + rectH / 2 + 4} textAnchor="start" fontSize="12" fontWeight="bold" fill="#1e3a8a">
                        {width} {unit}
                    </text>
                </svg>
                {caption && <p className="mt-2 text-xs text-slate-500 text-center">{caption}</p>}
            </div>
        </div>
    );
}

function ProcessFlowSvg({ spec }) {
    const steps = Array.isArray(spec.steps) && spec.steps.length > 0
        ? spec.steps
        : ['Step 1: Input', 'Step 2: Transformation', 'Step 3: Output'];
    const title = spec.title || 'System Process & Relational Diagram';
    const W = 560;
    const H = 155;
    const n = Math.min(6, steps.length);
    const boxW = Math.min(125, Math.floor((W - 50 - (n - 1) * 18) / n));

    return (
        <div
            data-testid="geogebra-physics-econ-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">{title}</span>
                <span className="font-mono text-indigo-700 font-semibold">{n}-Stage Schematic</span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                <defs>
                    <marker id="proc-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
                    </marker>
                </defs>
                {steps.slice(0, n).map((st, idx) => {
                    const x = 25 + idx * (boxW + 18);
                    const y = 38;
                    const label = typeof st === 'string' ? st : (st.label || st.title || `Stage ${idx + 1}`);
                    return (
                        <g key={idx}>
                            <rect x={x} y={y} width={boxW} height={74} rx="8" fill="#eff6ff" stroke="#3b82f6" strokeWidth="1.8" />
                            <text x={x + boxW / 2} y={y + 24} textAnchor="middle" fontSize="10" fontWeight="800" fill="#1d4ed8">
                                STAGE {idx + 1}
                            </text>
                            <text x={x + boxW / 2} y={y + 46} textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#0f172a">
                                {String(label).slice(0, 18)}
                            </text>
                            {String(label).length > 18 && (
                                <text x={x + boxW / 2} y={y + 61} textAnchor="middle" fontSize="9.5" fontWeight="600" fill="#475569">
                                    {String(label).slice(18, 36)}
                                </text>
                            )}
                            {idx < n - 1 && (
                                <line
                                    x1={x + boxW + 2}
                                    y1={y + 37}
                                    x2={x + boxW + 16}
                                    y2={y + 37}
                                    stroke="#2563eb"
                                    strokeWidth="2"
                                    markerEnd="url(#proc-arrow)"
                                />
                            )}
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function MicrographScaleSvg({ spec }) {
    const title = spec.title || 'Microscopic Slide & Scale Bar';
    const mag = spec.magnification || '400×';
    const specimen = spec.specimen || 'Cell Specimen';
    const scaleBar = spec.scale_bar_label || 'Image Width = 30 mm';

    return (
        <div
            data-testid="geogebra-micrograph-scale-view"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Light Microscopy • {specimen}
                </span>
                <span className="font-mono text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                    Magnification: {mag}
                </span>
            </div>
            <svg viewBox="0 0 560 300" className="w-full h-auto block bg-white">
                <circle cx="280" cy="140" r="115" fill="#f8fafc" stroke="#cbd5e1" strokeWidth="3" />
                <circle cx="280" cy="140" r="113" fill="none" stroke="#e2e8f0" strokeWidth="1.5" />
                <path
                    d="M 215 140 C 215 100, 245 85, 290 88 C 335 91, 355 115, 350 155 C 345 190, 310 200, 265 195 C 225 190, 215 170, 215 140 Z"
                    fill="#fef3c7"
                    fillOpacity="0.45"
                    stroke="#d97706"
                    strokeWidth="2.5"
                />
                <ellipse cx="295" cy="145" rx="22" ry="19" fill="#bbf7d0" fillOpacity="0.75" stroke="#16a34a" strokeWidth="2" />
                <circle cx="297" cy="143" r="5" fill="#15803d" />
                <circle cx="250" cy="130" r="2" fill="#d97706" fillOpacity="0.6" />
                <circle cx="270" cy="165" r="2" fill="#d97706" fillOpacity="0.6" />
                <circle cx="330" cy="135" r="2" fill="#d97706" fillOpacity="0.6" />
                <circle cx="240" cy="155" r="1.5" fill="#d97706" fillOpacity="0.6" />
                <line x1="220" y1="110" x2="160" y2="85" stroke="#64748b" strokeWidth="1.2" />
                <text x="155" y="82" textAnchor="end" fontSize="11" fontWeight="600" fill="#334155">Cell Membrane</text>
                <line x1="315" y1="145" x2="400" y2="120" stroke="#64748b" strokeWidth="1.2" />
                <text x="405" y="123" textAnchor="start" fontSize="11" fontWeight="600" fill="#334155">Nucleus (Dark Staining)</text>
                <line x1="260" y1="175" x2="200" y2="215" stroke="#64748b" strokeWidth="1.2" />
                <text x="195" y="225" textAnchor="end" fontSize="11" fontWeight="600" fill="#334155">Cytoplasm</text>
                <g transform="translate(180, 262)">
                    <rect x="0" y="0" width="200" height="24" rx="4" fill="#f1f5f9" stroke="#94a3b8" strokeWidth="1" />
                    <line x1="20" y1="12" x2="180" y2="12" stroke="#0f172a" strokeWidth="2" />
                    <line x1="20" y1="6" x2="20" y2="18" stroke="#0f172a" strokeWidth="2" />
                    <line x1="180" y1="6" x2="180" y2="18" stroke="#0f172a" strokeWidth="2" />
                    <text x="100" y="10" textAnchor="middle" fontSize="10.5" fontWeight="800" fill="#0f172a">
                        {scaleBar}
                    </text>
                </g>
            </svg>
        </div>
    );
}

function OrganicStructureSvg({ spec }) {
    const title = spec.title || 'Organic Molecular Structures';
    const nameA = spec.name || 'Compound A';
    const nameB = spec.name_b || 'Compound B';
    const formula = spec.formula || 'C4H10O';
    const isomerType = spec.isomer_type || 'Structural Isomers';

    return (
        <div
            data-testid="geogebra-organic-structure"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {title}
                </span>
                <span className="font-mono text-indigo-700 font-bold bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">
                    Formula: {formula}
                </span>
            </div>
            <svg viewBox="0 0 560 220" className="w-full h-auto block bg-white">
                <rect x="30" y="25" width="235" height="155" rx="8" fill="#f8fafc" stroke="#3b82f6" strokeWidth="1.8" />
                <rect x="30" y="25" width="235" height="32" rx="8" fill="#eff6ff" />
                <text x="147" y="46" textAnchor="middle" fontSize="12" fontWeight="800" fill="#1d4ed8">
                    COMPOUND A
                </text>
                <text x="147" y="85" textAnchor="middle" fontSize="13" fontWeight="700" fill="#0f172a">
                    {nameA}
                </text>
                <g transform="translate(60, 115)">
                    <rect x="0" y="0" width="175" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />
                    <text x="87" y="26" textAnchor="middle" fontSize="11" fontStyle="italic" fill="#475569">
                        Molecular Formula: {formula}
                    </text>
                </g>

                <rect x="295" y="25" width="235" height="155" rx="8" fill="#f8fafc" stroke="#6366f1" strokeWidth="1.8" />
                <rect x="295" y="25" width="235" height="32" rx="8" fill="#eef2ff" />
                <text x="412" y="46" textAnchor="middle" fontSize="12" fontWeight="800" fill="#4338ca">
                    COMPOUND B
                </text>
                <text x="412" y="85" textAnchor="middle" fontSize="13" fontWeight="700" fill="#0f172a">
                    {nameB}
                </text>
                <g transform="translate(325, 115)">
                    <rect x="0" y="0" width="175" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />
                    <text x="87" y="26" textAnchor="middle" fontSize="11" fontStyle="italic" fill="#475569">
                        Molecular Formula: {formula}
                    </text>
                </g>

                <g transform="translate(180, 190)">
                    <rect x="0" y="0" width="200" height="22" rx="11" fill="#f1f5f9" stroke="#94a3b8" strokeWidth="1" />
                    <text x="100" y="15" textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#334155">
                        Isomerism: {isomerType}
                    </text>
                </g>
            </svg>
        </div>
    );
}

export default function PhysicsAndEconomicsGraphRenderer({ spec }) {
    if (!spec) return null;
    switch (spec.kind) {
        case 'micrograph_scale_view':
            return <MicrographScaleSvg spec={spec} />;
        case 'organic_structure':
            return <OrganicStructureSvg spec={spec} />;
        case 'source_document':
            return <SourceDocumentSvg spec={spec} />;
        case 'sankey_energy':
            return <SankeyEnergySvg spec={spec} />;
        case 'grid_paper':
            return <GridPaperSvg spec={spec} />;
        case 'motion_graph':
            return <MotionGraphSvg spec={spec} />;
        case 'reaction_energy_profile':
        case 'kc_equilibrium_graph':
        case 'maxwell_boltzmann':
            return <ReactionEnergyProfileSvg spec={spec} />;
        case 'supply_demand':
            return <SupplyDemandSvg spec={spec} />;
        case 'circular_flow':
            return <CircularFlowSvg spec={spec} />;
        case 'production_chain':
            return <ProductionChainSvg spec={spec} />;
        case 'promissory_note':
            return <PromissoryNoteSvg spec={spec} />;
        case 'organogram':
        case 'porters_five_forces':
        case 'process_flow':
        case 'food_chain':
        case 'concept_map':
        case 'ph_scale':
            return <ProcessFlowSvg spec={spec} />;
        default:
            return null;
    }
}
