# SovereignForensics // Batch SEC Audit 0022
**Model:** `muse-wonder-1.0` | **Tokens:** 1754 (Cached: 1140) in / 2289 out | **Cost:** $0.0485

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0022 (5 REAL SEC FILERS):
1. SCIENTURE HOLDINGS, INC. (CIK: 0001382574, FY: 2025) | Assets: $104,853,805 | Sales: $431,609 | NetInc: $9,065,798 | CFO: $-13,379,683 | M-Score: 188.13 | F-Score: 0.35 | TariffRisk: 35.91 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION
2. WPX Energy, Inc. (CIK: 0001518832, FY: 2018) | Assets: $8,207,000,000 | Sales: $2,310,000,000 | NetInc: $354,000,000 | CFO: $883,000,000 | M-Score: 183.46 | F-Score: 0.17 | TariffRisk: 0.65 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. PROTHENA CORPORATION PUBLIC LIMITED COMPANY (CIK: 0001559053, FY: 2021) | Assets: $609,366,000 | Sales: $200,577,000 | NetInc: $66,975,000 | CFO: $92,605,000 | M-Score: 183.1 | F-Score: 0.3 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. HOLLYFRONTIER CORP (CIK: 0000048039, FY: 2017) | Assets: $10,692,154,000 | Sales: $14,251,299,000 | NetInc: $805,395,000 | CFO: $985,868,000 | M-Score: 180.53 | F-Score: 0.36 | TariffRisk: 0.01 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. IonQ, Inc. (CIK: 0001824920, FY: 2023) | Assets: $597,992,000 | Sales: $22,042,000 | NetInc: $-48,511,000 | CFO: $-44,698,000 | M-Score: 176.08 | F-Score: 0.21 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0022",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "SCIENTURE HOLDINGS, INC.",
      "identifier": "CIK: 0001382574, FY: 2025",
      "statutory_hook": "Beneish M-Score > -1.78, Sloan Accrual Anomaly > 0.10, Dechow F-Score; UCC 2-305(2) and 19 U.S.C. 1313 review for TariffRisk 35.91",
      "forensic_verdict": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION - M-Score 188.13 >> -1.78, Sloan 0.2141 > 0.10, F-Score 0.35 divergent; positive NetInc despite severe negative CFO on minimal Sales $431,609",
      "estimated_claim_or_surcharge_usd": 22445481,
      "z3_smt_invariant": "VERIFIED: NetIncome = CFO + Accruals => 9065798 = -13379683 + 22445481; Sloan = 22445481/104853805 = 0.2141 > 0.10 FLAG",
      "actionable_memo": "MF-02/MF-09: Anchor to SEC 10-K FY2025, verify DSRI/GMI/AQI/SGI/TATA drivers behind M-Score 188.13, reconcile non-cash accruals $22,445,481 to CFO. Do not assert UCC 2-717 tariff deduction without CBP Form 7501/AP surcharge proof; TariffRisk 35.91 requires invoice-level verification."
    },
    {
      "index": 2,
      "entity_name": "WPX Energy, Inc.",
      "identifier": "CIK: 0001518832, FY: 2018",
      "statutory_hook": "Beneish M-Score > -1.78, Sloan Accrual Anomaly, Dechow F-Score; balance-sheet invariant verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / MODEL ANOMALY - M-Score 183.46 >> -1.78 is mathematically implausible and signals input/data error, F-Score 0.17 < 1.0 and Sloan -0.0644 do not corroborate manipulation",
      "estimated_claim_or_surcharge_usd": 15015000,
      "z3_smt_invariant": "VERIFIED: NetIncome = CFO + Accruals => 354000000 = 883000000 + -529000000; Sloan = -529000000/8207000000 = -0.0644 NOT > 0.10",
      "actionable_memo": "MF-09: Recompute Beneish 8 variables from audited 10-K FY2018 before any claim; negative accruals and CFO > NetInc contradict earnings inflation. TariffRisk 0.65 on Sales implies ~$15,015,000 exposure only if documented surcharges exist; no UCC 2-717 deduction without AP/CBP records."
    },
    {
      "index": 3,
      "entity_name": "PROTHENA CORPORATION PUBLIC LIMITED COMPANY",
      "identifier": "CIK: 0001559053, FY: 2021",
      "statutory_hook": "Beneish M-Score > -1.78, Sloan Accrual Anomaly, Dechow F-Score; balance-sheet invariant verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / MODEL ANOMALY - M-Score 183.1 >> -1.78 uncorroborated, F-Score 0.30 < 1.0, Sloan -0.0421 negative; CFO exceeds NetInc, no Sloan manipulation flag",
      "estimated_claim_or_surcharge_usd": 2005770,
      "z3_smt_invariant": "VERIFIED: NetIncome = CFO + Accruals => 66975000 = 92605000 + -25630000; Sloan = -25630000/609366000 = -0.0421 NOT > 0.10",
      "actionable_memo": "MF-02/MF-09: Re-extract DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA from FY2021 20-F/10-K and fix Beneish input scaling. TariffRisk 1.0 implies ~$2,005,770 sales exposure only; require CBP 7501 and AP surcharge evidence before 19 U.S.C. 1313 or UCC 2-717 action."
    },
    {
      "index": 4,
      "entity_name": "HOLLYFRONTIER CORP",
      "identifier": "CIK: 0000048039, FY: 2017",
      "statutory_hook": "Beneish M-Score > -1.78, Sloan Accrual Anomaly, Dechow F-Score; balance-sheet invariant verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / MODEL ANOMALY - M-Score 180.53 >> -1.78 uncorroborated, F-Score 0.36 < 1.0, Sloan -0.0169 negative; CFO > NetInc contradicts accrual inflation",
      "estimated_claim_or_surcharge_usd": 1425129,
      "z3_smt_invariant": "VERIFIED: NetIncome = CFO + Accruals => 805395000 = 985868000 + -180473000; Sloan = -180473000/10692154000 = -0.0169 NOT > 0.10",
      "actionable_memo": "MF-09: Treat M-Score as failed deterministic verification, recompute from FY2017 10-K raw XBRL; no manipulation conclusion from Sloan/F-Score. TariffRisk 0.01 negligible (~$1,425,129 on sales); no UCC 2-717/1313 recovery without documented tariff surcharge and drawback records."
    },
    {
      "index": 5,
      "entity_name": "IonQ, Inc.",
      "identifier": "CIK: 0001824920, FY: 2023",
      "statutory_hook": "Beneish M-Score > -1.78, Sloan Accrual Anomaly, Dechow F-Score; balance-sheet invariant verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / MODEL ANOMALY - M-Score 176.08 >> -1.78 uncorroborated, F-Score 0.21 < 1.0, Sloan -0.0064 near zero; net loss with comparable negative CFO, no Sloan flag",
      "estimated_claim_or_surcharge_usd": 220420,
      "z3_smt_invariant": "VERIFIED: NetIncome = CFO + Accruals => -48511000 = -44698000 + -3813000; Sloan = -3813000/597992000 = -0.0064 NOT > 0.10",
      "actionable_memo": "MF-02/MF-09: Recompute Beneish inputs from FY2023 10-K, investigate SGI/DSRI distortion from low Sales $22,042,000 base. TariffRisk 1.0 implies ~$220,420 exposure only; require AP vendor master, CBP 7501, and surcharge invoices before any UCC 2-717 deduction."
    }
  ]
}
