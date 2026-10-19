# AWS Certified AI Practitioner (AIF-C01) 시험 안내 및 학습 전략

## 🔗 공식 사이트 & 시험 접수 바로가기 (Official Links & Registration)

> 💡 **시험 공식 가이드 문서 및 Pearson VUE 온라인/오프라인 시험 접수 안내**

| 구분 | 주요 내용 및 공식 링크 |
| :--- | :--- |
| **🌐 AWS 공식 자격증 소개** | [AWS Certified AI Practitioner 공식 페이지 ↗](https://aws.amazon.com/certification/certified-ai-practitioner/) |
| **📝 AWS 자격증 공식 접수 포털** | [AWS Training & Certification 시험 예약 포털 바로가기 ↗](https://www.aws.training/certification) *(Pearson VUE 온라인/센터 응시 접수)* |
| **📄 공식 시험 가이드 (영문 원문)** | [AWS Certified AI Practitioner Official Exam Guide (English PDF/Web) ↗](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Exam-Guide.pdf) |
| **📄 공식 샘플 문항 세트** | [AWS Certified AI Practitioner Sample Questions ↗](https://d1.awsstatic.com/training-and-certification/docs-ai-practitioner/AWS-Certified-AI-Practitioner_Sample-Questions.pdf) |
| **🎓 AWS Skill Builder 공식 수험 과정** | [Exam Prep Standard Course: AWS Certified AI Practitioner (AIF-C01) ↗](https://skillbuilder.aws/category/exam-prep) |

---

### 📌 시험 접수 및 예약 절차 가이드 (How to Register)

1. **AWS Training & Certification 계정 로그인**: [https://www.aws.training/certification](https://www.aws.training/certification)에 접속하여 개인 AWS Certification 계정으로 로그인합니다.
2. **시험 일정 예약 (Schedule an Exam)**: 대시보드 메인에서 **`Manage Pearson VUE Exams`** 또는 **`시험 예약(Schedule an Exam)`** 버튼을 클릭합니다.
3. **시험 코드 검색**: 응시 가능한 시험 목록에서 **`AIF-C01: AWS Certified AI Practitioner`**를 검색하여 선택합니다.
4. **응시 방식 선택**:
   * **온라인 감독관 응시 (Online at home or office)**: 웹캠과 마이크가 장착된 조용한 개인 공간에서 Pearson VUE OnVUE를 통해 자택 또는 사무실에서 실시간 원격 응시.
   * **공인 시험 센터 방문 (In-person at a testing center)**: 서울, 부산 등 전국 주요 Pearson VUE 공인 시험 센터를 직접 방문하여 지정된 PC로 응시.
5. **시험 언어 및 결제**:
   * 시험 기본 언어(English 등)와 시험 일시를 선택합니다.
   * 응시료: **$100 USD** (이전 AWS 자격증 취득자 50% 할인 바우처 적용 가능 시 **$50 USD**).
   * *(💡 핵심 팁: 영어가 모국어가 아닌 경우 시험 접수 전 계정 설정의 `Request Exam Accommodations`에서 **'ESL +30분 추가 시간 신청'**을 사전 승인받으면 120분 대신 **150분**으로 여유롭게 응시할 수 있습니다.)*

---

## 1. 시험 개요 (Exam Overview)

* **시험 코드**: AIF-C01 (AWS Certified AI Practitioner)
* **자격증 레벨**: Foundational (기초)
* **목표 대상**: 인공지능(AI), 머신러닝(ML), 생성형 AI(Generative AI)의 기본 원리와 AWS의 주요 AI 서비스(Bedrock, SageMaker, Q, Turnkey AI Services)를 실무에 올바르게 적용하고자 하는 프랙티셔너, 개발자, 기획자, 데이터 분석가
* **시험 문항 수**: **65문항** (채점 문항 50문항 + 점수에 반영되지 않는 사전 검증 문항 15문항)
* **문항 형식**:
  * 객관식 단일 선택 (Multiple Choice): 4개 보기 중 정답 1개 선택
  * 객관식 다중 선택 (Multiple Response): 5개 이상 보기 중 정답 2개 이상 선택
* **시험 시간**: **120분** (ESL 30분 연장 신청 시 **150분**)
* **합격 기준 점수**: 100~1,000점 환산 점수 체계 중 **700점 이상 합격**
* **언어 전략**: 시험 문제는 영문으로 출제되므로, **한국어로 개념 원리를 철저히 학습하고, 핵심 기술 키워드와 선택지는 영문 표현에 직관적으로 익숙해지는 한·영 듀얼 트랙(Bilingual Dual-Track)** 전략이 필수적입니다.

---

## 2. 도메인별 출제 비중 (Domain Weighting)

공식 AWS 가이드 기준 5개 도메인으로 구성되어 있습니다:

| 도메인 | 도메인 명칭 (Domain Name) | 출제 비중 | 핵심 평가 역량 |
| :---: | :--- | :---: | :--- |
| **Domain 1** | **AI 및 ML의 기초**<br>*(Fundamentals of AI and ML)* | **20%** | • AI, ML, Deep Learning 개념 차이 및 지도/비지도/강화학습 구분<br>• ML 엔드투엔드 수명주기(데이터 수집, 특성 공학, 학습, 튜닝, 서빙)<br>• 분류/회귀 평가 지표(Accuracy, Precision, Recall, F1, ROC-AUC, RMSE, MAE)<br>• 과적합(Overfitting) vs 과소적합(Underfitting) 진단 및 완화 기법 |
| **Domain 2** | **생성형 AI의 기초**<br>*(Fundamentals of Generative AI)* | **24%** | • 생성형 AI의 동작 원리 및 파운데이션 모델(FM/LLM/멀티모달)<br>• 프롬프트 엔지니어링 5대 기법(Zero/Few-shot, CoT, 시스템 프롬프트)<br>• 사전 훈련 vs 미세 조정(Fine-tuning, LoRA/PEFT) vs RAG 아키텍처 비교<br>• 토큰, 컨텍스트 윈도우, 환각(Hallucination) 원인 및 방지책 |
| **Domain 3** | **파운데이션 모델의 적용 및 평가**<br>*(Applications of Foundation Models)* | **28%** | • 유스케이스별 최적 FM 선정 기준(지연 시간, 비용, 정확도, 모델 크기)<br>• **Amazon Bedrock** 생태계(Knowledge Bases, Agents, Guardrails, Evaluation)<br>• **Amazon Q** (Q Business, Q Developer) & **Amazon SageMaker** (JumpStart, Canvas)<br>• 턴키 AI 서비스(Rekognition, Textract, Comprehend, Transcribe, Polly)<br>• 생성형 AI 평가 지표(ROUGE, BLEU, BERTScore, 인간 피드백/RLHF) |
| **Domain 4** | **책임 있는 AI 가이드라인**<br>*(Guidelines for Responsible AI)* | **14%** | • 책임 있는 AI 5대 기둥(공정성, 설명가능성, 견고성, 개인정보보호, 안전성)<br>• 편향(Bias) 탐지 및 SageMaker Clarify / SHAP 가치 분석<br>• 인간 참여 루프 (HITL: Human-in-the-Loop) - Amazon A2I<br>• 지적 재산권(IP), 저작권, 데이터 출처 및 모델 카드(Model Cards) |
| **Domain 5** | **AI 솔루션의 보안, 컴플라이언스 및 거버넌스**<br>*(Security, Compliance, and Governance)* | **14%** | • 데이터 보호(KMS 암호화, TLS), VPC 엔드포인트 격리, IAM 최소 권한 원칙<br>• 생성형 AI 보안 위협: 프롬프트 인젝션, 탈옥(Jailbreak), 데이터 오염<br>• 모니터링 및 감사 도구: CloudTrail, CloudWatch, Macie(PII 탐지)<br>• SageMaker Model Dashboard, Model Registry 거버넌스 |

---

## 3. 한국어 사용자를 위한 합격 3단계 로드맵

```
[1단계: 개념 체계화 & 한·영 기술 용어 맵핑] (예상 3~4일)
  - docs/01_GLOSSARY_KR_EN.md: 필수 영문 기술 키워드와 한글 개념 1:1 매핑
  - docs/02~06: 도메인 1~5 핵심 이론 및 기술 메커니즘 정독
  - docs/07: AWS AI 핵심 서비스 치트시트로 서비스별 역할과 차이점 숙지

[2단계: 도메인별 집중 문제 풀이 (Study Mode)] (예상 4~5일)
  - 포털 '도메인별 연습'에서 Domain 1부터 5까지 집중 풀이
  - 문제 풀이 시 [🌐 한/영 전환] 기능을 활용해 영문 지문과 한국어 번역 대조
  - 정답 제출 즉시 상세 해설을 읽고, 오답 원인 및 핵심 출제 포인트 체득

[3단계: 실전 모의고사 & 취약점 공략 (Exam Mode)] (예상 2~3일)
  - 실제 시험과 동일한 65문항, 120분 타이머 설정 후 실전 모의고사 응시
  - 모의고사 종료 후 도메인별 성취도(%) 레이더 차트 분석
  - '오답 노트 복습' 기능을 통해 틀린 문제와 헷갈렸던 플래그(🚩) 문항 100% 재학습
```

---

## 4. AIF-C01 시험 필수 핵심 팁 (Exam Tips)

1. **지문 키워드에 맞는 AWS 서비스 즉각 연상**:
   * *자연어 처리, 감정 분석, 키워드 추출* ➔ **Amazon Comprehend**
   * *문서 내 테이블, 서식, 텍스트 OCR* ➔ **Amazon Textract**
   * *이미지/영상 내 객체 검출, 안면 인식, 유해 콘텐츠 필터링* ➔ **Amazon Rekognition**
   * *음성 텍스트 변환 (STT)* ➔ **Amazon Transcribe**
   * *텍스트 음성 변환 (TTS)* ➔ **Amazon Polly**
   * *사내 문서 기반 엔터프라이즈 AI 어시스턴트* ➔ **Amazon Q Business**
   * *개발자 코드 추천 및 분석* ➔ **Amazon Q Developer**
   * *완전관리형 파운데이션 모델(FM) API 및 RAG/가드레일 통합* ➔ **Amazon Bedrock**
   * *노코드(No-code) 머신러닝 예측 모델 구축* ➔ **Amazon SageMaker Canvas**
   * *모델 편향 분석 및 특성 중요도(설명가능성)* ➔ **Amazon SageMaker Clarify**
   * *사람의 검토가 필요한 워크플로 (HITL)* ➔ **Amazon A2I (Augmented AI)**
   * *S3 버킷 내 개인식별정보(PII) 자동 탐지 및 보호* ➔ **Amazon Macie**

2. **비용 및 개발 리소스 효율성 원칙 (AWS Well-Architected)**:
   * "최소한의 개발 노력(Least operational overhead)", "코드 작성 불필요" 요구 시: 사전 구축된 AWS AI 서비스(Turnkey) 또는 Bedrock/Canvas 우선 고려
   * 맞춤형 커스텀 딥러닝 훈련이 필요할 때만 SageMaker Training/Hosting 고려

3. **생성형 AI 기법 선택 순서**:
   * **1순위 (비용/시간 최소)**: **Prompt Engineering** (프롬프트 개선, Few-shot)
   * **2순위 (최신 내부 데이터/문서 연동 필요 시)**: **RAG** (Retrieval-Augmented Generation + Bedrock Knowledge Bases)
   * **3순위 (특정 도메인 어조/출력 형식 고도화 필요 시)**: **Fine-tuning (PEFT/LoRA)**
   * **최후 순위 (비용/데이터 극대화)**: 처음부터 사전 훈련 (Pre-training from scratch)
