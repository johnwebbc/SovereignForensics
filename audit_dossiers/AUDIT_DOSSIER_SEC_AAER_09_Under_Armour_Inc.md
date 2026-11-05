# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Under Armour Inc

**Case ID:** SEC_AAER_09 | **Ticker:** UAA | **CIK:** 0001336917 | **Accession:** 0001336917-21-000028

**Status: draft, not publication-grade.** The input record has material inconsistencies, and no source documents, Z3 script, hashes, or evaluations were opened or run. Legal citations and case facts come from memory and need a cite-check.

## 1. Executive Summary & Exposure Classification

**Conclusion: this file supports no recovery action or demand against Under Armour.** The supplied recovery figure of $0.00 is the correct working number, and the null waterfall is consistent with it.

| Item | Classification | Basis |
|---|---|---|
| **Immediate financial impact** | **$0.00 recoverable** | No claimant, contract, duty payment, or damages are identified. |
| **Likelihood of recovery** | **None on this record** | The UCC and drawback theories have no factual predicate, and Â§ 17(a) is generally not privately enforceable. |
| **Legal exposure** | **Largely resolved; confirm any residual exposure** | The SEC matter settled in May 2021 for a reported $9M penalty, and the investor class action reportedly settled for $434M in 2024. |

### Corrections required before any use

| Input | Problem | Correction |
|---|---|---|
| **`sec_accounting_restatement`** | As I recall, the SEC order required no restatement and did not find the revenue improperly recognized. | Reclassify as a disclosure matter, pending review of the order. |
| **"ASC 606 Cutoff Distortion"** | The conduct ran from Q3 2015 to Q4 2016, but Under Armour adopted ASC 606 in 2018. ASC 605 and SAB Topic 13 governed. | Relabel it "disclosed-later pull-forward amount." It isn't an established cutoff error. |
| **Sloan accrual of 0.174** | -$781M / $4,844M = **-0.1612**, so both sign and magnitude differ. A 0.174 magnitude implies a $4,488.5M denominator. | Use -0.1612, or document the denominator. |
| **Beneish M-Score of 2.89** | This requires implausible index values (see Section 2). A value of -2.89 would be plausible, and it would fall below the common -1.78 flag. | Recompute from source data. |
| **Dechow logit of 0.768** | As a true logit, this implies a 68.3% probability and an F-score of about 185 (0.6831 / 0.0037). As an F-score, it signals below-baseline risk. | Define the field and recompute it. |
| **Financials** | The accession prefix suggests a 2021 filing, likely FY2020, while the conduct occurred in 2015â€“2016. The -$549M net loss also reflects a later period. | Score FY2014â€“FY2017 separately. |
| **Balance sheet and CFO** | These foot internally, but they don't match my recollection of FY2020 (assets near $4.44B, CFO near $212M). | Tie every value to XBRL. |
| **Z3 result of `SAT`** | No formula was supplied. SAT would show only that constraints are consistent, not that manipulation occurred. | Replace with the named checks in Section 4. |

## 2. Core Forensic Anomaly Decomposition

### What the case involves
The SEC alleged that Under Armour accelerated about $408M of existing orders across six consecutive quarters to help meet analyst revenue expectations. It also alleged that the company failed to disclose that reliance and its effect on future revenue.

The central issue is therefore misleading disclosure about the quality and sustainability of revenue, including known trends under Regulation S-K Item 303 (17 C.F.R. Â§ 229.303). A pull-forward shifts revenue between periods, so it says little by itself about permanent earnings overstatement.

### Beneish decomposition
M = -4.84 + 0.920Â·DSRI + 0.528Â·GMI + 0.404Â·AQI + 0.892Â·SGI + 0.115Â·DEPI - 0.172Â·SGAI + 4.679Â·TATA - 0.327Â·LVGI

Only TATA can be computed from the supplied data. The other seven indices need two years of line items, so their values are left open.

