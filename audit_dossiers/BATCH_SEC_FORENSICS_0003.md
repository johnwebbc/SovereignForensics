# SovereignForensics // Batch SEC Audit 0003
**Model:** `muse-wonder-1.0` | **Tokens:** 1742 (Cached: 1652) in / 1500 out | **Cost:** $0.0307

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0003 (5 REAL SEC FILERS):
1. VirnetX Holding Corporation (CIK: 0001082324, FY: 2023) | Assets: $152,975,000 | Sales: $48,000 | NetInc: $-27,871,000 | CFO: $-16,893,000 | M-Score: 4325.28 | F-Score: 0.32 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. First America Resources Corporation (CIK: 0001525306, FY: 2025) | Assets: $6,884,472 | Sales: $18,790,946 | NetInc: $211,112 | CFO: $458,921 | M-Score: 4270.87 | F-Score: 7.7 | TariffRisk: -4.38 | Flag: CRITICAL: CONCURRENT BENEISH + DECHOW FRAUD RISK
3. Titan Environmental Solutions Inc. (CIK: 0001514056, FY: 2023) | Assets: $22,175,474 | Sales: $7,624,584 | NetInc: $-658,663 | CFO: $-312,264 | M-Score: 4175.01 | F-Score: 270.27 | TariffRisk: -226.17 | Flag: CRITICAL: CONCURRENT BENEISH + DECHOW FRAUD RISK
4. INDEPENDENCE POWER HOLDINGS, INC. (CIK: 0002025878, FY: 2026) | Assets: $92,809,870 | Sales: $97,207,466 | NetInc: $-2,758,042 | CFO: $-337,267 | M-Score: 3842.2 | F-Score: 0.3 | TariffRisk: 1.03 | Flag: ELEVATED: BENEISH OUTLIER
5. MOON RIVER STUDIOS, INC. (CIK: 0001476278, FY: 2013) | Assets: $48,951,444 | Sales: $3,267,825 | NetInc: $-117,630 | CFO: $-2,099,533 | M-Score: 3790.14 | F-Score: 0.41 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER

## Meta Model Deliberation:
{
  "batch_id": "MICRO-BATCH LANE 1 #SEC_0003",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "VirnetX Holding Corporation",
      "identifier": "CIK: 0001082324, FY: 2023",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly audit; UCC 2-717 / 19 U.S.C. 1313 NOT established - no CBP Form 7501, importer AP, or tariff surcharge evidence in provided data",
      "forensic_verdict": "CRITICAL BALANCE SHEET IMBALANCE / BENEISH OUTLIER - REJECT M-SCORE AT FACE VALUE: M-Score 4325.28 >> -1.78, F-Score 0.32 < 1.0. Sales $48,000 vs Assets $152,975,000 makes SGI/DSRI/GMI mathematically explosive and non-deterministic. Sloan = (-27,871,000 - (-16,893,000))/152,975,000 = -0.0718, below +0.10 threshold. Net loss with negative CFO, no verifiable tariff claim.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "Z3 SAT: NetIncome == CFO + Accruals => -27871000 == -16893000 + (-10978000); Sloan=-0.0718 <= 0.10",
      "actionable_memo": "MF-02/MF-09 FAIL on tariff recovery: Do not deduct under UCC 2-717. Require full 10-K balance sheet tie-out Assets=Liabilities+Equity, prior-year Beneish inputs, and receivables/sales detail to explain 4325.28 outlier. No $50k+ MF-05 tariff claim verified; estimated claim $0 pending primary documents."
    },
    {
      "index": 2,
      "entity_name": "First America Resources Corporation",
      "identifier": "CIK: 0001525306, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78 and Dechow F-Score > 1.0 concurrent misstatement risk; UCC 2-717 / 19 U.S.C. 1313 NOT established - TariffRisk -4.38 is invalid/non-physical and no CBP/AP surcharge evidence provided",
      "forensic_verdict": "CRITICAL CONCURRENT BENEISH + DECHOW RISK: M-Score 4270.87 >> -1.78, F-Score 7.7 >> 1.0 signals high manipulation/misstatement probability per supplied models, but extreme M-Score indicates input distortion vs Sales $18,790,946 / Assets $6,884,472. Sloan = (211,112 - 458,921)/6,884,472 = -0.0360, below +0.10, CFO exceeds NetInc. Requires restatement-level review, not tariff deduction.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "Z3 SAT: NetIncome == CFO + Accruals => 211112 == 458921 + (-247809); Sloan=-0.0360 <= 0.10",
      "actionable_memo": "Halt AP deduction. Under MF-02/MF-09, demand audited 10-K prior-year comparatives for RSST, ChgRec, ChgInv, SoftAssets, issuance, and Beneish 8 variables; reconcile F-Score 7.7 drivers. Negative TariffRisk invalidates tariff model. No verified MF-05/MF-06 counterparty surcharge; claim $0."
    },
    {
      "index": 3,
      "entity_name": "Titan Environmental Solutions Inc.",
      "identifier": "CIK: 0001514056, FY: 2023",
      "statutory_hook": "Beneish M-Score > -1.78 and Dechow F-Score > 1.0 concurrent misstatement risk; UCC 2-717 / 19 U.S.C. 1313 NOT established - TariffRisk -226.17 invalid and no CBP Form 7501 or AP surcharge evidence provided",
      "forensic_verdict": "CRITICAL CONCURRENT BENEISH + DECHOW RISK - EXTREME OUTLIER: M-Score 4175.01 >> -1.78, F-Score 270.27 >> 1
