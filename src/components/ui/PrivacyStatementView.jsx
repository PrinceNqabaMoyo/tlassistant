import React, { useEffect } from 'react';
import { ArrowLeft, ShieldCheck, Lock, UserCheck, School, FileText, Mail, Database, Eye } from 'lucide-react';
import FundileLogo from './FundileLogo';

export default function PrivacyStatementView({ onBackToLanding = () => {} }) {
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    document.title = 'Fundile | Privacy Statement & POPIA Compliance';
    return () => {
      document.title = 'Fundile | Teaching & Learning Assistant';
    };
  }, []);

  const handleBack = () => {
    if (typeof onBackToLanding === 'function') {
      onBackToLanding();
    } else if (window.history.length > 1) {
      window.history.back();
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 font-sans selection:bg-blue-100 selection:text-[#13519C]">
      {/* Light Background Main Ribbon with 'Fundile' in Brand Blue */}
      <header className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/90 shadow-xs">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          {/* Brand Mark in Brand Blue */}
          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={handleBack}
              className="flex items-center gap-2 group cursor-pointer focus:outline-hidden"
              title="Return to Landing Page"
            >
              <FundileLogo
                className="h-9 w-auto text-[#13519C]"
                wordmarkColor="#13519C"
              />
            </button>
            <span className="hidden sm:inline-block px-2.5 py-0.5 rounded-full bg-blue-50 text-[#13519C] text-[11px] font-bold border border-blue-200/80">
              POPIA Section 35 Compliant
            </span>
          </div>

          {/* Smooth Back to Landing Page Button */}
          <button
            type="button"
            onClick={handleBack}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-[#13519C] hover:text-[#0b376b] text-xs sm:text-sm font-bold transition-all duration-150 cursor-pointer border border-slate-200/80 active:scale-95"
            style={{ fontFamily: 'Afacad, sans-serif' }}
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back to Landing Page</span>
          </button>
        </div>
      </header>

      {/* Main Privacy Statement Document */}
      <main className="max-w-4xl mx-auto px-4 sm:px-6 py-10 sm:py-14 space-y-10">
        {/* Hero Section */}
        <div className="bg-white p-6 sm:p-10 rounded-3xl border border-slate-200 shadow-xs space-y-4">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-50 border border-amber-200 text-amber-900 text-xs font-bold uppercase tracking-wider">
            <ShieldCheck className="w-4 h-4 text-[#FF9100]" />
            <span>Official Privacy Statement</span>
          </div>
          <h1
            className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 tracking-tight"
            style={{ fontFamily: 'Afacad, sans-serif' }}
          >
            Privacy Statement &amp; Child Data Protection
          </h1>
          <p className="text-base sm:text-lg text-slate-600 leading-relaxed max-w-3xl">
            Fundile is committed to safeguarding the personal information and academic dignity of minor learners, parents, educators, and schools across South Africa. We design our technology in strict compliance with the Protection of Personal Information Act (POPIA No. 4 of 2013), with specific adherence to <strong>Section 35</strong> governing the prohibition and lawful conditions on processing personal information concerning children.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-4 border-t border-slate-100 text-xs">
            <div className="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
              <span className="text-slate-400 block font-semibold uppercase text-[10px]">Jurisdiction</span>
              <span className="font-bold text-slate-800">Republic of South Africa</span>
            </div>
            <div className="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
              <span className="text-slate-400 block font-semibold uppercase text-[10px]">Regulatory Standard</span>
              <span className="font-bold text-slate-800">POPIA Act No. 4 of 2013</span>
            </div>
            <div className="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
              <span className="text-slate-400 block font-semibold uppercase text-[10px]">Minor Protection</span>
              <span className="font-bold text-slate-800">Section 35 Certified</span>
            </div>
          </div>
        </div>

        {/* Section 1: POPIA Section 35 & Parental Consent */}
        <section className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center font-bold">
              <Lock className="w-5 h-5" />
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
              1. Child Data Protection &amp; Parental Consent (Section 35)
            </h2>
          </div>
          <div className="space-y-3 text-sm sm:text-base text-slate-600 leading-relaxed">
            <p>
              In accordance with Section 35(1) of POPIA, a responsible party may not process personal information concerning a child unless the processing is carried out with the prior consent of a competent person (a parent or legal guardian) or is necessary for the establishment, exercise, or defence of a right or obligation in law.
            </p>
            <p>
              Fundile implements explicit parental or institutional authorization:
            </p>
            <ul className="list-disc pl-5 space-y-1.5 text-slate-700">
              <li>
                <strong>Independent Learners under 18:</strong> Accounts must be authorized by a parent or legal guardian via our Family Bridge linking protocol, allowing parents full transparency over data access.
              </li>
              <li>
                <strong>School Roster Enrolment:</strong> When schools register classes, the school warrants that it possesses the requisite institutional and parental consents under the South African Schools Act and national educational directives.
              </li>
              <li>
                <strong>Zero Commercial Monetization:</strong> We never sell, lease, rent, or trade student personal records or academic submissions to advertisers, data brokers, or third parties.
              </li>
            </ul>
          </div>
        </section>

        {/* Section 2: What Information We Collect */}
        <section className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
              <Database className="w-5 h-5" />
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
              2. Information We Collect and Process
            </h2>
          </div>
          <div className="space-y-3 text-sm sm:text-base text-slate-600 leading-relaxed">
            <p>
              We collect strictly the minimum personal information necessary to deliver adaptive curriculum learning:
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs sm:text-sm">
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                <h3 className="font-bold text-slate-900 mb-1">Account &amp; Profile Identifiers</h3>
                <p className="text-slate-600">Student full name, grade (7–12), school affiliation, email address (optional for minor learners via parent proxy), and optional avatar picture.</p>
              </div>
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                <h3 className="font-bold text-slate-900 mb-1">Formative Academic Telemetry</h3>
                <p className="text-slate-600">Question attempts, stepwise procedural working, ledger cell coordinates, accuracy scores, misconception tags, and time-on-task metrics.</p>
              </div>
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                <h3 className="font-bold text-slate-900 mb-1">Parent &amp; Guardian Links</h3>
                <p className="text-slate-600">Contact details of up to 2 linked parents/guardians strictly for delivery of weekly Sunday Academic Pulse summaries via WhatsApp or SMS.</p>
              </div>
              <div className="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                <h3 className="font-bold text-slate-900 mb-1">Teacher &amp; Classroom Links</h3>
                <p className="text-slate-600">Six-character class join codes connecting learners to their authentic school teachers for homework and exam dispatch.</p>
              </div>
            </div>
          </div>
        </section>

        {/* Section 3: Data Security & Lean Architecture */}
        <section className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-orange-50 text-[#FF9100] flex items-center justify-center font-bold">
              <Eye className="w-5 h-5" />
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
              3. Data Security, Retention &amp; Lean Bandwidth
            </h2>
          </div>
          <div className="space-y-3 text-sm sm:text-base text-slate-600 leading-relaxed">
            <p>
              All communication between your device and Fundile servers is encrypted using modern Transport Layer Security (TLS 1.3). Student data stored in our databases is encrypted at rest using industry-standard AES-256 encryption.
            </p>
            <p>
              Our ultra-lean architecture operates on under 2 MB of weekly data usage, caching curriculum templates locally on the learner's device so that personal study can continue uninterrupted during network disruptions and load shedding.
            </p>
            <p>
              Student assessment logs and diagnostic autopsies are retained for the duration of the learner's academic subscription and can be permanently purged upon written request from the parent or school administrator.
            </p>
          </div>
        </section>

        {/* Section 4: Parental Rights and Contact */}
        <section className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-xs space-y-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
              <UserCheck className="w-5 h-5" />
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
              4. Rights of Parents, Learners &amp; Schools
            </h2>
          </div>
          <div className="space-y-3 text-sm sm:text-base text-slate-600 leading-relaxed">
            <p>
              Under POPIA, data subjects and their competent representatives hold the following rights:
            </p>
            <ul className="list-disc pl-5 space-y-1.5 text-slate-700">
              <li><strong>Right to Access:</strong> Inspect all academic records, diagnostic histories, and profile details stored by Fundile.</li>
              <li><strong>Right to Rectification:</strong> Request correction of inaccurate personal information or class linkages.</li>
              <li><strong>Right to Deletion (Right to be Forgotten):</strong> Request the permanent deletion of personal records and test telemetry.</li>
              <li><strong>Right to Objection:</strong> Object to specific forms of processing where applicable.</li>
            </ul>
          </div>

          <div className="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
              <span className="text-xs text-slate-500 block">Information Officer &amp; Inquiries:</span>
              <a
                href="mailto:info@fundile.com?subject=POPIA%20Privacy%20Inquiry"
                className="text-sm font-bold text-[#13519C] hover:underline flex items-center gap-1.5"
              >
                <Mail className="w-4 h-4 text-[#13519C]" />
                <span>info@fundile.com</span>
              </a>
            </div>

            <button
              type="button"
              onClick={handleBack}
              className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0e3c73] text-white text-xs sm:text-sm font-bold shadow-md shadow-blue-900/20 transition cursor-pointer"
              style={{ fontFamily: 'Afacad, sans-serif' }}
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Back to Landing Page</span>
            </button>
          </div>
        </section>
      </main>
    </div>
  );
}
