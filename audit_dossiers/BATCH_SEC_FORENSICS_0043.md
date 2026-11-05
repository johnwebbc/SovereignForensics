# SovereignForensics // Batch SEC Audit 0043
**Model:** `muse-wonder-1.0` | **Tokens:** 1730 (Cached: 1140) in / 2406 out | **Cost:** $0.0507

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0043 (5 REAL SEC FILERS):
1. GOLD RESOURCE CORP (CIK: 0001160791, FY: 2023) | Assets: $210,098,000 | Sales: $138,724,000 | NetInc: $-6,321,000 | CFO: $14,157,000 | M-Score: 59.13 | F-Score: 0.18 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. Rio Bravo Oil, Inc. (CIK: 0001502774, FY: 2013) | Assets: $18,607,193 | Sales: $nan | NetInc: $-941 | CFO: $nan | M-Score: 59.03 | F-Score: 0.21 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. EVOKE PHARMA, INC. (CIK: 0001403708, FY: 2021) | Assets: $10,573,162 | Sales: $1,618,076 | NetInc: $-8,537,952 | CFO: $-6,630,007 | M-Score: 58.75 | F-Score: 0.32 | TariffRisk: 0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. ARS Pharmaceuticals, Inc. (CIK: 0001671858, FY: 2024) | Assets: $351,153,000 | Sales: $89,149,000 | NetInc: $7,998,000 | CFO: $13,548,000 | M-Score: 58.63 | F-Score: 0.36 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. COFFEESMITHS COLLECTIVE, INC. (CIK: 0001619055, FY: 2018) | Assets: $22,046,927 | Sales: $10,049,846 | NetInc: $-516,094 | CFO: $-6,135 | M-Score: 58.38 | F-Score: 0.37 | TariffRisk: 3.43 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0043",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "GOLD RESOURCE CORP",
      "identifier": "CIK: 0001160791, FY: 2023",
      "statutory_hook": "UCC § 2-717 and UCC § 2-305(2) tariff-surcharge deduction only if CBP Form 7501 and unrefunded surcharge invoices are verified; 19 U.S.C. § 1313 drawback requires export/destroyed merchandise proof",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 59.13 >> -1.78 threshold signals extreme Beneish inputs/data anomaly, F-Score 0.18 < 1.0 signals low Dechow misstatement risk, Sloan -0.0975 does not exceed 0.10; do not treat M-Score alone as manipulation proof",
      "estimated_claim_or_surcharge_usd": 6936200,
      "z3_smt_invariant": "SAT: NetIncome -6321000 = CFO 14157000 + Accruals -20478000; Sloan = (-6321000-14157000)/210098000 = -0.0975",
      "actionable_memo": "Hypothetical 5% midpoint surcharge on $138724000 sales = $6936200 unverified. Verify SEC 10-K source values, Beneish DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA inputs, AP vendor master, tariff invoices and any CBP refunds before any UCC § 2-717 deduction or credit-memo notice."
    },
    {
      "index": 2,
      "entity_name": "Rio Bravo Oil, Inc.",
      "identifier": "CIK: 0001502774, FY: 2013",
      "statutory_hook": "No enforceable UCC § 2-717, UCC § 2-305(2), or 19 U.S.C. § 1313 claim established on missing Sales/CFO data; verification required under MF-02 Public Record Verifiability",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / INDETERMINATE - M-Score 59.03 >> -1.78 is not reliable with NaN Sales and CFO, F-Score 0.21 < 1.0, Sloan accrual anomaly cannot be computed",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/INDETERMINATE: NetIncome -941 = CFO NaN + Accruals NaN; invariant Net Income = CFO + Accruals cannot be verified from provided data",
      "actionable_memo": "No deduction authorized. Retrieve complete FY2013 10-K/Q, balance sheet, income and cash-flow statements, recompute Beneish and Sloan from non-NaN values, and confirm AP/tariff exposure with CBP Form 7501 before estimating any claim."
    },
    {
      "index": 3,
      "entity_name": "EVOKE PHARMA, INC.",
      "identifier": "CIK: 0001403708, FY: 2021",
      "statutory_hook": "UCC § 2-717 / UCC § 2-305(2) not supported at TariffRisk 0.01 without supplier surcharge invoices and CBP refund records; 19 U.S.C. § 1313 requires qualifying export/destruction",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 58.75 >> -1.78 indicates Beneish outlier/data anomaly, F-Score 0.32 < 1.0 low Dechow risk, Sloan -0.1804 does not exceed 0.10 positive-accrual threshold",
      "estimated_claim_or_surcharge_usd": 809,
      "z3_smt_invariant": "SAT: NetIncome -8537952 = CFO -6630007 + Accruals -1907945; Sloan = (-8537952+6630007)/10573162 = -0.1804",
      "actionable_memo": "Tariff exposure de minimis: 5% x $1618076 x 0.01 = $809, below MF-05 $50000 magnitude. No credit memo. Audit Beneish input integrity and balance-sheet imbalance from primary 10-K before any forensic escalation."
    },
    {
      "index": 4,
      "entity_name": "ARS Pharmaceuticals, Inc.",
      "identifier": "CIK: 0001671858, FY: 2024",
      "statutory_hook": "UCC § 2-717 and UCC § 2-305(2) contingent on documented unilateral 3%-8% tariff surcharges and non-pass-through of CBP refunds; 19 U.S.C. § 1313 contingent on qualifying drawback merchandise",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 58.63 >> -1.78 indicates Beneish outlier/data anomaly, F-Score 0.36 < 1.0 low Dechow risk, Sloan -0.0158 does not exceed 0.10; positive NetIncome with CFO exceeding NetIncome does not show Sloan manipulation",
      "estimated_claim_or_surcharge_usd": 4457450,
      "z3_smt_invariant": "SAT: NetIncome 7998000 = CFO 13548000 + Accruals -5550000; Sloan = (7998000-13548000)/351153000 = -0.0158",
      "actionable_memo": "Hypothetical 5% midpoint surcharge on $89149000 sales = $4457450 unverified. Verify 10-K Beneish components, AP vendor records, tariff surcharge invoices, importer-of-record status and CBP refund/reliquidation records before any UCC § 2-717 withholding."
    },
    {
      "index": 5,
      "entity_name": "COFFEESMITHS COLLECTIVE, INC.",
      "identifier": "CIK: 0001619055, FY: 2018",
      "statutory_hook": "UCC § 2-717 / UCC § 2-305(2) contingent on verified supplier tariff surcharges; TariffRisk 3.43 is anomalous and cannot create a 19 U.S.C. § 1313 drawback claim without CBP Form 7501 and export/destruction proof",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 58.38 >> -1.78 indicates Beneish outlier/data anomaly, F-Score 0.37 < 1.0 low Dechow risk, Sloan -0.0231 does not exceed 0.10",
      "estimated_claim_or_surcharge_usd": 502492,
      "z3_smt_invariant": "SAT: NetIncome -516094 = CFO -6135 + Accruals -509959; Sloan = (-516094+6135)/22046927 = -0.0231",
      "actionable_memo": "Hypothetical 5% midpoint surcharge on $10049846 sales = $502492 unverified; do not scale by anomalous TariffRisk 3.43. Verify FY2018 filing completeness, balance-sheet identity, importer/AP records and any CBP refunds before credit-memo action."
    }
  ]
}
