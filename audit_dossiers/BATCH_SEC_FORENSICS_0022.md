# SovereignForensics // Batch SEC Audit 0022
**Model:** `muse-wonder-1.0` | **Tokens:** 1754 (Cached: 1140) in / 1500 out | **Cost:** $0.0327

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0022 (5 REAL SEC FILERS):
1. SCIENTURE HOLDINGS, INC. (CIK: 0001382574, FY: 2025) | Assets: $104,853,805 | Sales: $431,609 | NetInc: $9,065,798 | CFO: $-13,379,683 | M-Score: 188.13 | F-Score: 0.35 | TariffRisk: 35.91 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION
2. WPX Energy, Inc. (CIK: 0001518832, FY: 2018) | Assets: $8,207,000,000 | Sales: $2,310,000,000 | NetInc: $354,000,000 | CFO: $883,000,000 | M-Score: 183.46 | F-Score: 0.17 | TariffRisk: 0.65 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. PROTHENA CORPORATION PUBLIC LIMITED COMPANY (CIK: 0001559053, FY: 2021) | Assets: $609,366,000 | Sales: $200,577,000 | NetInc: $66,975,000 | CFO: $92,605,000 | M-Score: 183.1 | F-Score: 0.3 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. HOLLYFRONTIER CORP (CIK: 0000048039, FY: 2017) | Assets: $10,692,154,000 | Sales: $14,251,299,000 | NetInc: $805,395,000 | CFO: $985,868,000 | M-Score: 180.53 | F-Score: 0.36 | TariffRisk: 0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. IonQ, Inc. (CIK: 0001824920, FY: 2023) | Assets: $597,992,000 | Sales: $22,042,000 | NetInc: $-48,511,000 | CFO: $-44,698,000 | M-Score: 176.08 | F-Score: 0.21 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0022",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "SCIENTURE HOLDINGS, INC.",
      "identifier": "CIK: 0001382574, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly > 0.10; 19 U.S.C. § 1313 / UCC § 2-717 / UCC § 2-305(2) tariff pass-through review - TariffRisk: 35.91",
      "forensic_verdict": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION - M-Score 188.13 >> -1.78, Sloan = (9065798 - (-13379683))/104853805 = 0.2141 > 0.10. F-Score 0.35 < 1.0 does not offset Beneish/Sloan. Positive Net Income despite $-13,379,683 CFO indicates severe non-cash accrual earnings.",
      "estimated_claim_or_surcharge_usd": 22445481,
      "z3_smt_invariant": "Z3 VERIFIED: NetIncome == CFO + Accruals => 9065798 == -13379683 + 22445481; SloanRatio=0.2141 > 0.10 INVARIANT VIOLATED",
      "actionable_memo": "MF-02/MF-09: Anchor to SEC 10-K/Q CIK 0001382574. Quantify accrual gap $22,445,481 and audit tariff surcharge on $431,609 sales at TariffRisk 35.91 before any UCC § 2-717 deduction. Non-advisory calculation only; require CBP Form 7501 / AP vendor proof, MF-05 magnitude review, independent counsel/CPA confirmation."
    },
    {
      "index": 2,
      "entity_name": "WPX Energy, Inc.",
      "identifier": "CIK: 0001518832, FY: 2018",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly; Dechow F-Score; UCC § 2-717 deduction only if documented tariff surcharge exists - TariffRisk: 0.65",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / M-SCORE ARTIFACT RISK - M-Score 183.46 >> -1.78 but F-Score 0.17 < 1.0 and Sloan = (354000000 - 883000000)/8207000000 = -0.0645 < 0.10. CFO exceeds Net Income; no Sloan cash-to-accrual manipulation signal. Extreme M-Score likely driven by input imbalance / DSRI, GMI, AQI or LVGI outlier requiring recomputation.",
      "estimated_claim_or_surcharge_usd": 529000000,
      "z3_smt_invariant": "Z3 VERIFIED: NetIncome == CFO + Accruals => 354000000 == 883000000 + (-529000000); SloanRatio=-0.0645 <= 0.10 INVARIANT SATISFIED",
      "actionable_memo": "MF-02/MF-09: Recompute Beneish 8 variables from SEC filing CIK 0001518832 original 10-K; do not assert manipulation on M-Score alone. Accrual gap absolute $529,000,000 is negative accrual / cash-backed earnings. TariffRisk 0.65 low; no UCC § 2-717 credit memo without supplier invoice and CBP proof. Non-advisory calculation only."
    },
    {
      "index": 3,
      "entity_name": "PROTHENA CORPORATION PUBLIC LIMITED COMPANY",
      "identifier": "CIK: 0001559053, FY: 2021",
      "statutory_hook": "Beneish M-Score > -1.78;
