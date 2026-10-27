# -*- coding: utf-8 -*-
"""
Extract LANG_METADATA and DRAMA_SCRIPTS from sample_roleplay_preview.html
and write to data/roleplay_db.js.
"""
import re

with open('sample_roleplay_preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract LANG_METADATA
meta_match = re.search(r'const LANG_METADATA = (\{[\s\S]*?\n    \});', html)
if not meta_match:
    raise ValueError("LANG_METADATA not found")
lang_metadata_code = meta_match.group(1)

# Extract DRAMA_SCRIPTS
scripts_match = re.search(r'const DRAMA_SCRIPTS = (\{[\s\S]*?\n    \});', html)
if not scripts_match:
    raise ValueError("DRAMA_SCRIPTS not found")
drama_scripts_code = scripts_match.group(1)

# Replace file:///c:/DMDG_Jobs/.agents/assets/ with assets/agents/
# but with fallback support so both local and relative work
drama_scripts_code = drama_scripts_code.replace('file:///c:/DMDG_Jobs/.agents/assets/', 'assets/agents/')

roleplay_js_content = f"""// ============================================================
// 🎬 [말쌈 3D 숏폼 상황극 데이터베이스: K-컬처 6개국어 더빙 시뮬레이터]
// ============================================================

window.LANG_METADATA = {lang_metadata_code};

window.DRAMA_SCRIPTS = {drama_scripts_code};

window.ROLEPLAY_WORDS = [
  {{
    id: 202,
    word: "눈치",
    romanization: "nunchi",
    phonetic_respelling: "NOON-chee",
    sub_category: "relationship",
    era: "soul",
    cast: ["Demis (팀장)", "Craig (풀스택)", "Jennifer (UX)"],
    duration: "15s Shorts",
    episodes: [
      {{
        id: "ep1",
        title: "등산과 삼계탕 회식의 비극 (5G급 눈치 배틀)",
        scenesCount: 5
      }}
    ]
  }}
];
"""

with open('data/roleplay_db.js', 'w', encoding='utf-8') as f:
    f.write(roleplay_js_content)

print("Created data/roleplay_db.js successfully!")
