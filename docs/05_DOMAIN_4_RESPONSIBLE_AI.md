# 도메인 4: 책임 있는 AI 가이드라인 (Responsible AI)

> **출제 비중: 14%**  
> **핵심 키워드**: 책임 있는 AI 5대 핵심 기둥(공정성, 설명가능성, 투명성, 견고성, 개인정보보호), 편향(Bias) 유형 및 완화, SageMaker Clarify (SHAP 분석), 인간 참여 루프(HITL / Amazon A2I), SageMaker Model Cards, 지적 재산권(IP) 및 라이선스.

---

## 1. 책임 있는 AI 5대 핵심 기둥 (5 Pillars of Responsible AI)

AWS Well-Architected Framework의 머신러닝 렌즈 및 책임 있는 AI 표준에 따른 5대 원칙:

| 원칙 | 핵심 목표 | 시험 출제 주요 도전 과제 및 완화 방안 |
| :--- | :--- | :--- |
| **1. 공정성<br>(Fairness)** | 성별, 인종, 연령, 종교 등 보호 속성(Protected Attributes)에 따른 불합리한 차별 방지. | • 데이터셋 내 불균형 및 역사적 편향 식별<br>• **SageMaker Clarify**를 통한 편향 메트릭 측정<br>• 리샘플링, 가중치 재조정, 공정성 제약 조건 부여 |
| **2. 설명가능성<br>(Explainability)** | 모델이 특정 예측이나 판단을 내리게 된 이유와 특성(Feature)의 기여도를 인간이 이해할 수 있도록 규명. | • 블랙박스 딥러닝 모델의 해석 한계 극복<br>• **SHAP(Shapley Additive exPlanations)** 및 **LIME** 기법 활용<br>• 대출 거절 사유, 채용 탈락 사유 등의 규제 준수 설명 제공 |
| **3. 투명성<br>(Transparency)** | AI 시스템의 설계, 데이터 출처, 학습 메트릭, 한계점을 명확히 공개하여 신뢰 구축. | • **Amazon SageMaker Model Cards**를 통한 표준 모델 명세서 문서화<br>• **AWS AI Service Cards**를 통한 AWS 사전 훈련 서비스의 의도된 용도 파악 |
| **4. 견고성 및 신뢰성<br>(Robustness)** | 노이즈, 이상치, 적대적 입력(Adversarial attack) 환경에서도 안정적이고 일관된 성능 유지. | • 극단적 엣지 케이스 테스트 및 교차 검증<br>• 지속적인 모델 모니터링 (SageMaker Model Monitor) |
| **5. 개인정보 보호<br>(Privacy & Security)** | 고객의 개인식별정보(PII) 및 민감한 데이터의 유출, 도용, 무단 학습 차단. | • **Amazon Macie** 및 **Comprehend**를 활용한 PII 자동 식별 및 마스킹<br>• **Bedrock Guardrails** 민감 정보 필터 활성화 |

---

## 2. 머신러닝 편향(Bias)의 유형 및 완화 기법

### A. 편향의 대표적인 유형
1. **역사적 편향 (Historical Bias)**: 과거 사회 구조의 불평등이나 차별이 기존 축적된 데이터셋에 그대로 반영된 경우.
2. **표본 편향 (Sampling / Selection Bias)**: 특정 인구 집단이나 클래스가 훈련 데이터셋에 과소 대표(Under-represented)되어 모델이 해당 집단에 대해 오작동하는 경우.
3. **측정 편향 (Measurement Bias)**: 데이터를 수집하거나 라벨링하는 도구, 기준의 결함으로 인해 발생하는 오차.
4. **확증 편향 (Confirmation Bias)**: 데이터 수집자가 사전에 가진 편견이나 가설에 부합하는 데이터만 선별적으로 수집하는 경우.

### B. 편향 탐지 및 완화 (Amazon SageMaker Clarify)
* **훈련 전 편향 탐지 (Pre-training Bias)**:
  * 훈련 데이터셋 내에서 보호 그룹(예: 특정 연령대, 성별)과 기준 그룹 간의 표본 비율 불균형(Class Imbalance - CI), 차이 비율(Difference in Positive Proportions - DPL) 등을 측정.
* **훈련 후 편향 탐지 (Post-training Bias)**:
  * 모델이 생성한 예측 결과에서 그룹 간 정확도 차이, 오차율 차이(Disparate Impact) 등을 측정.
* **완화 기법**:
  * 데이터 수준 완화: 불균형 집단 오버샘플링(SMOTE), 언더샘플링, 데이터 증강.
  * 알고리즘 수준 완화: 손실 함수에 공정성 페널티 부여.

