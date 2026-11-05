# SovereignForensics // Batch SEC Audit 0012
**Model:** `muse-wonder-1.0` | **Tokens:** 1732 (Cached: 1140) in / 2706 out | **Cost:** $0.0567

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0012 (5 REAL SEC FILERS):
1. QUEST PATENT RESEARCH CORPORATION (CIK: 0000824416, FY: 2019) | Assets: $5,159,107 | Sales: $7,069,004 | NetInc: $-1,308,776 | CFO: $746,523 | M-Score: 593.28 | F-Score: 0.5 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. CORMEDIX INC. (CIK: 0001410098, FY: 2024) | Assets: $118,845,673 | Sales: $43,472,170 | NetInc: $-17,930,020 | CFO: $-38,409,480 | M-Score: 591.08 | F-Score: 0.5 | TariffRisk: 0.01 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION
3. ZRCN INC. (CIK: 0001901297, FY: 2024) | Assets: $27,614,106 | Sales: $31,519,187 | NetInc: $nan | CFO: $1,183,344 | M-Score: 582.24 | F-Score: 1.21 | TariffRisk: 0.89 | Flag: ELEVATED: DECHOW MISSTATEMENT RISK
4. Quest Resource Holding Corporation (CIK: 0001442236, FY: 2013) | Assets: $100,646,543 | Sales: $67,504,540 | NetInc: $-17,799,351 | CFO: $-3,820,068 | M-Score: 580.27 | F-Score: 0.52 | TariffRisk: 0.0 | Flag: ELEVATED: BENEISH OUTLIER
5. BOOMER HOLDINGS, INC. (CIK: 0001678746, FY: 2020) | Assets: $12,375,741 | Sales: $11,472,571 | NetInc: $-594,755 | CFO: $-473,805 | M-Score: 563.96 | F-Score: 0.56 | TariffRisk: 1.07 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0012",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "QUEST PATENT RESEARCH CORPORATION",
      "identifier": "CIK: 0000824416, FY: 2019",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly; 19 U.S.C. § 1313 and UCC § 2-305(2)/§ 2-717 only if CBP Form 7501 and supplier surcharge invoices are verified - TariffRisk 1.0 uncorroborated by filings data provided",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 593.28 is mathematically implausible under normal Beneish inputs and signals corrupted or extreme input variables. Sloan = (-1308776 - 746523) / 5159107 = -0.3984, absolute value > 0.10, severe negative accrual divergence. Do not assert manipulation or tariff recovery without re-extracting audited 10-K DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA.",
      "estimated_claim_or_surcharge_usd": 353450,
      "z3_smt_invariant": "FAIL/UNVERIFIED: Assert NetIncome == CFO + Accruals; Accruals = -2055299; Sloan -0.3984 breaches |0.10| invariant; M-Score 593.28 >> -1.78; balance-sheet identity must be re-verified from source 10-K before any deduction.",
      "actionable_memo": "MF-02/MF-09: Re-pull FY2019 10-K, recompute all 8 Beneish variables from primary statements, reconcile Assets=Liabilities+Equity. MF-05/MF-06: Tariff estimate is illustrative ceiling only: 7069004 x 1.0 x 5% = 353450. Require CBP 7501, vendor AP master, and 3%-8% surcharge invoices before any UCC § 2-717 credit memo; no withholding on current data alone."
    },
    {
      "index": 2,
      "entity_name": "CORMEDIX INC.",
      "identifier": "CIK: 0001410098, FY: 2024",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly; Dechow F-Score 0.5 below 1.0 threshold; TariffRisk 0.01 de minimis - no viable 19 U.S.C. § 1313 / UCC § 2-717 tariff hook on provided data",
      "forensic_verdict": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION FLAG REQUIRES CAUTION - M-Score 591.08 is an extreme outlier indicating likely input/data error, not literal proof of manipulation. Sloan = (-17930020 - (-38409480)) / 118845673 = 0.1723 > 0.10, positive accrual flag. F-Score 0.5 does not corroborate Dechow misstatement risk.",
      "estimated_claim_or_surcharge_usd": 21736,
      "z3_smt_invariant": "FAIL: Sloan 0.1723 > 0.10 invariant breached; NetIncome - CFO = 20479460 accrual gap unexplained; M-Score 591.08 >> -1.78 while F-Score 0.5 < 1.0 creates model conflict requiring SAT check on source inputs.",
      "actionable_memo": "MF-02/MF-09: Recompute Beneish and Sloan from audited FY2024 10-K, inspect receivables, soft assets, issuance and RSST accruals. Tariff ceiling illustrative only: 43472170 x 0.01 x 5% = 21736, below MF-05 $50000 threshold - close tariff lane absent CBP 7501 evidence. No AP deduction authorized on model scores alone."
    },
    {
      "index": 3,
      "entity_name": "ZRCN INC.",
      "identifier": "CIK: 0001901297, FY: 2024",
      "statutory_hook": "Dechow F-Score 1.21 > 1.0 misstatement-risk threshold; Beneish M-Score > -1.78; potential UCC § 2-305(2)/§ 2-717 and 19 U.S.C. § 1313 review only with verified import/surcharge records - TariffRisk 0.89",
      "forensic_verdict": "ELEVATED: DECHOW MISSTATEMENT RISK - UNDETERMINED ON EARNINGS. NetInc is NaN, so Sloan, TATA and NetIncome=CFO+Accruals cannot be verified. M-Score 582.24 is implausible as a literal Beneish result and indicates corrupted inputs. F-Score 1.21 alone does not prove misstatement.",
      "estimated_claim_or_surcharge_usd": 1402604,
      "z3_smt_invariant": "UNSAT/UNKNOWN: NetIncome = NaN violates deterministic verification MF-09; invariant NetIncome == CFO + Accruals cannot be evaluated with CFO 1183344; Sloan undefined; data extraction must be corrected before any verdict.",
      "actionable_memo": "MF-02/MF-09: Halt scoring, re-extract NetInc, total assets (average), receivables, inventory and accruals from FY2024 SEC filing; correct NaN source field. Tariff ceiling illustrative only: 31519187 x 0.89 x 5% = 1402604. Require CBP 7501, drawback/reliquidation status and supplier surcharge proof before pursuing any § 2-717 deduction."
    },
    {
      "index": 4,
      "entity_name": "Quest Resource Holding Corporation",
      "identifier": "CIK: 0001442236, FY: 2013",
      "statutory_hook": "Beneish M-Score > -1.78 and Sloan Accrual Anomaly; Dechow F-Score 0.52 below 1.0; TariffRisk 0.0 - no 19 U.S.C. § 1313 or UCC § 2-717 tariff surcharge hook on provided data",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 580.27 is far beyond plausible Beneish range and signals extreme or erroneous inputs, not standalone proof of manipulation. Sloan = (-17799351 - (-3820068)) / 100646543 = -0.1389, absolute value > 0.10, severe negative accrual divergence. F-Score 0.52 does not corroborate Dechow risk.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "FAIL: Sloan -0.1389 breaches |0.10| invariant; Accruals = NetIncome - CFO = -13979283; M-Score 580.27 >> -1.78 with F-Score 0.52 < 1.0 = cross-model inconsistency requiring source-data re-verification.",
      "actionable_memo": "MF-02/MF-09: Re-pull FY2013 10-K, recompute Beneish variables and average assets, investigate large loss vs CFO gap and any impairments/restructuring non-cash items explaining negative accruals. Estimated tariff claim 0 due TariffRisk 0.0. No credit memo or AP withholding on forensic scores alone."
    },
    {
      "index": 5,
      "entity_name": "BOOMER HOLDINGS, INC.",
      "identifier": "CIK: 0001678746, FY: 2020",
      "statutory_hook": "Beneish M-Score > -1.78; 19 U.S.C. § 1313 and UCC § 2-305(2)/§ 2-717 only if verified - TariffRisk 1.07 exceeds valid 0-1 range and is itself a data-integrity flag",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / DATA ANOMALY - M-Score 563.96 is implausible as literal Beneish output. Sloan = (-594755 - (-473805)) / 12375741 = -0.0098, within 0.10 threshold and does not corroborate accrual manipulation. F-Score 0.56 < 1.0. TariffRisk 1.07 invalid as a probability/ratio.",
      "estimated_claim_or_surcharge_usd": 573629,
      "z3_smt_invariant": "FAIL ON INPUT DOMAIN, PASS ON SLOAN: TariffRisk 1.07 > 1.0 violates bounded-input invariant; Sloan -0.0098 satisfies |Sloan| <= 0.10; M-Score 563.96 >> -1.78 conflicts with Sloan/F-Score and requires re-extraction; NetIncome - CFO = -120950.",
      "actionable_memo": "MF-02/MF-09: Re-verify FY2020 balance sheet identity Assets=Liabilities+Equity and all Beneish inputs from source filing; cap/correct TariffRisk. Tariff ceiling illustrative only using capped risk 1.0: 11472571 x 1.0 x 5% = 573629. Require CBP 7501, AP vendor records and explicit surcharge invoices before any UCC § 2-717 deduction; do not rely on cited precedent without independent legal verification."
    }
  ]
}
