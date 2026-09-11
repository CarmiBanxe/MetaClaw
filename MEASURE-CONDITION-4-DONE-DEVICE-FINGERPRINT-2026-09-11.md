# Условие 4, пройденное до конца на одной службе — и мина, названная прибором дерева

**Служба:** `device_fingerprint` — 4 запертых функции. **Дата:** 2026-09-11. Дерево `b87a9041`.
**Кто составил:** центральный терминал. **Я не автор переноса и не выпускающий** — условие 2 к
этой записи отношения не имеет и ею не затрагивается.

## Карта «донорская проба → наша», все девятнадцать

Донор: `tests/emi-stack/test_device_fingerprint/test_fingerprint.py`, **19 проб**.
Наша сторона: `services/financial-crime/device_fingerprint/src/*.spec.ts`, **41 проба**.

| # | донорская проба | наша | разряд |
|---:|---|---|---|
| 1 | `test_register_device_returns_profile` | «golden deterministic device id dev_<8hex>» + «appends a device.registered log entry» | mapped |
| 2 | `test_device_id_starts_with_dev` | «опознаватель устройства начинается с dev_» | mapped |
| 3 | `test_device_log_append_only` | «device log getter returns an independent copy» + «журнал устройств только дописывается» | mapped |
| 4 | `test_known_device_score_zero` | «known device… score '0.0'» | mapped |
| 5 | `test_new_device_score_03` | «unseen fingerprint under limit → 'new', score '0.3'» | mapped |
| 6 | `test_suspicious_device_cross_customer` | «same fingerprint registered to a DIFFERENT customer → 'suspicious', score '0.8'» | mapped |
| 7 | `test_score_is_decimal_string` | «оценка исхода есть строка, разбираемая как точное десятичное» | mapped |
| 8 | `test_score_not_float` | то же + «три оценки суть точные десятичные строки» | mapped |
| 9 | `test_max_devices_triggers_suspicious` | «6th distinct device… MAX_DEVICES_PER_CUSTOMER=5» | mapped |
| 10 | `test_hash_deterministic` | «is deterministic and 64 hex chars» | mapped |
| 11 | `test_hash_differs_for_different_ua` | «is sensitive to every signal» | mapped |
| 12 | `test_score_constants_are_decimal` | «три оценки суть точные десятичные строки 0.0, 0.3 и 0.8» | mapped |
| 13 | `test_score_constants_not_float` | то же | mapped |
| 14 | `test_get_by_customer_returns_registered` | «getByHash… getByCustomer filters» | mapped |
| 15 | `test_known_device_returns_match_result` | «знакомое устройство возвращает исход, а не предложение» | mapped |
| 16 | `test_suspicious_device_returns_hitl` | «suspicious cross-customer device (0.8 >= 0.7) → DeviceHITLProposal» | mapped |
| 17 | `test_hitl_not_auto_approved` | «не самоодобряется» | mapped |
| 18 | `test_hitl_requires_fraud_analyst` | «уходит на подпись FRAUD_ANALYST» | mapped |
| 19 | `test_proposals_accumulate` | — | **NOT-MAPPED** |

### Единственная `NOT-MAPPED` — с причиной, как требует условие 4

**`test_proposals_accumulate`** утверждает, что две оценки подряд копят **два** предложения.

**Причина:** поведение **перенесено** — `fingerprint-agent.ts` несёт `private readonly
proposalLog: DeviceHITLProposal[]` и геттер `proposals`, — но **пробы, утверждающей накопление, на
нашей стороне нет**. Это **пробел покрытия, а не различие поверхности**: чинится одной пробой, и
разряд `gap` для описи поверхности здесь неуместен.

### Обратное направление — где лежит настоящая работа

Наших проб **41**, донорских **19**. Двадцать две нашей стороны донорского происхождения не имеют:
золотые хеши, движок аномалий (`+30 NEW_DEVICE`, `+20 LOCATION_CHANGE`, `+40 impossible travel`,
`CRITICAL` при 90), запрет юрисдикции `I-02`, привязки сессий.

**Это предмет условия 6, а не 4**, и каждая обязана получить разряд `mapped` /
`intentional-change-with-authority` / `gap`. Настоящая стоимость пакета лежит **здесь**, а не в
карте условия 4: карта донор→мы сошлась восемнадцатью из девятнадцати за один проход чтения.

## Замечание о стоимости: 18 из 19 сошлись чтением, 0 из 19 — машиной

На `card_issuing` мой машинный сопоставитель дал «не сопоставлено 112 из 145» и был **негоден**:
он сравнивал английские имена с русскими описаниями. Здесь то же чтение дало **18 из 19 за один
проход**.

**Вывод о приёме, а не о службе:** условие 4 стоит дёшево **для читающего** и невозможно **для
сопоставителя имён**. Оценка «около сотни проб на службу» была верна по объёму чтения и неверна по
характеру работы.

## И мина, которую прибор дерева назвал сам

`scripts/durability_survey.py` печатает свои пределы **каждым прогоном**. Пятый из них:

> «КАРАНТИН измеряется наличием `PARITY-REPORT.md` у ближайшего предка, и это верно **ровно пока
> выпущенных служб нет**… В день, когда оператор выпустит первую, отчёт у неё останется, и место в
> ней замер по-прежнему сочтёт карантинным — **то есть промолчит там, где приговор станет
> обязателен**.»

**Это прямо связано с условием 2.** В тот же день, когда появится названный человек-выпускающий и
первая служба выйдет из карантина, мера долговечности **перестанет судить** её носители — молча,
потому что признак «есть `PARITY-REPORT.md`» переживёт выпуск.

**Мера названа честно и о себе; чинить её надо ДО выпуска, а не после.** После — некому будет
заметить, что она молчит.

## Чего запись НЕ делает

Не есть пакет доказательств и не заменяет его: условия 3, 5, 6, 7 здесь не закрыты. Не есть выпуск:
`released_by` не заполняется и заполняться не может. Карта донор→мы составлена чтением одного
человека и подлежит независимой проверке — тем же порядком, каким я проверяю чужое.
