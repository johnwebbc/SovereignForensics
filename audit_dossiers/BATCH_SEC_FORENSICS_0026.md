# SovereignForensics // Batch SEC Audit 0026
**Model:** `muse-wonder-1.0` | **Tokens:** 1727 (Cached: 1140) in / 2265 out | **Cost:** $0.0479

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0026 (5 REAL SEC FILERS):
1. SecureTech Innovations, Inc. (CIK: 0001703157, FY: 2025) | Assets: $19,190,202 | Sales: $7,720,757 | NetInc: $203,298 | CFO: $nan | M-Score: 141.57 | F-Score: 0.0 | TariffRisk: 2.67 | Flag: ELEVATED: BENEISH OUTLIER
2. Pernix Group, Inc. (CIK: 0001082198, FY: 2015) | Assets: $119,428,120 | Sales: $195,491,324 | NetInc: $-1,382,856 | CFO: $-4,650,272 | M-Score: 137.09 | F-Score: 0.49 | TariffRisk: 4.18 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. Carisma Therapeutics Inc. (CIK: 0001485003, FY: 2016) | Assets: $104,097,000 | Sales: $29,981,000 | NetInc: $19,487,000 | CFO: $nan | M-Score: 135.03 | F-Score: 0.31 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. CHINA HEALTH INDUSTRIES HOLDINGS, INC. (CIK: 0001309057, FY: 2023) | Assets: $50,747,518 | Sales: $111,579 | NetInc: $-353,950 | CFO: $2,115,726 | M-Score: 134.88 | F-Score: 0.11 | TariffRisk: 11329.1 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. ICON ECI FUND SIXTEEN (CIK: 0001561679, FY: 2014) | Assets: $20,596,681 | Sales: $939,235 | NetInc: $-100,379 | CFO: $593,696 | M-Score: 130.64 | F-Score: 0.36 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "LANE 1 #SEC_0026",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "SecureTech Innovations, Inc.",
      "identifier": "CIK: 0001703157, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly review; UCC § 2-717 and 19 U.S.C. § 1313 not triggered without documented tariff surcharge, CBP Form 7501, or AP remittance",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 141.57 >> -1.78 signals extreme Beneish variable distortion, likely from NaN/missing CFO and incomplete inputs rather than verified manipulation. CFO $nan prevents Sloan and Z3 verification. No MF-02 public-record verifiable tariff claim established.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNVERIFIABLE/UNSAT: NetIncome 203298 = CFO NaN + Accruals cannot be satisfied; Sloan ((203298-NaN)/19190202) undefined",
      "actionable_memo": "DO NOT deduct under UCC 2-717. No concrete $50k+ surcharge, counterparty AP record, or CBP refund documented per MF-02/MF-05/MF-06. Obtain complete 10-K/Q cash-flow statement, recompute DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA from primary filings, and only pursue if verified inputs still exceed -1.78."
    },
    {
      "index": 2,
      "entity_name": "Pernix Group, Inc.",
      "identifier": "CIK: 0001082198, FY: 2015",
      "statutory_hook": "Beneish M-Score > -1.78 and Dechow F-Score review; UCC § 2-717 and 19 U.S.C. § 1313 not triggered without documented tariff surcharge, CBP Form 7501, or AP remittance",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 137.09 >> -1.78 is not credible as a standalone manipulation proof and indicates corrupted/imbalanced inputs. F-Score 0.49 < 1.0 does not signal Dechow misstatement. Sloan 0.0274 < 0.10, no severe accrual anomaly despite flagged data.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: -1382856 = -4650272 + 3267416; Sloan = (-1382856 - (-4650272))/119428120 = 0.0274",
      "actionable_memo": "DO NOT deduct under UCC 2-717. TariffRisk 4.18 with no CBP 7501, surcharge invoice, or reliquidation right under CIT Slip Op. 26-123 verified. Reconcile balance-sheet imbalance from original SEC filing, recompute Beneish/Dechow from audited statements, and close unless primary-source discrepancy >= $50000 is documented."
    },
    {
      "index": 3,
      "entity_name": "Carisma Therapeutics Inc.",
      "identifier": "CIK: 0001485003, FY: 2016",
      "statutory_hook": "Beneish M-Score > -1.78 review; UCC § 2-717 and 19 U.S.C. § 1313 not triggered without documented tariff surcharge, CBP Form 7501, or AP remittance",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 135.03 >> -1.78 indicates extreme input distortion, not verified manipulation. F-Score 0.31 < 1.0 does not signal Dechow misstatement. CFO $nan prevents Sloan/TATA verification and MF-09 deterministic verification fails.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNVERIFIABLE/UNSAT: NetIncome 19487000 = CFO NaN + Accruals cannot be satisfied; Sloan ((19487000-NaN)/104097000) undefined",
      "actionable_memo": "DO NOT deduct under UCC 2-717. No importer/distributor surcharge, open-price-term violation under UCC 2-305(2), or drawback claim documented. Obtain FY2016 10-K/Q complete cash-flow and balance-sheet data, verify entity/period identity for CIK 0001485003, and recompute all forensic scores from primary sources before any action."
    },
    {
      "index": 4,
      "entity_name": "CHINA HEALTH INDUSTRIES HOLDINGS, INC.",
      "identifier": "CIK: 0001309057, FY: 2023",
      "statutory_hook": "Beneish M-Score > -1.78 review; UCC § 2-717 and 19 U.S.C. § 1313 not triggered without documented tariff surcharge, CBP Form 7501, or AP remittance",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 134.88 >> -1.78 and TariffRisk 11329.1 are mathematical artifacts of Sales $111579 vs Assets $50747518, not proof of tariff exposure. F-Score 0.11 < 1.0. Sloan -0.0487, absolute < 0.10, no severe positive accrual anomaly; CFO exceeds Net Income.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: -353950 = 2115726 + -2469676; Sloan = (-353950-2115726)/50747518 = -0.0487",
      "actionable_memo": "DO NOT deduct under UCC 2-717. TariffRisk cannot be monetized without sales/import volume, supplier invoices showing 3%-8% surcharge, and CBP records per MF-02/MF-05. Investigate going-concern, revenue collapse, and balance-sheet imbalance from original filing; no credit memo authorized on current evidence."
    },
    {
      "index": 5,
      "entity_name": "ICON ECI FUND SIXTEEN",
      "identifier": "CIK: 0001561679, FY: 2014",
      "statutory_hook": "Beneish M-Score > -1.78 review; UCC § 2-717 and 19 U.S.C. § 1313 not triggered without documented tariff surcharge, CBP Form 7501, or AP remittance",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - M-Score 130.64 >> -1.78 indicates corrupted Beneish inputs for a fund entity where standard operating-company Beneish variables may be inapplicable. F-Score 0.36 < 1.0. Sloan -0.0337, absolute < 0.10, no severe accrual anomaly.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: -100379 = 593696 + -694075; Sloan = (-100379-593696)/20596681 = -0.0337",
      "actionable_memo": "DO NOT deduct under UCC 2-717. No goods buyer-seller relationship, tariff surcharge, or CBP 7501 documented; fund structure makes UCC Article 2 and drawback analysis inapplicable on current record. Verify fund financial statements from SEC filing and close unless a concrete AP counterparty claim >= $50000 is independently documented."
    }
  ]
}
