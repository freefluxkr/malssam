// ============================================================
// 🏢 [K-오피스 생존 연구소 (K-Office Survival Lab) 모듈]
// ============================================================

const KOFFICE_NEP_DATA = {
  '넵': {
    reply: '넵! 지금 바로 확인하겠습니다.',
    title: '💎 [넵]의 심리학: 사회화 완료 200%의 생존어',
    desc: "'네'는 차갑고 '넹'은 가벼워서 탄생한 기적의 단어. 상사의 기분을 거스르지 않으면서 가장 안전하고 신속한 피드백을 전달하는 한국 직장인의 필수 생존어입니다."
  },
  '네!': {
    reply: '네! 준비 다 되었습니다!',
    title: '⚡ [네!]의 심리학: 의욕 넘치는 신입 모드',
    desc: "느낌표를 붙여 밝고 긍정적인 에너지를 뿜어냅니다. 하지만 1년 차가 넘어가면 타이핑 에너지 고갈로 자연스럽게 '넵'으로 수렴하게 됩니다."
  },
  '네': {
    reply: '네. 확인했습니다.',
    title: '🧊 [네.]의 심리학: 분노와 피로의 경계선',
    desc: "마침표가 찍힌 단호한 '네.'는 상대방에게 '내가 지금 화가 났거나 매우 지쳤다'는 무언의 신호를 줍니다. 상사가 이 답장을 받으면 살짝 긴장하게 됩니다."
  },
  '넹': {
    reply: '넹~ 바로 보내드릴게요 ㅎㅎ',
    title: '🌱 [넹]의 심리학: 친밀한 동기 전용 언어',
    desc: "친한 동기나 사수에게만 허용되는 애교 섞인 어투입니다. 부장님이나 임원 단톡방에 보냈다가는 1초 만에 등골이 오싹해질 수 있습니다."
  }
};

const KOFFICE_EXCUSES = [
  '"[긴급] 어머니: 집 보일러에 누수가 생겨서 아랫집에 물이 샌다는데 당장 와서 밸브 좀 확인해 봐라!"',
  '"[택배기사]: 냉동 신선식품이 문 앞에 배송되었는데 날이 더워 1시간 내로 냉동고에 넣으셔야 합니다."',
  '"[알림]: 내일 오전 8시 본사 대면 회의 자료 사전 검토 요청 (마감: 자정)"',
  '"[동생]: 집에 강아지가 문을 열고 탈출한 것 같아. 빨리 와서 같이 찾아봐야 해!"'
];

let kofficeTimerRunning = false;
let kofficeSecondsLeft = 2700;
let kofficeTimerInterval = null;
let kofficeLastExcuseIdx = 0;
let kofficeLastScore = null;
let kofficeLastGrade = '';

function stopKOfficeTimer() {
  if (kofficeTimerInterval) {
    clearInterval(kofficeTimerInterval);
    kofficeTimerInterval = null;
  }
  kofficeTimerRunning = false;
  kofficeSecondsLeft = 2700;
}

