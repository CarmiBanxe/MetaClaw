# AI Model Efficiency Methodology — BANXE EMI
## Методология оценки и мониторинга AI-моделей в регулируемом банке

**Статус:** Advisory — методология для ратификации оператором + Central перед встраиванием в watchdog.
**Область применения:** Ollama-ноды evo1/evo2, LiteLLM-шлюз, алиасы: project-reason / factory-fast/mid/heavy/coder / project-mid.
**Ограничение I-27:** watchdog только измеряет и эскалирует — не переключает модель автономно.
**Compliance-дедлайн:** EU AI Act Art. 9–15, 2 августа 2026.

***

## 1. Таксономия Эффективности

Эффективность AI-модели в проде раскладывается на две ортогональные оси: **операционная** (как быстро и дёшево работает система) и **качественная** (насколько хорошо решает задачу). Смешивать их нельзя: модель может быть операционно быстрой, но качественно бесполезной, и наоборот.[1][2]

### 1a. Операционная Эффективность

**Time To First Token (TTFT)**[3]

\[\mathrm{TTFT} = t_{\text{first\_token}} - t_{\text{request\_sent}}\]

Критична для interactive flows (reasoning-агент, project-reason). Для batch-flows (compliance-проверки) менее важна.

**Time Per Output Token (TPOT) / Throughput**[3]

\[\mathrm{TPOT} = \frac{t_{\text{last\_token}} - t_{\text{first\_token}}}{N_{\text{output\_tokens}}}\]

\[\mathrm{Throughput} = \frac{N_{\text{requests\_completed}}}{\Delta t} \quad [\text{req/s}]\]

**End-to-End Latency (E2E)**

\[\mathrm{Latency}_{E2E} = \mathrm{TTFT} + N_{\text{output}} \cdot \mathrm{TPOT}\]

Для мониторинга используются **перцентили** P50, P95, P99 — среднее значение маскирует хвостовые задержки, критичные для SLA.[4]

**Resource Utilisation**

\[\mathrm{VRAM\_util} = \frac{\mathrm{VRAM\_used}}{\mathrm{VRAM\_total}} \in [0,1]\]

\[\mathrm{Cost\_per\_1k\_tokens} = \frac{\text{GPU-hour cost} \cdot \mathrm{inference\_time\_h}}{N_{\text{tokens\_generated}} / 1000}\]

**Success Rate**

\[\mathrm{SR} = \frac{N_{\text{successful\_completions}}}{N_{\text{total\_requests}}} \in [0,1]\]

где successful = ответ получен, не пустой, без timeout.

### 1b. Эффективность-Качество

Качественная ось — насколько хорошо модель решает **конкретную задачу** алиаса. Единой метрики нет: тип задачи определяет тип метрики (см. §2).[5][6]

Ключевое разделение:
- **Детерминированные задачи** (классификация fraud/AML, extraction): метрики с ground truth.
- **Генеративные задачи** (reasoning, compliance-summary): метрики семантического качества.
- **Calibration** (confidence-gates): отдельная ось, критичная для CICD-порогов 0.75/0.90.

***

## 2. Автоматическое Измерение Качества

### 2a. LLM-as-Judge: Методология и Калибровка

LLM-as-judge — наиболее практичный метод для генеративных задач без однозначного ground truth. Используется «внешняя» модель (judge) для оценки вывода target-модели по структурированному рубрику.[7][5]

**Архитектура пайплайна:**

```
1. Target-model → output
2. Judge (отдельный endpoint, не self-judge) + rubric → score ∈ [0,1] + rationale
3. Score → метрика качества
```

Обязательное условие: **judge ≠ target** (self-agreement bias). Для factory-fast нельзя использовать ту же модель как judge.[8]

**Системные байасы и митигация**:[8]

| Байас | Описание | Митигация |
|---|---|---|
| Positional bias | Систематическое предпочтение первого/последнего ответа | Рандомизировать порядок кандидатов |
| Verbosity bias | Предпочтение длинных ответов независимо от качества | Включить критерий «conciseness» в рубрик |
| Overly positive skew | Сжатие оценок к верхнему краю | Chain-of-Thought с rationale ДО score |
| Self-consistency | Judge ≈ target → circular validation | Обязательное разделение judge/target |
| Prompt sensitivity | Незначительные изменения промта меняют оценки | Нормировать scores по gold calibration set |

