// AWS Certified AI Business Strategist (AIB-C01) Unified Portal & CBT Controller

class PortalApp {
  constructor() {
    this.currentTab = 'overview';
    this.cbtQuestions = [];
    this.cbtCurrentIndex = 0;
    this.cbtUserAnswers = {};
    this.cbtFlagged = new Set();
    this.cbtChecked = new Set();
    this.cbtMode = 'study';
    this.cbtKoreanVisible = false;
    this.cbtTimerInterval = null;
    this.cbtSecondsLeft = 0;
    this.serverOnline = false;

    this.initDOM();
    this.initMarkdownContent();
    this.bindEvents();
    this.checkServerStatus();
  }

  initDOM() {
    // 서버 상태 뱃지
    this.serverStatusBox = document.getElementById('server-status-box');
    this.serverStatusText = document.getElementById('server-status-text');
    this.statusIndicatorDot = document.querySelector('.status-indicator-dot');
    this.cbtHistorySection = document.getElementById('cbt-history-section');
    this.cbtHistoryTableContainer = document.getElementById('cbt-history-table-container');
    // 탭 버튼 및 패널
    this.navTabs = document.querySelectorAll('.nav-tab');
    this.tabPanels = document.querySelectorAll('.tab-panel');
    this.highlightCbtBtn = document.querySelector('.highlight-cbt');

    // 용어사전 검색
    this.glossarySearchInput = document.getElementById('glossary-search');
    this.glossaryClearBtn = document.getElementById('glossary-clear-btn');
    this.glossaryContentDiv = document.getElementById('glossary-content');

    // CBT 컴포넌트
    this.cbtTimerBox = document.getElementById('cbt-timer-box');
    this.cbtTimeDisplay = document.getElementById('cbt-time-display');
    this.cbtStartScreen = document.getElementById('cbt-start-screen');
    this.cbtExamScreen = document.getElementById('cbt-exam-screen');
    this.cbtResultScreen = document.getElementById('cbt-result-screen');

    this.cbtStartBtn = document.getElementById('cbt-start-btn');
    this.cbtQIndex = document.getElementById('cbt-q-index');
    this.cbtQDomain = document.getElementById('cbt-q-domain');
    this.cbtFlagBtn = document.getElementById('cbt-flag-btn');
    this.cbtFlagLabel = document.getElementById('cbt-flag-label');
    this.cbtTransBtn = document.getElementById('cbt-trans-btn');

    this.cbtQTextEn = document.getElementById('cbt-q-text-en');
    this.cbtQTextKr = document.getElementById('cbt-q-text-kr');
    this.cbtOptionsList = document.getElementById('cbt-options-list');

    this.cbtFeedbackBox = document.getElementById('cbt-feedback-box');
    this.cbtFeedbackBadge = document.getElementById('cbt-feedback-badge');
    this.cbtFeedbackTitle = document.getElementById('cbt-feedback-title');
    this.cbtFeedbackConceptTag = document.getElementById('cbt-feedback-concept-tag');
    this.cbtFeedbackDetail = document.getElementById('cbt-feedback-detail');

    this.cbtPrevBtn = document.getElementById('cbt-prev-btn');
    this.cbtNextBtn = document.getElementById('cbt-next-btn');
    this.cbtCheckAnsBtn = document.getElementById('cbt-check-ans-btn');
    this.cbtSubmitBtn = document.getElementById('cbt-submit-btn');

    this.cbtPaletteGrid = document.getElementById('cbt-palette-grid');
    this.cbtStatTotal = document.getElementById('cbt-stat-total');
    this.cbtStatAnswered = document.getElementById('cbt-stat-answered');
    this.cbtStatUnanswered = document.getElementById('cbt-stat-unanswered');
    this.cbtStatFlagged = document.getElementById('cbt-stat-flagged');

    // CBT 결과
    this.cbtPassFail = document.getElementById('cbt-pass-fail');
    this.cbtResultMeta = document.getElementById('cbt-result-meta');
    this.cbtScaledScore = document.getElementById('cbt-scaled-score');
    this.cbtAccuracy = document.getElementById('cbt-accuracy');
    this.cbtCorrectCount = document.getElementById('cbt-correct-count');
    this.cbtTimeSpentText = document.getElementById('cbt-time-spent');
    this.cbtDomainList = document.getElementById('cbt-domain-list');

    this.cbtReviewAllBtn = document.getElementById('cbt-review-all-btn');
    this.cbtReviewWrongBtn = document.getElementById('cbt-review-wrong-btn');
    this.cbtRestartBtn = document.getElementById('cbt-restart-btn');
    this.cbtHistorySection = document.getElementById('cbt-history-section');
    this.cbtHistoryTableContainer = document.getElementById('cbt-history-table-container');
    this.cbtClearHistoryBtn = document.getElementById('cbt-clear-history-btn');
  }

