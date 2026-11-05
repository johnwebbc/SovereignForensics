# SovereignForensics // Batch SEC Audit 0010
**Model:** `muse-wonder-1.0` | **Tokens:** 1738 (Cached: 1140) in / 2490 out | **Cost:** $0.0524

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0010 (5 REAL SEC FILERS):
1. Simply, Inc. (CIK: 0001274032, FY: 2021) | Assets: $30,437,000 | Sales: $79,111,000 | NetInc: $4,277,000 | CFO: $-2,209,000 | M-Score: 789.95 | F-Score: 270.27 | TariffRisk: 1.11 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. AMERICAN NANO SILICON TECHNOLOGIES, INC. (CIK: 0001415917, FY: 2013) | Assets: $27,057,450 | Sales: $798,390 | NetInc: $-2,086,393 | CFO: $-1,805,536 | M-Score: 737.57 | F-Score: 0.18 | TariffRisk: 29.98 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. Greenpro Capital Corp. (CIK: 0001597846, FY: 2015) | Assets: $9,068,366 | Sales: $2,946,164 | NetInc: $-133,671 | CFO: $-434,395 | M-Score: 724.45 | F-Score: 0.38 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
4. Titan Environmental Solutions Inc. (CIK: 0001514056, FY: 2022) | Assets: $8,552,595 | Sales: $1,582 | NetInc: $-6,448,875 | CFO: $-1,464,960 | M-Score: 724.37 | F-Score: 0.0 | TariffRisk: -0.01 | Flag: ELEVATED: BENEISH OUTLIER
5. Evolent Health, Inc. (CIK: 0001628908, FY: 2024) | Assets: $2,680,308,000 | Sales: $2,554,741,000 | NetInc: $1,596,000 | CFO: $142,582,000 | M-Score: 704.55 | F-Score: 270.27 | TariffRisk: 1.63 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "MICRO-BATCH LANE 1 #SEC_0010",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "Simply, Inc.",
      "identifier": "CIK: 0001274032, FY: 2021",
      "statutory_hook": "Beneish M-Score > -1.78 and Dechow F-Score > 1.0 and Sloan Accrual Anomaly > 0.10; UCC 2-717 / UCC 2-305(2) and 19 U.S.C. 1313 subject to CBP Form 7501 verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 789.95 >> -1.78 high manipulation probability, F-Score 270.27 >> 1.0 misstatement risk, Sloan (4277000-(-2209000))/30437000=0.2131 > 0.10 severe cash-to-accrual divergence. Net income positive while CFO negative.",
      "estimated_claim_or_surcharge_usd": 6486000,
      "z3_smt_invariant": "Z3 CHECK: NetIncome=4277000; CFO=-2209000; Accruals=NetIncome-CFO=6486000; 4277000 == -2209000+6486000 SAT; Sloan=6486000/30437000=0.2131 > 0.10 INVARIANT VIOLATED",
      "actionable_memo": "MF-02 Verify against SEC 10-K FY2021, CBP 7501 and AP vendor master before any deduction. MF-03 Do not execute UCC 2-717 setoff on forensic accrual amount alone; 6486000 is accrual exposure, not proven tariff surcharge. Isolate DSRI/GMI/AQI/TATA drivers, reconcile balance sheet imbalance, demand supporting receivables and tariff pass-through records."
    },
    {
      "index": 2,
      "entity_name": "AMERICAN NANO SILICON TECHNOLOGIES, INC.",
      "identifier": "CIK: 0001415917, FY: 2013",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly; UCC 2-717 / UCC 2-305(2) and 19 U.S.C. 1313 subject to CBP Form 7501 verification, TariffRisk 29.98 requires source verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 737.57 >> -1.78 high manipulation probability, F-Score 0.18 <= 1.0 low Dechow risk, Sloan (-2086393-(-1805536))/27057450=-0.0104 not > 0.10. Loss and negative CFO consistent, accrual anomaly not Sloan-driven; extreme M-Score likely distorted by Sales 798390 vs Assets 27057450.",
      "estimated_claim_or_surcharge_usd": 280857,
      "z3_smt_invariant": "Z3 CHECK: NetIncome=-2086393; CFO=-1805536; Accruals=NetIncome-CFO=-280857; -2086393 == -1805536-280857 SAT; Sloan=-280857/27057450=-0.0104 <= 0.10 INVARIANT PASSED",
      "actionable_memo": "MF-02 Verify against SEC filing FY2013 and balance sheet components causing imbalance; investigate Beneish inputs DSRI/GMI/AQI/SGI for division-by-small-base distortion. MF-05 Accrual exposure 280857 does not establish a 50k+ tariff claim; require CBP 7501, import and AP surcharge proof before UCC 2-717 action."
    },
    {
      "index": 3,
      "entity_name": "Greenpro Capital Corp.",
      "identifier": "CIK: 0001597846, FY: 2015",
      "statutory_hook": "Beneish M-Score > -1.78; UCC 2-717 / UCC 2-305(2) and 19 U.S.C. 1313 subject to CBP Form 7501 verification",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 724.45 >> -1.78 high manipulation probability, F-Score 0.38 <= 1.0 low Dechow risk, Sloan (-133671-(-434395))/9068366=0.0332 <= 0.10 no severe Sloan flag. Negative income and CFO, moderate positive accrual gap.",
      "estimated_claim_or_surcharge_usd": 300724,
      "z3_smt_invariant": "Z3 CHECK: NetIncome=-133671; CFO=-434395; Accruals=NetIncome-CFO=300724; -133671 == -434395+300724 SAT; Sloan=300724/9068366=0.0332 <= 0.10 INVARIANT PASSED",
      "actionable_memo": "MF-02 Recompute Beneish 8 variables from FY2015 10-K comparatives to locate outlier driver; extreme M-Score may reflect small-base ratios. MF-03 No self-enforcing tariff deduction supported on this record alone; obtain AP vendor master, surcharge invoices and CBP records to quantify any recoverable amount separately from 300724 accrual gap."
    },
    {
      "index": 4,
      "entity_name": "Titan Environmental Solutions Inc.",
      "identifier": "CIK: 0001514056, FY: 2022",
      "statutory_hook": "Beneish M-Score > -1.78; UCC 2-717 / UCC 2-305(2) and 19 U.S.C. 1313 subject to CBP Form 7501 verification",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 724.37 >> -1.78 high manipulation probability, F-Score 0.0 <= 1.0 no Dechow risk, Sloan (-6448875-(-1464960))/8552595=-0.5827 <= 0.10 negative accruals. Sales only 1582 vs Assets 8552595 and loss -6448875 indicates pre-revenue/distorted ratios, not positive accrual inflation.",
      "estimated_claim_or_surcharge_usd": 4983915,
      "z3_smt_invariant": "Z3 CHECK: NetIncome=-6448875; CFO=-1464960; Accruals=NetIncome-CFO=-4983915; -6448875 == -1464960-4983915 SAT; Sloan=-4983915/8552595=-0.5827 <= 0.10 INVARIANT PASSED",
      "actionable_memo": "MF-02 Verify FY2022 filing, going-concern, non-cash charges and asset composition; decompose SGI/DSRI where Sales 1582 creates mathematical outliers. MF-05 4983915 is absolute non-cash accrual gap, not a tariff surcharge claim. No UCC 2-717 deduction without documented supplier surcharge and CBP 7501 linkage."
    },
    {
      "index": 5,
      "entity_name": "Evolent Health, Inc.",
      "identifier": "CIK: 0001628908, FY: 2024",
      "statutory_hook": "Beneish M-Score > -1.78 and Dechow F-Score > 1.0; UCC 2-717 / UCC 2-305(2) and 19 U.S.C. 1313 subject to CBP Form 7501 verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 704.55 >> -1.78 high manipulation probability, F-Score 270.27 >> 1.0 misstatement risk, Sloan (1596000-142582000)/2680308000=-0.0526 <= 0.10 no Sloan flag. CFO strongly exceeds near-zero net income, indicating negative accruals/dechow inputs require reconciliation rather than earnings inflation via accruals.",
      "estimated_claim_or_surcharge_usd": 140986000,
      "z3_smt_invariant": "Z3 CHECK: NetIncome=1596000; CFO=142582000; Accruals=NetIncome-CFO=-140986000; 1596000 == 142582000-140986000 SAT; Sloan=-140986000/2680308000=-0.0526 <= 0.10 INVARIANT PASSED",
      "actionable_memo": "MF-02 Verify FY2024 10-K, RSST accruals, receivables/inventory and issuance inputs driving F-Score 270.27; extreme scores suggest data-scaling or balance-sheet imbalance error. MF-03 140986000 is CFO-NetIncome gap, not proven tariff recovery; require CBP 7501, importer-of-record and AP surcharge evidence before any UCC 2-717 or 1313 drawback claim."
    }
  ]
}
