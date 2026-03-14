<div align="center">

<img src="new_logo.png" alt="MetaClaw" width="600">

<br/>

# Apenas converse com seu agente, ele aprende e *EVOLUI*.

<p>Inspirado em como o cerebro aprende. Meta-aprenda e evolua seu 🦞 a partir de cada conversa real. Sem necessidade de GPU. Compativel com Kimi, Qwen, Claude, MiniMax e mais.</p>

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
  <img src="https://img.shields.io/badge/⚡_Totalmente_Assíncrono-yellow?style=flat&labelColor=555" alt="Totalmente Assíncrono" />
  <img src="https://img.shields.io/badge/☁️_Sem_Cluster_GPU-blue?style=flat&labelColor=555" alt="Sem Cluster GPU" />
  <img src="https://img.shields.io/badge/🛠️_Evolução_de_Skills-orange?style=flat&labelColor=555" alt="Evolução de Skills" />
  <img src="https://img.shields.io/badge/🚀_Deploy_com_Um_Clique-green?style=flat&labelColor=555" alt="Deploy com Um Clique" />
</p>

<br/>

[🇺🇸 English](../README.md) • [🇨🇳 中文](./README_ZH.md) • [🇯🇵 日本語](./README_JA.md) • [🇰🇷 한국어](./README_KO.md) • [🇫🇷 Français](./README_FR.md) • [🇩🇪 Deutsch](./README_DE.md) • [🇪🇸 Español](./README_ES.md) • [🇷🇺 Русский](./README_RU.md) • [🇮🇹 Italiano](./README_IT.md) • [🇻🇳 Tiếng Việt](./README_VI.md) • [🇸🇦 العربية](./README_AR.md) • [🇮🇳 हिन्दी](./README_HI.md)

<br/>

