// ============================================================
// 🎬 [말쌈 3D 숏폼 상황극 엔진: js/roleplay.js]
// - 스페인어 스타일 3D Flip Card 회전 제어
// - 6개국어(KR, EN, JA, ES, VI, ID) 자막 & Web Speech API 음성 더빙
// - onend 이벤트 기반 100% 대화 싱크 (말 끊김 제로)
// ============================================================

(function () {
  'use strict';

  let currentLang = 'ko';
  let currentScene = 0;
  let isPlaying = false;
  let isMuted = false;
  let fallbackTimer = null;
  let keepAliveInterval = null;

  // 🎴 모달 열기 / 닫기
  window.openRoleplayModal = function (wordId, ev) {
    if (ev && ev.stopPropagation) ev.stopPropagation();
    const modal = document.getElementById('roleplayModal');
    if (!modal) return;

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // 기본 언어 한국어 설정 및 씬 초기화
    setRoleplayLanguage('ko');
    flipToFront();
    currentScene = 0;
    renderScene(0);
  };

  window.closeRoleplayModal = function () {
    const modal = document.getElementById('roleplayModal');
    if (!modal) return;

    stopAudio();
    isPlaying = false;
    modal.classList.remove('active');
    document.body.style.overflow = '';
    flipToFront();
  };

  // 🌐 6개국어 전환
  window.setRoleplayLanguage = function (lang) {
    const metaMap = window.LANG_METADATA || {};
    const meta = metaMap[lang] || metaMap['ko'] || {};

    currentLang = lang;

    // 언어 버튼 활성화 UI
    document.querySelectorAll('.rp-lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // 앞면 메타데이터 갱신 (undefined 방지 및 다국어 실시간 매핑)
    const badgeEl = document.getElementById('rpFrontBadge');
    if (badgeEl) badgeEl.innerText = meta.badge || '💎 K-SOUL #01 · 번역불가 한국어';

    const titleEl = document.getElementById('rpFrontTitle');
    if (titleEl) titleEl.innerText = meta.word || '눈치';

    const pronEl = document.getElementById('rpFrontPron');
    if (pronEl) pronEl.innerText = meta.altPron ? `🗣️ ${meta.altPron}` : '🗣️ [nun-chi · NOON-chee]';

    const descEl = document.getElementById('rpFrontDesc');
    if (descEl) descEl.innerText = meta.def || '상대방의 기분, 분위기, 눈빛을 0.1초 만에 파악해 알아서 처신하는 한국 고유의 생존 본능.';

    const punchEl = document.getElementById('rpFrontPunch');
    if (punchEl) punchEl.innerText = meta.punchText ? `💡 ${meta.punchText}` : '💡 “말하지 않아도 공기를 읽는 K-직장인 생존술”';

    // 출연진 명칭 갱신
    const castDemisEl = document.getElementById('rpCastNameDemis');
    if (castDemisEl && meta.castDemis) castDemisEl.innerText = meta.castDemis;

    const castCraigEl = document.getElementById('rpCastNameCraig');
    if (castCraigEl && meta.castCraig) castCraigEl.innerText = meta.castCraig;

    const castJenniferEl = document.getElementById('rpCastNameJennifer');
    if (castJenniferEl && meta.castJennifer) castJenniferEl.innerText = meta.castJennifer;

    // 뒷면 언어 오디오 Pill
    const backLangEl = document.getElementById('rpCurrentLangPill');
    if (backLangEl) backLangEl.innerText = meta.pill || '🇰🇷 KO AUDIO';

    stopAudio();
    renderScene(currentScene);
    if (isPlaying) {
      playCurrentSceneAudio();
    }
  };

  // 🎴 3D FLIP 회전 제어
  window.flipToBackAndPlay = function () {
    const card = document.getElementById('rpFlipCardInner');
    if (card) card.classList.add('flipped');
    playShow();
  };

  window.flipToFront = function () {
    const card = document.getElementById('rpFlipCardInner');
    if (card) card.classList.remove('flipped');
    pauseShow();
  };

  // 앞면 퀵 발음 듣기
  window.speakQuickWord = function (word) {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(word || '눈치');
      u.lang = 'ko-KR';
      u.rate = 0.9;
      window.speechSynthesis.speak(u);
    }
  };

  // 씬 렌더링
  function renderScene(idx) {
    const scripts = (window.DRAMA_SCRIPTS && window.DRAMA_SCRIPTS[currentLang]) ? window.DRAMA_SCRIPTS[currentLang] : (window.DRAMA_SCRIPTS ? window.DRAMA_SCRIPTS['ko'] : []);
    if (!scripts || !scripts[idx]) return;

    const s = scripts[idx];
    const counterEl = document.getElementById('rpSceneCounter');
    if (counterEl) counterEl.innerText = `SCENE ${idx + 1} / ${scripts.length}`;

    // 액터 아바타 & 뱃지
    const avatarImg = document.getElementById('rpActorAvatar');
    if (avatarImg) avatarImg.src = s.avatar;

    const nameEl = document.getElementById('rpActorName');
    if (nameEl) nameEl.innerText = s.actor;

    const titleEl = document.getElementById('rpActorTitle');
    if (titleEl) {
      titleEl.innerText = s.title;
      titleEl.style.color = s.color || '#38bdf8';
    }

    const iconEl = document.getElementById('rpActorRoleIcon');
    if (iconEl) iconEl.innerText = s.roleIcon || '👤';

    const stickerEl = document.getElementById('rpReactionSticker');
    if (stickerEl) stickerEl.innerText = s.sticker || '✨';

    const hintEl = document.getElementById('rpActingHint');
    if (hintEl) hintEl.innerText = s.acting || '';

    const subEl = document.getElementById('rpMainSubtitle');
    if (subEl) subEl.innerText = s.dialogue || '';

    const transEl = document.getElementById('rpSubtitlesTrans');
    if (transEl) transEl.innerText = s.trans || '';

    // 애니메이션 & 시각 효과
    const stage = document.getElementById('rpCharacterStage');
    if (stage) stage.style.transform = `scale(${s.zoom || 1})`;

    const speedLines = document.getElementById('rpSpeedLines');
    if (speedLines) {
      if (s.speedLines) speedLines.classList.add('active');
      else speedLines.classList.remove('active');
    }

    const wrapper = document.getElementById('rpAvatarWrapper');
    if (wrapper) {
      wrapper.style.boxShadow = `0 0 35px ${s.color || '#ff007f'}88`;
      wrapper.style.background = `linear-gradient(135deg, ${s.color || '#ff007f'}, #ff007f)`;
    }

    const ambient = document.getElementById('rpAmbientLight');
    if (ambient) {
      ambient.style.background = `radial-gradient(circle, ${s.color || '#ff007f'}77 0%, transparent 70%)`;
    }

    const player = document.getElementById('rpCardBack');
    if (player) {
      if (s.shake) player.classList.add('rp-screen-shake');
      else player.classList.remove('rp-screen-shake');
    }

    // 프로그레스 바 게이지
    for (let i = 0; i < scripts.length; i++) {
      const fill = document.getElementById(`rpFill-${i}`);
      if (fill) {
        if (i < idx) fill.style.width = '100%';
        else if (i === idx) fill.style.width = '100%';
        else fill.style.width = '0%';
      }
    }
  }

  function stopAudio() {
    if (fallbackTimer) {
      clearTimeout(fallbackTimer);
      fallbackTimer = null;
    }
    if (keepAliveInterval) {
      clearInterval(keepAliveInterval);
      keepAliveInterval = null;
    }
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    window._activeUtterance = null;
    const sub = document.getElementById('rpMainSubtitle');
    if (sub) {
      sub.style.border = 'none';
      sub.style.boxShadow = 'none';
    }
  }

  function playCurrentSceneAudio() {
    stopAudio();
    const scripts = (window.DRAMA_SCRIPTS && window.DRAMA_SCRIPTS[currentLang]) ? window.DRAMA_SCRIPTS[currentLang] : (window.DRAMA_SCRIPTS ? window.DRAMA_SCRIPTS['ko'] : []);
    if (!scripts || !scripts[currentScene]) return;

    const s = scripts[currentScene];
    const metaMap = window.LANG_METADATA || {};
    const meta = metaMap[currentLang] || metaMap['ko'];

    const sub = document.getElementById('rpMainSubtitle');
    if (sub) {
      sub.style.border = `1.5px solid ${s.color || '#ff007f'}`;
      sub.style.borderRadius = '10px';
      sub.style.padding = '6px 10px';
      sub.style.background = 'rgba(0,0,0,0.5)';
      sub.style.boxShadow = `0 0 15px ${s.color || '#ff007f'}44`;
    }

    if (!isMuted && ('speechSynthesis' in window)) {
      const textToSpeak = s.speechText || s.dialogue;
      const u = new SpeechSynthesisUtterance(textToSpeak);
      u.lang = meta ? meta.ttsLang : 'ko-KR';
      u.rate = s.voiceRate || 1.0;
      u.pitch = s.pitch || 1.0;

      // 크롬 GC 수집 방지 전역 레퍼런스
      window._activeUtterance = u;

      // 크롬 백그라운드 침묵 방지 keep-alive 핑
      keepAliveInterval = setInterval(() => {
        if (window.speechSynthesis.speaking) {
          window.speechSynthesis.pause();
          window.speechSynthesis.resume();
        } else {
          clearInterval(keepAliveInterval);
        }
      }, 8000);

      // 🔥 핵심: 음성이 완전히 끝난 후 0.6초간 여유 호흡을 두고 다음 씬으로 전환
      u.onend = () => {
        clearInterval(keepAliveInterval);
        if (!isPlaying) return;
        fallbackTimer = setTimeout(() => {
          advanceNext();
        }, 600);
      };

      u.onerror = (e) => {
        clearInterval(keepAliveInterval);
        console.warn("SpeechSynthesis error:", e);
        if (isPlaying) {
          fallbackTimer = setTimeout(advanceNext, 4500);
        }
      };

      window.speechSynthesis.speak(u);

    } else {
      // 음소거 환경 넉넉한 읽기 시간
      const readTime = Math.max(3800, (s.dialogue || '').length * 150);
      fallbackTimer = setTimeout(() => {
        if (isPlaying) advanceNext();
      }, readTime);
    }
  }

  function advanceNext() {
    if (!isPlaying) return;
    const scripts = (window.DRAMA_SCRIPTS && window.DRAMA_SCRIPTS[currentLang]) ? window.DRAMA_SCRIPTS[currentLang] : (window.DRAMA_SCRIPTS ? window.DRAMA_SCRIPTS['ko'] : []);
    if (!scripts) return;

    currentScene++;
    if (currentScene < scripts.length) {
      renderScene(currentScene);
      playCurrentSceneAudio();
    } else {
      stopAudio();
      isPlaying = false;
      const playBtn = document.getElementById('rpBtnPlayPause');
      if (playBtn) playBtn.innerHTML = `<span>↺ 다시보기</span>`;
      currentScene = 0;
    }
  }

  window.prevRoleplayScene = function () {
    stopAudio();
    currentScene = Math.max(0, currentScene - 1);
    renderScene(currentScene);
    if (isPlaying) playCurrentSceneAudio();
  };

  window.nextRoleplayScene = function () {
    stopAudio();
    const scripts = (window.DRAMA_SCRIPTS && window.DRAMA_SCRIPTS[currentLang]) ? window.DRAMA_SCRIPTS[currentLang] : (window.DRAMA_SCRIPTS ? window.DRAMA_SCRIPTS['ko'] : []);
    if (!scripts) return;
    currentScene = (currentScene + 1) % scripts.length;
    renderScene(currentScene);
    if (isPlaying) playCurrentSceneAudio();
  };

  window.toggleRoleplayPlayPause = function () {
    if (isPlaying) {
      pauseShow();
    } else {
      playShow();
    }
  };

  function playShow() {
    isPlaying = true;
    const btn = document.getElementById('rpBtnPlayPause');
    if (btn) btn.innerHTML = `<span>⏸️ 일시정지</span>`;
    renderScene(currentScene);
    playCurrentSceneAudio();
  }

  function pauseShow() {
    isPlaying = false;
    const btn = document.getElementById('rpBtnPlayPause');
    if (btn) btn.innerHTML = `<span>▶️ 재생하기</span>`;
    stopAudio();
  }

  window.toggleRoleplayMute = function () {
    isMuted = !isMuted;
    const btn = document.getElementById('rpBtnSoundToggle');
    if (btn) btn.innerText = isMuted ? '🔇' : '🔊';
    if (isMuted) {
      stopAudio();
    } else if (isPlaying) {
      playCurrentSceneAudio();
    }
  };

  // 프로그레스 바 직접 클릭 바로가기
  window.jumpToRoleplayScene = function (idx) {
    stopAudio();
    currentScene = idx;
    renderScene(currentScene);
    if (isPlaying) {
      playCurrentSceneAudio();
    }
  };

})();
