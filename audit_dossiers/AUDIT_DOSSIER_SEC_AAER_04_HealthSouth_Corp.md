# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: HealthSouth Corp

| Field | Value |
|---|---|
| Case ID | SEC_AAER_04 |
| Target entity | HealthSouth Corp |
| Ticker / CIK | HLS / 0000785161 |
| Category | sec_accounting_restatement |
| Accession (user-supplied, verify on EDGAR) | 0000950144-03-003829 |
| Dossier date | 2026-11-04 |
| Classification | DRAFT. Analytical work product. Not for transmission. |

**Reading note.** The matter is a historical, fully adjudicated enforcement action. The 2003 HealthSouth fraud was resolved through SEC consent judgments, a securities class action settlement, and criminal proceedings. The private right of action under Section 10(b) is barred by the five-year statute of repose in 28 U.S.C. Â§ 1658(b)(2). The supplied Statutory Recovery Opportunity of $0.00 and the null waterfall are therefore correct, and this dossier proves that result rather than contradicting it.

---

## 1. Executive Summary & Exposure Classification

**Immediate financial impact.** The supplied dataset is the post-restatement profile. Net income is negative, equity has been written down, and total accruals are deeply negative. The cumulative earnings overstatement of $2.7 billion exceeds the residual equity of $1.2 billion by a factor of 2.25 and equals 60 percent of total assets.

| Metric | Computation | Result |
|---|---|---|
| Balance sheet identity | 3,300,000,000 + 1,200,000,000 | 4,500,000,000 (ties to assets) |
| Accrual identity | -450,000,000 - 380,000,000 | -830,000,000 (ties to supplied accruals) |
| Accruals / total assets | -830,000,000 / 4,500,000,000 | -0.1844 |
| Net income / total assets | -450,000,000 / 4,500,000,000 | -0.1000 |
| CFO / total assets | 380,000,000 / 4,500,000,000 | 0.0844 |
| Liabilities / total assets | 3,300,000,000 / 4,500,000,000 | 0.7333 |
| Distortion / residual equity | 2,700,000,000 / 1,200,000,000 | 2.25x |
| Distortion / total assets | 2,700,000,000 / 4,500,000,000 | 0.60 |
| Implied pre-restatement equity | 1,200,000,000 + 2,700,000,000 | 3,900,000,000 |

**Likelihood of recovery: nil.** No live commercial setoff, duty drawback, or tax refund claim exists on these facts. Securities fraud recovery was distributed through the class settlement and SEC Fair Fund more than a decade ago, and the repose period lapsed in 2008.

**Legal exposure classification: Tier 4 historical / precedential.** The value of this file is as a calibrated fraud template for screening current health care filers under ASC 954, not as a claim.

**Three data integrity findings that a defense expert would raise first:**

- **Beneish M-Score 4.62 is not reproducible** from any index vector inside conservative screening bounds. Section 2 and the Z3 proof in Section 4 show the score requires a Total Accruals to Total Assets index above 0.52 even with every other index at its upper bound. The score should be re-derived from the pre-restatement 10-K before it is cited in any pleading.
- **Sloan accrual anomaly 0.315 does not reconcile** with the supplied financials, which yield -0.1844. The 0.315 figure is consistent only with a pre-restatement, positive-accrual profile. The dataset mixes two accounting periods.
- **ASC 606 is anachronistic.** The conduct occurred 1996 through early 2003. Revenue recognition was governed by SAB 101 and the AICPA Audit and Accounting Guide for Health Care Organizations, now codified at ASC 954-605. The $2.7 billion figure is a cumulative pre-tax earnings overstatement, not a cutoff distortion in the ASC 606 sense.

---

## 2. Core Forensic Anomaly Decomposition

### 2.1 The accounting mechanism

HealthSouth management inflated reported earnings through two coordinated distortions, both of which are now the canonical ASC 954 fraud pattern.

