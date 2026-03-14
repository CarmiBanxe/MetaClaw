<div align="center">

<img src="new_logo.png" alt="MetaClaw" width="600">

<br/>

# Parla con il tuo agente, lui impara e si *EVOLVE*.

<p>Ispirato al modo in cui il cervello apprende. Meta-apprendi e fai evolvere il tuo 🦞 da ogni conversazione reale. Nessuna GPU necessaria. Funziona con Kimi, Qwen, Claude, MiniMax e altri.</p>

⚡ Supported LLM Providers & Platforms

<table>
<tr>
<td align="center" width="100">
  <a href="https://kimi.ai">
    <img src="https://github.com/MoonshotAI.png?size=200" width="48" height="48" alt="Kimi" />
  </a><br/>
  <sub><a href="https://kimi.ai"><b>Kimi</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://qwen.ai">
    <img src="https://github.com/QwenLM.png?size=200" width="48" height="48" alt="Qwen" />
  </a><br/>
  <sub><a href="https://qwen.ai"><b>Qwen</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://www.anthropic.com/claude">
    <img src="https://cdn.simpleicons.org/claude/D97757" width="48" height="48" alt="Claude" />
  </a><br/>
  <sub><a href="https://www.anthropic.com/claude"><b>Claude</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://www.minimax.io">
    <img src="https://github.com/minimax-ai.png?size=200" width="48" height="48" alt="MiniMax" />
  </a><br/>
  <sub><a href="https://www.minimax.io"><b>MiniMax</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://openai.com">
    <img src="https://github.com/openai.png?size=200" width="48" height="48" alt="OpenAI" />
  </a><br/>
  <sub><a href="https://openai.com"><b>OpenAI</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://gemini.google.com">
    <img src="https://cdn.simpleicons.org/googlegemini/8E75B2" width="48" height="48" alt="Gemini" />
  </a><br/>
  <sub><a href="https://gemini.google.com"><b>Gemini</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>+ Much<br/>More</b></sub>
</td>
</tr>
</table>

🧬 RL Training Backends for Weight Evolution

<table>
<tr>
<td align="center" width="100">
  <a href="https://www.thinkingmachines.ai/tinker/">
    <img src="tinker.jpg" width="48" height="48" alt="Tinker" />
  </a><br/>
  <sub><a href="https://www.thinkingmachines.ai/tinker/"><b>Tinker</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://github.com/MindLab-Research/mindlab-toolkit">
    <img src="https://github.com/MindLab-Research.png?size=200" width="48" height="48" alt="MinT" />
  </a><br/>
  <sub><a href="https://github.com/MindLab-Research/mindlab-toolkit"><b>MinT</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>More<br/>Coming</b></sub>
</td>
</tr>
</table>

<p>
  <a href="https://github.com/aiming-lab/MetaClaw"><img src="https://img.shields.io/badge/github-MetaClaw-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat&labelColor=555" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/⚡_Completamente_Asincrono-yellow?style=flat&labelColor=555" alt="Fully Async" />
  <img src="https://img.shields.io/badge/☁️_Nessun_Cluster_GPU-blue?style=flat&labelColor=555" alt="No GPU Cluster" />
  <img src="https://img.shields.io/badge/🛠️_Evoluzione_delle_Skill-orange?style=flat&labelColor=555" alt="Skill Evolution" />
  <img src="https://img.shields.io/badge/🚀_Deploy_con_Un_Click-green?style=flat&labelColor=555" alt="One-Click Deploy" />
</p>

<br/>

[🇺🇸 English](../README.md) • [🇨🇳 中文](./README_ZH.md) • [🇯🇵 日本語](./README_JA.md) • [🇰🇷 한국어](./README_KO.md) • [🇫🇷 Français](./README_FR.md) • [🇩🇪 Deutsch](./README_DE.md) • [🇪🇸 Español](./README_ES.md) • [🇧🇷 Português](./README_PT.md) • [🇷🇺 Русский](./README_RU.md) • [🇻🇳 Tiếng Việt](./README_VI.md) • [🇸🇦 العربية](./README_AR.md) • [🇮🇳 हिन्दी](./README_HI.md)

<br/>

