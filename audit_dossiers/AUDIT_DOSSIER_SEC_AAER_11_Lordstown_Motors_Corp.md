# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Lordstown Motors Corp

**Status: not publication-grade or ready to deliver.** The supplied record supports **$0.00** in recovery and contains unreconciled metrics. This dossier was prepared without access to filings or tools, so no code was run, no external source was checked, and legal citations and background facts come from memory. It needs attorney review and is not legal advice.

## 1. Executive Summary & Exposure Classification

| Item | Assessment |
|---|---|
| **Immediate financial impact** | $0.00 supported recovery; no waterfall can be calculated from a null input |
| **Likelihood of recovery** | Not supported on this record: no claimant, purchase history, damages, or surviving claim path |
| **Legal exposure** | Mainly a historical disclosure issue under Exchange Act Â§ 10(b) and Item 303; bankruptcy and time bars must be cleared before any new claim |
| **Core issue** | Alleged misleading presentation of fleet pre-orders; "zero purchase intent" needs customer-level evidence |

### Input reconciliation

| Input | Test | Result |
|---|---|---|
| Balance sheet | $140,000,000 + $380,000,000 | **Ties** to $520,000,000 in assets |
| Accruals | -$410,000,000 - (-$190,000,000) | **Ties** to -$220,000,000 |
| Sloan accrual, 0.165 | -$220,000,000 / $520,000,000 = **-0.4231** | **Fails** on sign and size; matching 0.165 would require a $1.33B denominator |
| Beneish M-Score, 3.12 | Requires ratios that appear undefined for a pre-revenue issuer | **Unverified** |
| Dechow "F-Score Logit," 0.789 | As a logit, implies a 68.76% probability and a scaled F-Score of about 185.8; as a scaled F-Score, implies below-normal risk | **Ambiguous** |
| ASC 606 distortion, $25,000,000 | Conflicts with my recollection of no revenue in FY2020â€“21 | **Unsupported** |
| Accession no. 0001759546-21-000031 | A 2021 accession can't be the FY2021 10-K, while the -$410M loss resembles FY2021 | **Possible period mismatch** |
| Z3 result, "SAT" | No formula was supplied; SAT shows only that constraints can be satisfied | **Not a proof** |

The $25,000,000 figure is also close to the roughly $25.5M SEC settlement I recall. Check whether a settlement amount was mislabeled as a revenue distortion.

## 2. Core Forensic Anomaly Decomposition

The prior-year and line-item data needed for a Beneish decomposition were not supplied. Only TATA can be calculated.

| Component | Weight | Status | Forensic reading |
|---|---:|---|---|
| **DSRI** | +0.920 | Not computable; undefined with zero revenue | No receivables-to-sales signal |
| **GMI** | +0.528 | Not computable; undefined with zero revenue | No meaningful margin trend |
| **AQI** | +0.404 | Not computable | Needs current and prior asset detail |
| **SGI** | +0.892 | Not computable; undefined with zero revenue | Pre-orders are not sales |
| **DEPI** | +0.115 | Not computable | Needs depreciation and PP&E |
| **SGAI** | -0.172 | Not computable; undefined with zero revenue | Needs SG&A and sales |
| **LVGI** | -0.327 | Not computable | Needs prior-year leverage |
| **TATA** | +4.679 | **-0.4231**, contributing **-1.9796** | Lowers the M-Score |

- **Sensitivity:** With the other seven ratios at a neutral 1.0, M = -4.84 + 2.36 - 1.9796 = **-4.4596**. Reaching 3.12 would require those weighted terms to total **9.9396** rather than 2.36.
- **Accruals:** Negative accruals here mean the net loss exceeded operating cash burn. Without a breakdown of the -$220M, they do not show income inflation.
- **Revenue recognition:** Non-binding pre-orders would generally fail the ASC 606-10-25-1 contract criteria, including commitment and probable collection. That points to a disclosure problem rather than a cutoff error.
- **Restatement label:** I recall the 2021 restatement concerning SPAC warrant accounting, not pre-orders. If confirmed, `sec_accounting_restatement` may conflate two separate issues.