---

## 3. 설명가능성(Explainability)과 SHAP 가치

복잡한 고차원 비선형 모델(XGBoost, 딥러닝)의 예측 결과를 설명하기 위한 대표적인 기법:

```
[최종 모델 예측: 대출 한도 5,000만 원 승인]
  ├── (+) 연간 소득 8,000만 원 (+2,500만 원 기여) ── SHAP Value 양수
  ├── (+) 신용 점수 850점 (+1,500만 원 기여)
  └── (-) 기존 기대출 3건 (-500만 원 기여) ───────── SHAP Value 음수
```

* **전역적 설명가능성 (Global Explainability)**:
  * 전체 데이터셋에 대해 어떤 특성(예: 소득, 연령, 신용도)이 모델의 전반적인 예측에 가장 큰 영향력을 미치는지 특성 중요도(Feature Importance) 파악.
* **국소적 설명가능성 (Local Explainability)**:
  * **특정 개별 고객**의 예측 결과에 대해 각 특성이 얼마만큼 기여했는지 개별 가치를 계산 (예: "이 특정 고객이 대출을 거절당한 주된 이유는 최근 연체 이력 때문임").
* **SHAP (Shapley Additive exPlanations)**:
  * 게임 이론의 섀플리 가치에 기반하여 모든 가능한 특성 조합을 평가함으로써 공정하고 일관된 기여도를 산출 (**SageMaker Clarify의 기본 엔진**).

---

## 4. 인간 참여 루프 (HITL: Human-in-the-Loop)와 Amazon A2I

완전 자동화가 불가능하거나 위험도가 높은 비즈니스 시나리오에서 인간의 전문 지식을 결합하는 구조:

```
[입력 문서 / 이미지] ──> [AWS AI 서비스 / 커스텀 모델] ──> [예측 및 신뢰도 점수 산출]
                                                                  │
                    ┌─────────────────────────────────────────────┴──────────────────┐
                    ▼ (신뢰도 점수 ≥ 95% - 안전)                                     ▼ (신뢰도 점수 < 95% 또는 불일치)
            [자동 처리 완료]                                                [Amazon A2I 워크플로 발동]
                                                                                     │
                                                                                     ▼
                                                                        [인간 검토자에게 라우팅]
                                                                        (Private Team / Crowd)
                                                                                     │
                                                                                     ▼
                                                                           [최종 승인 및 피드백]
```

* **Amazon Augmented AI (Amazon A2I)**:
  * 모델의 신뢰도(Confidence Score)가 사전 정의된 임계값 미만이거나, 민감한 조건이 충족되었을 때 인간 검토자에게 자동으로 작업을 라우팅하는 완전관리형 서비스.
  * **기본 통합 서비스**: Amazon Textract (양식/표 판독), Amazon Rekognition (콘텐츠 검토), Amazon SageMaker 커스텀 모델.
  * **검토자 풀 옵션**:
    1. **Private Workforce**: 사내 보안 규정을 준수해야 하는 임직원 검토 팀.
    2. **Vendor Workforce**: AWS Marketplace에 등록된 타사 전문 검토 인력.
    3. **Amazon Mechanical Turk**: 대규모 크라우드소싱 공개 인력 (비기밀 데이터).

---

## 5. 투명성 거버넌스 및 지적 재산권 (IP)

1. **Amazon SageMaker Model Cards**:
   * 모델의 용도, 아키텍처, 훈련 데이터 세부 정보, 의도된 용도 및 금지된 용도(Out-of-scope use), 성능 벤치마크, 윤리적 고려 사항을 하나의 정형화된 JSON/PDF 문서로 기록 및 관리.
   * 감사(Audit) 및 규제 준수(Compliance)를 입증하는 핵심 수단.
2. **AWS AI Service Cards**:
   * AWS가 직접 개발하여 제공하는 사전 구축 AI 서비스(Rekognition, Textract 등)의 의도된 사용 사례, 한계점, 책임 있는 배포 지침을 공개한 공식 문서.
3. **지적 재산권(IP) 및 저작권 준수**:
   * **데이터 출처(Data Provenance)**: 모델 훈련에 사용된 데이터셋의 저작권, 라이선스, 상업적 이용 가능 여부를 철저히 검증.
   * **Amazon Bedrock의 고객 데이터 보호 정책**:
     * AWS는 **고객의 입력 프롬프트 및 모델 출력을 Amazon 자체의 기본 파운데이션 모델을 훈련하는 데 절대 사용하지 않음**.
     * 고객의 데이터는 고객 전용 격리된 환경 내에 안전하게 유지됨.
