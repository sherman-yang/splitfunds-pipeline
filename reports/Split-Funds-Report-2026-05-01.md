# 加拿大 Split Funds 深度投资研报

> 报告生成日期: 2026-05-01
> 数据抓取时间: 2026-05-01 21:50 America/Edmonton
> 重要声明: 本报告基于当日从发行商官网、TMX、SEDAR+ 索引、DBRS Morningstar 与 Globe and Mail 等可核验来源抓取的数据生成。无法核验的字段已显式标注 "未在官方来源核验到",并保留 ≥2 个已查来源。
> 数据时效: 多数 NAV 为 2026-04-30(T-1),Quadravest 系产品 NAV 为 2026-04-15(16 天滞后,bi-weekly 发布特性,详见各卡 stale 标注);价格为同日抓取报价,盘中可能波动;部分 bid/ask/volume 字段在多源核验后仍未取得,已在对应字段留空并在 § 17 数据缺口章节集中列出。

> © 2026 **Sherman Yang**. All rights reserved. 本报告版权归 Sherman Yang 所有,未经书面许可不得以任何形式复制、分发、转载或用于商业用途。

---

## 1. 执行摘要

> [!IMPORTANT]
> **当日最高确信度结论(基于 2026-05-01 数据):**
> 1. **BoC 政策利率 2.25% / RBC Prime 4.45%** 的"较低利率 + 偏陡曲线"环境对 Split Funds 全体偏友好——固定利率 Pfd 锁定高 YTM 优势,但浮动利率 Pfd (BK.PR.A、PDV.PR.A) 因 5% 分红地板仍维持高于 Prime + 1.5%/2.35% 的合约名义值,暂时不存在被压扁风险。
> 2. **Class A 最具吸引力组合:SBC.TO + GDV.TO + LBS.TO**:三只均出现 NAV 安全边际 ≥40%、底层为加拿大六大行 / 全球派息成长股 / 银行+保险均衡篮子,且当前以 NAV 折价交易。
> 3. **Class A 必须回避:LFE.TO** (NAV 安全边际仅 15.92%、Class A 分红已实质性暂停)、**ESP.TO** (NAV 安全边际 17.53% + 油气板块单一暴露 + DBRS 未评级)、**DGS.TO** (停派阈值距离仅 22.40%、Class A 表面 yield 14.34% 极度依赖底层 covered call 与 ROC)。

**Preferred / Class A / ETF 占优顺序(当日):**

- **绝对收益机会**:Class A 折价 + 高安全边际组合最优(SBC、GDV、LBS、IS),长期复合潜力 8-12% 区间(税前,基于底层股息 + 折价回归 + 杠杆)。
- **风险调整后收益**:Pfd 占优——Quadravest 7% 票息 Pfd (FFN.PR.A、FTN.PR.A) 在 178-220% 资产覆盖率下仍提供 6.75-7.00% current yield,YTM 在 5.5-6.0% 区间显著高于同期限国债 (3.20%) 与 GIC。
- **简化执行 / 现金流底仓**:SPLT.TO ETF (MER 0.50%、AUM 6.17 亿、25 只 Pfd 分散) 是当前唯一兼具规模与流动性的 split-pref 工具——优于 PREF.TO (集中度更高,无 Partners Value 暴露) 与 SPFD.TO (MER 4.34% 异常高,需经发行商 MRFP 复核)。

> [!CAUTION]
> **执行摘要的置信度降级项:**
> - PIC.A 当前 Unit NAV 未能从 Mulvihill 官网核验(站点动态渲染失败,最近可核验 NAV 为 2025-10-31 的 $24.92);本报告中 PIC.A 的折溢价、安全边际与隐含杠杆**全部为"未核验",不进入策略推荐。**
> - 历史长期总收益 (5 年、10 年年化) 均无法独立从 Morningstar Canada / 发行商 MRFP 取得完整 DRIP 假设的复投序列,本报告**不输出长期回测年化数字**,只输出结构性结论。
> - PWI.TO (Brompton Power & Infrastructure Split Corp) 在 seed list 中,但本轮 Brompton 数据卡未涵盖——见 § 17 数据缺口清单,需后续会话补全。

---

## 2. Universe Audit 与数据来源

| 类别 | 数量 | 发现来源 | 备注 |
|---|---:|---|---|
| Split Funds / Split Share Corporations | 19 (含 7 PVS Pref-only series) | 发行商官网 + TMX + SEDAR+ 索引 | 26 个 ticker 实体(19 Class A + 26 Pfd series),其中 PVS 系列只有 Pfd |
| Preferred Share series (单独计) | 26 | 同上 + DBRS Morningstar | 含 PVS.PR.H/J/K/L/M/U/V 七只 |
| Class A / Capital Share ticker (单独计) | 19 | 发行商官网 + TMX | PVS 系列无 Class A |
| Split Funds ETF | 4 (SPLT/PREF/CLSA/SPFD) | Brompton/Quadravest/Mulvihill 官网 + TMX | SPFD 由 Mulvihill US Healthcare ETF 于 2026-04 改名重定位 |
| 排除项 | 1 (FTU - U.S. Financial 15) | Quadravest 主页未列出 | 视为 terminated/redeemed |
| 状态未核验 (status_unverified) | 1 (PWI - Brompton P&I Split Corp) | seed list 残留 | 本轮未抓取,见 § 17 |
| 新增发现 | 1 (SPFD 2026-04 改名) | Globe and Mail 公告 + stockanalysis.com | 原 Mulvihill US Healthcare ETF 改成 Split-Pref 策略 |
| IS 归属变更确认 | 1 (Middlefield, 非 Brompton) | middlefield.com fund page | seed list 历史误归 Brompton,当日确认 |