## 3. Statutory & Commercial Recovery Basis

| Basis | Key requirement | Application to this record |
|---|---|---|
| **15 U.S.C. Â§ 78j(b) / Rule 10b-5** | Actionable statement, scienter, reliance, purchase or sale, loss causation, and damages | Only plausible theory, but no eligible claimant or damages model is identified |
| **Reg. S-K Item 303, 17 C.F.R. Â§ 229.303** | Disclosure of known trends and uncertainties | Pure omissions are not actionable under Rule 10b-5(b), though half-truths can be |
| **UCC Â§ 2-717** | Buyer deducts damages from the price due under the same contract | No contract or unpaid price is shown |
| **UCC Â§ 2-305** | Parties intended a contract despite an open price | Non-binding pre-orders cut against this; see Â§ 2-305(4) |
| **19 U.S.C. Â§ 1313** | Eligible duty-paid goods, qualifying export or destruction, and a timely claim | No import, export, or duty records are provided |
| **Tax code** | Identified taxpayer, loss, and tax position | No tax return or net operating loss data is provided, so no recovery can be calculated |

### Threshold barriers

1. **Standing:** Private Rule 10b-5 plaintiffs must have bought or sold the security. *Blue Chip Stamps v. Manor Drug Stores*, 421 U.S. 723 (1975).
2. **Pleading and causation:** A claim must meet the scienter and loss-causation standards in *Tellabs*, 551 U.S. 308 (2007), and *Dura*, 544 U.S. 336 (2005).
3. **Item 303:** *Macquarie Infrastructure Corp. v. Moab Partners*, 601 U.S. 257 (2024), limits omission-based claims.
4. **Timeliness:** 28 U.S.C. Â§ 1658(b) sets a two-year discovery period and five-year repose period. Statements from 2020 through mid-2021 appear outside repose as of November 4, 2026. Each statement date needs checking.
5. **Bankruptcy:** Check the Chapter 11 plan, bar dates, releases, and injunctions, along with 11 U.S.C. Â§Â§ 362, 510(b), 524, and 1141. Also check whether the claimant is covered by a prior class settlement or release.

**Conclusion:** The supported claim value is **$0.00**. Commercial setoff, open-price, and duty-drawback theories don't fit this record.

## 4. Executable Z3 SMT Counterexample Proof

For each claim, the script tests whether its negation can hold. `unsat` proves the claim under the stated premises. The final check returns `sat` to show why a bare SAT result proves little.

