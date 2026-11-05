# SovereignForensics // Batch SEC Audit 0018
**Model:** `muse-wonder-1.0` | **Tokens:** 1726 (Cached: 1140) in / 2462 out | **Cost:** $0.0518

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
      "statutory_hook": "UCC § 2-717 and UCC § 2-305(2) not established on SEC data alone; 19 U.S.C. § 1313 requires CBP Form 7501 and export/destruction proof",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 269.66 > -1.78, but extreme value indicates likely input/model distortion requiring re-computation from 10-K; F-Score 0.21 < 1.0; Sloan Accrual = (10284000-17676000)/78033000 = -0.0947, below 0.10 threshold. No verified tariff deduction claim.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: 10284000 == 17676000 + (-7392000); Sloan=-0.0947",
      "actionable_memo": "MF-02 FAIL for tariff recovery: obtain supplier invoices, AP vendor master, tariff surcharge lines, and any CBP refund records before any UCC § 2-717 deduction. Recompute Beneish DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA from audited statements; do not treat 269.66 as proof of manipulation."
    },
    {
      "index": 2,
      "entity_name": "SOY ENERGY, LLC",
      "identifier": "CIK: 0001426780, FY: 2012",
      "statutory_hook": "No statutory hook established; TariffRisk 0.0 and no CBP Form 7501, supplier surcharge, or drawback evidence under UCC § 2-717, UCC § 2-305(2), or 19 U.S.C. § 1313",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / DATA INTEGRITY RISK - M-Score 267.47 > -1.78 is not reliable without balance-sheet equality verification; F-Score 0.17 < 1.0; Sloan Accrual = (-1929012-(-718202))/27229381 = -0.0445, below 0.10 threshold.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "PARTIAL SAT: -1929012 == -718202 + (-1210810); UNSAT-PENDING: Assets == Liabilities + Equity cannot be verified from provided fields",
      "actionable_memo": "Halt automated claim generation. Reconcile FY2012 Assets, Liabilities, and Equity to the filed balance sheet and correct source extraction. No credit memo, AP deduction, or drawback claim is supportable on this record."
    },
    {
      "index": 3,
      "entity_name": "EBET, Inc.",
      "identifier": "CIK: 0001829966, FY: 2022",
      "statutory_hook": "UCC § 2-717 and UCC § 2-305(2) not established on SEC data alone; 19 U.S.C. § 1313 requires CBP Form 7501 and export/destruction proof",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 263.79 > -1.78, but extreme value requires Beneish input audit; F-Score 0.41 < 1.0; Sloan Accrual = (-15200024-(-8308198))/68901212 = -0.1000, negative and below +0.10 severe-manipulation threshold despite losses and cash burn.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: -15200024 == -8308198 + (-6891826); Sloan=-0.1000",
      "actionable_memo": "MF-02 FAIL for tariff recovery: TariffRisk 1.08 is not an invoice. Obtain AP invoices showing discrete 3%-8% surcharges, supplier CBP refund status, and contract price terms before asserting UCC § 2-305(2) bad faith or deducting under § 2-717."
    },
    {
      "index": 4,
      "entity_name": "QXO, INC.",
      "identifier": "CIK: 0001236275, FY: 2025",
      "statutory_hook": "Potential UCC § 2-717 / UCC § 2-305(2) review only if discrete supplier tariff surcharges and non-pass-through of CBP refunds are documented; potential 19 U.S.C. § 1313 review only with CBP Form 7501 and export/destruction proof",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER, UNVERIFIED - M-Score 261.82 > -1.78 is an extreme likely model/input artifact requiring recalculation, especially given scale/acquisition activity; F-Score 0.37 < 1.0; Sloan Accrual = (28000000-261400000)/15887300000 = -0.0147, below 0.10 threshold and CFO exceeds Net Income.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: 28000000 == 261400000 + (-233400000); Sloan=-0.0147",
      "actionable_memo": "Largest MF-05/MF-06 audit priority due to $6,842,200,000 sales and TariffRisk 1.75, but $0 verified claim at this stage. Sample AP vendor master and supplier invoices for tariff surcharge percentages, trace to CBP entries/refunds, and only then quantify a § 2-717 credit memo; do not estimate recovery from Sales x TariffRisk."
    },
    {
      "index": 5,
      "entity_name": "vTv Therapeutics Inc.",
      "identifier": "CIK: 0001641489, FY: 2017",
      "statutory_hook": "No statutory hook established; missing CFO prevents accrual verification and no CBP Form 7501, supplier surcharge, or drawback evidence under UCC § 2-717, UCC § 2-305(2), or 19 U.S.C. § 1313",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / UNVERIFIABLE - CFO is NaN, so Sloan Accrual and MF-09 deterministic verification cannot be performed; M-Score 257.5 > -1.78 is unreliable on incomplete inputs; F-Score 0.19 < 1.0 does not cure missing cash-flow data.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/UNVERIFIABLE: CFO=NaN; -3650000 == NaN + Accruals cannot be proven; Sloan undefined",
      "actionable_memo": "Quarantine from pipeline. Retrieve FY2017 audited cash-flow statement, populate CFO, verify Assets == Liabilities + Equity, and recompute Beneish, Dechow, and Sloan metrics. No AP deduction, credit memo, or manipulation conclusion is supportable until MF-09 passes."
    }
  ]
}
