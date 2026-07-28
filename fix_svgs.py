import os

projects_content = """<svg viewBox="0 0 1000 450" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Projects by Umang Bhut">
  <style>
    :root { --bone: #444444; --rule: #C0C0C0; --muted: #888888; --dim: #AAAAAA; --accent: #555555; }
    @media (prefers-color-scheme: dark) { :root { --bone: #DDDDDD; --rule: #444444; --muted: #777777; --dim: #666666; --accent: #AAAAAA; } }
    .mono { font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
    .rise { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from { opacity:0;transform:translateY(12px); } to { opacity:1;transform:translateY(0); } }
    .a1{animation-delay:.15s} .a2{animation-delay:.35s} .a3{animation-delay:.55s}
    .head { font-size: 15px; fill: var(--bone); }
    .copy { font-size: 14px; fill: var(--muted); }
    .meta { font-size: 10px; fill: var(--accent); letter-spacing: 2.5px; }
    @media (prefers-reduced-motion: reduce) { .rise { animation: none; opacity: 1; } }
      :root { --bone: #000000; --muted: #000000; --dim: #000000; --rule: #000000; --accent: #000000; --node-bg: #FFFFFF; --core-bg: #FFFFFF; --ghost: #000000; }
  </style>

  <g class="rise a1">
    <text class="mono meta" x="48" y="42">001</text>
    <text class="mono head" x="48" y="70">PDM-AI — Predictive Maintenance</text>
    <text class="mono copy" x="48" y="96">AI system to predict machinery failure addressing replacement delays.</text>
    <text class="mono copy" x="48" y="118">Futuristic real-time dashboard displaying live sensor readings.</text>
    <text class="mono meta" x="48" y="148">PYTHON · SCIKIT-LEARN · REACT</text>
  </g>

  <g class="rise a2" transform="translate(0, 160)">
    <text class="mono meta" x="48" y="42">002</text>
    <text class="mono head" x="48" y="70">AI Architect — Blueprint Maker</text>
    <text class="mono copy" x="48" y="96">Auto-generates architectural blueprints from user-entered measurements.</text>
    <text class="mono copy" x="48" y="118">Translates raw plot dimensions into ready-to-use building layouts.</text>
    <text class="mono meta" x="48" y="148">PYTHON · GENERATIVE AI · COMPUTER VISION</text>
  </g>

  <g class="rise a3" transform="translate(0, 320)">
    <text class="mono meta" x="48" y="42">003</text>
    <text class="mono head" x="48" y="70">AI Startup Evaluation Engine</text>
    <text class="mono copy" x="48" y="96">AI platform helping startups assess/improve cost, roadmap &amp; structure.</text>
    <text class="mono copy" x="48" y="118">Startup DNA module profiling core strengths and gaps for founders.</text>
    <text class="mono meta" x="48" y="148">PYTHON · NLP · NEXTJS</text>
  </g>
</svg>"""