**Калибровка judge:**[9][10]
1. Сформировать human-labeled calibration set (мин. 200 примеров, banking-domain).
2. Запустить judge на том же наборе.
3. Вычислить TPR, TNR, Cohen's κ между judge и human. Порог κ > 0.6 (substantial agreement).
4. Если κ < 0.6 — пересмотреть рубрик, не менять judge автономно.
5. Revalidate при каждом обновлении промта или модели judge.

### 2b. Golden Set для Banking-домена

**Структура golden set:**[11][12]

```
GoldenExample:
  id: uuid
  task_type: reasoning | compliance | fraud_classification | aml | extraction
  input: <prompt>
  ground_truth: <exact answer или label>
  difficulty: easy | medium | hard
  domain_slice: kyc | aml | payments | treasury | regulatory
  created_by: human-annotator-id
  created_at: iso8601
  version: semver
```

**Минимальный размер:** 300–500 примеров на алиас для статистической значимости (confidence interval ≤ 3% при p=0.95). Для rare-class (fraud): мин. 200 positive-примеров.[12]

**Принципы формирования:**
- Seed из реальных production-ошибок («turn failures into tests»)[11]
- Покрыть head intents + long tail по domain_slice
- Inter-annotator agreement ≥ 0.75 (Cohen's κ) до включения в set
- Версионирование: prompt + context + output + label + judgment — единым snapshot

**Задачи, требующие human-построения golden set (не автоматизируемо):**
- Compliance-оценки с неоднозначными регуляторными трактовками
- AML-паттерны с новыми типологиями (до официальной публикации FinCEN/FATF)

### 2c. Метрики для Классификации (Fraud/AML)

**Почему PR-AUC, а не ROC-AUC при дисбалансе:**[13][14][15]

ROC-AUC оценивает общую способность ранжирования. При сильном дисбалансе (типичный fraud: 0.1–1% позитивов) ROC-AUC остаётся высоким даже для плохих классификаторов — потому что TN (истинные негативы) доминируют и FPR выглядит малым. PR-AUC игнорирует TN и фокусируется на том, насколько хороши предсказания по позитивному классу:

\[\mathrm{ROC\text{-}AUC} = \int_0^1 \mathrm{TPR}(t) \, d\mathrm{FPR}(t)\]

\[\mathrm{PR\text{-}AUC} = \int_0^1 P(r) \, dr \quad \text{где } P = \frac{TP}{TP+FP},\ r = \frac{TP}{TP+FN}\]

**Правило выбора:** при prevalence < 5% используй PR-AUC как primary metric, ROC-AUC как secondary для понимания общей separability.[15]

**F1 и cost-sensitive F1:**

\[F_1 = 2 \cdot \frac{P \cdot R}{P + R}\]

\[F_\beta = (1+\beta^2) \cdot \frac{P \cdot R}{\beta^2 P + R}\]

При β > 1 акцент на recall (пропустить fraud хуже, чем ложная тревога); при β < 1 — на precision.

**Оптимальный порог через cost-matrix:**[16][17][18]

\[\tau^* = \arg\min_\tau \; C(\tau) = \arg\min_\tau \left[ C_{FN} \cdot FN(\tau) + C_{FP} \cdot FP(\tau) \right]\]

где \(C_{FN}\) = стоимость пропущенного fraud (сумма транзакции), \(C_{FP}\) = стоимость ложной тревоги (операционная нагрузка + customer friction).

Suboptimal threshold setting increases misclassification costs by an average of 53% — это обоснование ручной ратификации каждого τ* оператором.[19]

### 2d. Метрики для Генерации и Reasoning

**Exact Match (EM)** — бинарный, только для детерминированных ответов:

\[\mathrm{EM} = \mathbb{1}[\hat{y} = y^*]\]

**BERTScore** — семантическое сходство с учётом перефразировок:[20]

\[\mathrm{BERTScore}_F = F_1(\mathrm{R}_{BERT}, \mathrm{P}_{BERT})\]

где \(\mathrm{R}_{BERT} = \frac{1}{|r|}\sum_{r_j \in r} \max_{h_i \in h} \cos(\mathbf{e}_{r_j}, \mathbf{e}_{h_i})\), и аналогично \(\mathrm{P}_{BERT}\).

Корреллирует с human judgment лучше, чем BLEU/ROUGE для banking-text.[20]

**Hallucination Rate:**[21]

\[\mathrm{HallucinationRate} = \frac{N_{\text{contradicted\_contexts}}}{N_{\text{total\_contexts}}}\]

Считается через LLM-judge с рубриком «is this claim supported by the provided context?». Для compliance/reasoning — критичная метрика (regulatory hallucination = high-risk output).

**Faithfulness Score** (для RAG-контуров):

\[\mathrm{Faithfulness} = \frac{N_{\text{claims\_grounded\_in\_context}}}{N_{\text{total\_claims\_in\_output}}}\]

### 2e. Калибровка Уверенности (ECE, Brier Score)

Критично для confidence-gates 0.75 и 0.90 в CICD — если модель заявляет confidence=0.90, а реальная точность 0.70, gate неработоспособен.[22][23]

**Expected Calibration Error (ECE):**[24][22]

\[\mathrm{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{n} \left| \mathrm{acc}(B_m) - \mathrm{conf}(B_m) \right|\]

где \(B_m\) — бины по predicted probability, \(\mathrm{acc}(B_m)\) — доля верных предсказаний в бине, \(\mathrm{conf}(B_m)\) — средний confidence в бине.

Требование: мин. 1000 samples per bin для стабильности. При дисбалансе классов — вычислять per-class ECE.[23]

**Maximum Calibration Error (MCE):**[22]

\[\mathrm{MCE} = \max_{m} \left| \mathrm{acc}(B_m) - \mathrm{conf}(B_m) \right|\]

MCE важнее ECE для gates: worst-case miscalibration в одном бине может полностью нарушить логику порогов.

**Brier Score:**[23][22]

\[\mathrm{BS} = \frac{1}{n} \sum_{i=1}^{n} (p_i - y_i)^2 \in [0,1]\]

Brier Score ≤ 0.1 считается хорошей калибровкой. Важно: после RLHF fine-tuning token entropy уплощается, confidence перестаёт быть значимым — требуется post-hoc temperature scaling или Platt scaling.[23]

**Reliability diagram** — обязателен как визуальный audit artifact: plot acc vs conf по 10 бинам. Откалиброванная модель лежит на диагонали y=x.

***

## 3. Детекция Деградации (Drift)

Watchdog должен отличать «модель стала хуже» от статистического шума. Для этого применяются методы Statistical Process Control (SPC).[25][26]

### 3a. Shewhart Control Chart (быстрые сдвиги)

Базовая baseline с ±3σ:

\[\mathrm{UCL} = \mu_0 + 3\sigma_0, \quad \mathrm{LCL} = \mu_0 - 3\sigma_0\]

Обнаруживает большие внезапные сдвиги (≥ 3σ), но нечувствителен к малым постепенным дрейфам.[26]

### 3b. CUSUM Chart (малые постепенные сдвиги) — основной инструмент

CUSUM аккумулирует отклонения от целевого значения и является более чувствительным к малым сдвигам (< 2σ), чем Shewhart:[27][26]

\[S_{hi}(i) = \max\left(0,\; S_{hi}(i-1) + x_i - \mu_0 - k\right)\]
\[S_{lo}(i) = \max\left(0,\; S_{lo}(i-1) + \mu_0 - k - x_i\right)\]

где:
- \(\mu_0\) — baseline mean (установленная в period in-control)
- \(k\) = allowable slack = \(\delta/2\) (половина обнаруживаемого сдвига δ, в единицах σ)
- Тревога при \(S_{hi}(i) > h\) или \(S_{lo}(i) > h\), где \(h = 4\sigma\) — стандартная практика[28]

Рекомендуемые параметры для banking-метрик: k = 0.5σ (обнаруживает сдвиг 1σ), h = 4σ (ARL₀ ≈ 465 при нормальном процессе — допустимый уровень ложных тревог).[26]

**CUSUM для calibration drift:**[29]

Специализированный calibration CUSUM строится на основе разницы между predicted probability и observed outcome. Если в sliding window наблюдается систематическое расхождение:

\[S_t = S_{t-1} + (y_t - \hat{p}_t - k)\]

Тревога при \(S_t > h_{\text{calib}}\). Обязателен для мониторинга ECE в runtime.[29]

### 3c. EWMA Chart (экспоненциальное взвешивание)

Альтернатива CUSUM, более устойчивая к выбросам:

\[Z_t = \lambda x_t + (1-\lambda) Z_{t-1}\]
\[\mathrm{UCL}_t = \mu_0 + L\sigma\sqrt{\frac{\lambda(1-(1-\lambda)^{2t})}{2-\lambda}}\]

λ ∈ [0.05, 0.3] — параметр сглаживания; L ≈ 3.0. EWMA лучше при неравномерном поступлении данных.[25]

### 3d. Скользящее Окно и Статистическая Значимость

**Размер окна:**
- Минимум: 50–100 запросов для бинарных метрик (fraud classification)[11]
- Для редких классов (fraud prevalence ~0.5%): окно ≥ 500 транзакций для стабильной оценки PR-AUC
- Для TTFT/latency: окно 100–500 запросов в зависимости от throughput

**Paired bootstrap test** для сравнения метрик между окнами:[11]

1. Выборка с возвращением из пар (baseline_window, current_window), n=1000 итераций.
2. Вычислить разницу метрики в каждой итерации.
3. p-value = доля итераций, где разница ≤ 0.
4. Сдвиг значим при p < 0.05 (двусторонний тест).

**Практическое правило:** CUSUM-тревога + подтверждение bootstrap-тестом → escalation. CUSUM-тревога без статзначимости → log-only (возможный шум).

***

## 4. Многокритериальное Сравнение Моделей (MAUT/TOPSIS/Парето)

Выбор «лучшей модели на алиас» — многокритериальная задача со скоростью, качеством и VRAM-ограничениями.[30][31][32]

### 4a. Построение Decision Matrix

Для n моделей-кандидатов и m критериев:

\[X = [x_{ij}]_{n \times m}, \quad i \in \text{models},\; j \in \text{criteria}\]

Критерии (пример для factory-fast алиаса):

| j | Критерий | Тип | Вес-кандидат |
|---|---|---|---|
| 1 | P95 Latency (ms) | min | 0.30 |
| 2 | Task Success Rate | max | 0.25 |
| 3 | VRAM usage (GB) | min | 0.15 |
| 4 | BERTScore F1 | max | 0.20 |
| 5 | ECE (calibration) | min | 0.10 |

Веса — **proposal, not adopted**; требуют ратификации оператором.

### 4b. TOPSIS: Нормализация и Scoring

**Шаг 1. Vector normalization:**[32]

\[r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^n x_{ij}^2}}\]

