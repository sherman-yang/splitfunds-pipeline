# 指令手册：生成带日期的加拿大 Split Funds 深度投资研报

**目标读者：** AI Agent (任何具备网页抓取、计算和文本生成能力的 Agent 都应能依此手册产出合格报告)  
**任务目标：** 生成一份以当天日期命名的《加拿大 Split Funds 深度投资研报》，覆盖加拿大市场全部可发现的 Split Funds（含最新上市标的）以及全部可发现的 Split Funds ETF。报告必须**仅基于当日从官方来源抓取的可核验数据**，不得凭记忆、训练数据或任何缓存内容推断任何数值。

输出文件命名：

```text
Split-Funds-Report-YYYY-MM-DD.md
```

本手册是独立 SOP。Agent 不需要、也不应该依赖任何已有的历史报告作为数据来源。所有 ticker、到期日、收益率、NAV、市价、评级、分红、税务信息**必须由 Agent 在生成当日从官方来源现场核验**。

---

## 0. 成功标准：什么才算合格报告

任何 AI Agent 使用本手册生成的报告，必须达到以下最低标准，否则视为未完成：

1. **详细程度必须达到机构级研报水准。** 报告不能只是几页摘要；必须包含：
  - 按发行商分类的逐只产品数据卡（每只字段达到第 3 节定义的 Tier 1 全部 + Tier 2 ≥70% + ≥3 段定性分析）
  - Preferred 全市场汇总表（一行一个 series）
  - Class A 全市场汇总表（一行一个 ticker）
  - Split Funds ETF 独立章节（每只独立数据卡 + 独立分析）
  - Class A 投资策略章节（≥3 种**操作上彼此独立**的策略，每种带步骤表 + "其他策略不适用时为何选这一种"的判断标准）
  - Preferred 投资策略章节（同上，≥3 种独立策略）
  - 高级配置策略章节（哑铃 / 60-40 / 抗通胀等）
  - 当前环境下的买入思路（具体到 ticker 级筛选）
  - 风险红线与数据缺口清单
2. **覆盖范围必须先审计再分析。** 必须先建立 universe audit，说明发现了多少 Split Funds、Preferred series、Class A/Capital Share ticker、Split Funds ETF，以及哪些标的已终止、改名、延期或无法核验。
3. **每个产品必须有完整证据链。** 每只 Split Fund、每只 ETF、每个 Preferred series 和每个 Class A ticker 都要能追溯到官网、TMX/TSX、SEDAR+、DBRS/Morningstar DBRS、Morningstar Canada 或其他明确来源。
4. **数据时效性分级核验。** 字段按时效性分两类：
   - **当前状态字段**（NAV、市价、bid/ask、当前分红、最新评级、当前 Prime Rate）必须当日核验
   - **结构性 / 历史字段**（成立日、招股条款、面值、停派阈值、历史总收益、T3 税务构成）必须给出"来源 + 时间区间 + 数据完整性等级"三件套，不要求当日
   未达上述任一标准的字段必须标注"未在官方来源核验到"。**严禁使用训练数据或缓存填充**。
5. **必须产生可操作结论。** 结论必须包含短期、中期、长期观点，说明 Preferred、Class A、ETF 哪类更占优，并给出机会、风险、回避名单和长期总收益策略。结论必须**具体到 ticker 级**，不允许仅停留在"金融板块"这种粗粒度。
6. **必须明确不确定性。** 如果历史分红、税务构成、total return、停派阈值或 NAV 无法核验，必须把不确定性写进产品卡和汇总表，不能用模糊语言掩盖。
7. **使用 GFM 视觉元素标注真正的关键点。** 在风险、税务陷阱、可疑数据、操作要点等地方使用 `[!NOTE]` `[!IMPORTANT]` `[!WARNING]` `[!TIP]` `[!CAUTION]`，**不强制每类至少一次**——为凑数量插入空洞 alert 反而降低可读性。
8. **任务原子化，优先 Sub-Agent 委派。**
   - **首选路径**：按第 0.2.7 节 Pattern A，把每只产品/ETF 作为原子单元委派给 sub-agent。Parent 上下文只增长 ~1 行/单元，单轮即可完成 50+ 标的全市场覆盖。
   - **次选路径**：Agent 不支持 sub-agent 时，按 Pattern B 多轮会话续接——本轮做能做的，写盘 + 收尾仪式 + 提示用户下一轮。
   - **严禁的路径**：对所有产品都"半半拉拉"地填字段来掩盖覆盖不足；用训练数据补未核验字段；隐藏未完成状态；任何形式的"提前退出 + 部分覆盖"作为合法终态。

9. **最大努力原则（Best Effort Principle）。** Agent 必须为每只产品、每个字段付出**最大努力**核验，**质量和准确性永远优先于速度和效率**。具体要求：

   - **每个 Tier 1 字段** 至少尝试 ≥3 个来源（官网主页 → 子页/factsheet → SEDAR+ / 最新公告 / WebSearch）；全部失败才允许标"未在官方来源核验到"。
   - **每个 Tier 2 字段** 至少尝试 ≥2 个来源。
   - **遇到失败先升级再放弃**: WebFetch 摘要器没找到 → 重新用更具体 prompt 重试 → WebSearch 跨站点核验 → browser MCP（如可用）抓 JS 渲染内容 → 仍无才标"未核验到"。
   - **覆盖范围必须穷尽**: Universe 中**每只 confirmed_active 产品**都必须尝试核验，**不允许**"只抓容易拿到数据的产品，跳过 SEDAR+ PDF / JS 渲染页 / 流动性差的标的"。
   - **不允许"提前满足"心态**: "Tier 2 已 70% 达标可以收工"、"8 只就够代表"、"反正剩下的可以下一轮"——这些都是**报告失败模式**。Agent 应在能力允许范围内**抓取尽可能多的产品 + 尽可能完整的字段**，不能完成的部分才用多轮续接。
   - **使用所有可用工具和时间预算**: Agent 不应为了"快"而跳过任何核验步骤。报告的价值来自准确性，不是生成速度。

10. **报告完成后必须清理临时文件。** Phase 5 完成后，Agent 必须执行第 0.2.2 节 Phase 6（清理）——默认归档 `.splitfunds-workspace/`，或按用户指示删除/保留。**不允许**任务结束后留下未清理的工作目录。

---

## 0.1 执行顺序：Agent 必须按这个顺序工作

**严禁从写报告开始。** 必须先完成数据工作底稿，再写最终报告。

1. **确定报告日期和文件名。** 使用当天日期生成 `Split-Funds-Report-YYYY-MM-DD.md`。
2. **建立 seed universe。** 从第 2 节发行商清单出发，结合 TSX/TMX 搜索、SEDAR+ 检索和发行商新闻稿，建立候选清单。
3. **逐只官网核验。** 对每个候选产品访问发行商官网，记录产品页、factsheet、NAV、分红、税务、公告和招股文件链接。**链接结构经常变化，必须以当日实际可访问 URL 为准**，不要使用任何缓存或记忆中的链接。
4. **交易数据核验。** 用 TSX/TMX、Yahoo Finance Canada、Google Finance 或其他可核验交易来源记录 latest price、bid/ask、volume 和抓取时间。
5. **宏观数据核验。** 查询 Bank of Canada、主要商业银行 Prime Rate、加拿大国债收益率曲线、CAD/USD 和关键板块环境。**Prime Rate 必须以 BoC 政策利率最近一次变动后的市场实际 Prime Rate 为准**，不要直接使用 BoC overnight rate。
6. **计算指标。** 计算 Class A NAV、折溢价、NAV 安全边际、隐含杠杆、Preferred current yield、YTM/YTW、资产覆盖率。
7. **标注数据完整性。** 对历史总收益、税务构成、分红记录、停派阈值和评级分别标注 High / Medium / Low。
8. **生成报告正文。** 严格使用第 7 节报告骨架和第 7.19 节产品卡模板。
9. **执行最终质量检查。** 使用第 8 节 checklist。若任何关键项失败，必须在报告中说明失败项和影响。
10. **清理临时文件。** 报告通过质量检查后,执行 Phase 6:询问用户偏好(归档/删除/保留),按指示清理 `.splitfunds-workspace/`。

---

## 0.2 长任务自主执行模型

任务被切分为 6 个文件化、可中断恢复的阶段（Phase 1-5 数据采集与报告生成，Phase 6 清理）。所有中间状态必须落盘到 `.splitfunds-workspace/`，绝不能只存在内存里。如果上下文窗口紧张，必须每完成一个阶段就写盘、更新 checkpoint，必要时由用户开新会话从检查点继续。

### 0.2.1 工作目录与文件布局

Agent 启动后必须在报告文件所在目录建立以下工作空间：

```text
<报告目录>/
├── .splitfunds-workspace/
│   ├── checkpoint.txt              # 当前阶段标识（PHASE-1-DONE ~ PHASE-3-PARTIAL ~ DONE）
│   ├── session_summary.md          # 多轮会话间的传递文档（详见 § 0.2.7）
│   ├── universe.json               # 阶段 1 输出：发现的全量 ticker 清单
│   ├── macro.json                  # 阶段 2 输出：宏观环境数据
│   ├── products/
│   │   └── <ticker>.json           # 阶段 3 输出：每只 Split Fund 的数据卡（一只一文件）
│   ├── etfs/
│   │   └── <ticker>.json           # 阶段 3 输出：每只 ETF 的数据卡（一只一文件）
│   ├── computed.json               # 阶段 4 输出：所有计算结果（YTM、折溢价等）
│   ├── errors.log                  # 失败记录与重试清单
│   └── sources.jsonl               # 所有抓取来源审计日志（每行一条）
└── Split-Funds-Report-YYYY-MM-DD.md  # 阶段 5 输出：最终报告
```

> [!IMPORTANT]
> **`.splitfunds-workspace/` 是中间状态。** Agent 完成阶段 5 后可以保留以便后续 review，但不应该 commit 到 git。请将该目录加入 `.gitignore`。

### 0.2.2 六阶段执行模型

任务被切分为 **6 个独立阶段**（Phase 1-5 数据与报告，Phase 6 清理）。每个阶段都有明确的输入、输出文件、成功判据。任何阶段失败时，Agent 应只重试该阶段，而不是整个任务。

#### Phase 1 — Universe Discovery（标的发现）

| 项目 | 内容 |
|---|---|
| **输入** | 第 2 节 seed universe + 发行商网站清单 |
| **动作** | 访问每个发行商官网、TSX/TMX 搜索、SEDAR+ 检索；记录所有发现的 ticker、状态、url |
| **输出** | `universe.json`（ticker → {issuer, security_type, status, url, source_urls[]}） |
| **成功判据** | seed universe 中的每个 ticker 都已查到当前状态；至少四只 seed ETF 都已确认 |
| **失败处理** | 若某发行商网站无法访问，记入 `errors.log`，下次重试时只重试该发行商 |
| **完成后写入** | `checkpoint.txt = "PHASE-1-DONE"` |

#### Phase 2 — Macro Snapshot（宏观快照）

| 项目 | 内容 |
|---|---|
| **输入** | 第 4.1 节宏观核验清单 |
| **动作** | 抓取 BoC 政策利率、Prime Rate、加拿大国债 2/5/10 年收益率、CAD/USD、关键板块指数 |
| **输出** | `macro.json` |
| **成功判据** | 全部宏观字段都有 as_of_date 和 source_url |
| **完成后写入** | `checkpoint.txt = "PHASE-2-DONE"` |

#### Phase 3 — Per-Product Data Collection（逐只数据采集）

| 项目 | 内容 |
|---|---|
| **输入** | `universe.json` |
| **执行模式** | **首选: Sub-Agent 委派**（每只产品一个 sub-agent，详见 § 0.2.7 Pattern A）。**回退: 多轮会话续接**（无 sub-agent 能力时）。 |
| **动作** | 对每只 Split Fund 和每只 ETF，访问官网/factsheet/NAV 页/分红公告/SEDAR+，按第 3 节字段分级要求填充 Tier 1 → Tier 2 → Tier 3 |
| **输出** | `products/<ticker>.json`（每个 ticker 一个文件；**抓完一只就立即写盘，禁止批量积攒在 context 里**） |
| **成功判据** | 每只标的 Tier 1 全部 + Tier 2 ≥70%；缺失字段用"未在官方来源核验到"标注并列出已查来源 |
| **失败处理** | 若某产品官网超时，跳过并记入 `errors.log`，进入下一只；最后批量重试 |
| **并行性** | Sub-agent 模式下，部分平台支持 parent 一次性 spawn 多个 sub-agent 并发执行；如不支持，sequential sub-agent 仍优于 parent 自己 fetch |
| **完成后写入** | `checkpoint.txt = "PHASE-3-DONE"` 仅当所有标的都至少处理过一次；部分完成时写 `PHASE-3-PARTIAL` |