experience_content = """<svg viewBox="0 0 1000 370" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Certifications and Training">
  <style>
    :root { --bone: #444444; --rule: #C0C0C0; --muted: #888888; --dim: #AAAAAA; --accent: #555555; }
    @media (prefers-color-scheme: dark) { :root { --bone: #DDDDDD; --rule: #444444; --muted: #777777; --dim: #666666; --accent: #AAAAAA; } }
    .mono { font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
    .rise { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }
    @keyframes rise { from { opacity:0;transform:translateY(8px); } to { opacity:1;transform:translateY(0); } }
    .a1{animation-delay:.15s} .a2{animation-delay:.35s} .a3{animation-delay:.55s} .a4{animation-delay:.75s}
    @media (prefers-reduced-motion: reduce) { .rise { animation: none; opacity: 1; } }
      :root { --bone: #000000; --muted: #000000; --dim: #000000; --rule: #000000; --accent: #000000; --node-bg: #FFFFFF; --core-bg: #FFFFFF; --ghost: #000000; }
  </style>

  <line x1="120" y1="10" x2="120" y2="360" stroke="var(--rule)" stroke-width="1" opacity=".4"/>

  <g class="rise a1">
    <text class="mono" x="48" y="42"  font-size="12" fill="var(--accent)" letter-spacing="2">2025</text>
    <text class="mono" x="136" y="42"  font-size="15" fill="var(--bone)">Oracle Cloud Infrastructure 2025 Certified AI Foundations Associate</text>
    <text class="mono" x="136" y="68"  font-size="14" fill="var(--muted)">Oracle University</text>
  </g>

  <g class="rise a2">
    <text class="mono" x="48" y="128" font-size="12" fill="var(--accent)" letter-spacing="2">2024</text>
    <text class="mono" x="136" y="128" font-size="15" fill="var(--bone)">Certification in Core Java (Grade B)</text>
    <text class="mono" x="136" y="154" font-size="14" fill="var(--muted)">Scholiverse Educare / Skill India / NSDC</text>
  </g>

  <g class="rise a3">
    <text class="mono" x="48" y="214" font-size="12" fill="var(--accent)" letter-spacing="2">2024</text>
    <text class="mono" x="136" y="214" font-size="15" fill="var(--bone)">The C++20 Masterclass: From Fundamentals to Advanced</text>
    <text class="mono" x="136" y="240" font-size="14" fill="var(--muted)">Udemy (115 hrs)</text>
  </g>

  <g class="rise a4">
    <text class="mono" x="48" y="300" font-size="12" fill="var(--accent)" letter-spacing="2">2026</text>
    <text class="mono" x="136" y="300" font-size="15" fill="var(--bone)">100 Days of Code: The Complete Python Pro Bootcamp</text>
    <text class="mono" x="136" y="326" font-size="14" fill="var(--muted)">Udemy (57 hrs)</text>
  </g>
</svg>"""

def fix_now(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    content = content.replace("3RD-YEAR CS @ IITE CHENNAI", "FINAL-YEAR IT @ IITE AHMEDABAD")
    content = content.replace("AI/ML & FULL-STACK DEVELOPER", "ASPIRING DATA SCIENTIST & ML ENGINEER")
    content = content.replace("ISPACE CLUB — WEB & APP DEV", "CERTIFIED ORACLE CLOUD AI ASSOCIATE")
    with open(filepath, 'w') as f:
        f.write(content)

def fix_whoami(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    content = content.replace("third-year CS student at Indus Institute of Technology & Engineering, Ahmedabad.", "final-year IT student at Indus Institute of Technology & Engineering, Ahmedabad.")
    content = content.replace("building across the full stack — SwiftUI · React · PostgreSQL · Node.js · CLI tooling.", "building end-to-end AI/ML solutions — Python · TensorFlow · PyTorch · Databricks.")
    content = content.replace("iSpace Club — Web & App Development department", "Oracle Cloud AI Foundations Associate")
    with open(filepath, 'w') as f:
        f.write(content)

# Update assets
with open('/Users/umang/Downloads/Sharann-del-main/assets/projects.svg', 'w') as f: f.write(projects_content)
with open('/Users/umang/Downloads/Sharann-del-main/assets/dark/projects.svg', 'w') as f: f.write(projects_content)

with open('/Users/umang/Downloads/Sharann-del-main/assets/experience.svg', 'w') as f: f.write(experience_content)
with open('/Users/umang/Downloads/Sharann-del-main/assets/dark/experience.svg', 'w') as f: f.write(experience_content)

fix_now('/Users/umang/Downloads/Sharann-del-main/assets/now.svg')
fix_now('/Users/umang/Downloads/Sharann-del-main/assets/dark/now.svg')
fix_whoami('/Users/umang/Downloads/Sharann-del-main/assets/whoami.svg')
fix_whoami('/Users/umang/Downloads/Sharann-del-main/assets/dark/whoami.svg')