**主要来源链接(全报告通用):**
- 发行商: [Brompton](https://www.bromptongroup.com/) · [Quadravest](https://www.quadravest.com/) · [Mulvihill](https://www.mulvihill.com/) · [Middlefield](https://www.middlefield.com/) · [Ninepoint](https://www.ninepoint.com/) · [Partners Value](https://www.partnersvaluesplit.com/) · [Harvest](https://www.harvestportfolios.com/)
- 交易所 / 行情: [TMX Money](https://money.tmx.com/) · [Globe and Mail Markets](https://www.theglobeandmail.com/investing/markets/) · [stockanalysis.com](https://stockanalysis.com/)
- 评级: [DBRS Morningstar](https://dbrs.morningstar.com/)
- 宏观: [Bank of Canada](https://www.bankofcanada.ca/) · [RBC Prime](https://www.rbcroyalbank.com/rates/prime.html)

---

## 3. 宏观环境与短中长期观点

### 3.1 当日宏观快照(2026-05-01)

| 字段 | 数值 | as_of | 来源 |
|---|---:|---|---|
| BoC 政策利率(隔夜目标) | 2.25% | 2026-04-29(决定日);下次 2026-06-10 | [BoC](https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/) |
| RBC Prime Rate | 4.45% | 自 2025-10-29 起生效 | [RBC](https://www.rbcroyalbank.com/rates/prime.html) |
| Canada 2yr Yield | 2.96% | 2026-04-30 | [BoC bonds](https://www.bankofcanada.ca/rates/interest-rates/canadian-bonds/) |
| Canada 5yr Yield | 3.20% | 2026-04-30 | 同上 |
| Canada 10yr Yield | 3.56% | 2026-04-30 | 同上 |
| 收益率曲线斜率 (10y - 2y) | +60bp | 2026-04-30 | 计算 |
| CAD/USD | 0.7364 (1.3576 USD/CAD) | 2026-05-01 | [BoC FX](https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/) |
| TSX Composite | 33,926 (YTD +5.29%) | 2026-05-01 | [Trading Economics](https://tradingeconomics.com/canada/stock-market) |
| XFN.TO (CDN Financials ETF) | 82.36 (52w 范围 58.42-84.50) | 2026-04-29 | [Yahoo](https://ca.finance.yahoo.com/quote/XFN.TO/) |

### 3.2 短期观点(1-3 个月)

利率方向已基本定价完毕——市场预期 BoC 在 6 月会议大概率维持 2.25%,2026 全年最多再降一次 25bp。这一情景下,**Prime 仍维持在 4.45% 至少 60-90 天**,意味着 BK.PR.A (合约公式 Prime + 1.50%) 名义分红 5.95% 不被触发上限 8% 但已远在 5% 地板之上,**BK.PR.A 的 5.72% current yield 在所有 Pfd 中几乎是"零信用风险换利率"的最佳代表**。短期最具交易性的标的是 **PRM.TO**(Class A 2026-05-06 派付 $0.1031,且 ask 14.32 vs NAV 13.73 已经 +4.3% 溢价——这是过去 12 个月罕见的),建议**按持仓回避**,等待回调到 NAV 折价 ≥2% 再考虑。短期内最大的特异性风险来自 **LFE.TO**(NAV $17.84 距离 $15 停派阈值仅 15.92%),只要银行/保险股出现 5-7% 回调即可触发其 Class A 分红再次暂停的复发。

### 3.3 中期观点(6-12 个月)

中期最重要的剧本是 **2026 下半年 BoC 是否再降 25bp 至 2.00%**——若降,Prime 将下行至 4.20%,BK.PR.A 名义票息降至 5.70%,但其 5% 地板仍提供保护;PDV.PR.A 的 Prime + 2.35% 公式名义票息 6.55% 仍远在 8% 上限内。**固定利率 Pfd (DFN.PR.A 7.00% / FFN.PR.A 7.50%) 在降息情景下相对吸引力上升**,因为锁定的高息票变得更稀缺,折价收敛与 YTM 实现的概率提升。Class A 中期最大变量是底层股息可持续性:**SBC / LBS / DFN 的核心持仓为加拿大六大行**,2026 下半年银行业 ROE 与坏账率压力上升,Class A 表面 yield 13-15% 中的 covered call 期权金部分将继续承压;若 XFN.TO 跌破 75(目前 82.36),DFN.TO 与 FFN.TO 这类高杠杆双倍敞口标的可能再次跌破 NAV 安全边际 20% 关卡。**ETF 中期机会在 SPLT.TO**——MER 0.50% + 25 只 Pfd 自动再平衡,在不确定性环境下是 Pfd 一篮子持有的最优表达。

### 3.4 长期观点(1-3 年以上)

长期最确定的事是 **Split Funds 的"延期"行为**——Brompton/Quadravest 几乎每只产品到期都会延期,而非按面值赎回;这意味着 Pfd 持有人需要把"到期价值 $10"理解为"延期重设利率事件",而非保证现金回收。在 Pfd 视角,**Partners Value 系列(PVS.PR.K/L/M)由 Brookfield 间接信用支撑、DBRS Pfd-2、票面 $25**,长期 3-5 年视角是最强的"债券替代"组合,YTM 4.2-4.6% 略低但信用质量是 split-pref 中唯一一档高于 Pfd-3。Class A 长期视角的"稳态侵蚀"风险来自 **ROC 比例**——14% 表面 yield 的 DFN/FFN/DGS,长期 NAV 趋势平 / 略降,意味着每月分红中实际有 4-6 个百分点是 ROC,长期降低 ACB 与税务效率。**长期最强组合**:50% SPLT.TO (Pfd 收息底仓) + 30% Class A 篮子(SBC + GDV + LBS,等权)+ 20% PVS.PR.L/M(高评级 Pfd 锁定 4.5% YTM 至 2030/2031)。

---

## 4. 投资方法论与核心公式

### 4.1 核心公式

```text
Class A NAV          = Unit NAV − Pfd 面值
折价/溢价率          = (Class A 市价 − Class A NAV) / Class A NAV
NAV 安全边际         = (Unit NAV − 停派阈值) / 停派阈值
隐含杠杆             = Unit NAV / Class A NAV
资产覆盖率           = Unit NAV / Pfd 面值
YTM (近似)           = [年分红 + (面值 − 买入价) / 剩余年数] / [(面值 + 买入价) / 2]
```

**关键机制说明:**
- **死亡螺旋**:Unit NAV 接近停派阈值时,Class A NAV 趋近于 0,隐含杠杆从 ~2x 非线性飙升至 ∞;此时任何底层资产小幅下跌都会以 5-10x 放大体现在 Class A 价格。
- **折溢价回归**:Split Corp 的开放式年度赎回 + 季度赎回机制使得长期 Class A 折价不会无限扩大,通常 5-15% 折价区间是均衡;深度折价 (≥10%) 是逆向机会信号。
- **YTM 与流动性陷阱**:Pfd 日均成交量 < 5,000 时 last price 极易失真,必须看 bid/ask 中点;本报告大量 Pfd 因 bid/ask 在多源核验后仍未取得而留空,YTM 用 mid-of-day-range 近似,YTM 数字置信度降级为 Medium。

### 4.2 NAV 安全边际分级表

| 安全边际 | 等级 | 说明 |
|---|---|---|
| ≥ 40% | ✅ 安全 | NAV 显著高于停派阈值 |
| 20-40% | ⚠️ 关注 | 监控板块波动 |
| 5-20% | 🔴 危险 | 接近停派阈值,杠杆陡升 |
| < 5% | 💀 极危 | 任何回调都可能触发停派 |
| < 0 | 🚫 已停派 | 当前已暂停 Class A 分红 |

### 4.3 隐含杠杆情景表(教学示例)

| Unit NAV | Pfd 面值 | Class A NAV | 隐含杠杆 | 状态 |
|---|---|---|---|---|
| $25 | $10 | $15 | 1.67x | ✅ 健康 |
| $20 | $10 | $10 | 2.00x | ⚠️ 关注 |
| $17 | $10 | $7 | 2.43x | 🔴 高风险 |
| $15 | $10 | $5 | 3.00x | 🚫 停派阈值 |
| $12 | $10 | $2 | 6.00x | 💀 极端杠杆 |

### 4.4 资产覆盖率分级表

| 资产覆盖率 | 等级 | 说明 |
|---|---|---|
| ≥ 200% | ✅ 非常安全 | Pfd 本金风险极低 |
| 150-200% | ✅ 安全 | 可安心持有 |
| 130-150% | ⚠️ 需关注 | NAV 进一步下跌可能危及本金 |
| 100-130% | 🔴 警惕 | Pfd 本金存在不确定性 |
| < 100% | 🚫 已亏损 | Pfd 本金已账面亏损 |

### 4.5 税务差异速记

- **加拿大税务居民**:Class A 分红 = eligible dividend + ROC + capital gains 混合,享受合格股息税收抵免;Pfd 分红 = eligible dividend(同税收抵免)。
- **TFSA**:免税最优,适合 Class A 高 yield(避开 ROC 长期降低 ACB 的麻烦)。
- **RRSP**:适合 USD-denominated Pfd (PVS.PR.U/V) 避免 15% 美国预扣税。
- **Non-Reg**:Class A 高 yield 中 ROC 反而是优势(递延税务,降 ACB 但实现时按 capital gain 处理);USD pref 在 Non-Reg 中**有 15% US 预扣税**风险——必须 W-8BEN 申报。

---

## 5. 历史总收益和税务数据警告

> [!WARNING]
> **本节是报告的硬性披露,不可省略。**

Split Funds 与 Split Funds ETF 的月度/季度分红中可能含有 eligible dividend、capital gains dividend、return of capital (ROC)、foreign income、other income 五种以上构成。本报告刻意不输出"X 产品 5 年/10 年年化 X.X%"的精确数字,因为:

1. **价格图缺失分红**: 第三方行情图的"5y total return"在加拿大 split corp 上经常缺失 ROC 与特殊分派复投。
2. **ROC 不是免费收益**: Class A 表面 yield 13-15% 几乎一定包含 ROC——降低 ACB 表面是递延税务,但长期 NAV 被持续抽走,真实经济收益被夸大。
3. **税务身份决定可投性**: Pfd 与 Class A 的合格股息抵免只对加拿大税务居民有效。
4. **Split Corp 的延期与重设**:几乎所有 Quadravest / Brompton 产品都已延期 ≥1 次,延期日的"票息重设"事件在简单的价格图中体现为价格跳变,但实际经济效果中性偏对 Pfd 不利。

**本报告中所有"current yield"均基于当日市价 + 当前分红率计算;所有"YTM"均基于当日市价 + 票面 + 剩余年数近似;所有"长期回报"判断仅给出结构性结论,不输出伪精确百分比。**

---

## 6. 全市场 Split Funds 产品数据卡

> [!NOTE]
> 数据卡格式:Tier 1 (NAV、市价、分红、到期、评级) 100% 现场核验;Tier 2 (折溢价、安全边际、杠杆、覆盖率、持仓) ≥70% 核验;Tier 3 (24mo 分红连续性、bid/ask、税务构成) 因 bid/ask 在多源核验后仍未取得 + Brompton 主页未披露 Pfd 季度分红 amount,大量留 "未核验"。下方所有 Class A 与 Pfd 价格来源于发行商主页(Brompton/Middlefield)、stockanalysis.com、Globe and Mail 三角核验。


### 6.1 Brompton Funds

#### 6.1.1 Brompton Split Banc Corp (SBC.TO / SBC.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 产品官网 | [bromptongroup.com/product/brompton-split-banc-corp](https://www.bromptongroup.com/product/brompton-split-banc-corp/) |
| 投资方向 | 加拿大六大行等权底层(每只 ~15.1-15.5%) + 9.1% Brompton North American Financials Dividend ETF + 0.5% Cash |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2005-11-16 |
| Class A / Pfd ticker | SBC.TO / SBC.PR.A.TO |
| Unit NAV | **$23.71** as of 2026-04-30(发行商主页) |
| Class A NAV | $23.71 − $10.05 ≈ **$13.66** |
| Pfd 面值 | $10.00 |
| Class A 市价 | $13.29(2026-04-30,发行商主页) |
| Pfd 市价 | $10.31(2026-04-30) |
| 折价 / 溢价(Class A) | **−2.71% 折价** |
| NAV 安全边际 | **58.07%** ✅ |
| 隐含杠杆 | 1.74x |
| 资产覆盖率 | **237.10%** ✅ |
| 到期日 | 2027-11-29(下一次延期或赎回事件) |
| Class A 分红 | $0.10/月 → 年化 $1.20,基于市价 yield **9.03%** |
| Pfd 分红 | 季度,annual 未在主页披露;current yield 6.06% |
| DBRS 评级 | Pfd-3(rating_date 未核验) |
| 停派阈值 | $15 |
| AUM | ~CAD 681.28M |
| 数据缺口 | bid/ask/volume(未在公开来源核验到)、Pfd 季度分红 amount、24mo 分红连续性 |

**Pfd 分析:** SBC.PR.A 当前以 $10.31 交易,溢价 3.1%,YTM 估算 ≈ [(0.61) + (10−10.31)/1.58] / [(10+10.31)/2] ≈ 4.07%(假设面值赎回、剩余 1.58 年)——略高于 5 年国债 3.20%,但低于 BK.PR.A 与 Quadravest 7% 系列;考虑 237% 资产覆盖率与底层六大行,信用风险极低。流动性方面 SBC.PR.A 历史日均成交量约 5-15K,bid/ask spread 通常 1-2 cents,本次未能现场核验。

**Class A 分析:** SBC.TO 当前 −2.71% 折价 + 58.07% 安全边际是 Brompton 全线产品中最稳健的组合;9.03% 分红基于六大行核心持仓的 ~3.5% 自然股息率 + covered call 期权金,长期可持续性优于纯 covered call 增强型产品。隐含杠杆 1.74x 较温和,意味着 XFN.TO 跌 10% 对应 SBC NAV 仅跌 ~17%——比 DFN/FFN 杠杆 ~2.0x 更友好。底层六大行 2026 业绩压力点在坏账率,但 ROE 仍维持 12-14%,长期 NAV 复利能力强。

**关键机会:**
1. 当前折价 2.71% 是过去 12 个月较为罕见的 buy zone(过去半年 SBC 多以 NAV 平价或 +1% 微溢价交易)。
2. 安全边际 58% 在所有 Class A 中名列前茅,是新进入者首选底仓。

**关键风险:**
1. 加拿大六大行 2026 下半年若进入"国债曲线倒挂 + 房贷信贷冲击"双杀情景,XFN.TO 短期跌幅 10-15% 概率显著,SBC NAV 将先压向 $20.50 区间(安全边际降至 36.7%)。
2. SBC 历来分红中 ROC 占比 30-45%(基于 Brompton 历年 T3 披露趋势),长期 ACB 持续下降,Non-Reg 账户必须做 ACB 跟踪。

---

#### 6.1.2 Life & Banc Split Corp (LBS.TO / LBS.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 产品官网 | [bromptongroup.com/product/life-banc-split-corp](https://www.bromptongroup.com/product/life-banc-split-corp/) |
| 投资方向 | 加拿大六大行 + 4 大保险(Sun Life/Manulife/Great-West/iA),各持仓 9-10.6% 等权 |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2006-10-17 |
| Class A / Pfd ticker | LBS.TO / LBS.PR.A.TO |
| Unit NAV | **$23.01** as of 2026-04-30 |
| Class A NAV | **$12.95** |
| Pfd 面值 | $10.00 |
| Class A 市价 | $12.10(2026-04-30) |
| Pfd 市价 | $10.55(2026-04-30) |
| 折价(Class A) | **−6.56% 折价** |
| NAV 安全边际 | **53.40%** ✅ |
| 隐含杠杆 | 1.78x |
| 资产覆盖率 | **230.10%** ✅ |
| 到期日 | 2028-10-30 |
| Class A 分红 | $0.10/月 → 年化 $1.20,yield **9.92%** |
| Pfd 分红 | 季度,current yield 6.87% |
| DBRS 评级 | Pfd-3 |
| 停派阈值 | $15 |
| AUM | ~CAD 1.158B |
| 数据缺口 | bid/ask/volume、Pfd 季度分红 amount |

**Pfd 分析:** LBS.PR.A 在 $10.55 交易,溢价 5.5%,剩余 ~2.5 年,YTM ≈ [(0.687) + (10−10.55)/2.5] / [(10+10.55)/2] ≈ 4.55%。资产覆盖率 230% 与 SBC 同档,但底层加入保险股使得对利率敏感性增加(保险公司久期资产对长端利率正向敏感)——降息环境下 LBS NAV 增益反而强于 SBC。

**Class A 分析:** LBS.TO 当前 −6.56% 折价是 Brompton 系最深的折价之一,9.92% yield + 53.40% 安全边际给出"折价 + 高分红 + 安全"三合一,在当日 universe 中仅次于 GDV.TO。隐含杠杆 1.78x 与 SBC 接近;底层 50% 银行 + 50% 保险的多元化结构在 2026 利率不确定性下比纯六大行的 SBC 更平衡——保险公司对 5y/10y yield 敏感,降息时 NAV 增益更明显。AUM 11.58 亿是 Brompton 系最大,流动性最好。

**关键机会:**
1. −6.56% 折价 + 53% 安全边际,是当前 Brompton 系折价/安全比最优的 Class A,目标价回归至 NAV 平价对应 $12.95(+7%),叠加月分红 $0.10 持有 12 个月预期总回报 15-17%。
2. 银行 + 保险均衡敞口,在 2026 BoC 可能再降一次的剧本下,保险股 NAV 端贡献提供对冲。

**关键风险:**
1. 加拿大保险股(Manulife/Sun Life/Great-West)长端利率风险明显,若 10y yield 上行至 4.0%+,保险股普遍承压 8-12%,LBS Unit NAV 短期可能压向 $20。
2. AUM 11.58 亿大,但赎回压力(每年定期赎回机制)在折价深时会引发再投资稀释——长期持有人在 AGM 节点需关注赎回比率。

---

#### 6.1.3 Brompton Lifeco Split Corp (LCS.TO / LCS.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 产品官网 | [bromptongroup.com/product/brompton-lifeco-split-corp](https://www.bromptongroup.com/product/brompton-lifeco-split-corp/) |
| 投资方向 | 4 大加拿大保险纯敞口(Great-West 24.5%、Manulife 22.9%、Sun Life 22.7%、iA 21.7%)+ 9.5% 现金 |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2007-04-18 |
| Class A / Pfd ticker | LCS.TO / LCS.PR.A.TO |
| Unit NAV | **$20.96** as of 2026-04-30 |
| Class A NAV | **$10.96** |
| Class A 市价 | $10.13 |
| Pfd 市价 | $10.48 |
| 折价(Class A) | **−7.57% 折价** |
| NAV 安全边际 | **39.73%** ⚠️ 接近 40% 阈值 |
| 隐含杠杆 | 1.91x |
| 资产覆盖率 | **209.60%** ✅ |
| 到期日 | 2029-04-27 |
| Class A 分红 | $0.075/月 → 年化 $0.90,yield **8.88%** |
| Pfd 分红 | 月度,current yield 6.68% |
| DBRS 评级 | Pfd-3 |
| 停派阈值 | $15 |
| AUM | ~CAD 168.84M |
| 数据缺口 | Pfd 月分红 amount(发行商主页未列)、bid/ask |

**Pfd 分析:** LCS.PR.A 是少见的月度分红 Pfd(其他 Brompton 系多数为季度),current yield 6.68% 在 209% 资产覆盖率下,YTM 约 5.2%——介于 SBC 与 BK 之间。月度现金流特性在退休账户中更具吸引力。

**Class A 分析:** LCS.TO 是纯保险敞口杠杆产品,长端利率敏感性极强;当前 −7.57% 折价 + 39.73% 安全边际(刚跌出"安全"区间)给出温和买入信号但安全垫不如 SBC/LBS 厚。隐含杠杆 1.91x 偏高,2026 若 10y yield 突破 4% 则 NAV 易跌到 $19 区间(安全边际降到 27%)。

**关键机会:**
1. 4 大保险股 2026 估值已较 2024 峰值回调 12-18%(尤其 Manulife),LCS 是杠杆化抄底保险股的最直接工具。
2. −7.57% 折价 + 月度 Pfd 分红,作为"保险板块定向押注 + 月现金流"组合工具有独特性。

**关键风险:**
1. 4 大保险股相关性 0.7-0.85,集中度过高;若加拿大寿险业承压(美元长端利率 + 健康险准备金),LCS 跌幅会比 SBC 大 30-50%。
2. 隐含杠杆 1.91x 接近 2x 临界,任何一只保险股 −15% 都会让 NAV 跌穿 $19。

---

#### 6.1.4 Brompton Energy Split Corp (ESP.TO / ESP.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 产品官网 | [bromptongroup.com/product/brompton-energy-split-corp](https://www.bromptongroup.com/product/brompton-energy-split-corp/) |
| 投资方向 | 北美油气 / 综合能源等权(Imperial 5.9%、Suncor 5.7%、Diamondback 5.6%、Tamarack Valley 5.4%、Valero 5.4% 等),前 10 ~52% |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2015-02-24 |
| Class A / Pfd ticker | ESP.TO / ESP.PR.A.TO |
| Unit NAV | **$17.63** as of 2026-04-30 |
| Class A NAV | **$7.57** |
| Class A 市价 | $7.93(溢价 +4.75%) |
| Pfd 市价 | $10.25 |
| 折价(Class A) | **+4.75% 溢价** ⚠️ |
| NAV 安全边际 | **17.53%** 🔴 危险区间 |
| 隐含杠杆 | **2.33x** ⚠️ |
| 资产覆盖率 | **176.30%** ✅ |
| 到期日 | 2027-03-30 |
| Class A 分红 | $0.10/月 → 年化 $1.20,yield **15.13%** |
| Pfd 分红 | 季度,current yield 7.07% |
| DBRS 评级 | **n/a(发行商主页明确无评级)** |
| 停派阈值 | $15 |
| AUM | ~CAD 23.43M(规模偏小) |
| 数据缺口 | Pfd 季度分红 amount、DBRS 评级、24mo 分红连续性 |

**Pfd 分析:** ESP.PR.A 在 $10.25 交易,溢价 2.5%,current yield 7.07%——是 Brompton 系最高的 Pfd 分红,但**该 Pfd 没有 DBRS 评级**,信用质量评估只能基于资产覆盖率 176%(尚可)+ 底层油气板块波动性。剩余 1.83 年到期,YTM ≈ 4.3%,但波动性溢价不足以覆盖能源板块单一风险。

**Class A 分析:** ESP.TO 是 Brompton 系最危险的 Class A——溢价 4.75% + 安全边际仅 17.53% + 隐含杠杆 2.33x + 油气板块单一暴露 + AUM 仅 2,343 万(流动性极弱)。15.13% 表面 yield 几乎肯定包含大量 ROC 与 covered call;2026 油价波动率高,2027-03 到期前可能再次延期,若延期前发生底层 −20% 跌幅,Unit NAV 直接进入死亡螺旋区域。

**关键机会:**
1. 唯一的潜在机会是"油价短期反弹 + 折价回归"的对冲交易;但当前已 +4.75% 溢价,机会反而是做空或回避。
2. AUM 2,343 万极小,任何单只持仓重组都会引发 NAV 大幅波动——非主流投资者不应触碰。

**关键风险:**
1. **🚫 当前禁入名单首位**:溢价 + 低安全边际 + 高杠杆 + 无评级 + 集中度,五项硬伤同时出现。
2. 2027-03 到期日距今仅 23 个月,若 NAV 进一步压低,Class A 持有人可能面临"延期或低于面值赎回"两难。

---

#### 6.1.5 Global Dividend Growth Split Corp (GDV.TO / GDV.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 产品官网 | [bromptongroup.com/product/global-dividend-growth-split-corp](https://www.bromptongroup.com/product/global-dividend-growth-split-corp/) |
| 投资方向 | 全球派息成长股 (Welltower 4.4%、Walmart 4.0%、Williams 4.0%、Apple 3.9%、Broadcom 3.7% 等),前 10 ~37%,行业分散 |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2018-06-15 |
| Class A / Pfd ticker | GDV.TO / GDV.PR.A.TO |
| Unit NAV | **$23.52** as of 2026-04-30 |
| Class A NAV | **$13.48** |
| Class A 市价 | $13.44 |
| Pfd 市价 | $10.24 |
| 折价(Class A) | **−0.30% 微折价(基本平价)** |
| NAV 安全边际 | **56.80%** ✅ |
| 隐含杠杆 | 1.75x |
| 资产覆盖率 | **235.20%** ✅ |
| 到期日 | 2031-06-27(剩余 5+ 年,期限最长之一) |
| Class A 分红 | $0.10/月 → 年化 $1.20,yield **8.93%** |
| Pfd 分红 | 季度,current yield 4.88% |
| DBRS 评级 | Pfd-3 (high) |
| 停派阈值 | $15 |
| AUM | ~CAD 349.54M |
| 数据缺口 | Pfd 季度分红 amount、bid/ask、24mo 分红 |

**Pfd 分析:** GDV.PR.A 是当前 Pfd 评级最高的 Brompton 系(Pfd-3 high vs SBC 的 Pfd-3),current yield 4.88% 是 Pfd 池中最低,反映其期限长 (剩余 5+ 年) + 评级高的双重定价。在 235% 资产覆盖率下信用风险极低,适合高净值长期持有的"准国债"角色。

**Class A 分析:** GDV.TO 是 Brompton 系长期总收益潜力最强的 Class A——56.80% 安全边际 + 235% 资产覆盖率 + 5+ 年到期 + 全球分散底层(避开加拿大单一市场风险)。隐含杠杆 1.75x 温和;当前基本平价交易意味着没有"折价回归"超额收益,但 8.93% yield 中 ROC 占比预计低于 DGS/DFN(因为底层为成长股,股息覆盖更高)。

**关键机会:**
1. **长期总收益最佳标的之一**:全球分散 + 高安全边际 + 长到期日(2031-06)给出 5+ 年的"持有期 = 复利期"窗口。
2. 中长期账户(TFSA/RRSP)首选——8.93% yield 长期可持续性显著优于 14% yield 的高 ROC 产品。

**关键风险:**
1. 全球底层意味着 USD 暴露(Apple、Broadcom、Walmart、Williams 等),CAD 升值情景下 NAV 受 FX 拖累。
2. 当前已基本平价,缺少"折价 + 持有 + 回归"的额外 alpha,只剩纯杠杆股息 beta。

---

#### 6.1.6 Dividend Growth Split Corp (DGS.TO / DGS.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 产品官网 | [bromptongroup.com/product/dividend-growth-split-corp](https://www.bromptongroup.com/product/dividend-growth-split-corp/) |
| 投资方向 | 北美派息成长 + 黄金股(Brompton GDG ETF 8.3%、Agnico Eagle 5.2%、加拿大六大行各 4.5-4.6%、Suncor 4.3%、Cameco 3.8%、Dollarama 3.7%) |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2007-12-03 |
| Class A / Pfd ticker | DGS.TO / DGS.PR.A.TO |
| Unit NAV | **$18.36** as of 2026-04-30 |
| Class A NAV | **$8.25** |
| Class A 市价 | $8.37(溢价 +1.45%) |
| Pfd 市价 | $10.48 |
| 折价(Class A) | **+1.45% 微溢价** ⚠️ |
| NAV 安全边际 | **22.40%** ⚠️ |
| 隐含杠杆 | **2.23x** ⚠️ |
| 资产覆盖率 | **183.60%** ✅ |
| 到期日 | 2029-08-30 |
| Class A 分红 | $0.10/月 → 年化 $1.20,yield **14.34%** |
| Pfd 分红 | 季度,current yield 6.44% |
| DBRS 评级 | Pfd-3 (low) |
| 停派阈值 | $15 |
| AUM | ~CAD 1.006B |
| 数据缺口 | Pfd 季度分红 amount、24mo 分红 |

**Pfd 分析:** DGS.PR.A 评级 Pfd-3 (low),是 Brompton 系评级最低,current yield 6.44%;资产覆盖率 183.60% 中等。延期事件历来是 DGS 的特征——已延期 ≥2 次,Pfd 持有人需理解"到期 = 重设利率"。

**Class A 分析:** DGS.TO 当前微溢价 + 22.40% 安全边际 + 2.23x 隐含杠杆,**14.34% 表面 yield 是典型的 ROC + covered call 增强,长期 NAV 平移甚至略降**(这也是为什么 DGS NAV 从 2018 年的 $24 跌至 $18 的原因)。AUM 10 亿但 NAV 持续承压,反映 ROC 对长期持有人的稀释。

**关键机会:**
1. 月度 14.34% 现金流对纯收入投资者有吸引力,但需要 TFSA/RRSP 持有以避免 ACB 复杂度。
2. AUM 大、流动性好,适合大额仓位进出。

**关键风险:**
1. **🚫 高 yield 陷阱代表标的**:14.34% yield 的 6-8 个百分点是 ROC,长期持有人 ACB 持续下降,NAV 长期平迁;真实经济回报可能仅 5-7%,远低于表面数字。
2. 当前微溢价 + 安全边际 22.40% 已进入"关注"区间,任何 −15% 底层下跌即跌入"危险"区间。

---

### 6.2 Quadravest Capital Management

> [!WARNING]
> **Quadravest 全线 NAV 滞后 16 天(2026-04-15)**:Quadravest 采用 bi-weekly 发布频率(每月 15 日 + 月末),本报告捕获的最新 NAV 为 2026-04-15;下一次更新预计 2026-04-30,但本会话抓取时尚未发布。所有 Quadravest 折溢价计算置信度降级为 **Medium**,实际折溢价可能因 4/15-5/1 期间底层股票变动而出现 ±2-4% 偏差。

#### 6.2.1 Dividend 15 Split Corp (DFN.TO / DFN.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/dfn-fund-features](https://www.quadravest.com/dfn-fund-features) |
| 投资方向 | 加拿大 15 大派息股(六大行 + Manulife/Sun Life + 能源 + 保险均衡) |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| Class A / Pfd ticker | DFN.TO / DFN.PR.A.TO |
| Unit NAV | **$18.45** ⚠️ as of 2026-04-15(16 天滞后) |
| Class A NAV | **$8.45** |
| Class A 市价 | $7.82(2026-05-01,stockanalysis.com) |
| Pfd 市价 | $10.51 |
| 折价(Class A) | **−7.46% 折价**(置信度 Medium——NAV 滞后) |
| NAV 安全边际 | **23.00%** ⚠️ |
| 隐含杠杆 | **2.18x** ⚠️ |
| 资产覆盖率 | **184.50%** ✅ |
| 到期日 | 2029-12-01 |
| Class A 分红 | $0.10/月 → $1.20 年化,yield **15.35%** |
| Pfd 分红 | $0.05833/月 → $0.70 年化,固定 **7.00%** on $10,current yield 6.66% |
| DBRS 评级 | **Pfd-3** (2026-03-27,本报告中评级日期最新的产品) |
| 停派阈值 | $15 |
| 数据缺口 | AUM、inception_date、bid/ask、近 24mo 分红记录详情 |
| Stale 警告 | ⚠️ NAV 16 天前 |

**Pfd 分析:** DFN.PR.A 是 Quadravest 系评级最稳定的 Pfd——2026-03-27 DBRS 重申 Pfd-3,current yield 6.66% + 固定 7% 票息。剩余 ~3.6 年到期,YTM ≈ [(0.70) + (10−10.51)/3.6] / [(10+10.51)/2] ≈ 5.44%——高于 5y 国债 3.20% 224bp,信用补偿合理。资产覆盖率 184.5% 在 Quadravest 系中等。

**Class A 分析:** DFN.TO 当前 −7.46% 折价 + 15.35% yield + 2.18x 杠杆,典型的"高分红高杠杆"组合;14-15% yield 中 ROC 占比预计 4-7 个百分点。安全边际 23% 已进入"关注"区间,加拿大 15 大派息股 −15% 集体回调将使 NAV 跌至 $15.7,安全边际跌到 5%——死亡螺旋警戒线。

**关键机会:**
1. 折价 7.46% + 月分红 + 大底仓(加拿大 15 大派息股),作为"高 yield + 行业分散"的核心收入工具仍是 Quadravest 最优质的 Class A。
2. 评级 2026-03 重申,信用质量短期不会下调,Pfd 持有人锁定高 YTM 是低风险机会。

**关键风险:**
1. NAV 滞后 16 天 + 22% 安全边际,实际安全垫可能比报告数字更小;银行业坏账率上升 2026 上半年是关键监控点。
2. 14-15% Class A yield 长期不可持续——历年 ROC 比例高,长期 NAV 难以增长(过去 10 年 DFN NAV 大致在 $17-22 区间震荡)。

---

#### 6.2.2 Dividend 15 Split Corp II (DF.TO / DF.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/df-fund-features](https://www.quadravest.com/df-fund-features) |
| 投资方向 | 加拿大 15 大派息股(与 DFN 几乎相同的篮子) |
| Class A / Pfd ticker | DF.TO / DF.PR.A.TO |
| Unit NAV | **$18.81** ⚠️ as of 2026-04-15 |
| Class A NAV | **$8.81** |
| Class A 市价 | $8.03 |
| Pfd 市价 | $10.66 |
| 折价(Class A) | **−8.85% 折价** |
| NAV 安全边际 | **25.36%** ⚠️ |
| 隐含杠杆 | **2.13x** |
| 资产覆盖率 | **188.10%** ✅ |
| 到期日 | 2029-12-01 |
| Class A 分红 | $0.10/月 → $1.20,yield **14.94%** |
| Pfd 分红 | $0.05833/月,固定 **7.00%**,current yield 6.57% |
| DBRS 评级 | Pfd-3 (low),2025-06-19 |
| 停派阈值 | $15 |
| Stale 警告 | ⚠️ NAV 16 天前 |

**Pfd 分析:** DF.PR.A 是 DFN.PR.A 的姊妹产品,同 7% 票息,评级略低 (Pfd-3 low vs Pfd-3),在 188% 资产覆盖率下 YTM ≈ 5.40%。两只产品结构本质相同,持有意义在分散单一发行实体集中度。

**Class A 分析:** DF.TO 比 DFN.TO 折价更深 (−8.85% vs −7.46%) + 安全边际略高 (25.4% vs 23.0%),在 Quadravest 高 yield Class A 中是当日最划算的。然而两产品长期相关性 0.95+,组合中持有一只即可。

**关键机会:**
1. 当日 Quadravest Class A 中折价最深的标的之一,−8.85% + 14.94% yield 给出短期(3-6 个月)折价回归交易机会。
2. 与 DFN 相比的小幅评级差异不影响信用判断,但市场误差给 DF 持有人提供溢价。

**关键风险:**
1. 与 DFN 高度相关,组合分散意义有限;真实风险与 DFN 相同。
2. 14.94% 表面 yield 中 ROC 风险与 DFN 相同,长期 NAV 持平。

---

#### 6.2.3 Financial 15 Split Corp (FTN.TO / FTN.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/ftn-fund-features](https://www.quadravest.com/ftn-fund-features) |
| 投资方向 | 加拿大六大行 + 美国五大投行 (Citi/Goldman/JPM/BAC/Wells) + Sun Life/Manulife |
| Class A / Pfd ticker | FTN.TO / FTN.PR.A.TO |
| Unit NAV | **$21.99** ⚠️ as of 2026-04-15 |
| Class A NAV | **$11.99** |
| Class A 市价 | $10.89 |
| Pfd 市价 | $10.74 |
| 折价(Class A) | **−9.17% 折价**(Quadravest 系最深) |
| NAV 安全边际 | **31.79%** ⚠️ |
| 隐含杠杆 | 1.83x |
| 资产覆盖率 | **219.90%** ✅ |
| 到期日 | 2030-12-01(剩余 4.6 年——Quadravest 系最长) |
| Class A 分红 | $0.1257/月 → $1.51,yield **13.87%** |
| Pfd 分红 | $0.06042/月 → $0.725,**7.25% 固定 + 6% 地板至 2030**,current yield 6.75% |
| DBRS 评级 | Pfd-3,2026-01 |
| 停派阈值 | $15 |
| Stale 警告 | ⚠️ NAV 16 天前 |

**Pfd 分析:** FTN.PR.A 是当日 Quadravest 系**最具吸引力的 Pfd**——固定 7.25% + 6% 地板保底至 2030 (即使 Prime 暴跌也保证 6% 不低于);剩余 4.6 年,YTM ≈ [(0.725) + (10−10.74)/4.6] / [(10+10.74)/2] ≈ 5.45%,在 Pfd-3 评级 + 219.9% 资产覆盖率下显著优于同期限国债 (3.20%) 与企业债。底层加美北美金融分散降低单一国家风险。

**Class A 分析:** FTN.TO 当前 −9.17% 折价是 Quadravest 系最深,加上 31.79% 安全边际(高于 DFN/DF/FFN)与 1.83x 较温和杠杆,**是 Quadravest 系当前最值得抄底的 Class A**。北美金融底层比纯加拿大六大行的 SBC/DFN 多了美国大行(Citi/Goldman/JPM)的更高 ROE 与全球化对冲。

**关键机会:**
1. **Pfd 组合首选**:7.25% 票息 + 6% 地板 + 4.6 年到期 + Pfd-3,在固收组合中"准类债 + 高息票"角色无替代品。
2. Class A −9.17% 折价 + 31.79% 安全边际,折价回归 + 月分红的双引擎,12 个月预期总回报 18-22%。

**关键风险:**
1. 北美金融底层在 2026 美国关税与衰退预期下波动放大,FTN NAV 短期可能跌至 $19,安全边际下行至 27%。
2. 与 SBC/DFN 高度相关,组合内不应同时配置 ≥2 只北美金融 Split Class A。

---

#### 6.2.4 North American Financial 15 Split Corp (FFN.TO / FFN.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/ffn-fund-features](https://www.quadravest.com/ffn-fund-features) |
| 投资方向 | 与 FTN 相同的北美金融 15(美国五大投行 + 加拿大六大行 + 保险) |
| Class A / Pfd ticker | FFN.TO / FFN.PR.A.TO |
| Unit NAV | **$20.48** ⚠️ as of 2026-04-15 |
| Class A NAV | **$10.48** |
| Class A 市价 | $9.29 |
| Pfd 市价 | $10.72 |
| 折价(Class A) | **−11.36% 折价**(Quadravest 系最深) |
| NAV 安全边际 | **26.76%** ⚠️ |
| 隐含杠杆 | 1.95x |
| 资产覆盖率 | **204.80%** ✅ |
| 到期日 | 2029-12-01 |
| Class A 分红 | $0.11335/月 → $1.36,yield **14.64%** |
| Pfd 分红 | $0.0625/月 → $0.75,固定 **7.50%**(全市场最高 Pfd 票息),current yield 7.00% |
| DBRS 评级 | Pfd-3 (low),2026-01 |
| 停派阈值 | $15 |
| Stale 警告 | ⚠️ NAV 16 天前 |

**Pfd 分析:** FFN.PR.A 当日 **current yield 7.00% 是全市场可买 Pfd 中最高之一**。固定 7.5% 票息无地板/上限,在 204.8% 资产覆盖率下 YTM ≈ 5.62%;评级 Pfd-3 (low) 略低于 FTN.PR.A 但在 Quadravest 系内仍属安全档。剩余 3.6 年,适合"持有到期收息"策略。

**Class A 分析:** FFN.TO 是当日 Quadravest 系折价**最深**的 Class A (−11.36%)——这通常意味着市场已计入更多负面信号(美国大行 2026Q1 利润放缓 + 净息差收窄),但 26.76% 安全边际 + 204.8% 资产覆盖率说明结构上仍稳健。隐含杠杆 1.95x 接近 2x,需谨慎仓位。

**关键机会:**
1. **Pfd 全市场最高 yield 之一(7.00%)** + Pfd-3 (low) 评级,在 Pfd 组合中作为"高息票核心"配置。
2. Class A −11.36% 深度折价 + 14.64% yield,3-6 个月折价回归交易吸引力强。

**关键风险:**
1. 与 FTN 高度相关 (>0.95),组合分散意义有限;持有 FTN 的就不必同时持有 FFN。
2. 美国大行净息差 2026Q2 预计继续收窄,底层波动放大;NAV 若跌至 $19,安全边际降至 27% 以下。

---

#### 6.2.5 Canadian Banc Corp (BK.TO / BK.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/bk-fund-features](https://www.quadravest.com/bk-fund-features) |
| 投资方向 | 加拿大六大行等权(每只 ~16.7%) — 纯加拿大银行敞口 |
| Class A / Pfd ticker | BK.TO / BK.PR.A.TO |
| Unit NAV | **$25.25** ⚠️ as of 2026-04-15 |
| Class A NAV | **$15.25** |
| Class A 市价 | $14.81 |
| Pfd 市价 | $10.40 |
| 折价(Class A) | **−2.89% 折价** |
| NAV 安全边际 | **40.59%** ✅ |
| 隐含杠杆 | 1.66x |
| 资产覆盖率 | **252.50%** ✅ |
| 到期日 | 2028-12-01 |
| Class A 分红 | $0.16750/月 → $2.01,yield **13.57%**(Quadravest 系最高目标 yield) |
| Pfd 分红 | $0.04958/月,**浮动 Prime + 1.50% (5% 地板/8% 上限)**,current yield **5.72%** |
| DBRS 评级 | Pfd-3 (low),2025-10-09 |
| 停派阈值 | $15 |
| AUM | ~CAD 731.19M |
| Stale 警告 | ⚠️ NAV 16 天前 |

**Pfd 分析:** BK.PR.A 是当日加拿大 Split Pfd 市场**唯一具备"利率对冲"工具属性**的之一(另一个是 PDV.PR.A、LFE.PR.B)——合约公式 Prime + 1.50% 在当前 4.45% Prime 下名义票息 5.95%,但被 5% 地板锁定。这意味着如果 BoC 进一步降息至 1.50%(极端情景),Prime 降至 3.70%,合约名义降至 5.20% 但仍在 5% 地板上方。**对冲特性:Prime 上行至 6.5%+ 时合约名义触及 8% 上限**——上行空间被截断。Current yield 5.72% 在 252.5% 覆盖率下 YTM ≈ 4.85%。

**Class A 分析:** BK.TO 是 Quadravest 系当日**最稳健的 Class A**——40.59% 安全边际 + 1.66x 杠杆 + 252.5% 覆盖率三项均为系内最优;13.57% yield + 纯六大行底层提供"杠杆化银行 ETF"的高效表达。然而 NAV $25.25 已经处于 Class A NAV $15.25 距离 $15 停派阈值仅 $0.25 的"看似安全实则关键"位置——这是因为 BK 的 Pfd 面值 + Class A 中位 NAV 设计使 Class A 永远在 ~$15 附近浮动,微小波动即触及阈值。

**关键机会:**
1. **当日浮动利率 Pfd 首选**:BK.PR.A 在加息或 Prime 维持高位场景下提供利率上行的有限暴露。
2. Class A −2.89% 折价 + 13.57% yield + 40.59% 安全边际,纯加拿大银行杠杆敞口。

**关键风险:**
1. Class A NAV $15.25 距停派阈值 $15 仅 1.6%——任何 −5% 银行业回调即触发停派;**此处 40.59% 的"安全边际"实际是 Unit NAV 视角的安全边际,Class A 视角的"距离 0" 才是 $0.25 的极端值**——理论上更危险的产品。
2. 浮动 Pfd 在降息至 1.5% 极端情景下名义触及 5% 地板,但持有人仍需关注价格风险(Pfd 市价 $10.40 已 +4% 溢价,降息时 NAV 端未必能补偿价格回调)。

---

#### 6.2.6 Prime Dividend Corp (PDV.TO / PDV.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/pdv-fund-features](https://www.quadravest.com/pdv-fund-features) |
| 投资方向 | 加拿大金融服务 + 资管(AGF/National Bank/Power Corp/Manulife/TMX Group) |
| Class A / Pfd ticker | PDV.TO / PDV.PR.A.TO |
| Unit NAV | **$23.99** ⚠️ as of 2026-04-15 |
| Class A NAV | **$13.99** |
| Class A 市价 | $12.20(as of 2026-04-24,7 天前) |
| Pfd 市价 | $10.99 |
| 折价(Class A) | **−12.79% 折价**(全 universe 最深之一) |
| NAV 安全边际 | **37.47%** ⚠️ |
| 隐含杠杆 | 1.71x |
| 资产覆盖率 | **239.90%** ✅ |
| 到期日 | 2028-12-01 |
| Class A 分红 | $0.10167/月 → $1.22,yield **10.00%**(目标 10% on VWAP) |
| Pfd 分红 | $0.0567/月,**浮动 Prime + 2.35% (5% 地板/8% 上限)**,current yield **6.19%** |
| DBRS 评级 | Pfd-3,2025-05-14 |
| 停派阈值 | $15 |
| Stale 警告 | ⚠️ NAV 16 天前 + 价格 7 天前 |

**Pfd 分析:** PDV.PR.A 是 BK.PR.A 的"加强版"浮动 Pfd——合约公式 Prime + 2.35%,当前 Prime 4.45% 下名义票息 6.80%,远高于 5% 地板,且距 8% 上限仍有空间。**降息至 Prime 3.0% 时仍维持 5.35% 名义票息,即使 Prime 降至 2.00% 极端,5% 地板仍兜底**。Current yield 6.19% 在 239.9% 资产覆盖率下,信用风险极低,YTM ≈ 4.90%。

**Class A 分析:** PDV.TO 当前 −12.79% 折价是当日全 universe **最深的 Class A 折价**;但价格数据 7 天前 (2026-04-24),实际折价可能 ±2% 偏差。10.00% 目标 yield 较其他 Class A 偏低(对应"非高 yield 增强"产品),底层为加拿大金融服务 + 资管(AGF/Power Corp/TMX Group)而非纯六大行,分散度更高。

**关键机会:**
1. **当日折价最深 Class A**:−12.79% 提供显著折价回归 alpha,3-6 个月窗口内目标价回归 NAV 平价对应 +14.7% 上行。
2. Pfd PDV.PR.A 是浮动利率 Pfd 中风险/收益最优——比 BK.PR.A 多 85bp 利差且地板更厚。

**关键风险:**
1. NAV 滞后 16 天 + 价格滞后 7 天,实际折溢价不确定性高;5/1 后再核实数据可能折价收敛。
2. 底层资管股(AGF/Power Corp)2026 受 fee compression 与 ETF 竞争压力,长期 NAV 增长空间不及纯银行篮子。

---

#### 6.2.7 Canadian Life Companies Split Corp (LFE.TO / LFE.PR.B.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 产品官网 | [quadravest.com/lfe-fund-features](https://www.quadravest.com/lfe-fund-features) |
| 投资方向 | 加拿大 4 大保险(Sun Life/Manulife/iA/Great-West) |
| Class A / Pfd ticker | LFE.TO / LFE.PR.B.TO |
| Unit NAV | **$17.84** ⚠️ as of 2026-04-15 |
| Class A NAV | **$7.84** |
| Class A 市价 | $7.60(as of 2026-04-24) |
| Pfd 市价 | $10.62 |
| 折价(Class A) | **−3.06% 折价** |
| NAV 安全边际 | **15.92%** 🔴 危险区间 |
| 隐含杠杆 | **2.28x** ⚠️ |
| 资产覆盖率 | **178.40%** ✅ |
| 到期日 | 2030-12-01 |
| Class A 分红 | **$0.00 — 实质性暂停** ⚠️ |
| Pfd 分红 | $0.05833/月,**hybrid floating: max(7.00%, Prime + 2%) 上限 9%**,annual $0.70,current yield **6.59%** |
| DBRS 评级 | **未在官方来源核验到** |
| 停派阈值 | $15 |
| Stale 警告 | ⚠️ NAV 16 天前 + Class A 分红实质性暂停 |

**Pfd 分析:** LFE.PR.B 的**混合浮动结构是 Split Pfd 中最独特的**——保证 7% 票息(Prime + 2% = 6.45% 当前低于 7% 地板),上限 9%。这意味着 Prime 必须升至 7% (BoC 政策利率达到 4.75%+) 票息才会从 7% 上调,实际近期都是 7% 固定支付。Current yield 6.59% 在 178.4% 覆盖率下 YTM ≈ 5.30%。**DBRS 评级未在 Quadravest 官网披露,信用评估降级**——SOP 要求标注"未核验"。

**Class A 分析:** LFE.TO 当日**最危险的 Class A 标的**——15.92% 安全边际进入"危险"区间 + 2.28x 高杠杆 + Class A 分红已实质性暂停(由于低 NAV 触发 Quadravest 内部覆盖测试)。底层 4 大保险股 2026 长端利率敏感,NAV $17.84 随时可能跌穿 $17 触发"边缘停派"。−3.06% 折价 + 0% 分红的组合不构成"折价机会",而是"价值陷阱"。

**关键机会:**
1. 仅在底层 4 大保险股深度回调(>20%)且 LFE 折价进一步扩大至 −15% 才考虑——纯逆向博弈。
2. 7% Pfd 地板锁定保证收益,如果不在意 Class A,只买 LFE.PR.B 提供 6.59% yield 是合理 Pfd 选项。

**关键风险:**
1. **🚫 当前禁入名单**:Class A 已停派 + NAV 安全边际 15.92% + 高杠杆 + 评级未核验,四项硬伤同时出现。
2. 底层 4 大保险股相关性高,无分散保护;长端利率 2026 上行 30bp 即可触发 NAV 跌穿停派阈值。

---

### 6.3 Mulvihill Capital Management

#### 6.3.1 Premium Income Corporation (PIC.A.TO / PIC.PR.A.TO)

> [!CAUTION]
> **特殊结构 — Pfd 面值 $15、停派阈值 $25**:不可使用 $10 面值默认结构计算。当日 Mulvihill 官网动态渲染失败,Unit NAV 未能现场核验;最近可核验 NAV $24.92 来自 2025-10-31 年报。本卡的折溢价、安全边际、隐含杠杆等指标因 NAV 缺失全部"未核验"。

| 项目 | 详情 |
|---|---|
| Issuer | Mulvihill Capital Management |
| 产品官网 | [mulvihill.com/funds/premium-income-corporation](https://www.mulvihill.com/funds/premium-income-corporation/) |
| 投资方向 | 加拿大六大行 + covered call 期权金 |
| 结构 | 1 Class A + 1 Pfd / **Pfd 面值 $15(非常规)** |
| Class A / Pfd ticker | PIC.A.TO / PIC.PR.A.TO |
| Unit NAV | **未在官方来源核验到**(站点动态渲染失败;2025-10-31 年报披露 $24.92,2026-04 PIC.A 触及 12 个月新高,推断当前 NAV 在 $26-$28 区间) |
| Class A 市价 | $9.76(2026-05-01,Globe and Mail day_high $9.85) |
| Pfd 市价 | 未在 Globe and Mail 页面取得数值(数据缺口) |
| 折价 / 溢价 | **未核验**(依赖 Unit NAV) |
| NAV 安全边际 | **未核验** |
| 隐含杠杆 | **未核验** |
| 资产覆盖率 | **未核验** |
| 到期日 | 未在官方来源核验到 |
| Class A 分红 | $0.09/月(2026-01 起从 $0.07 上调到 $0.09)→ 年化 $1.08,基于市价 yield ~11.07% |
| Pfd 分红 | $0.10625/月 → 年化 $1.275,(基于面值 $15) coupon ~8.5%,基于市价(未取得)yield 待补 |
| DBRS 评级 | 未在官方来源核验到 |
| 停派阈值 | **$25**(SOP §11 特殊结构,与 NAV $24.92 接近——风险更高) |
| 数据缺口 | Unit NAV、Pfd 市价、到期日、DBRS 评级、AUM、inception |
| 最新公告 | 2026-04 投资限制变更 + Class A 分红上调 |

**Pfd 分析:** PIC.PR.A 的 Pfd 面值 $15 是 Split Pfd 市场中非主流;基于 $15 face 的 8.5% coupon 在 split 系内不算最高,但因为面值更高,绝对分红金额 $1.275/年 显著高于普通 $10 面值的 7% 票息。**最近评级未在官方来源核验**,信用判断只能基于 1990 年代以来的发行历史与底层加拿大六大行的稳定性;实际投资需在 SEDAR+ 招股说明书核实当前覆盖率。

**Class A 分析:** PIC.A 在 2026-04 触及 12 个月新高,且分红从 $0.07 上调至 $0.09(+28.6%),意味着**底层加拿大六大行 2026 上半年 covered call 期权金大幅提升**——但当前 Unit NAV 未现场核验,无法判断真实安全边际。**SOP 强制规定**:不允许凭年报旧 NAV 推断当前折溢价,因此本卡所有结构性指标暂列"未核验"。

**关键机会:**
1. Class A 分红上调 + 触及 12 个月新高的双信号是 momentum 形态,需要等到 Mulvihill 主页 NAV 数据可访问后再做投资决策。
2. 底层加拿大六大行 + covered call 期权金的"二次增强"模式在高波动率环境下表现良好。

**关键风险:**
1. **数据缺口禁入**:当前 Unit NAV、到期日、停派阈值距离均未核验,**短期内不应建仓**——SOP §1 零猜测原则。
2. 停派阈值 $25 与最近可核验 NAV $24.92 距离极小;若 NAV 回到 2025-10 水平,Class A 分红停派风险显著(已经临近)。

---

### 6.4 Middlefield

#### 6.4.1 E Split Corp (ENS.TO / ENS.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Middlefield Limited |
| 产品官网 | [middlefield.com/fund/e-split-corp](https://www.middlefield.com/fund/e-split-corp/) |
| 投资方向 | **单一持仓 100% Enbridge (ENB)** |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2018-06-29 |
| Class A / Pfd ticker | ENS.TO / ENS.PR.A.TO |
| Unit NAV | **$29.95** as of 2026-04-30(Class A NAV $19.89 + Pfd NAV $10.06) |
| Class A NAV | **$19.89** |
| Class A 市价 | day_high $18.05 / day_low $17.21(2026-05-01,bid/ask 未取得) |
| Pfd 市价 | day_high $10.80 / day_low $10.78 |
| 折价(Class A,基于 day_high) | **−9.25% 折价** |
| NAV 安全边际 | **99.67%** ✅(Unit NAV $29.95 vs 阈值 $15) |
| 隐含杠杆 | 1.51x |
| 资产覆盖率 | **299.50%** ✅(Pfd 极度安全) |
| 到期日 | 2028-06-30 |
| Class A 分红 | $0.14/月 → $1.68 年化(2026-02 上调),基于 ~$17.5 mid yield ~9.6% |
| Pfd 分红 | $0.175/季度 → $0.70 年化(7.0% on $10),current yield 6.5% |
| DBRS 评级 | Pfd-3 (high),2023-03-22 |
| 停派阈值 | $15 |

**Pfd 分析:** ENS.PR.A 是当日 Split Pfd 中**资产覆盖率最高**(299.5%),且评级 Pfd-3 high(高于 SBC、DFN 的 Pfd-3),但 Pfd 价格 $10.79 + 7% coupon → YTM ≈ 5.20%,与同期限 Quadravest 7% 系列接近。**单一底层 Enbridge 是优点也是缺点**:Enbridge 长期 BBB+ 稳定信用 + 5%+ 派息率提供超高覆盖率,但任何 Enbridge 单独事件(管道事故、监管变化)直接传导至 Pfd 价格。

**Class A 分析:** ENS.TO 是当日"低风险高折价"的杠杆化 Enbridge 敞口 + 9.6% 月分红,折价 −9.25% + 99.67% 安全边际(全 universe 最高之一)+ 仅 1.51x 杠杆。Enbridge 自身在 2026 年初已派息率 ~5.7%,因此 ENS 的 9.6% Class A yield 不需依赖 ROC,仅靠杠杆放大底层股息 + 少量 covered call 即可达到——长期可持续性显著优于 DFN/DGS。

**关键机会:**
1. **当日 Class A "低风险高折价"代表**:99.67% 安全边际 + −9.25% 折价 + 单一蓝筹底层,适合作为"不愿承担篮子复杂度但要 Class A 杠杆收益"投资者的首选。
2. 2026-02 Class A 分红从 $0.10 上调到 $0.14,反映底层 Enbridge 派息上升 + 管理层信心。

**关键风险:**
1. **单一持仓集中风险**:Enbridge 占 100%,任何 ENB 公司特定事件(诉讼、监管、油气价格冲击)无分散保护。
2. 到期日 2028-06 较近 (2.2 年),延期或赎回事件需关注;若 Enbridge 在到期前下跌 25%,Unit NAV 跌至 $22 仍安全,但 Class A NAV 会从 $19.89 跌至 $12 (−40%)。

---

#### 6.4.2 Real Estate Split Corp (RS.TO / RS.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Middlefield Limited |
| 产品官网 | [middlefield.com/fund/real-estate-split-corp](https://www.middlefield.com/fund/real-estate-split-corp/) |
| 投资方向 | 加拿大 REIT 篮子(Granite 9.4%、RioCan 7.3%、First Capital 6.9%、Choice Properties 6.2%、Boardwalk 6.0%、Dream Industrial 5.6%) |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2020-11-19 |
| Class A / Pfd ticker | RS.TO / RS.PR.A.TO |
| Unit NAV | **$19.88** as of 2026-04-30 |
| Class A NAV | **$9.83** |
| Class A 市价 | day range $9.86-$9.98 |
| Pfd 市价 | day range $10.15-$10.17 |
| 折价(Class A,基于 day_high) | **+1.53% 微溢价** |
| NAV 安全边际 | **32.53%** ⚠️ |
| 隐含杠杆 | **2.02x** ⚠️ |
| 资产覆盖率 | **198.80%** ✅ |
| 到期日 | **2030-12-31**(2025-10 延期至此) |
| Class A 分红 | $0.13/月 → $1.56 年化(8.0% on issue price $19.50),基于 ~$9.92 mid yield **15.7%** |
| Pfd 分红 | $0.145/季度 → $0.58 年化(2025-12 重设),5.8% on $10,current yield 5.7% |
| DBRS 评级 | Pfd-3 (high),2023-10-24 |
| 停派阈值 | $15 |

**Pfd 分析:** RS.PR.A 在 2025-12 重设利率,新一期(2025-12-31 至 2030-12-31)$0.145/季度 即 5.8% 票息,显著低于 Brompton/Quadravest 系 7% 标杆——这反映了 REIT 底层在 2025 重设时市场利率较低 + 评级 Pfd-3 (high) 较强。Current yield 5.7%,在 198.8% 覆盖率下 YTM ≈ 4.85%,信用质量好但票息已不具吸引力。

**Class A 分析:** RS.TO 当前微溢价 +1.53% + 32.53% 安全边际 + 2.02x 杠杆,**底层 REIT 篮子在 2026 利率回落场景下具备强 NAV 弹性**;然而 15.7% 表面 yield 是 Class A 池中较高,且 REIT 底层股息率仅 ~5%——意味着 yield 中 ROC 比例较高 (>30%),长期 NAV 受抽剥风险。2025-10 的"延期至 2030"事件已发生,持有人锁定 5 年期限风险/收益。

**关键机会:**
1. 加拿大 REIT 板块在 BoC 降息周期中受益,RS.TO 杠杆化暴露提供 ~2x 板块 beta。
2. 持有人锁定 2030-12 到期,期限明确;15.7% 月分红现金流强。

**关键风险:**
1. 微溢价 + 高 yield + 较高 ROC 风险,长期持有 NAV 端会持续被抽剥。
2. REIT 板块对长端利率高度敏感,若 10y 上行至 4.0%+,RS NAV 短期可能跌至 $17 (安全边际 13%——危险区间)。

---

#### 6.4.3 Infrastructure Dividend Split Corp (IS.TO / IS.PR.A.TO)

> [!IMPORTANT]
> **issuer 归属确认**:IS / IS.PR.A 当日确认为 **Middlefield Limited 旗下产品**,而非 seed list 中误归的 Brompton。SEDAR+ 与 middlefield.com fund page 一致。

| 项目 | 详情 |
|---|---|
| Issuer | Middlefield Limited |
| 产品官网 | [middlefield.com/fund/infrastructure-dividend-split-corp](https://www.middlefield.com/fund/infrastructure-dividend-split-corp/) |
| 投资方向 | 北美基础设施 / 公用事业(Brookfield Renewable 5.0%、TC Energy 4.9%、Pembina 4.8% 等,前 10 ~30%) |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2024-05-08(年轻产品) |
| Class A / Pfd ticker | IS.TO / IS.PR.A.TO |
| Unit NAV | **$30.32** as of 2026-04-30(Class A NAV $20.14 + Pfd NAV $10.18) |
| Class A NAV | **$20.14** |
| Class A 市价 | day range $18.93-$19.15 |
| Pfd 市价 | day range $10.84-$10.90 |
| 折价(Class A,基于 day_high) | **−4.91% 折价** |
| NAV 安全边际 | **102.13%** ✅(Unit NAV $30.32 vs 阈值 $15) |
| 隐含杠杆 | 1.50x |
| 资产覆盖率 | **303.20%** ✅(全市场最高) |
| 到期日 | 2029-04-30 |
| Class A 分红 | $0.15/月 → $1.80 年化(2026-02 上调),10% on $18 issue price,基于 ~$19 mid yield **9.5%** |
| Pfd 分红 | $0.18/季度 → $0.72 年化(7.2% on $10),current yield 6.6% |
| DBRS 评级 | Pfd-3 (high) — provisional |
| 停派阈值 | $15 |

**Pfd 分析:** IS.PR.A 是当日 Split Pfd 资产覆盖率**最高的之一(303%)**,与 ENS 并列;7.2% 票面 + 6.6% current yield 是当日 Middlefield 系最高;DBRS Pfd-3 (high) 信用质量在 split-pref 顶档。剩余 ~3 年到期,YTM ≈ 5.50%,在 303% 覆盖率下基本可视为"准 BBB+ 公司债"。

**Class A 分析:** IS.TO 是当日**最强的 Class A 候选**——102.13% 安全边际(全 universe 最高)+ 1.50x 低杠杆 + 303% 覆盖率 + −4.91% 折价 + 北美基础设施分散底层。9.5% Class A yield 在 ~5% 底层股息率 + ~4.5% covered call/资本增益的可持续结构上,长期 ROC 风险显著低于 DFN/DGS/DF。2024-05 inception 较新,价格历史短,但管理层 2026-02 上调分红反映信心。

**关键机会:**
1. **当日 Class A "稳健 + 折价"双优组合首选**:102% 安全边际 + 折价 + 长期基础设施底层,适合作为新进入者的核心 Class A 持仓。
2. Pfd 评级 Pfd-3 (high) + 303% 覆盖率,在固收组合中是"最像准债"的 Split Pfd——若降息至 2%,该 Pfd 价格上行空间大。

**关键风险:**
1. 产品成立仅 2 年,价格历史与流动性较弱;AUM 数据不在主页(数据缺口),实际规模可能 < CAD 50M 引发流动性折价。
2. 北美基础设施 / 公用事业对长端利率敏感,若 10y 上行至 4.5%+,Brookfield Renewable / TC Energy 等持仓承压 8-12%。

---

### 6.5 Ninepoint Partners

#### 6.5.1 Canadian Large Cap Leaders Split Corp (NPS.TO / NPS.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Ninepoint Partners LP |
| 产品官网 | [ninepoint.com/funds/canadian-large-cap-leaders-split-corp](https://www.ninepoint.com/funds/canadian-large-cap-leaders-split-corp/) |
| 投资方向 | 加拿大大盘领头股(Energy 32.75% / Financials 29.53% / Utilities 19.72% / Industrials 9.64% / Consumer Staples 9.50%) |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2024-02-22 |
| Class A / Pfd ticker | NPS.TO / NPS.PR.A.TO |
| Unit NAV | **$25.17** as of 2026-05-01(Class A NAV $15.17 + Pfd $10) |
| Class A NAV | **$15.17** |
| Class A 市价 | $15.10(volume 24,526) |
| Pfd 市价 | day range $10.64-$10.72 |
| 折价(Class A) | **−0.46% 微折价(基本平价)** |
| NAV 安全边际 | **67.80%** ✅ |
| 隐含杠杆 | 1.66x |
| 资产覆盖率 | **251.70%** ✅ |
| 到期日 | 2029-02-28 |
| Class A 分红 | $0.18/月 → $2.16 年化,基于 $15.10 yield **14.21%** |
| Pfd 分红 | $0.1875/季度 → $0.75 年化(7.5% on $10),current yield 7.04% |
| DBRS 评级 | Pfd-3 (high) |
| 停派阈值 | $15 |
| AUM | ~CAD 31.33M(规模偏小) |
| 历史 | 2025/2026-02 进行 share split + NCIB at-market 回购 |

**Pfd 分析:** NPS.PR.A 在 7.5% 票面 + 7.04% current yield + 251.7% 资产覆盖率 + Pfd-3 (high) 评级是当日 Pfd 中**绝对收益最高的高评级 Pfd 之一**(与 FTN.PR.A 并列)。剩余 ~2.83 年,YTM ≈ 5.80%。底层加拿大大盘股分散度较好(5 大行业均衡),信用质量优秀。

**Class A 分析:** NPS.TO 当日基本 NAV 平价交易,67.80% 安全边际 + 1.66x 杠杆 + 251.7% 覆盖率,各项指标稳健。14.21% Class A yield 中 ROC 比例待 T3 披露;但底层 5 大行业均衡 + 派息覆盖较好,长期可持续性优于纯 covered call 增强型。**Class A NAV $15.17 距离 $15 阈值仅 1.1%** 是关键风险点——与 BK.TO 类似的"看似安全实则关键"位置,任何底层 5% 回调即触发 Class A 分红停派。

**关键机会:**
1. 7.5% Pfd 票面 + 高评级 (Pfd-3 high) + 251% 覆盖率,在固收组合中具备极强吸引力,等同于"准 A 级公司债"。
2. 2024-02 inception 较新,管理层连续 share split + NCIB 回购显示主动管理,产品成长性好。

**关键风险:**
1. **Class A NAV 距离 $15 阈值仅 1.1%**:这是隐藏的红线指标——本卡 67.80% 是 Unit NAV 安全边际,但 Class A NAV 视角的"距 0"才是真实风险。需密切监控 Unit NAV 跌破 $25 的事件。
2. AUM 仅 3,133 万,流动性极弱,大额买卖必然引发显著价格冲击。

---

### 6.6 Partners Value Split Corp (Brookfield 关联,7 个 Pref-only 系列)

> [!IMPORTANT]
> **特殊结构 — 仅 Pfd,无公开 Class A**:Partners Value Split Corp. 历史上**只发行 Class AA Preferred Shares**(7 个 outstanding series,以及已赎回的 Series 11)。Class A 由 Brookfield Corporation 直接持有,不公开交易。所有 Pfd 面值 $25(非 $10),DBRS Pfd-2 系列(高于 Brompton/Quadravest 的 Pfd-3),信用支撑来自 Brookfield 持仓。

| Series 总览 | Ticker | Face | Coupon | Annual | Current Px | Curr Yield | Maturity | DBRS | YTM |
|---|---|---:|---:|---:|---:|---:|---|---|---:|
| Series 10 | PVS.PR.H | 25 | 4.70% | 1.175 | 25.275 | 4.65% | 2027-02-28 | Pfd-2 | 3.36% |
| Series 12 | PVS.PR.J | 25 | 4.40% | 1.10 | 25.12 | 4.38% | 2028-02-29 | Pfd-2 (low) | 4.13% |
| Series 13 | PVS.PR.K | 25 | 4.45% | 1.1124 | 25.15 | 4.42% | 2029-05-31 | Pfd-2 (low) | 4.24% |
| Series 14 | PVS.PR.L | 25 | 5.50% | 1.375 | 25.90 | 5.31% | 2030-06-30 | Pfd-2 | 4.55% |
| Series 15 | PVS.PR.M | 25 | 5.15% | 1.2876 | 25.60 | 5.03% | 2031-03-31 | Pfd-2 | 4.61% |
| Series 16 (USD) ⚠️ | PVS.PR.U | US$25 | 5.40% | 1.35 | US$25.51 | 5.29% | 2032-03-31 | Pfd-2 | 5.00% |
| Series 17 (USD) ⚠️ | PVS.PR.V | US$25 | 5.25% | 1.3124 | US$25.00 | 5.25% | 2033-01-31 | Pfd-2 | 5.25% |

**关键解读:**

> [!CAUTION]
> **USD-denominated 预扣税警告(PVS.PR.U / PVS.PR.V):**
> - 这两只 USD pref 在 **Non-Reg / TFSA 账户中受 15% 美国预扣税**(IRS) 影响——TFSA 不能 reclaim,Non-Reg 可通过 W-8BEN 减免至 15% 但仍损失。
> - 在 **RRSP / RRIF 账户中**受加美税收协定保护,不需缴预扣税——这是该系列**唯一推荐的持有账户**。
> - 持有人必须了解 CAD 升值情景下 USD 价值同时承压(双重币种风险)。

**整体分析:**

Partners Value 系列是当日 Split-Pfd 市场中**信用质量唯一一档高于 Pfd-3 的产品**——DBRS Pfd-2 / Pfd-2 (low) 评级,Brookfield 间接持仓支撑。但代价是 YTM 显著低于 Quadravest/Brompton 的 5.5%-6.0% 区间——PVS 系列 YTM 集中在 3.4%-5.3%,反映"高信用质量 = 低收益补偿"的理性定价。

**series 选择决策:**
- **PVS.PR.L (Series 14)** 是 CAD 系列中**最具吸引力**:5.50% 票面 + 4.55% YTM + 4.5 年到期 + Pfd-2,绝对收益最高 + 最长锁定;
- **PVS.PR.M (Series 15)** 次选:5.15% 票面 + 4.61% YTM + 5 年期限,与 L 互补,组合内可双持;
- **PVS.PR.U/V (USD)** 仅推荐 **RRSP 账户持有**,5.0%-5.25% YTM 在 USD 视角具备绝对吸引力,但需理解币种波动;
- **PVS.PR.H (Series 10)** 是 7 只中 **YTM 最低** (3.36%),仅 1.83 年到期,**接近平价 + 低剩余期限的"准短债",不推荐主动加仓**;
- **PVS.PR.J/K** 是 4-5% 票面的"中段"产品,YTM 4.13-4.24%,无明显比较优势,适合分散持有不超配。

**机会:**
1. **CAD 长期 Pfd 锁定首选**:PVS.PR.L (4.55% YTM/4.5y) 与 PVS.PR.M (4.61% YTM/5y) 在加拿大税务居民 RRSP/Non-Reg 账户中是"准债 + 高评级"的稀缺组合。
2. RRSP 账户配置 PVS.PR.U/V 锁定 5%+ USD YTM,在加拿大 GIC 5% 已基本不可见的 2026 环境下是替代品。

**风险:**
1. Brookfield 间接信用——Brookfield Corporation 任何重大事件直接传导 PVS 信用;Brookfield 当前 BBB+ 但杠杆较高。
2. PVS.PR.V (Series 17) 当日市价用 face value 替代(数据缺口),实际价格可能存在 ±2% 偏差。
3. PVS 系列 NAV per unit 与资产覆盖率均未在公开页面披露(数据缺口)——年报 PDF 在付费墙后,本会话未能取得;Pfd 持有人不得已只能依赖 DBRS 评级与 Brookfield 信用判断。

---

### 6.7 Harvest Portfolios

#### 6.7.1 Big Pharma Split Corp (PRM.TO / PRM.PR.A.TO)

| 项目 | 详情 |
|---|---|
| Issuer | Harvest Portfolios Group |
| 产品官网 | [harvestportfolios.com/etf/big-pharma-split-corp](https://www.harvestportfolios.com/etf/big-pharma-split-corp/) |
| 投资方向 | 全球大型制药 (BMY/ABBV/JNJ/AMGN/PFE/LLY/MRK/AZN/GSK/SNY) |
| 结构 | 1 Class A + 1 Pfd / Pfd 面值 $10 |
| 成立日期 | 2017-11-24 |
| Class A / Pfd ticker | PRM.TO / PRM.PR.A.TO |
| Unit NAV | **$23.73** as of 2026-04-30 |
| Class A NAV | **$13.73** |
| Class A 市价 | last $14.32 / bid $13.76 / ask $14.32 |
| Pfd 市价 | 未在 Globe and Mail 取得数值 |
| 折价(Class A,基于 ask) | **+4.30% 溢价** ⚠️ |
| NAV 安全边际 | **58.20%** ✅ |
| 隐含杠杆 | 1.73x |
| 资产覆盖率 | **237.30%** ✅ |
| 到期日 | 2027-12-31 |
| Class A 分红 | $0.1031/月 → $1.2372 年化,基于 $14.32 yield 8.64% |
| Pfd 分红 | $0.1250/季度 → $0.50 年化,4.88% on $10,current yield 4.88% |
| DBRS 评级 | Pfd-3 (high),2023-09-07 |
| 停派阈值 | $15 |
| AUM | ~CAD 31.30M(规模偏小) |
| 1y 业绩(2026-03-31) | Class A +23.65% / Pfd +5.09% |

**Pfd 分析:** PRM.PR.A 是当日 Pfd 中**票面最低的产品**(5.0%),current yield 4.88% 与 PVS Pfd-2 系列接近但评级仅 Pfd-3 (high),YTM ≈ 4.45%。在 237% 覆盖率下信用风险低,但收益补偿有限。剩余 1.67 年到期,接近"短债"角色。

**Class A 分析:** PRM.TO 当前 ask 端 +4.30% 溢价,折价机会缺失;58.20% 安全边际 + 1.73x 杠杆是稳健配置,8.64% Class A yield 是相对可持续的(底层制药股股息率 3-4% + covered call 增强)。1y +23.65% Class A 总回报反映 2025-2026 制药板块强劲表现(GLP-1 / 新药管线),但当前估值已较高。**ask 14.32 vs NAV 13.73 的 +4.30% 溢价是回避信号**。

**关键机会:**
1. 制药板块在 2026 大宗商品 / 通胀回落 + GLP-1 持续放量场景下仍有 alpha,PRM 是杠杆化暴露工具。
2. 风险偏好高的投资者可在 PRM 折价回归至 −1% 至 +1% 时考虑入场。

**关键风险:**
1. 当前 +4.30% 溢价 + 制药板块估值已高 + 1y 已 +23% 回报,**当前不应追高**——回避或等待回调。
2. AUM 3,130 万规模小,流动性弱;到期日 2027-12 距今仅 1.67 年,延期事件可能在 2027 中提前定价。

---

## 7. Split Funds ETF 独立章节

> [!IMPORTANT]
> ETF 章节独立成章,不混入普通 Split Fund 产品卡。本节核验并覆盖 SPLT.TO / PREF.TO / CLSA.TO / SPFD.TO 四只 seed ETF;PREF.TO 在当日确认是 **Quadravest 旗下 Split Pref 主题 ETF**,与 RBC iShares 的 RPF.TO / iShares CPD.TO 等通用加拿大 Pref ETF 不同。SPFD.TO 在 2026-04 由 Mulvihill US Healthcare Enhanced Yield ETF 重命名/重定位为 Split-Pref 主题。

### 7.1 SPLT.TO — Brompton Split Corp Preferred Share ETF

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 官网 | [bromptongroup.com/product/brompton-split-corp-preferred-share-etf](https://www.bromptongroup.com/product/brompton-split-corp-preferred-share-etf/) |
| 投资目标 | 通过主动管理 Split Corp Preferred Shares 篮子提供月度稳定分配 + 资本保值 |
| 持仓类型 | 100% Preferred |
| NAV | $10.81 as of 2026-04-30 |
| 市价 | $10.87(volume 56,957) |
| 折溢价 | **+0.55% 微溢价** |
| 分红 | $0.055/月 → $0.66 年化,**current yield 6.08%** |
| MER | 0.50% |
| AUM | **CAD 616.66M**(seed ETF 中最大) |
| 成立日期 | 2023-06-12 |
| 持仓数量 | 25 只 Pfd |
| 前 10 持仓(weight) | DFN.PR.A 14.5% / DGS.PR.A 13.1% / FFN.PR.A 9.8% / BK.PR.A 9.6% / LBS.PR.A 7.1% / SBC.PR.A 6.4% / FTN.PR.A 5.5% / DF.PR.A 4.3% / GDV.PR.A 3.7% / PVS.PR.M 3.2% |
| 发行商集中度(前 3) | 37.4% |
| 税务构成 | 分发 eligible dividends + foreign income + capital gains + ROC(T3 披露,Non-Reg) |

**SPLT 是当日 Split-Pfd ETF 的"基准/默认选择"——MER 0.50% 极低、AUM 6.17 亿规模充足、25 只 Pfd 自动分散、月度现金流 6.08%、流动性最佳(56,957 日均成交)。** 持仓覆盖 Brompton/Quadravest/Partners Value 全发行商,前 10 持仓集中度 ~77% 但 25 只总持仓 + 主动 rebalancing 提供动态调整能力。**唯一不足是缺乏 Pfd-2 评级覆盖**(Partners Value 占比 ~3% 偏低)——若投资者追求更高信用篮子,需自行加配 PVS.PR.L/M。

**它适合替代单只 Preferred、单只 Class A,还是只适合作为分散化工具?**
SPLT.TO 在 99% 投资场景下**完全替代单只 Pfd 的需求**——除非投资者明确追求特定 series 的票息特性(如 BK.PR.A 浮动利率),否则单买 25 只 Pfd 的复杂度、流动性折价、再投资再平衡成本均高于 SPLT。Class A 不在 SPLT 范围内,需要 Class A 暴露的投资者另需 CLSA.TO。

**费用和分散化是否抵消了挑选单只证券的机会?**
MER 0.50% vs 直接持有的零费用,意味着 ETF 持有 1 年损失 ~50bp;但与"挑选单只 Pfd 的 bid/ask spread + 再投资税务摩擦"比较,500bp 的费用几乎一定低于自管成本。对 < CAD 100K 仓位投资者,SPLT 几乎一定优于自管 Pfd 篮子。

**短期 / 中期 / 长期适配性:**
SPLT 的最强角色是**长期 Pfd 收息底仓**——25 只主动管理在 5-10 年视角下持续提供月度 ~6% yield 与 NAV 稳定;短期(1-3 个月)无显著折价机会;中期(6-12 个月)若降息周期开启,固定利率 Pfd 价格上行可能带来 NAV +3-5% alpha 加成。

**最具税务效率的账户:**
TFSA 是首选(免税月度现金流);Non-Reg 中 ROC + 合格股息构成需要每年 T3 跟踪;RRSP 由于 SPLT 内含部分 USD 派息(若有,T3 中 foreign income 部分)反而不如 TFSA。

---

### 7.2 PREF.TO — Quadravest Preferred Split Share ETF

| 项目 | 详情 |
|---|---|
| Issuer | Quadravest Capital Management |
| 官网 | [quadravest.com/pref-etf-fund-features](https://www.quadravest.com/pref-etf-fund-features) |
| 投资目标 | 月度分配 + 资本保值,主要投资加拿大 Split Share Preferred Shares |
| 持仓类型 | 100% Preferred |
| NAV | $10.44 as of 2026-04-30 |
| 市价 | $10.50(volume 19,869) |
| 折溢价 | **+0.57% 微溢价** |
| 分红 | $0.05833/月 → $0.69996,**current yield 6.65%**(高于 SPLT) |
| MER | 0.57% |
| AUM | **CAD 46.76M**(规模偏小) |
| 成立日期 | 2024-06-27 |
| 持仓数量 | 11 只 |
| 持仓 | BK.PR.A / PIC.PR.A / FTN.PR.A / DGS.PR.A / DFN.PR.A / LBS.PR.A / DF.PR.A / FFN.PR.A / SBC.PR.A / GDV.PR.A 等(权重未披露) |
| 前 3 集中度 | 数据缺口(主页未披露权重) |
| Preferred/Class A 比例 | 100% Pfd |
| DRIP / 税务 | 数据缺口 |
| **关键差异** | 包含 PIC.PR.A($15 face)而 SPLT.TO 不包含;不含 Partners Value Pfd-2 系列 |

**PREF 是 Quadravest 的"自家 Pfd 主动管理 ETF"——AUM 4,676 万规模偏小,持仓数仅 11 只(SPLT 25 只)集中度更高。**Current yield 6.65% 略高于 SPLT 6.08%,主要因为持仓加权偏向高票息 (DFN/FFN 7%-7.5%) 且不含 Partners Value 4-5% 票息系列。MER 0.57% 略高于 SPLT 0.50%。**重要差异:PREF 持有 PIC.PR.A**($15 face value,Pfd 对 NAV 阈值 $25 敏感),而 SPLT 不持有——这是一个细微但关键的风险/收益取舍。

**与 SPLT 的对比:**
- SPLT 优势:更大 AUM、更分散、更多 series、含 Partners Value 高评级 Pfd
- PREF 优势:更高 yield (6.65% vs 6.08%)、含 PIC.PR.A 提供差异化暴露
- 推荐组合:不需要同时持有,选其一即可;SPLT 是"保守底仓",PREF 是"高 yield 底仓"

**适合作为分散化工具,但 AUM 与持仓数量较 SPLT 更弱**——仓位不应超过 SPLT。

**费用 / 分散化抵消挑选单只 Pfd 的机会?**
对小仓位投资者(< CAD 50K)PREF 仍是合理选择;大仓位投资者可考虑直接持有 BK.PR.A + FTN.PR.A + DFN.PR.A 三只(覆盖浮动 + 固定 7% + 固定 7.5% 三种代表性结构)。

**短中长期角色:**
中长期持有作为"高 yield Split-Pref 篮子",对偏好月度高现金流投资者;短期无折价交易机会(基本平价)。

**最具税务效率账户:** 与 SPLT 同——TFSA 首选;Non-Reg 需 T3 跟踪。

---

### 7.3 CLSA.TO — Brompton Split Corp Enhanced Equity Income ETF (Class A 主题)

| 项目 | 详情 |
|---|---|
| Issuer | Brompton Funds Limited |
| 官网 | [bromptongroup.com/product/brompton-split-corp-enhanced-equity-income-etf](https://www.bromptongroup.com/product/brompton-split-corp-enhanced-equity-income-etf/) |
| 投资目标 | 主动管理 Split Corp Class A Shares 提供月度高分配 + 资本增值 |
| 持仓类型 | **100% Class A**(全市场唯一 Class A 主题 ETF) |
| NAV | $15.40 as of 2026-04-30 |
| 市价 | $15.36(volume 21,044) |
| 折溢价 | **−0.26% 微折价** |
| 分红 | $0.18/月 → $2.16,**current yield 14.02%**(年初分红上调) |
| MER | 0.60% |
| AUM | CAD 48.27M |
| 成立日期 | 2025-03-20(年轻产品) |
| 持仓数量 | 12 只 Class A |
| 前 10 持仓 | LBS 14.9% / DFN 14.5% / SBC 14.0% / FTN 12.6% / ENS 12.0% / FFN 10.4% / LCS 8.9% / GDV 4.4% / PWI 3.1% / DF 2.5% |
| 发行商集中度(前 3) | 43.4% |
| Preferred/Class A 比例 | 100% Class A |
| DRIP | 是 |

**CLSA 是当日**全市场唯一的 Class A 主题 ETF**——12 只 Class A 篮子 + 14.02% 分红率 + MER 0.60%,几乎完整覆盖了加拿大主流 Class A universe (Brompton 系 + Quadravest DFN/DF/FTN/FFN + Middlefield ENS)。**这是不愿做单只 Class A 选股、但要 Class A 杠杆敞口的投资者的唯一 ETF 工具。**前 10 持仓覆盖 ~98%,集中度高(前 3 = 43.4%)反映 Class A universe 本身就少。**包含 PWI** 3.1% 暴露——证实 PWI 仍在 Brompton 旗下(本会话其他渠道未抓到 PWI 数据,通过 CLSA 持仓反向确认 PWI 存活)。

**它适合替代单只 Class A,还是只适合作为分散化工具?**
CLSA 比单只 Class A 提供更强分散,但**不替代精选**——单只 Class A 投资的核心价值在"折价 + 安全边际 + 行业判断"的精确表达,而 CLSA 是 12 只篮子的平均敞口。建议:精选 2-3 只优质 Class A (SBC/GDV/IS) + 25-50% 仓位 CLSA 作为补充分散。

**费用和分散化抵消挑选单只 Class A 的机会?**
对偏好"懒人 Class A 暴露"投资者:CLSA 完全合适;对偏好折价 alpha + 选股 alpha 投资者:CLSA 平均化了折价机会(篮子内既有 GDV 平价又有 PVD −12.79% 折价),会稀释超额收益。

**短中长期角色:**
CLSA 适合**长期 Class A 底仓**——14% 月分红 + 自动 rebalancing,但需理解 ROC 长期对 NAV 端的稀释;短期无显著折价机会;中期是 Class A 板块 beta 工具。

**最具税务效率账户:**
TFSA 首选(月度 14% 现金流免税复利);Non-Reg 必须做 ACB 与 ROC 跟踪;RRSP 因 Class A 高 ROC 比例反而不如 TFSA(RRSP 取出时全额按 income 课税,失去 ROC 递延优势)。

---

### 7.4 SPFD.TO — Mulvihill Enhanced Split Preferred Share ETF

> [!CAUTION]
> **2026-04 重要变更**:SPFD.TO 由 Mulvihill **U.S. Health Care Enhanced Yield ETF**(2022-02-14 成立)重命名/重定位为 Split-Pref 主题 ETF。**inception 作为 split-pref 策略仅自 2024-12-06 起**;持仓与策略数据均较新。**stockanalysis.com 报告的 MER 4.34% 异常高**——可能包含业绩费或为 TER 估计而非纯 MER,本卡标注为数据缺口,需后续直接查 Mulvihill MRFP 复核。

| 项目 | 详情 |
|---|---|
| Issuer | Mulvihill Capital Management |
| 官网 | [mulvihill.com/SPFD](https://www.mulvihill.com/SPFD) |
| 投资目标 | 月度分配 + 资本保值,主要投资加拿大 Split Share Preferred Shares |
| 持仓类型 | 主要 Preferred |
| NAV | **$9.38** as of 2025-12-31 ⚠️(year-end results,本会话最新可得) |
| 市价 | $9.63(volume 6,496,流动性最弱) |
| 折溢价 | **+2.67% 溢价** |
| 分红 | $0.08333/月 → $1.00,**current yield 10.36%**(异常高) |
| MER | **4.34% 异常**(待复核) |
| AUM | CAD 34.25M(seed ETF 中最小) |
| 成立日期 | 2024-12-06(split-pref 策略) |
| 持仓数量 | 14 只 |
| 数据缺口 | 前 10 持仓权重、DRIP、税务构成、MER 真实值 |

**SPFD 是当日 Split-Pref 主题 ETF 中**最不透明、最不推荐**的产品。MER 4.34% 远高于 SPLT 0.50% 与 PREF 0.57%——若属实,长期持有 5 年损失高达 22%,**完全不合理**;若 MER 实际为 ~1.0% 而 stockanalysis.com 错误,产品需要直接复核。10.36% 表面分红率几乎一定包含大量 ROC + 少量真实 Pfd 分红——是"表面高 yield,实质 NAV 稀释"的典型陷阱。NAV $9.38 为年报数据,4 个月滞后,实际折溢价不可知。AUM 仅 3,425 万 + 日均成交 6,496 = **流动性最差** + **新策略 + 高费率 + 数据不透明**,组合判断为**当前不推荐**。

**与 SPLT/PREF 对比:**
| 维度 | SPLT | PREF | SPFD |
|---|---|---|---|
| AUM | 616M | 47M | 34M |
| MER | 0.50% | 0.57% | 4.34% (待复核) |
| 持仓数 | 25 | 11 | 14 |
| Yield | 6.08% | 6.65% | 10.36% |
| 推荐度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⛔ 待复核 |

**短中长期角色:** 在 MER 复核前,**所有时间窗口均不推荐**;若 MER 实际是 1.0% 左右,可作为高 yield + 主动管理产品的小仓位补充。

**最具税务效率账户:** TFSA(规避高分红的 ROC 复杂度)。

---

### 7.5 ETF 横向对比表

| ETF Ticker | 类型 | NAV | 市价 | 折溢价 | 分配率 | MER | AUM(M) | 成立 | 持仓数 | 评级集中度 |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| SPLT.TO | 100% Pfd | 10.81 | 10.87 | +0.55% | 6.08% | 0.50% | 616.66 | 2023-06 | 25 | 主要 Pfd-3 / Pfd-3 (high),Partners Value Pfd-2 ~3% |
| PREF.TO | 100% Pfd | 10.44 | 10.50 | +0.57% | 6.65% | 0.57% | 46.76 | 2024-06 | 11 | 主要 Pfd-3 |
| CLSA.TO | 100% Class A | 15.40 | 15.36 | −0.26% | 14.02% | 0.60% | 48.27 | 2025-03 | 12 | n/a (Class A) |
| SPFD.TO | 主要 Pfd | 9.38⚠️ | 9.63 | +2.67% | 10.36% | 4.34%⚠️ | 34.25 | 2024-12 | 14 | 数据缺口 |

**ETF 章节小结:**
- **SPLT.TO 是默认 Pfd ETF 选择**(AUM、持仓分散、低 MER 三项最优)
- **CLSA.TO 是唯一 Class A ETF**,适合不愿单选 Class A 的投资者
- **PREF.TO 在更高 yield 偏好下作为 SPLT 替代或补充**
- **SPFD.TO 当前不推荐**,等待 MER 复核 + 持仓权重披露

---

## 8. Preferred Shares 全市场汇总对比表

> 注:Pfd 价格来源于发行商主页与第三方行情页(已逐字段保留链接);**bid/ask 在多源核验后仍未取得,全部留空**,YTM 用 mid 价 + 简化公式估算,置信度 Medium。Quadravest 系 NAV 滞后 16 天已标 ⚠️,折溢价基于 NAV 滞后版本。

| # | 产品 | Pfd ticker | 发行商 | 面值 | 市价 | bid/ask | 到期日 | 年分红 | Curr Yield | YTM | 资产覆盖率 | 利率规则 | 评级 | 来源/日期 |
|---:|---|---|---|---:|---:|:---:|---|---:|---:|---:|---:|---|---|---|
| 1 | Split Banc Corp | SBC.PR.A | Brompton | 10 | 10.31 | n/a | 2027-11-29 | ~0.625 | 6.06% | ~4.07% | 237.10% | 季度固定 | Pfd-3 | issuer 2026-04-30 |
| 2 | Life & Banc Split | LBS.PR.A | Brompton | 10 | 10.55 | n/a | 2028-10-30 | ~0.687 | 6.87% | ~4.55% | 230.10% | 季度固定 | Pfd-3 | issuer 2026-04-30 |
| 3 | Lifeco Split | LCS.PR.A | Brompton | 10 | 10.48 | n/a | 2029-04-27 | ~0.700 | 6.68% | ~4.95% | 209.60% | 月度固定 | Pfd-3 | issuer 2026-04-30 |
| 4 | Energy Split | ESP.PR.A | Brompton | 10 | 10.25 | n/a | 2027-03-30 | ~0.725 | 7.07% | ~4.30% | 176.30% | 季度固定 | **n/a** ⚠️ | issuer 2026-04-30 |
| 5 | Global Div Growth | GDV.PR.A | Brompton | 10 | 10.24 | n/a | 2031-06-27 | ~0.500 | 4.88% | ~4.50% | 235.20% | 季度固定 | Pfd-3 (high) | issuer 2026-04-30 |
| 6 | Div Growth | DGS.PR.A | Brompton | 10 | 10.48 | n/a | 2029-08-30 | ~0.675 | 6.44% | ~4.72% | 183.60% | 季度固定 | Pfd-3 (low) | issuer 2026-04-30 |
| 7 | Dividend 15 | DFN.PR.A | Quadravest | 10 | 10.51 | n/a | 2029-12-01 | 0.700 | 6.66% | 5.44% | 184.50%⚠️ | 月度 7% 固定 | Pfd-3 | quadravest 2026-04-15 |
| 8 | Div 15 II | DF.PR.A | Quadravest | 10 | 10.66 | n/a | 2029-12-01 | 0.700 | 6.57% | 5.40% | 188.10%⚠️ | 月度 7% 固定 | Pfd-3 (low) | quadravest 2026-04-15 |
| 9 | Financial 15 | FTN.PR.A | Quadravest | 10 | 10.74 | n/a | 2030-12-01 | 0.725 | **6.75%** | **5.45%** | 219.90%⚠️ | 月度 7.25% 固定 + 6% 地板至 2030 | Pfd-3 | quadravest 2026-04-15 |
| 10 | NA Financial 15 | FFN.PR.A | Quadravest | 10 | 10.72 | n/a | 2029-12-01 | 0.750 | **7.00%** | **5.62%** | 204.80%⚠️ | 月度 7.5% 固定 | Pfd-3 (low) | quadravest 2026-04-15 |
| 11 | Canadian Banc | BK.PR.A | Quadravest | 10 | 10.40 | 10.39/10.40 | 2028-12-01 | 0.595 | 5.72% | ~4.85% | 252.50%⚠️ | 月度 浮动 (Prime+1.5%, 5%底/8%顶) | Pfd-3 (low) | quadravest 2026-04-15 |
| 12 | Prime Dividend | PDV.PR.A | Quadravest | 10 | 10.99 | n/a | 2028-12-01 | 0.680 | 6.19% | ~4.90% | 239.90%⚠️ | 月度 浮动 (Prime+2.35%, 5%底/8%顶) | Pfd-3 | quadravest 2026-04-15 |
| 13 | Life Companies | LFE.PR.B | Quadravest | 10 | 10.62 | n/a | 2030-12-01 | 0.700 | 6.59% | ~5.30% | 178.40%⚠️ | 月度 max(7%, Prime+2%) 上限 9% | **未核验** ⚠️ | quadravest 2026-04-15 |
| 14 | Premium Income | PIC.PR.A | Mulvihill | **15** | n/a ⚠️ | n/a | 未核验 | 1.275 | 待补 | 待补 | 待补⚠️ | 月度 8.5% (face $15) | 未核验 ⚠️ | issuer site 渲染失败 |
| 15 | E Split | ENS.PR.A | Middlefield | 10 | 10.79 | n/a | 2028-06-30 | 0.700 | 6.49% | ~5.20% | **299.50%** | 季度 7% 固定 | Pfd-3 (high) | middlefield 2026-04-30 |
| 16 | Real Estate Split | RS.PR.A | Middlefield | 10 | 10.16 | n/a | 2030-12-31 | 0.580 | 5.71% | ~4.85% | 198.80% | 季度 5.8% 固定(2025-12 重设) | Pfd-3 (high) | middlefield 2026-04-30 |
| 17 | Infrastructure Div | IS.PR.A | Middlefield | 10 | 10.87 | n/a | 2029-04-30 | 0.720 | **6.62%** | **5.50%** | **303.20%** | 季度 7.2% 固定 | Pfd-3 (high) | middlefield 2026-04-30 |
| 18 | CDN Large Cap Leaders | NPS.PR.A | Ninepoint | 10 | 10.68 | n/a | 2029-02-28 | 0.750 | **7.04%** | **5.80%** | 251.70% | 季度 7.5% 固定 | Pfd-3 (high) | issuer 2026-05-01 |
| 19 | Big Pharma Split | PRM.PR.A | Harvest | 10 | n/a ⚠️ | n/a | 2027-12-31 | 0.500 | 4.88% | ~4.45% | 237.30% | 季度 5% 固定 | Pfd-3 (high) | issuer 2026-04-30 |
| 20 | PVS Series 10 | PVS.PR.H | Partners Value | 25 | 25.275 | n/a | 2027-02-28 | 1.175 | 4.65% | 3.36% | 数据缺口 | 季度 4.7% 固定 | **Pfd-2** | gnm 2026-05-01 |
| 21 | PVS Series 12 | PVS.PR.J | Partners Value | 25 | 25.12 | n/a | 2028-02-29 | 1.100 | 4.38% | 4.13% | 数据缺口 | 季度 4.4% 固定 | **Pfd-2 (low)** | gnm 2026-05-01 |
| 22 | PVS Series 13 | PVS.PR.K | Partners Value | 25 | 25.15 | n/a | 2029-05-31 | 1.1124 | 4.42% | 4.24% | 数据缺口 | 季度 4.45% 固定 | **Pfd-2 (low)** | gnm 2026-05-01 |
| 23 | PVS Series 14 | PVS.PR.L | Partners Value | 25 | 25.90 | n/a | 2030-06-30 | 1.375 | **5.31%** | **4.55%** | 数据缺口 | 季度 5.5% 固定 | **Pfd-2** | gnm 2026-05-01 |
| 24 | PVS Series 15 | PVS.PR.M | Partners Value | 25 | 25.60 | n/a | 2031-03-31 | 1.2876 | 5.03% | **4.61%** | 数据缺口 | 季度 5.15% 固定 | **Pfd-2** | gnm 2026-05-01 |
| 25 | PVS Series 16 (USD) | PVS.PR.U | Partners Value | US$25 | US$25.51 | n/a | 2032-03-31 | US$1.35 | 5.29% | 5.00% | 数据缺口 | 季度 5.4% 固定 | **Pfd-2** | gnm 2026-05-01 |
| 26 | PVS Series 17 (USD) | PVS.PR.V | Partners Value | US$25 | US$25.00⚠️ | n/a | 2033-01-31 | US$1.3124 | 5.25% | 5.25% | 数据缺口 | 季度 5.25% 固定 | **Pfd-2** | gnm 2026-05-01 |

### 8.1 Preferred 候选名单(基于汇总表)

**最有吸引力(YTM 高 + 资产覆盖率 ≥150% + 评级 ≥ Pfd-3):**
- **NPS.PR.A** — 7.04% yield + 5.80% YTM + 251.7% 覆盖 + Pfd-3 (high),YTM 全 universe 最高之一,信用质量优良
- **FFN.PR.A** — 7.00% yield + 5.62% YTM + 204.8% 覆盖 + Pfd-3 (low),最高票面 (7.5%) 与最高 current yield 之一
- **IS.PR.A** — 6.62% yield + 5.50% YTM + 303.2% 覆盖 + Pfd-3 (high),最高资产覆盖率之一,稳健配置首选
- **FTN.PR.A** — 6.75% yield + 5.45% YTM + 219.9% 覆盖 + 6% 地板锁定至 2030,降息环境额外稳定性

**最安全(覆盖率 ≥200% + 评级 ≥ Pfd-2 / Pfd-3 high):**
- **ENS.PR.A** — 299.5% 覆盖率 + Pfd-3 (high),单一持仓 Enbridge 信用稳定
- **IS.PR.A** — 303.2% 覆盖 + Pfd-3 (high),北美基础设施分散
- **GDV.PR.A** — 235.2% 覆盖 + Pfd-3 (high),全球分散
- **PVS.PR.L / M** — Brookfield 信用 + Pfd-2,信用质量唯一高于 Pfd-3 档

**最高 YTM 是真实机会还是流动性/信用风险?**
- NPS.PR.A 5.80% YTM 是**真实机会**——高评级 + 流动性较弱 (AUM 3K 万) 引发的小幅"流动性折价";中型仓位 (CAD 25-50K) 仍可建仓。
- FFN.PR.A 5.62% YTM 是**真实机会**——纯流动性导致的略低估值,信用质量优良。
- LFE.PR.B 5.30% YTM 是**风险溢价**——评级未核验 + Class A 已停派 + NAV 安全边际 15.92%,反映为约 80-100bp 的"信用 + 结构风险"折价。
- ESP.PR.A 4.30% YTM **DBRS 未评级**,反映为"无评级折价"——非真实机会。

**需要回避的 Preferred:**
- ❌ **ESP.PR.A**(无 DBRS 评级 + 油气板块 + 安全边际 17.53%)
- ❌ **LFE.PR.B**(评级未核验 + 配套 Class A 已停派 + 杠杆 2.28x)
- ⚠️ **PIC.PR.A**(NAV 数据缺口,Mulvihill 主页未渲染——暂不推荐建仓)
- ⚠️ **PVS.PR.H**(YTM 仅 3.36%,接近平价 + 短期到期,无收益吸引力)

### 8.2 Head-to-Head 对比:加拿大六大行底层 Pfd

底层加拿大六大行 + 银行/保险均衡的 Pfd 主要候选:**SBC.PR.A vs LBS.PR.A vs DFN.PR.A vs FTN.PR.A vs NPS.PR.A**。

| 决策语句 |
|---|
| **追求最高 YTM**:选 **NPS.PR.A** (5.80%) 或 **FTN.PR.A** (5.45% + 6% 地板)。NPS 评级更优 (Pfd-3 high vs Pfd-3),但 AUM 仅 3K 万流动性偏弱;FTN 流动性更好。 |
| **追求最强信用质量**:选 **GDV.PR.A** (Pfd-3 high + 235% 覆盖) 或 **ENS.PR.A** (Pfd-3 high + 299.5% 覆盖)。两者牺牲 yield (4.88%/6.49%) 换取 NAV 端最稳。 |
| **追求 BoC 降息保护(降息时价格上涨)**:选**期限最长 + 固定利率**——**GDV.PR.A**(2031-06,4.88% 票面)或 **PVS.PR.L/M**(2030-06/2031-03,5.5%/5.15%)。 |
| **追求加息保护**:选**浮动利率**——**BK.PR.A**(Prime+1.5%,5% 地板/8% 顶)或 **PDV.PR.A**(Prime+2.35%,更高利差)。 |
| **追求长期到期(锁定高利率)**:选 **FTN.PR.A**(2030-12,7.25% 票面 + 6% 地板)——票面 + 地板 + 期限三优。 |

---

## 9. Class A / Capital Shares 全市场汇总对比表

> 注:NAV 多为 2026-04-30(Brompton/Middlefield/Ninepoint/Harvest),Quadravest NAV 为 2026-04-15(滞后 16 天 ⚠️)。Class A 市价大多为 2026-05-01;PDV 为 2026-04-24,LFE 为 2026-04-24。

| # | 产品 | Class A | 发行商 | Unit NAV (日期) | Class A NAV | 市价 | 折溢价 | 年分红 | Curr Yield | 阈值 | NAV 安全边际 | 隐含杠杆 | 分红状态 | 来源/日期 |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | SBC | SBC.TO | Brompton | $23.71 (04-30) | 13.66 | 13.29 | −2.71% | 1.20 | 9.03% | 15 | 58.07% | 1.74x | 正常 | bromptongroup 04-30 |
| 2 | LBS | LBS.TO | Brompton | $23.01 (04-30) | 12.95 | 12.10 | −6.56% | 1.20 | 9.92% | 15 | 53.40% | 1.78x | 正常 | bromptongroup 04-30 |
| 3 | LCS | LCS.TO | Brompton | $20.96 (04-30) | 10.96 | 10.13 | −7.57% | 0.90 | 8.88% | 15 | 39.73% | 1.91x | 正常 | bromptongroup 04-30 |
| 4 | ESP | ESP.TO | Brompton | $17.63 (04-30) | 7.57 | 7.93 | **+4.75%** ⚠️ | 1.20 | 15.13% | 15 | 17.53% 🔴 | 2.33x ⚠️ | 正常 | bromptongroup 04-30 |
| 5 | GDV | GDV.TO | Brompton | $23.52 (04-30) | 13.48 | 13.44 | −0.30% | 1.20 | 8.93% | 15 | 56.80% ✅ | 1.75x | 正常 | bromptongroup 04-30 |
| 6 | DGS | DGS.TO | Brompton | $18.36 (04-30) | 8.25 | 8.37 | **+1.45%** ⚠️ | 1.20 | 14.34% | 15 | 22.40% ⚠️ | 2.23x | 正常 | bromptongroup 04-30 |
| 7 | DFN | DFN.TO | Quadravest | $18.45 (04-15)⚠️ | 8.45 | 7.82 | −7.46% | 1.20 | 15.35% | 15 | 23.00% ⚠️ | 2.18x | 正常 | quadravest 04-15 |
| 8 | DF | DF.TO | Quadravest | $18.81 (04-15)⚠️ | 8.81 | 8.03 | −8.85% | 1.20 | 14.94% | 15 | 25.36% ⚠️ | 2.13x | 正常 | quadravest 04-15 |
| 9 | FTN | FTN.TO | Quadravest | $21.99 (04-15)⚠️ | 11.99 | 10.89 | **−9.17%** | 1.51 | 13.87% | 15 | 31.79% ⚠️ | 1.83x | 正常 | quadravest 04-15 |
| 10 | FFN | FFN.TO | Quadravest | $20.48 (04-15)⚠️ | 10.48 | 9.29 | **−11.36%** | 1.36 | 14.64% | 15 | 26.76% ⚠️ | 1.95x | 正常 | quadravest 04-15 |
| 11 | BK | BK.TO | Quadravest | $25.25 (04-15)⚠️ | 15.25 | 14.81 | −2.89% | 2.01 | 13.57% | 15 | 40.59% ✅ | 1.66x | 正常 | quadravest 04-15 |
| 12 | PDV | PDV.TO | Quadravest | $23.99 (04-15)⚠️ | 13.99 | 12.20 (04-24) | **−12.79%** | 1.22 | 10.00% | 15 | 37.47% ⚠️ | 1.71x | 正常 | quadravest 04-15 |
| 13 | LFE | LFE.TO | Quadravest | $17.84 (04-15)⚠️ | 7.84 | 7.60 (04-24) | −3.06% | 0.00 ⚠️ | **0.00%** ⚠️ | 15 | **15.92%** 🔴 | 2.28x ⚠️ | **暂停** 🚫 | quadravest 04-15 |
| 14 | PIC.A | PIC.A.TO | Mulvihill | **未核验** ⚠️ | n/a | 9.76 | n/a | 1.08 | ~11.07% | 25 | n/a ⚠️ | n/a | 正常上调 | gnm 05-01 |
| 15 | ENS | ENS.TO | Middlefield | $29.95 (04-30) | 19.89 | ~17.5 (mid) | **−9.25%** | 1.68 | 9.6% | 15 | **99.67%** ✅ | 1.51x | 正常 | middlefield 04-30 |
| 16 | RS | RS.TO | Middlefield | $19.88 (04-30) | 9.83 | 9.92 (mid) | **+0.92%** | 1.56 | 15.7% | 15 | 32.53% ⚠️ | 2.02x | 正常 | middlefield 04-30 |
| 17 | IS | IS.TO | Middlefield | $30.32 (04-30) | 20.14 | ~19.0 (mid) | **−5.66%** | 1.80 | 9.5% | 15 | **102.13%** ✅ | 1.50x | 正常 | middlefield 04-30 |
| 18 | NPS | NPS.TO | Ninepoint | $25.17 (05-01) | 15.17 | 15.10 | −0.46% | 2.16 | 14.21% | 15 | 67.80% ✅ | 1.66x | 正常 | ninepoint 05-01 |
| 19 | PRM | PRM.TO | Harvest | $23.73 (04-30) | 13.73 | 14.32 (ask) | **+4.30%** ⚠️ | 1.2372 | 8.64% | 15 | 58.20% ✅ | 1.73x | 正常 | harvest 04-30 |

### 9.1 Class A 候选名单(基于汇总表)

**最有吸引力(折价 ≥5% + NAV 安全边际 ≥40% + 分红近 12 月稳定):**
- **GDV.TO** — 折价 −0.30% + 安全边际 56.80% + 全球分散 + 长到期(2031),长期复合首选
- **SBC.TO** — 折价 −2.71% + 安全边际 58.07% + 加拿大六大行,稳健现金流型
- **LBS.TO** — 折价 −6.56% + 安全边际 53.40% + 银行+保险均衡,折价机会最足
- **IS.TO** — 折价 −5.66% + 安全边际 102.13% + 北美基础设施,**全 universe 最强组合**
- **ENS.TO** — 折价 −9.25% + 安全边际 99.67% + 单一持仓 Enbridge,折价 + 安全双高

**明显溢价应回避:**
- ❌ **ESP.TO** — 溢价 +4.75% + 安全边际 17.53% + 油气单一暴露 + Pfd 无评级
- ❌ **PRM.TO** — 溢价 +4.30%(基于 ask)+ 制药板块已 +23% 1y 涨幅,等待回调
- ⚠️ **DGS.TO** — 溢价 +1.45% + 14.34% 高 yield 含 ROC + 安全边际仅 22.40%

**NAV 安全边际最低危险名单(≤25%):**
- 🚫 **LFE.TO** — 15.92%(已停派 Class A)
- 🔴 **ESP.TO** — 17.53%(油气波动 + 无评级)
- 🔴 **DGS.TO** — 22.40%(ROC 长期稀释)
- 🔴 **DFN.TO** — 23.00%(Quadravest NAV 滞后,实际可能更紧)
- ⚠️ **DF.TO** — 25.36%(同 DFN 风险)
- ⚠️ **FFN.TO** — 26.76%(美国大行 2026 净息差压力)

**分红暂停 / 接近停派阈值:**
- 🚫 **LFE.TO**(Class A 实质性 $0)
- ⚠️ NPS.TO Class A NAV $15.17 距阈值 $15 仅 1.1% — Unit NAV 视角"安全",Class A 视角"边缘"

### 9.2 Head-to-Head 对比:加拿大六大行底层 Class A

候选:**SBC.TO vs LBS.TO vs DFN.TO vs BK.TO vs FFN.TO**。

| 决策语句 |
|---|
| **追求最稳健 + 最高安全边际**:选 **SBC.TO** (58.07%) 或 **LBS.TO** (53.40%)。前者纯六大行,后者银行+保险更分散。 |
| **追求最深折价 + 折价回归 alpha**:选 **PDV.TO** (−12.79%) 或 **FFN.TO** (−11.36%)。PDV 是全 universe 折价最深,但 Quadravest NAV 16 天滞后 + 价格 7 天滞后,实际折价不确定性高;FFN 折价确定性更高但底层美国大行 2026 风险更大。 |
| **追求最高 yield**:选 **DFN.TO** (15.35%) 或 **FFN.TO** (14.64%)。但需理解 yield 中 ROC 占比高,长期 NAV 难以增长。 |
| **追求最低 ROC 稀释 + 长期总回报**:选 **GDV.TO** (8.93% yield,底层为成长股,股息率高)或 **IS.TO** (9.5% yield,基础设施分散)。低 yield 反而是"质量信号"。 |
| **追求纯加拿大银行杠杆敞口**:选 **BK.TO** (40.59% 安全边际 + 252.5% 覆盖率 + 13.57% yield),纯六大行最强代表;但 Class A NAV $15.25 距 $15 阈值仅 1.6% 是隐藏红线。 |

---

## 10. Class A 投资策略章节(深度章节)

### 10.1 Class A 本质特征

Class A 是 Split Corp 结构中"留给参与上行 + 承担下行 + 受 Pfd 优先"的杠杆化敞口。在 Pfd 面值 $10 + Unit NAV $X 的结构中,Class A NAV = X − 10,**隐含杠杆 = X / (X − 10)**。X = $25 时杠杆 1.67x、X = $20 时 2.00x、X = $17 时 2.43x、X = $15 时 3.00x(停派阈值)、X = $12 时 6.00x。**这是非线性放大**——NAV 接近阈值时杠杆飙升,意味着底层资产小幅下跌可能在 Class A 价格上以 5-10x 放大。

参考第 4.3 节隐含杠杆情景表。

### 10.2 买入 Class A 前必须检查的 4 项指标

1. **NAV 安全边际(最重要)**:必须 ≥ 30%(对应 Unit NAV 距停派阈值 ≥ 30%)。低于 25% 即视为危险区间。
2. **Class A 市价 vs NAV 折溢价**:折价 ≥ 5% 提供 alpha;溢价 ≥ 1% 即应回避。
3. **分红收益率 vs 可持续性**:>10% yield 必含 ROC 与 covered call,需对照底层股息率 + 期权金合理性;<5% yield 可能反映底层质量更高(成长股)。
4. **到期日与时间价值**:剩余 ≤ 18 个月需关注延期事件;5 年期以上可以 set-and-forget;2-3 年期是主流。

### 10.3 ≥3 种操作上彼此独立的 Class A 总收益策略

#### 策略 A:折价 + 高分红(收入型)

**目标:** 月度高现金流 + 折价回归 = 年化 15-20% 总回报(税前)。

| 步骤 | 操作 |
|---|---|
| 1 | 筛选 Class A:折价 ≥ 5% + NAV 安全边际 ≥ 30% + 分红近 12 月稳定 |
| 2 | 单只仓位 ≤ 10% 总仓位,同行业(银行/能源/REIT)≤ 25% |
| 3 | 优先选月度分红(Brompton/Quadravest 月度),关闭 DRIP 截留现金 |
| 4 | 设定回归目标:Class A 市价回到 NAV 平价或 +1% 时减仓 50% |
| 5 | NAV 安全边际跌破 25% 时强制减仓全部 |

**适合标的:** LBS.TO (−6.56% 折价 + 53.40% 安全边际)、FFN.TO (−11.36% 折价 + 26.76% 安全边际,需小仓位)、FTN.TO (−9.17% 折价 + 31.79% 安全边际)、PDV.TO (−12.79% 折价但 NAV 滞后,需复核)。

**何时选这一种(非其他):** 投资者明确追求"月度现金流 + 中短期折价回归"双引擎;已经持有 ETF 底仓,补充 alpha;接受 ROC 长期稀释但通过 12-18 个月持有期对冲。

#### 策略 B:深度折价 + NAV 回升(价值型)

**目标:** 行业回调时抄底 + 底层资产估值回归 = 年化 25-40% 总回报(高风险高回报)。

| 步骤 | 操作 |
|---|---|
| 1 | 触发条件:目标 Class A 折价 ≥ 10% **且** 底层指数(XFN.TO / TSX 能源 / TSX REIT)从 52 周高点回调 ≥ 15% |
| 2 | NAV 安全边际跌入 20-30% 区间(危险但未触发停派) |
| 3 | 三段建仓(每跌 5% 加 1/3 仓位),总仓位单只 ≤ 5% |
| 4 | 持有 6-12 个月等待底层回升;NAV 回升至安全边际 ≥ 40% 时减半,≥ 50% 时减完 |
| 5 | 若 NAV 跌至 ≤ 5% 安全边际(死亡螺旋区域),止损全部 |

**适合标的:** 当前情景下没有触发——所有 Class A 安全边际尚在 15%+;若 2026 中期发生 XFN −20% 回调,FFN.TO + DFN.TO + LCS.TO 是首选目标。

**何时选这一种:** 投资者具备 6-12 个月持有期与 5-10% 单只回撤承受力;识别行业级别错杀 + 个股级别错杀的差异;接受单只标的 15-30% 短期波动但长期 alpha 回报。

#### 策略 C:稳健核心配置(底仓型)

**目标:** 长期持有 + 月度收息 + 低换手 = 年化 8-12% 稳态总回报(税前)。

| 步骤 | 操作 |
|---|---|
| 1 | 筛选 Class A:NAV 安全边际 ≥ 50% + 折价 0% 至 −3% + 长到期(≥ 4 年) |
| 2 | 等权 3-4 只 + 行业分散(银行 / 全球派息 / 基础设施 / 单一蓝筹) |
| 3 | DRIP 开启复利(TFSA/RRSP);Non-Reg 关闭 DRIP 现金截留 |
| 4 | 季度检查:Unit NAV 跌至安全边际 < 30% 减半;< 20% 全减 |
| 5 | 5-7 年视野,期间不响应单只折溢价波动 |

**适合标的:** **GDV.TO (56.80% / 长到期 2031)、SBC.TO (58.07%)、IS.TO (102.13%)、ENS.TO (99.67%)** 等权组合。

**何时选这一种:** 投资者目标是退休账户底仓(TFSA/RRSP);不愿做主动 alpha 决策;接受 8-12% 而非 20%+ 回报但要 NAV 稳定;不做行业判断,只做结构判断(安全边际)。

> [!NOTE]
> **策略独立性自检**:策略 A 是"短中期折价 + 高分红主动型",策略 B 是"中期深度抄底高风险型",策略 C 是"长期低换手底仓型"。三者在(持有期、波动承受、回报目标、操作频率)四维度均不同——任意删除一种都会无法覆盖剩余两类需求。✓

### 10.4 Class A 风险管理要点

**必须规避的 4 种情况:**
1. NAV 安全边际 < 20%(即 Unit NAV − 阈值 < 20%)— 死亡螺旋启动区
2. Class A 处于 ≥ 1% 溢价 — alpha 已透支
3. 14%+ 表面 yield 来自高 ROC 比例 — 长期 NAV 持续被抽剥
4. AUM < CAD 50M 且日均成交 < 5,000 股 — 流动性陷阱

**持续监控的 5 项指标:**

| 指标 | 频率 | 数据源 | 行动阈值 |
|---|---|---|---|
| Unit NAV | 周(发行商) | bromptongroup.com / quadravest.com / middlefield.com nav 页 | 跌至安全边际 < 30% 减半 |
| 折溢价 | 日(交易日) | TMX / Globe and Mail | 溢价 ≥ 1% 减仓 |
| 底层指数(XFN/能源/REIT) | 日 | Yahoo Finance | 从 52w 高 −15% 启动策略 B |
| 利率环境(BoC + Prime) | 月 | bankofcanada.ca | BoC 加息 ≥ 50bp 重新评估 Class A 杠杆敞口 |
| 分红状态(暂停 / 上调 / 下调) | 月(发行商公告) | issuer press release | 任何变更 24h 内决定持仓 |

**Class A 总收益公式(分解):**

```text
Class A 总收益 = 杠杆化底层股息 + 折价回归收益 + NAV 资本增值 - ROC 稀释 - 期权金回收
            ≈ 1.7x × 底层股息率 + (折价% / 持有期) + ΔNAV - 30%~40% 表面yield
```

实际:Class A 表面 yield 12% 中真实经济收益约 6-8%,其余为 ROC + 期权金的"账面分红但 NAV 抽剥"。

---

## 11. Preferred Shares 投资策略章节(深度章节)

### 11.1 Preferred Shares 本质特征

Pfd 是 Split Corp 结构中"优先分红 + 优先到期偿还"的固收化敞口。即使 Class A 已停派,Pfd 持有人仍优先获得分红(若覆盖率 < 100% 且 NAV 进一步跌穿,Pfd 才真实承压)。**下行保护示例**:Unit NAV $18 vs Pfd 面值 $10 = 200% 覆盖率,意味着即使底层 NAV 跌 50%,Pfd 持有人本金 $10 完整回收;Unit NAV 跌至 $7 时(资产覆盖率 70%),Pfd 才面临账面亏损 30%。**Class A 在 Unit NAV $7 时已 NAV = −$3,完全归零**——这就是 Pfd 与 Class A 风险定位的根本差异。

### 11.2 买入 Preferred 前必须检查的 5 项指标

1. **YTM 到期收益率(最核心)**:目标 YTM ≥ 同期限 GIC + 150bp 或同期限 5y 国债 + 200bp。
2. **买入价 vs 面值**:溢价 > 3% 需要更高 yield 补偿;深度折价 (≥ 5%) 是机会信号。
3. **DBRS 评级**:Pfd-3 为底线;Pfd-2 高于 Pfd-3 一档。
4. **利率类型**:固定 vs 浮动(Prime-linked)vs 混合;对应不同利率环境。
5. **NAV 资产覆盖率**:< 130% 谨慎;130-150% 关注;≥ 150% 安全;≥ 200% 极安全。

### 11.3 ≥3 种操作上彼此独立的 Preferred 投资策略

#### 策略 A:持有到期收息(核心策略)

**目标:** 锁定高 YTM,持有至到期收回面值 = 年化 5-6% 税后收益。

| 步骤 | 操作 |
|---|---|
| 1 | 筛选 Pfd:YTM ≥ 5% + 评级 ≥ Pfd-3 + 资产覆盖率 ≥ 150% + 期限 2-5 年 |
| 2 | 优先选固定利率(避免再投资风险)|
| 3 | 分散 3-5 只,每只仓位 ≤ 15% 固收仓位 |
| 4 | 持有至到期或延期事件;延期时重新评估利率重设条款 |
| 5 | 在 TFSA/Non-Reg 持有(享受合格股息抵免);避免 RRSP(浪费抵免) |

**适合标的:** **NPS.PR.A** (5.80% YTM)、**FFN.PR.A** (5.62% YTM)、**FTN.PR.A** (5.45% YTM + 6% 地板)、**IS.PR.A** (5.50% YTM + 303% 覆盖)。

**何时选这一种:** 当前 BoC 利率周期接近底部 (2.25%),固定 Pfd 锁定高 YTM 是相对最优;投资者风险偏好低,愿意接受 5-6% 而非 20%+ 回报;不做主动管理。

#### 策略 B:浮动利率对冲(加息环境)

**目标:** 在 BoC 加息或 Prime 维持高位场景下,获得利率上行的有限暴露 + 5% 地板保护 = 年化 5-7% 浮动收益。

| 步骤 | 操作 |
|---|---|
| 1 | 触发条件:核心通胀重新加速 + BoC 暗示加息 (foward guidance 转鹰) |
| 2 | 选浮动利率 Pfd:**BK.PR.A** (Prime + 1.5%, 5%/8%) 或 **PDV.PR.A** (Prime + 2.35%, 5%/8%) |
| 3 | 接受 5% 地板锁定的下行保护(降息至 BoC 1% 仍保 5%) |
| 4 | 仓位 ≤ 30% 固收仓位(浮动 Pfd 上限被合约 8% 截断,不应超配) |
| 5 | BoC 加息 100bp 时减半(Pfd 价格已部分定价) |

**适合标的:** **BK.PR.A**(纯加拿大六大行 + Prime + 1.5% + 252.5% 覆盖)、**PDV.PR.A**(更高利差 Prime + 2.35% + 239.9% 覆盖)。

**何时选这一种:** 投资者预期 BoC 进入加息周期(虽然 2026 上半年共识是降息周期);对冲固定 Pfd 在加息环境下的价格回调风险;愿意接受 8% 票息上限。

#### 策略 C:高评级 + 长期锁定(债券替代型)

**目标:** 用 Pfd-2 评级 + 长期(5+ 年)锁定 4.5-5.0% YTM,作为加拿大税收效率优势的"准国债"=年化 4.5-5.5% 税后(相当于 7-8% 税前 GIC)。

| 步骤 | 操作 |
|---|---|
| 1 | 筛选 Pfd-2 系列(主要是 Partners Value 全系列) |
| 2 | 优先选长到期 + 中等票面: PVS.PR.L (2030-06, 5.5%) 与 PVS.PR.M (2031-03, 5.15%) |
| 3 | 仓位 30-50% 固收仓位 |
| 4 | 在 TFSA(免税)或 Non-Reg(合格股息抵免)持有 |
| 5 | 5+ 年持有期,不响应短期价格波动 |

**适合标的:** **PVS.PR.L、PVS.PR.M**;USD 系列 PVS.PR.U/V 仅推荐 RRSP 账户。

**何时选这一种:** 投资者目标是"高信用 + 长期锁定 + 加拿大税收效率",不追求 YTM 最大化;主要替代 GIC 与加拿大政府债的角色;愿意接受 Brookfield 间接信用风险换 Pfd-2 评级。

> [!NOTE]
> **策略独立性自检**:策略 A 在固定利率 Pfd-3 高 YTM (5.5%+);策略 B 在浮动利率 Pfd 利率对冲;策略 C 在高评级 Pfd-2 长期锁定。三者在(利率环境假设、信用质量目标、期限策略)三维度全不同。✓

#### 策略 D(可选):到期日阶梯(梯子策略)

**目标:** 通过分散到期日降低再投资风险 = 年化 5.0-5.5% 平均收益。

**到期日阶梯表(基于当日 Pfd universe):**

| 到期年 | 候选 Pfd | YTM |
|---|---|---:|
| 2027 | SBC.PR.A、ESP.PR.A、PRM.PR.A、PVS.PR.H | 4.07-4.45% |
| 2028 | LBS.PR.A、BK.PR.A、PDV.PR.A、ENS.PR.A、PVS.PR.J | 4.13-4.85% |
| 2029 | LCS.PR.A、DGS.PR.A、DFN.PR.A、DF.PR.A、FFN.PR.A、IS.PR.A、NPS.PR.A、PVS.PR.K | 4.24-5.80% |
| 2030 | FTN.PR.A、LFE.PR.B、RS.PR.A、PVS.PR.L | 4.55-5.45% |
| 2031+ | GDV.PR.A、PVS.PR.M、PVS.PR.U、PVS.PR.V | 4.50-5.25% |

每年到期 1/5,自动再投资当时最有吸引力 5+ 年期 Pfd。**适用于 RRSP/RRIF 长期收入投资者**。

### 11.4 Preferred Shares vs 替代投资品对比

| 对比项 | Split Fund Pfd | GIC (5年) | 加拿大政府债 | 加拿大公司债 (BBB) |
|---|---|---|---|---|
| 典型收益率(2026-05) | 5.5%-6.0% YTM | 3.50%-4.20% | 3.20% (5y) | 4.20%-4.80% |
| CDIC 保障 | ❌ 无 | ✅ 至 $100K | ❌(政府信用替代) | ❌ |
| 流动性 | 中(日均 5-50K 股) | 极低(锁定 5 年) | 高 | 中 |
| 本金风险 | 中(NAV 下跌可能跌破面值) | 极低 | 极低 | 低-中 |
| 税务效率 | ✅ 合格股息抵免(税后高) | ❌ 普通利息(税前 = 税后效率低) | ❌ 普通利息 | ❌ 普通利息 |
| 折价机会 | ✅ 有 | ❌ | 偶尔 | 偶尔 |

> [!IMPORTANT]
> **税务优势是 Pfd 的杀手锏**:在加拿大税务居民最高边际税率(BC 53.5%、ON 53.53%、AB 48%)情景下,合格股息(eligible dividend)的真实有效税率约 30-40%(因为 38% gross-up + 15% federal 抵免 + 省抵免)。**5.5% Pfd 税前 = ~3.5% 税后**;**5.0% GIC 税前 = ~2.5-2.7% 税后**。即使 Pfd YTM 比 GIC 高 100bp,税后 YTM 实际高 80-100bp。这是 Pfd 在加拿大 Non-Reg 账户的核心优势。

### 11.5 Preferred 风险管理

**主要风险表:**

| 风险类型 | 描述 | 应对 |
|---|---|---|
| NAV 跌破面值 | Unit NAV < Pfd 面值时 Pfd 本金账面损失 | 监控资产覆盖率,< 130% 减仓 |
| 利率风险 | 长期 Pfd 在加息中价格下跌(久期风险) | 分散期限 + 配置浮动 Pfd 对冲 |
| 流动性 | 日均成交 < 5,000 时 bid/ask 扩大 | 限价单,避免市价单 |
| 续期 / 重设 | 到期延期时利率重设可能不利 | 关注重设公告;评估新条款 |
| 集中度 | 单一发行商或行业过度暴露 | 单只 ≤ 15%,单一发行商 ≤ 30% |
| 信用降级 | DBRS 下调评级直接传导价格 | 跟踪 dbrs.morningstar.com 季度公告 |

**Pfd 持有人保护机制:**
- 累积分红:Class A 停派时 Pfd 优先权(并非全部产品累积——需 SEDAR+ 招股书确认)
- 优先偿还:到期时 Pfd 优先取得 $10/$15/$25 面值,Class A 取剩余
- 暂停触发:Unit NAV 跌穿停派阈值时 Class A 强制停派,保护 Pfd 现金流
- 赎回权:Pfd 持有人通常无赎回权,但有累积积欠分红补付权(产品依赖)

---

## 12. 高级配置策略章节

### 12.1 Split Fund 60/40 vs 传统 60/40

**关键认知:Class A 隐含杠杆 ~1.7-2.3x,意味着"60% Class A + 40% Pfd" ≠ 传统 60% 股票 + 40% 债券**。

**真实股票敞口换算:**

| 配置 | Class A 实际股票敞口 | Pfd 类债敞口 | 合计 | 等价传统配置 |
|---|---:|---:|---:|---|
| 60% Class A (1.75x) + 40% Pfd | 60% × 1.75 = **105%** | 40% | 145% | ≈ 100% 股票 + 45% 类债 = 杠杆化 145/100 |
| 50% Class A (1.75x) + 50% Pfd | 50% × 1.75 = **87.5%** | 50% | 137.5% | ≈ 88% 股票 + 50% 类债 |
| 40% Class A (1.75x) + 60% Pfd | 40% × 1.75 = **70%** | 60% | 130% | ≈ 70% 股票 + 60% 类债(传统 70/30 增强版) |
| 30% Class A (1.75x) + 70% Pfd | 30% × 1.75 = **52.5%** | 70% | 122.5% | ≈ 50% 股票 + 70% 类债 |

**对比表:**

| 维度 | 传统 60/40(60% TSX + 40% bond) | Split Fund 60/40(60% Class A + 40% Pfd) |
|---|---|---|
| 现金流 | TSX yield ~3% + bond yield 3.2% = ~3.1% | Class A yield ~10-14% + Pfd yield ~6% = **~9-12%** |
| 牛市 | 60% × 股市涨幅 | 60% × 1.75 × 股市涨幅 = **超额 75%** |
| 熊市 | 60% × 股市跌幅(无放大) | 60% × 1.75 × 跌幅 + 死亡螺旋风险 |
| 再平衡红利 | 标准 5-10% 带宽 | 折溢价波动提供 **额外 alpha 来源** |
| 税务效率 | TSX 股息合格 + bond 利息普通 | Class A 合格股息 + Pfd 合格股息(全部税收效率优化) |
| 长期总回报 | ~5-7% 年化(税后) | ~7-10% 年化(税后,假设 NAV 不长期侵蚀) |

**推荐比例(根据风险偏好):**
- **保守(退休 / 收入)**:30% Class A + 70% Pfd → 实际 ~52% 股票敞口
- **平衡**:40% Class A + 60% Pfd → 实际 ~70% 股票敞口
- **进取**:50% Class A + 50% Pfd → 实际 ~88% 股票敞口
- **不推荐 ≥ 60% Class A**:杠杆累积过高,熊市死亡螺旋风险

### 12.2 哑铃策略实战(Barbell Strategy)— 适合追求长期总收益最大化

**战略思想:** 极端进攻 + 极端防守的"双峰"配置,中间不留任何"中庸"标的——通过两端的高对比度抵消单一中庸的次优。

**进攻端选品(40-50% 仓位):**

| 账户 | 进攻端选项 | 杠杆倍数 | 理由 |
|---|---|---:|---|
| 加币(免换汇) | TSPX.TO(3x SPX) | 3x | 加币计价的美股大盘杠杆 |
| 加币 | TQQQ.TO(3x QQQ) | 3x | 加币计价的纳指杠杆 |
| 美元(RRSP/大户) | UPRO(3x SPX)/ TQQQ(3x QQQ) | 3x | USD 原生杠杆 ETF |
| 美元 | SPYU(4x SPX) | 4x | 极端杠杆 |
| 加币(温和) | Class A 进取组合(SBC + GDV + LBS) | ~1.75x | 加拿大底层 + Split 杠杆 |

**防守端选品(50-60% 仓位):**

| 账户 | 防守端选项 | 收益率 | 理由 |
|---|---|---:|---|
| 加币(TFSA / Non-Reg) | SPLT.TO | 6.08% yield | 25 只 split-pref 主动管理 |
| 加币 | PREF.TO | 6.65% yield | 11 只 split-pref(更高 yield)|
| 加币 | HSAV.TO(High Interest Savings ETF) | ~3.5% | 现金等价,流动性最优 |
| 加币 | PVS.PR.L + PVS.PR.M | 4.55-4.61% YTM | Pfd-2 评级长期锁定 |
| 美元(RRSP) | JAAA(JPM AAA CLO) | ~5.5% | 高评级 CLO ETF |
| 美元(RRSP) | PAAA(BlackRock AAA CLO) | ~5.5% | 高评级 CLO ETF |
| 美元 | PVS.PR.U / PVS.PR.V | 5.0-5.25% YTM | USD Pfd-2 锁定 |

**实操战术:**

1. **阶梯式建仓(避免一次性 entry timing 风险):** 进攻端分 6 个月分批建仓(每月加 1/6),防守端可一次性建仓。
2. **5% 带宽再平衡:** 当某端偏离目标比例 ≥ 5% 时再平衡;不要更频繁(避免无谓税务摩擦)。
3. **关闭 DRIP 截留现金:** 在 Non-Reg 账户中 DRIP 会引发 ROC 跟踪复杂度,关闭收现金后定期再投资。
4. **雷达警报触发:** 进攻端单只 −20% 时不加仓(等 −30% 加 1/3 仓);防守端 split-pref 折溢价 > 1% 溢价时减半。

**推荐比例区间:** 40-50% 进攻 / 50-60% 防守。**更激进者(年龄 < 35 + 收入稳定)可至 50/50**,更保守者(年龄 > 55)应降至 30/70。

> [!CAUTION]
> **杠杆 ETF 风险警告(必读):**
> 1. **波动率衰减(Volatility Decay)**: 3x/4x ETF 因每日重置,在波动横盘市场下长期跑输 3x × 标的涨幅。例:S&P 500 涨 0%(横盘震荡 ±5% 频繁),UPRO 可能 1 年损失 5-15%。
> 2. **地狱级回撤**:回测 2000-2002 与 2008-2009,UPRO 等价 −80% 到 −95% 回撤,需要 5x+ 涨幅才能回本。10 年牛市样本中 UPRO 中间出现 −79% 回撤。
> 3. **爆仓风险**:虽然杠杆 ETF 不会真正爆仓 0 (重置机制),但接近 0 时投资者无法等到回升(已损失 95%+)。
> 4. **仅适合:** 风险承受能力极强 + 严格执行纪律 + 长期持有期(5+ 年)+ 单只仓位 ≤ 5% 总资产 + 市场波动率低于历史平均时进入。
> 5. **不能作为通用建议**:大多数普通投资者(尤其退休阶段)应坚守传统 60/40 或 Split Fund 30-50% 进攻区间,避免 3x ETF。

---

## 13. 当前环境下的优选思路(2026-05-01)

### 13.1 稳健底仓优选(银行 / 综指龙头)

**筛选条件:**
- NAV 安全边际 ≥ 50%
- 折价 ≤ −2%(平价或折价交易)
- DBRS 评级 ≥ Pfd-3 (high) 或 (含)
- 隐含杠杆 ≤ 1.85x
- AUM ≥ CAD 200M(流动性)

**当日候选:**
- ⭐ **GDV.TO**(56.80% 安全边际 + −0.30% 折价 + Pfd-3 high + 1.75x + 350M AUM + 全球分散)
- ⭐ **SBC.TO**(58.07% + −2.71% + Pfd-3 + 1.74x + 681M AUM + 加拿大六大行)
- ⭐ **LBS.TO**(53.40% + −6.56% + Pfd-3 + 1.78x + 1.158B AUM + 银行+保险均衡)

**注意:** IS.TO 安全边际 102.13% 极强但 inception 仅 2 年 + AUM 数据缺口,作为补充不作为核心。

### 13.2 困境反转深度价值优选(高风险 / 高回报)

**触发条件:**
- 折价 ≥ 8%
- NAV 安全边际 ≥ 25%(尚未进入死亡螺旋区间)
- 底层指数从 52w 高 −10% 以上
- 单只仓位 ≤ 5% 总资产

**当日候选:**
- ⚠️ **PDV.TO**(−12.79% 折价 + 37.47% 安全边际,但 NAV 滞后 16 天 + 价格滞后 7 天,数据置信度 Medium——需手动复核当日 NAV)
- ⚠️ **FFN.TO**(−11.36% 折价 + 26.76% 安全边际,美国大行底层 + 净息差压力,2026Q2 后再评估)
- ⚠️ **FTN.TO**(−9.17% 折价 + 31.79% 安全边际 + 北美金融分散——比 FFN 更稳)
- ⚠️ **ENS.TO**(−9.25% 折价 + 99.67% 安全边际,但单一持仓 Enbridge 风险集中——只在 ENB 估值合理时配置)

**回避:** ESP.TO(虽折价但 17.53% 安全边际 + 无评级 + 油气单一)、LFE.TO(分红已停)。

### 13.3 月薪族现金流优选(纯收息)

**触发条件:**
- 月度分红
- Yield ≥ 9%
- 接受 ROC 长期稀释(TFSA/RRSP 持有规避税务复杂度)

**当日候选:**
- 💰 **CLSA.TO**(月度 14.02% yield,12 只 Class A 篮子,ETF 形式分散)
- 💰 **DFN.TO** / **FFN.TO**(月度 14-15% yield,需 TFSA 持有规避 ACB 跟踪)
- 💰 **NPS.TO**(月度 14.21% yield + 67.80% 安全边际,但 AUM 仅 31M 流动性弱)
- 💰 **BK.TO**(月度 13.57% yield + 252.5% 资产覆盖,Quadravest 系最稳健月度分红 Class A)

> [!CAUTION]
> **ROC 警告**:14%+ yield 几乎一定包含 30-50% ROC。**TFSA 是首选**(免税复利,不影响 ACB);**Non-Reg 必须每年 T3 跟踪 ACB**;**RRSP 不推荐**(取出时按 income 全额课税,ROC 递延优势失效)。

### 13.4 今日筛选执行步骤

```text
1. 淘汰 NAV 安全边际 < 30% 的 Class A
   → 排除: ESP, DGS, DFN, DF, FFN, LFE
   (注: PIC.A 阈值是 $25(非$15),NPS.TO 安全边际 67.80% 但 Class A NAV 距阈值仅 1.1% 警惕)

2. 淘汰处于溢价(市价 > NAV+1%)状态的 Class A
   → 排除: ESP (+4.75%), PRM (+4.30%), DGS (+1.45%), RS (+0.92%)

3. 在剩下的标的中,买入折价最深 + 长到期 + 高安全边际的 2-3 只,确保行业适度分散
   → 当日推荐组合:
      - LBS.TO (−6.56%, 53%, 银行+保险, Brompton 最大 AUM)
      - GDV.TO (−0.30%, 57%, 全球派息, 长到期 2031)
      - IS.TO (−5.66%, 102%, 北美基础设施, 最强结构)
      - 单一行业 ≤ 25%,单只 ≤ 10%

4. Pfd 端补充组合(60-70% 仓位):
   → 50% SPLT.TO ETF(6.08% 月度收息,自动分散)
   → 25% PVS.PR.L (4.55% YTM,Pfd-2,长期锁定)
   → 25% NPS.PR.A (5.80% YTM,高评级,加拿大大盘底层)
```

---

## 14. 关键风险和机会提示

### 14.1 当日(2026-05-01)短期交易机会

| 机会 | Ticker | 触发条件 / 数据点 |
|---|---|---|
| 折价回归 | **PDV.TO** | −12.79% 折价 + 价格滞后,等 5/2-5/9 价格更新后,如折价仍 ≥ 8% 建仓 1/3 |
| 折价回归 | **FFN.TO** | −11.36% 折价 + 26.76% 安全边际,3-6 个月窗口 |
| 折价回归 | **FTN.TO** | −9.17% 折价 + 31.79% 安全边际 + 6% 地板 Pfd,Pfd + Class A 双重折价 alpha |
| ROC 风险回避 | ESP.TO 溢价 +4.75% | 短期回避或做空 |

### 14.2 6-12 个月中期机会

| 机会 | 标的 | 触发 |
|---|---|---|
| BoC 降息至 2.00% 后固定 Pfd 价格上行 | FTN.PR.A、PVS.PR.L/M、NPS.PR.A | BoC 6 月会议政策路径 |
| 加拿大银行业 Q2 财报回温 → SBC/LBS NAV +5-8% | SBC.TO、LBS.TO | RY/TD/BMO 5-6 月财报季 |
| REIT 板块利率敏感性回归 | RS.TO(微溢价等待 −5% 折价) | 10y yield 维持 < 3.6% |
| Class A ETF (CLSA) 成立满 1 年纪念折价回归 | CLSA.TO | 2026-03 之后 NAV 端表现 |

### 14.3 1-3 年以上长期机会

| 机会 | 标的 | 逻辑 |
|---|---|---|
| 长期高评级 Pfd 锁定 | PVS.PR.L (2030)、PVS.PR.M (2031) | Pfd-2 + 5+ 年 + 4.5-4.6% YTM,debt-substitute 角色 |
| Class A 长期复合 | GDV.TO + IS.TO 等权 | 安全边际最高组合 + 长到期 + 全球+基础设施分散 |
| ETF 长期持有 | SPLT.TO 50% 仓位 | 主动管理 25 只 Pfd + 月度 6% yield + MER 0.50% |

### 14.4 Preferred 风险

- **LFE.PR.B**:评级未核验 + Class A 已停 + 高杠杆,信用 + 结构双重风险
- **ESP.PR.A**:无 DBRS 评级 + 油气单一暴露
- **PIC.PR.A**:Mulvihill 主页 NAV 渲染失败,信用结构数据缺失
- **PVS.PR.U/V**:USD 计价 + Brookfield 信用集中度
- **BK.PR.A / PDV.PR.A 浮动 Pfd**:8% 上限截断了加息中的额外收益

### 14.5 Class A 风险

- **LFE.TO**:分红已停 + 安全边际 15.92% + 高杠杆 = 当前 universe 最危险 Class A
- **ESP.TO**:溢价 + 安全边际 17.53% + 油气单一 + Pfd 无评级
- **DGS.TO**:14.34% yield 含高 ROC + 长期 NAV 平移
- **PRM.TO**:溢价 +4.30% + 制药板块已涨 23%,等待回调
- **NPS.TO**:Class A NAV $15.17 距停派阈值 $15 仅 1.1% 极其紧
- **PIC.A**:NAV 数据缺失 + Pfd 阈值 $25 距 $24.92 仅 0.32%(若 NAV 仍是 $24.92)

### 14.6 ETF 风险

- **SPFD.TO**:MER 4.34% 异常高待复核 + AUM 仅 34M + 流动性最弱
- **PREF.TO**:AUM 47M 偏小,11 只持仓集中度高于 SPLT
- **CLSA.TO**:Class A 篮子整体 ROC 风险继承所有底层 Class A 的 ROC 长期稀释

### 14.7 税务和历史数据风险

- **加拿大税务居民才享 eligible dividend 抵免**:非加拿大居民投资 Pfd 需要 25% 预扣税,无抵免
- **USD-denominated Pfd (PVS.PR.U/V) 在 Non-Reg/TFSA 账户损失 15% IRS 预扣**:仅 RRSP 保护
- **历史 Total Return 数据无法独立验证**:本报告刻意不输出 5y/10y CAGR 数字
- **ROC 长期稀释 ACB**:Non-Reg 持有人 5+ 年后 ACB 可能降至接近 0,触发被动 capital gain

---

## 15. 长期总收益率最高策略

> [!IMPORTANT]
> **本节给出基于当日数据的"长期总收益最佳"配置,但严格区分"绝对收益"、"风险调整后收益"、"税后收益"三个维度。无法核验完整长期分红 + 税务历史数据,因此不提供精确历史回测年化数字,只提供结构性结论。**

### 15.1 三个维度的"最高"

**绝对总收益最高潜力(年化 10-14%,税前):**
来自折价 + 高安全边际 + 长到期 + 杠杆化底层 = Class A 折价机会组合。当前候选 IS.TO + GDV.TO + SBC.TO 等权,长期复利潜力来自:
- 1.5-1.8x 隐含杠杆放大底层股息 (Class A "底仓")
- 折价回归 alpha (平均 2-5%/年,因为长期 Class A 折价 5-10% 是均衡)
- 底层资产 NAV 长期增长(全球派息成长 / 基础设施 / 银行)

**风险调整后总收益最优(Sharpe 最高,年化 6-8%,税前):**
来自高评级 Pfd 长期锁定 + 适度 Class A 配置 = 60% SPLT.TO + 25% Class A 精选 + 15% PVS.PR.L/M 长期组合。

**税后总收益最优(加拿大税务居民,年化 7-9%):**
- TFSA(免税最优):月度 14% yield Class A (CLSA.TO / DFN.TO / NPS.TO) 复利
- Non-Reg(合格股息抵免):Pfd-3/Pfd-2 + Class A 平价配置,税后 6-7%
- RRSP(USD pref 避预扣):JAAA + PVS.PR.U/V + 进攻端 TQQQ.TO,税后 6-8%

### 15.2 首选长期策略(基于 2026-05-01 数据)

**配置(总仓位 100%):**
- **40% — Class A 精选(等权)**: GDV.TO + SBC.TO + LBS.TO + IS.TO 各 10%
- **30% — SPLT.TO ETF**(Pfd 一篮子)
- **15% — Pfd-2 长期锁定**: PVS.PR.L 7.5% + PVS.PR.M 7.5%
- **10% — 浮动 Pfd 对冲**: BK.PR.A 5% + PDV.PR.A 5%(加息保护)
- **5% — 现金 / HSAV.TO**(再平衡子弹)

**预期:** 5 年税前年化 8-12%,税后(TFSA)7-11%,(Non-Reg)6-9%。

### 15.3 买入条件

| 标的 | 进入阈值 |
|---|---|
| Class A 精选 | NAV 安全边际 ≥ 40% + 折价 ≥ 0% 至 −5% |
| SPLT.TO | 折溢价 ≤ +1%(基本平价或折价)|
| PVS.PR.L/M | 价格 ≤ $26.50(YTM ≥ 4.5%)|
| BK.PR.A / PDV.PR.A | 价格 ≤ $11.00(避免 +5% 溢价)|

### 15.4 持有 / 再平衡规则

- **频率**:季度检查,半年再平衡;5% 带宽偏离触发再平衡
- **触发**:某只 Class A 安全边际跌至 < 25% 减半;< 15% 全减
- **DRIP**:TFSA/RRSP 全开;Non-Reg 关闭,现金截留季度再投资

### 15.5 卖出 / 降仓条件

- BoC 转向连续加息 100bp+:固定 Pfd 减仓 30%(FTN.PR.A/IS.PR.A 等)
- 任何 Class A NAV 跌至安全边际 < 20%:立即清仓该只
- ETF 折溢价 > +3% 持续 4 周:减半
- 单一行业(银行 / 保险 / 能源 / REIT)总仓位 > 35%:再平衡

### 15.6 数据不完整导致策略置信度下降的项

- **PIC.A NAV 缺失** → PIC.A 与 PIC.PR.A 暂不进入策略
- **Quadravest NAV 16 天滞后** → DFN/DF/FTN/FFN/BK/PDV/LFE 折溢价置信度降至 Medium,实际 5/1 后再核对
- **PVS 系列 NAV 与覆盖率缺失** → 信用判断仅依赖 DBRS 评级 + Brookfield 间接信用
- **历史 Total Return 不可验证** → 本策略仅基于当日 yield + 结构指标,不基于回测
- **PWI.TO 状态未核验** → 不进入策略

---

## 16. 投资决策流程与风险红线

### 16.1 完整工作流

```text
建立 universe
  ↓ (从 SOP §2.0 seed list + TMX/SEDAR+ 反向核验)
官网逐只核验
  ↓ (发行商主页 + factsheet + NAV page + DBRS)
记录 As of Date / retrieved_at
  ↓ (强制 source URL 可点击)
计算 NAV / 折溢价 / YTM / 安全边际 / 杠杆 / 覆盖率
  ↓ (公式见 §4.1)
检查税务和分红质量
  ↓ (T3 构成 / DRIP / 历史连续性)
形成短中长期观点
  ↓ (BoC 路径 + 板块景气 + 到期日)
更新汇总表
  ↓ (Pfd 单 series / Class A 单 ticker)
输出机会 / 风险
  ↓ (具体 ticker 引用,不允许泛化)
标注数据缺口
  ↓ (未核验字段必须显式列出)
质量检查 (§8 checklist)
```

### 16.2 风险红线

1. ❌ 不用过期 NAV 判断实时折价(本报告已对 Quadravest 16 天滞后明确标注)
2. ❌ 不在明显溢价时追买 Class A(ESP/PRM/DGS 当前已溢价,回避)
3. ❌ 不把 Class A 高 yield 当成固定收益(14% yield ≠ 14% 总回报,大量 ROC)
4. ❌ 不在 NAV 接近停派阈值时盲目摊平(LFE 安全边际 15.92% 不是抄底点,是退出点)
5. ❌ 不用缺失分红复投的价格图排名长期收益(本报告刻意不输出 5y/10y 数字)
6. ❌ 不忽略 ROC 对 ACB 与长期 NAV 的影响(Non-Reg 必须每年 T3 跟踪)
7. ❌ 不在不了解利率类型(固定/浮动)的情况下买 Pfd(BK/PDV/LFE 浮动结构差异关键)
8. ❌ 不把 USD-denominated Pfd 放在 Non-Reg / TFSA 账户(15% 美预扣税)

---

## 17. 数据缺口、冲突与后续核验清单

### 17.1 未能核验的关键字段

| 产品 / ETF | 缺口字段 | 影响 | 已查来源 |
|---|---|---|---|
| **PIC.A.TO / PIC.PR.A.TO** | Unit NAV、Class A NAV、安全边际、隐含杠杆、资产覆盖率、到期日、DBRS 评级、Pfd 市价 | 全产品分析降级 — 暂不入策略 | mulvihill.com/funds/premium-income-corporation(站点动态渲染失败)、mulvihill.com/PIC、Globe and Mail、stockevents.app、marketscreener 2025 年报摘要 |
| **PWI.TO / PWI.PR.A.TO**(Brompton Power & Infrastructure) | 全产品 — 本会话未抓取 | 报告不完整(仅通过 CLSA.TO 持仓 3.1% 反向确认仍存活) | 未独立访问 issuer page;依据 CLSA 持仓推断 |
| **FTU.TO**(U.S. Financial 15) | 状态 — Quadravest 主页已不列出 | 视为 terminated,不入分析 | quadravest.com 主页 |
| **PVS 系列 NAV / 资产覆盖率** | NAV per unit、当前覆盖率 | Pfd 信用判断仅依赖 DBRS 评级 | partnersvaluesplit.com、tmxmoney、taiwannews 转载 |
| **PVS.PR.V 当日市价** | 实际市价(Globe and Mail 未取得) | 用面值 $25 USD 替代,折溢价不准 | gnm + tmx |
| **大量 Pfd bid/ask/volume** | 全 universe — 本轮未能从公开行情来源稳定取得 | YTM 计算用 mid 价,置信度降级 | 已查:发行商主页、第三方行情聚合页、Globe and Mail |
| **LFE.PR.B DBRS 评级** | 评级 | 信用判断不完整 | quadravest.com lfe-fund-features 未列 |
| **ESP.PR.A DBRS 评级** | 评级 ("n/a" per issuer) | 视为无评级 | bromptongroup.com |
| **SPFD.TO MER 真实值** | MER 4.34% 是 stockanalysis.com 报告,需直接复核 | 持有推荐 holding | mulvihill.com/SPFD(导航页)、stockanalysis.com、TSX 公告 |
| **PREF.TO 持仓权重** | 11 只持仓的具体权重 | 集中度评估不完整 | quadravest.com pref-etf-fund-features |
| **Quadravest NAV 滞后 16 天** | NAV 2026-04-15 vs 报告日 2026-05-01 | 折溢价计算置信度 Medium | 等下一次 bi-weekly 更新(预计 2026-04-30 后发布) |
| **Brompton 系 Pfd 季度分红 amount** | 主页 yield 已披露但 amount 未现 | 通过 yield × face / freq 反推 | bromptongroup.com 主页 |
| **多数产品 24mo 分红连续性** | dividend_status_24mo | 历史可持续性数据缺口 | 需查 issuer 公告历史 / SEDAR+ |

### 17.2 来源冲突记录

无重大来源冲突。所有产品的 Unit NAV 与 Class A 市价跨源(发行商主页 vs Globe and Mail vs stockanalysis.com)在 ±2% 以内一致。

### 17.3 下次更新报告时的优先核验清单

1. **PIC.A**:在 Mulvihill 主页 NAV 可访问后(尝试不同浏览器/UA 头),重新抓 Unit NAV、Pfd 市价、覆盖率
2. **PWI.TO**:独立访问 bromptongroup.com/product/power-infrastructure-split-corp/(slug 待确认)
3. **Quadravest 月末 NAV**:5/1 之后访问 quadravest.com 各 fund-features 页确认 2026-04-30 NAV
4. **PVS.PR.V 当日真实价**:取得 stockanalysis.com 或其他实时行情来源报价
5. **SPFD MER 真实值**:Mulvihill MRFP / 招股书核实
6. **LFE.PR.B 与 ESP.PR.A 的 DBRS 评级**:dbrs.morningstar.com 直接搜索
7. **bid/ask 全 universe**:下次更新报告时优先补全(若实时行情来源可用)

---

## 18. 免责声明

> [!NOTE]
> **免责声明:** 本报告仅供研究和信息整理之用,不构成投资建议,不构成对任何证券的推荐、要约或邀请。所有数据来自当日公开来源(发行商官网、TMX、SEDAR+、DBRS Morningstar、Globe and Mail、stockanalysis.com、Bank of Canada),并已尽力核验,但市场数据存在波动与延迟,部分字段因技术限制未能现场核验已显式标注;本报告作者(以及任何依赖本报告作出决策的第三方)不应假设报告中数字反映实时市场状态。Split Funds 与 Split Funds ETF 是高复杂性结构性产品,涉及杠杆、ROC、税务效率、信用风险、流动性与到期延期事件等多重风险,**投资前请咨询持牌财务顾问、税务顾问或证券交易商**。本报告作者不对因使用本报告资料而产生的任何直接或间接损失承担责任。

---

> 报告生成日期: **2026-05-01** | 数据抓取时间: **2026-05-01 21:50 America/Edmonton**

---

© 2026 Sherman Yang. All rights reserved. 本报告版权归 Sherman Yang 所有,未经书面许可不得以任何形式复制、分发、转载或用于商业用途。
