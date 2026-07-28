import os

files_to_process = [
    '/Users/umang/Downloads/Sharann-del-main/assets/telemetry.svg',
    '/Users/umang/Downloads/Sharann-del-main/assets/dark/telemetry.svg'
]

replacement_languages = '''    <text fill="var(--bone)" x="48" y="108">python</text>       <rect class="bar g1" x="48" y="116" width="230" height="6" fill="var(--accent)"/><text fill="var(--muted)" x="288" y="123" font-size="10">45%</text>
    <text fill="var(--bone)" x="48" y="146">typescript</text>  <rect class="bar g2" x="48" y="154" width="145" height="6" fill="var(--bone)"/><text fill="var(--muted)" x="203" y="161" font-size="10">20%</text>
    <text fill="var(--bone)" x="48" y="184">c++</text>      <rect class="bar g3" x="48" y="192" width="120" height="6" fill="var(--bone)"/><text fill="var(--muted)" x="178" y="199" font-size="10">15%</text>
    <text fill="var(--bone)" x="48" y="222">java</text>  <rect class="bar g4" x="48" y="230" width="85" height="6" fill="var(--bone)"/><text fill="var(--muted)" x="143" y="237" font-size="10">10%</text>
    <text fill="var(--bone)" x="48" y="260">javascript</text>        <rect class="bar g5" x="48" y="268" width="68"  height="6" fill="var(--bone)"/><text fill="var(--muted)" x="126" y="275" font-size="10">5%</text>
    <text fill="var(--bone)" x="48" y="298">html/css</text> <rect class="bar g6" x="48" y="306" width="50"  height="6" fill="var(--bone)"/><text fill="var(--muted)" x="108" y="313" font-size="10">5%</text>'''

for filepath in files_to_process:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Repositories
    content = content.replace('51</text><text fill="var(--muted)" class="mono" x="790" y="112" font-size="10" letter-spacing="2.5">REPOSITORIES', '21</text><text fill="var(--muted)" class="mono" x="790" y="112" font-size="10" letter-spacing="2.5">REPOSITORIES')
    
    # Remove projects documented and shift up
    content = content.replace('<g class="rise n2"><text fill="var(--bone)" class="mono" x="720" y="178" font-size="44">15</text><text fill="var(--muted)" class="mono" x="790" y="172" font-size="10" letter-spacing="2.5">PROJECTS DOCUMENTED</text></g>', '')
    content = content.replace('x="720" y="238"', 'x="720" y="178"')
    content = content.replace('x="790" y="232"', 'x="790" y="172"')
    content = content.replace('x="718" y="298"', 'x="718" y="238"')
    content = content.replace('x="790" y="292"', 'x="790" y="232"')

    with open(filepath, 'w', encoding='utf-8') as f:
        lines = content.split('\n')
        skip = False
        for line in lines:
            if 'x="48" y="108"' in line:
                f.write(replacement_languages + '\n')
                skip = True
            elif skip and ('x="48" y="146"' in line or 'x="48" y="184"' in line or 'x="48" y="222"' in line or 'x="48" y="260"' in line or 'x="48" y="298"' in line):
                continue
            else:
                skip = False
                f.write(line + '\n')