[Visao Geral](#-visao-geral) • [Inicio Rapido](#-inicio-rapido) • [Comandos CLI](#️-comandos-cli) • [Configuracao](#️-configuracao) • [Skills](#-skills) • [Modo RL](#-avancado-modo-rl) • [Modo OPD](#-avancado-modo-opd) • [Agendador de Meta-Aprendizado](#-avancado-agendador-de-meta-aprendizado-v03) • [Citacao](#-citacao)

</div>

---

<div align="center">

### Dois comandos. So isso.
</div>

```bash
metaclaw setup              # assistente de configuracao inicial
metaclaw start              # padrao: modo madmax, Skills + treinamento RL agendado
metaclaw start --mode rl    # RL sem agendador (treina imediatamente com batch completo)
metaclaw start --mode skills_only  # apenas Skills, sem RL (sem necessidade de Tinker)
```

<div align="center">
<img src="metaclaw.gif" alt="MetaClaw demo" width="700">
</div>

---

## 🔥 Novidades

- **[13/03/2026]** **v0.3.1** Suporte ao backend MinT: o treinamento RL agora funciona tanto com Tinker quanto com MinT. Configuravel via `rl.backend` (auto/tinker/mint).
- **[13/03/2026]** **v0.3** Suporte a meta-aprendizado continuo: atualizacoes lentas de RL agora so ocorrem durante horarios de sono, tempo ocioso ou reunioes do Google Calendar. Adicionada separacao de conjuntos support/query para evitar que sinais de recompensa obsoletos contaminem as atualizacoes do modelo.
- **[11/03/2026]** **v0.2** Deploy com um clique via CLI `metaclaw`. Skills habilitadas por padrao, RL agora e opcional.
- **[09/03/2026]** Lancamento do **MetaClaw**. Apenas converse com seu agente e deixe-o evoluir automaticamente. **Sem necessidade** de deploy com GPU, basta conectar na **API**.

---

## 🎥 Demonstracao

https://github.com/user-attachments/assets/d86a41a8-4181-4e3a-af0e-dc453a6b8594

---

## 📖 Visao Geral

**MetaClaw e um agente que meta-aprende e evolui em cenarios reais.**
Basta conversar com seu agente normalmente. O MetaClaw transforma cada conversa ao vivo em um sinal de aprendizado, permitindo que o agente melhore continuamente por meio de implantacao no mundo real, e nao apenas por treinamento offline.

Internamente, ele posiciona seu modelo atras de um proxy compativel com OpenAI que intercepta interacoes do OpenClaw, injeta skills relevantes a cada turno e meta-aprende a partir da experiencia acumulada. As skills sao resumidas automaticamente apos cada sessao; com RL habilitado, um agendador de meta-aprendizado adia atualizacoes de pesos para janelas ociosas, garantindo que o agente nunca seja interrompido durante o uso ativo.

Sem necessidade de cluster GPU. O MetaClaw funciona com qualquer API LLM compativel com OpenAI, e utiliza um backend compativel com Tinker para treinamento LoRA na nuvem. O [Tinker](https://www.thinkingmachines.ai/tinker/) e o caminho de referencia padrao, e o MinT pode ser habilitado por meio de um pacote de compatibilidade separado quando necessario.

## 🤖 Funcionalidades Principais

### **Deploy com um clique**
Configure uma vez com `metaclaw setup`, depois `metaclaw start` inicia o proxy, injeta skills e conecta o OpenClaw automaticamente. Sem necessidade de scripts shell manuais.

### **Tres modos de operacao**

| Modo | Padrao | O que faz |
|------|--------|-----------|
| `madmax` | ✅ | RL + agendador inteligente. Skills sempre ativas; atualizacoes de pesos RL ocorrem apenas durante janelas de sono/ociosidade/reuniao. |
| `rl` | - | RL sem agendador. Treina imediatamente quando o batch esta completo (comportamento original v0.2). |
| `skills_only` | - | Proxy para sua API LLM. Skills injetadas, resumidas automaticamente apos cada sessao. Sem necessidade de GPU/Tinker. |

### **Injecao de Skills**
A cada turno, o MetaClaw recupera as instrucoes de skill mais relevantes e as injeta no system prompt do agente. Melhoria imediata de comportamento sem necessidade de retreinamento.

### **Resumo automatico de Skills**
Apos cada conversa, o mesmo LLM que voce ja esta usando analisa a sessao e destila novas skills automaticamente. Com RL habilitado, um modelo juiz dedicado extrai skills de episodios que falharam.

### **Sem necessidade de cluster GPU**
No modo `skills_only`, apenas uma conexao de rede e necessaria. O treinamento RL e delegado a um backend compativel com Tinker.

### **Dois modos de aprendizado**
O MetaClaw suporta ambos:
- **RL (GRPO)** para aprender a partir de sinais de feedback implicitos
- **Destilacao On-Policy (OPD)** para destilar um modelo professor maior para o aluno on-policy

No modo OPD, o modelo aluno gera respostas normalmente, e um modelo professor fornece log-probabilidades por token nas mesmas respostas. As logprobs do professor sao passadas para a funcao de perda (ex.: `cispo`) para que o aluno aprenda a distribuicao do professor. O professor deve estar servido atras de um endpoint `/v1/completions` compativel com OpenAI (ex.: vLLM, SGLang).

### **Assincrono por design**
Servico, modelagem de recompensa e treinamento sao totalmente desacoplados. O agente continua respondendo enquanto a pontuacao e a otimizacao ocorrem em paralelo.

---

## 🚀 Inicio Rapido

### 1. Instalacao

```bash
pip install -e .                        # modo skills_only (leve)
pip install -e ".[rl]"                  # + suporte a treinamento RL (torch, transformers, tinker)
pip install -e ".[evolve]"              # + evolucao de skills via LLM compativel com OpenAI
pip install -e ".[scheduler]"           # + integracao com Google Calendar para agendador
pip install -e ".[rl,evolve,scheduler]" # recomendado para configuracao completa RL + agendador
```

Se voce deseja usar `rl.backend=mint`, instale o pacote de compatibilidade MinT separadamente no mesmo ambiente, por exemplo [`mindlab-toolkit`](https://github.com/MindLab-Research/mindlab-toolkit). O MetaClaw mantem essa dependencia fora do pacote padrao para que usuarios de RL possam escolher explicitamente entre Tinker ou MinT.

### 2. Configuracao

```bash
metaclaw setup
```

O assistente interativo ira solicitar a escolha do provedor LLM (Kimi, Qwen, MiniMax ou personalizado), sua chave de API e, opcionalmente, a habilitacao do treinamento RL.

O caminho de RL do MetaClaw pode alternar explicitamente entre `tinker` e `mint`. O valor padrao recomendado e `auto`, que ainda consegue inferir o MinT a partir de credenciais ou base URLs no estilo Mint quando o pacote MinT esta instalado.

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
```

Os aliases legados `rl.tinker_api_key` e `rl.tinker_base_url` continuam sendo aceitos para compatibilidade retroativa.

### 3. Iniciar

```bash
metaclaw start
```

So isso. O MetaClaw inicia o proxy, configura automaticamente o OpenClaw e reinicia o gateway. Abra o OpenClaw e comece a conversar. Skills sao injetadas a cada turno, e a sessao e automaticamente resumida em novas skills quando voce termina.

---

## 🛠️ Comandos CLI

```
metaclaw setup                  # Assistente interativo de configuracao inicial
metaclaw start                  # Iniciar MetaClaw (padrao: modo madmax)
metaclaw start --mode rl        # Forcar modo RL (sem agendador) nesta sessao
metaclaw start --mode skills_only  # Forcar modo apenas Skills nesta sessao
metaclaw stop                   # Parar uma instancia MetaClaw em execucao
metaclaw status                 # Verificar saude do proxy, modo de execucao e estado do agendador
metaclaw config show            # Visualizar configuracao atual
metaclaw config KEY VALUE       # Definir um valor de configuracao
```

**Chaves de configuracao comuns:**

```bash
metaclaw config rl.enabled true           # Habilitar treinamento RL
metaclaw config rl.backend auto           # auto | tinker | mint
metaclaw config rl.api_key sk-...         # Definir chave do backend RL
metaclaw config rl.base_url https://mint.macaron.xin/  # Endpoint opcional do backend, ex.: MinT
metaclaw config skills.auto_evolve false  # Desabilitar resumo automatico de skills
metaclaw config proxy.port 31000          # Alterar porta do proxy
```

---

## ⚙️ Configuracao

O arquivo de configuracao fica em `~/.metaclaw/config.yaml`, criado por `metaclaw setup`.

```yaml
mode: madmax               # "madmax" | "rl" | "skills_only"

llm:
  provider: kimi            # kimi | qwen | openai | minimax | custom
  model_id: moonshotai/Kimi-K2.5
  api_base: https://api.moonshot.cn/v1
  api_key: sk-...

proxy:
  port: 30000
  api_key: ""              # opcional: bearer token para o proxy local do MetaClaw

skills:
  enabled: true
  dir: ~/.metaclaw/skills   # diretorio da sua biblioteca de skills
  retrieval_mode: template  # template | embedding
  top_k: 6
  task_specific_top_k: 10   # limite de skills especificas por tarefa (padrao 10)
  auto_evolve: true         # resumir skills automaticamente apos cada sessao

rl:
  enabled: false            # defina como true para habilitar treinamento RL
  backend: auto             # "auto" | "tinker" | "mint"
  model: moonshotai/Kimi-K2.5
  api_key: ""
  base_url: ""              # endpoint opcional do backend, ex.: https://mint.macaron.xin/ para MinT
  tinker_api_key: ""        # alias legado para api_key
  tinker_base_url: ""       # alias legado para base_url
  prm_url: https://api.openai.com/v1
  prm_model: gpt-5.2
  prm_api_key: ""
  lora_rank: 32
  batch_size: 4
  resume_from_ckpt: ""      # opcional: caminho do checkpoint para retomar treinamento
  evolver_api_base: ""      # deixe vazio para reutilizar llm.api_base
  evolver_api_key: ""
  evolver_model: gpt-5.2

opd:
  enabled: false            # defina como true para habilitar OPD (destilacao do professor)
  teacher_url: ""           # URL base do modelo professor (OpenAI compativel /v1/completions)
  teacher_model: ""         # nome do modelo professor (ex.: Qwen/Qwen3-32B)
  teacher_api_key: ""       # chave de API do modelo professor
  kl_penalty_coef: 1.0      # coeficiente de penalidade KL para OPD

max_context_tokens: 20000   # limite de tokens do prompt antes de truncamento

scheduler:                  # v0.3: agendador de meta-aprendizado (habilitado automaticamente no modo madmax)
  enabled: false            # modo madmax habilita automaticamente; defina manualmente para modo rl
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

Skills sao instrucoes curtas em Markdown injetadas no system prompt do agente a cada turno. Elas ficam no diretorio de skills (`~/.metaclaw/skills/` por padrao), organizadas como arquivos `SKILL.md` individuais.

**O resumo automatico de skills** e executado apos cada conversa. O LLM configurado analisa o que aconteceu e gera novas skills automaticamente. Nenhuma curadoria manual e necessaria. A biblioteca cresce com o uso.

Para pre-carregar o banco de skills integrado (mais de 40 skills em codificacao, seguranca, tarefas de agente, etc.):

```bash
cp -r memory_data/skills/* ~/.metaclaw/skills/
```

---

## 🔬 Avancado: Modo RL

Habilite o treinamento RL para ajustar continuamente o modelo a partir de conversas ao vivo, usando Tinker ou MinT:

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

No modo RL:
- Cada turno de conversa e tokenizado e submetido como amostra de treinamento
- Um LLM juiz (PRM) pontua respostas de forma assincrona
- Um backend compativel com Tinker, como Tinker cloud ou MinT, executa fine-tuning LoRA; pesos atualizados sao trocados a quente a cada `batch_size` amostras
- Um LLM evoluidor dedicado extrai novas skills de episodios que falharam

Se voce prefere o Tinker cloud, altere `rl.backend` para `tinker` ou mantenha em `auto` e omita o endpoint MinT.

**Rollout programatico** (sem necessidade de TUI OpenClaw): defina `openclaw_env_data_dir` para um diretorio de arquivos JSONL de tarefas:

```json
{"task_id": "task_1", "instruction": "Register the webhook at https://example.com/hook"}
```

---

## 🔬 Avancado: Modo OPD

A Destilacao On-Policy (OPD) permite destilar um modelo professor maior para o aluno enquanto ele treina on-policy. O aluno gera respostas normalmente; o professor fornece log-probabilidades por token nas mesmas respostas. Uma penalidade KL direciona o aluno para a distribuicao do professor.

```bash
metaclaw config opd.enabled true
metaclaw config opd.teacher_url http://localhost:8082/v1
metaclaw config opd.teacher_model Qwen/Qwen3-32B
metaclaw config opd.kl_penalty_coef 1.0
metaclaw start --mode rl
```

O professor deve estar servido atras de um endpoint `/v1/completions` compativel com OpenAI (ex.: vLLM, SGLang). OPD pode ser combinado com pontuacao PRM, ambos executam de forma assincrona.

Consulte `examples/run_conversation_opd.py` para um exemplo programatico e `scripts/run_openclaw_tinker_opd.sh` para um script de inicializacao pronto para uso.

---

## 🧠 Avancado: Agendador de Meta-Aprendizado (v0.3)

No modo RL, a etapa de troca a quente de pesos pausa o agente por varios minutos. O agendador (habilitado por padrao no modo `madmax`) adia atualizacoes RL para janelas de inatividade do usuario, garantindo que o agente nunca seja interrompido durante o uso ativo.

```bash
metaclaw config scheduler.sleep_start "23:00"
metaclaw config scheduler.sleep_end   "07:00"
metaclaw config scheduler.idle_threshold_minutes 30

# Opcional: integracao com Google Calendar
pip install -e ".[scheduler]"
metaclaw config scheduler.calendar.enabled true
metaclaw config scheduler.calendar.credentials_path ~/.metaclaw/client_secrets.json
```

Tres condicoes acionam uma janela de atualizacao (qualquer uma e suficiente): horarios de sono configurados, inatividade do teclado do sistema ou um evento ativo no Google Calendar. Se o usuario retornar durante uma atualizacao, o batch parcial e salvo e retomado na proxima janela.

Cada `ConversationSample` e marcado com uma versao `skill_generation`. Quando a evolucao de skills incrementa a geracao, o buffer RL e esvaziado para que apenas amostras pos-evolucao sejam usadas nas atualizacoes de gradiente (separacao de conjuntos support/query MAML).

---

## 📚 Citacao

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

## 🙏 Agradecimentos

O MetaClaw e construido sobre os seguintes projetos de codigo aberto:

- [OpenClaw](https://openclaw.ai), o framework de agente principal.
- [SkillRL](https://github.com/aiming-lab/SkillRL), nosso framework de RL aprimorado com skills.
- [Tinker](https://www.thinkingmachines.ai/tinker/), usado para treinamento RL online.
- [MinT](https://github.com/MindLab-Research/mindlab-toolkit), backend alternativo para treinamento RL online.
- [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL), inspiracao para nosso design de RL.
- [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills), fornece a base para nosso banco de skills.

---

## 📄 Licenca

Este projeto e licenciado sob a [Licenca MIT](LICENSE).
