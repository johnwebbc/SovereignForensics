# SovereignForensics // Batch SEC Audit 0032
**Model:** `muse-wonder-1.0` | **Tokens:** 1734 (Cached: 1140) in / 2171 out | **Cost:** $0.0460

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0032 (5 REAL SEC FILERS):
1. Keros Therapeutics, Inc. (CIK: 0001664710, FY: 2024) | Assets: $615,886,000 | Sales: $3,550,000 | NetInc: $-104,679,000 | CFO: $-70,062,000 | M-Score: 95.74 | F-Score: 0.32 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. SCYNEXIS, Inc. (CIK: 0001178253, FY: 2021) | Assets: $119,837,000 | Sales: $13,163,000 | NetInc: $-32,866,000 | CFO: $-49,354,000 | M-Score: 95.22 | F-Score: 0.3 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. MJ Holdings, Inc. (CIK: 0001456857, FY: 2019) | Assets: $8,175,755 | Sales: $897,696 | NetInc: $-5,007,928 | CFO: $-4,622,155 | M-Score: 95.1 | F-Score: 0.38 | TariffRisk: 0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. The OLB Group, Inc. (CIK: 0001314196, FY: 2018) | Assets: $11,999,274 | Sales: $9,019,876 | NetInc: $-662,297 | CFO: $-54,660 | M-Score: 93.73 | F-Score: 0.0 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. AgEagle Aerial Systems Inc. (CIK: 0000008504, FY: 2019) | Assets: $6,808,151 | Sales: $296,677 | NetInc: $-2,079,683 | CFO: $-1,778,138 | M-Score: 90.8 | F-Score: 0.23 | TariffRisk: 0.32 | Flag: ELEVATED: BENEISH OUTLIER

## Meta Model Deliberation:
{
  "batch_id": "SEC_0032",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "Keros Therapeutics, Inc.",
      "identifier": "CIK: 0001664710, FY: 2024",
      "statutory_hook": "No verified UCC § 2-717 / UCC § 2-305(2) or 19 U.S.C. § 1313 hook: no CBP Form 7501, import AP vendor, or 3%-8% tariff surcharge evidence in provided record; TariffRisk 1.0 unverified against $3,550,000 sales",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER NOT CORROBORATED - M-Score 95.74 >> -1.78 is mathematically implausible for standard Beneish 8-variable model and indicates input/balance-sheet distortion, not proof of manipulation. F-Score 0.32 < 1.0 low Dechow misstatement risk. Sloan Accrual = (-104,679,000 - (-70,062,000))/615,886,000 = -0.0562, not > 0.10, no severe positive accrual anomaly.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -104679000 = -70062000 + (-34617000); Sloan=-0.0562 <= 0.10; M-Score 95.74 flagged UNRELIABLE_INPUT, F-Score 0.32 < 1.0",
      "actionable_memo": "MF-02/MF-05/MF-06 FAIL for recovery: Do not deduct under UCC § 2-717. Pull FY2024 10-K, receivables, gross margin, depreciation and AP vendor master to recompute DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA from source. No $50,000+ verifiable tariff claim established; claim = $0 pending CBP 7501 evidence."
    },
    {
      "index": 2,
      "entity_name": "SCYNEXIS, Inc.",
      "identifier": "CIK: 0001178253, FY: 2021",
      "statutory_hook": "No verified UCC § 2-717 / UCC § 2-305(2) or 19 U.S.C. § 1313 hook: no CBP Form 7501, exported/destroyed merchandise, or supplier tariff surcharge pass-through evidence in provided record despite TariffRisk 1.0",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / SLOAN FLAG - M-Score 95.22 >> -1.78 is implausible and unreliable as computed. F-Score 0.30 < 1.0 low Dechow risk, contradicting Beneish. Sloan Accrual = (-32,866,000 - (-49,354,000))/119,837,000 = 0.1376 > 0.10, flags severe cash-to-accrual divergence requiring source verification, not a tariff recovery.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT arithmetically: NetIncome = CFO + Accruals => -32866000 = -49354000 + 16488000; Sloan=0.1376 > 0.10 VIOLATES accrual-quality invariant; M-Score input invariant UNSAT/UNRELIABLE",
      "actionable_memo": "MF-02/MF-09 FAIL: Halt any UCC § 2-717 withholding. Reconcile FY2021 10-K balance sheet, RSST accruals, ChgRec, ChgInv and SoftAssets from SEC source to explain positive $16,488,000 accrual gap and balance-sheet imbalance. No verifiable drawback or surcharge; claim = $0 pending documentary proof."
    },
    {
      "index": 3,
      "entity_name": "MJ Holdings, Inc.",
      "identifier": "CIK: 0001456857, FY: 2019",
      "statutory_hook": "No verified UCC § 2-717 / UCC § 2-305(2) or 19 U.S.C. § 1313 hook: TariffRisk 0.01 de minimis, no CBP Form 7501, import goods AP, or tariff surcharge evidence in provided record",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE NOT CORROBORATED - M-Score 95.10 >> -1.78 is implausible for standard Beneish model and indicates corrupted inputs. F-Score 0.38 < 1.0 low Dechow misstatement risk. Sloan Accrual = (-5,007,928 - (-4,622,155))/8,175,755 = -0.0472, not > 0.10, no severe positive accrual anomaly.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -5007928 = -4622155 + (-385773); Sloan=-0.0472 <= 0.10; M-Score 95.10 flagged UNRELIABLE_INPUT, F-Score 0.38 < 1.0",
      "actionable_memo": "MF-02/MF-05 FAIL: Do not pursue credit-memo deduction. Assets $8,175,755 and sales $897,696 with TariffRisk 0.01 cannot support a verified $50,000+ tariff claim on this record. Rebuild Beneish variables from FY2019 10-K and verify balance-sheet identity Assets = Liabilities + Equity before any forensic conclusion; claim = $0."
    },
    {
      "index": 4,
      "entity_name": "The OLB Group, Inc.",
      "identifier": "CIK: 0001314196, FY: 2018",
      "statutory_hook": "No verified UCC § 2-717 / UCC § 2-305(2) or 19 U.S.C. § 1313 hook: no CBP Form 7501, goods supplier AP record, or unilateral tariff surcharge evidence in provided record despite TariffRisk 1.0; payment-services revenue not shown as imported goods",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE NOT CORROBORATED - M-Score 93.73 >> -1.78 is implausible and unreliable as computed. F-Score 0.0 < 1.0 indicates no Dechow misstatement signal, contradicting Beneish. Sloan Accrual = (-662,297