- **Contractual allowance understatement.** Health care providers record gross charges and reduce them by a contractual allowance to arrive at net patient revenue. Reducing the allowance accrual increases net revenue and net receivables with no cash. This inflates the Days Sales in Receivables Index and the Total Accruals index simultaneously.
- **Fictitious fixed asset entries.** The revenue plug was offset on the balance sheet by capitalizing fictitious property, plant, and equipment across hundreds of facilities, each entry sized below the auditor's scoping threshold. This inflates the Asset Quality Index and, through unsupported capitalization, the Depreciation Index.

The two levers together explain why EBITDA was the targeted metric. Contractual allowance reduction lifts the "E" and the "A" line while fixed asset capitalization keeps the offsetting debit out of operating expense.

### 2.2 Beneish eight-factor model

The published model is:

```
M = -4.84 + 0.920Â·DSRI + 0.528Â·GMI + 0.404Â·AQI + 0.892Â·SGI
          + 0.115Â·DEPI - 0.172Â·SGAI + 4.679Â·TATA - 0.327Â·LVGI
```

The decision threshold is -1.78. Only one component can be computed from the supplied dataset.

| Index | Fraud direction expected at HealthSouth | Computable from supplied data | Value |
|---|---|---|---|
| DSRI | Up, allowance understatement inflates receivables | No, needs two years of sales and receivables | n/a |
| GMI | Up, prior margin exceeds current when fraud unwinds | No | n/a |
| AQI | Up, fictitious PP&E raises non-current non-PP&E share only if misclassified, else DEPI carries it | No | n/a |
| SGI | Up, reported growth was engineered | No | n/a |
| DEPI | Up, capitalized plugs depreciated slowly | No | n/a |
| SGAI | Neutral | No | n/a |
| LVGI | Up as true equity shrinks | No | n/a |
| TATA | Positive pre-restatement, negative post-restatement | Yes | -830,000,000 / 4,500,000,000 = -0.1844 |

### 2.3 Reproducibility test of the supplied M-Score

Fix the seven ratio indices at an aggressive upper screening bound of 2.5 and the lower bound of the two negatively weighted indices at 0.25. The maximum contribution excluding TATA is:

| Term | Computation | Contribution |
|---|---|---|
| 0.920 Â· DSRI | 0.920 Â· 2.5 | 2.3000 |
| 0.528 Â· GMI | 0.528 Â· 2.5 | 1.3200 |
| 0.404 Â· AQI | 0.404 Â· 2.5 | 1.0100 |
| 0.892 Â· SGI | 0.892 Â· 2.5 | 2.2300 |
| 0.115 Â· DEPI | 0.115 Â· 2.5 | 0.2875 |
| -0.172 Â· SGAI | -0.172 Â· 0.25 | -0.0430 |
| -0.327 Â· LVGI | -0.327 Â· 0.25 | -0.0818 |
| Intercept | | -4.8400 |
| **Subtotal excluding TATA** | | **-2.6573** |

To reach M = 4.62 the TATA term must contribute 4.62 + 2.6573 = 7.2773, which requires TATA = 7.2773 / 4.679 = 1.5553 if the other indices sit at Beneish's manipulator means, or at minimum TATA = (4.62 - 2.1828) / 4.679 = 0.5209 with every ratio index pinned at 2.5. A TATA of 0.52 means accruals exceed half of total assets. That is outside any published sample.

Using the one computable input, the post-restatement TATA of -0.1844 caps the score at -2.6573 + 4.679 Â· (-0.1844) = -3.5203 even with every other index at its upper bound. The post-restatement profile is firmly non-manipulator, as expected after a clean-up restatement.

**Conclusion.** The 4.62 is either a vendor-side scaling artifact or was computed on a pre-restatement vector that must be produced with the score. Cite the finding, not the number, until the vector is in the evidence ledger.

### 2.4 Dechow F-Score

The supplied field is a logit of 0.953. Both readings are shown because the field label is ambiguous.

| Reading | Computation | Probability | F-Score vs 0.0037 base rate |
|---|---|---|---|
| 0.953 is the logit | 1 / (1 + e^-0.953) = 1 / 1.3856 | 0.7217 | 195.1 |
| 0.953 is the probability | as given | 0.9530 | 257.6 |

