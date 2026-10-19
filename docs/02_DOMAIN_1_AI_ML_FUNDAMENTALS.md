# 도메인 1: AI 및 머신러닝의 기초 (AI and ML Fundamentals)

> **출제 비중: 20%**  
> **핵심 키워드**: AI vs ML vs DL vs GenAI, 지도/비지도/강화학습, ML 수명주기, 특성 공학(Feature Engineering), 분류 및 회귀 평가 지표(Confusion Matrix, Precision/Recall/F1, ROC-AUC, RMSE/MAE), 과적합 및 과소적합 완화 기법.

---

## 1. AI, 머신러닝, 딥러닝, 생성형 AI의 계층 구조

```
┌────────────────────────────────────────────────────────┐
│ Artificial Intelligence (AI)                           │
│  - 인간의 지적 행동과 추론을 모방하는 모든 기술         │
│ ┌────────────────────────────────────────────────────┐ │
│ │ Machine Learning (ML)                              │ │
│ │  - 데이터로부터 패턴을 통계적으로 학습하는 기술    │ │
│ │ ┌────────────────────────────────────────────────┐ │ │
│ │ │ Deep Learning (DL)                             │ │ │
│ │ │  - 다층 인공신경망 기반의 복잡한 비정형 데이터 │ │ │
│ │ │ ┌────────────────────────────────────────────┐ │ │ │
│ │ │ │ Generative AI (GenAI)                      │ │ │ │
│ │ │ │  - 텍스트, 이미지, 코드 등 새로운 콘텐츠   │ │ │ │
│ │ │ │    를 생성하는 딥러닝 분야                 │ │ │ │
│ │ │ └────────────────────────────────────────────┘ │ │ │
│ │ └────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────┘
```

1. **인공지능 (AI)**: 기계가 인간처럼 생각하고 판단하도록 하는 광의의 개념 (규칙 기반 전문가 시스템 포함).
2. **머신러닝 (ML)**: 데이터와 레이블을 바탕으로 알고리즘이 스스로 패턴을 학습 (Linear Regression, Decision Tree, Random Forest, XGBoost 등).
3. **딥러닝 (DL)**: 인간 뇌의 뉴런을 모방한 심층 신경망(Deep Neural Networks) 구조로, 수많은 파라미터를 통해 고차원 특징을 자동으로 학습 (CNN: 컴퓨터 비전, RNN/LSTM/Transformer: 순차 데이터 및 언어).
4. **생성형 AI (GenAI)**: 대규모 데이터로 사전 학습된 파운데이션 모델(FM)을 활용해 신규 콘텐츠를 능동적으로 창조.

---

## 2. 머신러닝 학습 패러다임 (Learning Paradigms)

| 구분 | 핵심 정의 | 주요 알고리즘 / 기법 | 대표적인 비즈니스 활용 사례 |
| :--- | :--- | :--- | :--- |
| **지도학습<br>(Supervised)** | **입력 데이터(X)와 레이블(정답 Y)**을 모두 제공하여 학습 | **분류(Classification)**: Logistic Regression, SVM, Random Forest<br>**회귀(Regression)**: Linear Regression, XGBoost | 고객 이탈 예측, 스팸 메일 필터링, 주택 가격 예측, 의료 영상 질병 판독 |
| **비지도학습<br>(Unsupervised)** | **정답(레이블) 없이** 데이터 자체의 숨겨진 구조, 군집, 상관관계를 탐색 | **군집화(Clustering)**: K-Means, DBSCAN<br>**차원 축소**: PCA, t-SNE<br>**이상 탐지**: Isolation Forest | 고객 세분화(Segmentation), 금융 이상 거래 탐지(Fraud Detection), 추천 시스템 잠재 요인 분석 |
| **준지도학습<br>(Semi-supervised)**| 소량의 정답 데이터와 대량의 비레이블 데이터를 결합하여 학습 | Self-training, Pseudo-labeling | 레이블링 비용이 극히 비싼 의료 데이터, 법률 문서 분석 |
| **강화학습<br>(Reinforcement)** | 에이전트가 환경(Environment)과 상호작용하며 **보상(Reward)을 극대화**하도록 정책(Policy)을 학습 | Q-Learning, PPO, Deep Q-Network (DQN) | 자율주행 차량 제어, 체스/바둑 게임 AI, 주식 자동 트레이딩, **LLM 정렬(RLHF)** |

---

## 3. 머신러닝 수명주기 (ML Lifecycle)

```
[1. 비즈니스 문제 정의] ➔ [2. 데이터 수집 & 라벨링] ➔ [3. 데이터 탐색 & 특성 공학]
                                                            │
[6. 모델 배포 & 모니터링] 🠔 [5. 모델 평가 & 검증] 🠔 [4. 모델 훈련 & 하이퍼파라미터 튜닝]
       │ (데이터 드리프트 발생 시 재학습 피드백)
       └──────────────────────────────────────────────┘
```

1. **데이터 준비 & 특성 공학 (Feature Engineering)**:
   * **결측치 처리 (Imputation)**: 평균(Mean), 중앙값(Median), 최빈값(Mode) 또는 삭제.
   * **범주형 데이터 인코딩**: 원-핫 인코딩(One-Hot Encoding, 명목형 변수), 라벨 인코딩(순서형 변수).
   * **스케일링 & 정규화**: Min-Max Scaling (0~1 범위), Standard Scaling (평균 0, 표준편차 1).
   * **특성 선택(Feature Selection)** 및 **차원 축소(PCA)**: 불필요한 노이즈 특성을 제거하여 과적합 방지 및 연산 가속화.
