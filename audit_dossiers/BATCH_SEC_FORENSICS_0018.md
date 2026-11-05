# SovereignForensics // Batch SEC Audit 0018
**Model:** `muse-wonder-1.0` | **Tokens:** 1726 (Cached: 1140) in / 1500 out | **Cost:** $0.0326

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0018 (5 REAL SEC FILERS):
1. Athena Bitcoin Global (CIK: 0001095146, FY: 2025) | Assets: $78,033,000 | Sales: $285,391,000 | NetInc: $10,284,000 | CFO: $17,676,000 | M-Score: 269.66 | F-Score: 0.21 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. SOY ENERGY, LLC (CIK: 0001426780, FY: 2012) | Assets: $27,229,381 | Sales: $10,389,138 | NetInc: $-1,929,012 | CFO: $-718,202 | M-Score: 267.47 | F-Score: 0.17 | TariffRisk: 0.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. EBET, Inc. (CIK: 0001829966, FY: 2022) | Assets: $68,901,212 | Sales: $58,596,620 | NetInc: $-15,200,024 | CFO: $-8,308,198 | M-Score: 263.79 | F-Score: 0.41 | TariffRisk: 1.08 | Flag: ELEVATED: BENEISH OUTLIER
4. QXO, INC. (CIK: 0001236275, FY: 2025) | Assets: $15,887,300,000 | Sales: $6,842,200,000 | NetInc: $28,000,000 | CFO: $261,400,000 | M-Score: 261.82 | F-Score: 0.37 | TariffRisk: 1.75 | Flag: ELEVATED: BENEISH OUTLIER
5. vTv Therapeutics Inc. (CIK: 0001641489, FY: 2017) | Assets: $54,495,000 | Sales: $634,000 | NetInc: $-3,650,000 | CFO: $nan | M-Score: 257.5 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0018",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "Athena Bitcoin Global",
      "identifier": "CIK: 0001095146, FY: 2025",
      "statutory_hook": "No substantiated UCC § 2-717 / UCC § 2-305(2) / 19 U.S.C. § 1313 claim on provided data; Beneish M-Score and Sloan Accrual forensic review only, no CBP Form 7501, AP surcharge invoice, or drawback record supplied",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 269.66 >> -1.78 threshold signals extreme model outlier, but F-Score 0.21 (<1.0) does not corroborate Dechow misstatement risk and Sloan accrual is negative; M-Score likely distorted by extreme DSRI/GMI/SGI inputs and requires variable-level recalculation from the filed 10-K before any manipulation conclusion",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => 10284000 = 17676000 + (-7392000); Sloan = (10284000-17676000)/78033000 = -0.0947, not >0.10",
      "actionable_memo": "Non-advisory calculation only: pull FY2025 10-K and recompute all 8 Beneish variables (DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA) from primary statements; do not execute any AP deduction or credit memo absent documented tariff surcharge, CBP refund, and vendor-master evidence. TariffRisk 1.0 is not a dollar claim."
    },
    {
      "index": 2,
      "entity_name": "SOY ENERGY, LLC",
      "identifier": "CIK: 0001426780, FY: 2012",
      "statutory_hook": "No substantiated UCC § 2-717 / UCC § 2-305(2) / 19 U.S.C. § 1313 claim on provided data; TariffRisk 0.0 and no CBP Form 7501, AP surcharge invoice, or drawback record supplied",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE FLAGGED - M-Score 267.47 >> -1.78 is an extreme non-credible outlier requiring source-data verification, but F-Score 0.17 (<1.0) and negative Sloan accrual do not corroborate Dechow/Sloan manipulation; stale FY2012 data cannot support a current recovery claim",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT arithmetically: NetIncome = CFO + Accruals => -1929012 = -718202 + (-1210810); Sloan = (-1929012-(-718202))/27229381 = -0.0445, not >0.10; balance-sheet identity Assets = Liabilities + Equity not verifiable from supplied fields",
      "actionable_memo": "Non-advisory calculation only: retrieve the actual FY2012 filing, verify Assets = Liabilities + Equity and all Beneish inputs, and investigate the flagged imbalance at source. No UCC § 2-717 withholding is authorized on this record; estimated recoverable balance is $0 until primary documents are produced."
    },
    {
      "index": 3,
      "entity_name": "EBET, Inc.",
      "identifier": "CIK: 0001829966, FY: 2022",
      "statutory_hook": "No substantiated UCC § 2-717 / UCC § 2-305(2) / 19 U.S.C. § 1313 claim on provided data; no CBP Form 7501, tariff surcharge invoice,
