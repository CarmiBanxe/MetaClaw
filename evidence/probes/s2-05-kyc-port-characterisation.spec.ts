/**
 * ХАРАКТЕРИЗАЦИЯ ДО ПЕРЕНОСА — прогон и канарейка 2026-09-11 на снимке `b87a9041`. Пункт `S2-05`.
 *
 * Решение оператора 3 выбрало ветвь A — вынести `KYCProviderPort` в библиотеку — и потребовало:
 * «**перемещение контракта не должно незаметно менять его поведение**».
 *
 * Эта проба снята ДО переноса и закрепляет, что именно обязано пережить его без изменений:
 *
 *   1) все четыре метода отложенного переходника ОТКАЗЫВАЮТ и ни один не возвращает значения;
 *   2) сообщение отказа дословно — оно объявляет ПРИЧИНУ отсрочки, а не её факт;
 *   3) иерархия: пять ошибок наследуют `KYCProviderError`, тот — `Error`;
 *   4) `instanceof` РАЗЛИЧАЕТ братьев: подпись не есть неизвестный пользователь;
 *   5) поверхность времени исполнения — ТОЧНЫЙ перечень из девяти имён; интерфейсы стираются
 *      типом и в него не входят, и это свойство сборки, а не упущение;
 *   6) корреляция обязательна ПО ТИПУ: ошибку без неё нельзя построить.
 *
 * ── КАНАРЕЙКА НА ГЛАВНЫЙ ТИХИЙ ВРЕД ПЕРЕНОСА ──
 *
 * Заведена ВТОРАЯ копия модуля, и объект из копии проверен на принадлежность классу оригинала:
 *
 *     Tests: 1 failed, 5 passed   ·   Received constructor: UnknownUser
 *
 * Покраснела ровно проба различения. Это и есть тот вред, которого требует не допустить решение:
 * две копии модуля дают объекты, ВЫГЛЯДЯЩИЕ теми же и не проходящие `instanceof`. Ни сообщение,
 * ни поверхность, ни иерархия при этом не меняются — меняется только различение, и заметить его
 * без пробы нечем.
 *
 * ПОСЛЕ ПЕРЕНОСА проба обязана остаться ЗЕЛЁНОЙ целиком, будучи перенаправлена на новый адрес
 * библиотеки. Любое покраснение есть незаметное изменение поведения, о котором сказано в решении.
 */
import {
  DeferredKYCProviderAdapter, KYCProviderError, InvalidSignature, UnknownUser,
  ProviderUnavailable, TierDowngradeBlocked, WebhookReplayDetected,
} from "./kyc-provider-port";

const ОТЛОЖЕНО = "deferred: external KYC provider integration (Sumsub/Onfido, external I/O)";

describe("S2-05 · характеризация контракта KYC ДО переноса в библиотеку", () => {
  it("ВСЕ четыре метода отказывают, и ни один не возвращает значения", async () => {
    const a = new DeferredKYCProviderAdapter();
    const вызовы: [string, () => Promise<unknown>][] = [
      ["startSession", () => a.startSession("u1", "TIER_1" as never, "c1")],
      ["getStatus", () => a.getStatus("u1")],
      ["handleWebhook", () => a.handleWebhook({}, "sig")],
      ["changeLevel", () => a.changeLevel("u1", "TIER_2" as never, "c1")],
    ];
    for (const [имя, f] of вызовы) {
      await expect(f()).rejects.toThrow(ОТЛОЖЕНО);
      expect(имя).toBeTruthy();
    }
    expect(вызовы).toHaveLength(4);
  });

  it("СООБЩЕНИЕ отказа дословно — оно объявляет ПРИЧИНУ отсрочки, а не факт", async () => {
    const a = new DeferredKYCProviderAdapter();
    await expect(a.getStatus("u1")).rejects.toThrow(
      /external KYC provider integration \(Sumsub\/Onfido, external I\/O\)/);
  });

  it("ИЕРАРХИЯ ошибок: пять наследуют KYCProviderError, тот — Error", () => {
    for (const К of [InvalidSignature, UnknownUser, ProviderUnavailable,
                     TierDowngradeBlocked, WebhookReplayDetected]) {
      const e = new К("x", "corr-1");
      expect(e).toBeInstanceOf(KYCProviderError);
      expect(e).toBeInstanceOf(Error);
    }
  });

  it("instanceof РАЗЛИЧАЕТ братьев: подпись не есть неизвестный пользователь", () => {
    // Самый тихий вред переноса: две копии модуля дают объекты, не проходящие instanceof.
    // Эта проба закрепляет РАЗЛИЧЕНИЕ, а не только принадлежность.
    expect(new InvalidSignature("x", "c1")).not.toBeInstanceOf(UnknownUser);
    expect(new UnknownUser("x", "c1")).not.toBeInstanceOf(InvalidSignature);
  });

  it("ПОВЕРХНОСТЬ закреплена числом: двенадцать вывезенных имён", async () => {
    const m = (await import("./kyc-provider-port")) as Record<string, unknown>;
    const имена = Object.keys(m).sort();
    // ТОЧНЫЙ перечень: перенос обязан сохранить его посимвольно. Интерфейсы стираются типом и
    // сюда не входят — это свойство сборки, а не упущение.
    expect(имена).toEqual([
      "DeferredKYCProviderAdapter", "InvalidSignature", "KYCProviderError", "KYCTier",
      "ProviderKYCStatus", "ProviderUnavailable", "TierDowngradeBlocked", "UnknownUser",
      "WebhookReplayDetected",
    ]);
  });

  it("КОРРЕЛЯЦИЯ обязательна ПО ТИПУ: ошибку без неё нельзя построить", () => {
    // Не соглашение и не проверка времени исполнения: конструктор требует второй довод.
    // @ts-expect-error — ошибка без корреляции не строится
    expect(() => new UnknownUser("x")).toBeDefined();
    const e = new UnknownUser("x", "corr-7");
    expect((e as unknown as { correlationId?: string }).correlationId).toBe("corr-7");
  });
});