> [!TIP]
> **增量恢复:** 进入阶段 3 前，Agent 应先扫描 `products/` 目录列出已完成的 ticker，只对缺失的产品 spawn sub-agent；这样可被中断 N 次后继续，每次都从断点续接。

> [!IMPORTANT]
> **强制持久化:** 即使在单会话内完成全部阶段，每只产品抓完也**必须**写入 `products/<ticker>.json`。Phase 5 写报告时**必须**回读 JSON，不能直接从 Phase 3 内存继续（即使 parent 看到 sub-agent 返回的状态也不行）。这是 Agent-agnostic 续接承诺的根基。

#### Phase 4 — Computation & Cross-Check（计算与交叉验证）

| 项目 | 内容 |
|---|---|
| **输入** | `products/*.json`、`etfs/*.json`、`macro.json` |
| **动作** | 计算 Class A NAV、折溢价、NAV 安全边际、隐含杠杆、Pfd YTM/YTW、资产覆盖率；交叉验证字段一致性；标注数据完整性 |
| **输出** | `computed.json` |
| **成功判据** | 所有公式可复算；冲突已在 `errors.log` 列出并标注采纳来源 |
| **完成后写入** | `checkpoint.txt = "PHASE-4-DONE"` |

#### Phase 5 — Report Generation（报告生成）

| 项目 | 内容 |
|---|---|
| **前置硬性条件** | `checkpoint.txt = "PHASE-4-DONE"`(即 Phase 1-4 全部完成);若仍是 `PHASE-3-PARTIAL` 则**严禁进入 Phase 5**——而是写 session_summary.md 让用户开下一轮 |
| **输入** | 全部 `products/*.json` + `etfs/*.json` + `macro.json` + `computed.json` |
| **动作** | 严格按第 7.22 节骨架生成 `Split-Funds-Report-YYYY-MM-DD.md`；产品卡使用第 7.19 模板，ETF 用第 7.20 模板。**必须通过文件读取 JSON,不能依赖 context 中的内存数据** |
| **输出** | 最终 Markdown 报告 |
| **成功判据** | 通过第 8 节质量检查清单全部条目 |
| **完成后写入** | `checkpoint.txt = "DONE"` |

#### Phase 6 — Cleanup（清理临时文件，必须执行）

| 项目 | 内容 |
|---|---|
| **前置条件** | `checkpoint.txt = "DONE"`，最终报告已通过 § 8 质量检查 |
| **动作** | 清理 `.splitfunds-workspace/`。**必须先询问用户偏好**（除非用户在启动时已显式指示），三种选项: <br>① **归档(默认推荐)**: `mv .splitfunds-workspace .splitfunds-workspace.archive-YYYY-MM-DD` — 非破坏性,保留审计追溯,后续可手动 `rm` <br>② **彻底删除**: `rm -rf .splitfunds-workspace` — 用户显式说"删除/clean/rm" 时执行 <br>③ **保留原状**: 用户说"keep" 或下次会有续接需要时,不动 |
| **输出** | workspace 已归档/删除/保留 + 向用户确认状态 |
| **重要原则** | **删除是不可逆的**——除非用户明确指示删除,默认采用归档(选项 ①)。Agent 不允许在没有用户确认的情况下执行 `rm -rf` |
| **完成后输出** | (1) 如选 ① 归档或 ② 删除: 在归档目录或新建一个根目录的 `.splitfunds-cleanup-receipt.txt` 中写入 `CLEANED YYYY-MM-DD action=archive\|delete` 作为最终标记; (2) 如选 ③ 保留: 把 `checkpoint.txt` 内容更新为 `CLEANED-KEPT`; (3) 向用户报告: "✅ 报告 `Split-Funds-Report-YYYY-MM-DD.md` 已生成。Workspace 已[归档到 X / 删除 / 保留]。" |

> [!CAUTION]
> Phase 6 删除选项是**破坏性操作**。Agent 必须在执行 `rm -rf` 前用对话方式获得用户明确确认("是的删除"、"yes delete"、"rm 它")，否则只允许执行归档(`mv`)或保留。归档可逆,删除不可逆。

### 0.2.3 恢复协议（Resume Protocol）

任何 Agent（包括与发起任务不同的 Agent）启动时，必须先执行以下恢复检查：

1. 检查 `<报告目录>/.splitfunds-workspace/checkpoint.txt` 是否存在。
2. 若不存在 → 从 Phase 1 开始。
3. 若存在 → 读取最后状态：
   - `PHASE-1-DONE` → 从 Phase 2 开始
   - `PHASE-2-DONE` → 从 Phase 3 开始（先扫描 `products/` 目录，列出已完成的 ticker，**只抓取缺失的**）
   - `PHASE-3-PARTIAL` → 同上（先读 `session_summary.md` 了解上轮进度），继续 Phase 3 直到全部完成
   - `PHASE-3-DONE` → 从 Phase 4 开始
   - `PHASE-4-DONE` → 从 Phase 5 开始
   - `DONE` → 报告已生成,但 Phase 6 清理可能未执行——检查 `.splitfunds-workspace/` 是否仍存在,若存在则进入 Phase 6 询问用户清理偏好
   - `CLEANED` → 任务完整结束;如用户要求重新生成,从 Phase 1 开始
4. **如果 `session_summary.md` 存在**，先读取它获取上一轮的"待完成清单"和优先级，按其中"下一轮启动指令"指引续接。
5. 检查 `errors.log` 中的失败项，先尝试重试再继续新工作。
6. 检查工作底稿的 `as_of_date`：如果距离当前时间已超过 24 小时，必须**重新抓取**所有市价、NAV 和宏观数据（不能复用昨天的盘面价格）。

> [!WARNING]
> **跨日陷阱：** 如果上次会话是昨天的，今天恢复时不能直接进入 Phase 5，必须返回 Phase 2 重新抓取宏观和价格数据。NAV 滞后 1-5 天是正常的，但市价必须是当日的。

### 0.2.4 失败、重试、放弃策略

| 情况 | 动作 |
|---|---|
| 单个 URL 超时 / 4xx / 5xx | 重试 ≤3 次；仍失败则记入 `errors.log` 并跳过该字段 |
| 整个发行商官网不可达 | 阶段 3 内跳过该发行商所有产品；阶段结束时尝试一次批量重试 |
| WebFetch 摘要器返回"未找到"但数据可能在页面 | 用更具体的字段名 + 数据格式 prompt 重试 ≤2 次（例："Find row labeled 'Distribution Threshold' in tables"）；仍无则**升级到 browser MCP**（见 0.2.4.1）；仍无则标"未在官方来源核验到" |
| 发行商主页只列产品名而无字段（常见） | 进入产品子页 `<base>/<ticker>-fund-features` 或 `<base>/product/<slug>/`；如失败则用 WebSearch 搜"<product name> NAV YYYY-MM"找最近发布的 distribution 公告 |
| 页面是 JS 渲染 / WebFetch 只看到 placeholder | **升级到 browser MCP**（见 0.2.4.1） |
| 字段在所有官方来源都查不到 | 在数据卡写"未在官方来源核验到"，列出已查的 ≥2 个来源 |
| 发现数据来源冲突 | 按第 2.4 节优先级裁决；在 `errors.log` 记录冲突来源 |
| Agent 上下文即将溢出 | 立即写盘当前已完成的产品 JSON + 更新 `checkpoint.txt = PHASE-N-PARTIAL` + 写 `session_summary.md`，请求用户开新会话从 checkpoint 续接（详见 § 0.2.7 多轮会话续接） |
| 关键宏观数据（如 Prime Rate）查不到 | 暂停任务，向用户报告；不允许编造 |

#### 0.2.4.1 工具能力升级阶梯

> [!IMPORTANT]
> **质量优先于速度。** 报告不追求生成快慢，而是数据的准确性和可核验性。当 WebFetch 反复失败或返回不完整数据时，Agent 应按以下阶梯升级工具，**只要 Agent 有对应工具就必须尝试**，宁可慢也不要凑数。

| 阶梯 | 工具示例 | 适用场景 | 代价 |
|:---:|---|---|---|
| 1 | `WebFetch` | 静态 HTML / Markdown 内容 | 低 (5-50k tokens / 次) |
| 2 | `WebSearch` | 找候选 URL / 跨站点交叉验证 / 搜最新公告 | 低 |
| 3 | Browser MCP `navigate` + `get_page_text` (例如 `mcp__Claude_in_Chrome__*`、`mcp__playwright-extension__*`) | JS 渲染页面、动态 factsheet、含交互的发行商网站 | 中-高 (10-100k tokens / 次, 5-30 秒) |
| 4 | Browser MCP `read_page` (accessibility tree) | 需要按结构提取字段（表格、列表、嵌套数据） | 中 |
| 5 | Browser MCP `javascript_eval` / `browser_evaluate` | 极端情况下从 `window` / DOM 直接读取页面数据对象 | 高 |