**Шаг 2. Weighted normalized matrix:**

\[v_{ij} = w_j \cdot r_{ij}\]

**Шаг 3. Ideal (A⁺) и Anti-Ideal (A⁻) решения:**

\[A^+ = \{v_j^+ = \max_i v_{ij} \text{ (для max)},\; \min_i v_{ij} \text{ (для min)}\}\]
\[A^- = \{v_j^- = \min_i v_{ij} \text{ (для max)},\; \max_i v_{ij} \text{ (для min)}\}\]

**Шаг 4. Euclidean distances:**

\[d_i^+ = \sqrt{\sum_{j=1}^m (v_{ij} - v_j^+)^2}, \quad d_i^- = \sqrt{\sum_{j=1}^m (v_{ij} - v_j^-)^2}\]

**Шаг 5. Closeness coefficient (ranking score):**

\[C_i = \frac{d_i^-}{d_i^+ + d_i^-} \in [0,1]\]

Чем ближе \(C_i\) к 1, тем ближе модель к ideal solution. Топ-1 по \(C_i\) — TOPSIS-рекомендация.

### 4c. Pareto Front для Несравнимых Моделей

Когда модели не доминируют друг друга по всем критериям — строится Pareto front:[33]

Модель A **доминирует** B если \(\forall j: x_{Aj} \geq x_{Bj}\) (с учётом направления) и \(\exists j: x_{Aj} > x_{Bj}\).

