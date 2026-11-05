# SovereignForensics // Batch SEC Audit 0014
**Model:** `muse-wonder-1.0` | **Tokens:** 1735 (Cached: 1140) in / 2593 out | **Cost:** $0.0545

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
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; UCC \u00a7 2-717, UCC \u00a7 2-305(2) and 19 U.S.C. \u00a7 1313 not established - no CBP Form 7501, tariff surcharge, or AP vendor record provided",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 456.1 >> -1.78 signals extreme manipulation probability or corrupted inputs, F-Score 0.42 < 1.0 does not confirm Dechow misstatement, Sloan (9422000-(-3845000))/133587000 = 0.0993 borderline < 0.10. No verifiable tariff claim.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "NetIncome = CFO + Accruals => 9422000 = -3845000 + 13267000; Accruals/Assets = 0.0993; arithmetic holds, deterministic verification FAILS on MF-09/MF-02 due to M-Score 456.1 balance-sheet imbalance flag",
      "actionable_memo": "Do not deduct under UCC 2-717. Re-pull audited 10-K for FY2018, reconcile DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA inputs causing M-Score 456.1, verify CFO and total assets, and require CBP 7501/tariff invoices before any 1313 drawback or surcharge recovery. MF-05 $50,000 minimum not met on public record provided."
    },
    {
      "index": 2,
      "entity_name": "Gaxos.ai Inc.",
      "identifier": "CIK: 0001895618, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; UCC \u00a7 2-717, UCC \u00a7 2-305(2) and 19 U.S.C. \u00a7 1313 not established - no CBP Form 7501, tariff surcharge, or AP vendor record provided",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 442.39 >> -1.78 signals extreme manipulation probability or corrupted inputs, F-Score 0.21 < 1.0 low Dechow risk, Sloan (-3418197-(-3280397))/17024536 = -0.0081 no accrual anomaly. No verifiable tariff claim despite TariffRisk 1.0.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "NetIncome = CFO + Accruals => -3418197 = -3280397 + -137800; Accruals/Assets = -0.0081; arithmetic holds, Beneish invariant fails plausibility threshold > -1.78 requiring input re-verification",
      "actionable_memo": "Do not deduct under UCC 2-717. Re-pull audited 10-K for FY2025, recompute all 8 Beneish variables from primary statements to explain M-Score 442.39, confirm receivables and asset quality, and require CBP 7501/tariff invoices before any 1313 drawback claim. MF-05 threshold not met on evidence provided."
    },
    {
      "index": 3,
      "entity_name": "Royal Energy Resources, Inc.",
      "identifier": "CIK: 0001102392, FY: 2016",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; UCC \u00a7 2-717, UCC \u00a7 2-305(2) and 19 U.S.C. \u00a7 1313 not established - no CBP Form 7501, tariff surcharge, or AP vendor record provided",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 437.94 >> -1.78, F-Score 0.41 < 1.0, Sloan (-20-6552000)/166242000 = -0.0394 no positive accrual anomaly. NetInc of -$20 against $138,569,000 sales is a probable scale/unit error invalidating forensic ratios. No verifiable tariff claim.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "NetIncome = CFO + Accruals => -20 = 6552000 + -6552020; Accruals/Assets = -0.0394; arithmetic holds only as stated, MF-09 verification FAILS on unit-scale inconsistency and M-Score 437.94 imbalance flag",
      "actionable_memo": "Do not deduct under UCC 2-717. Re-pull audited 10-K for FY2016 in original units, correct NetInc scale, recompute Beneish and Dechow inputs, reconcile CFO, and require CBP 7501/tariff invoices before any 1313 recovery. CIT Slip Op. 26-123 reliquidation not invocable without customs entry records."
    },
    {
      "index": 4,
      "entity_name": "PRECISION BIOSCIENCES INC",
      "identifier": "CIK: 0001357874, FY: 2020",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; UCC \u00a7 2-717, UCC \u00a7 2-305(2) and 19 U.S.C. \u00a7 1313 not established - no CBP Form 7501, tariff surcharge, or AP vendor record provided",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 415.79 >> -1.78, F-Score 0.19 < 1.0 low Dechow risk, Sloan (-92877000-(-71015000))/235233000 = -0.0929 negative accruals, no Sloan manipulation flag. Loss consistent with cash burn, not tariff exposure. No verifiable tariff claim.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "NetIncome = CFO + Accruals => -92877000 = -71015000 + -21862000; Accruals/Assets = -0.0929; arithmetic holds, Beneish plausibility FAILS at 415.79 >> -1.78 requiring source-statement recomputation",
      "actionable_memo": "Do not deduct under UCC 2-717. Re-pull audited 10-K for FY2020, recompute DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA, verify collaboration revenue recognition driving SGI/DSRI, and require CBP 7501/tariff invoices before any 1313 drawback claim. MF-05 threshold not met on evidence provided."
    },
    {
      "index": 5,
      "entity_name": "Alpine 4 Holdings, Inc.",
      "identifier": "CIK: 0001606698, FY: 2017",
      "statutory_hook": "Beneish M-Score > -1.78 review; Sloan and Dechow indeterminate due to missing CFO; UCC \u00a7 2-717, UCC \u00a7 2-305(2) and 19 U.S.C. \u00a7 1313 not established - TariffRisk 0.01 and no CBP Form 7501 or AP record provided",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / DATA INCOMPLETE - M-Score 409.2 >> -1.78, F-Score 0.29 < 1.0, CFO is NaN so Sloan ((NetIncome-CFO)/Assets) cannot be computed and earnings quality cannot be verified. Lowest tariff risk in batch. No verifiable tariff claim.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "NetIncome = CFO + Accruals => -2997420 = NaN + Accruals; UNSAT/INDETERMINATE under MF-09 Z3 verification due to missing CFO, invariant cannot be proven from filing data as supplied",
      "actionable_memo": "Do not deduct under UCC 2-717 and do not file 1313 claim. Obtain complete audited FY2017 cash flow statement to replace NaN CFO, recompute Sloan, Beneish and F-Score from primary statements, then re-audit. With TariffRisk 0.01 and no customs evidence, no credit-memo recovery is authorized."
    }
  ]
}
