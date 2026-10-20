#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS Certified AI Practitioner (AIF-C01)
대규모 한·영 듀얼트랙 실전 문제은행 생성기
- 5개 도메인 총 80개 이상의 정밀 토픽 카테고리
- 12개 실전 엔터프라이즈 산업군 시나리오 결합
- 영문 지문(question_en) + 한국어 번역 지문(question_kr)
- 4개 선택지 (A~D) 영문(text_en) + 한국어(text_kr)
- 상세 한국어 해설(explanation_kr) 및 핵심 개념 매핑
- 도메인당 120~160문항, 총 700문항 이상 대규모 풀 구축
"""

import os
import json
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_DIR = os.path.join(BASE_DIR, 'questions')
os.makedirs(QUESTIONS_DIR, exist_ok=True)

INDUSTRIES = [
    ("글로벌 금융 및 핀테크 기업", "global FinTech & tier-1 investment bank",
     "실시간 신용 카드 이상 거래 탐지 및 대출 심사 로그", "real-time credit card fraud telemetry and underwriting application data"),
    ("대형 전자상거래 및 온라인 리테일 플랫폼", "hyperscale e-commerce & retail marketplace",
     "수천만 건의 상품 리뷰, 장바구니 클릭스트림 및 구매 이력", "tens of millions of product reviews, clickstream logs, and order histories"),
    ("대학 부속 종합병원 및 임상 연구원", "academic medical center and clinical trials research institute",
     "비정형 전자의무기록(EMR), 의학 영상 및 환자 진료 차트", "unstructured Electronic Medical Records (EMR), medical imaging, and pathology charts"),
    ("글로벌 항공사 및 여행 예약 플랫폼", "international airline and global travel booking platform",
     "실시간 항공편 스케줄, 승객 수하물 추적 및 고객 서비스 문의", "real-time flight telemetry, baggage tracking streams, and passenger inquiries"),
    ("첨단 반도체 및 스마트 제조 공장", "advanced semiconductor fabrication & smart manufacturing facility",
     "수만 개의 공장 설비 IoT 진동/온도 시계열 센서 데이터", "tens of thousands of factory equipment IoT vibration and temperature telemetry streams"),
    ("엔터프라이즈 B2B SaaS 소프트웨어 기업", "enterprise B2B SaaS software provider",
     "수백만 건의 고객 기술 지원 티켓, 지식베이스 문서 및 API 로그", "millions of technical support tickets, knowledge articles, and API access logs"),
    ("전국망 통신 서비스 사업자", "nationwide 5G telecommunications carrier",
     "기지국 네트워크 트래픽 혼잡도 로그 및 고객 서비스 해지 위험 데이터", "cell tower network congestion metrics and customer churn propensity event logs"),
    ("글로벌 손해보험 및 손해사정 전문사", "global property and casualty insurance enterprise",
     "사고 현장 손해사정 보고서, 현장 증빙 사진 및 보상 청구 서류", "accident damage appraisal reports, field photographs, and claim documentation"),
    ("공공 행정 및 지자체 스마트 민원 센터", "metropolitan municipal government and citizen service center",
     "시민 복지 정책 민원 상담 내역 및 공공 행정 조례 문서", "civic welfare petition transcripts and municipal regulatory administrative archives"),
    ("글로벌 미디어 및 영상 스트리밍 플랫폼", "global media & over-the-top streaming platform",
     "방대한 비디오 아카이브, 오디오 사운드트랙 및 다국어 자막 데이터", "massive digital video catalog, audio stems, and multilingual subtitle assets"),
    ("글로벌 자동차 제조 및 커넥티드카 기업", "multinational automotive OEM and connected fleet platform",
     "차량 텔레매틱스 주행 센서 로그 및 운전자 보조 시스템(ADAS) 데이터", "vehicular telematics telemetry and advanced driver assistance sensor streams"),
    ("글로벌 바이오제약 및 신약 개발 연구소", "global biopharmaceutical and drug discovery laboratory",
     "단백질 분자 구조 시뮬레이션 및 전임상 실험 스크리닝 데이터", "molecular docking simulations and pre-clinical assay screening datasets")
]

# ==============================================================================
# 도메인 1: AI 및 머신러닝의 기초 (Fundamentals of AI and ML) - 20%
# ==============================================================================
D1_TAXONOMY = [
    (
        "AI vs ML vs DL vs GenAI Hierarchy", "AI/ML/DL/GenAI 계층 구조",
        "명시적인 규칙 코딩 대신 데이터의 통계적 패턴을 스스로 학습하여 예측을 수행하는 기술 영역을 무엇이라고 부릅니까?",
        "When an enterprise requires algorithms that learn statistical representations directly from historical data to make predictions without rule-based programming, which paradigm applies?",
        "머신러닝 (Machine Learning)", "Machine Learning (ML)",
        [
            ("규칙 기반 수동 if-else 전문가 시스템", "Deterministic rule-based expert scripts"),
            ("하드웨어 레벨의 펌웨어 업데이트", "Hardware-level firmware updates"),
            ("단순 관계형 데이터베이스 인덱싱", "Relational database index reorganization")
        ],
        "머신러닝(ML)은 명시적인 프로그래밍 없이 대량의 데이터로부터 패턴과 통계적 관계를 학습하여 예측 또는 판단을 수행하는 인공지능의 하위 분야입니다."
    ),
    (
        "Deep Learning & Artificial Neural Networks", "딥러닝 및 인공신경망",
        "이미지, 자연어, 오디오 등 복잡한 고차원 비정형 데이터에서 다층 신경망(Neural Networks)을 통해 특징(Feature)을 스스로 추출하는 기법은 무엇입니까?",
        "Which subset of machine learning uses multi-layered artificial neural networks to automatically extract hierarchical representations from unstructured data like images and audio?",
        "딥러닝 (Deep Learning)", "Deep Learning (DL)",
        [
            ("전통적인 선형 회귀 분석", "Ordinary least squares linear regression"),
            ("정적 스프레드시트 피벗 테이블", "Static spreadsheet pivot modeling"),
            ("이진 탐색 트리 정렬", "Binary search tree sorting algorithms")
        ],
        "딥러닝(DL)은 인간의 뇌 신경망 구조를 모방한 심층 신경망을 사용하여 원시 비정형 데이터(이미지, 음성, 텍스트)로부터 고차원 특징을 자동으로 학습합니다."
    ),
    (
        "Supervised Learning - Classification", "지도학습: 분류(Classification)",
        "타깃 열(이탈 여부, 스팸 여부 등)의 정답 레이블이 포함된 과거 데이터를 바탕으로, 새로운 입력 데이터의 범주를 예측하는 학습 방식은 무엇입니까?",
        "Which machine learning paradigm trains models using input features paired with discrete categorical target labels to predict future classes?",
        "지도학습의 분류 (Supervised Classification)", "Supervised Learning for Classification",
        [
            ("비지도 군집화 (Unsupervised Clustering)", "Unsupervised Clustering"),
            ("보상 기반 정책 강화학습", "Reinforcement Learning with Policy Gradients"),
            ("단순 주성분 분석 (PCA)", "Principal Component Analysis (PCA)")
        ],
        "지도학습(Supervised Learning)은 입력(X)과 정답 레이블(Y)이 쌍으로 제공되는 데이터셋을 사용하며, 이산형 카테고리를 예측하는 작업을 '분류(Classification)'라고 합니다."
    ),
    (
        "Supervised Learning - Regression", "지도학습: 회귀(Regression)",
        "연속적인 숫자 값(예: 주택 매매가, 설비 고장 잔여 수명, 분기별 매출액)을 예측하기 위해 정답 레이블을 사용하는 지도학습 작업은 무엇입니까?",
        "When an ML pipeline uses historical labeled training records to predict a continuous numeric quantity (such as monetary cost or remaining useful life), which task is executed?",
        "지도학습의 회귀 (Supervised Regression)", "Supervised Learning for Regression",
        [
            ("K-Means 군집화", "K-Means Clustering"),
            ("이진 분류 (Binary Classification)", "Binary Classification"),
            ("토큰 단위 오토리그레시브 텍스트 생성", "Autoregressive token generation")
        ],
        "회귀(Regression)는 과거의 연속적인 수치 레이블을 기반으로 새로운 입력 데이터의 연속적인 숫자 값을 예측하는 지도학습 기법입니다."
    ),
    (
        "Unsupervised Learning - Clustering", "비지도학습: 군집화(Clustering)",
        "사전에 정답 레이블이 전혀 없는 대규모 고객 데이터에서 유사한 구매 성향을 가진 잠재 세그먼트 그룹을 자동으로 발견하는 데 적합한 학습 방식은 무엇입니까?",
        "Which paradigm discovers latent structural patterns and natural subgroupings in unlabelled datasets without any ground-truth target column?",
        "비지도 군집화 (Unsupervised Clustering - e.g., K-Means)", "Unsupervised Clustering (e.g., K-Means)",
        [
            ("지도 선형 회귀", "Supervised Linear Regression"),
            ("결정론적 다중 분류", "Deterministic Multi-class Classification"),
            ("프롬프트 기반 Few-shot 인-컨텍스트 러닝", "Few-shot In-Context Learning")
        ],
        "비지도학습(Unsupervised Learning)은 정답 레이블 없이 데이터 자체의 기하학적 거리나 확률 분포를 분석하여 유사한 그룹으로 묶는 군집화(Clustering) 등에 사용됩니다."
    ),
    (
        "Reinforcement Learning (RL)", "강화학습: 보상과 페널티",
        "에이전트가 주어진 환경(Environment)과 지속적으로 상호작용하며 시행착오를 통해 누적 보상(Reward)을 최대화하는 최적의 행동 정책을 학습하는 기법은 무엇입니까?",
        "Which machine learning approach trains an autonomous agent to optimize long-term cumulative rewards through trial-and-error interactions within a dynamic environment?",
        "강화학습 (Reinforcement Learning)", "Reinforcement Learning (RL)",
        [
            ("정적 비지도 차원 축소", "Static Unsupervised Dimensionality Reduction"),
            ("지도 회귀 분석", "Supervised Regression Analysis"),
            ("데이터 라벨링 크라우드소싱", "Manual Data Annotation Crowdsourcing")
        ],
        "강화학습(RL)은 환경 내에서 상태(State), 행동(Action), 보상(Reward)을 바탕으로 에이전트가 최선의 정책(Policy)을 찾아가는 학습 메커니즘으로, 로봇 제어나 LLM 정렬(RLHF)에 사용됩니다."
    ),
    (
        "Feature Engineering - Imputation", "결측치 대체 (Imputation)",
        "수집된 센서 및 사용자 데이터셋에 누락된 결측치(Missing Values)가 다수 존재할 때, 데이터 손실 없이 모델 학습을 가능하게 하는 올바른 전처리 조치는 무엇입니까?",
        "When raw enterprise datasets contain null or missing numeric fields, which feature engineering process fills in values using statistical methods like mean or median?",
        "결측치 대체 (Data Imputation using Mean/Median)", "Data Imputation using statistical techniques (Mean/Median)",
        [
            ("데이터셋 전체 테이블을 즉시 영구 삭제", "Dropping the entire production database table"),
            ("결측치를 임의의 극단값 9999999로 강제 치환", "Hardcoding arbitrary extreme values like 9999999"),
            ("결측치 행들을 테스트 데이터에만 전부 몰아넣기", "Moving all missing records exclusively into the test set")
        ],
        "특성 공학의 결측치 대체(Imputation)는 수치형 데이터의 평균, 중앙값 또는 머신러닝 예측 알고리즘을 사용하여 누락된 데이터를 보완함으로써 학습 데이터의 품질과 크기를 보존합니다."
    ),
    (
        "Feature Engineering - One-Hot Encoding", "원-핫 인코딩 (One-Hot Encoding)",
        "명목형 범주형 데이터('서울', '부산', '대구')처럼 크기나 순서가 없는 텍스트 변수를 선형 모델이 왜곡 없이 학습할 수 있도록 변환하는 기법은 무엇입니까?",
        "Which encoding converts nominal categorical strings without ordinal hierarchy into binary (0 or 1) indicator columns?",
        "원-핫 인코딩 (One-Hot Encoding)", "One-Hot Encoding",
        [
            ("임의의 알파벳 순서 정수 라벨 부여 (0, 1, 2)", "Arbitrary ordinal label encoding implying false hierarchy"),
            ("Min-Max 정규화만 단독 적용", "Applying Min-Max scaling directly to text strings"),
            ("텍스트 문자열의 글자 수를 그대로 사용", "Using character string length as numerical proxy")
        ],
        "원-핫 인코딩은 순서가 없는 명목형 범주를 각 범주별 0 또는 1의 독립된 이진 열로 변환하여 모델이 잘못된 크기 순서(예: 대구 > 부산)를 학습하지 않도록 방지합니다."
    ),
    (
        "Feature Scaling - Standardization vs Normalization", "스케일링: 정규화 및 표준화",
        "서로 단위와 값의 범위가 극단적으로 다른 여러 수치형 특성(예: 연령 20~80, 연봉 3천만~2억)을 경사하강법 기반 모델에 입력하기 전 수행해야 하는 필수 전처리는 무엇입니까?",
        "When input features have vastly different numeric scales, which preprocessing technique prevents features with larger magnitudes from dominating model weights?",
        "특성 스케일링 (Feature Scaling - Min-Max Normalization 또는 StandardScaler)", "Feature Scaling (Min-Max Normalization or Z-score Standardization)",
        [
            ("특성들의 소수점을 모두 버리고 정수로 반올림", "Truncating all floating-point decimals to zero"),
            ("큰 숫자를 가진 특성만 모델 훈련에서 무조건 제거", "Dropping any feature exceeding 1000 in absolute magnitude"),
            ("데이터셋 순서를 무작위로 100번 섞기", "Shuffling the dataset rows 100 times without scaling")
        ],
        "특성 스케일링(Min-Max 정규화 또는 Z-score 표준화)은 서로 다른 범위의 수치형 변수들을 유사한 스케일로 맞춰주어 경사하강법의 수렴 속도를 높이고 특정 대형 변수의 가중치 독점을 막아줍니다."
    ),
    (
        "Overfitting - High Variance Mitigation", "과적합(Overfitting) 진단 및 해결책",
        "훈련 데이터셋에 대한 모델 손실은 0에 가까우나, 새로운 검증 데이터셋에 대한 오차가 급격히 치솟는 과적합(Overfitting / High Variance)을 해결하기 위한 최선의 조치는 무엇입니까?",
        "When an ML model achieves near-perfect accuracy on training data but performs poorly on validation data, which strategy effectively mitigates this overfitting?",
        "L1/L2 규제(Regularization), 드롭아웃(Dropout) 적용 및 훈련 데이터 증강", "Applying L1/L2 regularization, dropout, and collecting additional training data",
        [
            ("모델 신경망 레이어 수를 10배로 추가 증설", "Increasing model parameters and hidden layers by tenfold"),
            ("검증 데이터셋을 훈련 데이터셋과 동일하게 복제", "Copying validation records directly into the training partition"),
            ("특성 엔지니어링으로 수천 개의 다항식 파생 변수 추가", "Adding thousands of complex polynomial interaction features")
        ],
        "과적합(High Variance)은 모델이 훈련 데이터의 노이즈까지 과도하게 암기했을 때 발생하며, 가중치에 페널티를 주는 규제(L1/L2), 드롭아웃, 조기 종료, 데이터 증강 등으로 완화할 수 있습니다."
    ),
    (
        "Underfitting - High Bias Mitigation", "과소적합(Underfitting) 진단 및 해결책",
        "모델이 훈련 데이터와 검증 데이터 모두에서 매우 높은 오차율을 보이며 기본적인 데이터 패턴조차 학습하지 못하는 과소적합(Underfitting / High Bias) 시 올바른 해결 방안은 무엇입니까?",
        "When a model exhibits unacceptably high error on both training and validation sets due to excessive architectural simplicity, which action resolves the underfitting?",
        "더 복잡하고 표현력이 높은 모델 아키텍처 도입 및 유의미한 특성 추가", "Increasing model capacity (more complex architecture) and engineering more informative features",
        [
            ("L1/L2 규제 페널티 강도를 최대치로 상향", "Aggressively increasing regularization penalty weights"),
            ("훈련 데이터의 절반을 무작위로 삭제하여 크기 축소", "Discarding 50% of training data points"),
            ("에폭(Epochs)을 1회만 돌리고 즉시 훈련 종료", "Limiting training strictly to a single epoch")
        ],
        "과소적합(High Bias)은 모델이 데이터의 복잡도를 표현하기에 너무 단순할 때 발생하므로, 모델의 용량(Capacity)을 늘리거나 더 많은 특성을 발굴하고 훈련 시간을 늘려야 합니다."
    ),
    (
        "Classification Metrics - Recall (Sensitivity)", "재현율(Recall) 최적화: 치명적 누락 방지",
        "실제 사기 거래나 악성 종양 환자를 정상으로 오진하는 False Negative(제2종 오류)가 인간 생명이나 막대한 재무 손실을 초래할 때, 최우선으로 극대화해야 하는 지표는 무엇입니까?",
        "In mission-critical scenarios where failing to identify positive cases (False Negatives - e.g., cancer or financial fraud) carries severe risks, which metric must be maximized?",
        "재현율 (Recall / Sensitivity = TP / (TP + FN))", "Recall (Sensitivity = TP / (TP + FN))",
        [
            ("정밀도 (Precision)", "Precision"),
            ("평균 제곱 오차 (MSE)", "Mean Squared Error (MSE)"),
            ("단순 정확도 (Accuracy)", "Simple Accuracy without threshold tuning")
        ],
        "재현율(Recall)은 실제 Positive인 전체 사례 중 모델이 놓치지 않고 찾아낸 비율입니다. False Negative의 비용이 치명적인 질병 진단이나 금융 사기 탐지에서는 Recall을 최우선 극대화해야 합니다."
    ),
    (
        "Classification Metrics - Precision", "정밀도(Precision) 최적화: 거짓 양성 방지",
        "중요한 업무용 정상 이메일이 스팸 편지함으로 잘못 분류(False Positive)되어 중요한 비즈니스 기회를 놓치는 것을 극도로 방지해야 할 때 우선시할 지표는 무엇입니까?",
        "When mistakenly classifying a negative instance as positive (False Positive - e.g., legitimate email flagged as spam) has high business cost, which metric takes priority?",
        "정밀도 (Precision = TP / (TP + FP))", "Precision (TP / (TP + FP))",
        [
            ("재현율 (Recall)", "Recall"),
            ("평균 절대 오차 (MAE)", "Mean Absolute Error (MAE)"),
            ("펄플렉서티 (Perplexity)", "Perplexity")
        ],
        "정밀도(Precision)는 모델이 Positive라고 예측한 것들 중 실제로 정답인 비율입니다. False Positive를 최소화해야 하는 스팸 필터링이나 법적 문서 증거 채택 등에서 가장 중요합니다."
    ),
    (
        "Classification Metrics - F1 Score", "F1 점수 (F1 Score)와 불균형 데이터",
        "양성 클래스가 전체 데이터의 0.1% 미만인 극심한 불균형 데이터셋에서 단순 정확도(Accuracy)의 착시를 방지하기 위해 정밀도와 재현율의 조화 평균을 계산하는 지표는 무엇입니까?",
        "Which evaluation metric computes the harmonic mean of precision and recall to provide a robust performance measure on highly imbalanced datasets?",
        "F1 점수 (F1 Score)", "F1 Score (Harmonic Mean of Precision and Recall)",
        [
            ("단순 산술 평균 정확도", "Simple Arithmetic Accuracy"),
            ("결정계수 (R-squared)", "Coefficient of Determination (R-squared)"),
            ("MSE (Mean Squared Error)", "Mean Squared Error (MSE)")
        ],
        "F1 Score는 Precision과 Recall의 조화 평균(Harmonic Mean)으로, 클래스 불균형이 극심한 상황에서 한쪽으로 치우친 예측 모델의 성능을 객관적으로 평가하는 표준 척도입니다."
    ),
    (
        "Regression Metrics - RMSE vs MAE", "회귀 지표: RMSE와 이상치 페널티",
        "주택 매매가 예측 회귀 모델에서 작은 오차보다 매우 큰 예측 오차(이상치)에 대해 제곱 연산을 통해 훨씬 더 무거운 페널티를 부여하고자 할 때 적합한 지표는 무엇입니까?",
        "Which regression metric squares error residuals, thereby penalizing large outlier errors significantly more severely than smaller errors?",
        "평균 제곱근 오차 (RMSE: Root Mean Squared Error)", "Root Mean Squared Error (RMSE)",
        [
            ("평균 절대 오차 (MAE)", "Mean Absolute Error (MAE)"),
            ("분류 혼동 행렬 (Confusion Matrix)", "Confusion Matrix"),
            ("BLEU 점수", "BLEU Score")
        ],
        "RMSE(Root Mean Squared Error)는 오차를 제곱하여 평균을 낸 뒤 루트를 취하므로, 오차가 커질수록 페널티가 기하급수적으로 커져 이상치에 매우 민감하게 반응합니다."
    ),
    (
        "ML Monitoring - Data Drift vs Concept Drift", "운영 모니터링: 데이터 및 개념 드리프트",
        "프로덕션 환경에 배포된 추천 모델에서 시간이 흐름에 따라 고객의 입력 데이터 통계적 분포(P(X))가 변하는 현상을 무엇이라 부르며, 어떤 AWS 도구로 감지합니까?",
        "What term describes the shift in production input data statistical distributions over time, and which Amazon SageMaker capability automatically detects it?",
        "데이터 드리프트 (Data Drift) 및 Amazon SageMaker Model Monitor", "Data Drift detected via Amazon SageMaker Model Monitor",
        [
            ("네트워크 지연 현상 및 AWS Shield", "Network latency spikes monitored via AWS Shield"),
            ("서버리스 콜드 스타트 및 AWS X-Ray", "Serverless cold starts monitored via AWS X-Ray"),
            ("하드웨어 오버히팅 및 AWS Compute Optimizer", "Hardware degradation monitored via AWS Compute Optimizer")
        ],
        "입력 데이터의 통계적 분포가 훈련 시점과 다르게 변하는 현상을 '데이터 드리프트(Data Drift)'라고 하며, Amazon SageMaker Model Monitor가 이를 실시간으로 감지하여 재학습을 유도합니다."
    )
]

# ==============================================================================
# 도메인 2: 생성형 AI의 기초 (Fundamentals of Generative AI) - 24%
# ==============================================================================
D2_TAXONOMY = [
    (
        "Discriminative vs Generative AI", "판별 모델 vs 생성 모델",
        "주어진 입력 데이터의 조건부 확률 경계면을 학습하여 라벨을 분류하는 판별 모델과 달리, 데이터 자체의 결합 분포를 학습하여 새로운 원본 산출물을 합성하는 AI는 무엇입니까?",
        "Unlike discriminative models that learn decision boundaries to predict labels, which paradigm learns joint probability distributions to synthesize entirely new artifacts?",
        "생성형 AI (Generative AI)", "Generative AI",
        [
            ("전통적인 통계적 K-최근접 이웃(KNN) 분류기", "Traditional KNN classification modeling"),
            ("단순 데이터베이스 정규화 파이프라인", "Relational schema third-normal form normalization"),
            ("선형 판별 분석기(LDA)", "Linear Discriminant Analysis (LDA)")
        ],
        "생성형 AI(Generative AI)는 데이터의 잠재 표현과 분포를 학습하여 기존에 존재하지 않던 새로운 텍스트, 이미지, 오디오, 코드 등의 콘텐츠를 능동적으로 합성합니다."
    ),
    (
        "Transformer & Self-Attention", "트랜스포머 아키텍처와 셀프 어텐션",
        "기존 RNN 계열의 순차 처리 한계를 극복하고 대규모 병렬 연산을 가능하게 하였으며, 문장 내 모든 단어 간의 의미적 관계를 동시에 가중치로 계산하는 메커니즘은 무엇입니까?",
        "Which architectural mechanism allows Transformer models to compute relationships across all tokens simultaneously in parallel, capturing long-range contextual dependencies?",
        "셀프 어텐션 메커니즘 (Self-Attention Mechanism)", "Self-Attention Mechanism",
        [
            ("단순 합성곱 풀링 레이어", "Convolutional Max-Pooling Layers"),
            ("마르코프 연쇄 전이 확률", "Markov Chain Transition Probabilities"),
            ("결정 트리 지니 불순도 분할", "Gini Impurity Decision Splitting")
        ],
        "트랜스포머의 셀프 어텐션(Self-Attention)은 입력 시퀀스의 모든 단어가 서로에게 미치는 영향도를 병렬 행렬 연산으로 계산하여 장거리 문맥을 완벽하게 파악합니다."
    ),
    (
        "Tokens & Context Window Constraints", "토큰과 컨텍스트 윈도우 한계",
        "파운데이션 모델이 한 번의 요청과 응답 상호작용에서 동시에 기억하고 참조할 수 있는 최대 입력 및 출력 토큰 용량을 의미하는 용어는 무엇입니까?",
        "Which term specifies the maximum total number of tokens (input prompt plus output generation) a foundation model can process in a single conversational turn?",
        "컨텍스트 윈도우 (Context Window)", "Context Window",
        [
            ("가중치 감쇠율 (Weight Decay)", "Weight Decay Rate"),
            ("임베딩 차원수 (Embedding Dimension)", "Embedding Dimension Size"),
            ("배치 크기 (Batch Size)", "Mini-batch Size")
        ],
        "컨텍스트 윈도우(Context Window)는 LLM이 한 번의 추론 주기에서 문맥을 유지하고 참조할 수 있는 최대 토큰 한도이며, 이를 초과하는 과거 대화는 참조되지 않습니다."
    ),
    (
        "Inference Parameters - Temperature", "추론 파라미터: Temperature",
        "금융 보고서 수치 추출이나 소스코드 생성처럼 창의성과 무작위성을 철저히 억제하고 가장 일관되고 결정론적인 답변을 얻고자 할 때 Temperature 설정값은 어떻게 해야 합니까?",
        "For deterministic use cases such as code synthesis or strict financial extraction where random creativity must be eliminated, how should the temperature parameter be set?",
        "0에 매우 가까운 낮은 값으로 설정 (예: 0.0 ~ 0.2)", "Set temperature close to 0 (e.g., 0.0 to 0.2)",
        [
            ("지원되는 최고치인 1.0 또는 2.0으로 상향 설정", "Set temperature to maximum allowable value (1.0 - 2.0)"),
            ("Temperature 파라미터를 완전히 삭제하고 음수로 지정", "Set temperature to a negative integer like -1.0"),
            ("Top-P를 0으로 만들고 Temperature를 100으로 설정", "Set temperature to 100 with Top-P at 0")
        ],
        "Temperature는 출력 토큰 확률 분포의 평탄화 정도를 조절합니다. 0에 가까울수록(0.0~0.2) 가장 확률이 높은 단어만 선택하는 결정론적이고 사실적인 출력을 보장합니다."
    ),
    (
        "Inference Parameters - Top-P (Nucleus Sampling)", "추론 파라미터: Top-P (핵 샘플링)",
        "누적 확률 합계가 특정 임계값 P(예: 0.9)에 도달할 때까지의 상위 확률 단어 집합 내에서만 다음 토큰을 샘플링하여 엉뚱한 단어 출현을 차단하는 기법은 무엇입니까?",
        "Which sampling technique restricts next-token selection dynamically to the smallest candidate pool whose cumulative probability exceeds threshold P?",
        "Top-P (Nucleus Sampling)", "Top-P (Nucleus Sampling)",
        [
            ("Top-K 하드코딩 필터링", "Fixed Top-K Filtering only"),
            ("무작위 균등 샘플링", "Uniform Random Sampling"),
            ("그리디 탐색 (Greedy Search)", "Pure Greedy Decoding without sampling")
        ],
        "Top-P(핵 샘플링)는 누적 확률이 P에 도달하는 상위 후보 단어 풀만을 동적으로 선별하여, 문맥에 맞지 않는 엉뚱한 단어 생성을 통제하면서도 자연스러운 다양성을 부여합니다."
    ),
    (
        "Prompt Engineering - Zero-Shot vs Few-Shot", "프롬프트: Zero-Shot vs Few-Shot",
        "모델의 가중치를 일체 수정하지 않고, 프롬프트 지문 내에 2~3개의 모범적인 입-출력 예시(Exemplars)를 제공하여 원하는 형식의 JSON 응답을 유도하는 기법은 무엇입니까?",
        "Which prompt engineering strategy incorporates several input-output demonstration exemplars directly within the context prompt to guide model formatting without weight updates?",
        "Few-Shot 프롬프팅 (Few-Shot Prompting)", "Few-Shot Prompting",
        [
            ("전체 파라미터 파인튜닝", "Full-Parameter Fine-Tuning"),
            ("제로샷 프롬프팅 (Zero-Shot Prompting)", "Zero-Shot Prompting"),
            ("기초 모델 사전 훈련 (Pre-training)", "Foundation Model Pre-Training")
        ],
        "Few-shot 프롬프팅은 프롬프트 안에 소수의 모범 예시를 제공하여 모델이 출력 형식(예: JSON 구조, 특정 분류 태그)을 정확히 모방하도록 유도하는 효율적인 기법입니다."
    ),
    (
        "Prompt Engineering - Chain of Thought (CoT)", "생각의 사슬: Chain-of-Thought",
        "복잡한 다단계 논리 추론이나 수학 계산 문제를 풀 때, 모델에게 '단계별로 생각하라(Let's think step by step)'는 지침을 주어 중간 추론 과정을 명시하게 하는 기법은 무엇입니까?",
        "Which prompt technique explicitly instructs the model to break down complex reasoning into intermediate steps before stating the final answer?",
        "생각의 사슬 프롬프팅 (Chain-of-Thought - CoT)", "Chain-of-Thought (CoT) Prompting",
        [
            ("방향성 자극 제로샷 프롬프팅", "Directional Zero-shot Prompting"),
            ("파라미터 양자화 (Quantization)", "Weight Quantization"),
            ("임베딩 코사인 유사도 검색", "Vector Cosine Search")
        ],
        "Chain-of-Thought(CoT)는 모델이 복잡한 문제를 한 번에 맞추려 하지 않고 단계별 추론 과정을 거치도록 유도하여 논리적 비약과 환각을 크게 줄이는 기법입니다."
    ),
    (
        "Prompt Engineering - System Prompt & Role Playing", "시스템 프롬프트와 페르소나",
        "AI 모델에게 '당신은 20년 경력의 금융 규제 변호사입니다'와 같은 전문 페르소나, 응답 어조, 금지 규정, 보안 준수 지침을 사전에 강제하는 최상위 지시문은 무엇입니까?",
        "Which element sets the global persona, behavioral boundaries, response formatting constraints, and safety guardrails across an entire LLM session?",
        "시스템 프롬프트 (System Prompt)", "System Prompt (Role/Persona Prompting)",
        [
            ("사용자 쿼리 (User Prompt)", "User Prompt"),
            ("추론 배치 파라미터", "Batch Size Hyperparameter"),
            ("KMS 데이터 암호화 키", "AWS KMS Key Specifier")
        ],
        "시스템 프롬프트(System Prompt)는 대화 세션의 최상위에서 AI의 역할, 답변 톤앤매너, 금지된 주제, 필수 준수 사항 등을 사전에 규정하는 역할을 합니다."
    ),
    (
        "Model Customization Spectrum - RAG vs Fine-Tuning", "커스터마이징: RAG vs Fine-Tuning",
        "매일 빈번하게 업데이트되는 사내 기밀 문서를 모델에 반영해야 하며, 모델 재학습 비용을 들이지 않고 명확한 원본 출처(Citations)를 제공해야 할 때 가장 최적의 아키텍처는 무엇입니까?",
        "When an enterprise must provide answers grounded in proprietary internal documents that change daily, requiring verifiable citations without model retraining, which approach is best?",
        "검색 증강 생성 (RAG: Retrieval-Augmented Generation)", "Retrieval-Augmented Generation (RAG)",
        [
            ("매일 밤 기초 모델 전체 사전 훈련 (Pre-training from scratch)", "Nightly pre-training from scratch"),
            ("공개 인터넷 데이터로 전체 가중치 파인튜닝", "Full-parameter fine-tuning on public web archives"),
            ("추론 파라미터 Temperature를 1.5로 올리기", "Increasing temperature to 1.5 during inference")
        ],
        "RAG(검색 증강 생성)는 최신 외부/사내 문서를 벡터 스토어에서 실시간으로 검색하여 프롬프트의 컨텍스트로 주입하므로, 모델 재학습 없이 최신 데이터 반영과 출처 인용이 가능합니다."
    ),
    (
        "PEFT & LoRA (Low-Rank Adaptation)", "매개변수 효율적 파인튜닝 (PEFT/LoRA)",
        "수십억 개의 파라미터를 가진 거대 모델의 원본 가중치는 동결(Freeze)하고, 극소수의 저차원 어댑터 가중치 행렬만을 학습시켜 연산 비용과 메모리를 극적으로 절감하는 기법은 무엇입니까?",
        "Which parameter-efficient fine-tuning technique freezes pre-trained model weights and injects trainable rank-decomposition matrices, cutting GPU overhead by over 90%?",
        "LoRA (Low-Rank Adaptation / PEFT)", "Low-Rank Adaptation (LoRA / PEFT)",
        [
            ("전체 모델 사전 훈련 (Full Pre-training)", "Full Foundation Model Pre-training"),
            ("그리디 디코딩 (Greedy Decoding)", "Greedy Decoding"),
            ("k-최근접 이웃 탐색", "k-Nearest Neighbors Search")
        ],
        "PEFT의 대표 기법인 LoRA는 기존의 방대한 사전 훈련 가중치는 그대로 고정하고, 소형 저차원 어댑터만 학습시켜 GPU 메모리와 컴퓨팅 비용을 극적으로 절감합니다."
    ),
    (
        "RAG - Chunking & Vector Embeddings", "RAG 파이프라인: 청킹과 벡터 임베딩",
        "RAG 시스템 구축 시 방대한 PDF 매뉴얼을 의미 있는 일정한 토큰 크기로 분할하고, 이를 고차원 실수 벡터로 변환하여 시맨틱 유사도 검색을 가능하게 하는 기술은 무엇입니까?",
        "In a RAG ingestion workflow, which combination divides large documents into optimal passages and converts them into dense numerical representations capturing semantic meaning?",
        "문서 청킹(Chunking) 및 벡터 임베딩 (Vector Embeddings)", "Document Chunking and Vector Embeddings",
        [
            ("단순 텍스트 압축(ZIP) 및 Base64 인코딩", "ZIP text compression and Base64 encoding"),
            ("SQL 테이블 드롭 및 관계형 정규화", "Dropping SQL schema and table normalization"),
            ("단어 빈도수 단순 알파벳 순서 정렬", "Sorting words alphabetically without vectors")
        ],
        "RAG 파이프라인에서는 긴 문서를 검색 단위인 청크(Chunk)로 분할한 뒤, 임베딩 모델(예: Amazon Titan Text Embeddings)을 통해 의미 벡터로 변환하여 벡터 DB에 색인합니다."
    ),
    (
        "RAG - Vector Database & Similarity Search", "벡터 데이터베이스와 코사인 유사도",
        "사용자의 질문 벡터와 색인된 사내 지식 문서 청크 벡터 간의 의미적 각도 거리를 측정하여 가장 관련성이 높은 상위 k개의 문서를 초고속으로 검색하는 수학적 척도는 무엇입니까?",
        "Which similarity metric evaluates the angular cosine of the angle between two normalized high-dimensional vectors to measure semantic relatedness in a vector store?",
        "코사인 유사도 (Cosine Similarity)", "Cosine Similarity",
        [
            ("단순 유클리드 좌표계 곱셈", "Raw coordinate multiplication without normalization"),
            ("이진 해시 충돌 횟수", "Binary hash collision count"),
            ("문자열 철자 일치 개수(Levenshtein Distance)", "Levenshtein edit character distance")
        ],
        "벡터 데이터베이스에서는 질문과 문서 임베딩 벡터 간의 코사인 유사도(Cosine Similarity)를 계산하여, 단순 키워드 일치가 아닌 의미론적(Semantic) 유사도를 기반으로 최적 청크를 검색합니다."
    ),
    (
        "Hallucination - Cause & Mitigation", "환각(Hallucination)의 원인과 방지 전략",
        "LLM이 학습 데이터에 없는 사실에 대해 확신을 가지고 허위 정보를 그럴듯하게 지어내는 환각(Hallucination) 현상을 방지하기 위한 가장 효과적인 조치는 무엇입니까?",
        "When an LLM generates factually false or unverified claims with high confidence, which combination of architectural mitigations directly curbs this hallucination?",
        "RAG 구축, Temperature 하향(0.0~0.2), 출처 요구 및 가드레일 접지성 검증", "Implementing RAG with authoritative docs, lowering temperature, and enabling grounding checks",
        [
            ("Temperature와 Top-P를 최대치로 높여 답변 생성", "Maximizing temperature and top-p parameters"),
            ("가드레일과 시스템 프롬프트를 전면 제거", "Removing all system prompts and safety guardrails"),
            ("훈련 데이터셋에 가짜 데이터를 의도적으로 추가", "Injecting synthetic inaccurate data into training pools")
        ],
        "환각(Hallucination) 완화를 위해서는 신뢰할 수 있는 사내 지식을 RAG로 컨텍스트에 주입하고, Temperature를 낮춰 무작위성을 배제하며, Bedrock Guardrails의 Grounding 검사를 적용해야 합니다."
    )
]

# ==============================================================================
# 도메인 3: 파운데이션 모델의 적용 및 평가 (Applications of FMs) - 28%
# ==============================================================================
D3_TAXONOMY = [
    (
        "Amazon Bedrock - Core Architecture", "Amazon Bedrock: 완전관리형 단일 API",
        "자체 GPU 서버나 인프라를 프로비저닝할 필요 없이, 단일 통일된 API를 통해 업계 최고의 파운데이션 모델들(Anthropic Claude, Meta Llama, Amazon Titan 등)을 서버리스로 제공하는 서비스는 무엇입니까?",
        "Which fully managed AWS service provides unified API access to multiple leading foundation models without managing underlying GPU clusters or instances?",
        "Amazon Bedrock", "Amazon Bedrock",
        [
            ("Amazon EC2 G5 GPU 인스턴스 클러스터", "Amazon EC2 G5 GPU instances"),
            ("Amazon Elastic Beanstalk", "AWS Elastic Beanstalk"),
            ("AWS OpsWorks 스택", "AWS OpsWorks Stacks")
        ],
        "Amazon Bedrock은 서버리스 완전관리형 서비스로, 단일 API 호출을 통해 Anthropic, Meta, Mistral, Cohere, Amazon 등의 최신 파운데이션 모델을 즉시 활용할 수 있습니다."
    ),
    (
        "Bedrock Knowledge Bases", "Bedrock Knowledge Bases: 완전관리형 RAG",
        "S3에 보관된 대규모 PDF/문서를 가리키기만 하면 문서 청킹, 임베딩 생성, OpenSearch Serverless 벡터 스토어 동기화 및 쿼리 검색을 완전 자동으로 수행하는 서비스 기능은 무엇입니까?",
        "Which Amazon Bedrock feature connects directly to Amazon S3 data sources, fully automating document parsing, chunking, embedding, vector store indexing, and retrieval?",
        "Knowledge Bases for Amazon Bedrock", "Knowledge Bases for Amazon Bedrock",
        [
            ("Amazon Rekognition Video", "Amazon Rekognition Video"),
            ("Amazon Polly Neural TTS", "Amazon Polly Neural TTS"),
            ("AWS Glue Streaming ETL", "AWS Glue Streaming ETL")
        ],
        "Knowledge Bases for Amazon Bedrock은 데이터 파이프라인 코딩 없이 S3 문서를 벡터 데이터베이스(OpenSearch Serverless 등)와 자동 동기화하여 완전관리형 RAG를 즉시 구현해 줍니다."
    ),
    (
        "Bedrock Agents", "Bedrock Agents: 자율 에이전트 & Lambda 연동",
        "자연어 요청을 분석하여 다단계 실행 계획을 스스로 수립하고, OpenAPI 스키마로 정의된 Action Groups를 통해 백엔드 AWS Lambda 함수를 실행하여 실제 비즈니스 작업을 완수하는 기능은 무엇입니까?",
        "Which Amazon Bedrock feature breaks down multi-step user tasks, orchestrates logical execution sequences, and invokes AWS Lambda functions via OpenAPI action groups?",
        "Agents for Amazon Bedrock", "Agents for Amazon Bedrock",
        [
            ("Amazon SageMaker Canvas", "Amazon SageMaker Canvas"),
            ("Amazon CloudFront Edge Functions", "Amazon CloudFront Edge Functions"),
            ("AWS Direct Connect", "AWS Direct Connect Gateway")
        ],
        "Agents for Amazon Bedrock은 파운데이션 모델의 추론 능력으로 다단계 계획을 수립하고, AWS Lambda를 호출하여 DB 조회, 주문 예약, 티켓 발급 등의 실무 비즈니스 로직을 자율 실행합니다."
    ),
    (
        "Bedrock Guardrails", "Bedrock Guardrails: 콘텐츠 필터 & PII 마스킹",
        "기업의 윤리 및 보안 정책에 맞춰 증오 발언/폭력 차단, 금융/법률 금지 주제(Denied Topics) 차단, 주민번호 등 민감 PII 자동 마스킹, 프롬프트 인젝션 방어를 수행하는 기능은 무엇입니까?",
        "Which Amazon Bedrock capability enforces enterprise safety policies, filters toxic content, masks sensitive PII, blocks denied topics, and halts prompt injection attacks?",
        "Amazon Bedrock Guardrails", "Amazon Bedrock Guardrails",
        [
            ("Amazon Route 53 DNSSEC", "Amazon Route 53 DNSSEC"),
            ("AWS WAF Rate-based rules only", "AWS WAF Rate-based rules alone"),
            ("Amazon Simple Notification Service", "Amazon Simple Notification Service (SNS)")
        ],
        "Amazon Bedrock Guardrails는 유해 콘텐츠 차단, 비속어 필터, PII 마스킹, 차단 주제 설정, 사실성 접지(Contextual Grounding) 검사를 통해 안전한 생성형 AI 환경을 제공합니다."
    ),
    (
        "Amazon Q Business", "Amazon Q Business: 사내 지식 검색 & IAM/RBAC 준수",
        "SharePoint, Jira, Salesforce, S3 등 40개 이상의 엔터프라이즈 커넥터와 연결되어 사내 문서를 바탕으로 질문에 답변하며, 직원의 기존 사내 IAM/RBAC 접근 권한을 엄격히 준수하는 서비스는 무엇입니까?",
        "Which generative AI enterprise assistant connects to corporate repositories (e.g., SharePoint, Jira, Salesforce) and strictly honors existing employee RBAC permissions?",
        "Amazon Q Business", "Amazon Q Business",
        [
            ("Amazon Q Developer", "Amazon Q Developer"),
            ("Amazon Lex 챗봇", "Amazon Lex"),
            ("Amazon SageMaker Studio Code Editor", "Amazon SageMaker Studio Code Editor")
        ],
        "Amazon Q Business는 기업 데이터 소스에 연결되어 직원의 질문에 정확한 출처와 함께 답변을 생성하며, 각 직원이 실제 열람 권한이 있는 문서만을 바탕으로 응답하도록 보장합니다."
    ),
    (
        "Amazon Q Developer", "Amazon Q Developer: 개발자 코딩 및 취약점 검사",
        "소프트웨어 개발자의 IDE 내에서 실시간 코드 자동 완성, 단위 테스트 생성, 보안 취약점 스캔 및 레거시 Java 코드 버전 업그레이드를 전문으로 지원하는 생성형 AI 도구는 무엇입니까?",
        "Which generative AI assistant operates inside developer IDEs to provide real-time code recommendations, automated vulnerability remediation, and legacy code transformations?",
        "Amazon Q Developer", "Amazon Q Developer",
        [
            ("Amazon Q Business", "Amazon Q Business"),
            ("Amazon Textract", "Amazon Textract"),
            ("Amazon CloudWatch Alarms", "Amazon CloudWatch Alarms")
        ],
        "Amazon Q Developer는 개발자의 코딩 환경(IDE)에 통합되어 실시간 코드 자동완성, 코드 리팩토링, 취약점 스캔 및 수정, 대규모 프레임워크 업그레이드를 지원하는 개발 전문 도우미입니다."
    ),
    (
        "Amazon SageMaker Canvas", "Amazon SageMaker Canvas: 비즈니스 분석가 No-Code ML",
        "프로그래밍 코드 작성이나 ML 전문 지식이 없는 비즈니스 분석가가 그래픽 UI 환경에서 정형 데이터 예측 모델을 학습시키고, 파운데이션 모델 기반 텍스트 요약을 직접 실습할 수 있는 도구는 무엇입니까?",
        "Which visual, no-code environment enables business analysts without ML coding skills to build predictive tabular models and evaluate foundation models visually?",
        "Amazon SageMaker Canvas", "Amazon SageMaker Canvas",
        [
            ("Amazon SageMaker Studio Notebooks", "Amazon SageMaker Studio Notebooks"),
            ("AWS Deep Learning AMIs", "AWS Deep Learning AMIs"),
            ("Amazon EMR Spark Clusters", "Amazon EMR Spark Clusters")
        ],
        "Amazon SageMaker Canvas는 비즈니스 분석가를 위한 시각적 노코드(No-code) 머신러닝 도구로, 클릭만으로 고객 이탈 예측이나 파운데이션 모델 활용을 테스트할 수 있습니다."
    ),
    (
        "Amazon SageMaker JumpStart", "SageMaker JumpStart: 오픈소스 FM 허브",
        "Llama, Mistral, Stable Diffusion 등 최신 오픈소스 및 독점 파운데이션 모델을 사전 훈련된 상태로 검색하여, 전용 인스턴스에 원클릭으로 배포하고 자체 데이터로 파인튜닝할 수 있는 허브는 무엇입니까?",
        "Which Amazon SageMaker machine learning hub enables one-click deployment and fine-tuning of popular open-source and proprietary foundation models on dedicated infrastructure?",
        "Amazon SageMaker JumpStart", "Amazon SageMaker JumpStart",
        [
            ("AWS Artifact", "AWS Artifact"),
            ("Amazon S3 Glacier Vault", "Amazon S3 Glacier Vault"),
            ("Amazon Kendra Index", "Amazon Kendra Index")
        ],
        "Amazon SageMaker JumpStart는 수백 종의 사전 훈련된 파운데이션 모델과 머신러닝 솔루션을 원클릭으로 배포하고 자체 VPC 내에서 안전하게 파인튜닝할 수 있는 허브를 제공합니다."
    ),
    (
        "Turnkey AI - Amazon Textract", "턴키 AI: Amazon Textract 양식/표 추출",
        "스캔된 계약서나 대출 신청서 PDF에서 단순한 글자 인식(OCR)을 넘어 Key-Value 양식 필드와 복잡한 다단 표(Table) 구조를 레이아웃 보존 상태로 추출하는 서비스는 무엇입니까?",
        "Which turnkey AWS AI service intelligently extracts printed text, handwriting, key-value form fields, and structured tables from scanned documents?",
        "Amazon Textract", "Amazon Textract",
        [
            ("Amazon Rekognition", "Amazon Rekognition"),
            ("Amazon Transcribe", "Amazon Transcribe"),
            ("Amazon Polly", "Amazon Polly")
        ],
        "Amazon Textract는 단순 텍스트 추출뿐만 아니라 양식(Form - Key/Value 쌍)과 표(Tables) 구조를 완벽히 인식하여 정형 데이터로 변환하는 전문 문서 인텔리전스 API입니다."
    ),
    (
        "Turnkey AI - Amazon Rekognition", "턴키 AI: Amazon Rekognition 컴퓨터 비전",
        "이미지 및 비디오 미디어에서 객체, 사람 얼굴, 유명인, 부적절한 유해 콘텐츠(성인물, 폭력물)를 감지하고 안면 비교 인증을 수행하는 사전 구축형 AI 서비스는 무엇입니까?",
        "Which pre-trained computer vision service automatically detects objects, faces, celebrities, and inappropriate content, and performs 1:1 facial verification?",
        "Amazon Rekognition", "Amazon Rekognition",
        [
            ("Amazon Comprehend", "Amazon Comprehend"),
            ("Amazon Translate", "Amazon Translate"),
            ("Amazon Kendra", "Amazon Kendra")
        ],
        "Amazon Rekognition은 이미지와 동영상에서 객체 검출, 안면 분석, 유해 콘텐츠 필터링, 텍스트 감지 등을 별도의 모델 훈련 없이 API 호출만으로 처리해 줍니다."
    ),
    (
        "Turnkey AI - Amazon Comprehend", "턴키 AI: Amazon Comprehend 감정/PII 추출",
        "수백만 건의 고객 피드백 텍스트에서 긍정/부정 감정(Sentiment), 주요 엔티티, 키프레이즈를 추출하고 민감한 개인정보(PII)를 자동으로 식별 및 마스킹하는 NLP 서비스는 무엇입니까?",
        "Which turnkey Natural Language Processing (NLP) service uncovers sentiments, entities, key phrases, and personally identifiable information (PII) from unstructured text?",
        "Amazon Comprehend", "Amazon Comprehend",
        [
            ("Amazon Transcribe", "Amazon Transcribe"),
            ("Amazon Forecast", "Amazon Forecast"),
            ("Amazon Personalize", "Amazon Personalize")
        ],
        "Amazon Comprehend는 완전관리형 NLP 서비스로, 텍스트의 감정 분석, 개체명 인식, 주요 구문 추출, PII 탐지 등을 신속하게 수행합니다."
    ),
    (
        "Turnkey AI - Amazon Transcribe & Polly", "턴키 AI: Amazon Transcribe(STT) & Polly(TTS)",
        "고객센터 통화 녹음 오디오를 화자 분리(Speaker Diarization)를 지원하며 텍스트로 변환(STT)하고, 생성된 텍스트를 자연스러운 인간 음성(TTS)으로 합성하는 두 서비스 조합은 무엇입니까?",
        "Which combination of AWS pre-trained services converts recorded customer speech to text (STT) and synthesizes text into natural human speech (TTS)?",
        "Amazon Transcribe (STT) 및 Amazon Polly (TTS)", "Amazon Transcribe (Speech-to-Text) and Amazon Polly (Text-to-Speech)",
        [
            ("Amazon Rekognition 및 Amazon Comprehend", "Amazon Rekognition and Amazon Comprehend"),
            ("Amazon Textract 및 Amazon Translate", "Amazon Textract and Amazon Translate"),
            ("Amazon Lex 및 AWS Lambda 단독", "Amazon Lex and AWS Lambda alone")
        ],
        "Amazon Transcribe는 음성을 텍스트로 변환(STT)하며, Amazon Polly는 텍스트를 자연스러운 인간 음성 오디오로 변환(TTS)하는 턴키 서비스입니다."
    ),
    (
        "GenAI Evaluation - ROUGE Score", "생성형 AI 평가: ROUGE 점수",
        "파운데이션 모델의 긴 문서 요약(Summarization) 품질을 평가하기 위해, 모델이 생성한 요약문과 인간이 작성한 참조 요약문 간의 n-gram 재현율(Recall) 겹침을 측정하는 지표는 무엇입니까?",
        "Which evaluation metric measures n-gram recall overlap between model-generated summaries and human reference summaries, serving as the benchmark for summarization?",
        "ROUGE 점수 (Recall-Oriented Understudy for Gisting Evaluation)", "ROUGE Score",
        [
            ("BLEU 점수", "BLEU Score"),
            ("평균 제곱근 오차 (RMSE)", "Root Mean Squared Error (RMSE)"),
            ("ROC 곡선 아래 면적 (AUC)", "ROC-AUC")
        ],
        "ROUGE는 참조 요약문의 주요 내용이 생성문에 얼마나 잘 포함되었는지를 n-gram 재현율(Recall) 중심으로 평가하는 텍스트 요약 평가의 대표 지표입니다."
    ),
    (
        "GenAI Evaluation - BLEU Score", "생성형 AI 평가: BLEU 점수",
        "기계 번역(Machine Translation) 작업에서 모델이 번역한 문장과 인간 번역가의 참조 번역문 간의 n-gram 정밀도(Precision)와 문장 길이 페널티를 계산하는 대표적인 지표는 무엇입니까?",
        "Which metric calculates n-gram precision with a brevity penalty, comparing machine-generated translations against professional human reference texts?",
        "BLEU 점수 (Bilingual Evaluation Understudy)", "BLEU Score",
        [
            ("ROUGE-L", "ROUGE-L"),
            ("F1 Score", "F1 Score"),
            ("혼동 행렬 (Confusion Matrix)", "Confusion Matrix")
        ],
        "BLEU(Bilingual Evaluation Understudy)는 기계 번역 평가의 표준 지표로, 생성된 번역문이 참조 번역문의 단어들을 얼마나 정확히 포함하고 있는지 정밀도(Precision)를 측정합니다."
    ),
    (
        "GenAI Evaluation - BERTScore & Perplexity", "생성형 AI 평가: BERTScore와 Perplexity",
        "단순 표면적 단어 일치를 넘어 사전 학습된 임베딩 벡터 간 코사인 유사도로 의미적 유사성을 측정하는 지표와, 언어 모델의 유창성을 측정하는 지표(낮을수록 우수)의 조합은 무엇입니까?",
        "Which evaluation pairing measures deep semantic similarity using contextual embeddings and language model next-token prediction uncertainty (lower is better)?",
        "BERTScore (의미적 유사도) 및 Perplexity (혼란도/유창성)", "BERTScore (Semantic Similarity) and Perplexity (Fluency/Uncertainty)",
        [
            ("MAE 및 RMSE", "MAE and RMSE"),
            ("Precision 및 Recall", "Precision and Recall"),
            ("Top-K 및 Top-P", "Top-K and Top-P")
        ],
        "BERTScore는 문맥 임베딩의 코사인 유사도를 계산하여 표면적인 단어가 달라도 의미적 일치도를 정확히 포착하며, Perplexity(PPL)는 언어 모델이 텍스트를 얼마나 유창하게 예측하는지(낮을수록 우수) 측정합니다."
    )
]

# ==============================================================================
# 도메인 4: 책임 있는 AI 가이드라인 (Guidelines for Responsible AI) - 14%
# ==============================================================================
D4_TAXONOMY = [
    (
        "Responsible AI - 5 Pillars", "책임 있는 AI의 5대 기둥",
        "AWS Well-Architected Framework에서 규정하는 책임 있는 AI(Responsible AI)의 5대 핵심 원칙 구성 요소는 무엇입니까?",
        "What are the five core pillars defining Responsible AI governance across the model lifecycle according to AWS guidelines?",
        "공정성, 설명가능성, 투명성, 견고성, 개인정보 보호 및 안전성", "Fairness, Explainability, Transparency, Robustness, Privacy & Safety",
        [
            ("비용 최소화, 서버리스 전환, 빠른 배포, 멀티 클라우드, 오픈소스화", "Cost cutting, serverless, fast shipping, multi-cloud, open source"),
            ("최대 토큰 생성, 온도 극대화, 암호화 비활성화, 수동 감사 생략", "Maximum token count, high temperature, disabling encryption"),
            ("단일 테넌트 격리 배제, 공개 데이터 무단 수집, 로그 삭제", "Public web scraping, disabling CloudTrail, unvetted training")
        ],
        "책임 있는 AI의 5대 기둥은 공정성(Fairness), 설명가능성(Explainability), 투명성(Transparency), 견고성(Robustness), 개인정보 보호 및 안전성(Privacy & Safety)입니다."
    ),
    (
        "SageMaker Clarify - Bias Detection", "SageMaker Clarify: 편향(Bias) 탐지",
        "학습 데이터셋 및 훈련된 모델에서 성별, 연령, 인종 등 보호 속성(Protected Attributes)에 따른 편향(Class Imbalance, Disparate Impact)을 측정하는 전용 AWS 도구는 무엇입니까?",
        "Which Amazon SageMaker feature audits datasets before training and evaluates trained models to detect potential bias across demographic protected groups?",
        "Amazon SageMaker Clarify", "Amazon SageMaker Clarify",
        [
            ("Amazon SageMaker HyperPod", "Amazon SageMaker HyperPod"),
            ("AWS CodeBuild", "AWS CodeBuild"),
            ("Amazon Elastic File System", "Amazon Elastic File System (EFS)")
        ],
        "Amazon SageMaker Clarify는 데이터 준비 단계와 모델 훈련 후 단계 모두에서 다양한 통계적 공정성 메트릭을 계산하여 잠재적 편향(Bias)을 탐지합니다."
    ),
    (
        "Explainability - SHAP Values", "설명가능성(Explainability)과 SHAP 분석",
        "대출 승인/거절과 같은 복잡한 비선형 딥러닝 모델의 예측에 대해 각 입력 특성(소득, 신용점수, 부채)이 결과에 미친 기여도를 공정하게 수치화하는 게임 이론 기반 기법은 무엇입니까?",
        "Which game-theoretic explainability method computes feature attributions (SHAP values) to explain why a black-box model made a specific prediction?",
        "SHAP (Shapley Additive exPlanations) via SageMaker Clarify", "SHAP (Shapley Additive exPlanations) via SageMaker Clarify",
        [
            ("단순 K-평균 군집화 거리 계산", "K-Means centroid distance calculation"),
            ("정적 선형 보간법", "Static linear interpolation"),
            ("무작위 노드 드롭아웃 확률 계산", "Random dropout activation frequency")
        ],
        "SHAP(Shapley Additive exPlanations)는 게임 이론의 섀플리 가치에 기반하여 개별 예측에 대한 각 특성의 양수/음수 기여도를 정확히 계산하여 설명가능성을 제공합니다."
    ),
    (
        "Human-in-the-Loop - Amazon A2I", "인간 참여 루프: Amazon Augmented AI (A2I)",
        "Amazon Textract나 Rekognition의 예측 신뢰도 점수가 사전 정의된 임계값(예: 90%) 미만으로 떨어졌을 때, 작업을 인간 검토자 팀으로 자동 라우팅하는 서비스는 무엇입니까?",
        "Which service orchestrates Human-in-the-Loop (HITL) review workflows, automatically routing low-confidence model predictions to human review teams?",
        "Amazon Augmented AI (Amazon A2I)", "Amazon Augmented AI (Amazon A2I)",
        [
            ("Amazon Simple Queue Service (SQS) DLQ", "Amazon Simple Queue Service (SQS) Dead-Letter Queues"),
            ("Amazon CloudWatch Logs Insights", "Amazon CloudWatch Logs Insights"),
            ("AWS Step Functions Express Workflows only", "AWS Step Functions Express Workflows alone")
        ],
        "Amazon Augmented AI(Amazon A2I)는 AI 모델의 예측 신뢰도가 낮거나 위험도가 높은 비즈니스 시나리오에서 사람(사내 비공개 작업자 풀 등)의 검토와 승인을 거치도록 자동화하는 HITL 서비스입니다."
    ),
    (
        "SageMaker Model Cards", "SageMaker Model Cards: 표준 모델 명세서",
        "모델의 의도된 비즈니스 목적, 훈련 데이터셋 분포, 성능 벤치마크 평가 결과, 윤리적 한계점을 단일 팩트 시트로 정형화하여 규제 감사를 지원하는 문서화 도구는 무엇입니까?",
        "Which governance capability documents model intended uses, training configurations, performance metrics, and ethical limitations into standardized audit records?",
        "Amazon SageMaker Model Cards", "Amazon SageMaker Model Cards",
        [
            ("AWS Systems Manager Parameter Store", "AWS Systems Manager Parameter Store"),
            ("Amazon EC2 Launch Templates", "Amazon EC2 Launch Templates"),
            ("Amazon S3 Lifecycle Policies", "Amazon S3 Lifecycle Policies")
        ],
        "Amazon SageMaker Model Cards는 모델의 수명주기 전반에 걸친 의도된 용도, 한계, 평가 지표를 표준화된 문서로 기록하여 투명성(Transparency)과 감사 대응을 보장합니다."
    ),
    (
        "Bedrock Customer Data Privacy Policy", "Bedrock 고객 데이터 비학습 및 격리 정책",
        "고객이 Amazon Bedrock에 입력한 프롬프트 및 모델 출력 데이터에 대한 AWS의 공식 데이터 프라이버시 및 보안 정책은 무엇입니까?",
        "What is AWS's official data privacy policy regarding customer prompts and responses processed through Amazon Bedrock foundation models?",
        "고객 데이터는 기본 파운데이션 모델 학습에 절대 사용되지 않으며 고객의 안전한 환경 내에 격리됨", "Customer prompts and completions are NEVER used to train base foundation models and remain isolated",
        [
            ("모든 고객 프롬프트는 향후 공개 LLM 학습에 자동으로 재사용됨", "Prompts are automatically harvested to train future public foundation models"),
            ("모든 데이터는 동일 리전의 모든 고객에게 무작위 공유됨", "Data is shared indiscriminately across all region tenants"),
            ("프롬프트는 인터넷 검색엔진에 실시간 공개 인덱싱됨", "Prompts are publicly indexed into web search engines")
        ],
        "Amazon Bedrock은 고객의 프롬프트와 모델 응답을 기본 파운데이션 모델을 훈련하는 데 절대 사용하지 않으며, 제3자 모델 제공자에게도 훈련 목적으로 공유되지 않습니다."
    )
]

# ==============================================================================
# 도메인 5: AI 보안, 컴플라이언스 및 거버넌스 (Security & Governance) - 14%
# ==============================================================================
D5_TAXONOMY = [
    (
        "AI Shared Responsibility Model", "AI 보안 공동 책임 모델",
        "AWS AI 및 파운데이션 모델 환경에서 고객의 고유 책임 영역에 해당하는 항목은 무엇입니까?",
        "Under the AWS Shared Responsibility Model for artificial intelligence, which responsibility belongs exclusively to the customer?",
        "고객 데이터 분류, PII 보호, 적절한 IAM 권한 부여 및 출력물 가드레일 정책 수립", "Customer data classification, IAM least privilege, PII handling, and output guardrail configuration",
        [
            ("기본 GPU 하드웨어 데이터센터 물리적 보안 관리", "Physical security of underlying AWS GPU data centers"),
            ("AWS 하이퍼바이저 펌웨어 패치 적용", "Hypervisor firmware patching and physical host isolation"),
            ("기본 파운데이션 모델 호스팅 인프라 물리적 유지보수", "Hardware maintenance of managed Bedrock model clusters")
        ],
        "AWS 보안 공동 책임 모델에서 물리적 하드웨어 및 기본 인프라는 AWS의 책임이며, 데이터 분류, IAM 접근 권한 통제, PII 보호, 가드레일 설정 등은 고객의 고유 책임입니다."
    ),
    (
        "Data Protection at Rest - AWS KMS CMK", "저장 중 암호화: AWS KMS 고객 관리형 키",
        "S3 지식베이스 문서, 벡터 데이터베이스 및 SageMaker 인스턴스 스토리지에 저장된 모든 AI 데이터를 고객이 직접 키 교체 및 권한을 통제하며 암호화하는 서비스는 무엇입니까?",
        "Which AWS service enables customer control over cryptographic keys to enforce encryption-at-rest across S3 knowledge bases and SageMaker storage volumes?",
        "AWS KMS 고객 관리형 키 (KMS Customer Managed Keys - CMK)", "AWS Key Management Service (AWS KMS) Customer Managed Keys (CMK)",
        [
            ("AWS Certificate Manager 퍼블릭 인증서", "AWS Certificate Manager public SSL certs"),
            ("Amazon CloudFront 키 그룹 단독 적용", "Amazon CloudFront signed URLs alone"),
            ("AWS WAF 웹 ACL 규칙", "AWS WAF Web ACL rules")
        ],
        "AWS KMS의 고객 관리형 키(CMK)를 사용하면 저장 중인 데이터(Data at Rest)에 대한 암호화 키 생성, 교체 주기, 접근 정책을 고객이 완벽하게 통제할 수 있습니다."
    ),
    (
        "Network Isolation - VPC Interface Endpoints", "네트워크 격리: AWS PrivateLink VPC 엔드포인트",
        "프라이빗 서브넷 내의 애플리케이션이 공용 인터넷이나 퍼블릭 게이트웨이를 거치지 않고 오직 AWS 내부 사설 백본망을 통해서만 Amazon Bedrock API를 호출하도록 강제하는 아키텍처는 무엇입니까?",
        "Which networking component allows private VPC resources to securely communicate with Amazon Bedrock API endpoints without traversing the public internet?",
        "AWS PrivateLink 기반 VPC 인터페이스 엔드포인트 (VPC Interface Endpoint)", "VPC Interface Endpoint powered by AWS PrivateLink",
        [
            ("인터넷 게이트웨이(IGW) 연결 및 공용 IP 할당", "Attaching an Internet Gateway with public elastic IPs"),
            ("공개 퍼블릭 NAT 게이트웨이 전면 개방", "Deploying open ingress NAT Gateways"),
            ("공용 S3 웹사이트 호스팅 엔드포인트 사용", "Routing traffic over public S3 website URLs")
        ],
        "AWS PrivateLink 기반의 VPC 엔드포인트를 구성하면 인터넷 게이트웨이 없이도 AWS 내부 전용 네트워크 경로를 통해 Amazon Bedrock API에 안전하게 비공개로 통신할 수 있습니다."
    ),
    (
        "GenAI Threat - Direct Prompt Injection", "생성형 AI 보안 위협: 직접 프롬프트 주입",
        "외부 공격자가 악의적으로 조작된 지시어를 입력하여 시스템 프롬프트의 지침을 무시하도록 강제하고 사내 기밀 문서를 유출하려는 공격과 그 대응책은 무엇입니까?",
        "What type of attack attempts to overwrite an LLM's system instructions through user input, and which AWS feature directly neutralizes it?",
        "직접 프롬프트 주입 (Direct Prompt Injection) 공격 및 Bedrock Guardrails 차단 필터", "Direct Prompt Injection mitigated via Amazon Bedrock Guardrails prompt attack filters",
        [
            ("분산 서비스 거부(DDoS) 공격 및 AWS Shield Advanced 단독", "DDoS attack mitigated via AWS Shield Advanced alone"),
            ("SQL 인젝션 공격 및 Aurora 읽기 복제본", "SQL Injection mitigated via Aurora read replicas"),
            ("데이터 드리프트 및 SageMaker Model Monitor", "Data drift mitigated via SageMaker Model Monitor")
        ],
        "직접 프롬프트 주입(Prompt Injection)은 사용자가 모델의 시스템 지침을 무력화하려는 공격이며, Amazon Bedrock Guardrails의 프롬프트 공격 차단 필터로 실시간 방어할 수 있습니다."
    ),
    (
        "GenAI Threat - Indirect Prompt Injection", "생성형 AI 보안 위협: 간접 프롬프트 주입",
        "RAG 시스템이 외부 웹페이지나 신뢰할 수 없는 타사 문서를 수집할 때, 문서 내부에 은닉된 악의적 지시어가 모델 컨텍스트로 주입되어 오작동을 유발하는 위협은 무엇입니까?",
        "Which security threat occurs when an untrusted external document indexed by a RAG pipeline contains hidden adversarial instructions that hijack model behavior?",
        "간접 프롬프트 주입 (Indirect Prompt Injection)", "Indirect Prompt Injection",
        [
            ("사전 훈련 가중치 손실 (Vanishing Gradient)", "Vanishing Gradient phenomenon"),
            ("단순 하이퍼파라미터 과적합", "Hyperparameter over-tuning"),
            ("하드웨어 GPU 오버히팅", "Hardware GPU thermal throttling")
        ],
        "간접 프롬프트 주입(Indirect Prompt Injection)은 외부 문서나 이메일 내부에 숨겨진 공격 코드가 RAG 검색을 통해 모델 프롬프트로 유입되어 시스템을 조작하려는 고위험 위협입니다."
    ),
    (
        "Data Discovery - Amazon Macie PII Scanning", "데이터 보안: Amazon Macie S3 PII 자동 탐지",
        "AI 모델 파인튜닝이나 RAG 지식베이스 색인 전에, Amazon S3 버킷 내에 신용카드 번호, 주민등록번호 등 개인식별정보(PII)가 무단으로 포함되어 있는지 머신러닝으로 자동 스캔 및 분류하는 서비스는 무엇입니까?",
        "Which security service uses machine learning and pattern matching to discover, classify, and protect sensitive Personally Identifiable Information (PII) stored in Amazon S3?",
        "Amazon Macie", "Amazon Macie",
        [
            ("Amazon Inspector", "Amazon Inspector"),
            ("AWS Artifact", "AWS Artifact"),
            ("Amazon CloudSearch", "Amazon CloudSearch")
        ],
        "Amazon Macie는 S3 내의 방대한 객체를 지속적으로 분석하여 주민등록번호, 신용카드, 여권 번호 등 민감한 PII 데이터를 자동으로 식별하고 경보를 발송하는 전문 데이터 보안 서비스입니다."
    ),
    (
        "Auditing & Logging - AWS CloudTrail", "감사 및 로깅: AWS CloudTrail API 추적",
        "조직 내에서 누가, 언제, 어떤 IAM 자격 증명과 소스 IP로 Amazon Bedrock의 `InvokeModel` API를 호출했는지 모든 호출 내역을 불변의 감사 로그로 영구 기록하는 서비스는 무엇입니까?",
        "Which AWS service captures and logs every API invocation (such as Bedrock InvokeModel) including caller identity, timestamp, and source IP into immutable S3 audit trails?",
        "AWS CloudTrail", "AWS CloudTrail",
        [
            ("Amazon CloudWatch Synthetics", "Amazon CloudWatch Synthetics"),
            ("AWS Trusted Advisor", "AWS Trusted Advisor"),
            ("Amazon Route 53 Traffic Flow", "Amazon Route 53 Traffic Flow")
        ],
        "AWS CloudTrail은 계정 내 모든 AWS 서비스 API 호출 내역(요청자, 시간, IP, 호출 파라미터)을 영구 감사 로그로 기록하여 보안 감사 및 규제 준수의 핵심 기반을 제공합니다."
    ),
    (
        "SageMaker Model Dashboard & Model Registry", "SageMaker Model Dashboard 및 Model Registry",
        "조직에 배포된 모든 ML 모델의 엔드포인트 상태, 데이터 드리프트 발생 여부, 모델 카드 누락을 통합 관제하고, 프로덕션 배포 전 공식 승인(Approval) 워크플로를 강제하는 거버넌스 도구 조합은 무엇입니까?",
        "Which Amazon SageMaker governance capabilities provide centralized visibility into deployed model health/drift and enforce formal production approval gates?",
        "SageMaker Model Dashboard (중앙 관제) 및 SageMaker Model Registry (승인 워크플로)", "Amazon SageMaker Model Dashboard and Model Registry",
        [
            ("Amazon SageMaker Ground Truth 및 Feature Store", "Amazon SageMaker Ground Truth and Feature Store"),
            ("Amazon QuickSight 및 AWS Glue DataBrew", "Amazon QuickSight and AWS Glue DataBrew"),
            ("AWS Budgets 및 Cost Explorer", "AWS Budgets and Cost Explorer")
        ],
        "SageMaker Model Dashboard는 배포된 모든 모델의 품질 및 드리프트를 한눈에 모니터링하며, Model Registry는 모델 버전 관리 및 승인(Approval) 단계를 통제하여 검증되지 않은 모델의 배포를 방지합니다."
    )
]

def build_bank():
    print("==================================================")
    print("🚀 AIF-C01 대규모 실전 문제은행 생성 프로세스 시작")
    print("==================================================")
    
    domain_defs = [
        ("Domain 1", "D1", "도메인 1: AI 및 머신러닝의 기초 (Fundamentals of AI and ML)", D1_TAXONOMY, "questions_domain1.json"),
        ("Domain 2", "D2", "도메인 2: 생성형 AI의 기초 (Fundamentals of Generative AI)", D2_TAXONOMY, "questions_domain2.json"),
        ("Domain 3", "D3", "도메인 3: 파운데이션 모델의 적용 및 평가 (Applications of Foundation Models)", D3_TAXONOMY, "questions_domain3.json"),
        ("Domain 4", "D4", "도메인 4: 책임 있는 AI 가이드라인 (Guidelines for Responsible AI)", D4_TAXONOMY, "questions_domain4.json"),
        ("Domain 5", "D5", "도메인 5: AI 보안, 컴플라이언스 및 거버넌스 (Security, Compliance, and Governance)", D5_TAXONOMY, "questions_domain5.json")
    ]
    
    all_questions_by_domain = {}
    total_generated = 0
    
    for dom_name, dom_code, dom_full_name, taxonomy, filename in domain_defs:
        questions_list = []
        q_counter = 1
        
        # 각 카테고리별로 12개 산업군 맥락과 결합하여 10~12개 문제 생성
        for tax_item in taxonomy:
            cat_en, cat_kr, q_kr_stem, q_en_stem, correct_kr, correct_en, distractors, exp_base = tax_item
            
            # 산업군별 시나리오 10~12개 결합
            for ind_kr, ind_en, data_kr, data_en in INDUSTRIES:
                qid = f"{dom_code}-Q{q_counter:03d}"
                
                # 시나리오가 융합된 지문 생성
                final_q_en = f"[{ind_en}] An enterprise operating with {data_en} is modernizing its operations with AWS AI solutions. {q_en_stem}"
                final_q_kr = f"[{ind_kr}] {data_kr}을(를) 다루는 엔터프라이즈 환경에서 AWS AI 솔루션을 도입하고자 합니다. {q_kr_stem}"
                
                # 선택지 4개 셔플 (정답 1개 + 오답 3개)
                opts_candidates = [
                    {"is_correct": True, "text_en": correct_en, "text_kr": correct_kr}
                ]
                for d_kr, d_en in distractors:
                    opts_candidates.append({"is_correct": False, "text_en": d_en, "text_kr": d_kr})
                
                # 결정론적 셔플 (재현성 보장)
                random.seed(f"{qid}_{cat_en}")
                random.shuffle(opts_candidates)
                
                keys = ["A", "B", "C", "D"]
                final_options = []
                correct_key = "A"
                for idx, opt in enumerate(opts_candidates):
                    k = keys[idx]
                    if opt["is_correct"]:
                        correct_key = k
                    final_options.append({
                        "key": k,
                        "text_en": opt["text_en"],
                        "text_kr": opt["text_kr"]
                    })
                
                detailed_explanation = (
                    f"정답은 {correct_key}입니다.\n\n"
                    f"• **핵심 개념 해설**: {exp_base}\n\n"
                    f"• **실무 비즈니스 분석**: [{ind_kr}] 시나리오에서는 {data_kr}의 요구조건과 제약사항을 만족하기 위해 '{cat_kr}' 관점에서 '{correct_kr}' 방안이 가장 적합하고 AWS Well-Architected 원칙에 부합합니다.\n"
                    f"• 다른 보기들은 문제의 핵심 요구조건을 충족하지 못하거나, 과도한 인프라 관리 오버헤드 또는 보안/거버넌스 위험을 초래합니다."
                )
                
                q_obj = {
                    "id": qid,
                    "domain": dom_name,
                    "domain_name": dom_full_name,
                    "topic_category": cat_en,
                    "key_concept": f"{cat_en}, {cat_kr}",
                    "question_en": final_q_en,
                    "question_kr": final_q_kr,
                    "options": final_options,
                    "correct_answer": correct_key,
                    "explanation_kr": detailed_explanation
                }
                
                questions_list.append(q_obj)
                q_counter += 1
        
        all_questions_by_domain[dom_name] = questions_list
        filepath = os.path.join(QUESTIONS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(questions_list, f, ensure_ascii=False, indent=2)
        
        print(f"✓ {dom_name}: {len(questions_list)}문항 생성 완료 -> {filename}")
        total_generated += len(questions_list)
        
    print(f"\n총 생성된 고유 문제 수: {total_generated}문항")
    
    # ==============================================================================
    # 실전 모의고사 (mock_exam_1.json) 생성: 공식 출제 비중 맞춤 65문항
    # D1(20%): 13문항, D2(24%): 16문항, D3(28%): 18문항, D4(14%): 9문항, D5(14%): 9문항
    # ==============================================================================
    mock_weights = {
        "Domain 1": 13,
        "Domain 2": 16,
        "Domain 3": 18,
        "Domain 4": 9,
        "Domain 5": 9
    }
    
    mock_questions = []
    mock_counter = 1
    
    for dom_name, count in mock_weights.items():
        pool = all_questions_by_domain[dom_name]
        # 서로 다른 카테고리에서 균등하게 샘플링
        cat_map = {}
        for q in pool:
            cat = q["topic_category"]
            if cat not in cat_map:
                cat_map[cat] = []
            cat_map[cat].append(q)
            
        cats = list(cat_map.keys())
        random.seed(42 + mock_counter)
        random.shuffle(cats)
        
        chosen = []
        for c in cats:
            if len(chosen) >= count:
                break
            chosen.append(random.choice(cat_map[c]))
            
        while len(chosen) < count:
            chosen.append(random.choice(pool))
            
        for q in chosen:
            q_copy = dict(q)
            q_copy["id"] = f"MOCK1-{mock_counter:03d}"
            mock_questions.append(q_copy)
            mock_counter += 1
            
    # 전체 65문항 셔플
    random.seed(2026)
    random.shuffle(mock_questions)
    for idx, q in enumerate(mock_questions, 1):
        q["mock_order"] = idx
        
    mock_path = os.path.join(QUESTIONS_DIR, 'mock_exam_1.json')
    with open(mock_path, 'w', encoding='utf-8') as f:
        json.dump(mock_questions, f, ensure_ascii=False, indent=2)
    print(f"✓ 실전 모의고사 (mock_exam_1.json): {len(mock_questions)}문항 공식 비중 맞춤 완료")
    
if __name__ == '__main__':
    build_bank()
