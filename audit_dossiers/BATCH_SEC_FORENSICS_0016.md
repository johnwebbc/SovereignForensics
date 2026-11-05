# SovereignForensics // Batch SEC Audit 0016
**Model:** `muse-wonder-1.0` | **Tokens:** 1748 (Cached: 1140) in / 2736 out | **Cost:** $0.0574

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0016 (5 REAL SEC FILERS):
1. TURTLE BEACH CORPORATION (CIK: 0001493761, FY: 2014) | Assets: $246,968,000 | Sales: $207,136,000 | NetInc: $26,460,000 | CFO: $18,290,000 | M-Score: 326.45 | F-Score: 0.48 | TariffRisk: 0.26 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. Jingbo Technology, Inc. (CIK: 0001647822, FY: 2023) | Assets: $18,357,783 | Sales: $3,723,088 | NetInc: $-6,395,388 | CFO: $102,130 | M-Score: 325.48 | F-Score: 0.0 | TariffRisk: -3.07 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. CHINA TIANFEIHONG WINE INC (CIK: 0001501225, FY: 2014) | Assets: $6,176,037 | Sales: $8,681,546 | NetInc: $1,380,339 | CFO: $1,443,575 | M-Score: 306.25 | F-Score: 0.0 | TariffRisk: 0.02 | Flag: ELEVATED: BENEISH OUTLIER
4. CO-DIAGNOSTICS, INC. (CIK: 0001692415, FY: 2020) | Assets: $71,237,197 | Sales: $74,552,758 | NetInc: $42,478,529 | CFO: $28,165,235 | M-Score: 305.88 | F-Score: 0.2 | TariffRisk: 0.07 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION
5. GREENWAVE TECHNOLOGY SOLUTIONS, INC. (CIK: 0001589149, FY: 2021) | Assets: $38,177,570 | Sales: $8,098,036 | NetInc: $-1,632,421 | CFO: $-1,037,843 | M-Score: 302.01 | F-Score: 0.0 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER

## Meta Model Deliberation:
{
  "batch_id": "SEC_0016",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "TURTLE BEACH CORPORATION",
      "identifier": "CIK: 0001493761, FY: 2014",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; UCC \u00a7 2-717 and UCC \u00a7 2-305(2) tariff surcharge deduction; 19 U.S.C. \u00a7 1313 drawback",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 326.45 >> -1.78 threshold signals extreme Beneish outlier / deterministic imbalance. Sloan (26460000-18290000)/246968000=0.0331 below 0.10, so accrual anomaly alone is not severe, but M-Score magnitude invalidates DSRI/GMI/AQI inputs and requires restatement verification before any UCC 2-717 deduction.",
      "estimated_claim_or_surcharge_usd": 8170000,
      "z3_smt_invariant": "FAIL: assert NetIncome == CFO + Accruals; 26460000 == 18290000 + 8170000 holds arithmetically, but Beneish invariant M-Score <= -1.78 is violated (326.45), Z3 returns UNSAT for clean balance-sheet model",
      "actionable_memo": "MF-02/MF-09: Freeze AP deduction pending SEC 10-K re-pull for CIK 0001493761 FY2014. Recompute DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA from primary filings, reconcile Assets $246,968,000 vs Sales $207,136,000, and verify CBP Form 7501 tariff exposure. Do not execute $8,170,000 accrual-based credit memo until imbalance source is isolated; downside capped per MF-01."
    },
    {
      "index": 2,
      "entity_name": "Jingbo Technology, Inc.",
      "identifier": "CIK: 0001647822, FY: 2023",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; Dechow F-Score; UCC \u00a7 2-717 and UCC \u00a7 2-305(2)",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 325.48 >> -1.78, F-Score 0.0, TariffRisk -3.07 anomalous. Sloan (-6395388-102130)/18357783=-0.3539, large negative accrual divergence with net loss despite positive CFO, indicating non-cash charges, impairments or data imbalance requiring forensic isolation.",
      "estimated_claim_or_surcharge_usd": 6497518,
      "z3_smt_invariant": "FAIL: assert NetIncome == CFO + Accruals; -6395388 == 102130 + -6497518 holds arithmetically, but Beneish invariant M-Score <= -1.78 violated (325.48) and TariffRisk >= 0 violated (-3.07), Z3 returns UNSAT",
      "actionable_memo": "MF-02/MF-06/MF-09: Halt tariff recovery - negative TariffRisk invalidates 3%-8% surcharge model under UCC 2-305(2). Re-pull SEC filing CIK 0001647822 FY2023, verify Assets $18,357,783, loss $-6,395,388 vs CFO $102,130, trace non-cash accruals. No UCC 2-717 withholding until Z3 invariant passes; investigate going-concern and impairment disclosure."
    },
    {
      "index": 3,
      "entity_name": "CHINA TIANFEIHONG WINE INC",
      "identifier": "CIK: 0001501225, FY: 2014",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; UCC \u00a7 2-717; 19 U.S.C. \u00a7 1313 drawback for imported wine merchandise",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 306.25 >> -1.78 signals high manipulation probability by threshold, but magnitude indicates outlier/corrupt Beneish inputs. Sloan (1380339-1443575)/6176037=-0.0102 is benign and CFO exceeds Net Income, contradicting accrual manipulation; F-Score 0.0 low misstatement risk.",
      "estimated_claim_or_surcharge_usd": 63236,
      "z3_smt_invariant": "FAIL: Beneish invariant M-Score <= -1.78 violated (306.25) => Z3 UNSAT for manipulation-free model; PASS on Sloan invariant |(NetIncome-CFO)/Assets| <= 0.10 with -0.0102",
      "actionable_memo": "MF-02/MF-09/MF-05: Claim magnitude $63,236 below $50k-$10M efficient recovery focus except as Beneish input audit. Recompute all 8 Beneish variables from CIK 0001501225 FY2014 10-K, check DSRI/ AQI for division-by-near-zero prior-year bases causing 306.25 spike. Verify import duties on wine for 19 USC 1313 eligibility before any UCC 2-717 deduction."
    },
    {
      "index": 4,
      "entity_name": "CO-DIAGNOSTICS, INC.",
      "identifier": "CIK: 0001692415, FY: 2020",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly > 0.10; Dechow F-Score; UCC \u00a7 2-717 and UCC \u00a7 2-305(2)",
      "forensic_verdict": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION - M-Score 305.88 >> -1.78, Sloan (42478529-28165235)/71237197=0.2009 > 0.10 severe cash-to-accrual divergence. Net Income $42,478,529 far exceeds CFO $28,165,235 on Sales $74,552,758, consistent with aggressive revenue/receivable accruals in FY2020 surge period. F-Score 0.2 does not offset Sloan+Beneish convergence.",
      "estimated_claim_or_surcharge_usd": 14313294,
      "z3_smt_invariant": "FAIL: assert Sloan <= 0.10 and M-Score <= -1.78; 0.2009 > 0.10 and 305.88 > -1.78, NetIncome == CFO + Accruals (42478529 == 28165235 + 14313294) holds but earnings-quality invariants Z3 UNSAT",
      "actionable_memo": "MF-01/MF-05/MF-09: Highest priority forensic audit. Pull CIK 0001692415 FY2020 10-K/Q, recompute DSRI, ChgRec, ChgInv, RSST Accruals, test revenue recognition and receivables collectability driving $14,313,294 accrual gap. Quantify any supplier tariff surcharges separately under UCC 2-717 with CBP 7501 proof; do not conflate earnings-manipulation accrual with recoverable tariff claim without MF-02 public-record anchoring."
    },
    {
      "index": 5,
      "entity_name": "GREENWAVE TECHNOLOGY SOLUTIONS, INC.",
      "identifier": "CIK: 0001589149, FY: 2021",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; Dechow F-Score; UCC \u00a7 2-717 and UCC \u00a7 2-305(2); 19 U.S.C. \u00a7 1313",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 302.01 >> -1.78, TariffRisk 1.0 maximal, F-Score 0.0. Sloan (-1632421-(-1037843))/38177570=-0.0156 benign, both Net Income and CFO negative, so accrual manipulation not corroborated by Sloan. Beneish spike likely driven by Sales $8,098,036 vs Assets $38,177,570 scale mismatch, acquisitions or prior-year base effects.",
      "estimated_claim_or_surcharge_usd": 594578,
      "z3_smt_invariant": "FAIL: Beneish invariant M-Score <= -1.78 violated (302.01) => Z3 UNSAT; PASS Sloan invariant |-0.0156| <= 0.10; NetIncome == CFO + Accruals (-1632421 == -1037843 + -594578) holds",
      "actionable_memo": "MF-02/MF-09: Recompute Beneish variables for CIK 0001589149 FY2021, investigate SGI, AQI, LVGI drivers and asset acquisitions inflating Assets vs Sales. TariffRisk 1.0 requires CBP 7501 and AP vendor-master verification before estimating any 3%-8% UCC 2-305(2) surcharge or UCC 2-717 deduction; current $594,578 accrual gap is not a proven tariff recovery."
    }
  ]
}