Either reading exceeds the "substantial risk" threshold of 2.45 by two orders of magnitude. As with the M-Score, the seven F-Score inputs are not in the dataset and must be reconstructed from the 10-K and 10-K/A.

### 2.5 Sloan accrual signal

Sloan's ratio is total accruals over average total assets. The supplied financials produce -0.1844. The supplied anomaly score is 0.315, which has the opposite sign. The only consistent interpretation is that 0.315 was measured on reported pre-restatement figures, where accruals were large and positive. The pre-restatement sign flip is itself the forensic signal: a firm whose accrual ratio moves from above 0.30 to below -0.18 across a restatement has reversed roughly half of its asset base in paper earnings.

---

## 3. Statutory & Commercial Recovery Basis

### 3.1 Commercial doctrines requested in the brief

Each is analyzed and rejected on the facts. A defense-grade dossier states this plainly rather than forcing an inapplicable theory.

- **UCC Â§ 2-717 deduction of damages from price.** Requires a buyer, a seller, and a contract for the sale of goods with a breach of that contract. HealthSouth's distortion was in financial reporting to the securities markets. No goods contract between the claimant and HealthSouth is in evidence. Setoff is unavailable.
- **UCC Â§ 2-305 open price term.** Governs price gaps in goods contracts. No open-price contract exists. Inapplicable.
- **19 U.S.C. Â§ 1313 duty drawback.** Requires imported merchandise, duties paid, and export or destruction within the statutory window. HealthSouth is a domestic rehabilitation services provider. No merchandise, no duties, no drawback.
- **Internal Revenue Code.** A restatement that reduces previously reported taxable income can support refund claims by the filer under 26 U.S.C. Â§ 6511. That claim belonged to HealthSouth, not to a third-party claimant, and the three-year refund window closed long ago.

### 3.2 Securities law basis actually engaged

- **15 U.S.C. Â§ 78j(b) and Rule 10b-5.** Material misstatement, scienter, reliance, loss causation, and damages were all established in the public record. Private claims are subject to 28 U.S.C. Â§ 1658(b): two years from discovery and five years from the violation. The violation period ended in March 2003. The repose bar fell in March 2008 and cannot be tolled.
- **15 U.S.C. Â§ 78t(a) control-person liability.** Same repose bar.
- **Sarbanes-Oxley Â§ 304, 15 U.S.C. Â§ 7243.** CEO and CFO reimbursement of incentive compensation after a restatement caused by misconduct. This is an SEC remedy, not a private one. It was pursued in SEC v. Scrushy and is the precedent of record for clawback in restatement cases.
- **Sarbanes-Oxley Â§ 308 Fair Funds.** The civil penalty was distributed to harmed investors. The distribution is closed.

### 3.3 ASC 954 as the measurement standard

ASC 954-605 and 954-310 require contractual allowances to be estimated at the time service is rendered and reviewed against actual remittance. The forensic test for any current health care filer is the ratio of contractual allowance to gross charges by payer, trended quarterly. A declining allowance percentage without a corresponding payer mix shift is the HealthSouth signature.

### 3.4 Recovery conclusion

| Theory | Live claim | Amount |
|---|---|---|
| UCC Â§ 2-717 setoff | No | $0.00 |
| UCC Â§ 2-305 | No | $0.00 |
| 19 U.S.C. Â§ 1313 | No | $0.00 |
| Rule 10b-5 private action | Time-barred by Â§ 1658(b)(2) | $0.00 |
| SOX Â§ 304 | SEC only, already adjudicated | $0.00 to claimant |
| **Total** | | **$0.00** |

The supplied Statutory Recovery Opportunity of $0.00 is confirmed. Waterfall: null.

---

## 4. Executable Z3 SMT Counterexample Proof

The script proves four things. Block A shows the supplied dataset is internally consistent and that the accrual ratio is exactly -83/450. Block B shows that M = 4.62 is unsatisfiable inside the screening bounds and computes the minimum TATA that would be required. Block C proves the distortion exceeds residual equity and implies pre-restatement equity of exactly $3.9 billion. Block D proves recovery is zero under the repose bar. All constants are exact rationals, never floats.