Парето-множество — все недоминируемые модели. Это честная граница trade-off (например: evo2/qwen3.5:35b быстрее, но evo1/llama3.3:70b точнее — обе на Pareto front для разных задач).

### 4d. Lexicographic Gate (Safety-First, per Q2-ruling)

До TOPSIS-scoring — обязательный admissibility gate:[34][35]

```
IF VRAM_peak > VRAM_budget → BLOCKED (вне scoring)
IF P99_Latency > latency_SLA → BLOCKED для real-time алиасов
IF ECE > ECE_max → BLOCKED для confidence-gate алиасов
```

Только ADMISSIBLE модели участвуют в TOPSIS.

***

## 5. Пороги для Банка (Обоснованные)

Все пороги ниже — **proposal, not adopted**. Активируются только после ратификации оператором+Central.

### 5a. Операционные Пороги

**Latency (реальное время принятия решений):**

Для fraud/payment authorization: индустриальный стандарт — решение за **< 100ms при P99**. Leading platforms: p95 = 60–80ms.[36][4]

| Алиас | P50 target | P95 target | P99 SLA | Обоснование |
|---|---|---|---|---|
| factory-fast | ≤ 500ms | ≤ 1000ms | ≤ 2000ms | Interactive UI |
| factory-coder | ≤ 5s | ≤ 15s | ≤ 30s | Batch codegen |
| factory-mid | ≤ 1s | ≤ 3s | ≤ 5s | Balanced |
| project-reason | ≤ 10s | ≤ 30s | ≤ 60s | Deep reasoning |
| fraud inference | ≤ 50ms | ≤ 80ms | ≤ 100ms | Realtime payments |

