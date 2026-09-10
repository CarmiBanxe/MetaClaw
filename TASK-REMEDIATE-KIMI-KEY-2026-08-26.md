# TASK: Remediate Kimi API Key Access

**Date:** 2026-08-26  
**Priority:** P2 (blocking future consultations)  
**Assignee:** Operator  
**Context:** Canon Consolidation Fork consultation

---

## PROBLEM

Kimi (Moonshot) API unavailable despite 3 keys provided:
- `sk-dBf2QELANFatX1G8ybASFfyXc5GSKr8C9HAWWoaR6WRixrXz` (banxe-consortium)
- `sk-uZo57mXOcE26XjMRxxlGUS0HDuj2n1FDGmsQIAthOivtTcit` (banxe-consortium-2)
- `sk-k0y4EN7vOg13OwcjNB3...` (banxe-consortium-3, partial)

**Error:** `Invalid Authentication` (Moonshot API) / `User not found` (OpenRouter)

---

## ROOT CAUSE HYPOTHESIS

1. Keys not activated in Moonshot dashboard
2. Billing not configured
3. Email/phone verification pending
4. Key format mismatch (extra `sk-` in OpenRouter prefix)
5. Model name deprecated (tried: kimi-k2-0711, kimi-latest, kimi-k1.5, kimi-k2)

---

## REMEDIATION STEPS

### Option A: Moonshot Direct

1. Visit https://platform.moonshot.cn/
2. Check key status for all 3 keys
3. Verify billing setup
4. Complete any pending verification
5. Test key with:
   ```bash
   curl https://api.moonshot.cn/v1/models \
     -H "Authorization: Bearer <key>"
   ```

### Option B: OpenRouter

1. Visit https://openrouter.ai/keys
2. Verify keys are active
3. Check if Kimi/Moonshot model available
4. Test with correct key format (no extra `sk-` in prefix)

### Option C: Generate New Key

1. Create new Moonshot account/project
2. Generate fresh key
3. Share via secure channel

---

## ACCEPTANCE CRITERIA

- [ ] At least one key returns valid model list
- [ ] Test chat completion succeeds
- [ ] Document working key reference (NOT the key itself)

---

## IMPACT

- Current consultation: COMPLETED with 3 opinions (sufficient per canon)
- Future consultations: Kimi unavailable until resolved
- Mitigation: Use Codex primary + Fable-5 second + Mistral/Ollama third

---

**Filed by:** BEN (Right Terminal)  
**Status:** OPEN awaiting operator action