| Component | Measures | Contribution at neutral (1.0) | Expected pull-forward signal | Status |
|---|---|---|---|---|
| **DSRI** | Receivables relative to sales | +0.920 | Up if shipments cluster near quarter-end | Needs data |
| **GMI** | Prior vs. current gross margin | +0.528 | Up if incentives were used to secure acceleration | Needs data |
| **AQI** | Non-productive asset share | +0.404 | No direct link | Needs data |
| **SGI** | Sales growth | +0.892 | Up in the receiving period, down when the shift reverses | Needs data |
| **DEPI** | Depreciation rate | +0.115 | No direct link | Needs data |
| **SGAI** | SG&A relative to sales | -0.172 | Possibly down as accelerated sales increase the denominator | Needs data |
| **LVGI** | Leverage growth | -0.327 | No direct link | Needs data |
| **TATA** | Accruals to total assets | **-0.7544** (actual) | Up if receivables build; the supplied value is negative | Computed: -0.1612 |

### Why 2.89 fails
- **Neutral baseline:** with seven neutral indices and the actual TATA, M = -4.84 + 2.36 - 0.7544 = **-3.2344**.
- **Reaching +2.89:** this needs +6.1244 from the indices. DSRI alone would have to be about **7.66**, or the five positively weighted indices would all need to exceed about **3.05** with the other two at 0.5.
- **Reaching -2.89:** this needs only +0.3444, which is a modest change.

### Accrual reading
The -$781M accrual figure is arithmetically correct (-$549M - $232M), but it shows net income well below operating cash flow. That pattern is more consistent with non-cash charges in a loss year than with income inflated by accruals. It can't serve as evidence of the 2015â€“2016 pull-forwards.

## 3. Statutory & Commercial Recovery Basis

| Authority | Requires | Application | Result |
|---|---|---|---|
| **15 U.S.C. Â§ 77q(a)(2), (3)** | Negligent misstatement or deceptive conduct in an offer or sale (*Aaron v. SEC*, 446 U.S. 680 (1980)) | Fits the SEC's enforcement theory, but courts widely reject a private right of action (*Finkel v. Stratton Corp.*, 962 F.2d 169 (2d Cir. 1992); *Maldonado v. Dominguez*, 137 F.3d 1 (1st Cir. 1998)) | No private recovery |
| **UCC Â§ 2-717** | A buyer's notice and damages from a breach of the same contract | No buyer, contract, or breach is identified, and an order acceleration doesn't itself create setoff damages | Not available |
| **UCC Â§ 2-305** | A sale contract with an open price term | No such term is in the record | Not applicable |
| **19 U.S.C. Â§ 1313** | Qualifying imports, exports or destruction, and a timely claim, generally within 5 years of import (Â§ 1313(r)) | No entries, duties, or export records exist, and any claim would belong to the eligible claimant, not a third-party auditor | $0 supportable |
| **15 U.S.C. Â§ 78j(b), Rule 10b-5** | Scienter, reliance, loss causation, and timeliness | This was the proper private route, but the class settlement likely covers it, and the 5-year repose in 28 U.S.C. Â§ 1658(b) appears to have run for 2015â€“2016 statements | Check class membership and opt-out status only |
| **15 U.S.C. Â§ 7243 (SOX Â§ 304)** | An accounting restatement caused by misconduct | Not triggered if no restatement occurred, and it isn't privately enforceable in any case | Not available |
| **I.R.C. Â§ 162(f)** | Limits deductions for government fines and penalties | Affects the company's tax treatment of the penalty and creates no third-party recovery | Tax point only |

The $408M can't serve as a damages figure. It measures revenue moved between periods, and no one's actual loss can be derived from it.

## 4. Executable Z3 SMT Counterexample Proof

Each proof asserts the negation of a claim, so `unsat` means the claim holds under the stated inputs and assumptions. **This script has not been run.** Expected results are in the code, and my hand arithmetic agrees with the Beneish bound.