**Success Rate:** ≥ 0.99 для payment/compliance контура; ≥ 0.95 для factory.

**VRAM utilisation:** ≤ 0.85 sustained (headroom для batch-спайков).

### 5b. Качественные Пороги

**Fraud/AML classification:**[37][4]

- PR-AUC ≥ 0.85 (market-standard для зрелых fraud-программ)
- Value Detection Rate (VDR) ≥ 0.60 при False Positive Rate ≤ 0.01 (1%)[37]
- «Best-in-class»: VDR > 0.70 при intervention rate ≤ 0.1%[37]
- F₂-score ≥ 0.80 (recall-weighted, penalty за missed fraud)

**Reasoning/Compliance (generative):**

- BERTScore F1 ≥ 0.82 (semantic correctness)
- Hallucination Rate ≤ 0.03 (3%) для compliance — критический порог
- Faithfulness ≥ 0.95 для RAG-контуров

**Calibration (для confidence-gates):**[24][22]

- ECE ≤ 0.05 (приемлемо), ≤ 0.03 (хорошо) — обоснование: gates 0.75/0.90 работают корректно только при ECE ≤ 0.05
- MCE ≤ 0.10 (worst-case бин не должен иметь > 10% miscalibration)
- Brier Score ≤ 0.10

Обоснование ECE-порога: при ECE = 0.10 gate confidence=0.90 реально пропускает решения с точностью 0.80 → false security в CICD.

### 5c. EU AI Act Art. 15 — Accuracy, Robustness, Cybersecurity

EU AI Act требует «appropriate levels of accuracy, robustness and cybersecurity throughout the lifecycle» и обязывает обнаруживать деградацию и корректировать её. Конкретные пороги не регламентированы законом — они должны быть задокументированы провайдером как часть Risk Management System (Art. 9).[38][39][40]

***

## 6. Fail-Closed Метрика (I-27 Escalation Threshold)

### 6a. Формальное Определение

Fail-closed threshold — минимальное значение метрики, ниже которого модель **должна быть отстранена** от compliance/payment-тракта и watchdog эскалирует человеку (I-27). Обоснование через минимизацию expected regret.

**Expected Cost под моделью m:**[41][42][43]

\[EC(m, \tau) = \mathbb{E}\left[C_{FN} \cdot \mathbb{1}[\hat{y}=0, y=1] + C_{FP} \cdot \mathbb{1}[\hat{y}=1, y=0]\right]\]

**Regret модели m относительно oracle (оптимальной модели):**

\[R(m) = EC(m) - EC(m^*)\]

где \(m^*\) — best achievable model. Если \(m^*\) недоступна — бенчмарк по golden set.

**Fail-closed threshold через minimax regret:**[42]

\[\mathrm{threshold}_{FC} = \inf\{q \in [0,1] : R(m) > R_{\max}\}\]

где \(R_{\max}\) — максимально допустимый regret (задаётся оператором в governed config).

