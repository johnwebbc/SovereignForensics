# SovereignForensics // Batch SEC Audit 0004
**Model:** `muse-wonder-1.0` | **Tokens:** 1734 (Cached: 1140) in / 2202 out | **Cost:** $0.0466

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0004 (5 REAL SEC FILERS):
1. VirnetX Holding Corporation (CIK: 0001082324, FY: 2020) | Assets: $234,793,000 | Sales: $302,636,000 | NetInc: $280,429,000 | CFO: $281,389,000 | M-Score: 3171.99 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
2. Gyre Therapeutics, Inc. (CIK: 0001124105, FY: 2020) | Assets: $98,554,000 | Sales: $20,948,000 | NetInc: $-55,178,000 | CFO: $-43,613,000 | M-Score: 3111.41 | F-Score: 0.22 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
3. Datacentrex, Inc. (CIK: 0001853825, FY: 2025) | Assets: $66,841,910 | Sales: $6,963,477 | NetInc: $-8,502,885 | CFO: $-6,447,474 | M-Score: 3029.91 | F-Score: 0.27 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
4. ROKWADER, INC. (CIK: 0001322952, FY: 2016) | Assets: $16,036,382 | Sales: $5,201,542 | NetInc: $-471,406 | CFO: $527,485 | M-Score: 2001.72 | F-Score: 0.34 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
5. Swisher Hygiene Inc. (CIK: 0001504747, FY: 2015) | Assets: $113,199,000 | Sales: $0 | NetInc: $-46,808,000 | CFO: $-8,453,000 | M-Score: 1974.26 | F-Score: 0.19 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "SEC_0004",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "VirnetX Holding Corporation",
      "identifier": "CIK: 0001082324, FY: 2020",
      "statutory_hook": "No verifiable UCC § 2-717 / § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim on supplied record; no CBP Form 7501, AP vendor surcharge, or goods-sale evidence. Beneish and Sloan forensic review only.",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 3171.99 >> -1.78 signals extreme model outlier, but F-Score 0.19 < 1.0 and Sloan -0.0041 do not corroborate accrual manipulation. Likely distorted by extraordinary patent-litigation revenue/income, not deterministic earnings manipulation.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => 280429000 = 281389000 + (-960000); Sloan = -960000/234793000 = -0.0041 <= 0.10",
      "actionable_memo": "MF-02/MF-06: Do not execute UCC § 2-717 deduction. Obtain 10-K detail for litigation revenue, receivables and prior-year Beneish inputs to recompute DSRI/SGI/TATA; close tariff lane absent CBP 7501 or supplier surcharge invoices."
    },
    {
      "index": 2,
      "entity_name": "Gyre Therapeutics, Inc.",
      "identifier": "CIK: 0001124105, FY: 2020",
      "statutory_hook": "No verifiable UCC § 2-717 / § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim on supplied record; no CBP Form 7501 or AP surcharge evidence. Beneish and Sloan forensic review only.",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 3111.41 >> -1.78, but F-Score 0.22 < 1.0 and Sloan -0.1173 < 0.10. Net loss exceeds CFO loss; extreme M-Score requires prior-period input verification and is not corroborated as cash-to-accrual manipulation.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -55178000 = -43613000 + (-11565000); Sloan = -11565000/98554000 = -0.1173 <= 0.10",
      "actionable_memo": "MF-02/MF-09: Halt any credit-memo action. Reconcile balance-sheet imbalance, prior-year assets/receivables and non-cash charges from 10-K; recompute Beneish variables before any manipulation conclusion. No tariff recovery without import documentation."
    },
    {
      "index": 3,
      "entity_name": "Datacentrex, Inc.",
      "identifier": "CIK: 0001853825, FY: 2025",
      "statutory_hook": "No verifiable UCC § 2-717 / § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim on supplied record; TariffRisk 1.0 alone is insufficient without CBP Form 7501 or supplier AP surcharge records.",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 3029.91 >> -1.78 signals extreme model outlier, but F-Score 0.27 < 1.0 and Sloan -0.0307 do not corroborate severe accrual manipulation. Loss-making profile likely distorts SGI/GMI/DSRI inputs.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -8502885 = -6447474 + (-2055411); Sloan = -2055411/66841910 = -0.0307 <= 0.10",
      "actionable_memo": "MF-02/MF-05: No deductible claim quantified; $0 pending evidence. Pull FY2025 10-K and prior-year comparatives, verify receivables, margins and asset quality, and request any tariff surcharge invoices before reconsidering UCC § 2-717."
    },
    {
      "index": 4,
      "entity_name": "ROKWADER, INC.",
      "identifier": "CIK: 0001322952, FY: 2016",
      "statutory_hook": "No verifiable UCC § 2-717 / § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim on supplied record; no CBP Form 7501, import, or AP surcharge documentation provided.",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 2001.72 >> -1.78 signals extreme model outlier, but F-Score 0.34 < 1.0 and Sloan -0.0623, with positive CFO despite net loss, do not corroborate Sloan accrual manipulation. Prior-period Beneish inputs require verification.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -471406 = 527485 + (-998891); Sloan = -998891/16036382 = -0.0623 <= 0.10",
      "actionable_memo": "MF-02/MF-09: Do not withhold AP amounts. Obtain FY2015-FY2016 filings to recompute DSRI, GMI, AQI, SGI and TATA, investigate non-cash reconciling items, and close tariff lane absent documented surcharges."
    },
    {
      "index": 5,
      "entity_name": "Swisher Hygiene Inc.",
      "identifier": "CIK: 0001504747, FY: 2015",
      "statutory_hook": "No verifiable UCC § 2-717 / § 2-305(2) tariff surcharge or 19 U.S.C. § 1313 drawback claim on supplied record; Sales $0 precludes a current-period surcharge pass-through calculation without CBP Form 7501 or AP records.",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 1974.26 >> -1.78 with Sales $0 makes SGI/DSRI/GMI mathematically unstable. F-Score 0.19 < 1.0 and Sloan -0.3388 reflect large non-cash losses/impairments, not corroborated positive accrual manipulation.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: NetIncome = CFO + Accruals => -46808000 = -8453000 + (-38355000); Sloan = -38355000/113199000 = -0.3388 <= 0.10",
      "actionable_memo": "MF
