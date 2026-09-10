/**
 * ДОКАЗАННАЯ ПРОБА — прогон и ДВЕ канарейки 2026-09-10 на снимке `b87a9041`.
 *
 * Предмет: `OUTCOME_UNREADABLE` — ПОСЛЕДНИЙ отказ дирижёра, которого не держало НИ ЧТО.
 *
 * Как он найден: пересечением двух мер. «Не проверен пробой» ∩ «не сужает тип» дало у дирижёра
 * ТРИ имени, из которых два оказались ложными (`DIRECT_CBS_FORBIDDEN` стережёт дорогу, которой
 * нет; `HARDCODED_THRESHOLD` проверен типом исключения в соседнем файле). Остался один.
 *
 * Почему он был непроверяем: `outcomeOf` НЕ вывезена наружу. Проба идёт через `Instructor` с
 * подставным переносом — тот подаётся конструктором, и это единственная причина, по которой
 * предмет вообще досягаем.
 *
 * ДОКТРИНА, записанная в самом носителе: «Неизвестный исход НЕ приводится к ближайшему:
 * приведение выдало бы ДОГАДКУ за ответ отдела».
 *
 * ── НАЙДЕНО СВЕРХ ЗАДАЧИ, и обе находки закреплены пробами ──
 *   1) `405` и прочий не-200 суть РАЗНЫЕ отказы: «не приняли поручение» и «отдел отказал» —
 *      разные предметы, и свести их в один значило бы потерять причину.
 *   2) Положение решившего по умолчанию — `emulated`, а НЕ `appointed`. Умолчание в сторону
 *      покоя: неизвестное положение не выдаётся за назначение.
 *
 * ── КАНАРЕЙКИ ──
 *   неизвестный исход приводится к «решено»  →  2 failed, 3 passed (обе пробы неизвестного)
 *   положение по умолчанию — «назначено»     →  1 failed, 4 passed (ровно она)
 *
 * Служба вне карантина переноса.
 */
import { Instructor, type InstructionTransport } from "./http-instruction";

const перенос = (body: Record<string, unknown>, status = 200): InstructionTransport => ({
  async send() { return { status, body }; },
});
const поручение = {
  correlationId: "c1", room: "комната-1", verb: "prepare" as const,
  task: "подготовить выписку", expectedOutcome: "выписка", dueBy: "2026-09-11T00:00:00Z",
  changesState: false,
};
const дать = async (body: Record<string, unknown>, status = 200) => {
  const i = new Instructor(new Map([["комната-1", "http://127.0.0.1:9/dep"]]),
                           перенос(body, status));
  return i.instruct(поручение as never);
};

describe("исход отдела: неизвестное НЕ приводится к ближайшему", () => {
  it("OUTCOME_UNREADABLE — вид исхода не из перечня", async () => {
    const r = await дать({ outcome: { kind: "почти_решено", decided_by: "кто-то" } });
    expect(r.outcome).toEqual({ kind: "refused", refusalCode: "OUTCOME_UNREADABLE" });
  });

  it("OUTCOME_UNREADABLE — исхода нет вовсе", async () => {
    const r = await дать({});
    expect(r.outcome).toEqual({ kind: "refused", refusalCode: "OUTCOME_UNREADABLE" });
  });

  it("КОНТРОЛЬ: три известных вида читаются каждый по-своему", async () => {
    expect((await дать({ outcome: { kind: "prepared", prepared_by: "отдел" } })).outcome)
      .toEqual({ kind: "prepared", preparedBy: "отдел", awaitingDecision: true });
    expect((await дать({ outcome: { kind: "decided", decided_by: "чел", standing: "appointed" } })).outcome)
      .toEqual({ kind: "decided", decidedBy: "чел", standing: "appointed" });
    expect((await дать({ outcome: { kind: "refused", refusal_code: "СВОЙ_КОД" } })).outcome)
      .toEqual({ kind: "refused", refusalCode: "СВОЙ_КОД" });
  });

  it("ОТДЕЛЬНО: 405 и прочий не-200 суть РАЗНЫЕ отказы, а не один", async () => {
    expect((await дать({}, 405)).outcome)
      .toEqual({ kind: "refused", refusalCode: "INSTRUCTION_NOT_ACCEPTED" });
    expect((await дать({ code: "СВОЙ" }, 500)).outcome)
      .toEqual({ kind: "refused", refusalCode: "СВОЙ" });
  });

  it("положение решившего по умолчанию ЭМУЛИРОВАНО, а не назначено", async () => {
    // Умолчание в сторону покоя: неизвестное положение не выдаётся за назначение.
    const r = await дать({ outcome: { kind: "decided", decided_by: "чел" } });
    expect(r.outcome).toEqual({ kind: "decided", decidedBy: "чел", standing: "emulated" });
  });
});
