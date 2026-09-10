/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `PROPOSAL_FOR_ANOTHER_CUSTOMER` (`customer-gateway/src/conversation.ts:230`) —
 * «предложение, выданное одному клиенту, никогда не разрешает другому». Отказ не назывался ни
 * одной пробой дерева. Набор `conversation.spec.ts` проверяет восемь других кодов, включая
 * `NOT_THE_CUSTOMERS_CHANNEL` и `KEY_CROSSES_NAMESPACE`, — то есть изоляцию на ДРУГИХ слоях.
 *
 * ЧТО НАШЛОСЬ ПРИ НАПИСАНИИ. Первая редакция утверждала `not.toBe("ПРОШЛО")` — и была зелёной,
 * измеряя НЕ ТОТ рубеж: чужой клиент получает `PROPOSAL_UNKNOWN`, потому что пространство имён
 * памяти не пускает его к записи вовсе. Слабое утверждение скрыло бы это целиком. Тот же дефект,
 * что у проверки по классу исключения: имя шире предмета.
 *
 * ОТСЮДА ДВА РУБЕЖА, названные порознь:
 *   1) чужое предложение НЕ ВИДНО                  → `PROPOSAL_UNKNOWN`
 *   2) запись с чужим клиентом В СВОЁМ пространстве → `PROPOSAL_FOR_ANOTHER_CUSTOMER`
 * Второй проверяется подсадкой такой записи: так выглядел бы ПРОРЫВ первого.
 *
 * КАНАРЕЙКА: `stored.customerId !== this.customerId` ослеплено сравнением с самим собой.
 * `Tests: 1 failed, 3 passed`, и ответ второго рубежа — **`ПРОШЛО`**: предложение чужого клиента
 * ПРОВОДИТСЯ. Проба первого рубежа при этом остаётся ЗЕЛЁНОЙ.
 *
 * Вот чем эта пара доказывает, что второй рубеж НЕСУЩИЙ: набор, проверяющий только первый,
 * не заметил бы его снятия ничем.
 *
 * Служба вне карантина переноса.
 */
import { SharedMemory, VolatileRows, memoryKey } from "@bank-tree/banksy-memory";
import type { DepartmentReply } from "@bank-tree/banksy-protocol";
import { compose } from "./composite-identity";
import { Conversation, proposalKey, type DoorPort } from "./conversation";
import type { Session } from "./gateway";

const TERMS = { consentRef: "consent-1", retentionDays: 30 } as const;
const личность = (ref: string) => compose(
  { kind: "customer", ref, tenant: "t-1", grants: ["explain", "prepare", "submit", "execute"] as never },
  { ref: "banksy-client", grants: ["explain", "prepare", "submit", "execute"] as never },
);
const сессия = (): Session => ({
  deviceBound: true, assurance: "authenticated", consentRefs: ["consent-1"],
  confirmedOutsideModel: false, requestsThisMinute: 1,
});
class Дверь implements DoorPort {
  async handle(): Promise<DepartmentReply> {
    return { protocol: "banksy-department/v1", verdict: "готово", confidence: 1,
             evidence: ["дверь ответила"] } as DepartmentReply;
  }
}
const код = async (f: () => Promise<unknown>): Promise<string> => {
  try { await f(); return "ПРОШЛО"; } catch (e) { return (e as { code?: string }).code ?? "ОТКАЗ"; }
};

describe("предложение, выданное одному клиенту, никогда не разрешает другому", () => {
  it("ПЕРВЫЙ РУБЕЖ: чужое предложение вообще НЕ ВИДНО — PROPOSAL_UNKNOWN", async () => {
    const общая = new SharedMemory(new VolatileRows());
    const дверь = new Дверь();
    const первый = new Conversation("cust-1", общая.view("cust-1"), личность("cust-1"), дверь, TERMS);
    const второй = new Conversation("cust-2", общая.view("cust-2"), личность("cust-2"), дверь, TERMS);
    первый.consider({ tool: "balance.show", says: "покажу остаток" }, "corr-1");
    // Второй знает идентификатор — и этого мало: пространство имён памяти его не пускает.
    // ИМЕННО КОД, а не «что-нибудь»: слабое утверждение скрыло бы, ЧТО именно остановило.
    expect(await код(() => второй.carry("corr-1", сессия()))).toBe("PROPOSAL_UNKNOWN");
  });

  it("ВТОРОЙ РУБЕЖ: запись с чужим клиентом В СВОЁМ пространстве — PROPOSAL_FOR_ANOTHER_CUSTOMER", async () => {
    const общая = new SharedMemory(new VolatileRows());
    const вид = общая.view("cust-1");
    const c = new Conversation("cust-1", вид, личность("cust-1"), new Дверь(), TERMS);
    // Подсаживаем В СВОЁ пространство запись, помеченную ЧУЖИМ клиентом: так выглядел бы прорыв
    // первого рубежа. Второй страж обязан сработать сам по себе.
    вид.write({ key: memoryKey(proposalKey("corr-чужой")),
                value: { id: "corr-чужой", customerId: "cust-2", tool: "balance.show",
                         says: "покажу остаток", at: new Date().toISOString() },
                consentRef: "consent-1", provenance: "проба", retentionDays: 30 } as never,
              "role-2.manager");
    expect(await код(() => c.carry("corr-чужой", сессия()))).toBe("PROPOSAL_FOR_ANOTHER_CUSTOMER");
  });

  it("КОНТРОЛЬ: свой клиент проводит своё предложение", async () => {
    const общая = new SharedMemory(new VolatileRows());
    const дверь = new Дверь();
    const свой = new Conversation("cust-1", общая.view("cust-1"), личность("cust-1"), дверь, TERMS);
    свой.consider({ tool: "balance.show", says: "покажу остаток" }, "corr-2");
    expect(await код(() => свой.carry("corr-2", сессия()))).toBe("ПРОШЛО");
  });

  it("PROPOSAL_UNKNOWN — проведение того, чего не предлагали, проведением не является", async () => {
    const общая = new SharedMemory(new VolatileRows());
    const c = new Conversation("cust-1", общая.view("cust-1"), личность("cust-1"), new Дверь(), TERMS);
    expect(await код(() => c.carry("никогда-не-предлагали", сессия()))).toBe("PROPOSAL_UNKNOWN");
  });
});
