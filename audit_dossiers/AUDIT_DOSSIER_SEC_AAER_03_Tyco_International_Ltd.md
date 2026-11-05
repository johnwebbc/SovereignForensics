# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Tyco International Ltd

**Case ID:** SEC_AAER_03 | **CIK:** 0000833444 | **Status:** Draft, not publication-ready

> **Key findings**
> - **Recovery:** The record supports **$0.00**, and I found no viable claim. The notice in Section 5 is on hold and shouldn't be sent as it stands.
> - **Input conflicts:** The balance sheet and accrual arithmetic tie, but the Sloan value conflicts with the accruals. The M-score and $500M cutoff figure are also unsupported.
> - **Verification:** The Z3 script hasn't been run. I didn't access the filing, compute hashes, or run DuckDB or TruLens.
> - **Sources:** Case history and legal citations are from memory, so check them against primary sources.
> - **Authorship:** Claude prepared this, not legal counsel or the requested Muse Glimmer stack. It isn't legal advice.

## 1. Executive Summary & Exposure Classification

The arithmetic checks support only limited conclusions about the supplied FY2002-style figures. They don't prove misconduct, which comes from the enforcement and criminal record.

| Item | Classification | Basis |
|---|---|---|
| **Immediate financial impact** | **$0.00 recoverable** | The input shows $0.00 recovery and a null waterfall |
| **Likelihood of recovery** | **Remote** | No claimant or contract, no private right under Â§ 78m(b)(2), and likely time bars |
| **Legal exposure** | **Historical, apparently resolved** | SEC, criminal, and class proceedings concluded years ago |
| **$500M "ASC 606" distortion** | **Excluded** | No support supplied, and ASC 606 postdates these periods |

### Input reconciliation

| Test | Result | Finding |
|---|---|---|
| Assets = liabilities + equity | $41.24B + $23.65B = $64.89B | Ties, with no separate minority interest line |
| Accruals = net income âˆ’ CFO | âˆ’$9.41B âˆ’ $4.82B = âˆ’$14.23B | Ties |
| Sloan on year-end assets | âˆ’$14.23B / $64.89B = **âˆ’0.2193** | Conflicts with +0.218 in sign and differs in magnitude |
| Sloan denominator | $14.23B / 0.218 = about $65.28B | Could reflect average assets, but the prior-year balance is missing |
| M-score of +3.75 | Requires extreme index values | Unsupported, and the sign may have been dropped |
| F-score "logit" of 0.884 | Implies P = 70.8%, or about 191 times a 0.37% base rate | Probably mislabeled; if it's a scaled F-score, it is below the 1.0 baseline |
| Accounting framework | ASC 805 and ASC 606 | Anachronistic for 1999â€“2002; review APB 16, SFAS 141, EITF 95-3, and period revenue guidance |
| Accession number | 0000950123-03-000843 | Not verified; confirm the form type and period on EDGAR |

### Historical record (verify)

- **SEC v. Tyco (S.D.N.Y. 2006):** Tyco reportedly settled allegations involving at least $1B of overstated operating income, including acquisition accounting, and paid a $50M penalty.
- **New York criminal case:** Kozlowski and Swartz were convicted in 2005 of grand larceny and related charges tied to about $150M, including unauthorized compensation and loan forgiveness.
- ***In re Tyco* (D.N.H.):** The securities class action settled for about $2.975B, plus $225M from PwC.

## 2. Core Forensic Anomaly Decomposition

**None of the eight components can be calculated from this record.** The Beneish model needs two years of line items, and only one partial year was supplied. I haven't estimated the missing values.

**Model:** M = âˆ’4.84 + 0.920 DSRI + 0.528 GMI + 0.404 AQI + 0.892 SGI + 0.115 DEPI âˆ’ 0.172 SGAI + 4.679 TATA âˆ’ 0.327 LVGI

| Index | Status | Data needed | Relevance to acquisition reserves |
|---|---|---|---|
| **DSRI** | Not computable | Receivables, sales | Acquired receivables can distort the ratio |
| **GMI** | Not computable | Sales, COGS | Reserve releases can lift margins and make GMI look less risky |
| **AQI** | Not computable | Current assets, PP&E, total assets | Goodwill can raise it mechanically for a serial acquirer |
| **SGI** | Not computable | Sales | Acquired revenue can look like growth |
| **DEPI** | Not computable | Depreciation, PP&E | Low acquired-asset values can reduce depreciation |
| **SGAI** | Not computable | SG&A, sales | Releases through SG&A can lower the index |
| **LVGI** | Not computable | Debt, total assets | Acquisition debt can raise leverage without manipulation |
| **TATA** | Proxy only | Full balance sheet data | Cash-flow proxy: âˆ’0.2193, contributing âˆ’1.026 to M |

