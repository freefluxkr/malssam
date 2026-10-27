# -*- coding: utf-8 -*-
"""
Restore the exact 100% original pristine HTML layout from index_monolithic_backup.html
while preserving clean modular CSS, JS, K-Soul search, and 3D roleplay modal.
"""

with open('index_monolithic_backup.html', 'r', encoding='utf-8') as f:
    backup = f.read()

# 1. Extract original HTML body from <body> up to <script>
body_start = backup.find('<body>')
script_start = backup.find('<script', body_start)
original_body_html = backup[body_start + len('<body>'):script_start].strip()

# 2. Update K-Soul subcat section in original_body_html to include the dedicated search bar and 7 subcategories
old_subcat = '''  <!-- 💎 K-정서 전용 4대 서브 카테고리 칩 필터 바 -->
  <section class="soul-subcat-section" id="soulSubcatSection" style="display: none;">
    <div class="soul-subcat-container">
      <button class="soul-subcat-btn active" onclick="filterSoulSubcat('all', event)">
        <span>✨ 전체 K-Soul (118)</span>
      </button>
      <button class="soul-subcat-btn emotion" onclick="filterSoulSubcat('emotion', event)">
        <span>💭 1. 심리·감정 (36)</span>
      </button>
      <button class="soul-subcat-btn relationship" onclick="filterSoulSubcat('relationship', event)">
        <span>🤝 2. 관계·유대 (25)</span>
      </button>
      <button class="soul-subcat-btn behavior" onclick="filterSoulSubcat('behavior', event)">
        <span>🏃 3. 습관·행동 (25)</span>
      </button>
      <button class="soul-subcat-btn culture" onclick="filterSoulSubcat('culture', event)">
        <span>🎎 4. 사회·문화 (32)</span>
      </button>
    </div>
  </section>'''

new_subcat = '''  <!-- 💎 K-정서 전용 7대 서브 카테고리 칩 필터 바 & 메뉴 내 전용 실시간 검색창 -->
  <section class="soul-subcat-section" id="soulSubcatSection" style="display: none;">
    <!-- 💎 K-정서 전용 인라인 실시간 검색창 -->
    <div class="soul-search-wrap">
      <div class="soul-search-row">
        <span class="soul-search-icon">🔍</span>
        <input type="text" id="soulSearchInput" class="soul-search-input" 
               placeholder="💎 K-정서 단어 검색 (예: 눈치, 정, 한, 답답하다, 서운, 꼬르륵, 노르스름, nunchi, jeong...)" 
               oninput="handleSoulSearch()">
        <button type="button" id="soulSearchClearBtn" class="soul-search-clear-btn" onclick="clearSoulSearch()" title="검색어 지우기">✕</button>
      </div>
      <div class="soul-search-meta">
        <div class="soul-quick-tags">
          <span class="soul-quick-label">⚡ 빠른 검색:</span>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('눈치')">#눈치</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('정')">#정</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('한')">#한</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('답답하다')">#답답하다</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('서운하다')">#서운하다</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('꼬르륵')">#꼬르륵 (의성어)</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('아장아장')">#아장아장 (의태어)</button>
          <button type="button" class="soul-quick-chip" onclick="quickSoulSearch('노르스름하다')">#노르스름하다 (색채어)</button>
        </div>
        <span id="soulSearchStatus" class="soul-search-status">총 133선 K-SOUL 수록</span>
      </div>
    </div>

    <div class="soul-subcat-container">
      <button id="soulBtnAll" class="soul-subcat-btn active" onclick="filterSoulSubcat('all', event)">
        <span>✨ 전체 K-Soul (133)</span>
      </button>
      <button id="soulBtnEmotion" class="soul-subcat-btn emotion" onclick="filterSoulSubcat('emotion', event)">
        <span>💭 심리·감정 (36)</span>
      </button>
      <button id="soulBtnRelationship" class="soul-subcat-btn relationship" onclick="filterSoulSubcat('relationship', event)">
        <span>🤝 관계·유대 (25)</span>
      </button>
      <button id="soulBtnBehavior" class="soul-subcat-btn behavior" onclick="filterSoulSubcat('behavior', event)">
        <span>🏃 습관·행동 (25)</span>
      </button>
      <button id="soulBtnCulture" class="soul-subcat-btn culture" onclick="filterSoulSubcat('culture', event)">
        <span>🎎 사회·문화 (32)</span>
      </button>
      <button id="soulBtnOno" class="soul-subcat-btn onomatopoeia" onclick="filterSoulSubcat('onomatopoeia', event)">
        <span>🔊 의성어 (5)</span>
      </button>
      <button id="soulBtnMim" class="soul-subcat-btn mimetic" onclick="filterSoulSubcat('mimetic', event)">
        <span>✨ 의태어 (5)</span>
      </button>
      <button id="soulBtnCol" class="soul-subcat-btn color" onclick="filterSoulSubcat('color', event)">
        <span>🎨 색채어 (5)</span>
      </button>
    </div>
  </section>'''

