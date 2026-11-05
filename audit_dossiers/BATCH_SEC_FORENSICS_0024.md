# SovereignForensics // Batch SEC Audit 0024
**Model:** `muse-wonder-1.0` | **Tokens:** 1737 (Cached: 1140) in / 2839 out | **Cost:** $0.0594

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0024 (5 REAL SEC FILERS):
1. INTERNATIONAL BALER CORPORATION (CIK: 0000781902, FY: 2015) | Assets: $12,855,286 | Sales: $19,785,503 | NetInc: $812,368 | CFO: $2,686,872 | M-Score: 167.09 | F-Score: 0.18 | TariffRisk: 0.8 | Flag: ELEVATED: BENEISH OUTLIER
2. HTG Molecular Diagnostics, Inc. (CIK: 0001169987, FY: 2018) | Assets: $43,771,280 | Sales: $21,503,894 | NetInc: $-16,453,918 | CFO: $-13,173,918 | M-Score: 161.03 | F-Score: 0.33 | TariffRisk: 0.45 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. RESEARCH SOLUTIONS, INC. (CIK: 0001386301, FY: 2023) | Assets: $21,834,727 | Sales: $37,703,452 | NetInc: $571,623 | CFO: $3,383,847 | M-Score: 160.37 | F-Score: 0.35 | TariffRisk: 0.89 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. WALKER INNOVATION INC. (CIK: 0001294649, FY: 2016) | Assets: $25,588,000 | Sales: $4,278,000 | NetInc: $16,877,000 | CFO: $nan | M-Score: 159.72 | F-Score: 0.28 | TariffRisk: 0.78 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. SPENDSMART NETWORKS, INC. (CIK: 0001062273, FY: 2014) | Assets: $10,029,864 | Sales: $4,036,196 | NetInc: $-414,298 | CFO: $-6,591,020 | M-Score: 152.97 | F-Score: 0.17 | TariffRisk: 1.0 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION

## Meta Model Deliberation:
{
  "batch_id": "MICRO-BATCH LANE 1 #SEC_0024",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "INTERNATIONAL BALER CORPORATION",
      "identifier": "CIK: 0000781902, FY: 2015",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; UCC 2-717 and UCC 2-305(2) tariff surcharge deduction; 19 U.S.C. 1313 drawback",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 167.09 >> -1.78 signals extreme manipulation probability / model outlier requiring DSRI/GMI/AQI decomposition. Sloan: (812368-2686872)/12855286 = -0.1458, negative accruals, CFO exceeds NetInc, no positive Sloan flag >0.10. F-Score 0.18 <1.0 low Dechow misstatement risk. TariffRisk 0.8 high.",
      "estimated_claim_or_surcharge_usd": 791420,
      "z3_smt_invariant": "CHECK: NetInc == CFO + Accruals => 812368 == 2686872 + (-1874504) SAT; Sloan -0.1458; M-Score 167.09 violates threshold invariant M <= -1.78 UNSAT for clean filing",
      "actionable_memo": "MF-02/MF-06 anchor to SEC 10-K CIK 0000781902 FY2015. Recompute Beneish 8 variables from primary statements to isolate DSRI/GMI/AQI driver of 167.09 outlier before asserting manipulation. MF-03: quantify 3%-8% tariff surcharge on $19,785,503 sales at TariffRisk 0.8, est. $791,420 at 5%, verify via CBP Form 7501 and AP vendor master, deduct unrefunded surcharge under UCC 2-717 only with documented pass-through failure under UCC 2-305(2) and 19 U.S.C. 1313 drawback non-receipt. Non-advisory calculation only per MF-04."
    },
    {
      "index": 2,
      "entity_name": "HTG Molecular Diagnostics, Inc.",
      "identifier": "CIK: 0001169987, FY: 2018",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; Dechow F-Score; UCC 2-717 and UCC 2-305(2); 19 U.S.C. 1313 drawback",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 161.03 >> -1.78, but F-Score 0.33 <1.0. Sloan: (-16453918 - (-13173918))/43771280 = -0.0749, negative accrual drag, persistent losses NetInc $-16,453,918 on Sales $21,503,894. No Sloan >0.10 flag; imbalance flag requires liabilities/equity reconciliation, not accrual earnings inflation alone.",
      "estimated_claim_or_surcharge_usd": 483838,
      "z3_smt_invariant": "CHECK: NetInc == CFO + Accruals => -16453918 == -13173918 + (-3280000) SAT arithmetically; M-Score 161.03 <= -1.78 UNSAT; Assets invariant requires full Balance Sheet Assets == Liabilities + Equity verification from 10-K",
      "actionable_memo": "MF-02 verify CIK 0001169987 FY2018 10-K balance sheet imbalance source: soft assets, leverage LVGI, and issuance components for Dechow. MF-05/MF-01: tariff exposure limited at TariffRisk 0.45, est. $483,838 at 5% of sales, pursue only if CBP 7501 and supplier surcharge invoices document non-pass-through of refunds. Prioritize forensic restatement risk review over UCC 2-717 deduction until imbalance resolved. Non-advisory calculation only per MF-04."
    },
    {
      "index": 3,
      "entity_name": "RESEARCH SOLUTIONS, INC.",
      "identifier": "CIK: 0001386301, FY: 2023",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; UCC 2-717 and UCC 2-305(2) open price good faith; 19 U.S.C. 1313 drawback",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 160.37 >> -1.78, F-Score 0.35 <1.0 low Dechow risk. Sloan: (571623-3383847)/21834727 = -0.1288, CFO strongly exceeds NetInc, conservative negative accruals, no Sloan >0.10 flag. High TariffRisk 0.89 with Sales $37,703,452 creates primary UCC tariff-surcharge exposure despite accrual conservatism.",
      "estimated_claim_or_surcharge_usd": 1677804,
      "z3_smt_invariant": "CHECK: NetInc == CFO + Accruals => 571623 == 3383847 + (-2812224) SAT; Sloan -0.1288 <= 0.10 SAT for cash quality; M-Score 160.37 <= -1.78 UNSAT for clean filing",
      "actionable_memo": "MF-02/MF-06 anchor CIK 0001386301 FY2023. Decompose Beneish outlier and balance sheet imbalance before manipulation conclusion, as F-Score and Sloan contradict earnings inflation. MF-03/MF-05: highest tariff claim in batch, est. $1,677,804 at 5% x TariffRisk 0.89 on $37,703,452 sales; audit AP remittances, supplier 3%-8% surcharges, CBP 7501 and 19 U.S.C. 1313 refund pass-through, execute UCC 2-717 credit memo deduction only on documented unrefunded amounts. Non-advisory only per MF-04."
    },
    {
      "index": 4,
      "entity_name": "WALKER INNOVATION INC.",
      "identifier": "CIK: 0001294649, FY: 2016",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly indeterminate due to missing CFO; Z3 deterministic verification MF-09; UCC 2-717; 19 U.S.C. 1313",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / UNVERIFIABLE - M-Score 159.72 >> -1.78, F-Score 0.28 <1.0, but CFO = NaN prevents Sloan and accrual verification. NetInc $16,877,000 exceeds Sales $4,278,000 by 394%, indicating non-operating gain, discontinued operations, or filing extraction error, not sustainable operating earnings. Do not classify as proven manipulation without CFO statement.",
      "estimated_claim_or_surcharge_usd": 166842,
      "z3_smt_invariant": "UNSAT / INDETERMINATE: NetInc == CFO + Accruals => 16877000 == NaN + Accruals CANNOT SATISFY MF-09 deterministic verification; NetInc <= Sales operating invariant violated absent documented non-operating gain",
      "actionable_memo": "MF-09 FAIL: retrieve complete FY2016 10-K cash flow statement for CIK 0001294649 to replace NaN CFO, recompute Sloan, TATA, RSST accruals and reconcile $16,877,000 NetInc vs $4,278,000 sales to gain-on-sale / patent monetization disclosures. Hold Beneish conclusion in abeyance. Tariff est. $166,842 at 5% x 0.78 TariffRisk is low magnitude MF-05; pursue UCC 2-717 / 1313 claim only after verified CBP 7501 and AP surcharge proof. Non-advisory only per MF-04."
    },
    {
      "index": 5,
      "entity_name": "SPENDSMART NETWORKS, INC.",
      "identifier": "CIK: 0001062273, FY: 2014",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly > 0.10 severe; Dechow F-Score; UCC 2-717 and UCC 2-305(2); 19 U.S.C. 1313 drawback",
      "forensic_verdict": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION SIGNAL - M-Score 152.97 >> -1.78 and Sloan: (-414298 - (-6591020))/10029864 = 0.6158 >> 0.10, severe positive accruals despite net loss, CFO $-6,591,020 far below NetInc. F-Score 0.17 <1.0 contradicts Dechow, but Sloan + Beneish convergence is strongest accrual flag in batch. TariffRisk 1.0 maximum.",
      "estimated_claim_or_surcharge_usd": 201810,
      "z3_smt_invariant": "CHECK: NetInc == CFO + Accruals => -414298 == -6591020 + 6176722 SAT; Sloan 0.6158 <= 0.10 UNSAT; M-Score 152.97 <= -1.78 UNSAT for clean filing",
      "actionable_memo": "MF-01/MF-09 prioritize accrual forensic audit for CIK 0001062273 FY2014: trace $6,176,722 accrual gap to receivables DSRI, capitalized soft assets AQI, and non-cash charges; reconcile low F-Score 0.17 components. MF-02 verify in primary 10-K before external assertion. TariffRisk 1.0 but small sales base: est. $201,810 at 5% of $4,036,196 sales; verify supplier surcharges via AP master and CBP 7501, apply UCC 2-717 deduction and 19 U.S.C. 1313 drawback claim only on documented unrefunded duties. Non-advisory calculation only per MF-04."
    }
  ]
}
