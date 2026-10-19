# AIF-C01 필수 AI/ML/GenAI 한·영 기술 용어사전 (Glossary)

> 💡 **AIF-C01 시험은 영문 지문으로 출제됩니다.**  
> 본 사전은 한국어로 개념의 메커니즘을 확실히 이해하고, 영문 지문과 보기에서 마주치는 핵심 키워드를 즉시 식별할 수 있도록 구성된 핵심 대응표입니다.

---

## 1. AI, 머신러닝, 딥러닝 기초 (AI & ML Fundamentals)

| 영문 용어 (English) | 한국어 명칭 | 시험 출제 핵심 설명 (Exam Key Point) |
| :--- | :--- | :--- |
| **Artificial Intelligence (AI)** | 인공지능 | 인간의 인지 능력(학습, 추론, 문제 해결 등)을 모방하는 시스템의 총칭. |
| **Machine Learning (ML)** | 머신러닝 (기계학습) | 명시적인 규칙 코딩 없이, 대량의 데이터로부터 패턴과 통계적 관계를 학습하여 예측/판단을 수행하는 기술. |
| **Deep Learning (DL)** | 딥러닝 (심층학습) | 여러 층의 인공신경망(Artificial Neural Networks)을 활용하여 비정형 데이터(이미지, 텍스트, 음성)의 복잡한 특징을 스스로 추출하는 기법. |
| **Generative AI (GenAI)** | 생성형 AI | 기존 데이터를 바탕으로 텍스트, 이미지, 코드, 오디오 등의 새로운 원본 콘텐츠를 능동적으로 생성하는 인공지능 분야. |
| **Supervised Learning** | 지도학습 | **레이블(정답/Label)이 달린 훈련 데이터**를 제공하여 입력(X)과 출력(Y) 간의 관계를 학습하는 방식 (분류, 회귀). |
| **Unsupervised Learning** | 비지도학습 | **레이블(정답)이 없는 데이터**에서 내재된 패턴, 군집, 구조를 발견하는 학습 방식 (클러스터링, 차원 축소, 이상 탐지). |
| **Semi-supervised Learning** | 준지도학습 | 소량의 레이블 데이터와 대량의 비레이블 데이터를 결합하여 학습 비용을 낮추고 성능을 극대화하는 방식. |
| **Reinforcement Learning (RL)**| 강화학습 | 에이전트가 환경과 상호작용하며 **보상(Reward)을 최대화**하고 벌점(Penalty)을 최소화하도록 행동 정책을 학습하는 기법. |
| **Feature Engineering** | 특성 공학 | 모델이 학습하기 쉽도록 원시 데이터를 가공, 정규화, 결측치 처리, 파생 변수 생성 등으로 변환하는 프로세스. |
| **Data Imputation** | 결측치 대체 | 누락된 데이터 값을 평균, 중앙값, 최빈값 또는 예측 알고리즘으로 채워 넣는 기법. |
| **Data Drift** | 데이터 드리프트 | 훈련에 사용된 입력 데이터의 통계적 분포가 실제 운영 환경에서 시간이 지남에 따라 변하는 현상. |
| **Concept Drift** | 개념 드리프트 | 입력 데이터와 예측 대상(레이블) 간의 통계적 상관관계 자체가 변하여 모델 성능이 저하되는 현상. |

---

## 2. 모델 평가 및 학습 최적화 지표 (Metrics & Optimization)

