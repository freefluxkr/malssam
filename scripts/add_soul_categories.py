# -*- coding: utf-8 -*-
"""
Add onomatopoeia, mimetic, and color subcategories to data/words_db.js
and mark '눈치' with has_roleplay: true.
"""
import json
import re

with open('data/words_db.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JSON from 'window.DEFAULT_WORDS = [...];'
prefix = 'window.DEFAULT_WORDS = '
idx_start = content.find(prefix)
if idx_start == -1:
    raise ValueError("window.DEFAULT_WORDS not found")

json_text = content[idx_start + len(prefix):].strip()
if json_text.endswith(';;'):
    json_text = json_text[:-2].strip()
elif json_text.endswith(';'):
    json_text = json_text[:-1].strip()

words = json.loads(json_text)
print(f"Loaded {len(words)} words.")

# 1. Update '눈치' (id: 202)
for w in words:
    if w.get('id') == 202 or w.get('word') == '눈치':
        w['has_roleplay'] = True
        print("Updated '눈치' with has_roleplay=True")

# 2. Add 15 new untranslatable K-Culture words
new_items = [
    # ── 의성어 (Onomatopoeia - 5선) ───────────────────────────
    {
        "id": 319,
        "word": "꼬르륵",
        "pronunciation": "[ggoleuleuk]",
        "part_of_speech": "부사 / 의성어",
        "chosung": "ㄲㄹㄹ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "배가 몹시 고플 때 위장에서 맑고 요란하게 울리는 공복의 신호음.",
        "origin": "배 속의 가스와 액체가 음식물을 갈망하며 울리는 한국 고유의 생생한 청각 묘사.",
        "examples": [
            "A: 조용한 회의실에서 갑자기 배에서 '꼬르륵' 소리가 나서 얼굴이 빨개졌어요.\nB: 다들 배고픈 시간이라 다 이해했을 거예요!"
        ],
        "tags": ["꼬르륵", "의성어", "배고픔", "소리", "공복", "K정서"],
        "likes": 5420,
        "dislikes": 12,
        "toxicity_level": 0,
        "standard_korean_mapping": "배고플 때 뱃속에서 가볍게 울려 나오는 소리",
        "trend_status": "SOUL",
        "sub_category": "onomatopoeia",
        "en": {
            "slang": "Ggoleuleuk (Tummy Rumbling Sound)",
            "desc": "The vivid Korean sound-symbolic word for a hungry, rumbling stomach during quiet, awkward moments.",
            "ex": "A: In the middle of the silent exam room, my stomach went '꼬르륵' so loudly!"
        },
        "romanization": "ggoleuleuk",
        "phonetic_respelling": "GGO-reu-reuk"
    },
    {
        "id": 320,
        "word": "두근두근",
        "pronunciation": "[dugeundugeun]",
        "part_of_speech": "부사 / 의성어",
        "chosung": "ㄷㄱㄷㄱ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "좋아하는 사람을 보거나 중대한 발표를 앞두고 가슴속 심장이 빠르게 뛰는 소리와 울림.",
        "origin": "설렘과 긴장이 교차하는 찰나의 심장 박동을 청각적이면서도 감성적으로 담아낸 대표 단어.",
        "examples": [
            "A: 면접장에 들어가기 직전에 심장이 두근두근 터질 뻔했어요.\nB: 그래도 침착하게 잘 해내셨잖아요!"
        ],
        "tags": ["두근두근", "의성어", "설렘", "심쿵", "긴장", "K정서"],
        "likes": 8930,
        "dislikes": 15,
        "toxicity_level": 0,
        "standard_korean_mapping": "몹시 놀라거나 설레어 가슴이 자꾸 뛰는 모양이나 소리",
        "trend_status": "SOUL",
        "sub_category": "onomatopoeia",
        "en": {
            "slang": "Dugeun-dugeun (Pounding Heartbeat of Thrill)",
            "desc": "The quintessential Korean sound of a beating heart full of romance, fluttering anticipation, or nervous excitement.",
            "ex": "My heart went '두근두근' the first time we held hands under the cherry blossoms."
        },
        "romanization": "dugeundugeun",
        "phonetic_respelling": "DOO-geun-doo-geun"
    },
    {
        "id": 321,
        "word": "철렁",
        "pronunciation": "[cheolleong]",
        "part_of_speech": "부사 / 의성어·의태어",
        "chosung": "ㅊㄹ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "예상치 못한 충격적인 소식이나 위기 상황에 심장이 쿵 하고 아래로 덜컥 내려앉는 충격.",
        "origin": "깊은 우물에 큰 돌이 빠져 물이 출렁이듯, 가슴속 피와 심장이 순간 얼어붙는 감각의 형상화.",
        "examples": [
            "A: 지갑을 지하철에 두고 내린 걸 알고 가슴이 철렁 내려앉았어.\nB: 헐 분실물 센터에 바로 전화해 봐!"
        ],
        "tags": ["철렁", "의성어", "가슴철렁", "깜짝", "충격", "K정서"],
        "likes": 6120,
        "dislikes": 20,
        "toxicity_level": 0,
        "standard_korean_mapping": "갑자기 가슴이 서늘해지며 심장이 덜컥 내려앉는 느낌",
        "trend_status": "SOUL",
        "sub_category": "onomatopoeia",
        "en": {
            "slang": "Cheolleong (Heart Dropping Into Stomach)",
            "desc": "The sudden, visceral emotional shockwave when your heart violently sinks upon hearing shocking bad news or realizing a critical mistake.",
            "ex": "My heart sank with a '철렁' when I realized my laptop bag was missing."
        },
        "romanization": "cheolleong",
        "phonetic_respelling": "CHUL-lung"
    },
    {
        "id": 322,
        "word": "찰랑찰랑",
        "pronunciation": "[challangchallang]",
        "part_of_speech": "부사 / 의성어·의태어",
        "chosung": "ㅊㄹㅊㄹ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "맑고 깨끗한 물이 그릇의 가장자리까지 가득 차서 넘칠 듯 가볍게 일렁이며 부딪히는 소리와 모양.",
        "origin": "한국의 맑은 시냇물과 찻잔의 풍요로움을 오감으로 느끼는 시각·청각 복합 미학어.",
        "examples": [
            "A: 찻잔에 가득 따른 차가 찰랑찰랑 넘칠 것 같아 조심조심 들었어.\nB: 찰랑거리는 찻잔을 보니까 마음이 참 평화로워진다."
        ],
        "tags": ["찰랑찰랑", "의성어", "물소리", "맑음", "풍요로움", "K정서"],
        "likes": 4750,
        "dislikes": 8,
        "toxicity_level": 0,
        "standard_korean_mapping": "얕은 물이나 액체가 가득 차서 가볍게 흔들리며 부딪히는 소리나 모양",
        "trend_status": "SOUL",
        "sub_category": "onomatopoeia",
        "en": {
            "slang": "Challang-challang (Gentle Lapping / Brimming Ripples)",
            "desc": "The delicate visual and auditory sensation of clear water filled to the very brim, gently sloshing without spilling.",
            "ex": "The hot spring water was swaying '찰랑찰랑' against the cypress edge."
        },
        "romanization": "challangchallang",
        "phonetic_respelling": "CHAHL-lahng-chahl-lahng"
    },
    {
        "id": 323,
        "word": "쿵쾅쿵쾅",
        "pronunciation": "[kungkawngkungkawng]",
        "part_of_speech": "부사 / 의성어",
        "chosung": "ㅋㅋㅋㅋ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "층간소음처럼 무겁고 거친 발소리가 울리거나, 극도의 공포·긴장으로 심장이 세차게 방망이질하는 소리.",
        "origin": "묵직한 충격과 압박감이 공간을 타고 울려 퍼지는 극적인 음향의 순우리말 표현.",
        "examples": [
            "A: 윗집에서 밤마다 쿵쾅쿵쾅 걸어 다니는 소리에 잠을 못 자겠어요.\nB: 층간소음은 정말 쿵쾅거릴 때마다 스트레스 최고죠."
        ],
        "tags": ["쿵쾅쿵쾅", "의성어", "층간소음", "심장박동", "울림", "K정서"],
        "likes": 7320,
        "dislikes": 35,
        "toxicity_level": 0,
        "standard_korean_mapping": "무거운 물건이 잇따라 떨어지거나 발을 세게 굴러 울리는 소리",
        "trend_status": "SOUL",
        "sub_category": "onomatopoeia",
        "en": {
            "slang": "Kungkawng-kungkawng (Heavy Thumping / Stomping Echo)",
            "desc": "The resounding sound of heavy stomping footsteps overhead or violent heart pounding during high adrenaline.",
            "ex": "Someone was stomping '쿵쾅쿵쾅' upstairs in the middle of the night."
        },
        "romanization": "kungkawngkungkawng",
        "phonetic_respelling": "KOONG-kwahng-koong-kwahng"
    },

    # ── 의태어 (Mimetic - 5선) ───────────────────────────────
    {
        "id": 324,
        "word": "살금살금",
        "pronunciation": "[salgeumsalgeum]",
        "part_of_speech": "부사 / 의태어",
        "chosung": "ㅅㄱㅅㄱ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "남이 알아채지 못하게 발소리를 완전히 죽이고 고양이처럼 조심조심 걷는 모양.",
        "origin": "배려심이나 은밀함을 담아 발끝을 세워 소리를 지우는 한국인의 발걸음 미학.",
        "examples": [
            "A: 아기가 겨우 잠들어서 남편이 살금살금 거실로 걸어 나왔어요.\nB: 삐걱 소리라도 날까 봐 완전 닌자처럼 움직였겠네요!"
        ],
        "tags": ["살금살금", "의태어", "조심조심", "발소리", "고양이걸음", "K정서"],
        "likes": 5890,
        "dislikes": 9,
        "toxicity_level": 0,
        "standard_korean_mapping": "남의 눈이나 귀에 띄지 않도록 소리 없이 조심스럽게 행동하는 모양",
        "trend_status": "SOUL",
        "sub_category": "mimetic",
        "en": {
            "slang": "Salgeum-salgeum (Stealthy Tiptoeing)",
            "desc": "Walking on absolute tiptoes with feline grace and hyper-caution so as not to wake anyone or cause a sound.",
            "ex": "He walked '살금살금' across the wooden floor so he wouldn't wake the sleeping baby."
        },
        "romanization": "salgeumsalgeum",
        "phonetic_respelling": "SAHL-geum-sahl-geum"
    },
    {
        "id": 325,
        "word": "아장아장",
        "pronunciation": "[ajang-ajang]",
        "part_of_speech": "부사 / 의태어",
        "chosung": "ㅇㅈㅇㅈ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "첫걸음마를 뗀 아기나 작은 펭귄이 서툴지만 지극히 사랑스럽게 짧은 보폭으로 걷는 모양.",
        "origin": "작고 여린 생명체가 세상에 내딛는 첫걸음의 사랑스러움을 극대화한 한국어 고유의 온기.",
        "examples": [
            "A: 돌 지난 조카가 아장아장 걸어오는데 심장 녹아내리는 줄 알았어.\nB: 뒤뚱뒤뚱하면서도 엄마한테 안기려고 달려올 때 진짜 천사죠!"
        ],
        "tags": ["아장아장", "의태어", "걸음마", "귀여움", "아기", "K정서"],
        "likes": 9810,
        "dislikes": 7,
        "toxicity_level": 0,
        "standard_korean_mapping": "어린아이가 다리에 힘이 없어 짧은 걸음으로 위태롭게 걷는 모양",
        "trend_status": "SOUL",
        "sub_category": "mimetic",
        "en": {
            "slang": "Ajang-ajang (Adorable Toddling Baby Steps)",
            "desc": "The heartwarming, unsteady yet supremely adorable waddling steps of a baby learning to walk.",
            "ex": "The 1-year-old toddler walked '아장아장' across the lawn into her grandmother's open arms."
        },
        "romanization": "ajang-ajang",
        "phonetic_respelling": "AH-jahng-ah-jahng"
    },
    {
        "id": 326,
        "word": "말랑말랑",
        "pronunciation": "[mallangmallang]",
        "part_of_speech": "부사 / 의태어·형용사",
        "chosung": "ㅁㄹㅁㄹ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "손가락으로 살짝 누르면 폭신하게 쑥 들어갔다가 기분 좋게 튕겨 나오는 부드럽고 탄력 있는 촉감.",
        "origin": "떡, 젤리, 갓 구운 빵 등 한국인이 사랑하는 쫄깃하고 폭신한 디저트 질감의 정점.",
        "examples": [
            "A: 방금 쪄낸 찹쌀떡이 말랑말랑해서 입에서 사르르 녹아요.\nB: 아기 볼살도 진짜 말랑말랑해서 자꾸 만지고 싶어져요!"
        ],
        "tags": ["말랑말랑", "의태어", "촉감", "모찌", "폭신폭신", "K정서"],
        "likes": 8410,
        "dislikes": 11,
        "toxicity_level": 0,
        "standard_korean_mapping": "단단하지 않고 부드러우며 탄력 있게 탄탄한 촉감",
        "trend_status": "SOUL",
        "sub_category": "mimetic",
        "en": {
            "slang": "Mallang-mallang (Squishy Marshmallow Softness)",
            "desc": "The delightfully yielding, pillowy, and elastic tactile texture of freshly steamed mochi, squishies, or a baby's cheeks.",
            "ex": "The fresh rice cake was so '말랑말랑' and tender it melted on my tongue."
        },
        "romanization": "mallangmallang",
        "phonetic_respelling": "MAHL-lahng-mahl-lahng"
    },
    {
        "id": 327,
        "word": "반짝반짝",
        "pronunciation": "[banjjakbanjjak]",
        "part_of_speech": "부사 / 의태어",
        "chosung": "ㅂㅉㅂㅉ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "작은 빛이나 보석, 밤하늘의 별이 맑고 투명하게 주기적으로 빛을 발하는 황홀한 모양.",
        "origin": "맑은 이슬과 밤하늘 별빛의 영롱함을 동요처럼 맑고 순수하게 빚어낸 한국 대표 의태어.",
        "examples": [
            "A: 밤하늘을 올려다보니까 수많은 별들이 반짝반짝 빛나고 있더라고요.\nB: 반짝이는 별빛을 보면 도시의 피로가 싹 풀려요."
        ],
        "tags": ["반짝반짝", "의태어", "별빛", "영롱함", "빛남", "K정서"],
        "likes": 9120,
        "dislikes": 6,
        "toxicity_level": 0,
        "standard_korean_mapping": "작은 빛이 잇따라 잠깐씩 맑고 밝게 빛나는 모양",
        "trend_status": "SOUL",
        "sub_category": "mimetic",
        "en": {
            "slang": "Banjjak-banjjak (Twinkling Radiance)",
            "desc": "The pure, crystalline shimmering and twinkling of stars, morning dewdrops, or a loved one's sparkling eyes.",
            "ex": "The stars were glittering '반짝반짝' like diamonds scattered across the midnight sky."
        },
        "romanization": "banjjakbanjjak",
        "phonetic_respelling": "BAHN-jjak-bahn-jjak"
    },
    {
        "id": 328,
        "word": "뒤뚱뒤뚱",
        "pronunciation": "[dwittungdwittung]",
        "part_of_speech": "부사 / 의태어",
        "chosung": "ㄷㄸㄷㄸ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "오리나 펭귄, 또는 뚱뚱하거나 짐이 무거운 사람이 좌우로 크게 몸을 기우뚱거리며 걷는 해학적 모양.",
        "origin": "서툴면서도 유쾌하고 귀여운 신체 역학을 친근감 있게 풀어낸 한국어 특유의 풍류 묘사.",
        "examples": [
            "A: 뒤뚱뒤뚱 걸어가는 오리 떼를 보니까 절로 미소가 지어지네요.\nB: 무거운 배낭 메고 산에 오를 때 제 모습도 딱 뒤뚱뒤뚱이었어요!"
        ],
        "tags": ["뒤뚱뒤뚱", "의태어", "오리걸음", "유쾌함", "뒤뚱거림", "K정서"],
        "likes": 6340,
        "dislikes": 14,
        "toxicity_level": 0,
        "standard_korean_mapping": "몸의 균형을 잡지 못하고 이리저리 심하게 흔들리며 걷는 모양",
        "trend_status": "SOUL",
        "sub_category": "mimetic",
        "en": {
            "slang": "Dwittung-dwittung (Humorous Waddling Side-to-Side)",
            "desc": "The comical, affectionate waddling movement of ducks, penguins, or someone balancing a heavy backpack.",
            "ex": "The mother duck walked '뒤뚱뒤뚱' followed closely by her fuzzy ducklings."
        },
        "romanization": "dwittungdwittung",
        "phonetic_respelling": "DWEE-ttoong-dwee-ttoong"
    },

    # ── 색채어 (Korean Color Spectrum - 5선) ───────────────────
    {
        "id": 329,
        "word": "노르스름하다",
        "pronunciation": "[noreuseureumhada]",
        "part_of_speech": "형용사 / 색채어",
        "chosung": "ㄴㄹㅅㄹㅎㄷ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "단순한 노란색(Yellow)이 아니라, 알맞게 잘 구워진 군고구마나 식빵처럼 포근하고 먹음직스럽게 누런빛이 은은하게 감도는 상태.",
        "origin": "단일 색상 단어가 아닌, 채도와 명도, 심리적 온도가 얽혀 섬세하게 세분화된 한국어 14단계 황색 스펙트럼의 백미.",
        "examples": [
            "A: 노르스름하게 잘 익은 파전 냄새에 침이 꼴깍 넘어가네요.\nB: 겉바속촉으로 딱 저 색깔이 나올 때가 제일 맛있죠!"
        ],
        "tags": ["노르스름하다", "색채어", "황색", "식욕", "황금빛", "K정서"],
        "likes": 7680,
        "dislikes": 10,
        "toxicity_level": 0,
        "standard_korean_mapping": "조금 노란빛을 띠어 부드럽고 따스한 느낌을 주는 상태",
        "trend_status": "SOUL",
        "sub_category": "color",
        "en": {
            "slang": "Noreuseureumhada (Gently Toasted Golden-Yellow)",
            "desc": "Far more nuanced than plain 'yellow'—describes food toasted to mouth-watering golden perfection with a warm, appetizing glow.",
            "ex": "The Korean seafood pancake was fried to a delicate '노르스름하다' crispiness."
        },
        "romanization": "noreuseureumhada",
        "phonetic_respelling": "NOH-reu-seu-reum-hah-dah"
    },
    {
        "id": 330,
        "word": "파르스름하다",
        "pronunciation": "[pareuseureumhada]",
        "part_of_speech": "형용사 / 색채어",
        "chosung": "ㅍㄹㅅㄹㅎㄷ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "서늘한 새벽 공기나 맑은 빙하, 혹은 갓 깎은 머리칼 밑동처럼 투명하고 은은하게 푸른 기운이 감도는 색감.",
        "origin": "동틀 무렵의 서늘한 여명과 한반도 사계절의 맑은 냉기를 시각적으로 포착한 정교한 청색 표현.",
        "examples": [
            "A: 새벽 다섯 시에 창밖을 보니 하늘이 파르스름하게 밝아오고 있었어요.\nB: 그 파르스름한 새벽빛을 보면 마음이 차분해지죠."
        ],
        "tags": ["파르스름하다", "색채어", "청색", "새벽하늘", "서늘함", "K정서"],
        "likes": 6520,
        "dislikes": 12,
        "toxicity_level": 0,
        "standard_korean_mapping": "약간 푸른빛을 띠어 서늘하고 맑은 기운이 도는 상태",
        "trend_status": "SOUL",
        "sub_category": "color",
        "en": {
            "slang": "Pareuseureumhada (Subtly Ethereal Pale Cyan Tint)",
            "desc": "The translucent, cool, and serene bluish hue observed in early dawn skies, pristine ice, or fresh porcelain.",
            "ex": "The horizon was tinged with a quiet '파르스름하다' light just before sunrise."
        },
        "romanization": "pareuseureumhada",
        "phonetic_respelling": "PAH-reu-seu-reum-hah-dah"
    },
    {
        "id": 331,
        "word": "싯누렇다",
        "pronunciation": "[sinnureota]",
        "part_of_speech": "형용사 / 색채어",
        "chosung": "ㅅㄴㄹㄷ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "오래 굶주려 영양이 부족하거나 심한 탈진·질병으로 인해 얼굴이나 안색이 탁하고 짙게 누런빛을 띠는 모양.",
        "origin": "접두사 '싯-'이 붙어 탁함과 과도함을 극대화한 한국어 감각 접사 체계의 대표적 실례.",
        "examples": [
            "A: 며칠 밤샘 야근하더니 안색이 싯누렇게 떴어. 당장 병원 가 봐!\nB: 거울 보니까 진짜 싯누렇네요... 오늘은 일찍 퇴근해야겠어요."
        ],
        "tags": ["싯누렇다", "색채어", "안색", "피로", "건강", "K정서"],
        "likes": 5190,
        "dislikes": 22,
        "toxicity_level": 0,
        "standard_korean_mapping": "매우 탁하고 짙게 누렇다 (병색이나 피로의 상징)",
        "trend_status": "SOUL",
        "sub_category": "color",
        "en": {
            "slang": "Sinnureota (Sickly Jaundiced Sallow Yellow)",
            "desc": "The starkly sallow, pale, unhealthy deep yellow complexion of someone suffering severe burnout or acute exhaustion.",
            "ex": "After three consecutive all-nighters, his face had turned alarmingly '싯누렇다'."
        },
        "romanization": "sinnureota",
        "phonetic_respelling": "SHEET-noo-ruh-tah"
    },
    {
        "id": 332,
        "word": "푸르뎅뎅하다",
        "pronunciation": "[puredengdenghada]",
        "part_of_speech": "형용사 / 색채어",
        "chosung": "ㅍㄹㄷㄷㅎㄷ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "모서리에 세게 부딪쳐 짙게 피멍이 들었거나, 추위에 파랗게 질려 기분 나쁘고 얼룩덜룩하게 푸른빛이 도는 모양.",
        "origin": "불쾌하거나 병적인 청색 음영을 음성상징 접미사 '-뎅뎅'을 붙여 실감 나게 표출하는 순우리말.",
        "examples": [
            "A: 책상 모서리에 정강이를 찧었는데 푸르뎅뎅하게 멍이 올라왔어요.\nB: 앗 차가운 얼음 찜질부터 먼저 하세요!"
        ],
        "tags": ["푸르뎅뎅하다", "색채어", "멍", "피멍", "추위", "K정서"],
        "likes": 5830,
        "dislikes": 18,
        "toxicity_level": 0,
        "standard_korean_mapping": "산뜻하지 못하고 짙고 탁하게 푸른빛을 띠는 모양",
        "trend_status": "SOUL",
        "sub_category": "color",
        "en": {
            "slang": "Puredengdenghada (Livid Bruised Purplish-Blue)",
            "desc": "The unsightly, mottled bluish-purple discoloration of a deep contusion (bruise) or lips shivering in bitter cold.",
            "ex": "He stubbed his shin against the granite steps and it quickly turned '푸르뎅뎅하다'."
        },
        "romanization": "puredengdenghada",
        "phonetic_respelling": "POO-reu-deng-deng-hah-dah"
    },
    {
        "id": 333,
        "word": "발그레하다",
        "pronunciation": "[balgeurehada]",
        "part_of_speech": "형용사 / 색채어",
        "chosung": "ㅂㄱㄹㅎㄷ",
        "era": "soul",
        "era_name": "4. 💎 K-정서 (번역불가 118선+)",
        "era_period": "Untranslatable K-Soul",
        "generation": "전 세대 & 글로벌 K-컬처",
        "short_def": "수줍은 고백을 받거나 따뜻한 온천욕을 마친 후 뺨이 은은하고 사랑스럽게 연분홍빛으로 물든 모양.",
        "origin": "부끄러움과 건강한 혈색이 교차할 때 얼굴에 피어오르는 한국인 특유의 서정적 홍조 표현.",
        "examples": [
            "A: 칭찬 한마디에 볼이 발그레해지는 모습이 너무 사랑스럽더라고요.\nB: 수줍어할 때 살짝 올라오는 발그레한 홍조는 숨길 수가 없죠."
        ],
        "tags": ["발그레하다", "색채어", "홍조", "수줍음", "사랑스러움", "K정서"],
        "likes": 8740,
        "dislikes": 8,
        "toxicity_level": 0,
        "standard_korean_mapping": "엷게 붉은빛을 띠어 앙증맞고 사랑스러운 상태",
        "trend_status": "SOUL",
        "sub_category": "color",
        "en": {
            "slang": "Balgeurehada (Soft Rosy Blush)",
            "desc": "A charming, tender, and subtle flush of warmth blossoming on one's cheeks from shy embarrassment or cozy warmth.",
            "ex": "Her cheeks flushed with a sweet '발그레하다' warmth when he paid her a sincere compliment."
        },
        "romanization": "balgeurehada",
        "phonetic_respelling": "BAHL-geu-reh-hah-dah"
    }
]

words.extend(new_items)
print(f"Total words now: {len(words)}")

output = f"// MALSSAM {len(words)} Words Complete Database\nwindow.DEFAULT_WORDS = " + json.dumps(words, ensure_ascii=False, indent=2) + ";\n"

with open('data/words_db.js', 'w', encoding='utf-8') as f:
    f.write(output)

print("Saved updated data/words_db.js successfully!")
