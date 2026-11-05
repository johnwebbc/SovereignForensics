# SovereignForensics // Batch SEC Audit 0011
**Model:** `muse-wonder-1.0` | **Tokens:** 1739 (Cached: 1140) in / 2513 out | **Cost:** $0.0529

## Filers Screened:
MICRO-BATCH LANE 1 #SEC_0011 (5 REAL SEC FILERS):
1. Fisker Inc./DE (CIK: 0001720990, FY: 2023) | Assets: $1,831,687,000 | Sales: $272,883,000 | NetInc: $-471,341,000 | CFO: $-301,270,000 | M-Score: 703.12 | F-Score: 0.14 | TariffRisk: -0.22 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
2. SUMMER ENERGY HOLDINGS INC (CIK: 0001396633, FY: 2017) | Assets: $33,586,600 | Sales: $117,683,175 | NetInc: $1,266,608 | CFO: $-861,401 | M-Score: 656.29 | F-Score: 0.55 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
3. FREEDOM HOLDING CORP. (CIK: 0000924805, FY: 2018) | Assets: $330,086,000 | Sales: $55,224,000 | NetInc: $19,233,000 | CFO: $nan | M-Score: 639.18 | F-Score: 0.36 | TariffRisk: 1.0 | Flag: ELEVATED: BENEISH OUTLIER
4. CRAWFORD UNITED CORPORATION (CIK: 0000047307, FY: 2016) | Assets: $15,434,755 | Sales: $6,645,780 | NetInc: $5,152,576 | CFO: $2,513,886 | M-Score: 607.0 | F-Score: 0.37 | TariffRisk: 1.67 | Flag: CRITICAL: BALANCE SHEET IMBALANCE
5. CRISPR THERAPEUTICS AG (CIK: 0001674416, FY: 2023) | Assets: $2,243,057,000 | Sales: $914,963,000 | NetInc: $377,661,000 | CFO: $538,972,000 | M-Score: 600.05 | F-Score: 0.2 | TariffRisk: 1.0 | Flag: CRITICAL: BALANCE SHEET IMBALANCE