if old_subcat in original_body_html:
    original_body_html = original_body_html.replace(old_subcat, new_subcat)
    print("Replaced soul subcategory section with enhanced version.")
else:
    print("Warning: old_subcat not matched exactly, replacing by regex...")
    import re
    original_body_html = re.sub(
        r'<section class="soul-subcat-section" id="soulSubcatSection"[\s\S]*?</section>',
        new_subcat,
        original_body_html
    )

# 3. Add 3D Flip Card Roleplay Modal HTML before toast/footer
roleplay_modal_html = '''
  <!-- 🎴 [스페인어 스타일 3D FLIP CARD 상황극 모달] -->
  <div class="roleplay-modal-overlay" id="roleplayModal" onclick="if(event.target===this)closeRoleplayModal()">
    <div class="roleplay-modal-inner">
      <button type="button" class="roleplay-modal-close-btn" onclick="closeRoleplayModal()" title="닫기">&times;</button>
      
      <!-- 🌐 6개국 언어 셀렉터 바 -->
      <div class="rp-global-lang-bar">
        <button class="rp-lang-btn active" data-lang="ko" onclick="setRoleplayLanguage('ko')">🇰🇷 한국어</button>
        <button class="rp-lang-btn" data-lang="en" onclick="setRoleplayLanguage('en')">🇺🇸 English</button>
        <button class="rp-lang-btn" data-lang="ja" onclick="setRoleplayLanguage('ja')">🇯🇵 日本語</button>
        <button class="rp-lang-btn" data-lang="es" onclick="setRoleplayLanguage('es')">🇪🇸 Español</button>
        <button class="rp-lang-btn" data-lang="vi" onclick="setRoleplayLanguage('vi')">🇻🇳 Tiếng Việt</button>
        <button class="rp-lang-btn" data-lang="id" onclick="setRoleplayLanguage('id')">🇮🇩 Indonesia</button>
      </div>

      <!-- 3D FLIP CARD 스테이지 -->
      <div class="rp-flip-stage-container">
        <div class="rp-flip-card-inner" id="rpFlipCardInner">
          
          <!-- [앞면: 3D 네온 단어 카드] -->
          <div class="rp-flip-face rp-card-front" id="rpCardFront">
            <div class="rp-front-top-row">
              <span class="rp-k-soul-badge" id="rpFrontBadge">💎 K-SOUL #202 · 3D 플립 카드</span>
              <span class="rp-flip-hint-badge">3D INTERACTIVE</span>
            </div>

            <div>
              <h2 class="rp-front-word-title" id="rpFrontTitle">눈치</h2>
              <div class="rp-front-pron-bar">
                <span class="rp-pron-pill" id="rpFrontPron">🗣️ [nun-chi · NOON-chee]</span>
                <span class="rp-pron-alt">명사 / 사회적 초능력</span>
                <button class="rp-btn-quick-audio" onclick="speakQuickWord('눈치')" title="원어민 발음 듣기">🔊</button>
              </div>

              <div class="rp-front-desc-box" id="rpFrontDesc">
                말하지 않아도 침묵 속의 공기와 타인의 표정·행간을 5G 속도로 직관 감지하여 매끄럽게 처신하는 한국인의 고유한 사회적 레이더.
              </div>

              <div class="rp-punchline-card" id="rpFrontPunch">
                💡 "팀장님의 급발진 주말 등산 회식을 0.1초 만에 차단하는 마법!"
              </div>
            </div>

            <!-- DMDG 어벤져스 출연진 (Rule 2: width="65" 준수) -->
            <div class="rp-cast-preview-box">
              <div class="rp-cast-header">
                <span>DMDG 어벤져스 드라마 1화</span>
                <span>15초 숏폼</span>
              </div>
              <div class="rp-cast-avatar-row">
                <div class="rp-cast-avatar-item">
                  <img src="assets/agents/demis_profile.png" width="65" class="rp-cast-avatar-img" alt="Demis">
                  <span class="rp-cast-avatar-name" id="rpCastNameDemis">Demis (팀장)</span>
                </div>
                <div class="rp-cast-avatar-item">
                  <img src="assets/agents/craig_profile.png" width="65" class="rp-cast-avatar-img" alt="Craig">
                  <span class="rp-cast-avatar-name" id="rpCastNameCraig">Craig (풀스택)</span>
                </div>
                <div class="rp-cast-avatar-item">
                  <img src="assets/agents/jennifer_profile.png" width="65" class="rp-cast-avatar-img" alt="Jennifer">
                  <span class="rp-cast-avatar-name" id="rpCastNameJennifer">Jennifer (UX)</span>
                </div>
              </div>
            </div>

            <button class="rp-btn-fiesta-flip" onclick="flipToBackAndPlay()">
              <span>🎴 3D 회전 상황극 보기 ↺</span>
            </button>
          </div>

          <!-- [뒷면: 3D 숏폼 비디오 시뮬레이터] -->
          <div class="rp-flip-face rp-card-back" id="rpCardBack">
            <!-- 인스타 스토리 5단 진행 바 -->
            <div class="rp-story-progress-container">
              <div class="rp-story-progress-segment" onclick="jumpToRoleplayScene(0)"><div class="rp-story-progress-fill" id="rpFill-0"></div></div>
              <div class="rp-story-progress-segment" onclick="jumpToRoleplayScene(1)"><div class="rp-story-progress-fill" id="rpFill-1"></div></div>
              <div class="rp-story-progress-segment" onclick="jumpToRoleplayScene(2)"><div class="rp-story-progress-fill" id="rpFill-2"></div></div>
              <div class="rp-story-progress-segment" onclick="jumpToRoleplayScene(3)"><div class="rp-story-progress-fill" id="rpFill-3"></div></div>
              <div class="rp-story-progress-segment" onclick="jumpToRoleplayScene(4)"><div class="rp-story-progress-fill" id="rpFill-4"></div></div>
            </div>

            <!-- 백 페이스 탑 바 -->
            <div class="rp-back-top-bar">
              <button class="rp-btn-flip-back" onclick="flipToFront()"><span>↺ 단어로</span></button>
              <span class="rp-current-lang-pill" id="rpCurrentLangPill">🇰🇷 한국어</span>
              <button id="rpBtnSoundToggle" class="rp-btn-sound-toggle" onclick="toggleRoleplayMute()">🔊</button>
            </div>

            <!-- 메인 비디오 스테이지 -->
            <div class="rp-video-stage">
              <div class="rp-speed-lines" id="rpSpeedLines"></div>
              <div class="rp-stage-ambient-light" id="rpAmbientLight"></div>

              <div class="rp-character-stage" id="rpCharacterStage">
                <div class="rp-character-avatar-wrapper" id="rpAvatarWrapper">
                  <img id="rpActorAvatar" src="assets/agents/demis_profile.png" width="65" class="rp-character-avatar-img" alt="Actor">
                  <span id="rpReactionSticker" class="rp-reaction-sticker">☕</span>
                </div>
                <div class="rp-actor-badge">
                  <span id="rpActorRoleIcon">👔</span>
                  <strong id="rpActorName">데미스</strong>
                  <span id="rpActorTitle" class="rp-actor-title">총괄부장</span>
                </div>
              </div>

              <div id="rpActingHint" class="rp-acting-direction-box">(따뜻한 인자한 미소로 커피를 마시며)</div>
            </div>

            <!-- 자막 영역 -->
            <div class="rp-subtitles-container">
              <div id="rpMainSubtitle" class="rp-main-subtitle">"얘들아! 이번 주 토요일 아침 6시에 북한산 등산하고 삼계탕에 낮술 어때?"</div>
              <div id="rpSubtitlesTrans" class="rp-subtitles-trans">Demis: 이번 주 토요일 아침 6시 북한산 등산 어때? 삼계탕 쏜다!</div>
            </div>

            <!-- 하단 플레이어 컨트롤 -->
            <div class="rp-bottom-controls">
              <button class="rp-ctrl-btn" onclick="prevRoleplayScene()">⏮️ 이전</button>
              <button id="rpBtnPlayPause" class="rp-btn-play-pause" onclick="toggleRoleplayPlayPause()"><span>⏸️ 일시정지</span></button>
              <button class="rp-ctrl-btn" onclick="nextRoleplayScene()">⏭️ 다음</button>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
'''

