import re

with open('fundile-landing-improved.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the #demo-recording section with the 4 feature cards
features_html = '''  <!-- ========================================== -->
  <!-- 4. CORE COGNITIVE PILLARS -->
  <!-- ========================================== -->
  <section id="features" class="py-14 sm:py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <!-- Pillar 1: Smart Diagnostic Autopsy -->
        <div class="bg-slate-50/70 p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md transition duration-200">
          <div class="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
            <div class="w-8 h-8 rounded-lg bg-orange-50 text-brand-orange flex items-center justify-center shrink-0 border border-orange-100">
              <i data-lucide="activity" class="w-4 h-4"></i>
            </div>
            <span>Smart Diagnostic Autopsy</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Automatically pinpoints the exact calculation step where marks were lost, just like a master teacher spotting an error pattern on a graded test paper.
          </p>
        </div>

        <!-- Pillar 2: 5-Minute Focus Fixes -->
        <div class="bg-slate-50/70 p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md transition duration-200">
          <div class="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
            <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 border border-emerald-100">
              <i data-lucide="wrench" class="w-4 h-4"></i>
            </div>
            <span>5-Minute Focus Fixes</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Quick 3-question targeted practice sessions isolated purely to the single prerequisite step you stumbled on (such as calculating 15% VAT) before resuming full problems.
          </p>
        </div>

        <!-- Pillar 3: Fair Step Marking -->
        <div class="bg-slate-50/70 p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md transition duration-200">
          <div class="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
            <div class="w-8 h-8 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center shrink-0 border border-purple-100">
              <i data-lucide="check-square" class="w-4 h-4"></i>
            </div>
            <span>Fair Step Marking</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            You receive full method marks [M] for applying correct formulas and logic on subsequent steps, even if an early arithmetic calculation had a minor slip.
          </p>
        </div>

        <!-- Pillar 4: Skill Radar Calibration -->
        <div class="bg-slate-50/70 p-5 rounded-2xl border border-slate-200 shadow-xs hover:shadow-md transition duration-200">
          <div class="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
            <div class="w-8 h-8 rounded-lg bg-blue-50 text-[#13519C] flex items-center justify-center shrink-0 border border-blue-100">
              <i data-lucide="radar" class="w-4 h-4"></i>
            </div>
            <span>Skill Radar Calibration</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            A thought-paced 2 to 4 check radar that skips drills you've already mastered and jumps straight to your optimal challenge tier without anxiety-inducing timers.
          </p>
        </div>

      </div>

    </div>
  </section>'''

# Regex to replace demo-recording section
demo_pattern = re.compile(r'  <!-- ========================================== -->\s*<!-- 4\. SIMULATED SCREEN RECORDING CONTAINER.*?<\/section>', re.DOTALL)
if demo_pattern.search(content):
    content = demo_pattern.sub(features_html, content)
    print("Replaced demo-recording section with features section.")
else:
    print("ERROR: demo-recording section pattern not found!")

# 2. Update footer links
content = content.replace("switchPersonaRecording('learners')", "switchAudienceTab('learners')")
content = content.replace("switchPersonaRecording('parents')", "switchAudienceTab('parents')")
content = content.replace("switchPersonaRecording('teachers')", "switchAudienceTab('teachers')")
content = content.replace("switchPersonaRecording('schools')", "switchAudienceTab('schools')")
content = content.replace('<a href="#demo-recording" class="hover:text-brand-blue transition">Product Walkthrough</a>', '<a href="#features" class="hover:text-brand-blue transition">Core Features</a>')

# 3. Replace the simulation JS with clean navigation script
old_script_pattern = re.compile(r'  <!-- ========================================== -->\s*<!-- 11\. AUTOMATED SCREEN RECORDING SIMULATION ENGINE -->.*?<\/script>', re.DOTALL)

clean_script = '''  <!-- ========================================== -->
  <!-- 11. AUDIENCE NAVIGATION & INTERACTION SCRIPT -->
  <!-- ========================================== -->
  <script>
    lucide.createIcons();

    let activePersona = 'learners';
    const audienceSections = {
      learners: 'problem-promise',
      parents: 'not-a-chatbot',
      teachers: 'structured-system',
      schools: 'pricing'
    };

    const audienceLabels = {
      learners: 'Learner Experience • Step-by-Step Scaffolding',
      parents: 'Parent Overview • Transparent Weekly Progress',
      teachers: 'Teacher Workflow • Instant Exam Authoring',
      schools: 'School Administration • SASAMS & ATP Pacing'
    };

    function switchAudienceTab(role) {
      activePersona = role;

      // Update secondary ribbon pills
      ['learners', 'parents', 'teachers', 'schools'].forEach(r => {
        const btn = document.getElementById('ribbon-btn-' + r);
        const dot = document.getElementById('dot-' + r);
        if (btn) {
          if (r === role) {
            btn.className = 'relative z-10 inline-flex items-center gap-2 px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-full text-xs sm:text-sm font-bold transition-all duration-200 cursor-pointer shrink-0 bg-white text-[#13519C] ring-2 ring-[#FF9100] shadow-md shadow-amber-500/20 scale-[1.02]';
            if (dot) dot.classList.remove('hidden');
          } else {
            btn.className = 'relative z-10 inline-flex items-center gap-2 px-3.5 py-1.5 sm:px-4 sm:py-2 rounded-full text-xs sm:text-sm font-bold transition-all duration-200 cursor-pointer shrink-0 bg-white text-[#13519C] border border-slate-200/90 hover:bg-slate-50 hover:shadow-xs';
            if (dot) dot.classList.add('hidden');
          }
        }
      });

      // Update right context label
      const ribbonContext = document.getElementById('ribbon-context-text');
      if (ribbonContext && audienceLabels[role]) {
        ribbonContext.innerHTML = `<span class="w-2 h-2 rounded-full bg-brand-orange"></span><span>${audienceLabels[role]}</span>`;
      }

      // Smooth scroll to relevant section
      const targetId = audienceSections[role];
      if (targetId) {
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          const yOffset = -80;
          const y = targetEl.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }
    }
  </script>'''

if old_script_pattern.search(content):
    content = old_script_pattern.sub(clean_script, content)
    print("Replaced simulation script with clean audience navigation script.")
else:
    print("ERROR: simulation script pattern not found!")

with open('fundile-landing-improved.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated fundile-landing-improved.html successfully.")