**何时升级到浏览器（如果 Agent 有该能力）：**
- WebFetch 重试 ≥2 次仍无关键 Tier 1 字段
- 已知页面是 JS 渲染（如 [DBRS Morningstar](https://dbrs.morningstar.com/) 评级页、[SEDAR+](https://www.sedarplus.ca/) 文件查询、部分发行商的 factsheet 框架）
- 需要下载 PDF（招股说明书、年报）— browser 能跟踪下载链接，WebFetch 不行
- 数据是页面打开后异步加载的（factsheet 数字面板、AUM 实时计算）
- 需要登录后查看的内容（**SOP 不允许 Agent 自动登录**，但 browser 可以让用户先登录再让 Agent 读取）

**何时不升级（继续用 WebFetch）：**
- 页面 HTML 已包含目标字段（绝大多数发行商主页和产品页都是这种）
- 字段属于 Tier 3（缺失合理）
- Agent 没有 browser MCP 工具

**完全没有 browser MCP 工具的 Agent：**
- **不要伪造能力**。在产品卡 / 数据缺口章节明确标注"该字段需 JS 渲染浏览器才能抓取，本会话无浏览器能力，已跳过"
- 下次会话若用户提供有 browser 能力的 Agent，可补全
- **不允许**因此而提前结束任务——能用 WebFetch 拿到的产品仍必须详细覆盖；缺失字段标注后继续下一只产品

> [!NOTE]
> Browser MCP 工具名称随厂商变化（Chrome MCP / Playwright MCP / Puppeteer MCP / Claude_in_Chrome 等），但接口模式相似（`navigate` → `get_page_text` 或 `read_page` → 解析）。Agent 应识别自己可用的具体工具，按相同模式调用。

### 0.2.5 持续写盘原则

> [!IMPORTANT]
> **Agent 不需要自我评估能力或预算决定提前结束任务。** Agent 的职责是用尽工具能力直到无法继续——无法继续意味着工具调用持续失败、上下文确实溢出、或用户显式停止——而**不是**主动判断"我可能完不成,所以提前结束"。

Agent 的全部职责是遵守"持续写盘"原则，让任何中断都不会丢失已完成的工作：

1. **抓完一只产品** → 立即写 `.splitfunds-workspace/products/<ticker>.json`
2. **完成一个阶段** → 立即更新 `.splitfunds-workspace/checkpoint.txt`
3. **遇到失败** → 立即写入 `.splitfunds-workspace/errors.log`
4. **写最终报告** → 必须先回读 workspace 的 JSON，不能从 context 直接写

这样无论 Agent 在何处中断（context 耗尽、auto-compact 触发、用户取消、网络故障、Agent 进程崩溃），损失的最多只是当前正在抓取的那一只产品。下一个 Agent / 会话从 checkpoint 续接即可，结果一致。

#### 何时停下并报告中断（仅在客观信号出现时）

只有以下**客观信号**出现时，Agent 才应停下并向用户报告"建议新会话续接":
- 同一类操作连续失败 ≥3 次（如连续 3 次 WebFetch 超时）
- 系统/平台明确提示上下文压缩（如 auto-compact 警告）
- 用户显式要求停止

> [!WARNING]
> **不要把"猜测自己可能完不成"当作停下的理由。** Agent 应继续执行下一个原子单元；只要文件持续落盘，单会话能完成多少就是多少，不能完成的部分由下一轮会话续接（详见 § 0.2.7）。**绝不允许**因为"觉得吃力"或"已用 N% 上下文"就提前进入"部分覆盖"终态——这会导致质量严重下降。

### 0.2.6 进度可观测性

每个阶段开始时输出一句话状态摘要（例如："开始 Phase 3，已发现 22 个 ticker，剩余 18 个待抓取"），每完成一只产品/ETF 抓取后追加一行到 stdout 或日志，便于中断后判断进度。

### 0.2.7 任务原子化：Sub-Agent 委派为默认模式

> [!IMPORTANT]
> **核心设计原则:** 整个任务天然分解为大量独立的"原子单元"(每只产品 = 一个原子单元)。**Sub-Agent 委派应作为默认执行模式**——parent 上下文只增长 ~1 行/原子单元，而不是 5-50k tokens/单元。即使 Agent 单会话上下文只有 200k，通过 sub-agent 委派也能在单轮内完成 50+ 标的的全市场覆盖。
>
> 现代主流 AI Agent 普遍支持 sub-agent / task delegation 能力（Claude Code `Agent` 工具、Cursor agent 模式、Cline 子任务、Codex CLI、Gemini CLI、OpenCode、Google AntiGravity 等）。**Agent 必须优先尝试 sub-agent 委派**；只有在确认本平台不支持 sub-agent 时才回退到多轮会话模式。

#### 原子单元划分

| 原子单元 | 委派目标 | 写盘路径 |
|---|---|---|
| 每只 Split Corp 产品 | 抓取 + 字段解析 | `products/<ticker>.json` |
| 每只 ETF | 同上 | `etfs/<ticker>.json` |
| 每个发行商主页扫描 | 列出当前产品组合 | `universe.json` 的 issuer 局部 |
| 宏观数据集 | 单次抓取所有宏观字段 | `macro.json` |
| 每个 SEDAR+ 文件查询 | 抓取并提取关键条款 | 写入对应产品 JSON |

#### Pattern A: Sub-Agent 委派（默认，推荐）

```text
parent_agent 读取 universe.json
for each ticker in universe:
  if products/<ticker>.json exists: skip（已完成的不重做）
  else:
    spawn sub_agent with prompt（详见下方模板）
    parent receives 单行状态: "✓ SBC.json written, 15/18 fields verified"
                            或 "✗ SBC: NAV page 503"
parent 在所有 sub-agent 返回后:
  → 读 products/*.json 进行 Phase 4 计算
  → 写最终报告
```

**Sub-Agent prompt 模板**（parent 必须按此格式构造）:

```text
你的任务: 抓取加拿大 Split Corp 产品 <TICKER> 的所有字段，写入 JSON 文件。今日日期: <YYYY-MM-DD>。

输入:
- 产品名: <product_name>
- 发行商: <issuer>
- 已知 URL 候选: 
  * 主页: <issuer_product_url>
  * Factsheet: <factsheet_url_or_unknown>
  * 分红公告: <distribution_url_or_unknown>
- 字段清单（按 Tier）:
  Tier 1 (必须): ticker, NAV+date, 市价+date, 到期日, 年分红+频率, DBRS 评级
  Tier 2 (推荐): 折溢价、NAV 安全边际、隐含杠杆、停派阈值、资产覆盖率、底层持仓
  Tier 3 (尽力): T3 税务、历史总收益、DRIP、bid/ask/volume

工具使用顺序:
1. WebFetch 主页 → 解析能拿到的字段
2. 缺失字段 → WebFetch 子页（factsheet, fund-features 等）
3. 仍缺失 → 升级到 browser MCP（如 Agent 有此能力）抓 JS 渲染内容
4. 仍缺失 → 标 "未在官方来源核验到" + 列已查 URL ≥2 个

输出:
- 写入 .splitfunds-workspace/products/<TICKER_SAFE>.json
  - **文件名约定**: ticker 中的 `.` 替换为 `_`（例: PIC.A → PIC_A.json，PVS.PR.H → PVS_PR_H.json）
  - 结构示例:
    {
      "ticker_class_a": "...",
      "ticker_preferred": "...",
      "product_name": "...",
      "issuer": "...",
      "as_of_date": "<NAV 日期>",
      "retrieved_at": "<当前抓取时间 ISO 8601>",
      "fields": {
        "unit_nav": {"value": ..., "as_of_date": "...", "source_url": "..."},
        "class_a_nav": {...},
        "class_a_market_price": {...},
        "preferred_face_value": ...,
        "preferred_market_price": {...},
        "class_a_distribution": {"amount": ..., "frequency": "...", "current_yield_pct": ...},
        "preferred_distribution": {...},
        "maturity_date": "...",
        "dbrs_rating": {"rating": "...", "rating_date": "..."},
        "nav_suspension_threshold": ...,
        "top_holdings": [...],
        "total_nav": ...,
        "inception_date": "..."
      },
      "data_gaps": ["未核验字段名 1", ...],
      "sources": ["url1", "url2"]
    }
- 返回 parent 一行状态(不要返回 JSON 内容):
  "✓ <TICKER>.json written, X/Y T1+T2 fields verified" 
  或 "✗ <TICKER>: <错误原因>"

约束:
- 不调用其他 sub-agent（避免无限嵌套）
- 不修改 checkpoint.txt（parent 负责）
- 不写最终报告（parent 负责）
- 不使用训练数据填字段；任何无法核验的字段必须留空或标"未在官方来源核验到"
- 如果产品**只发行 Preferred Shares 而无 Class A**(例如 Partners Value 系列），ticker_class_a 字段留 null，相关 Class A 字段全部留 null，但 Preferred 字段必须完整
- 检查 NAV 日期是否 stale: 距今 >14 天必须在 JSON 中加 `"nav_staleness_warning": "..."` 字段
```

**好处:**
- 每只产品的 5-50k tokens fetch 输出**留在 sub-agent 上下文**，parent 只见一行状态
- Parent 处理 50+ 产品仍不溢出
- Sub-agent 失败时 parent 可立即重试（spawn 新 sub-agent）
- 部分平台支持**并行 sub-agent**（一次 spawn 多个），可大幅提速

**Parent 必须确保:**
- Sub-agent 继承了 WebFetch 工具
- 如可用，sub-agent 也继承 browser MCP 工具（`mcp__Claude_in_Chrome__*` / `mcp__playwright-extension__*` 等）
- Sub-agent 知道写盘路径约定和 ticker 文件名安全转换(`.` → `_`)
- Parent 在 sub-agent 返回后**立即检查文件存在**——sub-agent 可能错误地报告 "✓" 但实际未写盘

**Sub-Agent 工具权限不继承的应对**(部分 Agent 平台默认不让 sub-agent 用 parent 的工具):
- Parent **第一次** spawn sub-agent 前,先做"权限预检": spawn 一个测试 sub-agent 抓取一个无关键意义的公开 URL(例: example.com 或 BoC 主页),验证 WebFetch 工作
- 测试失败 → **立即放弃 sub-agent 模式**, 切换到 Pattern B 多轮会话续接 (parent 自己 fetch)
- 不要继续 spawn 25 个会全部失败的 sub-agent,这只会浪费时间和 token

#### Pattern B: 多轮会话续接（无 sub-agent 能力时的回退）

如果 Agent 平台不支持 sub-agent（少数 legacy CLI Agent），改用多轮会话模式：

```text
Round 1: Phase 1-2 + Phase 3 前 3-5 只 → 写盘 → 收尾仪式 → 报告"未完成"
Round 2: 续接 → Phase 3 接下 5-8 只 → 写盘 → 收尾 → 报告"未完成"
Round 3: 续接 → Phase 3 剩余 → Phase 4-5 → "完成"
```

#### Pattern C: Sub-Agent + 多轮组合（双重保险）

具备 sub-agent 的 Agent 也可同时使用多轮模式作为保险：
- 单轮内：Phase 3 用 sub-agent 委派每只产品，节约 parent 上下文
- 跨轮：仍持续写盘 + checkpoint
- 即使本轮 sub-agent 全部完成，下一轮可独立验证已写入的 JSON

#### 会话收尾仪式（任何 Pattern 下，本轮无法继续时必须执行）

无论用 Pattern A、B 还是 C，当本轮无法继续时必须执行以下 4 步:

1. **确保当前产品完整写盘**（不要留下半成品 JSON）
2. **更新 `checkpoint.txt`** 为精确状态:
   - `PHASE-1-DONE` / `PHASE-2-DONE` / `PHASE-4-DONE` / `DONE`（已完成的阶段）
   - `PHASE-3-PARTIAL` + 在 checkpoint.txt 第二行写 `completed_count=N total=M`（部分完成）
3. **写 `session_summary.md`** 到 `.splitfunds-workspace/`:

```markdown
# Session Summary — YYYY-MM-DD HH:MM TZ

## 本轮已完成
- Phase 1 Universe Discovery: 22 products + 4 ETFs identified
- Phase 2 Macro: BoC 2.25%, Prime 4.45%
- Phase 3 partial: 5/22 products fetched (SBC, DFN, ENS, LCS, BK)
- 已写入文件: products/SBC.json, products/DFN.json, ...

## 本轮未完成
- Phase 3 剩余: 17 products + 3 ETFs (PREF, SPFD details)
- Phase 4: Computations
- Phase 5: Final report

## 下一轮启动指令
请用户发起新会话，给 Agent 这条 prompt：

> "继续 ./split-funds-report-guide.md 任务。读取 .splitfunds-workspace/checkpoint.txt
> 和 session_summary.md 续接。优先抓取以下未完成产品：[ticker 列表]"
```

4. **向用户输出明确的"未完成"消息**:

```text
⚠️ 本轮未完成。已完成 5/22 产品 + 0/3 ETF（详见 .splitfunds-workspace/session_summary.md）。
请发起下一轮会话续接，prompt 见 session_summary.md 末尾。
```

#### 任何 Agent 能完成的最小路径

```text
现代 Agent (有 sub-agent + 200k+ 上下文):
  Round 1: 
    Phase 1-2 (parent 自己做)
    Phase 3: 委派 ~25 个 sub-agent (每只产品一个)
    Phase 4-5 (parent 读 JSON 自己做)
  → 单轮完成
```

```text
Legacy Agent (无 sub-agent，32k 上下文):
  Round 1: Phase 1-2 + Phase 3 前 3 只 → 报告"未完成"
  Round 2: 续接 → 接下 5 只 → 报告"未完成"  
  ...
  Round N: 剩余 + Phase 4-5 → "完成"
  → 多轮完成
```

> [!IMPORTANT]
> **两种模式都能让任何 Agent 完成任务。** 不要把"分多轮"当成失败——多轮模式 + 持续写盘 = 任何 Agent 都能产出高质量报告的设计保证。但**优先尝试 sub-agent 委派**，因为它通常更快、更可靠。

---

## 1. 不可妥协的数据原则

1. **零猜测、零幻觉，按时效性分级核验。**
   - **当前状态字段**（NAV、NAV 日期、市价、bid/ask、当前分红、最新评级、当前 Prime Rate、当前到期日剩余）：**必须当日核验**，否则字段标"未在官方来源核验到"。
   - **结构性字段**（成立日、招股条款、面值、利率规则、停派阈值、行业分类）：来源是当日访问的招股书或最新公告即可，**不要求当日发布**。
   - **历史字段**（历史总收益、过往年度 T3 税务构成、长期波动率）：必须给出"来源 + 时间区间（如 2020-2025）+ 数据完整性 High/Medium/Low"三件套，不能仅给一个数字。
2. **每个投资标的都必须去官网获取最新数据。** 对每一个 Split Fund 和 Split Funds ETF，必须访问发行商官网的产品页、factsheet、NAV 页面、公告、税务信息页或招股文件。**不允许跳过任何标的的现场核验。**
3. **官方来源优先级（从高到低）：**
  1. 发行商官网产品页 / factsheet / NAV page / 最新分红公告
  2. SEDAR+ 正式文件（招股说明书、年度信息表、管理层报告、重大事项公告）
  3. TSX/TMX 官方交易信息（ticker、状态、上市日期）
  4. DBRS/Morningstar DBRS 评级公告
  5. Bank of Canada / 主要加拿大银行（RBC/TD/BMO/CIBC/Scotia）页面（用于 Prime Rate）
4. **第三方来源只能辅助交叉验证。** Morningstar Canada、TMX、券商行情页、Yahoo Finance、Google Finance 等可以用于辅助核对价格、交易流动性和长期总收益，**但不能替代发行商官网**的 NAV、分红条款、到期日、税务构成和产品规则。**当 bid/ask/volume 等交易数据在发行商官网不可得时，TMX / Yahoo Finance Canada 是合法 fallback**——但必须显式标注来源。
5. **NAV 时效性硬阈值。** NAV、factsheet、分红、评级、税务构成、宏观利率和市价必须标注对应日期或抓取时间。
   - **不同发行商发布频率不同：** Brompton 通常周末/月末发布；Quadravest 半月（每月 15 日 + 月末）；Middlefield 不定期。
   - **NAV 日期距报告日 ≤ 7 天**：可正常使用，不需特殊标注。
   - **8-14 天**：必须在产品卡显式标"NAV 滞后 N 天"。
   - **15-30 天**：必须在产品卡和汇总表都标"⚠️ Stale NAV (N 天前)"，折溢价计算结果置信度降级为 Medium。
   - **>30 天**：视为 NAV 不可用，折溢价不可计算；产品卡只填 Tier 1 中其他字段。
6. **不允许用"同类产品推定"填数。** 如果某项条款没有在官方来源中找到，写成"未在官方来源核验到"，并说明已检查的来源（至少 2 个）。**不要把其他产品的规则套用到该产品。**
7. **不要把高分红当成高回报。** Split Funds 分红频繁，税务构成复杂，且第三方历史价格数据经常缺少分红、资本返还（ROC）或特殊分派。任何长期表现判断都必须明确数据来源、是否包含分红复投、是否考虑税务，以及数据完整性等级。

> [!CAUTION]
> **致命陷阱：** 发行说明书或营销材料中披露的 Pfd Target Yield 是发行时或某一报告期的目标收益率，与"今天买入的实际 YTM"是两回事。Agent 必须根据**今日市价**重新计算 YTM，不能直接复用任何历史 yield 数字。

---

## 2. 全量标的发现流程

报告必须先建立当日 universe，再进入分析。覆盖范围必须以当日发行商官网、TSX/TMX、SEDAR+ 现场抓取为准。

### 2.0 最低 seed universe（只作发现线索，不能当作当前事实）

下列清单是常见的加拿大 split share universe，只能作为"必须重新核验的候选清单"。Agent 必须用当日官方来源逐一核对每个 ticker 的当前状态。

> [!IMPORTANT]
> **Seed list 是历史快照，必须假设 ≥10% 条目已过时。** Agent 必须执行**反向核验**：
> 1. 对每个 seed ticker，在 TSX/TMX 搜索（[money.tmx.com](https://money.tmx.com/)）或 WebSearch 查 "<ticker>.TO 2026" 确认仍在交易；
> 2. 在对应发行商主页确认仍是产品组合的一部分；
> 3. 差异部分必须在 universe audit 中分类记录为：
>    - `confirmed_active` — seed 中存在且当日仍在交易
>    - `terminated` / `merged` / `redeemed` — 已退出
>    - `renamed` / `series_changed` — 仍存在但 ticker 或 series 字母变更
>    - `status_unverified` — 主页未列出且无法确认状态（**必须查 SEDAR+**）
>    - `new_discovery` — seed 中没有但当日发行商主页发现的产品

**已知风险点**（截至本手册维护日，需 Agent 重新核验）：
- ⚠️ "IS / IS.PR.A" 历史上常被误归 Brompton；实际为 **Middlefield Limited 旗下 Infrastructure Dividend Split Corp**——Agent 必须以当日发行商主页归属为准。
- ⚠️ Quadravest "PDV / PDV.PR.A" (Prime Dividend Corp) 历史 seed 中常出现，但近期 Quadravest 主页可能不再展示——Agent 必须查 SEDAR+ 确认当前状态。
- ⚠️ Ninepoint "NPS / NPS.PR.A" (Canadian Large Cap Leaders Split Corp) 在 Ninepoint 主页可能不显著——必须深度搜索或查 SEDAR+。

如果官网、TSX/TMX 或 SEDAR+ 证明某标的已终止、改名、延期、赎回或停止交易，必须在 universe audit 中说明。

**Brompton Funds seed tickers：**

- SBC / SBC.PR.A — Brompton Split Banc Corp
- LBS / LBS.PR.A — Life & Banc Split Corp
- LCS / LCS.PR.A — Brompton Lifeco Split Corp
- ESP / ESP.PR.A — Brompton Energy Split Corp
- GDV / GDV.PR.A — Global Dividend Growth Split Corp
- DGS / DGS.PR.A — Dividend Growth Split Corp
- PWI / PWI.PR.A — Power & Infrastructure Split Corp
- IS / IS.PR.A — Infrastructure Dividend Split Corp（Brompton 版，注意与 Middlefield Infrastructure 区分）

**Quadravest seed tickers：**

- DFN / DFN.PR.A — Dividend 15 Split Corp
- DF / DF.PR.A — Dividend 15 Split Corp II
- FTN / FTN.PR.A — Financial 15 Split Corp
- FFN / FFN.PR.A — North American Financial 15 Split Corp
- BK / BK.PR.A — Canadian Banc Corp
- PDV / PDV.PR.A — Prime Dividend Corp
- LFE / LFE.PR.B — Canadian Life Companies Split Corp（注意 series 字母随重设变化）
- FTU / FTU.PR.B — U.S. Financial 15 Split Corp（确认当前 outstanding preferred series）

**Mulvihill seed tickers：**

- PIC.A / PIC.PR.A — Premium Income Corporation（Pfd 面值 $15）
- PGIC / PGIC.PR.A — Premium Global Income Split Corp（原 World Financial Split Corp）

**Middlefield seed tickers：**

- ENS / ENS.PR.A — E Split Corp（单一持仓 Enbridge）
- RS / RS.PR.A — Real Estate Split Corp
- Middlefield Infrastructure Split（如有；不要与 Brompton IS 混淆）

**Ninepoint seed tickers：**

- NPS / NPS.PR.A — Canadian Large Cap Leaders Split Corp

**Partners Value seed tickers（Brookfield 关联，多 series）：**

- PVS.PR.H、PVS.PR.J、PVS.PR.K、PVS.PR.L、PVS.PR.M、PVS.PR.U（USD）、PVS.PR.V（USD）等
- 实际 outstanding series 必须以 partnersvaluesplit.com 和 SEDAR+ 为准
- 注意 Partners Value 通常**只发行 Preferred Shares，不公开发行 Class A**

**Harvest Portfolios seed tickers：**

- PRM / PRM.PR.A — Big Pharma Split Corp（注意若已到期或终止必须用官方公告确认）
- 检查 Harvest 官网是否有新增 Split Corp 产品

**Split Funds ETF seed tickers（必须至少覆盖以下四只）：**

- `SPLT.TO` — Brompton Split Corp Preferred Share ETF
- `PREF.TO` — Quadravest Canadian Preferred Share ETF（或 RPS/RPF 同类，以官网为准）
- `CLSA.TO` — Brompton Split Corp Class A ETF（确认全名）
- `SPFD.TO` — 加拿大 Split Share 主题 ETF（以官网当前披露的全名和发行商为准；可能与上述三只之一为不同发行商竞品或互补产品，必须独立核验持仓和投资目标）
- 任何通过发行商官网、TSX/TMX 或新闻稿发现的新增 Split Funds ETF 或 split-share-focused ETF（包括但不限于 Harvest、Hamilton、Evolve、Horizons、Global X 旗下若有 split share 主题产品）

> [!IMPORTANT]
> 报告至少必须核验并覆盖 `SPLT.TO`、`PREF.TO`、`CLSA.TO`、`SPFD.TO` 四只 ETF。如果发行商官网或 TSX/TMX 显示 ticker 已改名、终止、合并或停止交易，必须在 ETF 章节和 universe audit 中说明，并以官方当前 ticker 为准。**随着时间推移可能出现新的 Split Funds ETF**（例如其他发行商进入此细分），Agent 不能只停留在这四个 seed tickers，必须持续从发行商官网、TSX/TMX、SEDAR+ 和新闻稿发现新增 ETF。

如果 seed universe 与当日官方资料冲突，**以当日官方资料为准**，并在报告中说明冲突。

### 2.1 发行商官网发现

至少检查以下发行商官网的产品页、fund list、press release、new issue、closed-end funds 或 split share 页面：

- Brompton Funds — bromptongroup.com
- Quadravest Capital Management — quadravest.com
- Mulvihill Capital Management — mulvihill.com
- Middlefield — middlefield.com
- Ninepoint Partners — ninepoint.com
- Partners Value Split Corp. — partnersvaluesplit.com
- Harvest Portfolios — harvestportfolios.com
- Hamilton ETFs、Evolve、Horizons、Global X Canada — 检查是否有 split share 主题产品
- 任何通过 TSX/TMX、SEDAR+、新闻稿或发行商交叉引用发现的新增加拿大 Split Fund 或 Split Funds ETF 发行商

### 2.2 交易所与公告发现

必须用以下渠道补充"最新上市"和"遗漏标的"：

- TSX/TMX ticker 或 listed issuer 搜索（money.tmx.com、tmxmoney.com）
- 发行商 press releases / new issues 页面
- SEDAR+ (sedarplus.ca) 最新招股说明书、年度信息表、管理层报告、重大事项公告
- DBRS Morningstar 评级公告页（dbrs.morningstar.com）
- 已知 ticker 反查（包括历史曾发行的 split share），确认是否仍在交易、已合并、已延期、已赎回、已终止或改名

### 2.3 Universe Audit 表

报告中必须放置一个 universe audit 小表，说明当日覆盖范围：


| 类别                                     | 数量  | 发现来源                     | 备注                           |
| -------------------------------------- | --- | ------------------------ | ---------------------------- |
| Split Funds / Split Share Corporations |     | 发行商官网 + TSX/TMX + SEDAR+ | 包含仍在交易和已公告新上市标的              |
| Preferred Share series                 |     | 发行商官网 + DBRS + TSX/TMX   | 每个 series 单独计数               |
| Class A / Capital Share series         |     | 发行商官网 + TSX/TMX          | 每个交易符号单独计数                   |
| Split Funds ETF                        |     | 发行商官网 + TSX/TMX          | ETF 单独章节分析                   |
| 排除项                                    |     | 官方公告                     | 已终止、已赎回、停止交易或非加拿大 Split Fund |
| 新增发现                                   |     | 当日新闻 / 新公告               | 列出当日通过新闻或新公告发现的标的      |


如果无法确认是否全量，必须写明缺口和下一步核验路径，**不能声称"全市场完整"**。

---

## 2.4 数据工作底稿要求

最终报告可以是 Markdown，但生成前必须先维护一个可审计的数据工作底稿。可以是临时表格、CSV、Markdown 表或 Agent 内部 structured notes。报告中至少要体现这些字段：


| 字段              | 要求                                                                                      |
| --------------- | --------------------------------------------------------------------------------------- |
| `product_name`  | 产品官方全名                                                                                  |
| `issuer`        | 发行商                                                                                     |
| `security_type` | Class A / Capital / Preferred / ETF                                                     |
| `ticker`        | 当前交易 ticker                                                                             |
| `source_url`    | 直接来源链接                                                                                  |
| `source_type`   | issuer website / factsheet / NAV page / TMX / TSX / SEDAR+ / DBRS / Morningstar / macro |
| `as_of_date`    | 来源数据日期                                                                                  |
| `retrieved_at`  | 抓取时间和时区                                                                                 |
| `value`         | 具体数值或条款                                                                                 |
| `confidence`    | High / Medium / Low                                                                     |
| `notes`         | 数据缺口、冲突或计算假设                                                                            |


如果同一字段在不同来源冲突，必须按以下顺序处理：

1. 发行商官网和正式公告优先。
2. SEDAR+ 正式文件优先于营销页。
3. TSX/TMX 用于交易价格和交易状态。
4. DBRS/Morningstar DBRS 用于评级。
5. Morningstar Canada 可辅助核验 total return，但不得覆盖发行商条款。
6. 冲突无法解决时，报告中写"来源冲突"，列出冲突来源和选择依据。

---

## 3. 每个标的必须抓取的字段

每个 Split Fund 必须建立一张产品级数据卡。每个字段后面都要能追溯到来源链接和日期。

### 3.0 字段分级系统（关键）

**为什么分级:** 现实中很多字段（资产覆盖率、停派阈值、T3 税务构成）在发行商网站不公开披露，需要查 SEDAR+ 招股说明书；而后者经常是 PDF 形式且抓取困难。强制要求每个字段都核验会让 Agent 卡死。

字段分为三级，对应不同的合格标准：

| Tier | 名称 | 缺失含义 | 合格标准 |
|:---:|---|---|---|
| **T1** | 必须 | 缺失 → 产品卡作废，标"数据不可用，不纳入分析" | 100% |
| **T2** | 高度推荐 | 缺失需在产品卡的"数据缺口"明示 | ≥70% 标的有此字段 |
| **T3** | 尽力收集 | 缺失合理，标"未在官方来源核验到"+ 已查的 ≥2 个来源 | 不强制 |

**合格产品卡 = Tier 1 全部 + Tier 2 ≥70% + Tier 3 缺失明示。**

> [!NOTE]
> Tier 标记在第 3.1-3.4 各字段名后用 `[T1]` / `[T2]` / `[T3]` 显示。

### 3.1 基础字段

- 产品全名 `[T1]`
- 发行商 `[T1]`
- Class A / Capital Share ticker `[T1]`
- Preferred Share ticker 或所有 Preferred series ticker `[T1]`
- 当前到期日、延期条款 `[T1]`
- 发行结构：Class A + Preferred / 多 Preferred series / 单一底层股票型 / covered call 型 / 全球/加拿大/行业主题 `[T1]`
- 产品官网链接 `[T1]`
- 投资方向和底层持仓摘要（前 5-10 大持仓 + 行业分布）`[T2]`
- 成立日期 / inception date `[T2]`
- factsheet 链接、NAV 链接 `[T2]`
- 最近一次延期公告日期 `[T3]`
- SEDAR+ 链接 `[T3]`

### 3.2 Preferred Shares 字段

每个 Preferred series 必须单独记录：

- ticker、series、currency（CAD / USD）`[T1]`
- 面值或 redemption value `[T1]`
- 年化分红金额、支付频率（月度/季度）`[T1]`
- 利率规则：固定、浮动、Prime-linked、年度审核、最低/最高利率、重设规则 `[T1]`
- 到期日、赎回条款 `[T1]`
- DBRS/Morningstar DBRS 评级和评级日期 `[T1]` (未评级必须标"官方未核验到评级")
- 当前市价、价格时间戳 `[T1]`
- 当前 current yield（基于市价）`[T1]`
- 资产覆盖率或 downside protection（NAV / Pfd 面值）`[T2]`
- YTM/YTW 估算（含假设：买入价、面值、年分红、到期日、是否假设面值赎回）`[T2]`
- bid/ask spread `[T2]`
- 延期或重设条款细节 `[T3]`
- 日均成交量 `[T3]`

### 3.3 Class A / Capital Shares 字段

每个 Class A 或 Capital Share ticker 必须单独记录：

- ticker `[T1]`
- 最新 Unit NAV 和 NAV As of Date `[T1]`
- 最新市价、价格时间戳 `[T1]`
- 年化分红金额、支付频率 `[T1]`
- 分红状态：正常 / 暂停 / 恢复 / 变更 / 特殊分派 `[T1]`
- 当前分红率（基于市价）`[T1]`
- Preferred 面值扣除后的 Class A NAV 估算 `[T2]`
- 折价/溢价率（计算结果）`[T2]`
- NAV 安全边际（计算结果）`[T2]`
- 隐含杠杆率（计算结果）`[T2]`
- 停派阈值或覆盖测试规则 `[T2]`
- 底层资产质量、行业集中度、单一持仓风险、covered call 对上行空间的影响 `[T2]`
- 近 24 个月分红是否中断过 `[T3]`
- 是否提供 DRIP `[T3]`
- 官方历史总收益数据（含来源 + 时间区间 + 数据完整性等级）`[T3]`
- bid/ask、日均成交量 `[T3]`

### 3.4 Split Funds ETF 字段

Split Funds ETF 必须单独成章，不要混入普通 Split Fund 产品卡中。ETF 字段：

- ETF ticker、全名、发行商、官网链接 `[T1]`
- 投资目标：是否投资 Split Corp Preferred Shares、Class A、混合篮子或其他结构 `[T1]`
- 最新 NAV、NAV 日期 `[T1]`
- 最新市价 `[T1]`
- 分红金额、分红频率、当前分配率 `[T1]`
- MER `[T1]`
- 持仓类型（Preferred / Class A / 混合）`[T1]`
- AUM `[T2]`
- 成立日期 `[T2]`
- 持仓数量、前十大持仓 `[T2]`
- 折溢价（NAV vs 市价）`[T2]`
- 持仓中 Preferred/Class A 的比例、发行商集中度（前 3 / 前 5 占比）`[T2]`
- 与自行购买单只 Preferred / Class A 的优缺点定性比较 `[T2]`
- 到期日集中度、评级集中度 `[T3]`
- 税务构成和 historical distribution（T3 breakdown）`[T3]`
- DRIP 是否可用 `[T3]`
- Trading Expense Ratio (TER) `[T3]`

> [!IMPORTANT]
> 最低覆盖要求：ETF 章节必须至少包含 `SPLT.TO`、`PREF.TO`、`CLSA.TO`、`SPFD.TO` 四只 seed ETF 的逐只数据卡，除非官方来源确认某个 ETF 已改名、终止、合并或停止交易；这种情况必须明确写入 universe audit 和数据缺口。

---

## 4. 宏观环境与多周期观点

报告必须基于报告日期当天可核验信息，给出短期、中期、长期观点：

### 4.1 必须核验的宏观数据

- Bank of Canada 政策利率和最近一次利率决定日期、下次会议日期
- 加拿大主要商业银行 Prime Rate（注意：Prime Rate ≈ BoC overnight + 220bp，但以银行实际公告为准）
- 加拿大国债收益率曲线：至少包括 2 年、5 年、10 年
- 信用利差：投资级公司债与同期限国债的 OAS
- 主要板块环境：银行股（BMO/BNS/CIBC/NA/RY/TD）、保险股（MFC/SLF/GWO/IAG）、能源（ENB/TRP/CNQ/SU）、房地产 REIT、公用事业、基础设施
- CAD/USD 汇率和大宗商品环境（WTI、天然气、铜），如果影响底层资产
- VIX 或 加拿大波动率指数（如有）

### 4.2 必须输出的多周期观点

- **短期观点（1-3 个月）：** 哪些交易机会或风险由折溢价、滞后 NAV、流动性、公告事件（重设、延期、特殊分派）、分红恢复/暂停驱动。**必须给出具体 ticker 级判断**。
- **中期观点（6-12 个月）：** 利率路径、行业景气、到期/延期、Preferred 重设和 Class A 分红可持续性。**必须区分加息周期 vs 降息周期下浮动利率 Preferred (BK/PDV) 与固定利率 Preferred 的相对吸引力**。
- **长期观点（1-3 年以上）：** 底层资产复利能力、税后总回报、ROC 对 NAV 的侵蚀、ETF 与单只证券的长期适配性。**必须区分 Class A 长期持有的"稳态侵蚀"风险与"折价回归"机会**。

每个观点必须说明更有利于 Preferred、Class A、ETF，还是应该回避，并指明对应 ticker。

---

## 5. 历史总收益和税务数据的特殊警告

> [!WARNING]
> **这一节必须在报告中明确出现，不能省略。**

Split Funds 和 Split Funds ETF 经常月度或季度分红，且分红可能包含 eligible dividends、capital gains dividends、return of capital (ROC)、foreign income、other income 等不同税务构成。很多公开行情网站的长期图表只反映价格，不完整反映现金分红、再投资、特殊分派、资本返还、合并、延期、赎回或 ticker 变更。

### 5.1 必须遵守的 7 条铁律

1. **不能用简单价格走势代表总收益。** 价格图缺失分红会严重低估高分红 Class A 的真实总回报，但同时也可能遮掩 ROC 对 NAV 的长期侵蚀。
2. **不能用缺少分红复投的数据排名长期赢家。**
3. **不能把税前收益直接等同于税后收益。**
4. **ROC 不是免费收益。** ROC 可能递延税务，但会降低 ACB（Adjusted Cost Base），并可能反映 NAV 被长期抽走。**Class A 表面 yield 15%+ 几乎一定包含 ROC。**
5. **长期总收益排名必须有置信等级。** 如果官方 total return series、完整分红记录和复投假设无法核验，只能给出结构化判断，不能给出伪精确排名。
6. **税务身份决定可投性。** Split Fund Preferred 和 Class A 的合格股息税收抵免（Dividend Tax Credit）只对加拿大税务居民有效。USD-denominated Preferred (如 PVS.PR.U)、美国底层资产 ETF 在 RRSP 之外有 15% 美国预扣税。
7. **账户类型决定策略。** TFSA / RRSP / RESP / FHSA / Non-Registered 各有不同税务影响，报告必须在策略章节区分。

### 5.2 报告中每个历史收益结论必须标注

- 数据来源：发行商、Morningstar Canada、TMX 分红记录、SEDAR+ 财报或手工重建
- 时间区间（起止日期）
- 是否包含分红复投（DRIP 假设 vs 现金分红假设）
- 是否包含税务影响（税前 vs 税后）
- 数据完整性：High / Medium / Low
- 不能核验时的明确限制

---

## 6. 核心计算方法

所有计算必须显示公式，关键结果必须能复算。

### 6.1 NAV 安全边际

```text
NAV 安全边际 = (最新 Unit NAV - 停派阈值) / 停派阈值
```

解释要求：

- 安全边际越低，Class A 分红暂停风险越高。
- 当 Unit NAV 逼近停派阈值时，隐含杠杆会非线性飙升。
- 如果 NAV 日期滞后，必须提示折溢价和安全边际可能失真。

**分级标准（建议，可在报告中调整）：**


| 安全边际   | 等级     | 说明               |
| ------ | ------ | ---------------- |
| ≥ 40%  | ✅ 安全   | NAV 显著高于停派阈值     |
| 20-40% | ⚠️ 关注  | 监控板块波动           |
| 5-20%  | 🔴 危险  | 接近停派阈值，杠杆陡升      |
| < 5%   | 💀 极危  | 任何回调都可能触发停派      |
| < 0    | 🚫 已停派 | 当前已暂停 Class A 分红 |


### 6.2 Class A NAV 和折溢价

```text
Class A NAV = Unit NAV - Preferred redemption value
折价/溢价率 = (Class A 市价 - Class A NAV) / Class A NAV
```

若存在多个 Preferred series 或特殊结构（如 PIC.A 的 $15 面值 + $25 阈值），必须说明计算假设，**不能套用普通 $10 面值结构**。

### 6.3 隐含杠杆率

```text
隐含杠杆率 = Unit NAV / Class A NAV
```

若 Class A NAV 接近 0 或为负，必须标注为极端风险，不得输出误导性百分比。

**隐含杠杆情景表（必须在报告中至少出现一次，用于教学）：**


| Unit NAV | Pfd 面值 | Class A NAV | 隐含杠杆  | 状态      |
| -------- | ------ | ----------- | ----- | ------- |
| $25      | $10    | $15         | 1.67x | ✅ 健康    |
| $20      | $10    | $10         | 2.00x | ⚠️ 关注   |
| $17      | $10    | $7          | 2.43x | 🔴 高风险  |
| $15      | $10    | $5          | 3.00x | 🚫 停派阈值 |
| $12      | $10    | $2          | 6.00x | 💀 极端杠杆 |


### 6.4 Preferred YTM/YTW

```text
YTM 估算 ≈ [年分红 + (面值 − 买入价) ÷ 剩余年数] ÷ [(面值 + 买入价) ÷ 2]
```

必须说明：

- 是否假设到期按面值赎回
- 是否存在延期风险（延期通常对 Preferred 持有人不利或中性，需逐案评估）
- 是否可能提前赎回
- 是否使用 bid、ask、last price 或 mid price
- 流动性差时，last price 可能失真，应同时报告 bid 和 ask

### 6.5 资产覆盖率

```text
资产覆盖率 = Unit NAV ÷ Preferred 面值
```

**分级标准：**


| 资产覆盖率    | 等级     | 说明              |
| -------- | ------ | --------------- |
| ≥ 200%   | ✅ 非常安全 | Pfd 本金风险极低      |
| 150-200% | ✅ 安全   | 可安心持有           |
| 130-150% | ⚠️ 需关注 | NAV 进一步下跌可能危及本金 |
| 100-130% | 🔴 警惕  | Pfd 本金存在不确定性    |
| < 100%   | 🚫 已亏损 | Pfd 本金已处于账面亏损   |


### 6.6 分红可持续性

必须比较：

- Class A 表面 yield（基于市价）
- 底层资产自然股息率（指数 dividend yield 或前十大持仓加权 yield）
- covered call option premium 的可持续性（如适用）
- NAV 趋势（过去 12 / 36 个月 NAV 变化）
- ROC 比例（最近 T3 分红构成）
- 分红是否依赖资本增值或本金返还

> [!WARNING]
> **高 yield 只能作为风险信号之一，不能直接作为推荐理由。** 任何 Class A 表面 yield 高于底层资产自然股息率 + 5% 的情况，几乎必然包含资本返还或 covered call 期权金，长期会侵蚀 NAV。

---

## 7. 报告结构要求

最终 Markdown 报告必须包含以下章节，**顺序可以微调，但内容不能缺失**。

### 7.1 报告抬头

```markdown
# 加拿大 Split Funds 深度投资研报

> 报告生成日期: YYYY-MM-DD
> 数据抓取时间: YYYY-MM-DD HH:MM 时区
> 重要声明: 本报告只使用可核验来源；无法核验的数据明确标注，不以推断补齐。
> 数据时效: NAV 通常滞后 1-5 个交易日；价格为抓取时刻报价，盘中可能波动。
```

### 7.2 执行摘要

必须回答：

- 当日最重要的机会是什么（具体到 ticker）
- 当日最重要的风险是什么（具体到 ticker）
- Preferred、Class A、Split Funds ETF 哪一类更占优
- 哪些标的需要回避
- 哪些结论因为历史分红或税务数据不完整而需要降低置信度

执行摘要必须使用 `[!IMPORTANT]` 或 `[!TIP]` alert 高亮当日最高确信度结论。

### 7.3 Universe Audit 与数据来源摘要

放置第 2.3 节的 universe audit 表，并列出主要来源链接。

### 7.4 宏观环境与短中长期观点

使用第 4 节框架，必须给出短期、中期、长期观点，每段至少 3-5 句具体分析。

### 7.5 投资方法论与核心公式

展示第 6 节公式，并说明：

- 死亡螺旋（NAV 接近停派阈值时的非线性杠杆爆破）
- 折溢价回归机制
- YTM 计算与流动性陷阱
- 分红可持续性识别
- 税务差异（账户类型 + 分红构成）

必须包含第 6.1 节安全边际分级表、第 6.3 节隐含杠杆情景表、第 6.5 节资产覆盖率分级表。

### 7.6 Split Funds 全市场产品章节

按发行商分类列出所有 Split Funds。每个产品必须有：

- 产品数据卡（使用第 7.19 节模板）
- Preferred 分析（≥1 段）
- Class A 分析（≥1 段）
- 关键机会（≥2 条，引用本产品具体数据）
- 关键风险（≥2 条，引用本产品具体数据）
- 数据缺口（明确列出未核验字段）

### 7.7 Split Funds ETF 独立章节

单独列出所有 Split Funds ETF。**至少包括 `SPLT.TO`、`PREF.TO`、`CLSA.TO`、`SPFD.TO` 四只已知 seed ETF**，以及当日通过官方来源发现的任何新增或同类 ETF。不要把 ETF 当成普通 Split Share Corporation。若其中任何 seed ETF 已改名、终止、合并或停止交易，必须用官方来源说明，不得静默删除。

每只 ETF 必须说明：

- 投资组合实际持有什么（前十大持仓 + 发行商集中度）
- 与单买 Preferred/Class A 相比，收益、分散、费用、税务和流动性的差异
- 是否适合作为长期底仓、现金流工具或战术配置

ETF 章节末尾必须有 ETF 横向对比表：


| ETF Ticker | 类型  | NAV | 市价  | 分配率 | MER | AUM | 成立  | 持仓数 | 评级集中度 |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |


### 7.8 Preferred Shares 全市场汇总对比表

必须一行一个 Preferred ticker 或 series，**不能只按产品合并**。

建议字段：


| #   | 产品名称 | Preferred ticker/series | 发行商 | 面值  | 最新市价 | bid/ask | 到期日 | 年分红 | Current Yield | YTM/YTW 估算 | 资产覆盖率 | 利率规则 | 评级  | 数据来源/日期 |
| --- | ---- | ----------------------- | --- | --- | ---- | ------- | --- | --- | ------------- | ---------- | ----- | ---- | --- | ------- |


表格后必须给出（每条至少 1 个 ticker 引用）：

- 最有吸引力的 Preferred 候选（YTM 高 + 资产覆盖率 ≥150% + 评级 ≥ Pfd-3）
- 最安全的 Preferred 候选（资产覆盖率 ≥200% + 评级 ≥ Pfd-2 或 Pfd-3 high）
- 最高 YTM 是否由真实机会还是流动性/信用风险造成
- 需要回避的 Preferred（资产覆盖率 < 130% 或评级下调或市价显著溢价）
- **≥1 组 head-to-head 对比**：对底层资产或结构最相似的 2-3 只 Preferred 给出"在何种情景下选哪只"的 2-3 行决策语句（例：SBC.PR.A vs LBS.PR.A vs DFN.PR.A 在加拿大六大行底层下的差异）

### 7.9 Class A / Capital Shares 全市场汇总对比表

必须一行一个 Class A 或 Capital Share ticker。

建议字段：


| #   | 产品名称 | Class A ticker | 发行商 | Unit NAV (日期) | Class A NAV | 最新市价 | 折溢价 | 年分红 | 当前分红率 | 停派阈值 | NAV 安全边际 | 隐含杠杆 | 分红状态 | 数据来源/日期 |
| --- | ---- | -------------- | --- | ------------- | ----------- | ---- | --- | --- | ----- | ---- | -------- | ---- | ---- | ------- |


表格后必须给出（每条至少 1 个 ticker 引用）：

- 最有吸引力的 Class A 候选（折价 ≥5% + NAV 安全边际 ≥40% + 分红近 12 月稳定）
- 明显溢价且应回避的 Class A
- NAV 安全边际最低的危险名单
- 分红暂停、刚恢复、或接近停派阈值的名单
- **≥1 组 head-to-head 对比**：对底层资产最相似的 2-3 只 Class A（例：SBC vs LBS vs DFN 在加拿大六大行下的杠杆/折溢价/到期差异）

### 7.10 Class A 投资策略章节（深度章节）

必须包含以下子章节：

#### 7.10.1 Class A 本质特征

- 用具体数字解释 Class A 是底层组合的杠杆化敞口
- 给出隐含杠杆情景表（第 6.3 节）

#### 7.10.2 买入 Class A 前必须检查的 4 项指标

1. NAV 安全边际（最重要）
2. Class A 市价 vs NAV 折溢价
3. 分红收益率 vs 可持续性
4. 到期日与时间价值

#### 7.10.3 ≥3 种**操作上彼此独立**的 Class A 总收益策略

每种策略必须有：(1) 名称 + 目标，(2) 操作步骤表（步骤 / 操作），(3) 适合产品列表，(4) **"其他策略不适用时为何选这一种"的判断标准**——确保策略之间不重叠。

参考策略池（Agent 可从中选 3 种或自定义，但选出的必须真正独立）：

- **策略 A: 折价+高分红（收入型）** — 月度分红 + 折价回归
- **策略 B: 深度折价+NAV 回升（价值型）** — 行业回调时抄底
- **策略 C: 行业轮动（主动型）** — 利用 Split Fund 行业集中敞口
- **策略 D: 杠杆替代（进阶型）** — 用 Class A 替代保证金账户

每种策略后必须给出该策略下当前推荐 ticker 名单（基于当日数据）。

> [!NOTE]
> **独立性自检：** 写完策略后，Agent 应自问"如果删除其中一种，剩下的是否仍能覆盖大部分场景？"如果答案是"是"，说明策略之间重叠，需合并或重写。

#### 7.10.4 Class A 风险管理要点

- 必须规避的 4-5 种情况
- 持续监控的 5 项指标（频率 + 来源）
- Class A 总收益公式

#### 7.10.5 Class A 投资决策速查流程图（可选）

> [!NOTE]
> **流程图为可选**：若策略章节（7.10.3）已用步骤表充分呈现决策逻辑，可省略本节。仅当 Agent 判断流程图能在策略章节之外提供独立的"快速参考卡"价值时才包含。如包含，使用以下文本格式:

```text
开始
  │
  ▼
[1] 检查 NAV/Unit ──→ < $17? ──→ ⛔ 暂不买入
  │
  ▼ ≥ $17
[2] 计算折/溢价 ──→ 溢价 > 3%? ──→ ⛔ 等待折价
  │
  ▼ 折价或小幅溢价
[3] 检查分红历史 ──→ 近12月有停派? ──→ ⚠️ 调查原因
  │
  ▼ 分红稳定
[4] 比较同类 ──→ 选择折价最大 + 到期合适
  │
  ▼
[5] 仓位 ──→ 单只 ≤ 10%, 同行业 ≤ 25%
  │
  ▼
  ✅ 买入并设置监控
```

### 7.11 Preferred Shares 投资策略章节（深度章节）

必须包含以下子章节：

#### 7.11.1 Preferred Shares 本质特征

- 解释优先分红权、到期本金偿还、下行保护
- 用具体数字示例（NAV $18 vs NAV $7 两种情景）

#### 7.11.2 买入 Preferred 前必须检查的 5 项指标

1. YTM 到期收益率（最核心）
2. 买入价 vs 面值（折/溢价）
3. DBRS 评级
4. 利率类型（固定/浮动/年度审核）
5. NAV 资产覆盖率

#### 7.11.3 ≥3 种**操作上彼此独立**的 Preferred 投资策略

每种策略必须有：(1) 名称 + 目标，(2) 操作步骤表，(3) 适合产品列表，(4) **"其他策略不适用时为何选这一种"的判断标准**。

参考策略池：

- **策略 A: 持有到期收息（核心策略）** — 高 YTM + 持有到期收回面值
- **策略 B: 浮动利率对冲（加息环境）** — BK / PDV 利用 Prime Rate
- **策略 C: 折价抄底（价值型）** — 错杀折价 + 收敛收益
- **策略 D: 到期日阶梯（梯子策略）** — 分散到期风险

若选择策略 D，必须包含到期日阶梯表（按到期年份列出可选 Preferred）。

#### 7.11.4 Preferred Shares vs 替代投资品对比

必须包含一张完整对比表：


| 对比项     | Split Fund Preferred | GIC (5年) | 加拿大政府债券 | 公司债券 |
| ------- | -------------------- | -------- | ------- | ---- |
| 典型收益率   |                      |          |         |      |
| CDIC 保障 |                      |          |         |      |
| 流动性     |                      |          |         |      |
| 本金风险    |                      |          |         |      |
| 税务效率    |                      |          |         |      |
| 折价机会    |                      |          |         |      |


必须包含 `[!IMPORTANT]` alert 解释税务优势（合格股息 vs 利息）。

#### 7.11.5 Preferred 风险管理

- 主要风险表（NAV 跌破面值 / 利率风险 / 流动性 / 续期重置 / 集中度）
- Preferred 持有人保护机制（累积分红 / 优先偿还 / 暂停触发 / 赎回权）

#### 7.11.6 Preferred 投资决策速查流程图（可选）

> [!NOTE]
> **流程图为可选**：与 7.10.5 同理，若策略章节已充分覆盖决策逻辑，可省略。如包含，使用以下文本格式:

```text
开始
  │
  ▼
[1] 检查 NAV 资产覆盖率 ──→ < 130%? ──→ ⛔ 不买，本金风险过高
  │
  ▼ ≥ 130%
[2] 检查 DBRS 评级 ──→ 低于 Pfd-3? ──→ ⛔ 不买，信用质量不足
  │
  ▼ ≥ Pfd-3
[3] 计算 YTM ──→ < 当前 GIC 利率 + 1.5%? ──→ ⛔ 风险收益比不够
  │
  ▼ YTM 有吸引力
[4] 检查市价 vs 面值 ──→ 溢价 > 3%? ──→ ⚠️ 等待折价或平价买入
  │
  ▼ 折价或小幅溢价
[5] 利率环境判断:
    ├── 预期加息 ──→ 优选浮动利率（BK / PDV）或短期到期
    └── 预期降息 ──→ 优选固定利率 + 长到期（锁定高利率）
  │
  ▼
[6] 仓位 ──→ 单只 ≤ 15% 固收仓位，同行业 ≤ 30%
  │
  ▼
  ✅ 买入并持有到期
```

### 7.12 高级配置策略章节（必须出现）

必须至少包含以下两个子主题：

#### 7.12.1 Split Fund 60/40 vs 传统 60/40 对比

- 指出 Class A 的隐含杠杆使 "60% Class A + 40% Preferred" 实际相当于 90-120% 股票敞口
- 列出对比表：现金流、牛市、熊市、再平衡红利、税务效率、长期总回报
- 给出推荐比例（根据风险偏好分级）

#### 7.12.2 哑铃策略（Barbell Strategy）— 适合追求长期总收益最大化的投资者

必须包含：

- 战略思想：进攻端（杠杆 ETF / 进取 Class A）+ 防守端（高息低波 Preferred / Pref ETF / 现金等价）
- 防守端选品（按账户类型区分）：
  - 加币账户（TFSA / Non-Reg）：SPLT.TO / PREF.TO / HSAV.TO
  - 美元账户（RRSP）：JAAA / PAAA 等 AAA CLO ETF
- 进攻端选品：
  - 加币（免换汇）：TSPX.TO（3x SPX）/ TQQQ.TO（3x QQQ）
  - 美元原生（RRSP / 大户）：UPRO / TQQQ / SPYU
- 实操战术：阶梯式建仓、5% 带宽再平衡、关闭 DRIP 截留现金、雷达警报触发
- 必须明确给出推荐比例区间（例如 40-50% 进攻 / 50-60% 防守）

> [!CAUTION]
> 哑铃策略章节涉及 3x/4x 杠杆 ETF。Agent 必须明确写出波动率衰减（Volatility Decay）风险、地狱级回撤（10 年牛市样本中可能有 -79% 回撤）、爆仓风险，并指出策略仅适合**风险承受能力极强 + 严格执行纪律**的投资者。不能将其作为通用建议。

### 7.13 当前环境下的 Class A / Preferred 优选思路（必须出现）

必须基于当日宏观和市场数据，给出 3 类选股思路：

1. **稳健底仓优选**（银行 / 综指龙头）— 列出候选 ticker + 筛选条件
2. **困境反转深度价值优选**（高风险/高回报）— 列出候选 ticker + 触发条件
3. **月薪族现金流优选**（纯收息）— 列出候选 ticker + 注意点（ROC 警告）

**必须以"今日筛选执行步骤"结束**(Agent 应基于当日数据填入具体阈值,以下是模板):

```text
1. 淘汰 NAV 安全边际 < 30% 的 Class A
   （注:不同产品停派阈值不同——多数为 $15,PIC.A 为 $25;以"安全边际百分比"筛选才通用）
2. 淘汰处于溢价（市价 > NAV+1%）状态的 Class A
3. 在剩下的标的中,买入折价最深的 2-3 只,确保行业适度分散
   （单一行业 ≤25% 总仓位;单只 ≤10%）
```

### 7.14 关键风险和机会提示

必须用清单方式列出：

- 当日短期交易机会（具体 ticker + 触发条件）
- 6-12 个月中期机会
- 1-3 年以上长期机会
- Preferred 风险
- Class A 风险
- ETF 风险
- 税务和历史数据风险

每个机会和风险都必须引用对应数据，**不允许泛泛而谈**。

### 7.15 长期总收益率最高策略（核心结论章节）

必须给出一个面向长期总收益最大化的策略，但不能伪装成确定性预测。

策略必须区分：

- **绝对总收益最高潜力：** 通常来自折价买入、安全边际高、底层资产长期复利能力强、分红未严重侵蚀 NAV 的 Class A
- **风险调整后总收益：** 通常需要比较高评级 Preferred、期限结构、YTM、税后收益和 ETF 分散化
- **税后总收益：** 必须考虑 eligible dividend、ROC、capital gains、账户类型（TFSA/RRSP/Non-Reg）和 ACB 影响

必须输出：

1. **首选长期策略**（基于当日数据，给出具体配置比例和 ticker 名单）
2. **买入条件**（指标阈值，例如 NAV 安全边际 ≥40%, Preferred 折价 ≥3%）
3. **持有和再平衡规则**（频率 + 触发条件）
4. **卖出或降仓条件**（指标恶化 + 退出阈值）
5. **哪些数据不完整导致策略置信度下降**

> [!IMPORTANT]
> 如果无法核验完整长期分红和税务数据，必须写明"不能精确排名长期历史总收益"，然后用结构化证据给出当前最合理策略。**不允许伪装成精确历史回测结论。**

### 7.16 投资决策流程与风险红线

必须包含完整工作流：

```text
建立 universe → 官网逐只核验 → 记录 As of Date → 计算 NAV/折溢价/YTM → 检查税务和分红质量 → 形成短中长期观点 → 更新汇总表 → 输出机会/风险 → 标注数据缺口
```

风险红线至少包括：

- 不用过期 NAV 判断实时折价。
- 不在明显溢价时追买 Class A。
- 不把 Class A 高分红当成固定收益。
- 不在 NAV 接近停派阈值时盲目摊平。
- 不用缺失分红复投的价格图排名长期收益。
- 不忽略 ROC 对 ACB 和长期 NAV 的影响。
- 不在不了解利率类型（固定 vs 浮动）的情况下买 Preferred。
- 不把 USD-denominated Preferred 放在 Non-Reg 账户而不考虑预扣税。

### 7.17 数据缺口、冲突与后续核验清单

必须显式列出：

- 哪些产品的字段未能从官方核验
- 哪些 ETF 的 T3 税务构成未公布
- 哪些 Preferred 的 outstanding amount / 资产覆盖率仅有最近一期年报数据
- 哪些来源之间存在冲突（例如 TMX 和发行商对成交量/价格的差异）
- 下次更新报告时的优先核验清单

### 7.18 免责声明

必须包含简短免责声明（中文，例如"本报告仅供研究和信息整理，不构成投资建议。投资前请咨询持牌财务顾问"）。

---

### 7.19 产品数据卡模板

每个普通 Split Fund 至少使用以下模板。字段无法核验时保留该行，并写明"未在官方来源核验到"，**不要删除字段**。

```markdown
### N. 产品官方名称

| 项目 | 详情 |
|---|---|
| Issuer |  |
| 产品官网 |  |
| Factsheet / NAV 来源 |  |
| SEDAR+ / 公告来源 |  |
| 投资方向 |  |
| 底层持仓摘要 | 前 5-10 大持仓 + 行业分布 |
| 结构 | Class A + Preferred / 多 Preferred series / 单一持仓 / covered call / 其他 |
| 成立日期 |  |
| Class A / Capital ticker |  |
| Preferred ticker / series |  |
| Unit NAV | 数值 + As of Date + 来源 |
| Class A NAV | 计算值 + 公式 |
| Preferred 面值 / redemption value |  |
| 最新 Class A 市价 | price + bid/ask + volume + retrieved_at + 来源 |
| 最新 Preferred 市价 | price + bid/ask + volume + retrieved_at + 来源 |
| 折价 / 溢价（Class A） |  |
| NAV 安全边际 |  |
| 隐含杠杆 |  |
| 资产覆盖率（Pfd） |  |
| 到期日 / 延期条款 |  |
| Class A 年分红 / 频率 |  |
| Class A 当前分红率（基于市价） |  |
| Class A 近 24 个月分红是否中断 |  |
| Preferred 年分红 / 频率 |  |
| Preferred Current Yield |  |
| Preferred YTM/YTW 估算（含假设） |  |
| 利率规则（固定/浮动/年审） |  |
| 停派阈值 / 覆盖测试 |  |
| DBRS/Morningstar DBRS 评级 | 评级 + 日期 + 来源 |
| 税务构成 | 最新可得年份 + 来源 + 数据完整性 |
| 历史总收益 | 来源 + 是否含分红复投 + 数据完整性 |
| DRIP 是否可用 |  |
| 流动性（日均成交量） |  |
| 数据缺口 |  |
```

产品卡后必须写三段短分析：

```markdown
**Preferred 分析：** current yield、YTM/YTW、资产覆盖率、评级、期限/延期风险、流动性。至少 3 句具体陈述。

**Class A 分析：** 折溢价、NAV 安全边际、隐含杠杆、分红可持续性、停派风险、底层资产质量。至少 3 句具体陈述。

**机会与风险：** 至少各列 2 条，且每条必须引用本产品的数据。
```

### 7.20 ETF 数据卡模板

每个 Split Funds ETF 至少使用以下模板：

```markdown
### N. ETF 官方名称（Ticker）

| 项目 | 详情 |
|---|---|
| Issuer |  |
| 官网 |  |
| 投资目标 |  |
| 持仓类型 | Preferred / Class A / mixed / other |
| 最新 NAV | 数值 + As of Date + 来源 |
| 最新市价 | price + bid/ask + volume + retrieved_at + 来源 |
| 折溢价 / spread |  |
| 分红金额 / 频率 |  |
| 当前分配率 |  |
| MER |  |
| TER |  |
| AUM |  |
| 成立日期 |  |
| 持仓数量 |  |
| 前十大持仓 |  |
| 发行商集中度（前 3 占比） |  |
| Preferred/Class A 比例 |  |
| 到期日集中度 |  |
| 评级集中度 |  |
| DRIP 是否可用 |  |
| 税务构成 | 年份 + 来源 |
| 数据缺口 |  |
```

ETF 卡后必须回答（每个问题 ≥3 句）：

- 它适合替代单只 Preferred、单只 Class A，还是只适合作为分散化工具？
- 费用和分散化是否抵消了挑选单只证券的机会？
- 它更适合短期现金流、中期配置，还是长期底仓？
- 它在哪类账户（TFSA / RRSP / Non-Reg）中最具税务效率？

### 7.21 引用和证据格式

报告中的重要数据必须在同一行或同一段落提供来源，**不要只在文末堆链接**。

推荐格式：

```markdown
Unit NAV 为 $X.XX，截至 YYYY-MM-DD，来源：发行商 NAV 页面（URL）。
最新市价为 $X.XX，bid/ask 为 $X.XX/$X.XX，抓取时间 YYYY-MM-DD HH:MM America/Edmonton，来源：TMX（URL）。
DBRS 评级 Pfd-3 (high)，最新评级日期 YYYY-MM-DD，来源：DBRS Morningstar（URL）。
```

汇总表中的 `数据来源/日期` 字段至少包含来源名称和日期；正文中必须保留可点击链接。

### 7.22 最终报告骨架

最终报告应严格使用以下骨架（顺序可微调，但不可删减），确保详细度达到机构级研报水准：

```markdown
# 加拿大 Split Funds 深度投资研报

> 报告生成日期:
> 数据抓取时间:
> 重要声明:
> 数据时效:

## 1. 执行摘要
## 2. Universe Audit 与数据来源
## 3. 宏观环境与短中长期观点
## 4. 投资方法论与核心公式
## 5. 历史总收益和税务数据警告
## 6. 全市场 Split Funds 产品数据卡
### 6.1 Brompton Funds
### 6.2 Quadravest Capital Management
### 6.3 Mulvihill Capital Management
### 6.4 Middlefield
### 6.5 Ninepoint Partners
### 6.6 Partners Value Split Corp.
### 6.7 Harvest Portfolios
### 6.8 其他当日发现发行商
## 7. Split Funds ETF 独立章节
### 7.1 SPLT.TO
### 7.2 PREF.TO
### 7.3 CLSA.TO
### 7.4 SPFD.TO
### 7.5 其他当日发现 ETF
### 7.6 ETF 横向对比表
## 8. Preferred Shares 全市场汇总对比表
## 9. Class A / Capital Shares 全市场汇总对比表
## 10. Class A 投资策略章节
## 11. Preferred Shares 投资策略章节
## 12. 高级配置策略章节
### 12.1 Split Fund 60/40 vs 传统 60/40
### 12.2 哑铃策略实战
## 13. 当前环境下的优选思路
## 14. 关键风险和机会提示
## 15. 长期总收益率最高策略
## 16. 投资决策流程与风险红线
## 17. 数据缺口、冲突与后续核验清单
## 18. 免责声明
```

---

## 8. 最终质量检查清单

生成报告前必须逐项检查：

### 8.1 文件与结构

- [ ] 报告文件名包含当天日期，格式 `Split-Funds-Report-YYYY-MM-DD.md`
- [ ] 报告抬头包含生成日期、抓取时间、声明、时效说明
- [ ] 报告骨架完整，所有 18 个一级章节都存在

### 8.2 覆盖范围

- [ ] 已先建立 seed universe，并逐项核验是否仍有效
- [ ] Universe Audit 表已填充
- [ ] 每一个 Split Fund 都访问了发行商官网
- [ ] 每一个 Split Funds ETF 都访问了发行商官网，并有独立章节
- [ ] ETF 独立章节至少核验并覆盖 `SPLT.TO`、`PREF.TO`、`CLSA.TO`、`SPFD.TO`，或用官方来源说明其中任何一个已改名、终止、合并或停止交易
- [ ] 已检查 TSX/TMX、发行商公告和 SEDAR+，用于发现最新上市、终止、延期或改名

### 8.3 数据可核验性

- [ ] 每个产品卡都保留来源链接、As of Date、retrieved_at 和数据完整性说明
- [ ] 每个 NAV 都有 As of Date
- [ ] 每个市价都说明价格来源和抓取时间
- [ ] 每个 Preferred series 单独进入 Preferred 汇总表
- [ ] 每个 Class A ticker 单独进入 Class A 汇总表
- [ ] ETF 没有被错误混入普通 Split Fund 产品卡
- [ ] 所有"未核验到"的字段都列出已查来源（≥2 个），未用推定补齐
- [ ] 历史总收益数据说明了是否包含分红复投
- [ ] 税务构成说明了来源和年份，不能核验时明确标注

### 8.4 字段完整度（按 Tier）

- [ ] Universe 中所有 `confirmed_active` 产品都有详细产品卡(`terminated` / `merged` / `redeemed` 的产品在 universe audit 中说明状态即可,不需要产品卡)
- [ ] 不允许"主动跳过 confirmed_active 产品" — 抓取失败也必须有产品卡(标 Tier 1 全"未在官方来源核验到"+ ≥2 个已查来源)
- [ ] 每个产品卡：Tier 1 字段 100% 已核验或显式标"未核验到"
- [ ] 每个产品卡：Tier 2 字段 ≥70% 已核验
- [ ] Tier 3 缺失字段都已列出已查的 ≥2 个来源
- [ ] 每个产品后至少 3 段定性分析（Preferred / Class A / 机会风险）

> [!IMPORTANT]
> **注意:** 报告(Phase 5)只在 Phase 3 全部完成后才写。如果还在多轮中(checkpoint = `PHASE-3-PARTIAL`),**不要写最终报告**——只写 session_summary.md 让用户开下一轮。这条 8.4 检查清单只对完整报告生效。

### 8.5 详细度（结构性）

- [ ] Class A 投资策略章节包含 ≥3 种**操作上彼此独立**的策略
- [ ] Preferred 投资策略章节包含 ≥3 种**操作上彼此独立**的策略
- [ ] 高级配置策略章节包含 60/40 对比 + 哑铃策略实战
- [ ] 当前环境优选思路给出 ≥3 类筛选思路 + ticker 候选
- [ ] Preferred 汇总表后包含 ≥1 组 head-to-head 对比
- [ ] Class A 汇总表后包含 ≥1 组 head-to-head 对比
- [ ] GFM alert 用于真正的关键提示（不强制 5 类各 ≥1 次）

### 8.6 分析质量

- [ ] 短期、中期、长期观点都已经给出，每段 ≥3 句具体分析
- [ ] 每个观点都明确指出对 Preferred / Class A / ETF 的相对吸引力
- [ ] 长期总收益最高策略区分了绝对收益、风险调整后收益和税后收益
- [ ] 长期策略给出具体配置比例和 ticker 名单
- [ ] 隐含杠杆情景表已包含
- [ ] 资产覆盖率分级表已包含
- [ ] Preferred vs GIC vs 国债 vs 公司债对比表已包含
- [ ] (可选) Class A 决策流程图、Preferred 决策流程图

### 8.7 时效性

- [ ] 所有"当前状态字段"（NAV、市价、当前评级、当前 Prime Rate）都是当日核验
- [ ] NAV 滞后 >14 天的产品都已标 "⚠️ Stale NAV"；>30 天的不计算折溢价
- [ ] 所有"历史字段"（历史总收益、过往 T3）都标了来源 + 时间区间 + 数据完整性等级

### 8.8 一致性与免责

- [ ] 汇总表与产品章节中的数字一致
- [ ] 所有关键机会和风险都引用了具体数据，而不是泛泛判断
- [ ] 报告包含"数据缺口、冲突与后续核验清单"
- [ ] 报告最后有免责声明：研究信息，不构成投资建议
- [ ] 所有 USD-denominated 标的（如 PVS.PR.U / .V）的预扣税风险已说明
- [ ] 哑铃策略章节包含杠杆 ETF 风险警告（含 Volatility Decay 和最大回撤）

### 8.9 多轮会话续接（如本轮未完成全部 universe）

- [ ] checkpoint.txt 已更新为 `PHASE-N-PARTIAL` + completed_count / total
- [ ] 工作底稿 JSON 文件已持久化，便于后续会话续接
- [ ] session_summary.md 已写入并含"下一轮启动指令"
- [ ] 向用户输出明确的"⚠️ 本轮未完成 X/Y，请发起下一轮"消息
- [ ] **未在本轮内强行写报告**——报告只在 universe 全部覆盖且 Phase 4 计算完成后写

### 8.10 最大努力核验（Best Effort Verification）

- [ ] 每个 Tier 1 字段都尝试了 ≥3 个来源(主页 + 子页 + SEDAR+/WebSearch);全部失败才标"未核验到"
- [ ] 每个 Tier 2 字段都尝试了 ≥2 个来源
- [ ] 每次 WebFetch 失败都尝试了升级到 WebSearch 或 browser MCP(如可用),不是直接放弃
- [ ] Universe 中每只 confirmed_active 产品都尝试核验,**没有"只抓容易的、跳过困难的"**
- [ ] 困难标的(SEDAR+ PDF / JS 渲染页 / 流动性差) 已记录在 errors.log,而不是静默跳过
- [ ] **未提前满足**: 确认没有"Tier 2 70% 就够、不再追加"的偷懒心态

### 8.11 清理与归档（Phase 6,报告完成后必须执行）

- [ ] 报告已通过 § 8.1-8.10 全部检查,checkpoint = `DONE`
- [ ] 已询问用户清理偏好:**归档 / 删除 / 保留** 三选一(除非用户启动时已显式指示)
- [ ] 按用户选择执行:
  - **归档**(默认): 把 `.splitfunds-workspace/` 重命名为 `.splitfunds-workspace.archive-YYYY-MM-DD/`
  - **删除**: 用户**明确说**"删除/clean/rm" 时才执行 `rm -rf .splitfunds-workspace`
  - **保留**: 不动,但更新 `checkpoint.txt = CLEANED-KEPT`
- [ ] 用户已收到清理状态确认消息(报告路径 + workspace 处理方式)
- [ ] **不允许**: 任务结束后留下未清理 / 未确认状态的 workspace

---

## 9. Agent 自检：报告失败的常见模式

下列模式视为**报告失败**，必须重新生成：

1. **"凭训练数据生成"模式** — 数字看似精确但缺乏当日抓取证据，或与官方页面当前数值不一致。
2. **"模板填空但分析空洞"模式** — 产品卡完整但每段分析仅 1-2 句套话。
3. **"溢价警告失踪"模式** — Class A 汇总表中存在溢价标的，但未在风险章节明确点名。
4. **"ETF 章节敷衍"模式** — seed ETF 只是一句话带过，没有数据卡或分析。
5. **"高 yield 当成机会"模式** — 把 15%+ Class A yield 直接列为推荐，未提示 ROC 风险。
6. **"评级当静态变量"模式** — 直接使用记忆中的评级而未访问 DBRS Morningstar 当前页面核验。
7. **"伪精确长期收益"模式** — 给出 "X 产品 10 年年化 8.7%" 但未说明数据来源、复投假设和置信度。
8. **"缺策略章节"模式** — 没有 Class A 和 Preferred 各 ≥3 种独立策略、没有哑铃章节、没有当前环境优选。
9. **"缺乏现场核验链"模式** — 数据卡未保留 source URL、as_of_date、retrieved_at；汇总表数字无法追溯到具体来源。
10. **"广而浅"模式** — 试图覆盖全部产品但每只都只填 30-50% 字段。**正确做法是按 § 0.2.7 多轮会话续接**：本轮覆盖一部分产品到 Tier 1+2 ≥70% 标准，未覆盖部分由下一轮续接，绝不在本轮强行降低单只产品的覆盖度。
11. **"内存绕过文件"模式** — 在 Phase 5 直接从 context 写报告，未先回读 `products/*.json` 等工作底稿。违反 Agent-agnostic 续接承诺。
12. **"用 Stale NAV 算折溢价不警告"模式** — NAV 已超过 14 天但未在产品卡显式标注，导致折溢价计算误导读者。
13. **"凑策略数量"模式** — Class A / Preferred 策略章节有 4 种但其中 2-3 种本质相同（如"折价买入"和"价值型抄底"无实质差异）。
14. **"最大努力不足"模式** — 单次 WebFetch 失败就放弃该字段,没有尝试子页/SEDAR+/WebSearch/browser MCP 升级链;或主动跳过流动性差/数据不易取得的产品。质量优先于速度——Agent 必须用尽工具能力。
15. **"未清理工作目录"模式** — 报告生成后留下 `.splitfunds-workspace/` 未询问用户处理,直接结束任务。Phase 6 是必须执行的最后一步。
16. **"未询问就删除"模式** — Agent 主动 `rm -rf .splitfunds-workspace` 而没有用户明确确认。**默认必须归档(`mv`)**,只有用户明确说"删除"才能 `rm`。

---

## 10. 风格与语气要求

- **语言：** 中文为主，关键金融术语保留英文（如 NAV, YTM, ROC, MER, DBRS, Pfd-3, eligible dividends, Prime Rate）。
- **语气：** 专业、克制、可核验。**避免营销语言**（"绝佳机会"、"必涨"、"稳赚不赔" 等）。
- **数字精度：** 价格保留 2 位小数；百分比保留 2 位小数；日期使用 ISO 格式 `YYYY-MM-DD`。
- **表格：** 使用标准 Markdown 表格；数值列右对齐；日期/文字列左对齐。
- **链接：** 所有官方来源使用 markdown 链接 `[text](url)`，不要裸 URL。
- **代码块：** 公式、流程图使用 `代码块` 包裹，便于阅读。

---

## 11. 不可省略的特殊处理项

无论 universe 当日如何变化，下列处理项必须出现在报告中。**注意**:下列具体例子(PVS、PIC.A 等)是历史观察,Agent 仍须以当日核验为准——若条款已变更,以当日发行商官网或 SEDAR+ 为准。

1. **Split Funds ETF 独立章节**：第 7.7 节明确要求 ETF 不得混入普通 Split Fund 产品卡。
2. **Universe Audit 表**：第 2.3 节，明确说明覆盖范围、排除项、新增发现。
3. **数据完整性等级**：每个历史收益、税务构成、停派阈值、评级字段都必须标注 High / Medium / Low。
4. **多 Preferred series + 无 Class A 的特殊结构**：例如 Brookfield 关联的 Partners Value Split Corp 历史上**只发行 Preferred Shares、不公开发行 Class A**(以当日 partnersvaluesplit.com 为准);这类标的不能套用普通 Split Share 结构，必须只填 Preferred 相关字段并在产品卡中说明。
5. **USD-denominated Preferred 的税务警告**：例如 PVS.PR.U / PVS.PR.V 等以美元计价的 series(以当日核验为准),必须明确说明在 Non-Reg 账户中可能涉及的美国预扣税处理。
6. **特殊面值结构**：例如历史上 PIC.A 的 Pfd 面值 **$15** + NAV 阈值 **$25**(以当日核验为准),不能套用 $10 默认面值;**计算 Class A NAV、安全边际、隐含杠杆时必须用产品自身的面值和阈值**。
7. **覆盖率 / 停派阈值未公开披露的情况**：必须在产品卡中写"未在官方来源核验到"并列出已查来源 ≥2 个，禁止从同类产品推定。

---

> **本手册版本：** 2026-05-01  
> **修订原则：** 任何对手册的修改都必须保持五大核心原则:
> 1. **零猜测** — 不允许凭训练数据或记忆填充任何字段
> 2. **当日现场核验** — 所有当前状态字段必须当日从官方来源抓取
> 3. **机构级研报详细度** — 不允许偷工减料、广而浅、模板填空
> 4. **最大努力(Best Effort)** — Agent 必须用尽工具能力(WebFetch → WebSearch → browser MCP);质量永远优先于速度
> 5. **任务完整闭环** — 报告生成后必须执行 Phase 6 清理,不留下未处理的工作目录