  // 견고한 Fallback 마크다운 파서 (오프라인 및 CDN 지연 완벽 지원)
  parseMarkdownFallback(text) {
    if (!text) return '';
    let html = text.replace(/\r\n/g, '\n');

    // 1. 임시 보존할 태그 마스킹
    html = html
      .replace(/<div class="bilingual-grid">/gi, '___BILINGUAL_GRID_START___')
      .replace(/<div class="en-col">/gi, '___EN_COL_START___')
      .replace(/<div class="kr-col">/gi, '___KR_COL_START___')
      .replace(/<\/div>/gi, '___DIV_END___')
      .replace(/<span class="lang-badge en">/gi, '___LANG_EN_START___')
      .replace(/<span class="lang-badge kr">/gi, '___LANG_KR_START___')
      .replace(/<\/span>/gi, '___SPAN_END___')
      .replace(/<br\s*\/?>/gi, '___BR_TAG___');

    // 2. 코드 블록 선처리
    html = html.replace(/```([\s\S]*?)```/g, (match, code) => {
      const escaped = code.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      return `<pre><code>${escaped.trim()}</code></pre>`;
    });

    // 3. HTML 특수문자 이스케이프
    html = html
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    // 4. 마스킹 태그 복원
    html = html
      .replace(/___BILINGUAL_GRID_START___/g, '<div class="bilingual-grid">')
      .replace(/___EN_COL_START___/g, '<div class="en-col">')
      .replace(/___KR_COL_START___/g, '<div class="kr-col">')
      .replace(/___DIV_END___/g, '</div>')
      .replace(/___LANG_EN_START___/g, '<span class="lang-badge en">')
      .replace(/___LANG_KR_START___/g, '<span class="lang-badge kr">')
      .replace(/___SPAN_END___/g, '</span>')
      .replace(/___BR_TAG___/g, '<br>');

    // 5. 인라인 코드 및 링크 처리
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

    // 6. 헤더 및 수평선
    html = html.replace(/^### (.*$)/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.*$)/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.*$)/gm, '<h1>$1</h1>');
    html = html.replace(/^---$/gm, '<hr>');

    // 7. 인용구 (&gt; 로 이스케이프된 것 포함)
    html = html.replace(/^(&gt;|>)\s*(.*$)/gm, '<blockquote>$2</blockquote>');

    // 8. 글자 강조 (Bold / Italic)
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');

    // 9. 리스트 처리
    html = html.replace(/^[\*\-]\s+(.*$)/gm, '<li>$1</li>');

    // 10. 마크다운 테이블 처리
    const lines = html.split('\n');
    let inTable = false;
    let tableHtml = '';
    const newLines = [];

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line.startsWith('|') && line.endsWith('|')) {
        // 테이블 구분행 (| :--- | :--- | 또는 | --- |) 무시
        if (/^\|(\s*:?-+:?\s*\|)+$/.test(line)) {
          continue;
        }
        if (!inTable) {
          inTable = true;
          tableHtml = '<table><thead>';
          const cols = line.split('|').slice(1, -1);
          tableHtml += '<tr>' + cols.map(c => `<th>${c.trim()}</th>`).join('') + '</tr></thead><tbody>';
        } else {
          const cols = line.split('|').slice(1, -1);
          tableHtml += '<tr>' + cols.map(c => `<td>${c.trim()}</td>`).join('') + '</tr>';
        }
      } else {
        if (inTable) {
          inTable = false;
          tableHtml += '</tbody></table>';
          newLines.push(tableHtml);
        }
        newLines.push(lines[i]);
      }
    }
    if (inTable) {
      tableHtml += '</tbody></table>';
      newLines.push(tableHtml);
    }