```python
#!/usr/bin/env python3
"""Requires: pip install z3-solver"""
import sys
from z3 import *

A, L, E, NI, CFO, ACC = Reals("A L E NI CFO ACC")
FACTS = [
    A == 520000000,
    L == 140000000,
    E == 380000000,
    NI == -410000000,
    CFO == -190000000,
    ACC == -220000000,
]

DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI = Reals(
    "DSRI GMI AQI SGI DEPI SGAI LVGI"
)
RATIOS = [DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI]
TATA = ACC / A
M = (
    Q(-484, 100)
    + Q(92, 100) * DSRI
    + Q(528, 1000) * GMI
    + Q(404, 1000) * AQI
    + Q(892, 1000) * SGI
    + Q(115, 1000) * DEPI
    - Q(172, 1000) * SGAI
    + Q(4679, 1000) * TATA
    - Q(327, 1000) * LVGI
)


def prove(label, premises, claim):
    solver = Solver()
    solver.add(premises)
    solver.add(Not(claim))
    result = solver.check()
    passed = result == unsat
    print(f"{label}: {result} -> {'PROVED' if passed else 'FAILED'}")
    return passed


checks = []

# 1. Balance sheet identity
checks.append(prove("balance_sheet", FACTS, A == L + E))

# 2. Accrual identity
checks.append(prove("accrual_identity", FACTS, ACC == NI - CFO))

# 3. Reported Sloan value does not match period-end assets
sloan = ACC / A
checks.append(prove(
    "sloan_mismatch",
    FACTS,
    And(sloan != Q(165, 1000), sloan != Q(-165, 1000)),
))

# 4. M-Score cannot reach 3.12 with all ratios in an illustrative band
band = [And(r >= Q(1, 2), r <= 2) for r in RATIOS]
checks.append(prove("m_score_band", FACTS + band, M <= Q(-135, 100)))

# 5. ASSUMPTION: revenue was zero; must be confirmed from the filing
REV, DIST = Reals("REV DIST")
checks.append(prove(
    "cutoff_bound",
    [REV == 0, DIST >= 0, DIST <= REV],
    DIST != 25000000,
))

# 6. Restates the record's missing predicates; not independent evidence
has_setoff, has_drawback = Bools("has_setoff has_drawback")
RECOVERY, AMOUNT = Reals("RECOVERY AMOUNT")
checks.append(prove(
    "recovery_zero",
    [
        Not(has_setoff),
        Not(has_drawback),
        RECOVERY == If(Or(has_setoff, has_drawback), AMOUNT, RealVal(0)),
    ],
    RECOVERY == 0,
))

# 7. SAT witness: 3.12 is reachable if ratios are otherwise unconstrained
witness = Solver()
witness.add(FACTS)
witness.add([r >= 0 for r in RATIOS])
witness.add(M == Q(312, 100))
witness_result = witness.check()
print(f"m_score_witness: {witness_result}")
if witness_result == sat:
    print(witness.model())
checks.append(witness_result == sat)

sys.exit(0 if all(checks) else 1)
```

### Expected results (derived by hand, not executed)

| Check | Expected | Meaning |
|---|---|---|
| `balance_sheet` | `unsat`, PROVED | Assets equal liabilities plus equity |
| `accrual_identity` | `unsat`, PROVED | Accruals equal net income minus CFO |
| `sloan_mismatch` | `unsat`, PROVED | -11/26 does not equal Â±0.165 |
| `m_score_band` | `unsat`, PROVED | Maximum M is -1.3511 when all ratios fall within the illustrative 0.5â€“2.0 band |
| `cutoff_bound` | `unsat`, PROVED | $25M cannot be a revenue overstatement if recognized revenue was zero |
| `recovery_zero` | `unsat`, PROVED | Recovery is $0 given the missing predicates; this restates the inputs |
| `m_score_witness` | `sat` | The formula can reach 3.12, but that doesn't validate the score |

## 5. Actionable Legal Remediation & Demand Notice Template

**Do not send this notice as a demand.** A notice demanding payment needs a real claimant and a calculated amount, and it could create risk if the claim is discharged or enjoined. A 10-day cure period also has no evident basis because a past misstatement is not a curable commercial breach. The template therefore uses a 10-day response period.

### Required before use

- [ ] Claimant identified, with trade or contract records
- [ ] Damages calculated from those records
- [ ] Limitations and repose cleared for each statement
- [ ] Chapter 11 plan, bar dates, releases, injunctions, and prior class settlements reviewed
- [ ] Correct recipient and notice address confirmed
- [ ] Counsel approval obtained

### Template

