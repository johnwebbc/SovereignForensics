# SovereignForensics // Batch SEC Audit 0008
**Model:** `muse-wonder-1.0` | **Tokens:** 1745 (Cached: 1140) in / 1500 out | **Cost:** $0.0326

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0008 (5 REAL SEC FILERS):
1. American Realty Capital Global Trust II, Inc. (CIK: 0001609865, FY: 2015) | Assets: $677,120,000 | Sales: $21,648,000 | NetInc: $-20,000 | CFO: $-2,840,000 | M-Score: 962.51 | F-Score: 0.39 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. LIBERATOR MEDICAL HOLDINGS, INC. (CIK: 0000017485, FY: 2014) | Assets: $54,329,000 | Sales: $74,569,000 | NetInc: $7,802,000 | CFO: $13,633,000 | M-Score: 958.84 | F-Score: 0.49 | TariffRisk: 0.77 | Flag: ELEVATED: BENEISH OUTLIER
3. FORWARD INDUSTRIES, INC. (CIK: 0000038264, FY: 2013) | Assets: $17,111,802 | Sales: $30,910,506 | NetInc: $-206,886 | CFO: $2,250,412 | M-Score: 933.06 | F-Score: 0.17 | TariffRisk: 0.0 | Flag: ELEVATED: BENEISH OUTLIER
4. NEW CONCEPT ENERGY, INC. (CIK: 0000105744, FY: 2014) | Assets: $13,308,000 | Sales: $4,363,000 | NetInc: $426,000 | CFO: $1,602,000 | M-Score: 918.43 | F-Score: 0.37 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
5. UNIPROP MANUFACTURED HOUSING COMMUNITIES INCOME FUND II /MI/ (CIK: 0000805993, FY: 2014) | Assets: $31,407,960 | Sales: $2,163,000 | NetInc: $-107,728 | CFO: $nan | M-Score: 912.62 | F-Score: 0.18 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0008",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "American Realty Capital Global Trust II, Inc.",
      "identifier": "CIK: 0001609865, FY: 2015",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly screening; no documented UCC 2-717, UCC 2-305(2), or 19 U.S.C. 1313 tariff/drawback claim on this record",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - NOT PROVEN MANIPULATION. M-Score 962.51 is an extreme computational/data outlier requiring variable-level DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA recomputation from the 10-K. F-Score 0.39 is below 1.0. Sloan accrual = (-20000 - (-2840000))/677120000 = 0.0042, below 0.10, so cash-to-accrual manipulation is not flagged.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -20000 = -2840000 + 2820000; Accruals/Assets = 0.0042",
      "actionable_memo": "Do not deduct from AP under UCC 2-717 without invoice-level CBP Form 7501, supplier surcharge, and unrefunded refund proof. Recompute all Beneish inputs from primary SEC filing; investigate near-zero net income denominator effects causing M-Score explosion. No recoverable tariff claim quantified on supplied evidence."
    },
    {
      "index": 2,
      "entity_name": "LIBERATOR MEDICAL HOLDINGS, INC.",
      "identifier": "CIK: 0000017485, FY: 2014",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly screening; no documented UCC 2-717, UCC 2-305(2), or 19 U.S.C. 1313 tariff/drawback claim on this record",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - CASH-BACKED EARNINGS, NOT PROVEN MANIPULATION. M-Score 958.84 is an extreme outlier requiring variable-level recomputation. F-Score 0.49 is below 1.0. Sloan accrual = (7802000 - 13633000)/54329000 = -0.1073, indicating negative accruals and CFO exceeding net income, inconsistent with Sloan accrual-inflation flag despite absolute magnitude.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => 7802000 = 13633000 + (-5831000); Accruals/Assets = -0.1073",
      "actionable_memo": "Do not assert tariff recovery under UCC 2-717/2-305(2) or 19 U.S.C. 1313 without AP vendor, import, and surcharge records. Audit Beneish drivers, especially receivables, margin, and leverage inputs that may produce an artifact score. Earnings are cash-supported on supplied CFO data; no quantified claim."
    },
    {
      "index": 3,
      "entity_name": "FORWARD INDUSTRIES, INC.",
      "identifier": "CIK: 0000038264, FY: 2013",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly screening; TariffRisk 0.0, no UCC 2-717, UCC 2-305(2), or 19 U.S.C. 1313 basis shown",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - NOT PROVEN MANIPULATION. M-Score 933.06 is an extreme data/variable outlier requiring recomputation. F-Score 0.17 is well below 1.0. Sloan accrual = (-206886 - 2250412)/17111802 = -0.1436, indicating strongly negative accruals and positive CFO despite a small net loss, not accrual-inflated earnings under the >0.10 test.",
      "estimated
