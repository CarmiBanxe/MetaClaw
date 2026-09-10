/**
 * ПОКАЗ ДЕФЕКТА — прогон 2026-09-11 на снимке `b87a9041`. Пункт `S1-08`.
 *
 * Проба ЗЕЛЕНА и закрепляет СЕГОДНЯШНЕЕ поведение, признанное неверным решением оператора 8:
 * «имя `sim://` и присутствие в перечне сами по себе не удостоверяют вызывающего… двойник не
 * должен позволять ЛЮБОМУ ЗАПРОСУ присвоить должность».
 *
 *     S1-08 подъём посторонним  → 200
 *     S1-08 СНЯТИЕ посторонним  → 200      ← тяжелее: снимается ЗАЩИТА
 *
 * Посторонний, знающий строку `sim://sandbox/MLRO`, поднимает и снимает глобальную остановку.
 * Дверь проверяет ФОРМУ имени (`HOLDER_NOT_EMULATED`) и ПРИСУТСТВИЕ В ПЕРЕЧНЕ
 * (`INTERRUPTION_HOLDER_UNKNOWN`) — обе проверки работают, обе доказаны контролями здесь же — и
 * ни одна не отвечает на вопрос, КТО обращается.
 *
 * АСИММЕТРИЯ ДВЕРЕЙ, ради которой проба написана. В том же файле `server.ts` дверь
 * `/v0/director/restore` берёт личность ИЗ ЗАПРОСА:
 *
 *     const кто_просит = parts.subjects.resolve(req);
 *     if (кто_просит === undefined) → 403 SUBJECT_NOT_ESTABLISHED
 *
 * а дверь `/v0/director/interruption` — ИЗ ТЕЛА:
 *
 *     const by = String(body["by"] ?? "");
 *
 * Две двери, один вопрос, разные ответы. Образец починки написан в том же файле и в `main.ts`:
 * «заглушка, возвращающая значение из тела, вернула бы ровно ту подмену, против которой порт и
 * заведён. Пока удостоверение не построено, запись решений закрыта — отказ честнее видимости
 * работы».
 *
 * ПОСЛЕ ИСПОЛНЕНИЯ S1-08 первые две пробы обязаны ПОКРАСНЕТЬ. Контроли обязаны остаться зелёными:
 * они проверяют форму и перечень, и те никуда не деваются.
 */
import type { AddressInfo } from "node:net";
import { VolatileLog, VolatileRecords } from "@bank-tree/banksy-durable";
import { buildDirectorServer } from "./server";
import { InterruptionStore } from "../adapters/interruption-store";

const ВЫДАЮЩИЕ = { trusted: (ref: string) => ref === "sim://sandbox/MLRO" };

async function дверь() {
  const store = new InterruptionStore(new VolatileRecords() as never, new VolatileLog() as never);
  const built = buildDirectorServer({} as never,
    { interruption: store, issuers: ВЫДАЮЩИЕ } as never);
  await new Promise<void>((ok) => built.server.listen(0, "127.0.0.1", ok));
  const port = (built.server.address() as AddressInfo).port;
  return {
    port, close: () => new Promise<void>((ok) => built.server.close(() => ok())),
    async post(body: unknown) {
      const r = await fetch(`http://127.0.0.1:${port}/v0/director/interruption`, {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify(body),
      });
      return { status: r.status, body: (await r.json()) as Record<string, unknown> };
    },
  };
}

describe("S1-08 · рычаг прерывания: чем удостоверяется вызывающий", () => {
  it("ПОСТОРОННИЙ, знающий строку двойника, ПОДНИМАЕТ остановку", async () => {
    const d = await дверь();
    try {
      const r = await d.post({ by: "sim://sandbox/MLRO", reason: "основание названо словами",
                               stopped: true, scopes: [] });
      // eslint-disable-next-line no-console
      console.log("S1-08 подъём посторонним →", r.status, JSON.stringify(r.body).slice(0, 90));
      expect(r.status).toBe(200);          // ← ДЕФЕКТ: удостоверения нет, только знание строки
    } finally { await d.close(); }
  });

  it("ПОСТОРОННИЙ СНИМАЕТ остановку — и это тяжелее подъёма", async () => {
    const d = await дверь();
    try {
      await d.post({ by: "sim://sandbox/MLRO", reason: "остановка по основанию", stopped: true });
      const r = await d.post({ by: "sim://sandbox/MLRO", reason: "снятие по основанию",
                               stopped: false });
      // eslint-disable-next-line no-console
      console.log("S1-08 СНЯТИЕ посторонним →", r.status, JSON.stringify(r.body).slice(0, 90));
      expect(r.status).toBe(200);          // ← ДЕФЕКТ, и он опаснее: снимается ЗАЩИТА
    } finally { await d.close(); }
  });

  it("КОНТРОЛЬ: чужая строка вне перечня отвергается", async () => {
    const d = await дверь();
    try {
      const r = await d.post({ by: "sim://sandbox/ПОСТОРОННИЙ", reason: "основание названо",
                               stopped: true });
      expect(r.status).toBe(403);
      expect(r.body["code"]).toBe("INTERRUPTION_HOLDER_UNKNOWN");
    } finally { await d.close(); }
  });

  it("КОНТРОЛЬ: человекоподобное имя отвергается", async () => {
    const d = await дверь();
    try {
      const r = await d.post({ by: "Иван Петров", reason: "основание названо", stopped: true });
      expect(r.status).toBe(403);
      expect(r.body["code"]).toBe("HOLDER_NOT_EMULATED");
    } finally { await d.close(); }
  });
});
