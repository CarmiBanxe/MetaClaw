/**
 * ДОКАЗАННАЯ ПРОБА — прогон и канарейка 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `VALUE_DIFFERS_UNDER_SAME_KEY` (`libraries/banksy-memory/src/store.ts:106`).
 * Повтор с тем же ключом и ТЕМ ЖЕ значением идемпотентен; с ДРУГИМ значением — отказ, потому что
 * «тихая перезапись не идемпотентность, а потеря: первое значение исчезло бы, и никто бы не
 * узнал». Отказ не назван ни одной пробой дерева.
 *
 * КАНАРЕЙКА: сравнение обращено и погашено (`=== … && false`) — расхождение перестаёт быть
 * отказом. `Tests: 1 failed, 2 passed`, ответ `НЕ БРОСИЛ`. Число проб набора не изменилось (3),
 * сборка цела — значит замер действителен, а не отравлен канарейкой.
 *
 * ПОЧЕМУ ЗДЕСЬ `&& false` ДОПУСТИМО. Обычно это запрещённая канарейка: она ломает сужение типа и
 * тем меняет число проверок. Здесь сужения нет — сравнение строк булево, — и число проб осталось
 * прежним. Признак действительности замера: не «канарейка красная», а «счёт проб не сдвинулся».
 *
 * Третья проба (чужой клиент) осталась зелёной под канарейкой и потому доказывает, что отказ
 * стережёт СОВПАДЕНИЕ КЛЮЧА, а не границу клиента: границу держит другое место.
 */
import { SharedMemory } from "./store";
import { TenantRefusal, memoryKey } from "./keys";

const код = (f: () => unknown): string => {
  try { f(); return "НЕ БРОСИЛ"; } catch (e) { return (e as TenantRefusal).code ?? String(e); }
};
const предмет = { key: memoryKey("last_screen"), value: "accounts",
                  kind: "convenience" as const, writtenAt: "2026-09-10T00:00:00.000Z" };

describe("повтор под тем же ключом: идемпотентность против тихой потери", () => {
  it("тот же ключ и ТО ЖЕ значение — идемпотентно, второй записи не возникает", () => {
    const m = new SharedMemory();
    const a = m.view("cust_a").write(предмет as never, "role-2.manager");
    const b = m.view("cust_a").write(предмет as never, "role-2.manager");
    expect(b.value).toBe(a.value);
    expect(m.view("cust_a").read(memoryKey("last_screen"))?.value).toBe("accounts");
  });

  it("тот же ключ и ДРУГОЕ значение — ОТКАЗ, а не тихая перезапись", () => {
    const m = new SharedMemory();
    m.view("cust_a").write(предмет as never, "role-2.manager");
    expect(код(() => m.view("cust_a").write({ ...предмет, value: "cards" } as never, "role-2.manager")))
      .toBe("VALUE_DIFFERS_UNDER_SAME_KEY");
    // и главное: ПЕРВОЕ значение уцелело
    expect(m.view("cust_a").read(memoryKey("last_screen"))?.value).toBe("accounts");
  });

  it("другой клиент под тем же ключом — не задевает чужого", () => {
    const m = new SharedMemory();
    m.view("cust_a").write(предмет as never, "role-2.manager");
    m.view("cust_b").write({ ...предмет, value: "cards" } as never, "role-2.manager");
    expect(m.view("cust_a").read(memoryKey("last_screen"))?.value).toBe("accounts");
    expect(m.view("cust_b").read(memoryKey("last_screen"))?.value).toBe("cards");
  });
});
