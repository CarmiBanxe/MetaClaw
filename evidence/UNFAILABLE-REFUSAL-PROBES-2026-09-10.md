# Пробы, которые не могут упасть: отказ проверяется только в `catch`

**Найдено:** 24 проб в 19 файлах. Замер на `HEAD` дерева `bt-sepa01`.

## Предмет

```ts
try { вызов(); } catch (e) { expect((e as Ошибка).code).toBe("X"); }
```

**Проба зелена и тогда, когда вызов не бросил вовсе:** до `catch` дело не доходит, `expect` не
исполняется, отсутствие отказа читается как исполненный отказ. Утверждения внутри верны — проба
просто не умеет заметить, что проверяемого отказа больше нет.

Правильная форма несёт стража: `return` в `catch` и `throw` после блока, либо `expect(...).toThrow`.

## Подтверждено прямой пробой, а не выведено поиском

`libraries/ledger-projection`: снят отказ `GROUP_STATE_MIXED` целиком
(`if (false as boolean && …)`, типы целы, счёт неизменен **21 → 21**).

| проба | итог при снятом отказе |
|---|---|
| «ГЛАВНОЕ: половина проведённой проводки — расхождение» (через помощника `code()`) | **красная** |
| «отказ называет, ЧТО именно разошлось» (`try/catch` без стража) | **ЗЕЛЁНАЯ** |

Мера исчезла, вторая проба этого не заметила.

## Перечень


**services/ledger/ledger/src/adapters/tigerbeetle.adapter.spec.ts**
- `:168` — `try { await a.createAccount(account(B)); }`

**services/banksy/conductor/src/orchestrator/orchestrator.spec.ts**
- `:143` — `try { agent.refuseMutation("initiate_payment"); }`
- `:150` — `try { agent.refuseMutation("write_anything"); }`

**services/banksy/conductor/src/composition/org-binding.spec.ts**
- `:83` — `try { bindOrg(manifest(["B-mlro"]), org); }`

**services/banksy/customer-gateway/src/director-channel.spec.ts**
- `:36` — `try { await ch.ask({ correlationId: "c", spec: lookup("balance.show") }); }`

**services/banksy/customer-gateway/src/step-up-proof.spec.ts**
- `:70` — `try { v.verify(p, { ...b, amount: "1.00", currency: "GBP" }, NOW); }`

**services/banksy/customer-gateway/src/execution-authority.spec.ts**
- `:50` — `try { assertMay(compose(customer, agent), "execute"); }`
- `:54` — `try { assertMay(compose(narrow, { ref: "a", grants: ["explain", "execute"] } }`

**services/fx/trading_gateway/src/trading-gateway.characterization.spec.ts**
- `:1535` — `try { assertHitlConfirmed(undefined); }`

**services/audit/audit/src/audit-export.spec.ts**
- `:47` — `try { releaseAuditExport(п, одобрение(п, { by: "sim://conductor" }), [], ДИА }`

**services/products/agreement/src/agreement.characterization.spec.ts**
- `:139` — `try { svc.recordSignature({ agreementId: a.agreementId, customerId: "intrude }`

**services/payments/payment/src/http/sepa-crash-restart.spec.ts**
- `:320` — `try { resolveCrashPoint({ BANXE_ENVIRONMENT: "production", SEPA_CRASH_AT: "a }`

**libraries/ledger-projection/src/projection.spec.ts**
- `:156` — `try { groupState(["posted", "pending"]); }`

**libraries/banksy-reconciliation/src/receipt-recon.spec.ts**
- `:71` — `try { assertReconciled(r); }`
- `:80` — `try { reconcile([], [record("c1"), record("c1")]); }`

**libraries/banksy-treasury-ports/src/treasury-ports.spec.ts**
- `:69` — `try { кривой.getExposure("GBP/EUR"); }`

**libraries/banksy-maturity/src/ladder.spec.ts**
- `:161` — `try { productionFrom(candidate()); }`

**libraries/ledger-lifecycle/src/lifecycle.spec.ts**
- `:74` — `try { assertSettleAmount(10000n, 8700n, 3); }`
- `:88` — `try { assertSettleAmount(10000n, 0n, 2); }`

**libraries/banksy-durable/src/write-once.spec.ts**
- `:54` — `try { s.put("idempotent_reply", "k", { a: 2 }); }`

**libraries/banksy-durable/src/seen-set.spec.ts**
- `:40` — `try { s.remember("nonce", "", NOW); }`

**libraries/ledger-address/src/address.spec.ts**
- `:74` — `try { ledgerForCurrency("CHF"); }`

**libraries/banksy-data-class/src/provenance.spec.ts**
- `:43` — `try { assertWritable(training, "prod"); }`
- `:49` — `try { assertWritable(training, "prod"); }`
