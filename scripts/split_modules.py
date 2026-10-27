# -*- coding: utf-8 -*-
import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in index.html: {len(lines)}")

# 1. Extract CSS (lines 12 to 1900, 0-indexed: 11 to 1900)
css_content = ''.join(lines[12:1900])
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content.strip() + '\n')
print("Extracted css/style.css")

# 2. Extract DEFAULT_WORDS to data/words_db.js
# From line 2461 (const DEFAULT_WORDS = [) to line 15347 (];)
words_code = ''.join(lines[2461:15347])
with open('data/words_db.js', 'w', encoding='utf-8') as f:
    f.write("// MALSSAM 318 Words Complete Database\nwindow.DEFAULT_WORDS = " + words_code.replace("const DEFAULT_WORDS = ", "").strip() + ";\n")
print("Extracted data/words_db.js")

# 3. Extract KAKAO_SEED_CARDS to data/kakao_cards.js
# Search for KAKAO_SEED_CARDS
kakao_start = None
kakao_end = None
for i, line in enumerate(lines):
    if 'const KAKAO_SEED_CARDS =' in line:
        kakao_start = i
    if kakao_start is not None and i > kakao_start and '];' in line:
        kakao_end = i + 1
        break

if kakao_start and kakao_end:
    kakao_code = ''.join(lines[kakao_start:kakao_end])
    with open('data/kakao_cards.js', 'w', encoding='utf-8') as f:
        f.write("// MALSSAM Kakao Seed Cards\nwindow.KAKAO_SEED_CARDS = " + kakao_code.replace("const KAKAO_SEED_CARDS = ", "").strip() + "\n")
    print("Extracted data/kakao_cards.js")

# 4. Extract MALSSAM_BATTLE_QUESTIONS to data/battle_questions.js
battle_start = None
battle_end = None
for i, line in enumerate(lines):
    if 'const MALSSAM_BATTLE_QUESTIONS =' in line:
        battle_start = i
    if battle_start is not None and i > battle_start and '];' in line and i > battle_start + 50:
        battle_end = i + 1
        break

if battle_start and battle_end:
    battle_code = ''.join(lines[battle_start:battle_end])
    with open('data/battle_questions.js', 'w', encoding='utf-8') as f:
        f.write("// MALSSAM Live Battle Questions\nwindow.MALSSAM_BATTLE_QUESTIONS = " + battle_code.replace("const MALSSAM_BATTLE_QUESTIONS = ", "").strip() + "\n")
    print("Extracted data/battle_questions.js")

print("Data & CSS extraction step complete!")
