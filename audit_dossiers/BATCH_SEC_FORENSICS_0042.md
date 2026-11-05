# SovereignForensics // Batch SEC Audit 0042
**Model:** `muse-wonder-1.0` | **Tokens:** 1733 (Cached: 1140) in / 2513 out | **Cost:** $0.0529

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0042 (5 REAL SEC FILERS):
1. KAOPU GROUP INC (CIK: 0001602706, FY: 2016) | Assets: $11,519,781 | Sales: $7,986,658 | NetInc: $-191,304 | CFO: $nan | M-Score: 62.87 | F-Score: 0.23 | TariffRisk: 3.2 | Flag: ELEVATED: BENEISH OUTLIER
2. Siga Technologies INC (CIK: 0001010086, FY: 2021) | Assets: $214,726,575 | Sales: $133,670,454 | NetInc: $69,450,766 | CFO: $71,519,228 | M-Score: 61.21 | F-Score: 0.48 | TariffRisk: 3.26 | Flag: ELEVATED: IEEPA/SEC 301 TARIFF SURCHARGE DISTORTION
3. GLOBAL CLEAN ENERGY HOLDINGS, INC. (CIK: 0000748790, FY: 2020) | Assets: $206,077,922 | Sales: $nan | NetInc: $-10,550,175 | CFO: $-2,447,717 | M-Score: 60.96 | F-Score: 0.33 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
4. ASTROTECH Corp (CIK: 0001001907, FY: 2015) | Assets: $44,218,000 | Sales: $513,000 | NetInc: $10,778,000 | CFO: $-552,000 | M-Score: 60.51 | F-Score: 0.15 | TariffRisk: 2.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. Myomo, Inc. (CIK: 0001369290, FY: 2022) | Assets: $20,095,412 | Sales: $1,000,000,000 | NetInc: $-10,372,329 | CFO: $-9,547,695 | M-Score: 60.38 | F-Score: 0.22 | TariffRisk: 0.02 | Flag: ELEVATED: BENEISH OUTLIER

