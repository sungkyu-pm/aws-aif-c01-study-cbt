# AWS Certified AI Practitioner (AIF-C01) 학습 & CBT 플랫폼

> **한국어 사용자를 위한 AIF-C01 시험 대비 올인원(All-in-One) 학습 공간 및 실전 CBT 가상 실습 시스템**  
> 공식 가이드 기준 도메인 1~5 완벽 반영 | 한·영 듀얼 트랙 학습 | 65문항 실전 모의고사 & 도메인별 집중 실습 | 동적 무작위 출제 & 오답노트 지원

🌐 **온라인 실시간 포털 바로가기**: **[https://sungkyu-pm.github.io/aws-aif-c01-study-cbt/](https://sungkyu-pm.github.io/aws-aif-c01-study-cbt/)**

---

## 🔗 공식 시험 및 접수 링크 (Official Links)
* **AWS 공인 자격증 소개**: [AWS Certified AI Practitioner 공식 페이지 ↗](https://aws.amazon.com/certification/certified-ai-practitioner/)
* **공식 시험 가이드 (영문 PDF)**: [AWS Certified AI Practitioner Official Exam Guide ↗](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf)
* **공식 샘플 문제집 (영문 PDF)**: [AWS Certified AI Practitioner Sample Questions ↗](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Sample-Questions.pdf)
* **AWS 자격증 시험 접수 포털**: [AWS Training & Certification (Pearson VUE) ↗](https://www.aws.training/certification)
* **AWS Skill Builder 시험 준비 코스**: [Skill Builder AIF-C01 Exam Prep Course ↗](https://skillbuilder.aws/category/exam-prep)

---

## 🚀 빠른 시작 (Quick Start)

### 🌐 방법 1: 온라인 웹에서 바로 학습 (추천! 별도 설치 불필요)
브라우저에서 바로 접속하여 모바일/PC 어디서나 시험 응시 및 학습이 가능합니다:  
👉 **[https://sungkyu-pm.github.io/aws-aif-c01-study-cbt/](https://sungkyu-pm.github.io/aws-aif-c01-study-cbt/)**

---

### 💻 방법 2: 로컬 서버 실행
시험 응시 이력 저장, 실시간 채점, 오답 노트 누적 기록을 지원하는 전용 로컬 경량 백엔드 서버입니다 (추가 pip 라이브러리 설치 불필요).

터미널에서 아래 명령어를 실행하면 서버가 구동되며 브라우저가 자동으로 열립니다:
```bash
cd AIF_AWS
./run.sh
```
또는 파이썬으로 직접 실행:
```bash
python3 server.py
```
접속 주소: **`http://localhost:8001`** *(AIB-C01과 포트 충돌 방지를 위해 기본 8001번 포트 사용)*

---

### 📂 방법 2: 브라우저 직접 열기 (파일 모드)
서버 실행 없이 브라우저로 바로 확인하고 싶다면:
* Finder에서 `AIF_AWS/index.html` 파일을 더블 클릭하여 Chrome 또는 Safari로 엽니다.
* 모든 데이터가 JavaScript 번들(`portal-docs-data.js`, `questions-data.js`)로 포함되어 있어 오프라인에서도 100% 동작합니다.

---

## 📂 프로젝트 구성 안내

```
AIF_AWS/
├── docs/                                  # 📚 체계적인 이론 및 가이드 자료실
│   ├── 00_AIF-C01_EXAM_GUIDE.md           # 시험 개요, 도메인 비중 및 3단계 합격 로드맵
│   ├── 01_GLOSSARY_KR_EN.md               # [핵심] AI/ML/GenAI 필수 한·영 기술 용어사전
│   ├── 02_DOMAIN_1_AI_ML_FUNDAMENTALS.md  # 도메인 1: AI 및 머신러닝의 기초 (20%)
│   ├── 03_DOMAIN_2_GENERATIVE_AI_FM.md    # 도메인 2: 생성형 AI 및 파운데이션 모델 (24%)
│   ├── 04_DOMAIN_3_FM_APPLICATIONS.md     # 도메인 3: 파운데이션 모델의 적용 및 평가 (28%)
│   ├── 05_DOMAIN_4_RESPONSIBLE_AI.md      # 도메인 4: 책임 있는 AI 가이드라인 (14%)
│   ├── 06_DOMAIN_5_SECURITY_GOVERNANCE.md # 도메인 5: AI 보안, 컴플라이언스 및 거버넌스 (14%)
│   └── 07_AWS_AI_SERVICES_CHEAT_SHEET.md  # Bedrock/SageMaker/Q/턴키 AI 서비스 종합 치트시트
│
├── questions/                             # 📝 실전 수준 문제은행 (JSON 포맷)
│   ├── questions_domain1.json             # 도메인 1 전용 문제은행 & 상세 한국어 해설
│   ├── questions_domain2.json             # 도메인 2 전용 문제은행 & 상세 한국어 해설
│   ├── questions_domain3.json             # 도메인 3 전용 문제은행 & 상세 한국어 해설
│   ├── questions_domain4.json             # 도메인 4 전용 문제은행 & 상세 한국어 해설
│   ├── questions_domain5.json             # 도메인 5 전용 문제은행 & 상세 한국어 해설
│   └── mock_exam_1.json                   # 공식 비중 맞춤 실전 모의고사 세트 (65문항)
│
├── index.html                             # 모던 인터랙티브 통합 포털 웹 애플리케이션
├── portal.css                             # 반응형 모던 테마 스타일시트
├── portal.js                              # 포털 & CBT 통합 제어 엔진 (타이머, 채점, 한영 전환)
├── portal-docs-data.js                    # 오프라인 브라우저 구동용 Docs 번들
├── questions-data.js                      # 오프라인 브라우저 구동용 문제은행 번들
├── server.py                              # 내장 라이브러리 기반 로컬 REST API 서버
├── run.sh                                 # 원클릭 서버 실행 스크립트
├── sync_docs_and_questions.py             # 문서 및 문제은행 자동 번들러
└── build_aif_question_bank.py             # 문제은행 빌더 스크립트
```

---

## 🎯 핵심 학습 전략 (한·영 듀얼 트랙)

실제 시험은 **영문**으로 출제되기 때문에, 단순히 한국어로만 공부하면 시험장에서 영문 기술 용어(*Overfitting, Recall, LoRA, Context Window, Hallucination, Guardrails, SHAP, Prompt Injection, Data Drift*)를 마주했을 때 체감 난이도가 높아집니다.

1. **1단계 (이론 & 한·영 용어 매핑)**:
   * [`docs/01_GLOSSARY_KR_EN.md`](file:///Users/sungkyu/Study/AIF_AWS/docs/01_GLOSSARY_KR_EN.md)에서 영문 키워드와 한글 개념을 먼저 대조합니다.
   * [`docs/02` ~ `06`](file:///Users/sungkyu/Study/AIF_AWS/docs/02_DOMAIN_1_AI_ML_FUNDAMENTALS.md) 도메인별 핵심 요약 노트로 기술 메커니즘을 정독합니다.
   * [`docs/07_AWS_AI_SERVICES_CHEAT_SHEET.md`](file:///Users/sungkyu/Study/AIF_AWS/docs/07_AWS_AI_SERVICES_CHEAT_SHEET.md)로 Bedrock, SageMaker, Q, 턴키 AI 서비스의 트리거 키워드를 암기합니다.

2. **2단계 (학습 모드 - Study Mode 풀이)**:
   * 영문 지문을 먼저 읽어보고, 이해가 어려울 때는 **[🌐 한국어 번역 토글]** 버튼을 눌러 확인합니다.
   * 문제를 푼 직후 **[정답 확인]**을 눌러 왜 정답인지, 왜 오답인지 상세한 한국어 해설을 습득합니다.

3. **3단계 (실전 모드 - Exam Mode & 오답노트)**:
   * 실전과 동일하게 120분 타이머를 켜고 65문항 종합 모의고사를 신속히 풉니다.
   * 헷갈리는 문제는 **[🚩 검토 표시(Flag)]**를 활용합니다.
   * 시험 제출 후 **도메인별 성취도(%)**를 분석하고, **[❌ 틀린 문제만 오답노트 복습]**을 통해 취약 영역을 100% 보완합니다.

---

## 🛠️ 문제 추가 및 데이터 동기화 방법
새로운 문제를 추가하거나 문서를 수정한 후에는 다음 스크립트를 실행하여 번들을 업데이트합니다:
```bash
python3 sync_docs_and_questions.py
```
