<div align="center">

# 🐳 SOYA Personal Board

### Your private board of directors — great minds from history, on call for your decisions, your mornings, and your growth.

**让曾国藩、芒格、马斯克等 12 位智者，成为你的私人董事会。** · **A self-management system for DeepSeek Harness (DSH) & any Skills-capable agent.**

[中文版说明](README.zh-CN.md) · [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) · [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)

![license](https://img.shields.io/badge/license-MIT-green)
![dsh-plugin](https://img.shields.io/badge/DSH-plugin-blue)
![platform](https://img.shields.io/badge/platform-DeepSeek%20Harness%20%7C%20Claude%20Code%20%7C%20any%20Skills--agent-lightgrey)

</div>

---

## ✨ What is SOYA Personal Board?

Most AI assistants answer questions. **SOYA runs your life's operating system.**

It is a **self-management framework** packaged as:

1. **An agent preset for DeepSeek Harness** — spin up an AI assistant with a fixed "persona" and three built-in skills, one command away.
2. **Three portable skills** — work with Claude Code, Codex, or any agent that supports `SKILL.md`.

The idea is simple and ancient: **when you face a decision, would you rather hear one voice — your own — or twelve of the wisest minds in history?**

- **曾国藩 (Zeng Guofan)** for perseverance & self-discipline
- **查理·芒格 (Charlie Munger)** for inverse thinking & rational decisions
- **埃隆·马斯克 (Elon Musk)** for first-principles & bold execution
- **凯文·凯利 (Kevin Kelly)** for long-term vision
- **苏轼 (Su Shi)** for equanimity in stormy times
- …and 7 more, from Leonardo da Vinci to Simone de Beauvoir, Zhang Xiaolong, Peter Drucker & Chris Voss.

> 💡 **How it works**: the board advises, **you decide**. This is a thinking amplifier, not a decision replacer.

---

## 🧩 The System — Three Engines

| | 🌅 Morning Meeting | 👥 Board Consultation | 🗂️ Card Vault |
|---|---|---|---|
| **Skill** | `soya-morning-meeting` | `personal-board` | `soya-card-vault` |
| **When** | Every morning | Major decisions | Anytime you learned something |
| **What it does** | Grounds in your *real* recent material → surfaces 1-3 core issues → 3-5 board members give one judgment + one action each → closes with one calming sentence | Runs the 5-step process: clarify → pick 3-5 members → consult → find consensus/divergence/blind spots → **you** decide | Distills experience into small, reusable, searchable Markdown cards, filed into your local knowledge base |
| **Output** | Executable: *do this, skip that, done when* | A decision memo | Cards that future-you can actually use |

**Design principles:** facts before opinions · advice is few & hard (1-3 actions) · local-first (your data stays in your vault) · privacy by default (sensitive workplace details are automatically neutralized) · never fabricate what wasn't read.

---

## 🚀 Quick Start

### For DeepSeek Harness (recommended)

> Requires [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH), an open-source agent harness where *everything is a plugin*.

```bash
# 1. Copy the preset into your local presets directory
mkdir -p ~/.dsh/.agent-presets/soya-personal-board
cp -R agent-preset/* ~/.dsh/.agent-presets/soya-personal-board/

# 2. Restart DSH, then pick "SOYA 个人董事会" from the preset picker
# 3. Tell your SOYA assistant where your knowledge base lives:
#    "我的知识库根目录是：/path/to/your/vault"
# 4. Start: "来开晨会。"  or  "帮我用个人董事会分析：<你的问题>"
```

### For Claude Code / any Skills-capable agent

```bash
git clone https://github.com/soyoungzsy/soya.git
cp -R skills/personal-board ~/.claude/skills/
cp -R skills/soya-morning-meeting ~/.claude/skills/
cp -R skills/soya-card-vault ~/.claude/skills/
```

### The decision template CLI

```bash
python3 skills/personal-board/scripts/decision_template.py "我是否应该换工作？"
python3 skills/personal-board/scripts/decision_template.py "我是否应该换工作？" 职业选择
python3 skills/personal-board/scripts/decision_template.py --list
```

---

## 🖼️ Demo

> _Screenshots & GIFs coming soon — PRs welcome!_

```
┌─────────────────────────────────────────────────────────┐
│  🌅 个人董事会日会 · 2026-08-20                          │
│                                                         │
│  事实简报                                                │
│  • 昨天完成项目 A 的里程碑验收，客户反馈正面              │
│  • 本周三有季度绩效沟通，材料尚未准备                    │
│  • 连续 3 天 12 点后入睡                                 │
│                                                         │
│  核心问题                                                │
│  1. 绩效沟通如何呈现真实贡献？                           │
│  2. 睡眠与工作节奏失衡                                   │
│                                                         │
│  董事发言                                                │
│  • 德鲁克: 先定义"贡献"，再谈"表现"→ 今晚列出 3 条成果   │
│  • 沃斯: 用"校准问题"引导对话 → 准备 2 个反问            │
│  • 曾国藩: 耐烦 → 今天就睡，明天 6 点起                  │
│                                                         │
│  今日行动：① 写 3 条贡献清单 ② 准备 2 个反问 ③ 23:30 睡  │
│  一句话安顿心神：世界是自己的，与他人毫无关系。           │
└─────────────────────────────────────────────────────────┘
```

---

## 📦 Repository Layout

```
soya/
├── agent-preset/               # DeepSeek Harness preset (copy & go)
│   ├── preset.yml              #   display metadata
│   ├── agent.cordis.yml        #   composition (forked from standard)
│   └── skills/                 #   embedded skills
├── skills/                     # portable skills (any Skills-capable agent)
│   ├── personal-board/         #   board consultation + member profiles
│   ├── soya-morning-meeting/   #   daily morning meeting
│   └── soya-card-vault/        #   knowledge card vault
├── templates/                  # ready-to-use Markdown templates
│   └── member-card.md          #   blank card for adding YOUR members
├── docs/
│   ├── board-design.md         # why these 12 — full selection logic
│   ├── customize-your-board.md # how to pick, swap & build your own board
│   └── philosophy.md           # why this works
└── LICENSE                     # MIT
```

---

## 🧠 The 12 Board Members

| Member | Role | Ask about |
|--------|------|-----------|
| 曾国藩 Zeng Guofan | Chief of Mindset | resilience, self-discipline, adversity |
| 查理·芒格 Charlie Munger | Chief of Rationality | decisions, risk, avoiding stupidity |
| 埃隆·马斯克 Elon Musk | Chief of Innovation | first principles, execution |
| 凯文·凯利 Kevin Kelly | Chief of Trends | long-term vision, career |
| 苏轼 Su Shi | Chief of Life | emotions, balance, equanimity |
| 达·芬奇 Leonardo da Vinci | Chief of Curiosity | creativity, cross-domain learning |
| 杨绛 Yang Jiang | Chief of Spirit | inner peace, writing, growth |
| 波伏娃 Simone de Beauvoir | Chief of Freedom | independence, self-realization |
| 张小龙 Zhang Xiaolong | Chief of Product | product taste, user insight |
| 俞军 Yu Jun | Chief of Strategy | data-driven decisions, growth |
| 彼得·德鲁克 Peter Drucker | Chief of Effectiveness | management, contribution, upward mgmt |
| 克里斯·沃斯 Chris Voss | Chief of Negotiation | hard conversations, alignment |

_Full profiles in [`skills/personal-board/references/member_profiles.md`](skills/personal-board/references/member_profiles.md)._

### 🤔 Why these 12? — not a celebrity list, a thinking toolkit

Every member passed the same **four admission questions**: ① ideas tested by time (Su Shi: 900 years; Zeng Guofan: 150 — no trending influencers) ② covers one irreplaceable dimension of life ③ thinking that compiles into executable principles ("next time X happens, do Y") ④ complementary enough to argue with each other — **every board needs an opposition**.

The 12 span six life dimensions: **decide** (Munger, Yu Jun) · **do** (Musk, da Vinci) · **endure** (Zeng, Su Shi, Yang Jiang) · **direction** (Kevin Kelly) · **freedom** (de Beauvoir) · **communicate** (Voss, Drucker).

> 📖 [**board-design.md**](docs/board-design.md) — the full selection logic, member-by-member reasoning, and why there are no "trending influencers" on the board.

### 🎨 Build your own board — it's yours, not ours

The default 12 are a **starting template**, not a fixed roster:

- **Pick 3-5 per session**: locate your issue on a dimension → match the needed mindset → core lineup + one "devil's advocate"
- **Add**: pass a new person through the four admission questions, file them with the blank [member card](templates/member-card.md)
- **Swap**: only when you've truly internalized a member's thinking, or your life stage changed — not because you're bored
- **Trim**: fewer than 15 members total; more voices ≠ better advice

> 📖 [**customize-your-board.md**](docs/customize-your-board.md) — 3-step selection, scenario lineups (performance review, career change, burnout, management…), and the four traps to avoid.

---

## 🗺️ Roadmap

- [x] Board consultation skill
- [x] Morning meeting skill
- [x] Card vault skill
- [x] DSH agent preset
- [x] Selection logic & customization guide
- [ ] Interactive demo GIFs
- [ ] English member profiles
- [ ] Automation recipe (cron-driven daily meeting)
- [ ] Multi-language (JA/EN) board sessions

---

## 🤝 Contributing

Ideas, member additions, templates, translations and bug reports are all welcome — open an issue or a PR.

**Important**: this project is built on a **privacy-first** philosophy. Never commit real personal or workplace data; when sharing examples, use the neutral placeholders used throughout this repo.

## 📄 License

[MIT](LICENSE) © SOYA

---

<div align="center"><sub>Made with 🐳 by SOYA · 万物皆可插件，人生皆可治理</sub></div>