## Meta Model Deliberation:
{
  "batch_id": "MICRO-BATCH LANE 1 #SEC_0011",
  "targets_count": 5,
  "results": [
    {
      "index": 1,
      "entity_name": "Fisker Inc./DE",
      "identifier": "CIK: 0001720990, FY: 2023",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; MF-02/MF-09 Deterministic Verification - No UCC 2-717 tariff claim established on TariffRisk -0.22",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / BENEISH OUTLIER - M-Score 703.12 >> -1.78 signals high manipulation probability, likely distorted by extreme DSRI/SGI/AQI inputs. F-Score 0.14 < 1.0 does not corroborate Dechow misstatement. Sloan = (-471341000 - (-301270000))/1831687000 = -0.0929, negative accruals, below +0.10 severe threshold. Do not assert fraud without 10-K balance-sheet reconciliation.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT for accrual identity only: Accruals = NetIncome - CFO = -471341000 - (-301270000) = -170071000; NetIncome == CFO + Accruals verified arithmetically, balance-sheet imbalance flag UNSAT pending Assets=Liabilities+Equity source data",
      "actionable_memo": "HOLD tariff/AP deduction. Pull FY2023 10-K, recompute all 8 Beneish variables from prior-year comparatives, reconcile balance-sheet imbalance, and investigate receivables/inventory accruals. No UCC 2-717 or 19 USC 1313 recovery quantifiable from provided data; MF-05 $50k threshold not met on verifiable surcharge."
    },
    {
      "index": 2,
      "entity_name": "SUMMER ENERGY HOLDINGS INC",
      "identifier": "CIK: 0001396633, FY: 2017",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; UCC 2-305(2) Good Faith / UCC 2-717 only if CBP 7501 tariff surcharge pass-through documented",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER - M-Score 656.29 >> -1.78 signals high manipulation probability. F-Score 0.55 < 1.0, moderate-low Dechow risk. Sloan = (1266608 - (-861401))/33586600 = 0.0634, elevated positive accruals but below 0.10 severe threshold. Positive earnings despite negative CFO is accrual-quality red flag.",
      "estimated_claim_or_surcharge_usd": 5884159,
      "z3_smt_invariant": "SAT: Accruals = 1266608 - (-861401) = 2128009; NetIncome == CFO + Accruals (1266608 == -861401 + 2128009); Sloan 0.0634 < 0.10",
      "actionable_memo": "Audit FY2017 10-K receivables, unbilled revenue and DSRI/GMI drivers. TariffRisk 1.0: estimated exposure capped at 5% x Sales 117683175 = 5884159 for screening only - require supplier invoices, CBP Form 7501 and surcharge pass-through proof before any UCC 2-717 deduction or credit memo."
    },
    {
      "index": 3,
      "entity_name": "FREEDOM HOLDING CORP.",
      "identifier": "CIK: 0000924805, FY: 2018",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; MF-09 Deterministic Verification Failure due to missing CFO - No enforceable UCC 2-717 claim on unverified data",
      "forensic_verdict": "ELEVATED: BENEISH OUTLIER / UNVERIFIABLE - M-Score 639.18 >> -1.78 signals high manipulation probability. F-Score 0.36 < 1.0. Sloan and Dechow cash components cannot be computed: CFO = NaN. Net income $19,233,000 on sales $55,224,000 (34.8% margin) requires independent verification, especially for financial-services balance-sheet classification where Beneish may be structurally distorted.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "UNSAT/UNKNOWN: NetIncome == CFO + Accruals cannot be verified; CFO is NaN, Accruals undefined; Z3 invariant fails MF-09 deterministic verification",
      "actionable_memo": "DO NOT EXECUTE deduction. Retrieve FY2018 10-K cash-flow statement from SEC EDGAR, replace NaN CFO, recompute Sloan, TATA, RSST and Beneish. TariffRisk 1.0 is unsupported for a financial holding company without import/AP records; MF-02 public-record verifiability not met, MF-05 claim = $0 until documented."
    },
    {
      "index": 4,
      "entity_name": "CRAWFORD UNITED CORPORATION",
      "identifier": "CIK: 0000047307, FY: 2016",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly > 0.10; UCC 2-305(2) / UCC 2-717 and 19 USC 1313 subject to import documentation",
      "forensic_verdict": "CRITICAL: BALANCE SHEET IMBALANCE / SEVERE ACCRUAL ANOMALY - M-Score 607.0 >> -1.78. F-Score 0.37 < 1.0 conflicts with Beneish. Sloan = (5152576 - 2513886)/15434755 = 0.1710 > 0.10, severe cash-to-accrual divergence. Net income is 77.5% of sales, implausible for operating sales alone and suggests non-operating gain, discontinued operation or data misclassification requiring footnote audit.",
      "estimated_claim_or_surcharge_usd": 332289,
      "z3_smt_invariant": "SAT for accrual identity: Accruals = 5152576 - 2513886 = 2638690; NetIncome == CFO + Accruals verified; Sloan 0.1710 > 0.10 violates conservative accrual invariant; balance-sheet imbalance UNSAT pending source filing",
      "actionable_memo": "Priority forensic review: reconcile FY2016 10-K income statement, gain-on-sale/discontinued ops, receivables and balance sheet. TariffRisk 1.67 highest in batch: screening exposure 5% x Sales 6645780 = 332289, recoverable only with CBP 7501, AP vendor master and unrefunded surcharge proof under UCC 2-717; otherwise treat as earnings-quality, not tariff, claim."
    },
    {
      "index": 5,
      "entity_name": "CRISPR THERAPEUTICS AG",
      "identifier": "CIK: 0001674416, FY: 2023",
      "statutory_hook": "Beneish 8-Variable M-Score > -1.78; Sloan Accrual Anomaly; MF-02/MF-09 Verification - No UCC 2-717 tariff claim established without import surcharge records",
      "forensic_verdict": "CRITICAL FLAG BUT ACCRUAL-CONSERVATIVE: M-Score 600.05 >> -1.78 signals Beneish outlier, likely driven by extreme SGI from collaboration revenue spike (Sales $914,963,000). F-Score 0.20 < 1.0 low Dechow risk. Sloan = (377661000 - 538972000)/2243057000 = -0.0719, negative accruals, CFO exceeds net income, contradicting accrual manipulation hypothesis. Balance-sheet imbalance flag unproven on provided data.",
      "estimated_claim_or_surcharge_usd": 0,
      "z3_smt_invariant": "SAT: Accruals = 377661000 - 538972000 = -161311000; NetIncome == CFO + Accruals (377661000 == 538972000 - 161311000); Sloan -0.0719 < 0.10",
      "actionable_memo": "Do not pursue tariff deduction on current evidence. Recompute Beneish with FY2022 comparatives and segregate one-time collaboration/license revenue in SGI/DSRI; verify balance-sheet equation from FY2023 10-K. Conservative cash accruals support earnings quality despite M-Score distortion; MF-05 verifiable surcharge = $0."
    }
  ]
}
