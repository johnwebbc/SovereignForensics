# SovereignForensics // Batch SEC Audit 0023
**Model:** `muse-wonder-1.0` | **Tokens:** 1737 (Cached: 1140) in / 2899 out | **Cost:** $0.0606

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0023 (5 REAL SEC FILERS):
1. 1847 HOLDINGS LLC (CIK: 0001599407, FY: 2017) | Assets: $8,084,455 | Sales: $6,410,620 | NetInc: $-269,844 | CFO: $-415 | M-Score: 175.12 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. CATALYST PHARMACEUTICALS, INC. (CIK: 0001369568, FY: 2019) | Assets: $112,376,230 | Sales: $102,306,337 | NetInc: $31,875,337 | CFO: $34,611,473 | M-Score: 173.81 | F-Score: 0.32 | TariffRisk: 0.17 | Flag: ELEVATED: BENEISH OUTLIER
3. Uni-Pixel (CIK: 0001171012, FY: 2016) | Assets: $24,847,000 | Sales: $4,100,000 | NetInc: $-5,574,000 | CFO: $-16,644,000 | M-Score: 171.16 | F-Score: 0.06 | TariffRisk: 0.61 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. TOMI ENVIRONMENTAL SOLUTIONS, INC. (CIK: 0000314227, FY: 2013) | Assets: $5,733,103 | Sales: $1,166,457 | NetInc: $-1,750,407 | CFO: $-386,195 | M-Score: 170.81 | F-Score: 0.23 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. SHARPLINK, INC. (CIK: 0001981535, FY: 2025) | Assets: $2,431,766,000 | Sales: $28,055,000 | NetInc: $10,099,000 | CFO: $-17,542,000 | M-Score: 169.95 | F-Score: 0.41 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER

## Meta Model Deliberation:
{
  "batch_id": "SEC_0023",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "1847 HOLDINGS LLC",
      "identifier": "CIK: 0001599407, FY: 2017",
      "statutory_hook": "Beneish M-Score > -1.78; 19 U.S.C. § 1313 and UCC § 2-717 / § 2-305(2) tariff-surcharge review, contingent on CBP Form 7501 verification",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 175.12 is far above -1.78 threshold and is not economically plausible as a standard Beneish value, indicating probable input, scaling, or prior-period denominator error requiring recomputation of DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI and TATA. F-Score 0.19 (<1.0) does not corroborate Dechow misstatement risk. Sloan Accrual = (-269844 - (-415)) / 8084455 = -0.0333, below 0.10 severe-accrual threshold.",
      "estimated_claim_or_surcharge_usd": 320531,
      "z3_smt_invariant": "VERIFIED_ARITHMETIC: NetIncome (-269844) = CFO (-415) + Accruals (-269429); Accruals/Assets = -0.0333; M-Score invariant flagged UNSAT for plausibility pending source-variable recomputation",
      "actionable_memo": "Do not execute UCC § 2-717 deduction on M-Score alone. Pull FY2016-FY2017 10-K, recompute all 8 Beneish variables from audited statements, and verify tariff exposure with CBP Form 7501 and AP vendor records. Estimated surcharge exposure is a screening proxy only: $6,410,620 Sales x 1.0 TariffRisk x 5% midpoint surcharge = $320,531, recoverable only if unrefunded surcharge and drawback are documented."
    },
    {
      "index": 2,
      "entity_name": "CATALYST PHARMACEUTICALS, INC.",
      "identifier": "CIK: 0001369568, FY: 2019",
      "statutory_hook": "Beneish M-Score > -1.78; UCC § 2-305(2) good-faith open-price review; 19 U.S.C. § 1313 low applicability at TariffRisk 0.17",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 173.81 >> -1.78 but extreme magnitude signals likely Beneish input/scaling error rather than proven manipulation. F-Score 0.32 (<1.0) is low. Sloan Accrual = (31875337 - 34611473) / 112376230 = -0.0243, below 0.10 threshold, with CFO exceeding Net Income, inconsistent with severe cash-to-accrual manipulation on this metric.",
      "estimated_claim_or_surcharge_usd": 869604,
      "z3_smt_invariant": "VERIFIED_ARITHMETIC: NetIncome (31875337) = CFO (34611473) + Accruals (-2736136); Accruals/Assets = -0.0243; Beneish plausibility invariant UNSAT pending DSRI/GMI/AQI recomputation",
      "actionable_memo": "Recompute Beneish from FY2018-FY2019 10-K source lines before any finding; investigate receivables, gross margin and asset-quality inputs causing outlier. Tariff claim is low-priority at TariffRisk 0.17. Screening proxy: $102,306,337 x 0.17 x 5% = $869,604, not actionable under UCC § 2-717 or § 1313 without supplier surcharge invoices, import entries, and proof of non-pass-through of refunds."
    },
    {
      "index": 3,
      "entity_name": "Uni-Pixel",
      "identifier": "CIK: 0001171012, FY: 2016",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly > 0.10; 19 U.S.C. § 1313 and UCC § 2-717 review contingent on balance-sheet reconciliation",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE AND SLOAN FLAG - M-Score 171.16 >> -1.78 and extreme, requiring recomputation. F-Score 0.06 (<1.0) is very low and conflicts with Beneish. Sloan Accrual = (-5574000 - (-16644000)) / 24847000 = 0.4456, exceeding 0.10 severe threshold because CFO loss greatly exceeds net loss, indicating large non-cash, working-capital, impairment or classification effects that must be reconciled, not automatically manipulation.",
      "estimated_claim_or_surcharge_usd": 125050,
      "z3_smt_invariant": "VERIFIED_ARITHMETIC: NetIncome (-5574000) = CFO (-16644000) + Accruals (11070000); Accruals/Assets = 0.4456 > 0.10 Sloan threshold; balance-sheet identity invariant FLAGGED UNSAT per source flag",
      "actionable_memo": "Priority forensic reconciliation: tie FY2015-FY2016 balance sheet, cash-flow statement and accrual bridge in the 10-K; isolate impairments, stock compensation, receivables/inventory changes and discontinued items driving +$11,070,000 accruals. Hold any § 2-717 deduction until imbalance is resolved. Tariff screening proxy: $4,100,000 x 0.61 x 5% = $125,050, requiring CBP Form 7501 and vendor surcharge proof."
    },
    {
      "index": 4,
      "entity_name": "TOMI ENVIRONMENTAL SOLUTIONS, INC.",
      "identifier": "CIK: 0000314227, FY: 2013",
      "statutory_hook": "Beneish M-Score > -1.78; 19 U.S.C. § 1313 and UCC § 2-717 / § 2-305(2) tariff-surcharge review, contingent on balance-sheet reconciliation",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 170.81 >> -1.78 and extreme, indicating probable Beneish denominator/scaling error for a small filer. F-Score 0.23 (<1.0) does not corroborate Dechow risk. Sloan Accrual = (-1750407 - (-386195)) / 5733103 = -0.2379, negative and not above +0.10 severe positive-accrual threshold, despite large magnitude requiring accrual-bridge review.",
      "estimated_claim_or_surcharge_usd": 58323,
      "z3_smt_invariant": "VERIFIED_ARITHMETIC: NetIncome (-1750407) = CFO (-386195) + Accruals (-1364212); Accruals/Assets = -0.2379; balance-sheet identity invariant FLAGGED UNSAT per source flag",
      "actionable_memo": "Reconcile FY2012-FY2013 audited statements, restatements and cash-flow classifications before any manipulation conclusion; recompute Beneish variables with correct prior-period denominators. Tariff screening proxy: $1,166,457 x 1.0 x 5% = $58,323, meeting magnitude screening only if documented by import entries, supplier surcharge invoices and AP records sufficient for a § 2-717 credit-memo claim."
    },
    {
      "index": 5,
      "entity_name": "SHARPLINK, INC.",
      "identifier": "CIK: 0001981535, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78; UCC § 2-305(2) and 19 U.S.C. § 1313 review at TariffRisk 1.0, contingent on separating operating sales from non-operating asset-driven income",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 169.95 >> -1.78 and extreme, not plausible without recomputation, especially given Assets $2,431,766,000 versus Sales only $28,055,000, suggesting asset structure distorts SGI, AQI, LVGI and TATA. F-Score 0.41 (<1.0) is below misstatement threshold. Sloan Accrual = (10099000 - (-17542000)) / 2431766000 = 0.0114, below 0.10 threshold.",
      "estimated_claim_or_surcharge_usd": 1402750,
      "z3_smt_invariant": "VERIFIED_ARITHMETIC: NetIncome (10099000) = CFO (-17542000) + Accruals (27641000); Accruals/Assets = 0.0114; Beneish plausibility invariant UNSAT pending variable-level recomputation and asset-composition review",
      "actionable_memo": "Pull FY2024-FY2025 10-K/Q, identify non-cash and digital-asset or investment gains bridging +$27,641,000 accruals, and recompute Beneish excluding non-comparable asset inflation. Do not base a tariff deduction on asset total. Screening proxy: $28,055,000 x 1.0 x 5% = $1,402,750, actionable only with CBP Form 7501, supplier surcharge invoices, proof of export/destruction for § 1313 drawback, and AP records for § 2-717."
    }
  ]
}
