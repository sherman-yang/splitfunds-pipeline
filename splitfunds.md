# 加拿大分级基金（Split Share Funds / Split Corp）可交易清单与静态站

**文档版本**：v1.0（最终稿）  
**目标读者**：实现者（Codex/工程）、你自己（策略/使用）  
**适用账户**：GitHub 个人免费账户（Free）  

---

## 0. 摘要

本项目构建一个“可交易清单数据库”（文件型、可追溯）与一个“静态网页榜单”（GitHub Pages 托管），每天自动刷新，输出：

- **Class A 榜单**：以“安全垫/折价/到期结构”为核心排序与筛选，展示尽可能完整的结构、估值、分派、回报与流动性信息。
- **Preferred（优先股）榜单**：展示价格、现金分红收益率（实际利分红率）、折价率、年化折价率、剩余年限、成交量、本金等完整信息。

采用你选择的 **方案 A**：

- **私有仓库（pipeline）**：抓取/合并/计算/生成站点产物；包含你的免费 API 与密钥；不公开。
- **公开仓库（site）**：只保存“生成好的静态网页与数据文件”；开启 GitHub Pages。

---

## 1. 约束与假设

### 1.1 GitHub Pages 与账号限制（必须遵守）

- 你是 **GitHub 个人免费账户**：GitHub Pages 可用于 **public 仓库**；若要从 **private 仓库**发布 Pages 通常需要付费计划（Pro/Team/Enterprise）。
- GitHub Pages 为静态站点托管：不支持服务端数据库与服务端逻辑；所有数据与页面必须在 Actions 中“预生成”。
- GitHub Pages 有站点体积、部署超时等限制；因此本项目的发布产物必须精简。
- Git 仓库有单对象文件大小与单次 push 的硬限制；因此历史数据要做分区与裁剪。

### 1.2 数据与市场假设

- Split Corp 常见结构：**1 Unit = 1 股 Class A + 1 股 Preferred**。
- Preferred 的本金（par/redemption）常见为 **10 CAD**，但必须允许不同基金存在不同本金（以条款为准）。
- “停派门槛（Gate）”常见为 Unit NAV < 15（若 PrefPar=10，则约等于 coverage < 1.5x），但不同基金可能不同；必须允许每只基金独立配置/解析。

### 1.3 数据源假设

你提供的免费 API 能提供：

- 实时/最新价格
- 成交量
- 52 周高低
- 多区间 Total Return（1/3/5/10y 等）

发行人/产品页/公告提供：

- Unit NAV、各类股 NAV（如披露）
- 到期日、展期规则
- 分派金额、频率、停派条件
- 其它结构性信息（例如 ROC 说明、税务拆分等，若可获得则纳入）

---

## 2. 项目目标与非目标

### 2.1 目标（必须实现）

1) **每日自动刷新**：GitHub Actions 定时运行，生成并发布静态站。

2) **数据完整性**：对 Class A 与 Preferred 均输出“尽可能全”的字段（见第 4 章）。

3) **派生指标**：在原有派生指标上新增并统一实现：

- **折价率**（Class A 与 Preferred）
- **年化折价率**（Class A 与 Preferred）
- **剩余年限**（Class A 与 Preferred）
- **成交量**（动态字段）

4) **网页 UI**：单站点 `index.html`，包含两个 Tab：

- Tab A：Class A
- Tab P：Preferred

两张表格均需在浏览器端支持：排序、搜索、过滤、列显示开关、导出。

5) **可扩展**：发行人适配器（adapter）可逐个新增，且不会破坏现有数据结构。

### 2.2 非目标（本期不做/不承诺）

- 不做实时流式更新（只做每日批处理；可额外支持手动触发）。
- 不承诺完全覆盖所有 Split Corp（先覆盖主流发行人/可交易标的；通过 TSX 列表发现与扩展）。
- 不提供投资建议；输出仅用于研究与信息展示。

---

## 3. 总体架构（方案 A：私有 pipeline + 公开 site）

### 3.1 仓库划分

#### Repo 1：`splitfunds-pipeline`（私有）

