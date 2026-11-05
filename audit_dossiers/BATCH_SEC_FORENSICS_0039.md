# SovereignForensics // Batch SEC Audit 0039
**Model:** `muse-wonder-1.0` | **Tokens:** 1745 (Cached: 1140) in / 2656 out | **Cost:** $0.0558

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0039 (5 REAL SEC FILERS):
1. ARROWHEAD PHARMACEUTICALS, INC. (CIK: 0000879407, FY: 2017) | Assets: $128,176,505 | Sales: $31,407,709 | NetInc: $-5,519,741 | CFO: $nan | M-Score: 69.67 | F-Score: 0.16 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. PHATHOM PHARMACEUTICALS, INC. (CIK: 0001783183, FY: 2024) | Assets: $413,842,000 | Sales: $55,252,000 | NetInc: $-201,592,000 | CFO: $-137,580,000 | M-Score: 68.73 | F-Score: 0.18 | TariffRisk: 0.03 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. BIMI Holdings Inc. (CIK: 0001213660, FY: 2020) | Assets: $33,202,139 | Sales: $12,844,902 | NetInc: $-1,997,083 | CFO: $-2,064,792 | M-Score: 68.26 | F-Score: 1.04 | TariffRisk: -0.06 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. VIVIC CORP. (CIK: 0001703073, FY: 2024) | Assets: $5,494,294 | Sales: $5,950,692 | NetInc: $2,850,514 | CFO: $-261,488 | M-Score: 68.21 | F-Score: 0.44 | TariffRisk: 0.44 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. Palvella Therapeutics, Inc. (CIK: 0001583648, FY: 2017) | Assets: $103,876,000 | Sales: $25,275,000 | NetInc: $-17,647,000 | CFO: $nan | M-Score: 67.81 | F-Score: 0.39 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0039",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "ARROWHEAD PHARMACEUTICALS, INC.",
      "identifier": "CIK: 0000879407, FY: 2017",
      "statutory_hook": "Beneish M-Score / Sloan Accrual Anomaly / MF-09 Deterministic Verification; UCC § 2-717 and 19 U.S.C. § 1313 NOT actionable on unverified CFO",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - REJECT/QUARANTINE. M-Score 69.67 >> -1.78 threshold is mathematically implausible and indicates corrupted inputs, not proven manipulation. CFO=NaN prevents Sloan and Dechow verification. F-Score 0.16 < 1.0 does not independently support misstatement. No UCC § 2-305(2)/§ 2-717 tariff deduction verified.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "FAIL/UNSAT: NetIncome(-5519741) = CFO(NaN) + Accruals => Accruals undefined; Sloan=(NetIncome-CFO)/128176505 unsatisfiable; Z3 invariant cannot verify",
      "actionable_memo": "Do not withhold AP or claim drawback. Re-extract CFO, average assets, DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA from audited 10-K and CBP Form 7501 if any. TariffRisk 1.0 is unanchored without import/surcharge invoices. Re-run Beneish/Dechow after NaN remediation; MF-02 public-record verifiability fails at present."
    },
    {
      "index": 2,
      "entity_name": "PHATHOM PHARMACEUTICALS, INC.",
      "identifier": "CIK: 0001783183, FY: 2024",
      "statutory_hook": "Beneish M-Score / Sloan Accrual Anomaly; UCC § 2-717 inapplicable - TariffRisk 0.03, no verified 3%-8% surcharge pass-through failure under UCC § 2-305(2)",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - DATA INTEGRITY FAILURE, NOT PROVEN MANIPULATION. M-Score 68.73 >> -1.78 is implausible/corrupted. Sloan = (-201592000 - (-137580000))/413842000 = -0.1547, negative accruals inconsistent with positive earnings-inflation hypothesis. F-Score 0.18 < 1.0 low misstatement risk.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "CHECKABLE BUT INPUT-INVALID: NetIncome(-201592000) = CFO(-137580000) + Accruals(-64012000) holds arithmetically; Beneish inputs producing 68.73 violate bounded-variable invariants",
      "actionable_memo": "No credit-memo deduction authorized. Accrual magnitude $64,012,000 is a loss-driven CFO/NetIncome gap requiring 10-K reconciliation of non-cash charges, not a recoverable surcharge. Verify Beneish 8 variables from prior/current year filings before any forensic referral. Tariff exposure de minimis at 0.03."
    },
    {
      "index": 3,
      "entity_name": "BIMI Holdings Inc.",
      "identifier": "CIK: 0001213660, FY: 2020",
      "statutory_hook": "Dechow F-Score Logit Misstatement Multiplier > 1.0; Beneish M-Score; UCC § 2-717 inapplicable - TariffRisk -0.06, no positive surcharge identified",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE WITH ELEVATED F-SCORE. M-Score 68.26 >> -1.78 implausible/corrupted. F-Score 1.04 > 1.0 marginally signals misstatement risk requiring RSST/ChgRec/ChgInv/SoftAssets review. Sloan = (-1997083 - (-2064792))/33202139 = 0.0020, well below 0.10, no Sloan accrual anomaly.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "ARITHMETIC PASS, MODEL FAIL: NetIncome(-1997083) = CFO(-2064792) + Accruals(67709) satisfied; Beneish invariant violated by M-Score 68.26 outside feasible range",
      "actionable_memo": "No AP withholding or 19 U.S.C. § 1313 claim quantified. Prioritize Dechow component audit from 10-K: receivables, inventory, soft assets, issuance and ROA change to validate F-Score 1.04. Negative TariffRisk precludes UCC § 2-305(2) surcharge recovery. Recompute M-Score from source statements; do not allege manipulation on corrupted score."
    },
    {
      "index": 4,
      "entity_name": "VIVIC CORP.",
      "identifier": "CIK: 0001703073, FY: 2024",
      "statutory_hook": "Sloan Accrual Anomaly > 0.10; Beneish M-Score; Dechow F-Score; potential UCC § 2-717 review only after surcharge invoices verified - TariffRisk 0.44",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE AND SEVERE SLOAN ANOMALY. Sloan = (2850514 - (-261488))/5494294 = 0.5664 >> 0.10, indicating earnings entirely accrual-driven with negative CFO despite positive NetIncome. M-Score 68.21 >> -1.78 implausible/corrupted. F-Score 0.44 < 1.0 does not confirm Dechow misstatement.",
      "estimated_claim_or_surcharge_usd": 3112002,
      "z3_smt_invariant": "ARITHMETIC PASS, QUALITY FAIL: NetIncome(2850514) = CFO(-261488) + Accruals(3112002) satisfied; Accruals/AverageAssets=0.5664 violates Sloan <=0.10 quality invariant",
      "actionable_memo": "Flag $3,112,002 accrual gap for forensic review, not as automatic recoverable cash. Demand receivables/inventory accrual schedules, revenue-recognition support from 10-K/Q, and any supplier tariff invoices before invoking UCC § 2-717. Illustrative 5% surcharge on $5,950,692 sales at 0.44 risk is unverified and excluded. Recompute Beneish from source data."
    },
    {
      "index": 5,
      "entity_name": "Palvella Therapeutics, Inc.",
      "identifier": "CIK: 0001583648, FY: 2017",
      "statutory_hook": "Beneish M-Score / Sloan Accrual Anomaly / MF-09 Deterministic Verification; UCC § 2-717 and 19 U.S.C. § 1313 NOT actionable on unverified CFO",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - REJECT/QUARANTINE. M-Score 67.81 >> -1.78 threshold is mathematically implausible and indicates corrupted inputs. CFO=NaN prevents Sloan, TATA and Dechow cash-margin verification. F-Score 0.39 < 1.0 does not independently support misstatement. No verified tariff surcharge.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "FAIL/UNSAT: NetIncome(-17647000) = CFO(NaN) + Accruals => Accruals undefined; Sloan=(NetIncome-CFO)/103876000 unsatisfiable; Z3 invariant cannot verify",
      "actionable_memo": "Do not withhold AP or claim 99% drawback under 19 U.S.C. § 1313. Re-extract CFO and all Beneish/Dechow variables from audited 10-K, and obtain CBP Form 7501/AP vendor records if TariffRisk 1.0 is to be substantiated. MF-02 and MF-09 fail until NaN remediated and M-Score recomputed within feasible bounds."
    }
  ]
}
