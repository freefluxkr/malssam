# 💎 [말쌈 / MALSSAM.com] v9.0.0 글로벌 발음 기호 & 음성 TTS 엔진 릴리즈 보고서

- **일시**: 2026년 10월 27일 22:45 (KST)
- **주제**: 전 세계 K-컬처 팬 및 한국어 학습자를 위한 318개 전 단어 글로벌 발음 기호(로마자/영문 직관 표기) 및 원어민 Web Speech TTS 엔진 정식 탑재
- **주관**: DMDG 어벤져스 팀
- **서비스 URL**: https://malssam.com

---

## 1. 📌 개발 배경 및 사장님 제안
사장님의 **"글로벌 사이트들에는 각 단어 발음 기호도 붙여주면 좋을 것 같은데..."**라는 혜안에 따라, 한글을 읽지 못하는 외국인도 소리 내어 한국어를 학습하고 즐길 수 있도록 **3단계 글로벌 발음 시스템**을 전격 개발·배포 완료.

---

## 2. 🌐 3단계 글로벌 발음 시스템 구축 내역

1. **표준 로마자(RR) 표기**:
   - 국립국어원 표준 로마자 표기법(Revised Romanization)을 318개 전 단어에 자동 생성 및 정밀 보정 (예: `눈치` ➔ `[nunchi]`, `정` ➔ `[jeong]`, `개운하다` ➔ `[gaeunhada]`).
2. **영미권 직관 발음 가이드 (Phonetic Respelling)**:
   - 영미권 화자가 보고 즉각 정확한 음절 강세로 발음할 수 있는 대문자 하이픈 발음 표기 주입 (예: `[NOON-chee]`, `[JUNG]`, `[GEH-oon-hah-dah]`, `[DAHP-dahp-hah-dah]`).
3. **🔊 원클릭 원어민 음성 재생 엔진 (Web Speech API)**:
   - 각 단어 카드 표제어 옆에 `[🔊]` 버튼 탑재.
   - 클릭 시 브라우저 내장 한국어 TTS(`ko-KR`) 엔진이 0.01초 만에 또렷한 원어민 발음으로 음성 출력.
   - 재생 중 핑크 네온 사운드 링 펄스 애니메이션(`btn-sound-speak.speaking`) 시각 피드백 제공.

---

## 3. 🛠️ 기술 반영 및 파일 동기화
1. `words_db.json`: `v9.0.0` 판올림, `romanization` 및 `phonetic_respelling` 필드 318개 전수 반영.
2. `index.html`: Web Speech API `speakWord()` 함수 탑재, 로컬스토리지 캐시 키 `malssam_words_v9` 갱신.
3. `DMDG_LIVE/10_korean_urban_dictionary`: 양대 폴더 100% 동기화.
4. GitHub Pages (`https://github.com/freefluxkr/malssam.git`): 커밋 & 푸시 완료.
