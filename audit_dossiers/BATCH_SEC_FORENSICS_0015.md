# SovereignForensics // Batch SEC Audit 0015
**Model:** `muse-wonder-1.0` | **Tokens:** 1728 (Cached: 1140) in / 2643 out | **Cost:** $0.0554

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0015 (5 REAL SEC FILERS):
1. MEDWELLAI, INC. (CIK: 0001520118, FY: 2021) | Assets: $13,363,965 | Sales: $1,851,390 | NetInc: $-1,081,775 | CFO: $-671,101 | M-Score: 379.59 | F-Score: 0.97 | TariffRisk: -2.63 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. China Xuefeng Environmental Engineering Inc. (CIK: 0001518487, FY: 2016) | Assets: $35,297,419 | Sales: $22,187,094 | NetInc: $5,992,930 | CFO: $5,457,579 | M-Score: 371.6 | F-Score: 0.33 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
3. Crisp Momentum Inc. (CIK: 0000924396, FY: 2023) | Assets: $5,820,481 | Sales: $81,179 | NetInc: $-2,556,714 | CFO: $-286,527 | M-Score: 343.53 | F-Score: 0.24 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
4. MIGOM GLOBAL CORP. (CIK: 0001697412, FY: 2020) | Assets: $19,280,025 | Sales: $3,839,242 | NetInc: $nan | CFO: $2,178,574 | M-Score: 338.52 | F-Score: 0.39 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
5. HWH     INTERNATIONAL INC. (CIK: 0001897245, FY: 2025) | Assets: $6,408,722 | Sales: $1,253,577 | NetInc: $-2,630,620 | CFO: $-1,750,290 | M-Score: 334.86 | F-Score: 270.27 | TariffRisk: -0.86 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0015",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "MEDWELLAI, INC.",
      "identifier": "CIK: 0001520118, FY: 2021",
      "statutory_hook": "No verifiable UCC 2-717, UCC 2-305(2), or 19 USC 1313 claim in provided data; forensic screening under Beneish M-Score, Dechow F-Score, and Sloan Accrual Anomaly only",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE flagged; M-Score 379.59 >> -1.78 threshold signals extreme Beneish outlier/manipulation probability, but value is implausibly large and likely reflects input/data distortion requiring re-verification from original 10-K. F-Score 0.97 < 1.0 borderline. Sloan Accrual: (-1081775 - (-671101)) / 13363965 = -0.0307, below 0.10 threshold.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/UNVERIFIED: Assert NetIncome == CFO + Accruals; -1081775 == -671101 + Accruals implies Accruals == -410674, Sloan ratio -0.0307; balance-sheet imbalance flag prevents deterministic verification without full Assets = Liabilities + Equity inputs",
      "actionable_memo": "Do not execute AP deduction or credit memo on this data alone. Pull original SEC 10-K for FY2021, recompute all 8 Beneish variables and balance-sheet identity, reconcile receivables, assets, and accruals, and obtain CBP Form 7501/AP surcharge invoices before asserting any tariff recovery; no recoverable amount is publicly verifiable from the supplied figures."
    },
    {
      "index": 2,
      "entity_name": "China Xuefeng Environmental Engineering Inc.",
      "identifier": "CIK: 0001518487, FY: 2016",
      "statutory_hook": "No verifiable UCC 2-717, UCC 2-305(2), or 19 USC 1313 claim in provided data; forensic screening under Beneish M-Score, Dechow F-Score, and Sloan Accrual Anomaly only",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER; M-Score 371.6 >> -1.78 signals extreme Beneish outlier, but magnitude is implausible for a standard Beneish calculation and likely indicates missing prior-year inputs or data scaling error. F-Score 0.33 < 1.0 low misstatement signal. Sloan Accrual: (5992930 - 5457579) / 35297419 = 0.0152, below 0.10 threshold, cash earnings broadly support net income.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SATISFIABLE ON ACCRUAL IDENTITY ONLY: 5992930 == 5457579 + Accruals implies Accruals == 535351, Sloan ratio 0.0152; full NetIncome = CFO + Accruals and balance-sheet invariants cannot be Z3-verified without complete filing inputs",
      "actionable_memo": "Recompute Beneish DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, and TATA from the original FY2016 and prior-year SEC filings before any conclusion; investigate the source of the 371.6 M-Score. No tariff surcharge, CBP entry, or AP counterparty evidence is supplied, so estimated recoverable claim is $0 pending documentary proof."
    },
    {
      "index": 3,
      "entity_name": "Crisp Momentum Inc.",
      "identifier": "CIK: 0000924396, FY: 2023",
      "statutory_hook": "No verifiable UCC 2-717, UCC 2-305(2), or 19 USC 1313 claim in provided data; forensic screening under Beneish M-Score, Dechow F-Score, and Sloan Accrual Anomaly only",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER; M-Score 343.53 >> -1.78 is an extreme, implausible Beneish value requiring recalculation. F-Score 0.24 < 1.0 low. Sloan Accrual: (-2556714 - (-286527)) / 5820481 = -0.3900, severe negative accrual/cash divergence in absolute terms, with NetInc $-2,556,714 on Sales of only $81,179 against Assets $5,820,481 indicating heavy losses/non-cash charges to investigate, not a >0.10 positive Sloan flag.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SATISFIABLE ON ACCRUAL IDENTITY ONLY: -2556714 == -286527 + Accruals implies Accruals == -2270187, Sloan ratio -0.3900; deterministic verification fails without complete balance-sheet and prior-year Beneish inputs",
      "actionable_memo": "Pull FY2023 10-K and prior-year comparatives, explain loss drivers, impairments, and non-cash accruals, and recompute M-Score from source data. No CBP Form 7501, supplier surcharge invoice, or AP vendor record is supplied, so do not withhold payment and book $0 verified tariff claim."
    },
    {
      "index": 4,
      "entity_name": "MIGOM GLOBAL CORP.",
      "identifier": "CIK: 0001697412, FY: 2020",
      "statutory_hook": "No verifiable UCC 2-717, UCC 2-305(2), or 19 USC 1313 claim in provided data; forensic screening under Beneish M-Score, Dechow F-Score, and Sloan Accrual Anomaly only",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER WITH MISSING DATA; M-Score 338.52 >> -1.78 is an extreme, implausible Beneish value. F-Score 0.39 < 1.0. NetInc is NaN, so Sloan Accrual (NetIncome - CFO) / Assets is undefined and earnings quality cannot be assessed despite CFO $2,178,574 on Sales $3,839,242 and Assets $19,280,025.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/UNDEFINED: NetIncome is NaN; assert NetIncome == CFO + Accruals fails because NaN != 2178574 + Accruals for any real Accruals; Z3 invariant cannot be satisfied or verified",
      "actionable_memo": "Reject this record for audit proof until Net Income is sourced from the original FY2020 SEC filing; then recompute Sloan, Beneish, and F-Score and reconcile positive CFO to earnings. No tariff, drawback, surcharge, or AP evidence is supplied, so verified claim is $0 and no deduction memo should issue."
    },
    {
      "index": 5,
      "entity_name": "HWH INTERNATIONAL INC.",
      "identifier": "CIK: 0001897245, FY: 2025",
      "statutory_hook": "No verifiable UCC 2-717, UCC 2-305(2), or 19 USC 1313 claim in provided data; forensic screening under Beneish M-Score, Dechow F-Score, and Sloan Accrual Anomaly only",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE flagged; M-Score 334.86 >> -1.78 extreme Beneish outlier and F-Score 270.27 >> 1.0 extreme Dechow value, both magnitudes implausible under standard formulas and indicative of corrupted/missing inputs. Sloan Accrual: (-2630620 - (-1750290)) / 6408722 = -0.1374, large negative accrual divergence, not a >0.10 positive Sloan flag.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/UNVERIFIED: -2630620 == -1750290 + Accruals implies Accruals == -880330, Sloan ratio -0.1374; balance-sheet imbalance flag and extreme F-Score/M-Score prevent deterministic verification without full Assets = Liabilities + Equity and RSST inputs from the filing",
      "actionable_memo": "Escalate for source-data validation: retrieve FY2025 SEC filing, rebuild trial balance, recompute Dechow RSST, ChgRec, ChgInv, SoftAssets, ChgCashMargin, ChgROA, and Issuance, and recompute Beneish from prior-year data. No CBP, surcharge, or AP vendor evidence is supplied, so do not assert drawback or UCC deduction; verified claim is $0."
    }
  ]
}
