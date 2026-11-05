# SovereignForensics // Batch SEC Audit 0006
**Model:** `muse-wonder-1.0` | **Tokens:** 1738 (Cached: 1140) in / 1500 out | **Cost:** $0.0326

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0006 (5 REAL SEC FILERS):
1. KAANAPALI LAND, LLC (CIK: 0001230058, FY: 2013) | Assets: $132,782,000 | Sales: $8,831,000 | NetInc: $1,461,000 | CFO: $-432,000 | M-Score: 1430.87 | F-Score: 0.32 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. WASTE ENERGY CORP. (CIK: 0001515139, FY: 2021) | Assets: $5,335,874 | Sales: $472,435 | NetInc: $-4,012,599 | CFO: $-337,855 | M-Score: 1356.11 | F-Score: 0.0 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. Synergy CHC Corp. (CIK: 0001562733, FY: 2015) | Assets: $27,139,456 | Sales: $13,456,377 | NetInc: $-960,092 | CFO: $-489,175 | M-Score: 1307.5 | F-Score: 0.43 | TariffRisk: 0.02 | Flag: ELEVATED: BENEISH OUTLIER
4. EMPIRE RESORTS INC (CIK: 0000906780, FY: 2015) | Assets: $65,418,000 | Sales: $70,961,000 | NetInc: $-3,416,000 | CFO: $-4,342,000 | M-Score: 1243.13 | F-Score: 0.35 | TariffRisk: 1.05 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. TOTALIGENT, INC. (CIK: 0000846377, FY: 2013) | Assets: $41,360,924 | Sales: $6,098,374 | NetInc: $262,752 | CFO: $-2,855,751 | M-Score: 1229.59 | F-Score: 0.42 | TariffRisk: 1.0 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION

## Meta Model Deliberation:
{
  "batch_id": "SEC_0006",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "KAANAPALI LAND, LLC",
      "identifier": "CIK: 0001230058, FY: 2013",
      "statutory_hook": "UCC § 2-717 and UCC § 2-305(2); 19 U.S.C. § 1313; Beneish M-Score > -1.78",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER. M-Score 1430.87 >> -1.78 signals high manipulation probability, F-Score 0.32 < 1.0. Sloan Accrual = (1461000 - (-432000))/132782000 = 0.0143 < 0.10, no severe Sloan anomaly. Extreme M-Score likely driven by DSRI/GMI/AQI distortion and flagged imbalance; requires restatement verification before UCC deduction.",
      "estimated_claim_or_surcharge_usd": 441550,
      "z3_smt_invariant": "SAT: NetIncome(1461000) == CFO(-432000) + Accruals(1893000); Sloan=0.0143",
      "actionable_memo": "MF-02/MF-09: Anchor to SEC 10-K FY2013, re-extract balance sheet to resolve imbalance, verify receivables/asset quality inputs to Beneish. MF-05 Tariff estimate = Sales 8831000 x TariffRisk 1.0 x 5% = $441,550 contingent on CBP Form 7501 and AP surcharge proof. Do not execute § 2-717 deduction until deterministic Z3 balance-sheet identity Assets==Liabilities+Equity verifies."
    },
    {
      "index": 2,
      "entity_name": "WASTE ENERGY CORP.",
      "identifier": "CIK: 0001515139, FY: 2021",
      "statutory_hook": "UCC § 2-717 and UCC § 2-305(2); 19 U.S.C. § 1313; Beneish M-Score > -1.78; Sloan Accrual Anomaly",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER. M-Score 1356.11 >> -1.78, F-Score 0.0 < 1.0. Sloan Accrual = (-4012599 - (-337855))/5335874 = -0.6887, absolute > 0.10 flags severe cash-to-accrual divergence. Net loss vastly exceeds operating cash burn, indicating non-cash accrual/write-down distortion.",
      "estimated_claim_or_surcharge_usd": 23622,
      "z3_smt_invariant": "SAT: NetIncome(-4012599) == CFO(-337855) + Accruals(-3674744); Sloan=-0.6887",
      "actionable_memo": "MF-02/MF-09: Verify FY2021 SEC filing balance-sheet imbalance and accrual composition; obtain AP vendor master and C