职责：

- 拉取你的免费 API（价格/成交量/52w/回报）
- 抓取发行人页面/公告（NAV/条款/分派/到期等）
- 归一化与校验
- 计算派生指标与评分
- 生成静态站点产物（HTML + JSON/CSV）
- **推送产物到公开 repo**（仅推送产物，不推送任何密钥、抓取逻辑可选择不公开）

Secrets（必须）

- `PERF_API_KEY`（你的 API key，如果需要）
- `PUBLIC_REPO_PAT`（fine-grained PAT，仅允许写入公开 repo）

#### Repo 2：`splitfunds`（公开）

职责：

- 保存静态站点产物
- 开启 GitHub Pages

内容仅包含：

- `index.html` 与前端资源
- `data/latest.json`（以及可选的 `data/latest.csv`）
- （可选）`data/history_last_365d.json`（仅最近 365 天关键字段，用于图表/趋势；不要发布全历史）

### 3.2 数据流（每日批处理）

1) **Universe 发现**：从 TSX/发行人列表获取可交易 split corp 清单（或至少维护一个主列表并支持增量发现）。
2) **行情与回报**：调用你的免费 API 获取当日价格、成交量、52w 高低、1/3/5/10y total return。
3) **结构与 NAV**：抓取发行人披露的 Unit NAV、各自 NAV、到期日、展期、分派与停派门槛文本。
4) **归一化**：统一字段、日期、货币、频率与缺失处理。
5) **校验与异常标记**：对异常值/缺失字段打标签，生成 run report。
6) **派生指标与评分**：计算折价、年化折价、杠杆、覆盖率、安全垫、剩余年限、score。
7) **生成静态站产物**：输出 JSON/CSV + 渲染 HTML。
8) **发布**：推送到公开 repo，触发 Pages 部署（或直接由 site repo 的 workflow 部署）。

---

## 4. 数据模型与字段规范（Schema）

> 设计原则：**“一行一证券”**（row-per-security），前端按 `security_type` 分到两个 Tab。这样最利于排序、过滤、导出与扩展。

### 4.1 统一主键与枚举

- `fund_id`：Split Corp 的 base 标识（通常用基础 ticker，如 `DFN`、`LBS`）
- `security_type`：`CLASS_A` 或 `PREFERRED`
- `ticker`：证券 ticker（`DFN` 或 `DFN.PR.A`）
- `asof`：抓取时间戳（ISO8601，UTC）

### 4.2 静态/低频字段（条款/结构）

- `issuer_manager`：发行人/管理人（Brompton / Quadravest / Middlefield / Harvest / …）
- `theme`：主题/标的简介（如“加拿大金融股息组合”“全球股息增长”等）
- `holdings_hint`：持仓/标的提示（可选：top holdings 列表摘要）
- `maturity_date`：到期/终止日（ISO date）
- `extendable`：是否可展期（bool）
- `extend_terms_text`：展期条款摘要（可选）

**优先股本金与门槛**

- `pref_par`：优先股本金/票面（CAD，常见 10；以条款为准）
- `gate_nav`：触发 Class A 停派/保护条件的 Unit NAV 门槛（若可解析；否则可配置默认）
- `gate_rule_text`：停派/保护规则文本摘要

### 4.3 动态字段（每日更新）

**行情与流动性（来自你的免费 API 优先）**

- `price`：最新价或收盘价（需在 `price_kind` 标记来源/口径）
- `volume`：当日成交量（股数）
- `high_52w`：52 周最高
- `low_52w`：52 周最低
- `price_asof`：价格时间戳（若 API 提供）

**回报（Total Return）**

- `tr_1y` / `tr_3y` / `tr_5y` / `tr_10y`：百分比（以小数存储，如 0.154 表示 15.4%）
- `tr_method`：回报口径说明（例如 total return / price return；由你的 API 定义）

**NAV（发行人披露优先）**

- `unit_nav`：Unit NAV（1A + 1Pref 对应净值）
- `nav_self`：该证券的自身 NAV（Class A 的 NAV 或 Preferred 的 NAV，若发行人披露）
- `nav_asof_date`：NAV 日期