```python
#!/usr/bin/env python3
"""SEC_AAER_09 arithmetic and recovery-bound checks.

Requires: pip install z3-solver
Financial values are in USD millions. Inputs are unverified.
The Beneish bounds and recovery rule are explicit modeling assumptions.
"""
import sys

from z3 import *

A, L, E, NI, CFO, ACCR = 4844, 2980, 1864, -549, 232, -781
results = []


def check(label, expected, *constraints):
    s = Solver()
    s.add(*constraints)
    got = s.check()
    passed = got == expected
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {label}: {got} (expected {expected})")


# P1-P2: reported financials are internally consistent.
check("P1 assets = liabilities + equity", unsat,
      Not(IntVal(A) == IntVal(L) + IntVal(E)))
check("P2 accruals = net income - CFO", unsat,
      Not(IntVal(ACCR) == IntVal(NI) - IntVal(CFO)))

# P3: the reported Sloan value does not match accruals / assets.
sloan = Q(ACCR, A)
reported_sloan = Q(174, 1000)
check("P3a computed Sloan is negative", unsat, Not(sloan < 0))
check("P3b magnitude differs by more than 0.01", unsat,
      Not(reported_sloan + sloan > Q(1, 100)))

# P4: test the reported M-score against bounded Beneish indices.
COEF = {
    "DSRI": Q(920, 1000),
    "GMI": Q(528, 1000),
    "AQI": Q(404, 1000),
    "SGI": Q(892, 1000),
    "DEPI": Q(115, 1000),
    "SGAI": Q(-172, 1000),
    "LVGI": Q(-327, 1000),
}
idx = {name: Real(name) for name in COEF}
m_score = (
    Q(-484, 100)
    + Sum([COEF[name] * idx[name] for name in COEF])
    + Q(4679, 1000) * sloan
)


def bounds(high):
    return And([And(v >= Q(1, 2), v <= high) for v in idx.values()])


check("P4a M=+2.89 infeasible with indices in [0.5, 3.00]", unsat,
      bounds(RealVal(3)), m_score == Q(289, 100))
check("P4b M=-2.89 feasible with indices in [0.5, 3.00]", sat,
      bounds(RealVal(3)), m_score == Q(-289, 100))
check("P4c M=+2.89 infeasible at upper bound 3.05", unsat,
      bounds(Q(305, 100)), m_score == Q(289, 100))
check("P4d M=+2.89 feasible at upper bound 3.06", sat,
      bounds(Q(306, 100)), m_score == Q(289, 100))

# P5: one-quarter pull-forwards conserve revenue across a closed window.
N = 7
base = IntVector("base", N)
pull = IntVector("pull", N - 1)
recognized = [
    base[i]
    + (pull[i] if i < N - 1 else 0)
    - (pull[i - 1] if i > 0 else 0)
    for i in range(N)
]
check("P5a total window revenue is conserved", unsat,
      Not(Sum(recognized) == Sum(base)))
check("P5b $408M can move while the window total is unchanged", sat,
      And([p >= 0 for p in pull]),
      Sum(pull) == 408,
      Sum(recognized) == Sum(base),
      recognized[0] != base[0])

# P6: under the encoded rule, no privity or breach means no setoff.
privity, breach = Bools("privity breach")
damages, setoff = Reals("damages setoff")
rule = And(
    damages >= 0,
    setoff >= 0,
    setoff <= damages,
    Implies(setoff > 0, And(privity, breach)),
)
check("P6 recovery bound is $0 without privity", unsat,
      rule, Not(privity), Not(setoff == 0))

print(f"\n{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
```

**Limits of the proof:**
- **What it covers:** the script tests arithmetic and the encoded assumptions.
- **What it doesn't cover:** it can't establish the source figures, legal conclusions, or intent. P6 only applies the rule as written, and P5 assumes each order moved one quarter and was not canceled.

## 5. Actionable Legal Remediation & Demand Notice Template

### Remediation
1. **Hold the notice.** Don't send a demand on this record, because it would assert a claim with no identified claimant, contract, or loss.
2. **Correct the case record.** Apply the Section 1 changes and rebuild the metrics from period-matched filings.
3. **Get the primary sources.** Pull the SEC order to confirm the AAER number, findings, and penalty, along with the class settlement documents.
4. **Refer any investor questions.** Anyone with a possible investor claim should ask securities counsel about class membership, opt-outs, and timing.

### Conditional template
Use this only if a real claimant has a real contract claim, and have licensed counsel review it first. It deliberately omits the SEC matter, since that matter doesn't establish a contract breach and shouldn't be used as leverage.