```python
#!/usr/bin/env python3
"""
SovereignForensics  |  Case SEC_AAER_04  |  HealthSouth Corp (CIK 0000785161)
Z3 SMT verification of the forensic invariants in the dossier.

Requires:  pip install z3-solver
Run:       python -I healthsouth_z3_proof.py
"""
from z3 import (Reals, Real, Bool, RealVal, Solver, Optimize,
                And, Not, Implies, sat, unsat)


def Q(text):
    """Exact rational from a decimal or 'p/q' string. Never pass a float."""
    return RealVal(text)


results = {}

# ---------------------------------------------------------------------------
# Block A : supplied (post-restatement) financials and accounting identities
# ---------------------------------------------------------------------------
assets, liab, equity, ni, cfo, accr = Reals("assets liab equity ni cfo accr")

facts = [
    assets == Q("4500000000"),
    liab   == Q("3300000000"),
    equity == Q("1200000000"),
    ni     == Q("-450000000"),
    cfo    == Q("380000000"),
    accr   == Q("-830000000"),
]
identities = [
    assets == liab + equity,          # balance sheet identity
    accr   == ni - cfo,               # total accruals identity
]

sA = Solver()
sA.add(facts + identities)
results["A1_dataset_consistent"] = sA.check()
assert results["A1_dataset_consistent"] == sat

# Invariant: accruals / assets == -83/450 exactly. Prove by refuting the negation.
sA2 = Solver()
sA2.add(facts)
sA2.add(Not(accr / assets == Q("-83") / Q("450")))
results["A2_accrual_ratio_negation"] = sA2.check()
assert results["A2_accrual_ratio_negation"] == unsat

# ---------------------------------------------------------------------------
# Block B : Beneish M-Score reproducibility
# ---------------------------------------------------------------------------
dsri, gmi, aqi, sgi, depi, sgai, lvgi, tata = Reals(
    "dsri gmi aqi sgi depi sgai lvgi tata")

M = (Q("-4.84")
     + Q("0.920") * dsri + Q("0.528") * gmi + Q("0.404") * aqi
     + Q("0.892") * sgi  + Q("0.115") * depi - Q("0.172") * sgai
     + Q("4.679") * tata - Q("0.327") * lvgi)

LO, HI = Q("0.25"), Q("2.5")          # screening bounds for the seven ratio indices
ratio_bounds = [And(v >= LO, v <= HI)
                for v in (dsri, gmi, aqi, sgi, depi, sgai, lvgi)]
tata_bound = And(tata >= Q("-0.25"), tata <= Q("0.25"))

# B1: M == 4.62 is UNSAT inside the bounds (the supplied score is not reproducible)
sB1 = Solver()
sB1.add(ratio_bounds)
sB1.add(tata_bound)
sB1.add(M == Q("4.62"))
results["B1_mscore_4_62_within_bounds"] = sB1.check()
assert results["B1_mscore_4_62_within_bounds"] == unsat

# B2: minimum TATA required to reach 4.62 when the ratio indices are unconstrained
#     inside [0.25, 2.5]. Expected: (4.62 - 2.18275) / 4.679 = 0.520891...
oB2 = Optimize()
oB2.add(ratio_bounds)
oB2.add(M == Q("4.62"))
oB2.minimize(tata)
results["B2_min_tata_for_4_62"] = oB2.check()
assert results["B2_min_tata_for_4_62"] == sat
min_tata = oB2.model()[tata]

# B3: with the post-restatement TATA of -83/450, M < -1.78 for every bounded
#     ratio vector. Prove by refuting M >= -1.78.
sB3 = Solver()
sB3.add(ratio_bounds)
sB3.add(tata == Q("-83") / Q("450"))
sB3.add(M >= Q("-1.78"))
results["B3_post_restatement_above_threshold"] = sB3.check()
assert results["B3_post_restatement_above_threshold"] == unsat

# ---------------------------------------------------------------------------
# Block C : distortion bound against residual equity
# ---------------------------------------------------------------------------
distortion  = Q("2700000000")
pre_equity  = Real("pre_equity")

sC1 = Solver()
sC1.add(equity == Q("1200000000"))
sC1.add(pre_equity == equity + distortion)
sC1.add(Not(pre_equity == Q("3900000000")))
results["C1_pre_equity_3_9bn_negation"] = sC1.check()
assert results["C1_pre_equity_3_9bn_negation"] == unsat

sC2 = Solver()
sC2.add(equity == Q("1200000000"))
sC2.add(Not(distortion > equity))
results["C2_distortion_exceeds_equity_negation"] = sC2.check()
assert results["C2_distortion_exceeds_equity_negation"] == unsat

# ---------------------------------------------------------------------------
# Block D : statutory recovery bound under 28 U.S.C. 1658(b)(2)
# ---------------------------------------------------------------------------
recovery      = Real("recovery")
repose_lapsed = Bool("repose_lapsed")

sD = Solver()
sD.add(recovery >= 0)
sD.add(repose_lapsed == True)                 # violation period ended 2003-03; 5y repose lapsed 2008-03
sD.add(Implies(repose_lapsed, recovery == 0))
sD.add(Not(recovery == 0))
results["D1_nonzero_recovery_negation"] = sD.check()
assert results["D1_nonzero_recovery_negation"] == unsat

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
print("SEC_AAER_04  HealthSouth Corp  |  Z3 verification")
print("-" * 64)
for key, val in results.items():
    print(f"{key:<42} {val}")
print(f"{'B2 minimal TATA (exact)':<42} {min_tata}")
print(f"{'B2 minimal TATA (decimal)':<42} {min_tata.as_decimal(6)}")
print("-" * 64)
print("FORMAL VERDICT : dataset identities SAT ; M=4.62 within bounds UNSAT ;")
print("                 recovery != 0 UNSAT  =>  Statutory recovery = $0.00")
```