**Практическая формула для compliance-контура:**

Пусть \(q_{\text{critical}}\) — минимально допустимое значение метрики качества (например, PR-AUC или F₂).

\[\mathrm{BLOCK\ if:}\quad Q_m < q_{\text{critical}}\]

\[q_{\text{critical}} = q_{\text{baseline}} - k \cdot \sigma_{q}\]

где \(q_{\text{baseline}}\) — установленный baseline при деплое, \(\sigma_q\) — стандартное отклонение метрики на golden set, \(k\) — коэффициент tolerable degradation (proposal: k = 2.0, соответствует ~2σ).

### 6b. Worst-Case Loss Minimization

Для условий неопределённости (concept drift в fraud patterns): minimax regret approach:[43][42]

\[d^*_{\mathrm{MMR}} = \arg\min_{d \in \mathcal{D}} \max_{\theta \in \Theta} R(d, \theta)\]

Операционализация: если на скользящем окне \(n=200\) транзакций наблюдается:

\[\bar{R}_{\text{window}} = \frac{1}{n}\sum_{t=1}^n r_t > R_{\max}\]

→ watchdog эскалирует: модель временно заблокирована на payment-контуре, human review.

### 6c. Агрегированный Fail-Closed Score

\[FC_{\text{score}} = \mathbb{1}\left[\mathrm{PR\text{-}AUC} \geq 0.85\right] \cdot \mathbb{1}\left[\mathrm{ECE} \leq 0.05\right] \cdot \mathbb{1}\left[\mathrm{P99\_lat} \leq \mathrm{SLA}\right] \cdot \mathbb{1}\left[\mathrm{SR} \geq 0.99\right]\]

\[FC_{\text{score}} < 1 \Rightarrow \mathrm{ESCALATE}\]

Логическое AND: модель проходит только если **все** условия выполнены (fail-closed, не fail-soft). Пороги — proposal, active при ратификации.

***

## 7. Что Логировать (EU AI Act Art. 14, Art. 12)

EU AI Act Art. 12 обязывает high-risk AI системы иметь **автоматическое логирование событий** с tamper-resistant хранением (мин. 6 месяцев). Art. 14 требует логирование действий human oversight.[44][45][46]

### 7a. Минимальный Набор Полей на Каждое Измерение

```
EfficiencyMeasurement:
  # === Identity & Tracing ===
  measurement_id:     uuid (immutable)
  model_alias:        string (e.g. "factory-fast")
  model_id:           string (e.g. "qwen3:30b@evo2")
  request_id:         uuid (linked to upstream request)
  timestamp_utc:      iso8601
  measurement_type:   latency | quality | calibration | drift

  # === Operational Metrics ===
  ttft_ms:            float | null
  tpot_ms_per_token:  float | null
  e2e_latency_ms:     float
  tokens_input:       int
  tokens_output:      int
  success:            bool
  error_code:         string | null
  vram_used_gb:       float | null

  # === Quality Metrics (when golden set used) ===
  golden_example_id:  uuid | null
  task_type:          classification | generation | reasoning
  metric_name:        string (e.g. "PR-AUC", "BERTScore", "ECE")
  metric_value:       float
  metric_threshold:   float
  threshold_passed:   bool

  # === Calibration ===
  predicted_confidence: float | null
  actual_outcome:       bool | null
  brier_contribution:   float | null

  # === Drift Signal ===
  cusum_shi:          float | null
  cusum_slo:          float | null
  drift_signal:       bool

  # === Compliance / Human Oversight (Art. 14) ===
  escalated:          bool
  escalation_reason:  string | null
  human_reviewer_id:  string | null
  human_decision:     approved | overridden | deferred | null
  human_review_ts:    iso8601 | null

  # === Immutability ===
  prev_record_hash:   sha256  # append-only chain
  record_hash:        sha256
```

**Retention:** мин. 6 месяцев (Art. 12(2)); для compliance-контура рекомендуется 12 месяцев (audit cycle).[46]

**Tamper resistance:** Kafka (append-only topic) + WORM S3 (object lock). Любое чтение/запись через API, без прямого доступа к хранилищу.

### 7b. Что Автоматизируемо vs Требует Человека

