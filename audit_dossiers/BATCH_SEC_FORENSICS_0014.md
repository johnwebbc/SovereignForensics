# SovereignForensics // Batch SEC Audit 0014
**Model:** `muse-wonder-1.0` | **Tokens:** 1735 (Cached: 1140) in / 1500 out | **Cost:** $0.0326

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0014 (5 REAL SEC FILERS):
1. GREAT ELM CAPITAL GROUP, INC. (CIK: 0001082506, FY: 2018) | Assets: $133,587,000 | Sales: $5,935,000 | NetInc: $9,422,000 | CFO: $-3,845,000 | M-Score: 456.1 | F-Score: 0.42 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. Gaxos.ai Inc. (CIK: 0001895618, FY: 2025) | Assets: $17,024,536 | Sales: $1,933,030 | NetInc: $-3,418,197 | CFO: $-3,280,397 | M-Score: 442.39 | F-Score: 0.21 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
3. Royal Energy Resources, Inc. (CIK: 0001102392, FY: 2016) | Assets: $166,242,000 | Sales: $138,569,000 | NetInc: $-20 | CFO: $6,552,000 | M-Score: 437.94 | F-Score: 0.41 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. PRECISION BIOSCIENCES INC (CIK: 0001357874, FY: 2020) | Assets: $235,233,000 | Sales: $24,285,000 | NetInc: $-92,877,000 | CFO: $-71,015,000 | M-Score: 415.79 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. Alpine 4 Holdings, Inc. (CIK: 0001606698, FY: 2017) | Assets: $15,970,950 | Sales: $10,091,491 | NetInc: $-2,997,420 | CFO: $nan | M-Score: 409.2 | F-Score: 0.29 | TariffRisk: 0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0014",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "GREAT ELM CAPITAL GROUP, INC.",
      "identifier": "CIK: 0001082506, FY: 2018",
      "statutory_hook": "No verifiable UCC § 2-717 / UCC § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim evidenced in provided data; Beneish M-Score, Dechow F-Score and Sloan Accrual analysis only",
      "forensic_verdict": "CRITICAL DATA INTEGRITY / INCONCLUSIVE MANIPULATION: M-Score 456.1 is orders of magnitude above -1.78 threshold and is not a plausible Beneish output, indicating balance-sheet imbalance or input scaling error. F-Score 0.42 < 1.0 does not signal Dechow misstatement. Sloan = (9422000 - (-3845000)) / 133587000 = 0.0993, just below 0.10 severe-accrual threshold. No tariff recovery established on this record.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT arithmetically: NetIncome 9422000 = CFO -3845000 + Accruals 13267000; Sloan 0.0993. Beneish inputs UNSAT for plausibility, requires source 10-K re-extraction.",
      "actionable_memo": "Do not deduct under UCC 2-717 without AP vendor invoices, CBP Form 7501, and surcharge pass-through proof. Re-extract audited 10-K balance sheet, recompute DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA from prior-year comparatives, and verify assets/liabilities/equity balance before any claim."
    },
    {
      "index": 2,
      "entity_name": "Gaxos.ai Inc.",
      "identifier": "CIK: 0001895618, FY: 2025",
      "statutory_hook": "No verifiable UCC § 2-717 / UCC § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim evidenced in provided data; Beneish M-Score, Dechow F-Score and Sloan Accrual analysis only",
      "forensic_verdict": "ELEVATED BENEISH OUTLIER / INCONCLUSIVE: M-Score 442.39 >> -1.78 is implausible as a standard Beneish score and indicates corrupted, scaled, or non-comparable inputs, not proof of manipulation. F-Score 0.21 < 1.0 low misstatement risk. Sloan = (-3418197 - (-3280397)) / 17024536 = -0.0081, no accrual anomaly.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT arithmetically: NetIncome -3418197 = CFO -3280397 + Accruals -137800; Sloan -0.0081. Beneish variable construction UNVERIFIED.",
      "actionable_memo": "No AP deduction authorized on this evidence. Obtain filed 10-K/Q, prior-year financials, receivables/inventory/PP&E schedules, and any supplier tariff invoices/CBP 7501s; recompute Beneish from primary statements before escalation."
    },
    {
      "index": 3,
      "entity_name": "Royal Energy Resources, Inc.",
      "identifier": "CIK: 0001102392, FY: 2016",
      "statutory_hook": "No verifiable UCC § 2-717 / UCC § 2-305(2) tariff surcharge or