**分派（尽量结构化）**

对 Class A：

- `dist_amt`：每期分派金额
- `dist_freq`：`monthly`/`quarterly`/`other`
- `dist_status`：`paying`/`suspended`/`unknown`
- `roc_flag`：是否含 ROC（bool/unknown）
- `roc_ratio`：ROC 占比（若可得）

对 Preferred：

- `pref_div_amt`：每期固定分红/股息金额
- `pref_div_freq`：`monthly`/`quarterly`/`other`
- `pref_yield_issue`：发行文件给出的发行收益率（若可得）

**来源标记（每行/每字段至少要有行级）**

- `source_price`：如 `your_api`
- `source_nav`：如 `issuer`
- `source_terms`：如 `issuer`/`rating_report`

---

## 5. 派生指标（Derived Metrics，含新增项）

> 所有百分比建议**以小数存储**（0.061 -> 6.1%）。

### 5.1 基础结构指标（fund 级，按 row 复制）

设：

- `UnitNAV = unit_nav`
- `PrefPar = pref_par`

则：

- **安全垫（Cushion）**
  - `cushion = UnitNAV - PrefPar`
- **覆盖率（Coverage）**
  - `coverage = UnitNAV / PrefPar`（PrefPar>0）
- **到门槛距离（Distance to Gate）**
  - `distance_to_gate = UnitNAV - gate_nav`（gate_nav 可用时）

### 5.2 Class A 残值与杠杆

- **Class A 内在残值（结构内在价值）**
  - `classa_intrinsic = max(UnitNAV - PrefPar, 0)`

- **理论杠杆（结构弹性）**（当 UnitNAV > PrefPar）
  - `leverage_th = UnitNAV / (UnitNAV - PrefPar)`

- **交易杠杆（含折价/溢价影响的近似）**
  - `leverage_mkt ≈ UnitNAV / price`（price>0）

### 5.3 折价率（新增：Class A 与 Preferred 都要）

> 折价率统一定义：**正数 = 折价（discount）**，负数 = 溢价（premium）。

#### 5.3.1 对自身 NAV 的折价（若有 nav_self）

- `discount_to_nav = (nav_self - price) / nav_self`（nav_self>0）

#### 5.3.2 Preferred 对本金（Par）的折价（强烈建议永远计算）

- `discount_to_par = (pref_par - price) / pref_par`（pref_par>0）

#### 5.3.3 Class A 对结构残值（Intrinsic）的折价（强烈建议永远计算）

- `discount_to_intrinsic = (classa_intrinsic - price) / classa_intrinsic`（classa_intrinsic>0）

> 若 `classa_intrinsic <= 0`，该指标设为 `null`，并标记风险：`flag_intrinsic_le_0=true`。

### 5.4 年化折价率（新增：Class A 与 Preferred 都要）

核心定义：在剩余年限 T 内，假设价格向某锚点 Anchor 收敛，则折价带来的“年化回报贡献”为：

- `annualized_pull = (Anchor / Price)^(1/T) - 1`

其中：

- `T = years_to_maturity`（建议用 **years_to_first_maturity**，见 5.5）

#### 5.4.1 Preferred：默认锚点 = Par

- `annualized_discount_to_par = (pref_par / price)^(1/T) - 1`

#### 5.4.2 Class A：默认锚点 = Intrinsic

- `annualized_discount_to_intrinsic = (classa_intrinsic / price)^(1/T) - 1`

#### 5.4.3 可选高级锚点：NAV

- `annualized_discount_to_nav = (nav_self / price)^(1/T) - 1`

**边界处理（必须一致）：**

- 若 `T <= 0` 或缺失：年化折价率 = `null`
- 若 `Anchor <= 0` 或缺失：`null`
- 若 `price <= 0`：`null`
- 若 `extendable=true`：默认 `T` 取 **years_to_first_maturity**，并在 UI 显示 “可展期/不确定” 标记。

### 5.5 剩余年限（新增：Class A 与 Preferred 都要）