toast_idx = original_body_html.find('<!-- 토스트 알림 -->')
if toast_idx != -1:
    original_body_html = original_body_html[:toast_idx] + roleplay_modal_html + '\n  ' + original_body_html[toast_idx:]
else:
    original_body_html += roleplay_modal_html

# 4. Assemble complete clean index.html
complete_html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>말쌈 (MALSSAM) - 3대 세대별 한국어 신조어 사전 & 세대 공감 배틀</title>
  
  <!-- SEO & 메타 태그 -->
  <meta name="description" content="1990년대 PC통신 라떼 감성부터 2026 최신 영포티·영ㅋㅋ 밈, K-정서 118선까지 전 세대를 잇는 실시간 한국어 신조어 아카이브">
  <meta name="keywords" content="신조어, 한국어유행어, 라떼신조어, 2026밈, 영포티, 영ㅋㅋ, 꼰대, 럭키비키, 중꺾마, 알잘딱깔센, 번역불가한국어">
  <meta property="og:title" content="말쌈 (MALSSAM) - 세대 간 소통 단절 극복 프로젝트">
  <meta property="og:description" content="부모와 자녀, 팀장님과 신입사원이 함께 즐기는 세대공감 퀴즈 & 318선 신조어 사전">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://malssam.com/">
  
  <script src="js/anti-scraping.js?v=20261023_shield_fix"></script>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📖</text></svg>">

  <!-- 🎨 모듈화 CSS: 말쌈 디자인 시스템 & 3D 상황극 스타일 -->
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/roleplay.css">

  <!-- 포트원 (PortOne v2 브라우저 SDK) -->
  <script src="https://cdn.portone.io/v2/browser-sdk.js"></script>
  <script src="https://cdn.iamport.kr/v1/iamport.js"></script>
  <!-- PayPal SDK (등록된 라이브 Client ID) -->
  <script src="https://www.paypal.com/sdk/js?client-id=AaYtg54hxqwI7fn87ym2M28kTDOl7NQ1RZJUjdX0tIutj048JX2TovDkCWytSy8K-B9lIpcf7_IHDA-c&currency=USD"></script>
  
  <!-- Firebase Firestore 클라우드 실시간 DB -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
  <script>
    const firebaseConfig = {{
      projectId: "dmdg-live",
      appId: "1:357433220336:web:1a8914811da09123a0f635",
      storageBucket: "dmdg-live.firebasestorage.app",
      apiKey: "AIzaSyBcS8aS5yHk2KFNYPImXslsFkSyoBwYrKI",
      authDomain: "dmdg-live.firebaseapp.com",
      messagingSenderId: "357433220336"
    }};

    let firestoreDb = null;
    let isFirebaseReady = false;

    try {{
      if (typeof firebase !== 'undefined') {{
        if (!firebase.apps.length) {{
          firebase.initializeApp(firebaseConfig);
        }}
        firestoreDb = firebase.firestore();
        isFirebaseReady = true;
        console.log("🔥 Firebase Firestore connected successfully (asia-northeast3 / dmdg-live)");
      }}
    }} catch (e) {{
      console.warn("Firebase initialization warning:", e);
    }}

    window.loadFirestoreWords = async function() {{
      if (!isFirebaseReady || !firestoreDb) return [];
      try {{
        const snapshot = await firestoreDb.collection("malssam_words").get();
        const fbWords = [];
        snapshot.forEach(doc => {{
          const d = doc.data();
          fbWords.push({{
            id: 'fb_' + doc.id,
            docId: doc.id,
            isFirestore: true,
            word: d.word,
            pronunciation: d.pronunciation || ('[' + d.word + ']'),
            part_of_speech: d.part_of_speech || "신조어",
            chosung: d.chosung || "",
            era: d.era || "shorts",
            era_name: d.era_name || "3. ⚡ 요즘 1020 밈 (쇼츠/릴스/틱톡)",
            generation: d.generation || "사용자 제보 세대",
            short_def: d.short_def || "",
            origin: d.origin || "사용자 실시간 등록",
            examples: d.examples || [d.example || ""],
            tags: d.tags || ["실시간커뮤니티"],
            likes: Number(d.likes) || 1,
            dislikes: Number(d.dislikes) || 0,
            author: d.author || "익명",
            toxicity_level: d.toxicity_level || 1,
            standard_korean_mapping: d.standard_korean_mapping || "실시간 등록어",
            trend_status: "HOT"
          }});
        }});
        return fbWords;
      }} catch (err) {{
        console.warn("Firestore fetch error:", err);
        return [];
      }}
    }};
  </script>
</head>
<body>
{original_body_html}

  <!-- ============================================================
       📦 [클린 모듈화 시스템: 데이터 & 기능별 분리 스크립트]
       ============================================================ -->
  <!-- 1. 데이터 모듈 (333단어, 15대 밸런스 배틀, 10대 카톡 안건, 3D 상황극 DB) -->
  <script src="data/words_db.js"></script>
  <script src="data/battle_questions.js"></script>
  <script src="data/kakao_cards.js"></script>
  <script src="data/roleplay_db.js"></script>

  <!-- 2. 기능별 독립 JS 모듈 -->
  <script src="js/audio.js"></script>
  <script src="js/render.js"></script>
  <script src="js/battle.js"></script>
  <script src="js/quiz.js"></script>
  <script src="js/kakao.js"></script>
  <script src="js/payments.js"></script>
  <script src="js/roleplay.js"></script>

  <!-- 3. 메인 앱 초기화 모듈 -->
  <script src="js/app.js"></script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(complete_html)

print("Restored original HTML layout with modular structure successfully!")