| 영문 용어 (English) | 한국어 명칭 | 시험 출제 핵심 설명 (Exam Key Point) |
| :--- | :--- | :--- |
| **Overfitting** | 과적합 | 모델이 훈련 데이터에 너무 과도하게 맞춰져, **새로운 검증/테스트 데이터에 대한 일반화 능력이 떨어지는 현상** (High Variance). |
| **Underfitting** | 과소적합 | 모델이 너무 단순하여 훈련 데이터의 기본적인 패턴조차 제대로 학습하지 못한 상태 (High Bias). |
| **Bias-Variance Tradeoff** | 편향-분산 트레이드오프 | 모델의 편향(단순함으로 인한 오차)과 분산(데이터 변동에 따른 민감도) 간의 상충 관계. |
| **Regularization (L1/L2)** | 정규화 (규제) | 과적합을 방지하기 위해 가중치 크기에 페널티(L1 Lasso: 희소화, L2 Ridge: 가중치 감쇠)를 부여하는 기법. |
| **Dropout** | 드롭아웃 | 신경망 훈련 시 일부 노드를 무작위로 비활성화하여 특정 뉴런에 대한 의존도를 낮추고 과적합을 방지하는 기법. |
| **Cross-Validation (k-fold)** | 교차 검증 | 데이터를 k개 그룹으로 나누어 k번 반복 검증함으로써 모델의 일반화 성능을 안정적으로 추정하는 기법. |
| **Confusion Matrix** | 혼동 행렬 | TP(True Positive), FP, FN, TN으로 구성된 분류 모델 성능 평가 매트릭스. |
| **Accuracy** | 정확도 | 전체 예측 중 맞춘 예측의 비율. 클래스 불균형(Imbalanced Data) 시 왜곡될 수 있음. |
| **Precision** | 정밀도 | 모델이 Positive라고 예측한 것 중 실제 Positive인 비율. *(FP를 줄여야 할 때 중요, 예: 스팸 메일 분류)* |
| **Recall (Sensitivity)** | 재현율 | 실제 Positive인 것 중 모델이 올바르게 찾아낸 비율. *(FN을 치명적으로 줄여야 할 때 중요, 예: 암 진단, 사기 탐지)* |
| **F1 Score** | F1 점수 | Precision과 Recall의 **조화 평균(Harmonic Mean)**으로, 불균형 데이터셋 평가의 핵심 표준. |
| **ROC-AUC** | ROC 곡선 아래 면적 | 임계값(Threshold) 변화에 따른 분류기의 종합적 변별력을 0.0~1.0 사이로 측정한 척도. |
| **MAE / RMSE / R²** | 회귀 평가 지표 | MAE(평균 절대 오차), RMSE(평균 제곱근 오차 - 큰 오차에 민감), R²(결정계수 - 데이터 설명력). |

---

## 3. 생성형 AI 및 파운데이션 모델 (Generative AI & Foundation Models)

| 영문 용어 (English) | 한국어 명칭 | 시험 출제 핵심 설명 (Exam Key Point) |
| :--- | :--- | :--- |
| **Foundation Model (FM)** | 파운데이션 모델 | 대규모 비레이블 데이터셋으로 사전 훈련(Pre-trained)되어, 다양한 다운스트림 작업(요약, 질의응답, 추론 등)에 범용적으로 활용 가능한 초대형 모델. |
| **Large Language Model (LLM)** | 거대 언어 모델 | 수십억~수천억 개의 파라미터를 바탕으로 인간 언어의 문맥을 이해하고 생성하는 텍스트 전문 파운데이션 모델. |
| **Multimodal Model** | 멀티모달 모델 | 텍스트, 이미지, 음성, 비디오 등 둘 이상의 서로 다른 형태(모달리티)의 데이터를 동시에 입력받고 처리/생성할 수 있는 모델 (예: Claude 3, Titan Multimodal). |
| **Token** | 토큰 | LLM이 텍스트를 처리하는 기본 단위. 통상 1,000토큰은 약 750개의 영어 단어에 해당. |
| **Context Window** | 컨텍스트 윈도우 | 모델이 한 번의 프롬프트 처리 과정에서 기억하고 참조할 수 있는 최대 토큰 허용량. |
| **Temperature** | 온도 파라미터 | 모델 출력의 무작위성(창의성 vs 결정론)을 조절하는 하이퍼파라미터. 낮을수록(0에 가까움) 일관되고 사실적이며, 높을수록 창의적이고 다양함. |
| **Top-P (Nucleus Sampling)** | 핵 샘플링 | 누적 확률이 P 이하인 가장 가능성 높은 토큰 집합 내에서만 다음 단어를 샘플링하는 기법. |
| **Prompt Engineering** | 프롬프트 엔지니어링 | 모델의 가중치를 수정하지 않고, 입력 지시문(Prompt)을 전략적으로 설계하여 원하는 최적의 출력을 이끌어내는 기술. |
| **Zero-shot Prompting** | 제로샷 프롬프팅 | 예시(Example) 없이 바로 지시문이나 질문만 전달하여 답변을 유도하는 기법. |
| **Few-shot Prompting** | 퓨샷 프롬프팅 | 프롬프트 내에 몇 가지 모범 입력-출력 예시(Exemplars)를 제공하여 원하는 형식과 스타일을 유도하는 기법. |
| **Chain-of-Thought (CoT)** | 생각의 사슬 | 모델에게 "단계별로 생각하라(Think step-by-step)"는 지시를 주어 복잡한 다단계 추론이나 수학 문제를 해결하도록 유도하는 기법. |
| **System Prompt** | 시스템 프롬프트 | AI 모델의 페르소나, 역할, 응답 지침, 금지 사항 등을 사전에 규정하는 최상위 시스템 지침. |