- `years_to_maturity = (maturity_date - today)/365.25`

若 `extendable=true`，建议额外输出：

- `years_to_first_maturity`：按当前披露到期日
- `years_to_final_maturity`：若条款可计算最大展期范围则输出，否则置空

### 5.6 优先股“实际利分红率”（必须）

Preferred 的“实际利分红率”建议使用 **current yield**：

- `pref_div_cash_annual = pref_div_amt * payments_per_year`
- `pref_yield_current = pref_div_cash_annual / price`

其中 `payments_per_year` 由 `pref_div_freq` 映射：

- monthly -> 12
- quarterly -> 4

若某基金的 preferred 分红并非固定或存在特殊条款，需在 `pref_div_kind` 标记。

---

## 6. 网页（静态站）需求：两个 Tab（Class A / Preferred）

### 6.1 页面结构

- 单页面：`index.html`
- 顶部 Tab：
  - `Class A`
  - `Preferred`

### 6.2 表格通用能力（两 Tab 都要）

- 浏览器端排序（数值、字符串、日期）
- 全局搜索（ticker / manager / theme）
- 条件过滤（范围过滤、布尔过滤）
- 列显示开关（默认列 + 高级列）
- 导出 CSV（当前筛选/排序后的结果）
- 显示更新时间：`asof`
- 行级风险标记（badge/颜色/tooltip）：
  - near_gate（距离门槛太近）
  - nav_missing
  - intrinsic_le_0
  - dist_suspended
  - low_liquidity

### 6.3 Class A Tab：默认列（首屏必备）

1) 基础识别
- `ticker`
- `issuer_manager`
- `theme`

2) 行情/流动性
- `price`
- `volume`
- `high_52w` / `low_52w`

3) 结构与安全
- `unit_nav`
- `pref_par`
- `coverage`
- `cushion`
- `gate_nav`、`distance_to_gate`

4) 估值与折价（新增）
- `classa_intrinsic`
- `discount_to_intrinsic`
- `annualized_discount_to_intrinsic`

5) 期限（新增）
- `years_to_(first_)maturity`

6) 分派与回报
- `dist_amt` / `dist_freq` / `dist_status`
- `tr_1y` / `tr_3y` / `tr_5y` / `tr_10y`

7) 排名
- `score_conservative`
- `score_aggressive`

### 6.4 Preferred Tab：默认列（你要求必须齐）

1) 基础识别
- `ticker`
- `issuer_manager`
- `theme`

2) 行情/流动性（新增成交量）
- `price`
- `volume`
- `high_52w` / `low_52w`

3) 本金与票息
- `pref_par`（本金）
- `pref_div_amt` / `pref_div_freq`

4) 实际利分红率（必须）
- `pref_yield_current`

5) 折价与年化折价（必须）
- `discount_to_par`
- `annualized_discount_to_par`

6) 剩余年限（必须）
- `years_to_(first_)maturity`

7) 风险刻度（推荐默认显示）
- `unit_nav`
- `coverage`

### 6.5 高级列（可勾选显示）

- `nav_self`
- `discount_to_nav`
- `annualized_discount_to_nav`
- `leverage_th` / `leverage_mkt`（Class A）
- `pref_yield_issue`（Preferred）
- `gate_rule_text`
- `extendable` / `extend_terms_text`
- `source_price` / `source_nav` / `source_terms`

### 6.6 前端数据加载方式

- 静态站内放置：`data/latest.json`
- 页面加载后：
  - `fetch('data/latest.json')`
  - `rows.filter(security_type === 'CLASS_A')` -> Class A Tab
  - `rows.filter(security_type === 'PREFERRED')` -> Preferred Tab

---

## 7. 排名模型（Class A 核心筛选）

> Preferred 页以信息展示为主；是否也做 Preferred 排名可作为后续增强。

### 7.1 两套 preset

#### 7.1.1 保守（Conservative）

Hard filters（不满足直接剔除）：
- `coverage >= 1.8`
- `distance_to_gate >= 2.0`（gate 可用时）
- `classa_intrinsic > 0`