> **[CLAIMANT LETTERHEAD]**
> **[DATE]**
>
> **VIA [CONTRACTUALLY REQUIRED DELIVERY METHOD]**
> [Notice Party, Title]
> Under Armour, Inc.
> [Notice Address from Contract]
>
> **Re: Notice of Breach and Demand for Cure: [Agreement Name], dated [Date]**
>
> To [Notice Party]:
>
> [Claimant] gives notice under [Agreement Â§ __] and, where applicable, UCC Â§Â§ 2-607(3)(a) and 2-717, that Under Armour, Inc. has breached the Agreement as follows: [specific obligation, date, and conduct].
>
> **Claim calculation**
>
> | Item | Document | Amount |
> |---|---|---|
> | [Invoice or purchase order] | [Reference] | $[____] |
> | [Direct damages] | [Reference] | $[____] |
> | [Credits or offsets] | [Reference] | ($[____]) |
> | **Total demanded** | | **$[____]** |
>
> **Demand.** Within ten (10) calendar days of receipt, please (a) pay $[____] to [payment instructions] or (b) cure the breach by [specific action].
>
> **Setoff.** If the UCC and the Agreement permit, [Claimant] intends to deduct proven damages of $[____] from the price still due under the same contract, namely [Invoice No.].
>
> **Preservation.** Please preserve documents and data relating to this matter, including [categories].
>
> This notice does not state every relevant fact or remedy, and [Claimant] reserves its rights under the Agreement and applicable law.
>
> Sincerely,
>
> [Authorized Signatory or Counsel]
> [Claimant]
>
> *Prepared by:*
> John Webb, Principal
> John Webb & Co., Louisville, KY
> 502-693-2779

**Current claim amount: $0.00. Status: do not issue.**

## 6. Verification & Chain of Custody

### Verification status

| Control | Status | Required action |
|---|---|---|
| **Muse Glimmer 30B** | Not run | Record the model and prompt if it is used later. |
| **Z3 proof** | Not run | Save stdout, the exit code, and the `z3-solver` version. |
| **DuckDB 2.0.0 LTS** | Not run; version not confirmed | Load the data and record `SELECT version();`. |
| **SHA-256 integrity** | No hashes generated | Hash the retrieved sources and final artifacts. |
| **TruLens RAG triad** | Not run; no scores exist | Evaluate only after the source corpus is indexed. |
| **SEC order and AAER No. 4218** | Not verified | Retrieve the order and confirm the citation. |
| **Accession 0001336917-21-000028** | Not opened | Confirm its form type and fiscal period. |
| **Legal authorities and settlement facts** | From memory | Cite-check against primary sources. |

### SHA-256 capture
```powershell
Get-FileHash -Algorithm SHA256 .\sources\* | Export-Csv .\sha256_manifest.csv -NoTypeInformation
```

### DuckDB schema
```sql
CREATE TABLE source_artifact (
    artifact_id     VARCHAR PRIMARY KEY,
    case_id         VARCHAR NOT NULL,
    source_url      VARCHAR,
    accession_no    VARCHAR,
    retrieved_at    TIMESTAMPTZ NOT NULL,
    sha256          VARCHAR NOT NULL CHECK (length(sha256) = 64),
    verified_by     VARCHAR
);

CREATE TABLE financial_fact (
    case_id         VARCHAR NOT NULL,
    fiscal_period   VARCHAR NOT NULL,
    concept         VARCHAR NOT NULL,
    value_usd       DECIMAL(18, 2) NOT NULL,
    artifact_id     VARCHAR NOT NULL REFERENCES source_artifact (artifact_id),
    PRIMARY KEY (case_id, fiscal_period, concept)
);

CREATE TABLE forensic_metric (
    case_id         VARCHAR NOT NULL,
    fiscal_period   VARCHAR NOT NULL,
    metric          VARCHAR NOT NULL,
    reported_value  DOUBLE,
    computed_value  DOUBLE,
    formula_version VARCHAR NOT NULL,
    status          VARCHAR NOT NULL CHECK (status IN ('MATCH', 'MISMATCH', 'UNVERIFIED')),
    PRIMARY KEY (case_id, fiscal_period, metric, formula_version)
);

CREATE TABLE proof_run (
    run_id          VARCHAR PRIMARY KEY,
    case_id         VARCHAR NOT NULL,
    script_sha256   VARCHAR NOT NULL CHECK (length(script_sha256) = 64),
    z3_version      VARCHAR NOT NULL,
    executed_at     TIMESTAMPTZ NOT NULL,
    exit_code       INTEGER NOT NULL,
    stdout          VARCHAR NOT NULL
);
```

### TruLens RAG triad

| Measure | Test | Score |
|---|---|---|
| **Context relevance** | Do the retrieved passages address the specific claim? | Not run |
| **Groundedness** | Is each factual and legal claim supported by a hashed source? | Not run |
| **Answer relevance** | Does the dossier answer the case question and required sections? | Not run |

**Release gate:** keep this dossier in draft until the source tie-out, proof run, hash manifest, legal cite-check, and counsel review are complete.