---

## 4. 모델 커스터마이징 및 지식 증강 (Customization & RAG)

| 영문 용어 (English) | 한국어 명칭 | 시험 출제 핵심 설명 (Exam Key Point) |
| :--- | :--- | :--- |
| **RAG (Retrieval-Augmented Generation)** | 검색 증강 생성 | 최신 외부 데이터베이스/사내 문서를 실시간으로 검색하여 관련 정보를 프롬프트의 컨텍스트로 주입한 뒤 답변을 생성하는 아키텍처. 모델 재학습 없이 최신/비공개 데이터 활용 가능. |
| **Vector Embedding** | 벡터 임베딩 | 텍스트나 이미지의 의미적(Semantic) 정보를 수백~수천 차원의 연속적인 실수 벡터로 수치화한 표현. |
| **Vector Database** | 벡터 데이터베이스 | 고차원 임베딩 벡터 간의 유사도(코사인 유사도 등)를 초고속으로 근사 검색(k-NN)할 수 있는 저장소 (Amazon OpenSearch Serverless, Aurora pgvector 등). |
| **Chunking** | 청킹 (문서 분할) | 긴 문서를 검색 및 임베딩 처리에 적합한 일정한 크기(토큰 단위)의 조각으로 나누는 전처리 기법. |
| **Fine-Tuning** | 미세 조정 | 사전 훈련된 모델의 가중치를 특정 도메인의 전용 데이터셋을 사용해 추가 훈련시켜 도메인 특화 어조 및 전문 지식을 학습시키는 작업. |
| **PEFT (Parameter-Efficient Fine-Tuning)** | 매개변수 효율적 미세조정 | 모델의 모든 파라미터를 업데이트하지 않고, 일부 파라미터나 소형 어댑터 계층만 학습시켜 연산 비용과 메모리를 극적으로 절감하는 기법. |
| **LoRA (Low-Rank Adaptation)** | 저차원 적응 기법 | 대표적인 PEFT 방식으로, 사전 학습된 가중치 행렬을 고정하고 저차원 분해 행렬만을 학습시키는 효율적 기법. |
| **RLHF (Reinforcement Learning from Human Feedback)** | 인간 피드백 강화학습 | 인간 평가자의 선호도 피드백을 기반으로 보상 모델을 구축하고 모델의 출력을 인간의 가치와 의도에 일치(Alignment)시키는 튜닝 기법. |

---

## 5. 생성형 AI 평가 지표 (GenAI Evaluation Metrics)

