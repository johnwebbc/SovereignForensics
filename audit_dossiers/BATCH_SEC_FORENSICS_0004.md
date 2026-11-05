# SovereignForensics // Batch SEC Audit 0004
**Model:** `muse-wonder-1.0` | **Tokens:** 1734 (Cached: 1140) in / 1500 out | **Cost:** $0.0326

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0004 (5 REAL SEC FILERS):
1. VirnetX Holding Corporation (CIK: 0001082324, FY: 2020) | Assets: $234,793,000 | Sales: $302,636,000 | NetInc: $280,429,000 | CFO: $281,389,000 | M-Score: 3171.99 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. Gyre Therapeutics, Inc. (CIK: 0001124105, FY: 2020) | Assets: $98,554,000 | Sales: $20,948,000 | NetInc: $-55,178,000 | CFO: $-43,613,000 | M-Score: 3111.41 | F-Score: 0.22 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. Datacentrex, Inc. (CIK: 0001853825, FY: 2025) | Assets: $66,841,910 | Sales: $6,963,477 | NetInc: $-8,502,885 | CFO: $-6,447,474 | M-Score: 3029.91 | F-Score: 0.27 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
4. ROKWADER, INC. (CIK: 0001322952, FY: 2016) | Assets: $16,036,382 | Sales: $5,201,542 | NetInc: $-471,406 | CFO: $527,485 | M-Score: 2001.72 | F-Score: 0.34 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
5. Swisher Hygiene Inc. (CIK: 0001504747, FY: 2015) | Assets: $113,199,000 | Sales: $0 | NetInc: $-46,808,000 | CFO: $-8,453,000 | M-Score: 1974.26 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0004",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "VirnetX Holding Corporation",
      "identifier": "CIK: 0001082324, FY: 2020",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; no documented UCC \u00a7 2-717 tariff surcharge, UCC \u00a7 2-305(2) pass-through, or 19 U.S.C. \u00a7 1313 drawback claim in provided record",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 3171.99 >> -1.78 signals extreme model outlier, but F-Score 0.19 < 1.0 and Sloan -0.0041 do not corroborate accrual manipulation; M-Score likely distorted by non-recurring licensing revenue/scale variables and requires prior-year DSRI/GMI/AQI/SGI recomputation before any finding",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome 280429000 = CFO 281389000 + Accruals -960000; Sloan=(280429000-281389000)/234793000=-0.0041 <= 0.10",
      "actionable_memo": "Do not execute UCC 2-717 AP deduction on this record: no CBP Form 7501, supplier surcharge invoice, or AP vendor balance >=$50000 is verified. Recompute Beneish 8 variables from FY2019/FY2020 10-K, isolate non-recurring patent-litigation revenue, and close unless primary filings corroborate manipulation."
    },
    {
      "index": 2,
      "entity_name": "Gyre Therapeutics, Inc.",
      "identifier": "CIK: 0001124105, FY: 2020",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; no documented UCC \u00a7 2-717 tariff surcharge, UCC \u00a7 2-305(2) pass-through, or 19 U.S.C. \u00a7 1313 drawback claim in provided record",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 3111.41 >> -1.78, but F-Score 0.22 < 1.0 and Sloan -0.1173 show negative, not income-inflating, accruals; loss-making biotech profile can distort SGI/DSRI/GMI inputs, so manipulation is unproven on supplied totals",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome -55178000 = CFO -43613000 + Accruals -11565000; Sloan=(-55178000+43613000)/98554000=-0.1173 <= 0.10",
      "actionable_memo": "Do not execute UCC 2-717 AP deduction on this record: no tariff surcharge, CBP entry, or verified AP balance is documented. Obtain FY2019/FY2020 10-K balance-sheet components, verify assets/liabilities/equity identity, and recompute DSRI, AQI, LVGI and TATA before escalating."
    },
    {
      "index": 3,
      "entity_name": "Datacentrex, Inc.",
      "identifier": "CIK: 0001853825, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; no documented UCC \u00a7 2-717 tariff surcharge, UCC \u00a7 2-305(2) pass-through, or 19 U.S.C. \u00a7 1313 drawback claim in provided record",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 