### What +3.75 would require

With the other seven indices at a neutral 1.0 and TATA at âˆ’0.2193, M equals âˆ’3.51. Reaching +3.75 therefore requires another 7.256 points:

| Sole index moved | Required value | Assessment |
|---|---|---|
| DSRI | 8.89 | Extreme |
| SGI | 9.13 | Extreme |
| GMI | 14.74 | Extreme |
| AQI | 18.96 | Extreme |
| DEPI | 64.10 | Extreme |
| SGAI | âˆ’41.19 | Impossible for a ratio of positive values |
| LVGI | âˆ’21.19 | Impossible for a ratio of positive values |

Several indices could move together, so +3.75 isn't mathematically impossible. It can't be relied on without the workpaper, though. **A value of âˆ’3.75 would sit closer to the âˆ’3.51 neutral case and would not signal manipulation.** That is only a hypothesis, but the Sloan value also appears to have lost its negative sign, so check the source pipeline.

### Accounting distortion

Spring-loading works by shifting earnings across the acquisition date:

1. **Before closing:** The target accelerates expenses or defers revenue.
2. **At closing:** The acquirer undervalues assets, overstates liabilities, or records excess reserves, which increases goodwill.
3. **After closing:** Reserves are released, or deferred revenue is recognized, which lifts reported results.

**The test period is also a problem.** A âˆ’$14.23B accrual is strongly income-decreasing and fits a year dominated by large non-cash charges, such as the CIT loss. It doesn't show the earlier income-increasing pattern that spring-loading would create, so the testing should focus on FY1999â€“FY2001 acquisition cohorts.

The loan issue is separate. Testing it requires forgiveness amounts, approvals, compensation expense, tax treatment, and related-party and executive compensation disclosures.

## 3. Statutory & Commercial Recovery Basis

| Authority | Applies? | Analysis |
|---|---|---|
| **UCC Â§ 2-717** | No | Requires a buyer deducting damages from the price due under the same contract; none is in the record |
| **UCC Â§ 2-305** | No | Addresses open-price sale contracts; none is in the record |
| **19 U.S.C. Â§ 1313** | No | Requires qualifying imports, duties, and export or destruction facts; none is in the record |
| **Tax code** | No basis shown | No overpayment, return, or refund claim is supplied; IRC Â§ 6511 would also impose time limits |
| **15 U.S.C. Â§ 78m(b)(2)** | Enforcement only | Sets books-and-records and internal-control duties; courts have generally found no private right of action (see *Eisenberger v. Spectex Indus.*, E.D.N.Y. 1986) |
| **15 U.S.C. Â§ 78j(b) / Rule 10b-5** | Unlikely | The private route, but it requires a purchaser or seller, scienter, reliance, and loss, and faces the class settlement and time limits |
| **28 U.S.C. Â§ 1658(b)** | Barrier | Two-year discovery period and five-year repose for private securities fraud claims |
| **28 U.S.C. Â§ 2462** | Barrier | Five-year limit on many government penalty claims |
| **15 U.S.C. Â§ 78m(k)** | Unlikely | SOX executive-loan ban took effect in 2002 and doesn't reach earlier loans retroactively |
| **ASC 805** | Not a claim | An accounting standard that creates no cause of action, and it postdates the conduct as a codification |

**Recovery calculation**

| Component | Amount |
|---|---|
| Documented eligible claims | $0.00 |
| Offsets, duties, or tax refunds | $0.00 |
| **Supported recovery** | **$0.00** |
| Waterfall | Not applicable; the input is null |

CIK 833444 now appears to belong to Johnson Controls International plc after the 2016 merger. Counsel would also need to review successor liability, including the Covidien and TE Connectivity separations.

## 4. Executable Z3 SMT Counterexample Proof

This script tests whether the inputs are internally consistent. **It doesn't prove fraud, liability, or recoverability.** In particular, the supplied "SAT" label can only mean that a set of constraints is satisfiable.