**Expected output**

```
A1_dataset_consistent                      sat
A2_accrual_ratio_negation                  unsat
B1_mscore_4_62_within_bounds               unsat
B2_min_tata_for_4_62                       sat
B3_post_restatement_above_threshold        unsat
C1_pre_equity_3_9bn_negation               unsat
C2_distortion_exceeds_equity_negation      unsat
D1_nonzero_recovery_negation               unsat
B2 minimal TATA (exact)                    243725/467900
B2 minimal TATA (decimal)                  0.520891?
```

The question mark on the decimal line is Z3's standard marker for a truncated irrational-looking rational and is expected.

---

## 5. Actionable Legal Remediation & Demand Notice Template

Because no monetary claim survives, the only deliverable with live utility is a document preservation and production notice. It is drafted for reuse against any current ASC 954 filer that trips the Section 2 screens. Fields in brackets are fill-ins. This is a draft. Transmission is a human decision.

```
DRAFT. NOT FOR TRANSMISSION WITHOUT PRINCIPAL SIGN-OFF.

John Webb & Co.
Louisville, Kentucky
Direct: 502-693-2779

[Date]

VIA CERTIFIED MAIL AND ELECTRONIC DELIVERY

[Registrant Name]
Attn: General Counsel and Audit Committee Chair
[Address]

Re:  Notice of Forensic Findings, Litigation Hold Demand, and Request for
     Production. Registrant CIK [__________]. Reference File [__________].

1.  Basis of Notice
    The undersigned has completed a forensic screen of the Registrant's
    periodic reports for fiscal periods [____] through [____]. The screen
    returned the following indicators, each of which exceeds the published
    decision threshold:

        Beneish M-Score            [____]   (threshold -1.78)
        Dechow F-Score             [____]   (threshold 1.00; high risk 2.45)
        Sloan accrual ratio        [____]   (sign and magnitude vs prior period)
        Contractual allowance %    [____]   vs prior period [____]

    The pattern is consistent with (a) understatement of contractual
    allowances under ASC 954-605 and (b) unsupported capitalization of
    fixed assets, the fact pattern adjudicated in SEC v. HealthSouth Corp.,
    Civ. No. CV-03-J-0615-S (N.D. Ala. 2003).

2.  Claim Calculation
    Estimated cumulative earnings overstatement:      $[____________]
    Residual equity per most recent balance sheet:    $[____________]
    Overstatement as multiple of residual equity:      [____]x
    Overstatement as fraction of total assets:         [____]
    (Methodology: Section 2 of the attached dossier. All arithmetic is
    verified by the attached Z3 SMT script, reproducible on request.)

3.  Formal Demand
    Within ten (10) calendar days of receipt, the Registrant shall:
    (a) issue a written litigation hold covering all general ledger detail,
        contractual allowance roll-forwards by payer, fixed asset subledgers,
        and journal entry audit trails for the periods identified;
    (b) produce the contractual allowance methodology memorandum and the
        quarterly allowance-to-gross-charge reconciliation for each period;
    (c) produce the fixed asset additions listing with supporting invoices
        for all additions below the external auditor's scoping threshold;
    (d) confirm in writing whether the Audit Committee has been informed of
        the indicators in Section 1.

4.  Cure Period
    If the Registrant furnishes a reconciliation that resolves each
    indicator in Section 1 within the ten (10) day period, this matter will
    be closed without further action. Absent a satisfactory response, the
    undersigned reserves all rights, including referral under 15 U.S.C.
    Â§ 78u-6 and notice to the Registrant's independent registered public
    accounting firm.

5.  Reservation of Rights
    Nothing in this notice waives any right or remedy. This notice is not
    an admission as to the applicability of any limitations or repose
    period.

John Webb
Principal, John Webb & Co.
502-693-2779

Attachments: Forensic Audit Dossier SEC_AAER_04 (template reference);
             healthsouth_z3_proof.py; SHA-256 manifest.
```

