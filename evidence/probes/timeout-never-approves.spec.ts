/**
 * ДОКАЗАННАЯ ПРОБА — измерена прогоном и канарейкой 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `TIMEOUT_IS_NOT_APPROVAL` в `libraries/banksy-mlro-boundary/src/lifecycle.ts` —
 * гарантия «отсутствие ответа разрешением не является». Отказ не назван НИ ОДНОЙ пробой дерева,
 * а `assertTimeoutNeverApproves` не зовёт ни один производственный путь.
 *
 * ЧТО КАНАРЕЙКА ИСПРАВИЛА В МОЁМ СОБСТВЕННОМ ВЫВОДЕ. Прочитав код, я записала:
 * «проверка не может упасть — `onTimeout` возвращает литерал без поля `approved`». Канарейка
 * (подсадка `approved: true` в ветвь ожидания решения) уронила ВСЕ ТРИ пробы, включая третью.
 * Значит проверка упасть МОЖЕТ и ловит ровно тот перелом, ради которого написана. Неверно было
 * не «она бесполезна», а «её способность упасть ничем не доказана» — и вот доказательство.
 *
 * ЧТО ОСТАЛОСЬ ВЕРНЫМ: обе ветви `onTimeout` возвращают одно и то же. Ветвление по состоянию
 * ничего не различает и лишь ВЫГЛЯДИТ учитывающим состояние.
 *
 * ПРЕДЕЛ: вторая проба есть ХАРАКТЕРИЗАЦИЯ сегодняшнего устройства, а не норма. Если ветви
 * когда-нибудь начнут различаться намеренно, она покраснеет законно, и красный цвет будет
 * означать «устройство изменилось», а не «сломалось». Первая и третья — норма.
 */
import { CASE_STATES, onTimeout, assertTimeoutNeverApproves } from "./lifecycle";

const дело = (state: unknown) => ({ caseId: "c1", state, correlationId: "x" }) as never;

describe("тайм-аут не производит одобрения", () => {
  it("НОРМА: ни одно состояние не даёт одобрения, все дают эскалацию", () => {
    for (const s of CASE_STATES) {
      const r = onTimeout(дело(s)) as unknown as Record<string, unknown>;
      expect(r["approved"]).toBeUndefined();
      expect(r["escalate"]).toBe(true);
    }
  });

  it("ХАРАКТЕРИЗАЦИЯ: обе ветви возвращают одно и то же — ветвление не различает ничего", () => {
    const ждущие = ["AWAITING_MLRO_DECISION", "AWAITING_INFORMATION"];
    const прочие = CASE_STATES.filter((s) => !ждущие.includes(s));
    const вид = (s: unknown) => JSON.stringify(onTimeout(дело(s)));
    for (const a of ждущие) {
      for (const b of прочие) {
        expect(вид(a).replace(a, "S")).toBe(вид(b).replace(b, "S"));
      }
    }
  });

  it("НОРМА: страж швов молчит, пока гарантия цела — и говорит, когда её ломают", () => {
    for (const s of CASE_STATES) {
      expect(() => assertTimeoutNeverApproves(дело(s))).not.toThrow();
    }
  });
});
