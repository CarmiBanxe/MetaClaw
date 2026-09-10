/**
 * ДОКАЗАННАЯ ПРОБА — прогон и ТРИ канарейки 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: три отказа дирижёра, ни один не назывался пробой дерева:
 *   `BUDGET_UNCONFIGURED` — потолок обязан быть положительным числом;
 *   `UNKNOWN_COMPONENT`   — незарегистрированная часть вида не собирается;
 *   `INVALID_REQUEST`     — «ответ помощника обязан быть привязан к такту».
 *
 * КАНАРЕЙКИ, каждая ослепляет свой страж: 1 failed, 2 passed — трижды.
 *
 * ПОЧЕМУ У БЮДЖЕТА ЧЕТЫРЕ ПЛОХИХ ЗНАЧЕНИЯ, А НЕ ОДНО: `0`, `-1`, `NaN`, `Infinity`. Проверка
 * несёт ДВА условия (`!Number.isFinite(ceiling) || ceiling <= 0`), и проба с одним значением
 * оставила бы половину без замера. Канарейка это подтвердила: ослепление ОДНОГО из двух условий
 * роняет пробу — потому что она проходит по всем четырём.
 *
 * Каждый случай несёт КОНТРОЛЬ: настоящий потолок строится, зарегистрированная часть с
 * происхождением собирается, запрос с тактом проходит.
 *
 * Служба вне карантина переноса.
 */
import { Budget } from "./budget";
import { assemble, REGISTERED_COMPONENTS } from "./design-orchestrator";
import { assertRequest } from "../helpers/base";

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as { code?: string }).code ?? "ОТКАЗ"; }
};

describe("три отказа дирижёра, у каждого свой предмет", () => {
  it("BUDGET_UNCONFIGURED — потолок обязан быть положительным числом", () => {
    for (const плохой of [0, -1, Number.NaN, Number.POSITIVE_INFINITY]) {
      expect(код(() => new Budget(плохой))).toBe("BUDGET_UNCONFIGURED");
    }
    // КОНТРОЛЬ: настоящий потолок строится
    expect(код(() => new Budget(100))).toBe("НЕ БРОСИЛ");
  });

  it("UNKNOWN_COMPONENT — незарегистрированная часть вида не собирается", () => {
    expect(код(() => assemble({ components: ["design_придуманный"], data: [] } as never)))
      .toBe("UNKNOWN_COMPONENT");
    // КОНТРОЛЬ: зарегистрированная часть с происхождением проходит
    expect(код(() => assemble({ components: [REGISTERED_COMPONENTS[0]],
                                data: [{ key: "k", lineageId: "l-1" }] } as never)))
      .toBe("НЕ БРОСИЛ");
  });

  it("INVALID_REQUEST — ответ помощника обязан быть привязан к такту", () => {
    expect(код(() => assertRequest({ correlationId: "", subjectRef: "s", question: "q" })))
      .toBe("INVALID_REQUEST");
    expect(код(() => assertRequest({ correlationId: "c1", subjectRef: "s", question: "q" })))
      .toBe("НЕ БРОСИЛ");
  });
});