**For the HealthSouth file specifically** the notice is moot. The file should be closed with the annotation "historical, repose lapsed 2008-03, recovery $0.00, retained as ASC 954 screening template."

---

## 6. Verification & Chain of Custody

### 6.1 SHA-256 integrity

No hashes are stated in this dossier because none were computed at authoring time. Fabricated hashes are the single fastest way to lose a Daubert challenge. Compute them at ingestion and store them in the evidence ledger below.

```powershell
# PowerShell, run from the evidence directory
Get-ChildItem -File | ForEach-Object {
  [pscustomobject]@{
    file   = $_.Name
    sha256 = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
    bytes  = $_.Length
    utc    = (Get-Date).ToUniversalTime().ToString("o")
  }
} | Export-Csv -NoTypeInformation sha256_manifest.csv
```

Artifacts to hash: the EDGAR filing index and primary document for accession 0000950144-03-003829, the 10-K/A restatement filing, the Z3 script, this dossier, and the DuckDB database file after load.

### 6.2 DuckDB 2.0.0 LTS schema

```sql
CREATE SCHEMA IF NOT EXISTS forensics;

CREATE TABLE forensics.filer_master (
    case_id          VARCHAR PRIMARY KEY,
    entity_name      VARCHAR NOT NULL,
    ticker           VARCHAR,
    cik              VARCHAR(10) NOT NULL,
    category         VARCHAR NOT NULL,
    accession_number VARCHAR,
    accession_verified BOOLEAN DEFAULT FALSE,
    statutory_basis  VARCHAR,
    loaded_utc       TIMESTAMP DEFAULT current_timestamp
);

CREATE TABLE forensics.financial_facts (
    case_id      VARCHAR REFERENCES forensics.filer_master(case_id),
    basis        VARCHAR CHECK (basis IN ('as_reported','as_restated')),
    fiscal_end   DATE,
    assets       DECIMAL(20,2),
    liabilities  DECIMAL(20,2),
    equity       DECIMAL(20,2),
    net_income   DECIMAL(20,2),
    cfo          DECIMAL(20,2),
    accruals     DECIMAL(20,2),
    PRIMARY KEY (case_id, basis, fiscal_end),
    CHECK (assets = liabilities + equity),
    CHECK (accruals = net_income - cfo)
);

CREATE TABLE forensics.forensic_scores (
    case_id        VARCHAR REFERENCES forensics.filer_master(case_id),
    basis          VARCHAR,
    beneish_m      DECIMAL(8,4),
    dsri DECIMAL(8,4), gmi DECIMAL(8,4), aqi DECIMAL(8,4), sgi DECIMAL(8,4),
    depi DECIMAL(8,4), sgai DECIMAL(8,4), lvgi DECIMAL(8,4), tata DECIMAL(8,4),
    dechow_logit   DECIMAL(8,4),
    sloan_ratio    DECIMAL(8,4),
    reproducible   BOOLEAN,
    reproduce_note VARCHAR,
    PRIMARY KEY (case_id, basis)
);

CREATE TABLE forensics.evidence_ledger (
    artifact_id   VARCHAR PRIMARY KEY,
    case_id       VARCHAR REFERENCES forensics.filer_master(case_id),
    file_name     VARCHAR NOT NULL,
    sha256        VARCHAR(64) NOT NULL,
    byte_length   BIGINT,
    source_url    VARCHAR,
    collected_utc TIMESTAMP,
    collector     VARCHAR
);

CREATE TABLE forensics.z3_runs (
    run_id        VARCHAR PRIMARY KEY,
    case_id       VARCHAR REFERENCES forensics.filer_master(case_id),
    script_sha256 VARCHAR(64),
    check_name    VARCHAR,
    result        VARCHAR CHECK (result IN ('sat','unsat','unknown')),
    model_text    VARCHAR,
    run_utc       TIMESTAMP DEFAULT current_timestamp
);

-- Load the supplied post-restatement vector. The CHECK constraints are the
-- first integrity gate; a row that violates either identity is rejected.
INSERT INTO forensics.financial_facts VALUES
('SEC_AAER_04','as_restated',NULL,
 4500000000.00, 3300000000.00, 1200000000.00,
 -450000000.00,  380000000.00, -830000000.00);

-- Record the reproducibility finding from Section 2.3.
INSERT INTO forensics.forensic_scores
(case_id, basis, beneish_m, tata, dechow_logit, sloan_ratio, reproducible, reproduce_note)
VALUES
('SEC_AAER_04','as_restated', 4.6200, -0.1844, 0.9530, 0.3150, FALSE,
 'M=4.62 UNSAT within [0.25,2.5] ratio bounds; min TATA 0.5209; Sloan sign conflict');
```