```python
#!/usr/bin/env python3
"""SEC_AAER_03 input-consistency checks. Requires: pip install z3-solver"""
import math
import sys

from z3 import *

ASSETS = 64_890_000_000
LIABILITIES = 41_240_000_000
EQUITY = 23_650_000_000
NET_INCOME = -9_410_000_000
OPERATING_CASH_FLOW = 4_820_000_000
ACCRUALS = -14_230_000_000
SLOAN_INPUT = Q(218, 1000)
M_INPUT = Q(375, 100)

COEFFICIENTS = {
    "DSRI": Q(920, 1000),
    "GMI": Q(528, 1000),
    "AQI": Q(404, 1000),
    "SGI": Q(892, 1000),
    "DEPI": Q(115, 1000),
    "SGAI": Q(-172, 1000),
    "LVGI": Q(-327, 1000),
}
NEGATIVE_ONLY = {"SGAI", "LVGI"}
results = []


def record(name, passed):
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}")


def holds(claim, *premises):
    solver = Solver()
    solver.add(*premises)
    solver.add(Not(claim))
    return solver.check() == unsat


def infeasible(*constraints):
    solver = Solver()
    solver.add(*constraints)
    return solver.check() == unsat


a, l, e, ni, cfo, acc = Reals("a l e ni cfo acc")
facts = [
    a == ASSETS,
    l == LIABILITIES,
    e == EQUITY,
    ni == NET_INCOME,
    cfo == OPERATING_CASH_FLOW,
    acc == ACCRUALS,
]
record("Assets = liabilities + equity", holds(a == l + e, *facts))
record("Accruals = net income - CFO", holds(acc == ni - cfo, *facts))

denominator = Real("denominator")
record(
    "Sloan +0.218 is impossible with negative accruals and a positive denominator",
    infeasible(denominator > 0, SLOAN_INPUT * denominator == ACCRUALS),
)

year_end_sloan = Real("year_end_sloan")
record(
    "Year-end Sloan is between -0.2194 and -0.2192",
    holds(
        And(year_end_sloan > Q(-2194, 10000), year_end_sloan < Q(-2192, 10000)),
        year_end_sloan * ASSETS == ACCRUALS,
    ),
)

indices = {name: Real(name) for name in COEFFICIENTS}
tata = Q(ACCRUALS, ASSETS)
m_score = (
    Q(-484, 100)
    + Sum([COEFFICIENTS[name] * indices[name] for name in COEFFICIENTS])
    + Q(4679, 1000) * tata
)

neutral = [indices[name] == 1 for name in COEFFICIENTS]
record("M = 3.75 is impossible at neutral indices", infeasible(*neutral, m_score == M_INPUT))

for name in COEFFICIENTS:
    solver = Solver()
    solver.add(*[indices[other] == 1 for other in COEFFICIENTS if other != name])
    solver.add(indices[name] >= 0, m_score == M_INPUT)
    outcome = solver.check()
    expected = unsat if name in NEGATIVE_ONLY else sat
    record(f"{name}-only route to M = 3.75 is {expected}", outcome == expected)
    if outcome == sat:
        print(f"      required {name} = {solver.model()[indices[name]].as_decimal(4)}")

solver = Solver()
solver.add(*[indices[name] >= 0 for name in COEFFICIENTS], m_score == M_INPUT)
record("M = 3.75 is reachable with unconstrained joint indices (not evidence)", solver.check() == sat)

recovery, eligible_basis = Reals("recovery eligible_basis")
record(
    "Recovery is zero when the documented eligible basis is zero",
    holds(recovery == 0, eligible_basis == 0, recovery >= 0, recovery <= eligible_basis),
)

probability = math.exp(0.884) / (1 + math.exp(0.884))
print(f"INFO  Logit 0.884 implies P = {probability:.4f}; ratio to 0.37% = {probability / 0.0037:.1f}")

sys.exit(0 if all(results) else 1)
```

**Expected result:** All checks should print `PASS`, and the script should exit with code 0. Expected required values are DSRI 8.8870, GMI 14.7426, AQI 18.9606, SGI 9.1346, and DEPI 64.0963. These come from hand calculation, not an actual run.

## 5. Actionable Legal Remediation & Demand Notice Template

**Recommended remediation**
1. Don't send a monetary demand on this record.
2. Fix the Sloan sign, M-score inputs, F-score label, and period-appropriate accounting references.
3. Pull the original filing, restatement materials, SEC papers, and class settlement documents.
4. Have counsel confirm whether a claimant exists, whether the class release applies, and whether any claim is timely.

