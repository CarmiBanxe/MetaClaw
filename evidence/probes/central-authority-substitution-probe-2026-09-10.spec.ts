/**
 * ПРОБА ЦЕНТРАЛЬНОГО ТЕРМИНАЛА — недоверенное заявление как основание полномочий. РЕДАКЦИЯ 3.
 *
 * ПОЧЕМУ РЕДАКЦИЯ 3. Редакция 2 **перестала собираться**: у `issue` появился третий довод —
 * содержимое конверта. Это и была починка, которую проба нашла: «дефект жил не в проверке, а в
 * ФОРМЕ ЗАПИСИ: она не умела выразить того, что обязана была закрепить».
 *
 * Проба, переставшая компилироваться, тихо перестала быть пробой: она не красная и не зелёная,
 * её просто нет. Это хуже непадающей — та хотя бы числится.
 *
 * ЧТО ИЗМЕРЕНО РЕДАКЦИЕЙ 3. Подделка содержимого ОТВЕРГАЕТСЯ ЦЕЛИКОМ кодом
 * `AUTHORITY_CONTENT_ALTERED` — и расширение `allowed`, и стирание `prohibited` пустым массивом.
 * Не «очищается молча», а именно отвергается: очистка позволила бы предъявителю узнать, что его
 * подмену заметили и простили.
 *
 * КАНАРЕЙКА: сверка `allowed`/`prohibited` с записью ослеплена (`&& false` у обоих сравнений) —
 * `Tests: 2 failed, 2 passed`. Покраснели ровно две подменные; «годный конверт» и «конверт,
 * никем не выданный» остались зелёными. Различает.
 *
 * ЧЕГО ЭТА ПРОБА НЕ ДОКАЗЫВАЕТ: что имя выдающего связано с содержимым чем-то, кроме перечня
 * доверенных. Носитель говорит об этом сам: «`trusted` отвечает на вопрос об ИМЕНИ, и одного
 * имени мало».
 */
import { NamedIssuers, VolatileRevocations, verifyEnvelope } from "./authority-envelope";

const ВЫДАЮЩИЙ = "оператор";
const реестр = () => {
  const i = new NamedIssuers([ВЫДАЮЩИЙ]);
  i.issue("env-1", ВЫДАЮЩИЙ, { allowed: ["write:src/"], prohibited: ["network:egress"],
                                scope: { workId: "работа-1" } });
  return i;
};
const конверт = (over: Record<string, unknown> = {}) =>
  ({ allowed: ["write:src/"], prohibited: ["network:egress"], grantedBy: ВЫДАЮЩИЙ,
     envelopeId: "env-1", scope: { workId: "работа-1" },
     issuedAt: "2026-09-10T00:00:00Z", ...over });

describe("central: содержимое берётся у ВЫДАВШЕГО, а не у предъявителя", () => {
  it("годный конверт проходит", () => {
    const v = verifyEnvelope(конверт(), { workId: "работа-1" }, реестр(), new VolatileRevocations());
    expect(v.ok).toBe(true);
  });

  it("предъявитель РАСШИРЯЕТ allowed — наружу уходит ЗАПИСЬ, а не предъявление", () => {
    const v = verifyEnvelope(конверт({ allowed: ["write:/etc/shadow"] }), { workId: "работа-1" },
                             реестр(), new VolatileRevocations());
    // Замер: расширенный перечень ОТВЕРГАЕТСЯ целиком, а не очищается молча.
    expect(v.ok).toBe(false);
    expect((v as { code?: string }).code).toBe("AUTHORITY_CONTENT_ALTERED");
  });

  it("предъявитель СТИРАЕТ prohibited пустым массивом — запрет остаётся", () => {
    const v = verifyEnvelope(конверт({ prohibited: [] }), { workId: "работа-1" },
                             реестр(), new VolatileRevocations());
    expect(v.ok).toBe(false);
    expect((v as { code?: string }).code).toBe("AUTHORITY_CONTENT_ALTERED");
  });

  it("конверт, никем не выданный, не проходит", () => {
    const v = verifyEnvelope(конверт({ envelopeId: "env-чужой" }), { workId: "работа-1" },
                             реестр(), new VolatileRevocations());
    expect(v.ok).toBe(false);
  });
});