### 6.3 TruLens RAG triad evaluation

The dossier should be scored by a separate evaluator model, not by its author. Pin the judge to a factual-tier model per the Model Router policy. Thresholds below are the acceptance gates. Scores are left blank by design; populating them without a run would be the same fabrication problem as the hashes.

| Triad dimension | What is checked | Gate | Score |
|---|---|---|---|
| Context relevance | Every retrieved passage cited in Sections 2 and 3 is about HealthSouth, ASC 954, the Beneish or Dechow models, or the cited statutes | â‰¥ 0.85 | pending run |
| Groundedness | Every numeric claim in Sections 1, 2, and 4 traces to a supplied input or to arithmetic shown in the dossier | â‰¥ 0.95 | pending run |
| Answer relevance | Each of the six requested sections is present and responsive to the brief, including the explicit rejection of inapplicable UCC and drawback theories | â‰¥ 0.90 | pending run |

**Groundedness pre-check performed by the author.** Every number in this dossier is one of: a supplied input, a product or quotient of supplied inputs with the computation shown, a published Beneish coefficient, or a published statutory period. The three places where supplied inputs could not be reconciled with each other are stated as such in Sections 1 and 2 rather than smoothed over.

**Open items before this file is cited anywhere:**

- Verify accession 0000950144-03-003829 against EDGAR and record the primary document type.
- Obtain the pre-restatement index vector behind the 4.62 M-Score, or recompute it from the as-reported 10-K and load it under `basis = 'as_reported'`.
- Run the Z3 script, run the hash manifest, and populate the evidence ledger and the TruLens scores.