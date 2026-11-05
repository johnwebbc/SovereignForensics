# SovereignForensics // Batch SEC Audit 0007
**Model:** `muse-wonder-1.0` | **Tokens:** 1738 (Cached: 1140) in / 2679 out | **Cost:** $0.0562

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0007 (5 REAL SEC FILERS):
1. SKYX Platforms Corp. (CIK: 0001598981, FY: 2023) | Assets: $76,341,203 | Sales: $58,785,762 | NetInc: $-27,035,941 | CFO: $-12,998,073 | M-Score: 1210.35 | F-Score: 1.19 | TariffRisk: -0.0 | Flag: ELEVATED: DECHOW MISSTATEMENT RISK
2. Nobilis Health Corp. (CIK: 0001409916, FY: 2016) | Assets: $305,435,000 | Sales: $285,744,000 | NetInc: $50,840,000 | CFO: $6,715,000 | M-Score: 1109.6 | F-Score: 0.71 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. MIX 1 LIFE, INC. (CIK: 0001501112, FY: 2015) | Assets: $22,755,843 | Sales: $2,279,226 | NetInc: $-1,995,519 | CFO: $-1,116,850 | M-Score: 1007.63 | F-Score: 3.37 | TariffRisk: -0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. AppTech Payments Corp. (CIK: 0001070050, FY: 2023) | Assets: $12,519,000 | Sales: $504,000 | NetInc: $-16,281,000 | CFO: $-8,199,000 | M-Score: 993.25 | F-Score: 0.39 | TariffRisk: 0.91 | Flag: ELEVATED: BENEISH OUTLIER
5. Exceed World, Inc. (CIK: 0001634293, FY: 2018) | Assets: $29,239,878 | Sales: $36,860,282 | NetInc: $4,233,254 | CFO: $nan | M-Score: 991.07 | F-Score: 0.55 | TariffRisk: -0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0007",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "SKYX Platforms Corp.",
      "identifier": "CIK: 0001598981, FY: 2023",
      "statutory_hook": "Beneish M-Score > -1.78; Dechow F-Score > 1.0; Sloan Accrual Anomaly; UCC 2-717 and 19 USC 1313 not established without CBP Form 7501 verification",
      "forensic_verdict": "ELEVATED: DECHOW MISSTATEMENT RISK - M-Score 1210.35 is an extreme outlier far above -1.78 threshold, indicating probable data distortion or manipulation inputs requiring recomputation from primary 10-K. F-Score 1.19 > 1.0. Sloan = (-27035941 - (-12998073)) / 76341203 = -0.1839, absolute accrual magnitude > 0.10.",
      "estimated_claim_or_surcharge_usd": 14037868,
      "z3_smt_invariant": "FAIL/UNVERIFIED: NetIncome = CFO + Accruals implies Accruals = -14037868; Sloan -0.1839 violates |Sloan| <= 0.10 invariant. M-Score 1210.35 violates plausible Beneish range, requires DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA recomputation.",
      "actionable_memo": "Do not execute AP deduction on tariff basis: TariffRisk -0.0 shows no verified surcharge. Recompute Beneish and Dechow from audited 10-K balance sheet, income and cash-flow statements, reconcile receivables, gross margin and accruals, and obtain CBP 7501 evidence before any UCC 2-717 claim."
    },
    {
      "index": 2,
      "entity_name": "Nobilis Health Corp.",
      "identifier": "CIK: 0001409916, FY: 2016",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly > 0.10; UCC 2-717 and 19 USC 1313 not established without CBP Form 7501 verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 1109.6 is an extreme outlier far above -1.78. F-Score 0.71 <= 1.0 does not clear risk. Sloan = (50840000 - 6715000) / 305435000 = 0.1445 > 0.10, flagging severe cash-to-accrual divergence: net income greatly exceeds CFO.",
      "estimated_claim_or_surcharge_usd": 44125000,
      "z3_smt_invariant": "FAIL: NetIncome = CFO + Accruals implies Accruals = 44125000; Sloan 0.1445 violates Sloan <= 0.10 invariant. M-Score 1109.6 violates plausible Beneish range, indicating balance-sheet input imbalance.",
      "actionable_memo": "No verified tariff surcharge claim despite TariffRisk 1.0, which is inconsistent with healthcare operations and requires source verification. Prioritize forensic reconciliation of receivables, revenue recognition and accruals from 10-K, and do not withhold AP amounts without documented supplier surcharge invoices and CBP records."
    },
    {
      "index": 3,
      "entity_name": "MIX 1 LIFE, INC.",
      "identifier": "CIK: 0001501112, FY: 2015",
      "statutory_hook": "Beneish M-Score > -1.78; Dechow F-Score > 1.0; UCC 2-717 and 19 USC 1313 not established without CBP Form 7501 verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 1007.63 is an extreme outlier far above -1.78. F-Score 3.37 >> 1.0 signals high Dechow misstatement risk. Sloan = (-1995519 - (-1116850)) / 22755843 = -0.0386, within 0.10 threshold, so Sloan alone does not confirm manipulation.",
      "estimated_claim_or_surcharge_usd": 878669,
      "z3_smt_invariant": "FAIL/UNVERIFIED: NetIncome = CFO + Accruals implies Accruals = -878669; Sloan -0.0386 satisfies |Sloan| <= 0.10, but M-Score 1007.63 and F-Score 3.37 violate Beneish <= -1.78 and F-Score <= 1.0 invariants, indicating input imbalance.",
      "actionable_memo": "TariffRisk -0.01 shows no verified tariff exposure; estimated amount is accrual-at-risk, not a recoverable surcharge. Recompute RSST Accruals, ChgRec, ChgInv, SoftAssets, ChgCashMargin, ChgROA and Issuance from primary filings before any claim, credit memo or AP deduction."
    },
    {
      "index": 4,
      "entity_name": "AppTech Payments Corp.",
      "identifier": "CIK: 0001070050, FY: 2023",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly; UCC 2-305(2), UCC 2-717 and 19 USC 1313 require verified surcharge and CBP Form 7501 evidence",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 993.25 is an extreme outlier far above -1.78. F-Score 0.39 <= 1.0. Sloan = (-16281000 - (-8199000)) / 12519000 = -0.6456, absolute magnitude >> 0.10 with losses far exceeding CFO on only $504000 sales, flagging severe accrual and going-concern distortion risk.",
      "estimated_claim_or_surcharge_usd": 8082000,
      "z3_smt_invariant": "FAIL: NetIncome = CFO + Accruals implies Accruals = -8082000; Sloan -0.6456 violates |Sloan| <= 0.10 invariant. Sales/Assets and loss magnitude violate plausible operating-scale invariants pending recomputation.",
      "actionable_memo": "TariffRisk 0.91 is unverified and inconsistent with payments-business profile; do not treat accrual-at-risk as tariff recovery. Verify any 3%-8% supplier surcharge with invoices, contracts and CBP 7501s, recompute Beneish variables from 10-K, and assess liquidity before any UCC 2-717 deduction."
    },
    {
      "index": 5,
      "entity_name": "Exceed World, Inc.",
      "identifier": "CIK: 0001634293, FY: 2018",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly indeterminate due to missing CFO; UCC 2-717 and 19 USC 1313 not established without CBP Form 7501 verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 991.07 is an extreme outlier far above -1.78. F-Score 0.55 <= 1.0 cannot be relied upon. CFO is NaN/missing, so Sloan = (4233254 - CFO) / 29239878 is indeterminate and cash earnings quality cannot be verified.",
      "estimated_claim_or_surcharge_usd": 4233254,
      "z3_smt_invariant": "UNSAT/INDETERMINATE: NetIncome = CFO + Accruals cannot be verified because CFO is missing/NaN; Accruals and Sloan are undefined. M-Score 991.07 violates plausible Beneish range invariant.",
      "actionable_memo": "TariffRisk -0.01 shows no verified tariff claim; amount shown is unverified net income at risk, not a recoverable surcharge. Obtain complete audited cash-flow statement from 10-K, restore CFO, recompute Sloan, Beneish and Dechow, and obtain CBP documentation before any credit memo or AP action."
    }
  ]
}