## Meta Model Deliberation:
{
  "batch_id": "SEC_0042",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "KAOPU GROUP INC",
      "identifier": "CIK: 0001602706, FY: 2016",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; UCC 2-305(2) Good Faith Open Price Terms; UCC 2-717 Deduction of Damages From Price contingent on verified AP surcharge",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 62.87 >> -1.78 signals high manipulation probability; F-Score 0.23 < 1.0 low Dechow misstatement; Sloan Accrual Anomaly indeterminate due to CFO=$nan, deterministic verification fails. No verified tariff claim without CBP Form 7501/AP records.",
      "estimated_claim_or_surcharge_usd": 255573,
      "z3_smt_invariant": "UNSAT/UNVERIFIABLE: CFO=NaN => assert NetIncome(-191304) == CFO + Accruals cannot be satisfied; MF-09 Deterministic Verification FAILED",
      "actionable_memo": "MF-02/MF-06: Pull SEC 10-K FY2016 cash flow statement to replace NaN CFO, recompute DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA and Sloan. Hold UCC 2-717 deduction pending verified supplier tariff invoices; indicative exposure 3.2% x Sales $7,986,658 = $255,573, not self-enforcing until documented."
    },
    {
      "index": 2,
      "entity_name": "Siga Technologies INC",
      "identifier": "CIK: 0001010086, FY: 2021",
      "statutory_hook": "Beneish M-Score > -1.78; UCC 2-305(2) IEEPA/Section 301 Tariff Surcharge Good Faith; UCC 2-717; 19 U.S.C. 1313 Duty Drawback if CBP refunds not passed through",
      "forensic_verdict": "ELEVATED: IEEPA/SEC 301 TARIFF SURCHARGE DISTORTION - M-Score 61.21 >> -1.78 outlier, but F-Score 0.48 < 1.0 and Sloan -0.0096 does not flag accrual manipulation; Beneish inputs likely distorted by sales/receivables volatility, requires component-level review.",
      "estimated_claim_or_surcharge_usd": 4357657,
      "z3_smt_invariant": "SAT: NetIncome(69450766) == CFO(71519228) + Accruals(-2068462); Sloan=(69450766-71519228)/214726575=-0.0096 <= 0.10 PASS",
      "actionable_memo": "MF-02/MF-05/MF-07: Verify TariffRisk 3.26% x Sales $133,670,454 = $4,357,657 against CBP Form 7501, supplier AP master and surcharge invoices. If importer retained CBP refunds, issue UCC 2-717 credit-memo deduction notice; do not book recovery on M-Score alone, decompose Beneish variables from 10-K."
    },
    {
      "index": 3,
      "entity_name": "GLOBAL CLEAN ENERGY HOLDINGS, INC.",
      "identifier": "CIK: 0000748790, FY: 2020",
      "statutory_hook": "Beneish M-Score > -1.78; Sloan Accrual Anomaly; UCC 2-717 inapplicable without verified sales/AP surcharge; MF-09 Deterministic Verification",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / DATA INTEGRITY - M-Score 60.96 >> -1.78 outlier, F-Score 0.33 < 1.0, Sales=$nan prevents DSRI/SGI and tariff exposure calculation; Sloan -0.0393 not severe. Forensic models unreliable until sales verified.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/UNVERIFIABLE for revenue invariants: Sales=NaN => DSRI/SGI undefined; SAT for cash: NetIncome(-10550175) == CFO(-2447717) + Accruals(-8102458); Sloan=-0.0393 <= 0.10",
      "actionable_memo": "MF-02/MF-09: Reject claim quantification at $0 under MF-05 until FY2020 10-K sales, receivables and AP vendor master are sourced. Recompute Beneish/Dechow after correcting NaN; TariffRisk 1.0 cannot be applied to unknown sales base. No UCC 2-717 withholding authorized on this record."
    },
    {
      "index": 4,
      "entity_name": "ASTROTECH Corp",
      "identifier": "CIK: 0001001907, FY: 2015",
      "statutory_hook": "Sloan Accrual Anomaly > 0.10; Beneish M-Score > -1.78; UCC 2-717 contingent on verified AP surcharge only",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / SEVERE ACCRUAL ANOMALY - NetInc $10,778,000 vs CFO -$552,000 on Sales $513,000 indicates non-operating/discontinued gain or classification imbalance; M-Score 60.51 >> -1.78, F-Score 0.15 < 1.0, Sloan 0.2562 > 0.10 flags severe cash-to-accrual divergence.",
      "estimated_claim_or_surcharge_usd": 10260,
      "z3_smt_invariant": "SAT arithmetically but VIOLATES Sloan invariant: NetIncome(10778000) == CFO(-552000) + Accruals(11330000); Sloan=11330000/44218000=0.2562 > 0.10 FAIL",
      "actionable_memo": "MF-02/MF-05: Investigate FY2015 10-K for discontinued operations/asset sale driving NetInc >> Sales. Indicative tariff exposure 2.0% x $513,000 = $10,260 below $50,000 MF-05 threshold - deprioritize tariff recovery, focus on accrual classification and non-recurring gain disclosure. No UCC 2-717 deduction on earnings flag alone."
    },
    {
      "index": 5,
      "entity_name": "Myomo, Inc.",
      "identifier": "CIK: 0001369290, FY: 2022",
      "statutory_hook": "Beneish M-Score > -1.78; UCC 2-305(2) Good Faith; UCC 2-717 contingent on verified AP surcharge; MF-02 Public Record Verifiability",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER WITH SALES DATA ANOMALY - M-Score 60.38 >> -1.78, F-Score 0.22 < 1.0, Sloan -0.0410 not severe; Sales $1,000,000,000 vs Assets $20,095,412 is implausible/rounded placeholder and invalidates SGI/DSRI and tariff base until verified in 10-K.",
      "estimated_claim_or_surcharge_usd": 200000,
      "z3_smt_invariant": "SAT for cash: NetIncome(-10372329) == CFO(-9547695) + Accruals(-824634); Sloan=-824634/20095412=-0.0410 <= 0.10 PASS; Sales/Assets=49.76 VIOLATES plausibility invariant",
      "actionable_memo": "MF-02/MF-09: Correct FY2022 sales from SEC 10-K before any claim; unverified indicative 0.02% x $1,000,000,000 = $200,000 must not be relied upon. Recompute Beneish components, verify AP/tariff invoices and CBP records; only then assess UCC 2-717 credit memo, otherwise classify as data-quality outlier not recoverable surcharge."
    }
  ]
}