function renderKOfficeLab() {
  stopKOfficeTimer();

  const container = document.getElementById('wordsContainer');
  if (!container) return;

  const titleEl = document.getElementById('feedTitleText');
  if (titleEl) titleEl.innerText = '🏢 K-오피스 생존 연구소 (K-Office Survival Lab)';
  const badgeEl = document.getElementById('feedCountBadge');
  if (badgeEl) badgeEl.innerText = '3종 시뮬레이터';

  container.innerHTML = `
    <div class="ko-lab-wrapper">
      <div class="ko-lab-header">
        <div>
          <div class="ko-lab-badge">🔥 말쌈 × Book 21746 공식 인터랙티브 랩</div>
          <h2 class="ko-lab-title">K-오피스 생존 연구소</h2>
          <p class="ko-lab-subtitle">꼰대력 테스트 · 넵(Nep) 감정 번역기 · 회식 틈새 탈출 타이머</p>
        </div>
        <a href="k_office_lab.html" class="ko-lab-fullpage-link">↗ 전용 페이지로 크게 보기</a>
      </div>

      <div class="ko-lab-tabs">
        <button type="button" class="ko-lab-tab-btn active" onclick="switchKOfficeSubTab('quiz', this)">
          <span class="ko-lab-emoji">👔</span>
          <span>꼰대력 진단</span>
        </button>
        <button type="button" class="ko-lab-tab-btn" onclick="switchKOfficeSubTab('nep', this)">
          <span class="ko-lab-emoji">💬</span>
          <span>넵 감정 번역기</span>
        </button>
        <button type="button" class="ko-lab-tab-btn" onclick="switchKOfficeSubTab('escape', this)">
          <span class="ko-lab-emoji">🏃‍♂️</span>
          <span>회식 탈출 타이머</span>
        </button>
      </div>

      <!-- Panel 1: 꼰대력 진단 -->
      <div id="ko-panel-quiz" class="ko-lab-panel active">
        <div class="ko-lab-panel-title">
          <span>📊</span>
          <span>당신의 오피스 꼰대력 &amp; 라떼 지수 진단기</span>
        </div>

        <form id="ko-quiz-form">
          <div class="ko-lab-question">
            <div class="ko-lab-q-title">Q1. 신입사원이 출근 시간 8시 59분에 도착했을 때 나의 첫 생각은?</div>
            <div class="ko-lab-opts">
              <label class="ko-lab-opt"><input type="radio" name="ko_q1" value="0" checked> 제시간에 맞게 잘 도착했네.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q1" value="10"> 최소 10분 전에는 와서 커피도 마시고 준비해야 하는 것 아닌가?</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q1" value="25"> 우리 때는 30분 전에 와서 선배들 책상 닦았는데... 요즘 애들은 참 편해.</label>
            </div>
          </div>

          <div class="ko-lab-question">
            <div class="ko-lab-q-title">Q2. 후배가 퇴근 시간인 18시 00분에 노트북을 닫고 일어설 때?</div>
            <div class="ko-lab-opts">
              <label class="ko-lab-opt"><input type="radio" name="ko_q2" value="0" checked> 고생했어! 즐거운 저녁 보내길.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q2" value="10"> 오늘 하던 일은 마무리 다 하고 가는 건가 살짝 궁금하다.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q2" value="25"> 팀장이 아직 일하고 있는데 눈치도 없이 칼퇴하네?</label>
            </div>
          </div>

          <div class="ko-lab-question">
            <div class="ko-lab-q-title">Q3. 부서 회식 메뉴를 정할 때 나의 행동 패턴은?</div>
            <div class="ko-lab-opts">
              <label class="ko-lab-opt"><input type="radio" name="ko_q3" value="0" checked> 막내에게 예산만 알려주고 먹고 싶은 곳 예약하게 한다.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q3" value="10"> "아무거나 괜찮아"라고 해놓고 삼겹살에 소주 쪽으로 은근히 유도한다.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q3" value="25"> "회식은 무조건 1차 삼겹살, 2차 호프집이지!" 단골집으로 직행한다.</label>
            </div>
          </div>

          <div class="ko-lab-question">
            <div class="ko-lab-q-title">Q4. 후배가 슬랙/카톡으로 "네" 대신 "넵"이나 이모지를 보낼 때?</div>
            <div class="ko-lab-opts">
              <label class="ko-lab-opt"><input type="radio" name="ko_q4" value="0" checked> 친근하고 즉각적인 답장이라 마음이 편하다.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q4" value="10"> 크게 상관은 없지만 이메일엔 좀 더 정중했으면 좋겠다.</label>
              <label class="ko-lab-opt"><input type="radio" name="ko_q4" value="25"> "네"라고 딱딱하게 하거나 가볍게 답장하면 예의가 없다고 느낀다.</label>
            </div>
          </div>

          <button type="button" class="ko-lab-btn" onclick="calculateKOfficeKondae()">내 꼰대력 점수 확인하기</button>
        </form>

        <div id="ko-quiz-result" class="ko-lab-result">
          <div class="ko-lab-score-circle">
            <div class="ko-lab-score-val" id="ko-score-text">0</div>
            <div class="ko-lab-score-unit">/ 100점</div>
          </div>
          <div class="ko-lab-result-grade" id="ko-grade-text">완벽한 MZ 천사 동료</div>
          <div class="ko-lab-result-desc" id="ko-desc-text">꼰대 지수 0%! 당신은 글로벌 IT 테크 기업에서도 사랑받을 열린 마인드의 소유자입니다.</div>
          <button type="button" class="ko-lab-share-btn" onclick="shareKOfficeKondae()">📢 내 꼰대력 점수 공유하기</button>
        </div>
      </div>

      <!-- Panel 2: 넵 감정 번역기 -->
      <div id="ko-panel-nep" class="ko-lab-panel">
        <div class="ko-lab-panel-title">
          <span>💬</span>
          <span>글자 하나로 갈리는 '넵병(Nep Syndrome)' 실시간 판독기</span>
        </div>

        <div class="ko-lab-chat">
          <div class="ko-lab-bubble ko-lab-bubble-boss">
            김대리님, 오늘 부탁드린 시장 분석 보고서 17시까지 가능할까요?
          </div>
          <div class="ko-lab-bubble ko-lab-bubble-reply" id="ko-preview-reply">
            넵! 지금 바로 확인하겠습니다.
          </div>
        </div>

        <div class="ko-lab-picker-label">답변 뉘앙스 선택해보기:</div>
        <div class="ko-lab-nep-grid">
          <button type="button" class="ko-lab-nep-btn selected" onclick="pickKOfficeNep('넵', this)">넵</button>
          <button type="button" class="ko-lab-nep-btn" onclick="pickKOfficeNep('네!', this)">네!</button>
          <button type="button" class="ko-lab-nep-btn" onclick="pickKOfficeNep('네', this)">네.</button>
          <button type="button" class="ko-lab-nep-btn" onclick="pickKOfficeNep('넹', this)">넹~</button>
        </div>

        <div class="ko-lab-analysis">
          <div class="ko-lab-analysis-title" id="ko-nep-type">💎 [넵]의 심리학: 사회화 완료 200%의 생존어</div>
          <div class="ko-lab-analysis-text" id="ko-nep-desc">
            '네'는 차갑고 '넹'은 가벼워서 탄생한 기적의 단어. 상사의 기분을 거스르지 않으면서 가장 안전하고 신속한 피드백을 전달하는 한국 직장인의 필수 생존어입니다.
          </div>
        </div>
      </div>

      <!-- Panel 3: 회식 탈출 타이머 -->
      <div id="ko-panel-escape" class="ko-lab-panel">
        <div class="ko-lab-panel-title">
          <span>🏃‍♂️</span>
          <span>회식 1차 틈새 탈출 카운트다운 &amp; 비상 탈출 메시지</span>
        </div>

        <div class="ko-lab-timer-box">
          <div class="ko-lab-timer-sub">1차 고깃집에서 2차로 이동하는 골든타임</div>
          <div class="ko-lab-time" id="ko-escape-timer">00:45:00</div>
          <div class="ko-lab-timer-actions">
            <button type="button" class="ko-lab-btn ko-lab-timer-btn" id="ko-timer-toggle-btn" onclick="toggleKOfficeTimer(this)">타이머 시작</button>
            <button type="button" class="ko-lab-btn-secondary" onclick="resetKOfficeTimer()">초기화</button>
          </div>
        </div>

        <div class="ko-lab-sms">
          <div class="ko-lab-sms-header">
            <span>🚨 [비상 탈출용 자동 알림 템플릿]</span>
            <span>오후 8:45</span>
          </div>
          <div class="ko-lab-sms-content" id="ko-sms-text">${KOFFICE_EXCUSES[0]}</div>
        </div>
        <button type="button" class="ko-lab-btn-secondary ko-lab-btn-full" onclick="refreshKOfficeSms()">
          🔄 다른 핑계 템플릿 생성하기
        </button>
      </div>

      <!-- Footer Banner -->
      <div class="ko-lab-wikidocs">
        <div class="ko-lab-wb-text">
          <h3>📖 더 깊은 K-오피스 생존술이 궁금하다면?</h3>
          <p>위키독스 공식 연재 《K-오피스 생존 바이블》(Book 21746) 전 16개 챕터 열람</p>
        </div>
        <a href="https://wikidocs.net/book/21746" target="_blank" rel="noopener" class="ko-lab-wb-btn">위키독스 무료 읽기 →</a>
      </div>
    </div>
  `;
}

