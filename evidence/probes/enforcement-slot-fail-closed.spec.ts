/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `ENFORCEMENT_NOT_PREPARED` (`conductor/src/http/client-enforcement.ts`) — умолчание
 * слота подготовленных исходов. Неподготовленный слот обязан ОТКАЗЫВАТЬ, а не разрешать:
 * «слот, которого нет, есть отсутствие проверки, и читать его как „проверено и можно“ было бы
 * худшим из умолчаний». Отказ не назван ни одной пробой дерева.
 *
 * КАНАРЕЙКА: умолчание заменено разрешающим (`{ allowed: true }` вместо `NOT_PREPARED`) —
 * `Tests: 2 failed, 2 passed`. Покраснели ровно те две, что зависят от закрытого умолчания;
 * «подготовленный исход отдаётся тот же» и «константа заморожена» остались зелёными. Различает.
 *
 * Служба вне карантина переноса: подъём пробы ничьего паритета не задевает.
 */
import { PreparedEnforcement, NOT_PREPARED } from "./client-enforcement";

const задание = (requestId: string) => ({ requestId }) as never;

describe("слот подготовленных исходов: неподготовленное есть ОТКАЗ", () => {
  it("ключа нет — отказ ENFORCEMENT_NOT_PREPARED, а не разрешение", () => {
    const слот = new PreparedEnforcement();
    const v = слот.fn(задание("нет-такого"));
    expect(v.allowed).toBe(false);
    expect(v.refusalCode).toBe("ENFORCEMENT_NOT_PREPARED");
    expect(v.trail).toEqual([]);
  });

  it("подготовленный исход отдаётся ТОТ ЖЕ, а не пересобранный", () => {
    const слот = new PreparedEnforcement();
    const исход = Object.freeze({ allowed: false, trail: Object.freeze(["шаг"]),
                                  refusalCode: "SUPERVISION_BLOCK" }) as never;
    слот.put("r1", исход);
    expect(слот.fn(задание("r1"))).toBe(исход);
    expect(слот.size()).toBe(1);
  });

  it("чужой ключ не берёт чужой исход", () => {
    const слот = new PreparedEnforcement();
    слот.put("r1", { allowed: true, trail: [], refusalCode: undefined } as never);
    expect(слот.fn(задание("r2")).refusalCode).toBe("ENFORCEMENT_NOT_PREPARED");
  });

  it("константа отказа заморожена: её нельзя испортить на месте", () => {
    expect(Object.isFrozen(NOT_PREPARED)).toBe(true);
    expect(() => { (NOT_PREPARED as { allowed: boolean }).allowed = true; }).toThrow();
    expect(NOT_PREPARED.allowed).toBe(false);
  });
});