Score 权重（示例，总分 100）：
- 安全：45（cushion/coverage/distance_to_gate）
- 估值：30（discount_to_intrinsic）
- 到期：15（偏好 1–3 年）
- 成本：10（pref_yield_current 或 pref_yield_mkt 作为资金成本刻度，可选）

#### 7.1.2 激进（Aggressive）

Hard filters：
- `coverage >= 1.6`
- `distance_to_gate >= 0.5`
- `classa_intrinsic > 0`

Score 权重（示例）：
- 安全：35
- 估值：40
- 到期：15
- 成本：10

### 7.2 可解释性

每条 Class A 行最好输出：

- `score_total_*`
- `score_components`（分项）
- `flags[]`（near_gate、low_liquidity、intrinsic_le_0 等）

---

## 8. 文件型“数据库”（方案 A 存储）

### 8.1 最小存储（推荐 MVP）

- 仅输出 `latest.json`（站点也仅发布它）

优点：

- 体积极小
- 几乎不会触及 GitHub 文件限制/Pages 体积限制

### 8.2 轻量历史（推荐 v1.1）

目的：支持趋势展示、异常检测、策略信号（折价均值回归等），但不让仓库膨胀。

**存储策略：按月分区**

- `data/history/2026-01.csv`
- `data/history/2026-02.csv`
- …

每行存“关键字段”即可（避免把全部字段每天 commit）：

- `asof`, `ticker`, `security_type`, `price`, `volume`, `unit_nav`, `nav_self`, `coverage`, `cushion`, `discount_to_intrinsic/discount_to_par`, `score_*`

**站点发布策略**

- 只发布：`history_last_365d.json`（可选）
- 不发布全历史（避免 Pages 站点体积增长）

---

## 9. 数据源与适配器（Adapters）

### 9.1 数据源优先级（建议默认）

- 价格/成交量/52w/区间回报：你的免费 API（优先）
- NAV/条款/分派/到期：发行人页面（优先）
- 回报 fallback：Middlefield fund list（当 API 缺某些 ticker 时）
- Universe 发现：TSX/交易所发行人列表（用于发现新增/退市/名称变化）

### 9.2 适配器统一输出契约（强烈建议）

每个 adapter 返回同一结构：

- `fund_level`：`fund_id`, `maturity_date`, `extendable`, `pref_par`, `gate_nav`, `gate_rule_text`, `theme`...
- `securities[]`：
  - 每条证券：`security_type`, `ticker`, `nav_self`, `dist terms`, `pref_div terms`...
- `asof` / `source`

pipeline 最终做合并：

- 以 `ticker` 为 key 合并行级数据
- 以 `fund_id` 合并 fund-level 字段并广播到两条证券行

### 9.3 冲突解决与溯源

- 每行至少保留：`source_price`, `source_nav`, `source_terms`
- 若字段冲突：按优先级覆盖，并在 `notes` 或 `field_sources` 记录差异

---

## 10. 校验与异常检测（必须做）

每次运行输出 `run_report.json`（可不发布到站点，留在私有 repo）。

### 10.1 必做校验

- `price <= 0` -> invalid
- `pref_par <= 0` -> invalid
- `unit_nav <= 0` -> invalid 或 missing
- `coverage < 1.0` -> 高风险或数据错误（标记）
- `discount_*` 极端值（例如 > +80% 或 < -50%）-> 标记
- `volume` 缺失 -> `liquidity_unknown`

### 10.2 变化率异常

- `unit_nav` 日变动 > ±10%（无公告时）-> 标记
- `price` 日变动 > ±20% -> 标记

### 10.3 门槛与停派风险标记

- `distance_to_gate < 1.0` -> `near_gate`
- 若能解析到 `dist_status=suspended` -> `dist_suspended`
- `classa_intrinsic <= 0` -> `intrinsic_le_0`

---

## 11. GitHub Actions 设计

### 11.1 私有 repo（pipeline）工作流：每日刷新 + 推送到公开 repo

触发：

- `schedule`（每日一次）
- `workflow_dispatch`（手动）