2. **모델 훈련 및 하이퍼파라미터 튜닝**:
   * 파라미터(Parameter): 모델이 데이터로부터 직접 학습하는 가중치($W$)와 편향($b$).
   * 하이퍼파라미터(Hyperparameter): 학습률(Learning Rate), 에폭(Epochs), 배치 크기(Batch Size), 트리의 최대 깊이 등 인간이 사전에 지정하는 설정값.
   * **Amazon SageMaker Automatic Model Tuning (HPO)**을 통해 최적의 하이퍼파라미터 탐색.
3. **모델 평가 및 검증**:
   * 데이터 분할: Train (60~70%), Validation (15~20%), Test (15~20%).
   * **k-fold 교차 검증 (Cross-Validation)**: 데이터를 k개로 분할하여 검증을 반복함으로써 분산 감소 및 일반화 성능 신뢰도 확보.
4. **배포 및 모니터링**:
   * **Amazon SageMaker Model Monitor**: 운영 중 실시간 데이터 드리프트(Data Drift: 입력 분포 변화) 및 개념 드리프트(Concept Drift: 정답 관계 변화) 자동 감지.

---

## 4. 모델 성능 평가 지표 (Evaluation Metrics)

### A. 분류 모델 (Classification)과 혼동 행렬 (Confusion Matrix)

```
                     실제 (Actual) Positive      실제 (Actual) Negative
예측 (Predict) Positive       TP (True Positive)         FP (False Positive - Type I Error)
예측 (Predict) Negative       FN (False Negative - Type II)  TN (True Negative)
```

1. **정확도 (Accuracy)**:
   $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
   * **주의점**: 클래스 불균형(예: 사기 거래가 0.1%인 경우 전부 정상으로 찍어도 99.9% 정확도) 시 치명적인 착시 발생.
2. **정밀도 (Precision)**:
   $$\text{Precision} = \frac{TP}{TP + FP}$$
   * 모델이 Positive라고 예측한 것 중 진짜 Positive인 비율.
   * **적용 사례**: **스팸 메일 필터링**, 채용 서류 추천 (False Positive를 최소화해야 할 때: 정상 메일이 스팸함에 들어가면 안 됨).
3. **재현율 (Recall / Sensitivity)**:
   $$\text{Recall} = \frac{TP}{TP + FN}$$
   * 실제 Positive인 대상 중 모델이 빠뜨리지 않고 찾아낸 비율.
   * **적용 사례**: **암 환자 진단, 금융 이상/사기 탐지(Fraud)** (False Negative를 극도로 줄여야 할 때: 암 환자를 정상으로 오진하면 사망 위험).
4. **F1 Score**:
   $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
   * 정밀도와 재현율의 **조화 평균(Harmonic Mean)**. 불균형 데이터셋 분류 성능의 가장 표준적인 지표.
5. **ROC-AUC (Receiver Operating Characteristic - Area Under Curve)**:
   * 분류 결정 임계값(Threshold)을 0에서 1까지 변경할 때 나타나는 TPR(재현율)과 FPR의 곡선 아래 면적.
   * 1.0에 가까울수록 완벽한 변별력을 의미하며, 0.5는 동전 던지기(무작위 추측) 수준.

### B. 회귀 모델 (Regression)

1. **MAE (Mean Absolute Error, 평균 절대 오차)**:
   * 예측값과 실제값 차이의 절댓값 평균. 해석이 가장 직관적이고 이상치(Outlier)에 덜 민감함.
2. **MSE (Mean Squared Error) & RMSE (Root Mean Squared Error)**:
   * 오차를 제곱하므로, **큰 오차(이상치)에 대해 훨씬 더 강력한 페널티**를 부여함.
3. **$R^2$ (결정계수, Coefficient of Determination)**:
   * 모델이 데이터의 분산을 얼마나 잘 설명하는지 나타내는 지표 (최대 1.0).

---

## 5. 과적합(Overfitting) vs 과소적합(Underfitting) 완화 전략

| 현상 | 원인 및 상태 | 진단 (Train vs Validation 오차) | 시험 출제 완화 및 해결 방안 |
| :--- | :--- | :--- | :--- |
| **과소적합<br>(Underfitting)** | 모델이 너무 단순하여 데이터의 본질적 패턴을 학습하지 못함 (High Bias). | 훈련 오차도 높고, 검증 오차도 높음. | • 더 복잡한 모델 아키텍처 사용 (예: 선형 회귀 ➔ Random Forest / 신경망)<br>• 추가 특성(Feature) 발굴 및 피처 엔지니어링<br>• 훈련 시간(Epochs) 증가<br>• 규제(Regularization) 강도 완화 |
| **과적합<br>(Overfitting)** | 모델이 훈련 데이터의 노이즈까지 외워버려 새로운 데이터 예측에 실패함 (High Variance). | 훈련 오차는 매우 낮으나, 검증 오차는 급격히 높아짐. | • **더 많은 훈련 데이터 수집** 또는 데이터 증강(Data Augmentation)<br>• **특성 축소**: 중요한 특성만 선택 또는 PCA 적용<br>• **규제 기법(Regularization)**: L1(Lasso), L2(Ridge/Weight Decay)<br>• **드롭아웃 (Dropout)**: 신경망 노드 무작위 비활성화<br>• **조기 종료 (Early Stopping)**: 검증 손실이 증가하기 시작할 때 학습 중단<br>• **k-fold 교차 검증 (Cross-Validation)** 적용 |