| Действие | Автоматизируемо сейчас | Требует golden set | Требует человека |
|---|---|---|---|
| Измерение TTFT/TPOT/E2E | ✅ | — | — |
| Success Rate | ✅ | — | — |
| VRAM utilisation | ✅ | — | — |
| CUSUM drift signal | ✅ | baseline | — |
| PR-AUC / F₁ / F₂ | ✅ | ✅ | Построение golden set |
| ECE / Brier Score | ✅ | ✅ | Построение golden set |
| BERTScore F1 | ✅ | ✅ | — |
| Hallucination Rate | Частично (LLM-judge) | ✅ | Judge-калибровка |
| Faithfulness | Частично (LLM-judge) | ✅ | Judge-калибровка |
| CUSUM → escalation | ✅ | baseline | ✅ (human resolve) |
| Threshold ратификация (τ*, w_j, FC) | — | — | ✅ (оператор+Central) |
| Judge-калибровка (κ > 0.6) | — | ✅ | ✅ |
| Golden set формирование | — | — | ✅ |

***

## Итоговая Таблица Метрик

| Метрика | Формула (сокращ.) | Порог-кандидат | Ось | Авто |
|---|---|---|---|---|
| TTFT | \(t_{1st} - t_{req}\) | ≤ 500ms (fast) | Операц. | ✅ |
| TPOT | \(\Delta t / N_{out}\) | ≤ 50ms/tok | Операц. | ✅ |
| P95/P99 Latency | перцентиль E2E | P99 ≤ 100ms (fraud) | Операц. | ✅ |
| Success Rate | \(N_{ok}/N_{total}\) | ≥ 0.99 (payment) | Операц. | ✅ |
| VRAM util | \(used/total\) | ≤ 0.85 | Операц. | ✅ |
| PR-AUC | \(\int P\,dr\) | ≥ 0.85 | Качество | ✅ (golden) |
| ROC-AUC | \(\int TPR\,dFPR\) | ≥ 0.92 | Качество | ✅ (golden) |
| F₂-score | \(5PR/(4P+R)\) | ≥ 0.80 | Качество | ✅ (golden) |
| Optimal threshold τ* | cost-matrix | domain-specific | Качество | ✅/👤 |
| BERTScore F1 | cosine-match BERT | ≥ 0.82 | Качество | ✅ (golden) |
| Hallucination Rate | contradicted/total | ≤ 0.03 | Качество | Частично |
| Faithfulness | grounded/claims | ≥ 0.95 | Качество | Частично |
| ECE | \(\sum\|acc-conf\|w_m\) | ≤ 0.05 | Calibration | ✅ (golden) |
| MCE | \(\max\|acc-conf\|\) | ≤ 0.10 | Calibration | ✅ (golden) |
| Brier Score | \(\frac{1}{n}\sum(p_i-y_i)^2\) | ≤ 0.10 | Calibration | ✅ (golden) |
| CUSUM S_hi/S_lo | \(\max(0, S+x-\mu_0-k)\) | h = 4σ | Drift | ✅ |
| Bootstrap p-value | paired resample | < 0.05 | Drift | ✅ |
| TOPSIS C_i | \(d^-/(d^++d^-)\) | rank-based | Multi-crit. | ✅ |
| FC Score | AND(gates) | = 1 | Fail-closed | ✅ |

*Авто: ✅ = полностью автоматизируемо; Частично = требует judge-калибровки; 👤 = требует человека.*

***

## Compliance-Примечания

**EU AI Act Art. 12** (logging): все поля §7 логируются автоматически, tamper-resistant, retention ≥ 6 месяцев.[46]

**EU AI Act Art. 14** (human oversight): поля `escalated`, `human_reviewer_id`, `human_decision` документируют meaningful human review — не rubber-stamp. Watchdog лишь эскалирует; решение — человек.[44]

**EU AI Act Art. 15** (accuracy/robustness): CUSUM + bootstrap + FC-score формируют documented evidence для Art. 15 «appropriate levels of accuracy throughout lifecycle».[39][38]

**FCA/PRA SS1/23 Model Risk**: любые веса w_j и пороги q_critical, влияющие на material decisions, подлежат independent model validation до активации.[47][48]

**I-27 Invariant:** watchdog никогда не переключает модель автономно. FC_score < 1 → escalation record в append-only log → human decision.