步骤：

1) checkout 私有 repo
2) 安装依赖
3) 运行 `refresh.py` 生成 `site/` 产物
4) 使用 `PUBLIC_REPO_PAT` checkout 公开 repo 到 `./public_repo`
5) 将 `site/` 同步到公开 repo（覆盖旧文件）
6) commit & push

注意：

- cron 使用 UTC
- 避开整点（例如 `17 15 * * *`）

### 11.2 公开 repo（site）工作流：部署 Pages

两种模式（二选一）：

- **模式 A**：site repo 仅靠 Pages “从分支发布”（简单；但你要确保输出位置正确）
- **模式 B（推荐）**：自定义 Actions workflow：upload artifact -> deploy pages（更可控）

---

## 12. 公开站点内容与安全

- 公开站点/公开仓库 **不得包含**：
  - API key、token
  - 抓取逻辑细节（如果你不想公开，可只公开产物）
  - 任何可被滥用的接口细节

- 公开站点应包含免责声明（footer）：
  - 信息仅供研究；不构成投资建议
  - 数据可能延迟/错误

---

## 13. 目录结构（建议落地）

### 13.1 私有 repo：`splitfunds-pipeline`

```
./
  scripts/
    refresh.py
    adapters/
      api_provider.py
      issuer_brompton.py
      issuer_quadravest.py
      issuer_middlefield.py
      tsx_universe.py
    compute_metrics.py
    scoring.py
    validate.py
    sitegen/
      render_index.py
      templates/
        index.html.j2
  config/
    sources.yaml
    scoring.yaml
    universe.yaml
  site/
    index.html
    assets/
      app.js
      app.css
    data/
      latest.json
      latest.csv
      history_last_365d.json  # 可选
  data/
    history/
      2026-01.csv
  .github/workflows/
    refresh-and-publish.yml
  README.md
```

### 13.2 公开 repo：`splitfunds`

```
./
  index.html
  assets/
    app.js
    app.css
  data/
    latest.json
    latest.csv
    history_last_365d.json  # 可选
  .github/workflows/
    deploy-pages.yml         # 若用自定义部署
  README.md
```

---

## 14. 验收标准（Definition of Done）

### 14.1 数据与计算

- 每日生成 `data/latest.json` 且包含两类证券行（Class A + Preferred）。
- 每行包含：price、volume、52w high/low、remaining term、折价率、年化折价率（按本规范定义）。
- Class A 行包含：unit_nav、coverage、cushion、intrinsic、distance_to_gate、scores。
- Preferred 行包含：pref_par、pref_yield_current、discount_to_par、annualized_discount_to_par。

### 14.2 网页

- 单页面两个 Tab，切换无刷新。
- 表格支持：排序、搜索、过滤、列开关、导出 CSV。
- 页面显示最后更新时间 `asof`。
- 风险标记正常（near_gate、intrinsic_le_0、nav_missing、low_liquidity 等）。

### 14.3 部署

- Actions 每天自动运行并更新公开站点。
- 公开站点可通过 GitHub Pages URL 正常访问。
- 公开仓库不包含任何 secrets。

---

## 15. 后续增强（Roadmap）

- v1.1：详情页（单 ticker），展示 365 天折价/Unit NAV/score 趋势图（只发布轻量历史）。
- v1.2：事件流（展期公告、分派变更、停派恢复），以及条款抽取器（自动识别 gate/展期）。
- v1.3：Preferred 的 IRR/到期收益率近似（在更完善条款与现金流规则下）。

---

## 16. 附录：关键公式速查

- `cushion = unit_nav - pref_par`
- `coverage = unit_nav / pref_par`
- `classa_intrinsic = max(unit_nav - pref_par, 0)`
- `discount_to_intrinsic = (classa_intrinsic - price) / classa_intrinsic`
- `discount_to_par = (pref_par - price) / pref_par`
- `annualized_discount = (Anchor/Price)^(1/T) - 1`
- `years_to_maturity = (maturity_date - today)/365.25`
- `pref_yield_current = (pref_div_amt * payments_per_year) / price`
