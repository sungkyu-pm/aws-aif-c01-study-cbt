# AIF-C01 핵심 AWS AI 서비스 종합 치트시트 (Cheat Sheet)

> 💡 **시험 직전 10분 총정리!**  
> 문제 지문에 등장하는 요구사항 키워드를 보고 즉시 정답 AWS 서비스를 찾아낼 수 있도록 1:1 매핑한 실전 치트시트입니다.

---

## 1. 서비스 카테고리별 선택 기준 매트릭스

| 비즈니스 요구사항 및 시나리오 | 최우선 정답 서비스 | 대안 또는 비교 대상 |
| :--- | :--- | :--- |
| **"코드 작성 없이(No-code) 머신러닝 예측 모델을 만들거나 GenAI를 테스트하고 싶다"** | **Amazon SageMaker Canvas** | 개발자가 직접 코딩할 때는 SageMaker Studio |
| **"자체 인프라 관리 없이, 단일 API로 최신 LLM(Claude, Llama 등)을 활용하고 RAG를 구축하고 싶다"** | **Amazon Bedrock** | 오픈소스 모델을 직접 인스턴스에 올려 미세조정/호스팅할 때는 SageMaker JumpStart |
| **"사내 문서(SharePoint, Jira 등)를 바탕으로 직무 권한을 지키며 답변하는 엔터프라이즈 챗봇이 필요하다"** | **Amazon Q Business** | 개발자 전용 IDE 코드 도우미는 Amazon Q Developer |
| **"개발자 IDE에서 실시간 코드 자동완성, 코드 변환, 취약점 스캔을 지원받고 싶다"** | **Amazon Q Developer** | 사내 비즈니스 문서 검색은 Amazon Q Business |
| **"기존 문서/데이터셋에 대한 단순 OCR이나 음성/텍스트 변환 등 이미 만들어진 AI 기능이 필요하다"** | **사전 구축(Turnkey) AI 서비스**<br>*(Textract, Transcribe, Rekognition 등)* | 모델을 직접 훈련할 필요 없이 API만 호출 |
| **"AI 모델의 신뢰도가 낮을 때 사람이 직접 수동으로 검토하는 프로세스(HITL)를 구축하고 싶다"** | **Amazon Augmented AI (Amazon A2I)** | 수동 검토 없이 완전 자동화만 할 때는 일반 API |

---

## 2. 사전 구축형(Turnkey) AI 서비스 핵심 키워드 맵

문제 지문에서 아래 키워드가 나오면 고민 없이 해당 서비스를 정답으로 선택하세요:

| 서비스명 | 지문 핵심 키워드 (Trigger Keywords) | 대표 사용 예시 |
| :--- | :--- | :--- |
| **Amazon Textract** | 스캔된 문서, PDF, 영수증, 계약서, **표(Table), 양식(Form - Key/Value 쌍)**, 필기체 텍스트 추출 | 대출 신청서 양식 자동 데이터화 |
| **Amazon Rekognition** | 이미지/영상 객체 감지, **안면 인식/비교(Facial Analysis)**, 유명인 인식, **부적절한 유해 콘텐츠 검출** | 신분증 얼굴 대조, 유해 사진 자동 차단 |
| **Amazon Comprehend** | 텍스트 **감정 분석(Sentiment)**, 핵심 구문(Keyphrases), 개체명(Entities), **PII(개인식별정보) 탐지** | 고객 리뷰 긍정/부정 분류, 이메일 민감정보 마스킹 |
| **Amazon Transcribe** | **음성 텍스트 변환 (STT: Speech-to-Text)**, 콜센터 통화 녹음 분석, 화자 분리(Speaker Diarization) | 고객센터 통화 녹취록 자동 텍스트 생성 |
| **Amazon Polly** | **텍스트 음성 변환 (TTS: Text-to-Speech)**, 자연스러운 음성 합성, 음성 지원 앱 | 뉴스 기사 오디오북 변환 |
| **Amazon Translate** | **다국어 실시간 번역**, 현지화, 언어 장벽 해소 | 글로벌 웹사이트 콘텐츠 자동 번역 |
| **Amazon Lex** | **대화형 챗봇(Chatbot) 및 음성 봇 구축**, 대화 흐름(Intent, Slot), 음성 인식+자연어 이해 | 고객 상담 예약 대화 챗봇 |
| **Amazon Kendra** | **기계학습 기반 지능형 엔터프라이즈 검색**, 비정형 문서에서 질문에 대한 직접 답변 추출 | 사내 기술 문서 및 사규 FAQ 검색 |
| **Amazon Personalize** | 실시간 **개인화 맞춤 추천(Recommendation)**, 사용자 행동 기반 아이템 추천 | 쇼핑몰 연관 상품 추천, OTT 영화 추천 |

