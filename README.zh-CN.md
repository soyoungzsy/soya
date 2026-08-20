<div align="center">

# 🐳 SOYA Personal Board · SOYA 个人董事会

### 你的私人董事会——让古今 12 位智者，随叫随到地帮你做决策、开晨会、沉淀人生。

**一个把"自我管理"做成 AI 技能体系的开源项目，适配 DeepSeek Harness 与一切支持 Skills 的 Agent。**

[English](README.md) · [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) · [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)

![license](https://img.shields.io/badge/license-MIT-green)
![dsh-plugin](https://img.shields.io/badge/DSH-plugin-blue)
![platform](https://img.shields.io/badge/platform-DeepSeek%20Harness%20%7C%20Claude%20Code%20%7C%20any%20Skills--agent-lightgrey)

</div>

---

## ✨ 这是什么？

大多数 AI 助手只会"回答问题"。**SOYA 帮你运行人生的操作系统。**

它是一个**自我管理体系**，以三种形态交付：

1. **DeepSeek Harness 的 Agent 预设**：一条命令装好一个"人格固定 + 内置三项技能"的 AI 助手。
2. **三个可移植技能**：Claude Code、Codex 以及任何支持 `SKILL.md` 的 Agent 都能用。
3. **一套可复用的方法论**：决策模板、晨会模板、卡片模板，全部开源。

核心理念古老而简单：**面临抉择时，你愿意只听自己的一个声音，还是听历史上 12 位智者一起发言？**

> 💡 **运作方式**：董事会给建议，**决定权永远在你**。这是思考放大器，不是决策替代品。

---

## 🧩 三大引擎

| | 🌅 每日晨会 | 👥 董事会咨询 | 🗂️ 卡片仓 |
|---|---|---|---|
| **技能** | `soya-morning-meeting` | `personal-board` | `soya-card-vault` |
| **时机** | 每天早晨 | 重大决策 | 任何有收获的时刻 |
| **做什么** | 基于**真实**近期材料 → 提炼 1-3 个核心问题 → 3-5 位董事各给"一个判断 + 一个行动" → 一句安顿心神的话收尾 | 5 步法：明确问题 → 选 3-5 位成员 → 分别请教 → 找共识/分歧/盲点 → **你做决定** | 把经验沉淀成小而精、可复用、可检索的 Markdown 卡片，归档进你的本地知识库 |
| **产出** | 可执行的今天：做什么、少做什么、怎么算完成 | 一份决策备忘录 | 未来的你真能用上的卡片 |

**设计原则**：事实先于观点 · 建议少而硬（1-3 条）· 本地优先（数据留在你的知识库）· 隐私默认（敏感职场信息自动中性化）· 读不到的材料绝不编造。

---

## 🚀 快速开始

### DeepSeek Harness 用户（推荐）

> 需要先安装 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（开源 Agent 框架，万物皆可插件）。

```bash
# 1. 把预设复制到本地预设目录
mkdir -p ~/.dsh/.agent-presets/soya-personal-board
cp -R agent-preset/* ~/.dsh/.agent-presets/soya-personal-board/

# 2. 重启 DSH，在预设选择器里选「SOYA 个人董事会」
# 3. 告诉你的 SOYA 助手你的知识库位置：
#    "我的知识库根目录是：/path/to/your/vault"
# 4. 开始："来开晨会。" 或 "帮我用个人董事会分析：<你的问题>"
```

### Claude Code / 其他支持 Skills 的 Agent

```bash
git clone https://github.com/soyoungzsy/soya.git
cp -R skills/personal-board ~/.claude/skills/
cp -R skills/soya-morning-meeting ~/.claude/skills/
cp -R skills/soya-card-vault ~/.claude/skills/
```

### 决策模板命令行

```bash
python3 skills/personal-board/scripts/decision_template.py "我是否应该换工作？"
python3 skills/personal-board/scripts/decision_template.py "我是否应该换工作？" 职业选择
python3 skills/personal-board/scripts/decision_template.py --list
```

---

## 🖼️ 演示

> _截图与 GIF 制作中，欢迎 PR！_

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

## 📦 仓库结构

```
soya/
├── agent-preset/               # DeepSeek Harness 预设（复制即用）
│   ├── preset.yml              #   显示元数据
│   ├── agent.cordis.yml        #   插件组成（fork 自 standard 预设）
│   └── skills/                 #   内嵌技能
├── skills/                     # 可移植技能包（任何支持 Skills 的 Agent）
│   ├── personal-board/         #   董事会咨询 + 成员档案
│   ├── soya-morning-meeting/   #   每日晨会
│   └── soya-card-vault/        #   知识卡片仓
├── templates/                  # 即用 Markdown 模板
│   └── member-card.md          #   空白成员卡（添加你自己的成员用）
├── docs/
│   ├── board-design.md         # 为什么是这 12 人——完整选人逻辑
│   ├── customize-your-board.md # 如何选人、换人、组建自己的董事会
│   └── philosophy.md           # 为什么这套体系有效
└── LICENSE                     # MIT
```

---

## 🧠 12 位董事会成员

| 成员 | 角色 | 适合咨询 |
|------|------|---------|
| 曾国藩 | 首席心性官 | 韧性、自律、逆境 |
| 查理·芒格 | 首席理性官 | 决策、风险、避免愚蠢 |
| 埃隆·马斯克 | 首席创新官 | 第一性原理、执行 |
| 凯文·凯利 | 首席趋势官 | 长期视野、职业规划 |
| 苏轼 | 首席生活官 | 情绪、平衡、豁达 |
| 达·芬奇 | 首席好奇心官 | 创意、跨界学习 |
| 杨绛 | 首席精神导师 | 内心宁静、写作、成长 |
| 波伏娃 | 首席自由官 | 独立、自我实现 |
| 张小龙 | 首席产品官 | 产品品味、用户洞察 |
| 俞军 | 首席策略官 | 数据决策、增长 |
| 彼得·德鲁克 | 首席组织有效性官 | 管理、贡献、向上管理 |
| 克里斯·沃斯 | 首席谈判沟通官 | 关键对话、对齐 |

_完整档案见 [`skills/personal-board/references/member_profiles.md`](skills/personal-board/references/member_profiles.md)。_

### 🤔 为什么是这 12 人？——不是名人名单，是思维工具库

每位成员都通过了同样的**入选四问**：① 思想经得起时间检验（苏轼被验证 900 年，曾国藩 150 年——没有流量红人）② 覆盖一个无可替代的人生维度 ③ 思想能"编译"成可执行原则（"下次遇到 X 就做 Y"）④ 彼此互补到能互怼——**董事会里必须有反对派**。

12 人覆盖六大人生维度：**怎么想**（芒格、俞军）· **怎么做**（马斯克、达·芬奇）· **怎么扛**（曾国藩、苏轼、杨绛）· **怎么走**（凯文·凯利）· **怎么活**（波伏娃）· **怎么说**（沃斯、德鲁克）。

> 📖 [**board-design.md**](docs/board-design.md) —— 完整选人逻辑、逐个入选理由，以及"为什么没有当代红人"的诚实回答。

### 🎨 组建你自己的董事会——它是你的，不是我们的

默认 12 人只是**起点模板**，不是固定名单：

- **每次选 3-5 人**：定位议题（哪一维）→ 匹配思维方式 → 核心阵容 + 一名"反对派"
- **加人**：用"入选四问"把关，用空白[成员卡](templates/member-card.md)建档
- **换人**：成员思想已内化、或人生阶段变了再换——不是因为腻了
- **精简**：总数建议 8-12 人；人多不等于建议好

> 📖 [**customize-your-board.md**](docs/customize-your-board.md) —— 三步选人法、场景阵容速查表（绩效沟通/创业/低谷/管理……）、四个必踩的坑。

---

## 🗺️ 路线图

- [x] 董事会咨询技能
- [x] 每日晨会技能
- [x] 卡片仓技能
- [x] DSH Agent 预设
- [x] 选人逻辑与定制指南
- [ ] 演示 GIF
- [ ] 英文成员档案
- [ ] 自动化方案（定时晨会）
- [ ] 多语言晨会（日/英）

---

## 🤝 贡献

任何想法、新成员、模板、翻译和 bug 报告都欢迎——开 Issue 或 PR 即可。

**重要**：本项目奉行**隐私优先**。请勿提交真实个人或职场数据；分享示例时，请使用本仓库统一的中性占位表述。

## 📄 许可证

[MIT](LICENSE) © SOYA

---

<div align="center"><sub>Made with 🐳 by SOYA · 万物皆可插件，人生皆可治理</sub></div>