    return newLines.join('\n').replace(/\n\n+/g, '<p></p>');
  }

  renderMarkdown(text) {
    if (typeof marked !== 'undefined' && typeof marked.parse === 'function') {
      try {
        return marked.parse(text);
      } catch (e) {
        console.warn('marked.parse failed, using fallback', e);
      }
    }
    return this.parseMarkdownFallback(text);
  }

  initMarkdownContent() {
    const docs = (typeof window !== 'undefined' && window.PORTAL_DOCS) ? window.PORTAL_DOCS : (typeof PORTAL_DOCS !== 'undefined' ? PORTAL_DOCS : null);
    if (!docs) return;

    const mapping = {
      'overview-content': docs.overview || docs.exam_guide,
      'glossary-content': docs.glossary,
      'domain1-content': docs.domain1,
      'domain2-content': docs.domain2,
      'domain3-content': docs.domain3,
      'domain4-content': docs.domain4,
      'domain5-content': docs.domain5,
      'aws_services-content': docs.aws_services
    };

    Object.keys(mapping).forEach(elId => {
      const el = document.getElementById(elId);
      if (el && mapping[elId]) {
        try {
          el.innerHTML = this.renderMarkdown(mapping[elId]);
        } catch (e) {
          console.error('Error rendering markdown for', elId, e);
        }
      }
    });

    // CDN 지연 로드 대응: window load 시 marked가 뒤늦게 준비되었으면 고품질 렌더링으로 갱신
    if (typeof window !== 'undefined') {
      window.addEventListener('load', () => {
        if (typeof marked !== 'undefined' && typeof marked.parse === 'function') {
          Object.keys(mapping).forEach(elId => {
            const el = document.getElementById(elId);
            if (el && mapping[elId]) {
              try {
                el.innerHTML = marked.parse(mapping[elId]);
              } catch (e) {}
            }
          });
        }
      });
    }
  }

  bindEvents() {
    // 탭 전환 이벤트
    this.navTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const targetTab = tab.dataset.tab;
        this.switchTab(targetTab);
      });
    });

    if (this.highlightCbtBtn) {
      this.highlightCbtBtn.addEventListener('click', () => {
        this.switchTab('cbt');
      });
    }

    // 용어사전 검색 필터
    if (this.glossarySearchInput) {
      this.glossarySearchInput.addEventListener('input', (e) => {
        this.filterGlossary(e.target.value.toLowerCase().trim());
      });
      this.glossaryClearBtn.addEventListener('click', () => {
        this.glossarySearchInput.value = '';
        this.filterGlossary('');
      });
    }

    // CBT 이벤트
    this.cbtStartBtn.addEventListener('click', () => this.handleStartCbt());
    this.cbtPrevBtn.addEventListener('click', () => this.navigateCbt(-1));
    this.cbtNextBtn.addEventListener('click', () => this.navigateCbt(1));
    this.cbtTransBtn.addEventListener('click', () => this.toggleCbtTranslation());
    this.cbtFlagBtn.addEventListener('click', () => this.toggleCbtFlag());
    this.cbtCheckAnsBtn.addEventListener('click', () => this.checkCbtAnswer());
    this.cbtSubmitBtn.addEventListener('click', () => this.confirmSubmitCbt());

    this.cbtReviewAllBtn.addEventListener('click', () => this.reviewCbt(false));
    this.cbtReviewWrongBtn.addEventListener('click', () => this.reviewCbt(true));
    this.cbtRestartBtn.addEventListener('click', () => this.resetCbtToStart());
    if (this.cbtClearHistoryBtn) {
      this.cbtClearHistoryBtn.addEventListener('click', () => this.clearHistory());
    }
  }

  switchTab(tabKey) {
    this.currentTab = tabKey;
    this.navTabs.forEach(t => {
      t.classList.toggle('active', t.dataset.tab === tabKey);
    });
    this.tabPanels.forEach(p => {
      p.classList.toggle('active', p.id === `tab-${tabKey}`);
    });

    // CBT 탭일 때와 아닐 때 타이머 헤더 노출 제어
    if (tabKey === 'cbt' && this.cbtExamScreen.classList.contains('active')) {
      this.cbtTimerBox.classList.remove('hidden');
    } else {
      this.cbtTimerBox.classList.add('hidden');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  filterGlossary(query) {
    if (!this.glossaryContentDiv) return;
    const tables = this.glossaryContentDiv.querySelectorAll('table');
    tables.forEach(table => {
      const rows = table.querySelectorAll('tbody tr');
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        if (!query || text.includes(query)) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  }

  // ==========================================
  // CBT 엔진 로직
  // ==========================================

  // Fisher-Yates 배열 셔플 유틸리티
  shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // 문항 내 보기(A~D) 순서 셔플 및 정답 키 동적 재매핑
  randomizeQuestionOptions(question) {
    const q = JSON.parse(JSON.stringify(question));
    if (!Array.isArray(q.options) || q.options.length < 2) return q;

    const isMultiple = Array.isArray(q.correct_answer);
    const origCorrect = isMultiple ? new Set(q.correct_answer) : new Set([q.correct_answer]);

    // 각 옵션의 원래 정답 여부 태깅
    const tagged = q.options.map(opt => ({
      opt: { ...opt },
      isCorrect: origCorrect.has(opt.key)
    }));

    const shuffled = this.shuffleArray(tagged);
    const keyLetters = ['A', 'B', 'C', 'D', 'E', 'F'];
    const newCorrect = [];

    shuffled.forEach((item, idx) => {
      const letter = keyLetters[idx];
      item.opt.key = letter;
      if (item.isCorrect) {
        newCorrect.push(letter);
      }
    });

    q.options = shuffled.map(item => item.opt);
    q.correct_answer = isMultiple ? newCorrect.sort() : (newCorrect[0] || q.correct_answer);
    return q;
  }

  // 중복 출제 방지: 카테고리/문제 타입별 1문항씩 추출하는 스마트 샘플링
  sampleDistinctByCategory(pool, count) {
    if (!pool || pool.length === 0) return [];

    // 1. 문제 타입/카테고리별로 문항 그룹화
    const categoryMap = new Map();
    pool.forEach(q => {
      let cat = q.topic_category;
      if (!cat && q.key_concept) {
        cat = q.key_concept.split(',')[0].trim();
      }
      if (!cat) cat = q.id;

      if (!categoryMap.has(cat)) {
        categoryMap.set(cat, []);
      }
      categoryMap.get(cat).push(q);
    });

    // 2. 카테고리 순서를 셔플하여 매회 다양한 분야가 골고루 선정되도록 보장
    const categories = this.shuffleArray(Array.from(categoryMap.keys()));

    const selected = [];
    const usedQuestionIds = new Set();

    // 3. 1차 패스: 각 카테고리(문제 타입)당 최대 1문항씩만 엄격히 추출 (중복 출제 원천 차단)
    for (const cat of categories) {
      if (selected.length >= count) break;
      const catQuestions = this.shuffleArray(categoryMap.get(cat));
      const chosen = catQuestions.find(q => !usedQuestionIds.has(q.id));
      if (chosen) {
        selected.push(chosen);
        usedQuestionIds.add(chosen.id);
      }
    }

    // 4. 요청 문항수가 카테고리 수보다 많은 경우 예외 보충 (중복 ID 없이)
    if (selected.length < count) {
      const remaining = this.shuffleArray(pool.filter(q => !usedQuestionIds.has(q.id)));
      for (const q of remaining) {
        if (selected.length >= count) break;
        selected.push(q);
        usedQuestionIds.add(q.id);
      }
    }

    // 5. 최종 추출된 문항들의 출제 순서 셔플
    return this.shuffleArray(selected);
  }

  async handleStartCbt() {
    const setInput = document.querySelector('input[name="cbtSet"]:checked');
    const modeInput = document.querySelector('input[name="cbtMode"]:checked');
    const scopeInput = document.querySelector('input[name="cbtRandomScope"]:checked');
    const selectedSet = setInput ? setInput.value : 'mock1';
    const selectedMode = modeInput ? modeInput.value : 'study';
    const selectedScope = scopeInput ? scopeInput.value : 'sample';

    let rawQuestions = [];
    const source = (typeof window !== 'undefined' && window.EXAM_DATA) ? window.EXAM_DATA : (typeof EXAM_DATA !== 'undefined' ? EXAM_DATA : null);

    if (source) {
      if (selectedScope === 'canonical') {
        // 기본 출제: 셔플 없이 공식 순서 그대로 출제
        if (selectedSet === 'mock1') {
          rawQuestions = JSON.parse(JSON.stringify(source.mock1 || []));
        } else if (source[selectedSet]) {
          rawQuestions = JSON.parse(JSON.stringify((source[selectedSet] || []).slice(0, 15)));
        }
      } else if (selectedSet === 'mock1') {
        // AWS 공식 가이드 비중에 맞춘 65문항 중복 없는 카테고리별 추출 (D1:13, D2:16, D3:18, D4:9, D5:9)
        const d1 = this.sampleDistinctByCategory(source.domain1 || [], 13);
        const d2 = this.sampleDistinctByCategory(source.domain2 || [], 16);
        const d3 = this.sampleDistinctByCategory(source.domain3 || [], 18);
        const d4 = this.sampleDistinctByCategory(source.domain4 || [], 9);
        const d5 = this.sampleDistinctByCategory(source.domain5 || [], 9);
        rawQuestions = this.shuffleArray([...d1, ...d2, ...d3, ...d4, ...d5]);
      } else if (source[selectedSet]) {
        const pool = source[selectedSet] || [];
        if (selectedScope === 'full') {
          rawQuestions = this.shuffleArray(pool); // 도메인 300문항 전체 순서 셔플
        } else {
          // 카테고리(문제 타입)별 1문항씩 중복 없이 15문항 균등 추출
          rawQuestions = this.sampleDistinctByCategory(pool, 15);
        }
      }
    }

    if (!rawQuestions || rawQuestions.length === 0) {
      // 서버 API 폴백 시도
      try {
        const res = await fetch(`/api/questions?set=${selectedSet}`);
        if (res.ok) {
          const data = await res.json();
          const fetched = data.questions || [];
          if (selectedScope === 'canonical') {
            rawQuestions = (selectedSet === 'mock1') ? fetched : fetched.slice(0, 15);
          } else if (selectedSet === 'mock1') {
            rawQuestions = this.sampleDistinctByCategory(fetched, 60);
          } else if (selectedScope === 'full') {
            rawQuestions = this.shuffleArray(fetched);
          } else {
            rawQuestions = this.sampleDistinctByCategory(fetched, 15);
          }
        }
      } catch (e) {
        console.warn('API question load failed, checking fallback...', e);
      }
    }

    if (!rawQuestions || rawQuestions.length === 0) {
      alert('문제 데이터를 로드할 수 없습니다. 페이지를 새로고침(F5) 해주세요.');
      return;
    }

    // 기본 출제(canonical) 모드인 경우 보기 셔플 없이 원본 그대로 출제, 그 외 모드는 보기(A~D) 셔플
    const questions = (selectedScope === 'canonical')
      ? rawQuestions
      : rawQuestions.map(q => this.randomizeQuestionOptions(q));

    this.startCbtSession(questions, selectedMode);
  }

  startCbtSession(questionList, mode = 'study', keepAnswers = false) {
    this.cbtQuestions = questionList;
    this.cbtCurrentIndex = 0;
    this.cbtMode = mode;
    this.isReviewMode = keepAnswers;

    if (!keepAnswers) {
      this.cbtUserAnswers = {};
      this.cbtFlagged = new Set();
      this.cbtChecked = new Set();
      this.cbtKoreanVisible = false;
      this.cbtSecondsLeft = (selectedSet === 'mock1') ? 7200 : (this.cbtQuestions.length * 110);
      this.cbtTimeSpent = 0;
      this.cbtSubmitBtn.textContent = '시험 제출 (Submit) ✔';
      this.cbtSubmitBtn.className = 'btn btn-primary';

      // 모드 설정
      if (this.cbtMode === 'study') {
        this.cbtCheckAnsBtn.classList.remove('hidden');
      } else {
        this.cbtCheckAnsBtn.classList.add('hidden');
        this.cbtFeedbackBox.classList.add('hidden');
      }
    } else {
      // 복습/리뷰 모드
      this.cbtKoreanVisible = true;
      this.cbtTransBtn.textContent = '🌐 영어 원문만 보기';
      this.cbtChecked = new Set(this.cbtQuestions.map(q => q.id));
      this.cbtCheckAnsBtn.classList.add('hidden');
      this.cbtSubmitBtn.textContent = '📊 결과 리포트로 돌아가기';
      this.cbtSubmitBtn.className = 'btn btn-info';
    }

    try {
      this.cbtStartScreen.classList.remove('active');
      this.cbtResultScreen.classList.remove('active');
      this.cbtExamScreen.classList.add('active');

      if (!this.isReviewMode) {
        this.cbtTimerBox.classList.remove('hidden');
        this.startCbtTimer();
      } else {
        this.cbtTimerBox.classList.add('hidden');
        clearInterval(this.cbtTimerInterval);
      }

      // 화면 최상단으로 강제 이동
      window.scrollTo(0, 0);

      this.renderCbtPalette();
      this.renderCbtQuestion();
      this.updateCbtSummary();
    } catch (err) {
      console.error('CBT Session start error:', err);
      alert('CBT 화면 로드 중 오류가 발생했습니다: ' + err.message);
    }
  }

  startCbtTimer() {
    clearInterval(this.cbtTimerInterval);
    this.updateTimerText();

    this.cbtTimerInterval = setInterval(() => {
      this.cbtTimeSpent++;
      if (this.cbtMode === 'exam') {
        this.cbtSecondsLeft--;
        if (this.cbtSecondsLeft <= 0) {
          clearInterval(this.cbtTimerInterval);
          alert('시험 시간이 종료되었습니다! 시험이 자동 제출됩니다.');
          this.submitCbt();
          return;
        }
      }
      this.updateTimerText();
    }, 1000);
  }

  updateTimerText() {
    const displaySec = this.cbtMode === 'exam' ? this.cbtSecondsLeft : this.cbtTimeSpent;
    const mins = Math.floor(displaySec / 60);
    const secs = displaySec % 60;
    this.cbtTimeDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  renderCbtPalette() {
    this.cbtPaletteGrid.innerHTML = '';
    this.cbtQuestions.forEach((q, idx) => {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.textContent = idx + 1;
      btn.id = `portal-pal-btn-${idx}`;

      btn.addEventListener('click', () => {
        this.cbtCurrentIndex = idx;
        this.renderCbtQuestion();
      });

      this.cbtPaletteGrid.appendChild(btn);
    });
    this.updateCbtPaletteStatus();
  }

  updateCbtPaletteStatus() {
    this.cbtQuestions.forEach((q, idx) => {
      const btn = document.getElementById(`portal-pal-btn-${idx}`);
      if (!btn) return;

      btn.classList.remove('cur', 'done', 'flag');

      if (idx === this.cbtCurrentIndex) {
        btn.classList.add('cur');
      }

      if (this.isReviewMode) {
        const userAns = this.cbtUserAnswers[q.id];
        const isMultiple = Array.isArray(q.correct_answer);
        const isCorrect = isMultiple
          ? (Array.isArray(userAns) && userAns.length === q.correct_answer.length && userAns.every((val, i) => val === q.correct_answer[i]))
          : (userAns === q.correct_answer);
        if (isCorrect) {
          btn.classList.add('done');
        } else {
          btn.classList.add('flag');
        }
      } else {
        const ans = this.cbtUserAnswers[q.id];
        if (ans && (Array.isArray(ans) ? ans.length > 0 : true)) {
          btn.classList.add('done');
        }

        if (this.cbtFlagged.has(q.id)) {
          btn.classList.add('flag');
        }
      }
    });
  }

  renderCbtQuestion() {
    const q = this.cbtQuestions[this.cbtCurrentIndex];
    if (!q) return;

    this.cbtQIndex.textContent = `Question ${this.cbtCurrentIndex + 1} of ${this.cbtQuestions.length}`;
    this.cbtQDomain.textContent = q.domain || 'General';

    // 플래그 버튼
    if (this.cbtFlagged.has(q.id)) {
      this.cbtFlagBtn.classList.add('btn-warning');
      this.cbtFlagBtn.classList.remove('btn-outline');
      this.cbtFlagLabel.textContent = '플래그 해제';
    } else {
      this.cbtFlagBtn.classList.remove('btn-warning');
      this.cbtFlagBtn.classList.add('btn-outline');
      this.cbtFlagLabel.textContent = '검토 표시 (Flag)';
    }

    // 지문 텍스트
    this.cbtQTextEn.textContent = q.question_en;
    this.cbtQTextKr.textContent = q.question_kr;
    if (this.cbtKoreanVisible) {
      this.cbtQTextKr.classList.remove('hidden');
    } else {
      this.cbtQTextKr.classList.add('hidden');
    }

    // 선지 렌더링
    const isMultiple = Array.isArray(q.correct_answer);
    this.cbtOptionsList.innerHTML = '';
    const currentSelected = this.cbtUserAnswers[q.id] || (isMultiple ? [] : null);

    q.options.forEach(opt => {
      const isSelected = isMultiple
        ? currentSelected.includes(opt.key)
        : currentSelected === opt.key;

      const item = document.createElement('div');
      item.className = `cbt-option-item ${isSelected ? 'selected' : ''}`;

      if ((this.cbtChecked.has(q.id) && this.cbtMode === 'study') || this.isReviewMode) {
        const isCorrect = isMultiple
          ? q.correct_answer.includes(opt.key)
          : q.correct_answer === opt.key;
        if (isCorrect) item.classList.add('correct');
        else if (isSelected && !isCorrect) item.classList.add('incorrect');
      }

      item.innerHTML = `
        <div class="cbt-opt-ctrl">
          <input type="${isMultiple ? 'checkbox' : 'radio'}" name="portal_opt" value="${opt.key}" ${isSelected ? 'checked' : ''} ${this.isReviewMode ? 'disabled' : ''}>
        </div>
        <div class="cbt-opt-content">
          <div class="cbt-opt-en"><strong>(${opt.key})</strong> ${opt.text_en}</div>
          <div class="cbt-opt-kr ${this.cbtKoreanVisible ? '' : 'hidden'}">${opt.text_kr}</div>
        </div>
      `;

      item.addEventListener('click', () => {
        this.selectCbtOption(q, opt.key, isMultiple);
      });

      this.cbtOptionsList.appendChild(item);
    });

    // 이전/다음 버튼
    this.cbtPrevBtn.disabled = this.cbtCurrentIndex === 0;
    this.cbtNextBtn.disabled = this.cbtCurrentIndex === this.cbtQuestions.length - 1;

    // 학습 모드 또는 리뷰 모드 피드백
    if ((this.cbtMode === 'study' && this.cbtChecked.has(q.id)) || this.isReviewMode) {
      this.displayCbtFeedback(q);
    } else {
      this.cbtFeedbackBox.classList.add('hidden');
    }

    this.updateCbtPaletteStatus();
    this.updateCbtSummary();
  }

  selectCbtOption(q, key, isMultiple) {
    if (this.isReviewMode) return; // 리뷰 모드에서는 기존 제출 정답 변경 방지

    if (isMultiple) {
      let current = this.cbtUserAnswers[q.id] || [];
      if (!Array.isArray(current)) current = [current];

      if (current.includes(key)) {
        current = current.filter(k => k !== key);
      } else {
        current.push(key);
      }
      this.cbtUserAnswers[q.id] = current.sort();
    } else {
      this.cbtUserAnswers[q.id] = key;
    }

    if (this.cbtMode === 'study' && this.cbtChecked.has(q.id)) {
      this.displayCbtFeedback(q);
    }

    this.renderCbtQuestion();
  }

  toggleCbtTranslation() {
    this.cbtKoreanVisible = !this.cbtKoreanVisible;
    this.cbtTransBtn.textContent = this.cbtKoreanVisible
      ? '🌐 영어 원문만 보기'
      : '🌐 한국어 번역 토글';
    this.renderCbtQuestion();
  }

  toggleCbtFlag() {
    const q = this.cbtQuestions[this.cbtCurrentIndex];
    if (this.cbtFlagged.has(q.id)) {
      this.cbtFlagged.delete(q.id);
    } else {
      this.cbtFlagged.add(q.id);
    }
    this.renderCbtQuestion();
  }

  navigateCbt(delta) {
    const newIdx = this.cbtCurrentIndex + delta;
    if (newIdx >= 0 && newIdx < this.cbtQuestions.length) {
      this.cbtCurrentIndex = newIdx;
      this.renderCbtQuestion();
    }
  }

  checkCbtAnswer() {
    const q = this.cbtQuestions[this.cbtCurrentIndex];
    this.cbtChecked.add(q.id);
    this.displayCbtFeedback(q);
    this.renderCbtQuestion();
  }

  displayCbtFeedback(q) {
    const userAns = this.cbtUserAnswers[q.id];
    const isMultiple = Array.isArray(q.correct_answer);

    let isCorrect = false;
    if (isMultiple) {
      isCorrect = Array.isArray(userAns) &&
        userAns.length === q.correct_answer.length &&
        userAns.every((val, idx) => val === q.correct_answer[idx]);
    } else {
      isCorrect = userAns === q.correct_answer;
    }

    const myChoiceText = userAns ? (Array.isArray(userAns) ? userAns.join(', ') : userAns) : '미선택';
    const correctChoiceText = Array.isArray(q.correct_answer) ? q.correct_answer.join(', ') : q.correct_answer;

    this.cbtFeedbackBox.classList.remove('hidden', 'correct', 'wrong');
    if (isCorrect) {
      this.cbtFeedbackBox.classList.add('correct');
      this.cbtFeedbackBadge.className = 'badge badge-navy';
      this.cbtFeedbackBadge.style.backgroundColor = 'var(--success)';
      this.cbtFeedbackBadge.style.color = 'white';
      this.cbtFeedbackBadge.textContent = '정답입니다! 🎉';
      this.cbtFeedbackTitle.textContent = `내가 선택한 정답: (${myChoiceText})`;
    } else {
      this.cbtFeedbackBox.classList.add('wrong');
      this.cbtFeedbackBadge.className = 'badge';
      this.cbtFeedbackBadge.style.backgroundColor = 'var(--danger)';
      this.cbtFeedbackBadge.style.color = 'white';
      this.cbtFeedbackBadge.textContent = '오답입니다 ⚠️';
      this.cbtFeedbackTitle.textContent = `내가 선택한 답: (${myChoiceText}) | 정답: (${correctChoiceText})`;
    }

    this.cbtFeedbackConceptTag.textContent = q.key_concept || 'AWS AI Strategy';
    this.cbtFeedbackDetail.textContent = q.explanation_kr;
  }

  updateCbtSummary() {
    const total = this.cbtQuestions.length;
    let answered = 0;
    this.cbtQuestions.forEach(q => {
      const a = this.cbtUserAnswers[q.id];
      if (a && (Array.isArray(a) ? a.length > 0 : true)) answered++;
    });

    this.cbtStatTotal.textContent = total;
    this.cbtStatAnswered.textContent = answered;
    this.cbtStatUnanswered.textContent = total - answered;
    this.cbtStatFlagged.textContent = this.cbtFlagged.size;
  }

  confirmSubmitCbt() {
    if (this.isReviewMode) {
      // 복습 모드에서 클릭하면 다시 결과 리포트 화면으로 복귀
      this.cbtExamScreen.classList.remove('active');
      this.cbtResultScreen.classList.add('active');
      return;
    }
    const total = this.cbtQuestions.length;
    let answered = 0;
    this.cbtQuestions.forEach(q => {
      const a = this.cbtUserAnswers[q.id];
      if (a && (Array.isArray(a) ? a.length > 0 : true)) answered++;
    });

    const unanswered = total - answered;
    let msg = `총 ${total}문항 중 ${answered}문항을 풀었습니다.`;
    if (unanswered > 0) {
      msg += `\n아직 ${unanswered}문항이 미응답 상태입니다. 그래도 제출하시겠습니까?`;
    } else {
      msg += '\n모든 문제를 완료했습니다. 시험을 제출하시겠습니까?';
    }

    if (confirm(msg)) {
      this.submitCbt();
    }
  }

  submitCbt() {
    clearInterval(this.cbtTimerInterval);

    let correctCount = 0;
    const domainStats = {};

    this.cbtQuestions.forEach(q => {
      const domKey = q.domain || 'Domain Other';
      if (!domainStats[domKey]) {
        domainStats[domKey] = { total: 0, correct: 0, name: q.domain_name || domKey };
      }
      domainStats[domKey].total++;

      const userAns = this.cbtUserAnswers[q.id];
      const isMultiple = Array.isArray(q.correct_answer);

      let isCorrect = false;
      if (isMultiple) {
        isCorrect = Array.isArray(userAns) &&
          userAns.length === q.correct_answer.length &&
          userAns.every((val, idx) => val === q.correct_answer[idx]);
      } else {
        isCorrect = userAns === q.correct_answer;
      }

      if (isCorrect) {
        correctCount++;
        domainStats[domKey].correct++;
      }
    });

    const total = this.cbtQuestions.length;
    const accuracy = total > 0 ? (correctCount / total) * 100 : 0;
    const scaled = Math.round(100 + (accuracy / 100) * 900);
    const passed = scaled >= 700;

    this.cbtPassFail.className = `result-badge ${passed ? 'pass' : 'fail'}`;
    this.cbtPassFail.textContent = passed ? 'PASSED (합격)' : 'FAILED (불합격)';

    this.cbtScaledScore.textContent = `${scaled} / 1000`;
    this.cbtAccuracy.textContent = `${Math.round(accuracy)}%`;
    this.cbtCorrectCount.textContent = `${correctCount} / ${total} 정답`;

    const mins = Math.floor(this.cbtTimeSpent / 60);
    const secs = this.cbtTimeSpent % 60;
    this.cbtTimeSpentText.textContent = `${mins}분 ${secs}초`;

    const avgSec = total > 0 ? Math.round(this.cbtTimeSpent / total) : 0;
    this.cbtResultMeta.textContent = `총 문항: ${total}문항 | 합격 기준: 700점 | 평균 응시 속도: 문항당 ${avgSec}초`;

    // 도메인별 성적 리스트
    this.cbtDomainList.innerHTML = '';
    Object.keys(domainStats).sort().forEach(dom => {
      const stat = domainStats[dom];
      const domPct = Math.round((stat.correct / stat.total) * 100);

      let fillClass = 'high';
      if (domPct < 60) fillClass = 'low';
      else if (domPct < 75) fillClass = 'medium';

      const domItem = document.createElement('div');
      domItem.className = 'domain-item';
      domItem.style.marginBottom = '1rem';
      domItem.innerHTML = `
        <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem; font-weight:600;">
          <span><strong>${dom}</strong>: ${stat.name}</span>
          <span>${stat.correct} / ${stat.total} (${domPct}%)</span>
        </div>
        <div style="height:10px; background:#e2e8f0; border-radius:5px; overflow:hidden;">
          <div style="height:100%; width:${domPct}%; background:${domPct >= 75 ? 'var(--success)' : (domPct >= 60 ? 'var(--warning)' : 'var(--danger)')};"></div>
        </div>
      `;
      this.cbtDomainList.appendChild(domItem);
    });

    // 시험 결과 저장 (서버 연동 또는 localStorage 정적 브라우저 저장)
    // 시험 결과 저장 (서버 연동 또는 localStorage 정적 브라우저 저장)
    const selectedSet = document.querySelector('input[name="cbtSet"]:checked')?.value || 'mock1';
    const wrongQuestionIds = [];
    this.cbtQuestions.forEach(q => {
      const userAns = this.cbtUserAnswers[q.id];
      const isMultiple = Array.isArray(q.correct_answer);
      let isCorrect = false;
      if (isMultiple) {
        isCorrect = Array.isArray(userAns) &&
          userAns.length === q.correct_answer.length &&
          userAns.every((val, idx) => val === q.correct_answer[idx]);
      } else {
        isCorrect = userAns === q.correct_answer;
      }
      if (!isCorrect) wrongQuestionIds.push(q.id);
    });

    const resultRecord = {
      timestamp: new Date().toISOString().replace('T', ' ').substring(0, 19),
      set: selectedSet,
      mode: this.cbtMode,
      total: total,
      correct_count: correctCount,
      accuracy: Math.round(accuracy),
      scaled_score: scaled,
      passed: passed,
      time_spent_seconds: this.cbtTimeSpent,
      domain_stats: domainStats,
      wrong_question_ids: wrongQuestionIds
    };

    try {
      const localHist = JSON.parse(localStorage.getItem('aib_cbt_history') || '[]');
      localHist.unshift(resultRecord);
      localStorage.setItem('aib_cbt_history', JSON.stringify(localHist.slice(0, 20)));
    } catch (e) {}

    if (this.serverOnline) {
      fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          set: selectedSet,
          mode: this.cbtMode,
          user_answers: this.cbtUserAnswers,
          time_spent_seconds: this.cbtTimeSpent,
          client_evaluated: resultRecord
        })
      }).then(res => res.json()).then(data => {
        console.log('Exam result saved to local server:', data);
      }).catch(err => console.warn('Failed to save result to server', err));
    }

    this.cbtExamScreen.classList.remove('active');
    this.cbtResultScreen.classList.add('active');
    this.cbtTimerBox.classList.add('hidden');
  }

  reviewCbt(wrongOnly = false) {
    let reviewList = this.cbtQuestions;
    if (wrongOnly) {
      reviewList = this.cbtQuestions.filter(q => {
        const userAns = this.cbtUserAnswers[q.id];
        const isMultiple = Array.isArray(q.correct_answer);
        if (isMultiple) {
          return !(Array.isArray(userAns) &&
            userAns.length === q.correct_answer.length &&
            userAns.every((val, idx) => val === q.correct_answer[idx]));
        } else {
          return userAns !== q.correct_answer;
        }
      });

      if (reviewList.length === 0) {
        alert('틀린 문제가 없습니다! 모든 문제를 맞추셨습니다 👏');
        return;
      }
    }

    // 답안 보존 모드로 복습 세션 시작 (keepAnswers = true)
    this.startCbtSession(reviewList, 'study', true);
  }

  async checkServerStatus() {
    try {
      const res = await fetch('/api/status', { cache: 'no-store' });
      if (res.ok) {
        const data = await res.json();
        this.serverOnline = true;
        if (this.statusIndicatorDot) {
          this.statusIndicatorDot.className = 'status-indicator-dot online';
        }
        if (this.serverStatusText) {
          this.serverStatusText.textContent = `로컬 서버 온라인 (${data.total_exams_taken}회 응시 기록됨)`;
        }
        this.loadExamHistory();
      } else {
        throw new Error('Not ok');
      }
    } catch (e) {
      this.serverOnline = false;
      if (this.statusIndicatorDot) {
        this.statusIndicatorDot.className = 'status-indicator-dot online';
      }
      if (this.serverStatusText) {
        this.serverStatusText.textContent = '웹 정적 호스팅 모드 (GitHub Pages / Cloudflare)';
      }
      this.loadExamHistory();
    }
  }

  async loadExamHistory() {
    if (this.serverOnline) {
      try {
        const res = await fetch('/api/history', { cache: 'no-store' });
        if (res.ok) {
          const data = await res.json();
          const history = data.history || [];
          this.renderHistoryTable(history);
          return;
        }
      } catch (e) {}
    }

    // localStorage 폴백
    try {
      const localHist = JSON.parse(localStorage.getItem('aib_cbt_history') || '[]');
      this.renderHistoryTable(localHist);
    } catch (e) {}
  }

  renderHistoryTable(history) {
    if (!this.cbtHistorySection || !this.cbtHistoryTableContainer) return;
    if (history.length === 0) {
      this.cbtHistorySection.classList.add('hidden');
      return;
    }

    this.cbtHistorySection.classList.remove('hidden');
    let rowsHtml = '';
    history.slice(0, 5).forEach((item, idx) => {
      const mins = Math.floor((item.time_spent_seconds || 0) / 60);
      const secs = (item.time_spent_seconds || 0) % 60;
      rowsHtml += `
        <tr>
          <td>${item.timestamp}</td>
          <td><strong>${item.set}</strong> (${item.mode === 'exam' ? '실전' : '학습'})</td>
          <td>${item.correct_count} / ${item.total} (${item.accuracy}%)</td>
          <td><strong>${item.scaled_score}점</strong></td>
          <td><span class="history-badge ${item.passed ? 'pass' : 'fail'}">${item.passed ? '합격' : '불합격'}</span></td>
          <td>${mins}분 ${secs}초</td>
        </tr>
      `;
    });

    this.cbtHistoryTableContainer.innerHTML = `
      <table class="history-table">
        <thead>
          <tr>
            <th>응시 일시</th>
            <th>시험 세트</th>
            <th>정답률</th>
            <th>환산 점수</th>
            <th>결과</th>
            <th>소요 시간</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    `;
  }

  async clearHistory() {
    if (!confirm('최근 시험 응시 이력을 모두 초기화하시겠습니까?')) return;
    try {
      localStorage.removeItem('aib_cbt_history');
    } catch (e) {}

    if (this.serverOnline) {
      try {
        await fetch('/api/history/clear', { method: 'POST' });
      } catch (e) {}
    }

    if (this.cbtHistorySection) {
      this.cbtHistorySection.classList.add('hidden');
    }
    if (this.cbtHistoryTableContainer) {
      this.cbtHistoryTableContainer.innerHTML = '';
    }
    alert('시험 응시 이력이 성공적으로 초기화되었습니다.');
  }

  resetCbtToStart() {
    this.isReviewMode = false;
    clearInterval(this.cbtTimerInterval);
    this.cbtUserAnswers = {};
    this.cbtFlagged = new Set();
    this.cbtChecked = new Set();
    this.cbtSubmitBtn.textContent = '시험 제출 (Submit) ✔';
    this.cbtSubmitBtn.className = 'btn btn-primary';
    this.cbtStartScreen.classList.add('active');
    this.cbtExamScreen.classList.remove('active');
    this.cbtResultScreen.classList.remove('active');
    this.cbtTimerBox.classList.add('hidden');
    this.loadExamHistory();
  }
}

// 안전한 즉시/이벤트 초기화 (브라우저 readyState 방어)
function initPortalApp() {
  if (!window.portalApp) {
    try {
      window.portalApp = new PortalApp();
      console.log('✅ PortalApp initialized successfully!');
    } catch (err) {
      console.error('❌ Failed to initialize PortalApp:', err);
    }
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPortalApp);
} else {
  initPortalApp();
}