function switchKOfficeSubTab(tab, btn) {
  document.querySelectorAll('.ko-lab-tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.ko-lab-panel').forEach(p => p.classList.remove('active'));

  if (btn) btn.classList.add('active');

  const target = document.getElementById(`ko-panel-${tab}`);
  if (target) target.classList.add('active');
}

function calculateKOfficeKondae() {
  const form = document.getElementById('ko-quiz-form');
  if (!form) return;

  let total = 0;
  ['ko_q1', 'ko_q2', 'ko_q3', 'ko_q4'].forEach(q => {
    const val = form.querySelector(`input[name="${q}"]:checked`);
    if (val) total += parseInt(val.value, 10);
  });

  const box = document.getElementById('ko-quiz-result');
  const scoreText = document.getElementById('ko-score-text');
  const gradeText = document.getElementById('ko-grade-text');
  const descText = document.getElementById('ko-desc-text');

  if (scoreText) scoreText.innerText = total;

  let grade = '';
  let desc = '';
  if (total <= 20) {
    grade = '🌟 완벽한 젠틀 동료 (청정 구역)';
    desc = '꼰대 지수 최저! 상대방의 자율성과 시간을 극도로 존중하는 최고의 팀메이트입니다.';
  } else if (total <= 50) {
    grade = '☕ 영포티 낀 세대 (조심 단계)';
    desc = "마음은 열려 있으나, 나도 모르게 '우리 때는 말이야'가 목 끝까지 차오르는 낀 세대 감성입니다.";
  } else if (total <= 75) {
    grade = '⚠️ 은밀한 마이크로매니저 (경보)';
    desc = "조직의 룰을 지나치게 엄격하게 적용하여 후배들이 당신 앞에서 '넵병'에 걸리기 직전입니다.";
  } else {
    grade = '🚨 살아있는 조선시대 참모총장 (적색경보)';
    desc = "신속히 《K-오피스 생존 바이블》 02장 '꼰대의 7가지 유형학'을 정독하여 자아 성찰이 필요합니다!";
  }

  kofficeLastScore = total;
  kofficeLastGrade = grade;

  if (gradeText) gradeText.innerText = grade;
  if (descText) descText.innerText = desc;
  if (box) {
    box.style.display = 'block';
    box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

function shareKOfficeKondae() {
  const score = kofficeLastScore !== null ? kofficeLastScore : 0;
  const grade = kofficeLastGrade || '🌟 완벽한 젠틀 동료 (청정 구역)';
  const shareText = `[말쌈 × K-오피스 생존 연구소] 나의 꼰대력 진단 점수: ${score}점 (${grade})\n꼰대력 테스트 · 넵 번역기 · 회식 탈출 타이머 👉 https://malssam.com/#k-office`;

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(shareText).then(() => {
      if (typeof showToast === 'function') {
        showToast('🔗 꼰대력 진단 결과와 말쌈 링크가 클립보드에 복사되었습니다!');
      }
    }).catch(() => {
      if (typeof showToast === 'function') showToast('클립보드 복사에 실패했습니다.');
    });
  } else if (typeof showToast === 'function') {
    showToast('공유하기를 지원하지 않는 브라우저입니다.');
  }
}

function pickKOfficeNep(type, btn) {
  document.querySelectorAll('.ko-lab-nep-btn').forEach(b => b.classList.remove('selected'));
  if (btn) btn.classList.add('selected');

  const d = KOFFICE_NEP_DATA[type];
  if (!d) return;

  const replyEl = document.getElementById('ko-preview-reply');
  const typeEl = document.getElementById('ko-nep-type');
  const descEl = document.getElementById('ko-nep-desc');
  if (replyEl) replyEl.innerText = d.reply;
  if (typeEl) typeEl.innerText = d.title;
  if (descEl) descEl.innerText = d.desc;
}

function toggleKOfficeTimer(btn) {
  if (!kofficeTimerRunning) {
    kofficeTimerRunning = true;
    btn.innerText = '일시정지';
    btn.classList.add('running');
    kofficeTimerInterval = setInterval(() => {
      const timerEl = document.getElementById('ko-escape-timer');
      if (!timerEl) {
        stopKOfficeTimer();
        return;
      }
      if (kofficeSecondsLeft > 0) {
        kofficeSecondsLeft--;
        const m = String(Math.floor(kofficeSecondsLeft / 60)).padStart(2, '0');
        const s = String(kofficeSecondsLeft % 60).padStart(2, '0');
        timerEl.innerText = `00:${m}:${s}`;
      } else {
        stopKOfficeTimer();
        timerEl.innerText = '00:45:00';
        btn.innerText = '타이머 시작';
        btn.classList.remove('running');
        alert('🚨 1차 종료 골든타임 도달! 지금 신발 끈 묶고 지하철역으로 달리세요!');
      }
    }, 1000);
  } else {
    kofficeTimerRunning = false;
    btn.innerText = '타이머 재개';
    btn.classList.remove('running');
    if (kofficeTimerInterval) {
      clearInterval(kofficeTimerInterval);
      kofficeTimerInterval = null;
    }
  }
}

function resetKOfficeTimer() {
  stopKOfficeTimer();
  const timerEl = document.getElementById('ko-escape-timer');
  const btn = document.getElementById('ko-timer-toggle-btn');
  if (timerEl) timerEl.innerText = '00:45:00';
  if (btn) {
    btn.innerText = '타이머 시작';
    btn.classList.remove('running');
  }
}

function refreshKOfficeSms() {
  let idx = Math.floor(Math.random() * KOFFICE_EXCUSES.length);
  if (KOFFICE_EXCUSES.length > 1 && idx === kofficeLastExcuseIdx) {
    idx = (idx + 1) % KOFFICE_EXCUSES.length;
  }
  kofficeLastExcuseIdx = idx;
  const smsEl = document.getElementById('ko-sms-text');
  if (smsEl) smsEl.innerText = KOFFICE_EXCUSES[idx];
}

function openKOfficeTab() {
  if (typeof switchEra === 'function') {
    switchEra('koffice');
  }
  if (history && history.replaceState) {
    history.replaceState(null, '', '#k-office');
  }
  const infoBox = document.getElementById('eraInfoBox');
  if (infoBox) {
    infoBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}