> **DRAFT: NOT FOR DELIVERY UNTIL CLEARED BY COUNSEL**
>
> **Date:** [DATE]
> **To:** [VERIFIED SUCCESSOR ENTITY / PLAN ADMINISTRATOR], Attn: [LEGAL DEPARTMENT], [VERIFIED ADDRESS]
> **From:** [CLAIMANT OR COUNSEL OF RECORD]
> **Re:** Notice of Potential Claim and Preservation Request, Lordstown Motors Corp (CIK 0001759546)
>
> [CLAIMANT] writes regarding statements about commercial fleet pre-orders made on [DATES] in [DOCUMENTS]. [CLAIMANT] [purchased/sold] [SECURITY] on [DATES], as shown in Exhibit A.
>
> **Claim calculation**
>
> | Element | Amount |
> |---|---:|
> | Documented out-of-pocket loss | $[AMOUNT] |
> | Offsets and prior recoveries | $([AMOUNT]) |
> | **Net claimed amount** | **$[AMOUNT]** |
>
> **Requested response.** Within ten (10) calendar days of receipt, please: (1) state whether the claim is disputed or subject to a bankruptcy plan, release, or injunction; (2) identify the proper claims contact; and (3) confirm that relevant records are being preserved, including pre-order agreements, customer communications, and investor materials.
>
> This notice is not intended to violate any automatic stay, discharge, or plan injunction. If any such provision applies, please identify it and treat this letter as an inquiry only. All rights and defenses are reserved.
>
> [SIGNATURE]
> [NAME, FIRM, ADDRESS, PHONE, EMAIL]

The signature block is blank because the record does not identify John Webb or John Webb & Co. as a claimant or counsel.

## 6. Verification & Chain of Custody

| Control | Status | Evidence |
|---|---|---|
| **Source filing** | Not retrieved | Accession number is unverified against EDGAR |
| **SHA-256 integrity** | Not computed | No source bytes were available, and no hash has been invented |
| **DuckDB 2.0.0 LTS** | Not run | Schema below is proposed; version is unverified |
| **Z3 proof** | Not run | Script and expected results are unexecuted |
| **TruLens RAG triad** | Not evaluated | Context relevance, groundedness, and answer relevance have no scores |
| **Legal citations** | Not cite-checked | Written from memory |

To hash the filing and proof script once saved:

```powershell
Get-FileHash -Algorithm SHA256 .\source_filing.htm, .\z3_proof.py
```

### Proposed DuckDB schema

```sql
CREATE TABLE evidence_artifact (
    artifact_id      VARCHAR PRIMARY KEY,
    case_id          VARCHAR NOT NULL,
    accession_number VARCHAR,
    source_url       VARCHAR,
    retrieved_at     TIMESTAMPTZ,
    sha256           VARCHAR CHECK (sha256 IS NULL OR length(sha256) = 64),
    custodian        VARCHAR
);

CREATE TABLE filer_financials (
    case_id        VARCHAR NOT NULL,
    cik            VARCHAR NOT NULL,
    fiscal_period  VARCHAR NOT NULL,
    assets         DECIMAL(18,2) NOT NULL,
    liabilities    DECIMAL(18,2) NOT NULL,
    equity         DECIMAL(18,2) NOT NULL,
    net_income     DECIMAL(18,2) NOT NULL,
    cfo            DECIMAL(18,2) NOT NULL,
    accruals       DECIMAL(18,2) NOT NULL,
    source_artifact_id VARCHAR REFERENCES evidence_artifact(artifact_id),
    PRIMARY KEY (case_id, fiscal_period),
    CHECK (assets = liabilities + equity),
    CHECK (accruals = net_income - cfo)
);

CREATE TABLE verification_run (
    run_id        VARCHAR PRIMARY KEY,
    case_id       VARCHAR NOT NULL,
    tool          VARCHAR NOT NULL,
    tool_version  VARCHAR NOT NULL,
    check_name    VARCHAR NOT NULL,
    result        VARCHAR NOT NULL,
    run_at        TIMESTAMPTZ NOT NULL,
    output_sha256 VARCHAR CHECK (output_sha256 IS NULL OR length(output_sha256) = 64)
);
```

### Release gates

1. Pull the filing and confirm its form type and fiscal period.
2. Rebuild the financial inputs and recalculate the Beneish, Dechow, and Sloan metrics from source data.
3. Remove the ASC 606 figure unless recognized revenue and a cutoff error can be documented.
4. Run the Z3 script and record its version, output, and hashes.
5. Run TruLens against the retrieved source set, if RAG was used.
6. Have counsel cite-check the dossier and confirm the claimant, time bars, and bankruptcy position.