---

## 3. Amazon Bedrock 4대 핵심 기능 총정리

1. **Bedrock Knowledge Bases (지식 베이스)**:
   * **키워드**: 완전관리형 RAG, S3 문서 연결, 자동 청킹(Chunking) 및 임베딩, 벡터 데이터베이스 연동.
   * **목적**: 모델 재학습 없이 사내 최신 데이터 기반으로 정확한 답변 생성 및 환각 방지.
2. **Bedrock Agents (에이전트)**:
   * **키워드**: 자율 다단계 작업 수행(Orchestration), 비즈니스 로직 실행, **AWS Lambda 연동**, OpenAPI 스키마.
   * **목적**: 사용자의 대화 요청을 바탕으로 실제 데이터베이스 조회, 항공권 예약, 결제 처리 등 실천적 작업 자동화.
3. **Bedrock Guardrails (가드레일)**:
   * **키워드**: 안전 정책 강제, **유해 콘텐츠 필터링, PII(개인정보) 마스킹, 차단 주제(Denied Topics) 설정, 프롬프트 인젝션 방어, 사실성 검증(Contextual Grounding)**.
   * **목적**: 기업 윤리 준수 및 악의적 공격 방어.
4. **Bedrock Model Evaluation (모델 평가)**:
   * **키워드**: 파운데이션 모델 비교, **ROUGE, BLEU 자동 평가 지표, 인간 평가자(팀/크라우드)** 지원.
   * **목적**: 우리 회사 업무에 가장 비용 효율적이고 정확한 모델 선택.

---

## 4. Amazon SageMaker 주요 거버넌스 & 개발 도구 맵

| 도구 명칭 | 핵심 기능 및 시험 빈출 포인트 |
| :--- | :--- |
| **SageMaker Canvas** | 비즈니스 분석가를 위한 **시각적 노코드(No-code) ML & GenAI** 워크스페이스. |
| **SageMaker JumpStart** | 오픈소스 FM(Llama, Mistral 등)을 원클릭으로 검색, 배포 및 자체 인프라 파인튜닝하는 허브. |
| **SageMaker Clarify** | 학습 전/후 **데이터 편향(Bias) 탐지** 및 **SHAP 가치 기반 모델 설명가능성(Explainability)** 제공. |
| **SageMaker Model Cards** | 모델 목적, 훈련 데이터, 벤치마크 메트릭, 의도된 용도/한계점을 기록하는 **표준 모델 명세서**. |
| **SageMaker Model Dashboard** | 배포된 모든 엔드포인트의 품질, 드리프트, 가용성을 모니터링하는 **통합 거버넌스 대시보드**. |
| **SageMaker Model Monitor** | 프로덕션 운영 중 발생하는 **데이터 드리프트(Data Drift) 및 개념 드리프트(Concept Drift)** 자동 감지. |
| **SageMaker Role Manager** | 직무 역할(데이터 과학자, 엔지니어 등)에 맞춘 **최소 권한의 IAM 정책 템플릿**을 손쉽게 생성. |

---

## 5. 보안 및 데이터 보호 도구 매핑

* **저장 중 암호화 (Data at Rest)**: **AWS KMS** (고객 관리형 키 CMK로 완전한 제어권 확보).
* **전송 중 암호화 (Data in Transit)**: **TLS 1.2 / TLS 1.3**.
* **프라이빗 통신 (인터넷 미노출)**: **AWS PrivateLink 기반 VPC 엔드포인트**를 통해 사내 VPC에서 Bedrock/SageMaker로 직접 안전하게 접속.
* **PII(개인정보) 자동 발견/감사**: **Amazon Macie** (S3 버킷 내 민감정보 머신러닝 스캔).
* **API 호출 추적 및 감사**: **AWS CloudTrail** (누가 언제 모델을 호출했는지 영구 감사 로깅).
* **실시간 리소스 지표 및 알람**: **Amazon CloudWatch** (지연 시간, 오류율, 호출 건수 알람).