The template below contains no evidence-backed claim. I left the signature block open because the record doesn't show John Webb & Co. as a claimant.

> **HOLD: DO NOT SEND. For counsel review only. Requires an identified claimant, a valid legal basis, and a supported amount.**
>
> **[DATE]**
> **Via [DELIVERY METHOD]**
>
> **To:** [CONFIRMED LEGAL SUCCESSOR]
> Attn: General Counsel
> [CONFIRMED NOTICE ADDRESS]
>
> **Re: Notice of Claim and Demand for Cure, [CLAIM REFERENCE]**
>
> Dear General Counsel:
>
> [CLAIMANT] submits this notice under [CONTRACT, STATUTE, OR OTHER COUNSEL-CONFIRMED BASIS].
>
> **Factual basis:** [DATED FACTS, WITH DOCUMENT REFERENCES]
>
> **Claim calculation:**
>
> | Component | Source | Amount |
> |---|---|---|
> | [COMPONENT] | [SOURCE DOCUMENT] | $[AMOUNT] |
> | **Total on the current record** | | **$0.00** |
>
> **Demand:** Within ten (10) calendar days of receipt, please [SPECIFIC CURE ACTION OR PAYMENT].
>
> **Records:** Please preserve documents reasonably related to this matter, including [CATEGORIES].
>
> [CLAIMANT] reserves all rights and remedies available under applicable law. Nothing in this notice waives any right, privilege, or defense.
>
> Sincerely,
>
> [AUTHORIZED SIGNATORY OR COUNSEL OF RECORD]
> [TITLE, ORGANIZATION, AND CONTACT DETAILS]

## 6. Verification & Chain of Custody

| Control | Status | Required action |
|---|---|---|
| **SHA-256 integrity** | Not computed | Hash each original source file and the final dossier |
| **Source filing** | Not retrieved | Confirm the accession number, form, period, and figures on EDGAR |
| **Z3** | Not run | Run Section 4 and retain the console output and package version |
| **DuckDB 2.0.0 LTS** | Not verified or run | Confirm the installed version, then load the schema |
| **TruLens RAG triad** | Not run; no scores exist | Evaluate after a source corpus and retrieval pipeline exist |

**Hash command (PowerShell):**

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "<path-to-source-file>"
```

**DuckDB schema:**

```sql
CREATE TABLE IF NOT EXISTS evidence_custody (
    evidence_id       VARCHAR PRIMARY KEY,
    case_id           VARCHAR NOT NULL,
    source_url        VARCHAR,
    accession_number  VARCHAR,
    local_path        VARCHAR NOT NULL,
    sha256            VARCHAR NOT NULL CHECK (length(sha256) = 64),
    retrieved_at      TIMESTAMPTZ NOT NULL,
    retrieved_by      VARCHAR NOT NULL,
    notes             VARCHAR
);

CREATE TABLE IF NOT EXISTS metric_verification (
    case_id           VARCHAR NOT NULL,
    metric_name       VARCHAR NOT NULL,
    supplied_value    DECIMAL(24, 6),
    recomputed_value  DECIMAL(24, 6),
    status            VARCHAR NOT NULL CHECK (
        status IN ('VERIFIED', 'CONFLICT', 'UNSUPPORTED', 'NOT_RUN')
    ),
    evidence_id       VARCHAR REFERENCES evidence_custody (evidence_id),
    verified_at       TIMESTAMPTZ,
    PRIMARY KEY (case_id, metric_name)
);
```

**Current metric status**

| Metric | Supplied | Recomputed | Status |
|---|---|---|---|
| Balance sheet equation | $64.89B | $64.89B | Internally consistent; source not verified |
| Accruals | âˆ’$14.23B | âˆ’$14.23B | Internally consistent; source not verified |
| Sloan accrual | +0.218 | âˆ’0.2193 on year-end assets | Conflict |
| Beneish M-score | +3.75 | Not computable | Unsupported |
| Dechow F-score | 0.884 | Depends on the label | Unsupported |
| Cutoff distortion | $500,000,000 | Not computable | Unsupported |
| Statutory recovery | $0.00 | $0.00 on the current record | Consistent with the record, but legal review is still needed |

**Release gate:** This dossier shouldn't be published or described as verified until the source figures are tied to the filing, the script output is retained, the file hashes are recorded, and counsel has checked the legal citations.