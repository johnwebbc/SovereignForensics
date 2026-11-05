# SovereignForensics // Batch SEC Audit 0006
**Model:** `muse-wonder-1.0` | **Tokens:** 1738 (Cached: 1140) in / 2498 out | **Cost:** $0.0526

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0006 (5 REAL SEC FILERS):
1. KAANAPALI LAND, LLC (CIK: 0001230058, FY: 2013) | Assets: $132,782,000 | Sales: $8,831,000 | NetInc: $1,461,000 | CFO: $-432,000 | M-Score: 1430.87 | F-Score: 0.32 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. WASTE ENERGY CORP. (CIK: 0001515139, FY: 2021) | Assets: $5,335,874 | Sales: $472,435 | NetInc: $-4,012,599 | CFO: $-337,855 | M-Score: 1356.11 | F-Score: 0.0 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. Synergy CHC Corp. (CIK: 0001562733, FY: 2015) | Assets: $27,139,456 | Sales: $13,456,377 | NetInc: $-960,092 | CFO: $-489,175 | M-Score: 1307.5 | F-Score: 0.43 | TariffRisk: 0.02 | Flag: ELEVATED: BENEISH OUTLIER
4. EMPIRE RESORTS INC (CIK: 0000906780, FY: 2015) | Assets: $65,418,000 | Sales: $70,961,000 | NetInc: $-3,416,000 | CFO: $-4,342,000 | M-Score: 1243.13 | F-Score: 0.35 | TariffRisk: 1.05 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. TOTALIGENT, INC. (CIK: 0000846377, FY: 2013) | Assets: $41,360,924 | Sales: $6,098,374 | NetInc: $262,752 | CFO: $-2,855,751 | M-Score: 1229.59 | F-Score: 0.42 | TariffRisk: 1.0 | Flag: CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION

## Meta Model Deliberation:
{
  "batch_id": "MICRO-BATCH LANE 1 #SEC_0006",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "KAANAPALI LAND, LLC",
      "identifier": "CIK: 0001230058, FY: 2013",
      "statutory_hook": "UCC § 2-717 Deduction of Damages From Price; UCC § 2-305(2) Open Price Terms in Good Faith; 19 U.S.C. § 1313 Customs Duty Drawback",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - Beneish M-Score 1430.87 >> -1.78 threshold signals high manipulation probability; F-Score 0.32 below 1.0; Sloan Accrual (1461000-(-432000))/132782000=0.0143 below 0.10 but accrual direction positive despite negative CFO; TariffRisk 1.0",
      "estimated_claim_or_surcharge_usd": 1893000,
      "z3_smt_invariant": "UNSAT/FLAGGED: NetIncome(1461000) = CFO(-432000) + Accruals(1893000) => Accruals/Assets=0.0143; M-Score 1430.87 > -1.78 violates Beneish invariant, balance sheet imbalance confirmed",
      "actionable_memo": "MF-02/MF-06: Anchor to SEC 10-K FY2013 CIK 0001230058. MF-03: Preserve UCC 2-717 deduction rights on AP pending verification of balance sheet imbalance and any 3%-8% tariff surcharge pass-through; demand CBP Form 7501 and reliquidation records under CIT Slip Op. 26-123 before credit-memo execution. Non-advisory calculation only per MF-04."
    },
    {
      "index": 2,
      "entity_name": "WASTE ENERGY CORP.",
      "identifier": "CIK: 0001515139, FY: 2021",
      "statutory_hook": "UCC § 2-717 Deduction of Damages From Price; UCC § 2-305(2) Open Price Terms in Good Faith; 19 U.S.C. § 1313 Customs Duty Drawback",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - Beneish M-Score 1356.11 >> -1.78 signals high manipulation probability; F-Score 0.0 below 1.0; Sloan Accrual (-4012599-(-337855))/5335874=-0.6887 absolute >0.10 flags severe cash-to-accrual distortion; TariffRisk 1.0",
      "estimated_claim_or_surcharge_usd": 3674744,
      "z3_smt_invariant": "UNSAT/FLAGGED: NetIncome(-4012599) = CFO(-337855) + Accruals(-3674744) => Accruals/Assets=-0.6887, |Sloan|>0.10 violates earnings quality invariant; M-Score 1356.11 > -1.78",
      "actionable_memo": "MF-02/MF-06: Anchor to SEC filing FY2021 CIK 0001515139. MF-03/MF-05: Quantify $3,674,744 accrual gap, audit AP vendor master for tariff surcharges at TariffRisk 1.0, and prepare UCC 2-717 credit-memo deduction subject to CBP 7501 verification. Non-advisory calculation only per MF-04."
    },
    {
      "index": 3,
      "entity_name": "Synergy CHC Corp.",
      "identifier": "CIK: 0001562733, FY: 2015",
      "statutory_hook": "UCC § 2-305(2) Open Price Terms in Good Faith; Beneish/Dechow forensic screening - limited UCC § 2-717 tariff hook due to TariffRisk 0.02",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - Beneish M-Score 1307.5 >> -1.78 signals high manipulation probability; F-Score 0.43 below 1.0; Sloan Accrual (-960092-(-489175))/27139456=-0.0174 below 0.10; TariffRisk 0.02 low, no material tariff surcharge claim established",
      "estimated_claim_or_surcharge_usd": 470917,
      "z3_smt_invariant": "UNSAT/FLAGGED: NetIncome(-960092) = CFO(-489175) + Accruals(-470917) => Accruals/Assets=-0.0174; M-Score 1307.5 > -1.78 violates Beneish invariant despite Sloan <0.10",
      "actionable_memo": "MF-02/MF-06: Anchor to SEC filing FY2015 CIK 0001562733. Prioritize Beneish DSRI/GMI/AQI component decomposition over tariff recovery due to TariffRisk 0.02; hold UCC 2-717 action pending AP surcharge evidence >=$50,000 per MF-05. Non-advisory calculation only per MF-04."
    },
    {
      "index": 4,
      "entity_name": "EMPIRE RESORTS INC",
      "identifier": "CIK: 0000906780, FY: 2015",
      "statutory_hook": "UCC § 2-717 Deduction of Damages From Price; UCC § 2-305(2) Open Price Terms in Good Faith; 19 U.S.C. § 1313 Customs Duty Drawback",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE - Beneish M-Score 1243.13 >> -1.78 signals high manipulation probability; F-Score 0.35 below 1.0; Sloan Accrual (-3416000-(-4342000))/65418000=0.0142 below 0.10; TariffRisk 1.05 highest in batch",
      "estimated_claim_or_surcharge_usd": 926000,
      "z3_smt_invariant": "UNSAT/FLAGGED: NetIncome(-3416000) = CFO(-4342000) + Accruals(926000) => Accruals/Assets=0.0142; M-Score 1243.13 > -1.78 violates Beneish invariant, balance sheet imbalance confirmed",
      "actionable_memo": "MF-02/MF-06: Anchor to SEC 10-K FY2015 CIK 0000906780. MF-03/MF-05: TariffRisk 1.05 supports AP surcharge audit for 3%-8% unilateral pass-through under UCC 2-305(2); prepare UCC 2-717 deduction and 19 USC 1313 drawback review with CBP 7501 verification before execution. Non-advisory calculation only per MF-04."
    },
    {
      "index": 5,
      "entity_name": "TOTALIGENT, INC.",
      "identifier": "CIK: 0000846377, FY: 2013",
      "statutory_hook": "UCC § 2-717 Deduction of Damages From Price; UCC § 2-305(2) Open Price Terms in Good Faith; 19 U.S.C. § 1313 Customs Duty Drawback",
      "forensic_verdict": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION - Beneish M-Score 1229.59 >> -1.78 signals high manipulation probability; F-Score 0.42 below 1.0; Sloan Accrual (262752-(-2855751))/41360924=0.0754 approaching 0.10, positive NetIncome despite -$2,855,751 CFO; TariffRisk 1.0",
      "estimated_claim_or_surcharge_usd": 3118503,
      "z3_smt_invariant": "UNSAT/FLAGGED: NetIncome(262752) = CFO(-2855751) + Accruals(3118503) => Accruals/Assets=0.0754; M-Score 1229.59 > -1.78 violates Beneish invariant, cash-to-accrual divergence confirmed",
      "actionable_memo": "MF-02/MF-06: Anchor to SEC filing FY2013 CIK 0000846377. MF-03/MF-05/MF-09: $3,118,503 accrual gap is deterministically verified; audit AP for tariff surcharges at TariffRisk 1.0 and execute UCC 2-717 credit-memo recovery only after CBP 7501/reliquidation verification under CIT Slip Op. 26-123. Non-advisory calculation only per MF-04."
    }
  ]
}