[Panoramica](#-panoramica) • [Avvio Rapido](#-avvio-rapido) • [Comandi CLI](#️-comandi-cli) • [Configurazione](#️-configurazione) • [Skills](#-skills) • [Modalita RL](#-avanzato-modalita-rl) • [Modalita OPD](#-avanzato-modalita-opd) • [Scheduler di Meta-Apprendimento](#-avanzato-scheduler-di-meta-apprendimento-v03) • [Citazione](#-citazione)

</div>

---

<div align="center">

### Due comandi. Tutto qui.
</div>

```bash
metaclaw setup              # configurazione guidata iniziale
metaclaw start              # predefinito: modalita madmax, Skill + addestramento RL programmato
metaclaw start --mode rl    # RL senza scheduler (addestra immediatamente a batch completo)
metaclaw start --mode skills_only  # solo Skill, nessun RL (Tinker non necessario)
```

<div align="center">
<img src="metaclaw.gif" alt="MetaClaw demo" width="700">
</div>

---

## 🔥 Novita

- **[13/03/2026]** **v0.3.1** Supporto backend MinT: l'addestramento RL ora funziona sia con Tinker che con MinT. Configurabile tramite `rl.backend` (auto/tinker/mint).
- **[13/03/2026]** **v0.3** Supporto al meta-apprendimento continuo: gli aggiornamenti RL lenti vengono eseguiti solo durante le ore di sonno, i periodi di inattivita o le riunioni di Google Calendar. Aggiunta la separazione tra set support/query per evitare che segnali di ricompensa obsoleti inquinino gli aggiornamenti del modello.
- **[11/03/2026]** **v0.2** Deploy con un click tramite la CLI `metaclaw`. Le Skill sono attive per impostazione predefinita, l'RL e ora opzionale.
- **[09/03/2026]** Rilascio ufficiale di **MetaClaw**. Parla con il tuo agente e lascia che si evolva automaticamente. **Nessuna** GPU necessaria, basta collegarsi alla **API**.

---

## 🎥 Demo

https://github.com/user-attachments/assets/d86a41a8-4181-4e3a-af0e-dc453a6b8594

---

## 📖 Panoramica

**MetaClaw e un agente che meta-apprende e si evolve in scenari reali.**
Parla con il tuo agente come faresti normalmente. MetaClaw trasforma ogni conversazione in tempo reale in un segnale di apprendimento, consentendo all'agente di migliorare continuamente attraverso il deploy nel mondo reale, non solo con l'addestramento offline.

Sotto il cofano, posiziona il tuo modello dietro un proxy compatibile con OpenAI che intercetta le interazioni da OpenClaw, inietta le Skill pertinenti ad ogni turno e meta-apprende dall'esperienza accumulata. Le Skill vengono riassunte automaticamente dopo ogni sessione; con l'RL attivato, uno scheduler di meta-apprendimento posticipa gli aggiornamenti dei pesi alle finestre di inattivita, in modo che l'agente non venga mai interrotto durante l'uso attivo.

Nessun cluster GPU necessario. MetaClaw funziona con qualsiasi API LLM compatibile con OpenAI, e utilizza un backend compatibile con Tinker per l'addestramento LoRA nel cloud. [Tinker](https://www.thinkingmachines.ai/tinker/) e il percorso di riferimento predefinito, e MinT puo essere abilitato tramite un pacchetto di compatibilita separato quando necessario.

## 🤖 Funzionalita Principali

### **Deploy con un click**
Configura una sola volta con `metaclaw setup`, poi `metaclaw start` avvia il proxy, inietta le Skill e collega OpenClaw automaticamente. Nessuno script shell manuale necessario.

### **Tre modalita operative**

| Modalita | Predefinita | Descrizione |
|----------|-------------|-------------|
| `madmax` | ✅ | RL + scheduler intelligente. Le Skill sono sempre attive; gli aggiornamenti dei pesi RL vengono eseguiti solo durante le finestre di sonno/inattivita/riunioni. |
| `rl` | - | RL senza scheduler. Addestra immediatamente quando il batch e pieno (comportamento originale v0.2). |
| `skills_only` | - | Proxy verso la tua API LLM. Skill iniettate, riassunte automaticamente dopo ogni sessione. Nessuna GPU / Tinker necessaria. |

### **Iniezione delle Skill**
Ad ogni turno, MetaClaw recupera le istruzioni Skill piu pertinenti e le inietta nel system prompt dell'agente. Miglioramento immediato del comportamento senza riaddestramento.

### **Riepilogo automatico delle Skill**
Dopo ogni conversazione, lo stesso LLM che stai gia utilizzando analizza la sessione e genera nuove Skill automaticamente. Con l'RL attivato, un modello giudice dedicato estrae le Skill dagli episodi falliti.

### **Nessun cluster GPU necessario**
In modalita `skills_only`, serve solo una connessione di rete. L'addestramento RL viene delegato a un backend compatibile con Tinker.

### **Due modalita di apprendimento**
MetaClaw supporta entrambe:
- **RL (GRPO)** per apprendere da segnali di feedback impliciti
- **Distillazione On-Policy (OPD)** per distillare un modello teacher piu grande nello studente on-policy

In modalita OPD, il modello studente genera le risposte normalmente, e un modello teacher fornisce le log-probabilita per token sulle stesse risposte. Le logprob del teacher vengono passate alla funzione di loss (es. `cispo`) cosi che lo studente impari a replicare la distribuzione del teacher. Il teacher deve essere servito dietro un endpoint `/v1/completions` compatibile con OpenAI (es. vLLM, SGLang).

### **Completamente asincrono per design**
Serving, reward modeling e addestramento sono completamente disaccoppiati. L'agente continua a rispondere mentre lo scoring e l'ottimizzazione vengono eseguiti in parallelo.

---

## 🚀 Avvio Rapido

### 1. Installazione

```bash
pip install -e .                        # modalita skills_only (leggera)
pip install -e ".[rl]"                  # + supporto addestramento RL (torch, transformers, tinker)
pip install -e ".[evolve]"              # + evoluzione Skill tramite LLM compatibile OpenAI
pip install -e ".[scheduler]"           # + integrazione Google Calendar per lo scheduler
pip install -e ".[rl,evolve,scheduler]" # consigliato per la configurazione completa RL + scheduler
```

Se vuoi usare `rl.backend=mint`, installa separatamente il pacchetto di compatibilita MinT nello stesso ambiente, ad esempio [`mindlab-toolkit`](https://github.com/MindLab-Research/mindlab-toolkit). MetaClaw mantiene questa dipendenza fuori dal pacchetto predefinito, cosi gli utenti RL possono scegliere esplicitamente tra Tinker e MinT.

### 2. Configurazione

```bash
metaclaw setup
```

La procedura guidata interattiva ti chiedera di scegliere il tuo provider LLM (Kimi, Qwen, MiniMax o personalizzato), inserire la tua API key e, opzionalmente, abilitare l'addestramento RL.

Il percorso RL di MetaClaw puo commutare esplicitamente tra `tinker` e `mint`. `auto` e il valore predefinito consigliato e inferira comunque MinT da credenziali o base URL in stile Mint quando il pacchetto MinT e installato.

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
```

Gli alias legacy `rl.tinker_api_key` e `rl.tinker_base_url` sono ancora accettati per compatibilita con le versioni precedenti.

### 3. Avvio

```bash
metaclaw start
```

Tutto qui. MetaClaw avvia il proxy, configura automaticamente OpenClaw e riavvia il gateway. Apri OpenClaw e inizia a chattare: le Skill vengono iniettate ad ogni turno, e la sessione viene automaticamente riassunta in nuove Skill al termine.

---

## 🛠️ Comandi CLI

```
metaclaw setup                  # Procedura guidata di configurazione iniziale
metaclaw start                  # Avvia MetaClaw (predefinito: modalita madmax)
metaclaw start --mode rl        # Forza la modalita RL (senza scheduler) per questa sessione
metaclaw start --mode skills_only  # Forza la modalita solo Skill per questa sessione
metaclaw stop                   # Ferma un'istanza MetaClaw in esecuzione
metaclaw status                 # Controlla lo stato del proxy, la modalita e lo scheduler
metaclaw config show            # Visualizza la configurazione corrente
metaclaw config KEY VALUE       # Imposta un valore di configurazione
```

**Chiavi di configurazione comuni:**

```bash
metaclaw config rl.enabled true           # Abilita l'addestramento RL
metaclaw config rl.backend auto           # auto | tinker | mint
metaclaw config rl.api_key sk-...         # Imposta la chiave del backend RL
metaclaw config rl.base_url https://mint.macaron.xin/  # Endpoint backend opzionale, es. MinT
metaclaw config skills.auto_evolve false  # Disabilita il riepilogo automatico delle Skill
metaclaw config proxy.port 31000          # Cambia la porta del proxy
```

---

## ⚙️ Configurazione

La configurazione si trova in `~/.metaclaw/config.yaml`, creata da `metaclaw setup`.

```yaml
mode: madmax               # "madmax" | "rl" | "skills_only"

llm:
  provider: kimi            # kimi | qwen | openai | minimax | custom
  model_id: moonshotai/Kimi-K2.5
  api_base: https://api.moonshot.cn/v1
  api_key: sk-...

proxy:
  port: 30000
  api_key: ""              # opzionale: bearer token per il proxy MetaClaw locale

skills:
  enabled: true
  dir: ~/.metaclaw/skills   # la tua libreria di Skill
  retrieval_mode: template  # template | embedding
  top_k: 6
  task_specific_top_k: 10   # limite Skill specifiche per task (predefinito 10)
  auto_evolve: true         # riepilogo automatico delle Skill dopo ogni sessione

rl:
  enabled: false            # impostare su true per abilitare l'addestramento RL
  backend: auto             # "auto" | "tinker" | "mint"
  model: moonshotai/Kimi-K2.5
  api_key: ""
  base_url: ""              # endpoint backend opzionale, es. https://mint.macaron.xin/ per MinT
  tinker_api_key: ""        # alias legacy per api_key
  tinker_base_url: ""       # alias legacy per base_url
  prm_url: https://api.openai.com/v1
  prm_model: gpt-5.2
  prm_api_key: ""
  lora_rank: 32
  batch_size: 4
  resume_from_ckpt: ""      # opzionale: percorso checkpoint per riprendere l'addestramento
  evolver_api_base: ""      # lasciare vuoto per riutilizzare llm.api_base
  evolver_api_key: ""
  evolver_model: gpt-5.2

opd:
  enabled: false            # impostare su true per abilitare OPD (distillazione teacher)
  teacher_url: ""           # base URL del modello teacher (OpenAI-compatibile /v1/completions)
  teacher_model: ""         # nome del modello teacher (es. Qwen/Qwen3-32B)
  teacher_api_key: ""       # API key del modello teacher
  kl_penalty_coef: 1.0      # coefficiente di penalita KL per OPD

max_context_tokens: 20000   # limite di token del prompt prima del troncamento

scheduler:                  # v0.3: scheduler di meta-apprendimento (abilitato automaticamente in modalita madmax)
  enabled: false            # la modalita madmax lo abilita automaticamente; impostare manualmente per la modalita rl
  sleep_start: "23:00"
  sleep_end: "07:00"
  idle_threshold_minutes: 30
  min_window_minutes: 15
  calendar:
    enabled: false
    credentials_path: ""
    token_path: ""
```

---

## 💪 Skills

Le Skill sono brevi istruzioni Markdown iniettate nel system prompt dell'agente ad ogni turno. Si trovano nella directory delle Skill (`~/.metaclaw/skills/` per impostazione predefinita), organizzate come singoli file `SKILL.md`.

Il **riepilogo automatico delle Skill** viene eseguito dopo ogni conversazione. L'LLM configurato analizza automaticamente cosa e successo e genera nuove Skill. Nessuna curatela manuale necessaria: la libreria cresce con l'utilizzo.

Per precaricare la banca di Skill integrata (oltre 40 Skill per coding, sicurezza, task agentici e altro):

```bash
cp -r memory_data/skills/* ~/.metaclaw/skills/
```

---

## 🔬 Avanzato: Modalita RL

Abilita l'addestramento RL per perfezionare continuamente il modello dalle conversazioni in tempo reale, con Tinker o MinT:

```bash
metaclaw config rl.enabled true
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
metaclaw config rl.prm_url https://api.openai.com/v1
metaclaw config rl.prm_api_key sk-...
metaclaw start
```

In modalita RL:
- Ogni turno di conversazione viene tokenizzato e inviato come campione di addestramento
- Un LLM giudice (PRM) valuta le risposte in modo asincrono
- Un backend compatibile con Tinker, come Tinker cloud o MinT, esegue il fine-tuning LoRA; i pesi aggiornati vengono sostituiti a caldo ogni `batch_size` campioni
- Un LLM evolver dedicato estrae nuove Skill dagli episodi falliti

Se preferisci Tinker cloud, imposta `rl.backend` su `tinker` oppure lascialo su `auto` e ometti l'endpoint MinT.

**Rollout programmatico** (senza la TUI di OpenClaw): imposta `openclaw_env_data_dir` su una directory contenente file JSONL di task:

```json
{"task_id": "task_1", "instruction": "Register the webhook at https://example.com/hook"}
```

---

## 🔬 Avanzato: Modalita OPD

La Distillazione On-Policy (OPD) permette di distillare un modello teacher piu grande nello studente mentre quest'ultimo si addestra on-policy. Il modello studente genera le risposte normalmente; il modello teacher fornisce le log-probabilita per token sulle stesse risposte. Una penalita KL guida lo studente verso la distribuzione del teacher.

```bash
metaclaw config opd.enabled true
metaclaw config opd.teacher_url http://localhost:8082/v1
metaclaw config opd.teacher_model Qwen/Qwen3-32B
metaclaw config opd.kl_penalty_coef 1.0
metaclaw start --mode rl
```

Il teacher deve essere servito dietro un endpoint `/v1/completions` compatibile con OpenAI (es. vLLM, SGLang). L'OPD puo essere combinato con lo scoring PRM: entrambi vengono eseguiti in modo asincrono.

Consulta `examples/run_conversation_opd.py` per un esempio programmatico e `scripts/run_openclaw_tinker_opd.sh` per uno script di avvio pronto all'uso.

---

## 🧠 Avanzato: Scheduler di Meta-Apprendimento (v0.3)

In modalita RL, il passaggio di sostituzione a caldo dei pesi mette in pausa l'agente per diversi minuti. Lo scheduler (abilitato per impostazione predefinita in modalita `madmax`) posticipa gli aggiornamenti RL alle finestre di inattivita dell'utente, in modo che l'agente non venga mai interrotto durante l'uso attivo.

```bash
metaclaw config scheduler.sleep_start "23:00"
metaclaw config scheduler.sleep_end   "07:00"
metaclaw config scheduler.idle_threshold_minutes 30

# Opzionale: integrazione Google Calendar
pip install -e ".[scheduler]"
metaclaw config scheduler.calendar.enabled true
metaclaw config scheduler.calendar.credentials_path ~/.metaclaw/client_secrets.json
```

Tre condizioni attivano una finestra di aggiornamento (una qualsiasi e sufficiente): le ore di sonno configurate, l'inattivita della tastiera di sistema o un evento attivo di Google Calendar. Se l'utente ritorna durante un aggiornamento, il batch parziale viene salvato e ripreso alla finestra successiva.

Ogni `ConversationSample` e contrassegnato con una versione `skill_generation`. Quando l'evoluzione delle Skill incrementa la generazione, il buffer RL viene svuotato in modo che solo i campioni post-evoluzione vengano utilizzati per gli aggiornamenti del gradiente (separazione set support/query MAML).

---

## 📚 Citazione

```bibtex
@misc{xia2026metaclaw,
  author       = {Xia, Peng and Chen, Jianwen and Yang, Xinyu and Tu, Haoqin and Han, Siwei and Qiu, Shi and Zheng, Zeyu and Xie, Cihang and Yao, Huaxiu},
  title        = {MetaClaw: Just Talk --- An Agent That Meta-Learns and Evolves in the Wild},
  year         = {2026},
  organization = {GitHub},
  url          = {https://github.com/aiming-lab/MetaClaw},
}
```

---

## 🙏 Ringraziamenti

MetaClaw si basa sui seguenti progetti open-source:

- [OpenClaw](https://openclaw.ai) - il framework agente principale.
- [SkillRL](https://github.com/aiming-lab/SkillRL) - il nostro framework RL potenziato con Skill.
- [Tinker](https://www.thinkingmachines.ai/tinker/) - utilizzato per l'addestramento RL online.
- [MinT](https://github.com/MindLab-Research/mindlab-toolkit) - backend alternativo per l'addestramento RL online.
- [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) - ispirazione per il nostro design RL.
- [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - fornisce le basi per la nostra banca di Skill.

---

## 📄 Licenza

Questo progetto e distribuito sotto la [Licenza MIT](LICENSE).