| 영문 용어 (English) | 한국어 명칭 | 시험 출제 핵심 설명 (Exam Key Point) |
| :--- | :--- | :--- |
| **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)** | ROUGE 점수 | 생성된 텍스트와 참조(정답) 요약문 간의 n-gram 겹침(재현율 중심)을 측정하는 지표. **문서 요약(Summarization) 평가**의 대표 지표. |
| **BLEU (Bilingual Evaluation Understudy)** | BLEU 점수 | 생성된 번역문과 참조 번역문 간의 n-gram 정밀도(Precision)를 측정하는 지표. **기계 번역(Translation) 평가**의 대표 지표. |
| **BERTScore** | 버트스코어 | 표면적인 단어 일치가 아닌, 사전 학습된 BERT 임베딩 간의 코사인 유사도를 계산하여 **의미적 유사도(Semantic Similarity)**를 평가하는 지표. |
| **Perplexity (PPL)** | 펄플렉서티 (혼란도) | 언어 모델이 다음 단어를 얼마나 헷갈려하지 않고 잘 예측하는지 나타내는 지표. **값이 낮을수록 언어 모델의 유창성과 성능이 뛰어남**. |
| **Hallucination** | 환각 현상 | 사실이 아니거나 출처에 근거하지 않은 허위 정보, 지어낸 논리를 그럴듯하게 확신을 가지고 생성하는 LLM의 결함. |

---

## 6. 책임 있는 AI, 보안 및 거버넌스 (Responsible AI & Security)

| 영문 용어 (English) | 한국어 명칭 | 시험 출제 핵심 설명 (Exam Key Point) |
| :--- | :--- | :--- |
| **Responsible AI (RAI)** | 책임 있는 AI | 공정성(Fairness), 설명가능성(Explainability), 투명성(Transparency), 견고성(Robustness), 개인정보보호(Privacy)를 보장하는 AI 개발 원칙. |
| **Explainability & Interpretability**| 설명가능성 & 해석가능성 | 모델이 특정 예측이나 판단을 내리게 된 이유와 메커니즘을 인간이 이해하고 감사할 수 있는 정도 (SHAP, LIME). |
| **Amazon SageMaker Clarify** | 세이지메이커 클래리파이 | 데이터셋의 잠재적 편향(Bias)을 탐지하고, SHAP 기법을 통해 특성 중요도(Feature Importance) 및 모델 예측의 설명가능성을 제공하는 서비스. |
| **Human-in-the-Loop (HITL)** | 인간 참여 루프 | 모델의 예측 신뢰도(Confidence)가 낮거나 고위험 의사결정일 때 사람(전문가)의 검토와 승인을 거치도록 설계된 워크플로 (**Amazon A2I**). |
| **Amazon Bedrock Guardrails** | 베드록 가드레일 | 유해 콘텐츠 차단, 비속어 필터링, 민감한 개인정보(PII) 마스킹, 프롬프트 인젝션 방어, 허용되지 않은 주제 차단 등 안전 정책을 시행하는 기능. |
| **Prompt Injection** | 프롬프트 주입 공격 | 사용자가 악의적인 프롬프트를 입력하여 시스템 지침을 우회하거나 내부 정보를 탈취, 시스템을 통제하려는 공격. |
| **Jailbreaking** | 탈옥 | 모델에 설정된 윤리적/안전 가드레일을 무력화하여 유해하거나 금지된 콘텐츠를 생성하도록 유도하는 특수 공격. |
| **Data Poisoning** | 데이터 오염 공격 | 모델의 훈련 데이터셋에 악의적인 위조/왜곡 데이터를 의도적으로 주입하여 모델의 추론 결과를 조작하는 공격. |
| **Model Inversion / Stealing** | 모델 역공학 / 도용 | 모델의 출력값만을 지속적으로 쿼리하여 원본 훈련 데이터(개인정보)를 역추적하거나 모델의 지적 자산을 복제하는 공격. |
| **Model Cards** | 모델 카드 | 모델의 의도된 용도, 아키텍처, 훈련 데이터셋, 한계점, 평가 지표 및 윤리적 고려사항을 표준화하여 문서화한 명세서 (**SageMaker Model Cards**). |
