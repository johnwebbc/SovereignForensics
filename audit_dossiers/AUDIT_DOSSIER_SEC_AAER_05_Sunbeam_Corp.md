# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Sunbeam Corp

**Status: analytical draft, not publication-ready and not for delivery.** No filing or database was accessed, and the Z3 script, hashes, and TruLens checks were not run. Historical facts marked **[recall]** come from memory and need checking against primary sources. This draft requires review by a licensed attorney and a CPA.

## 1. Executive Summary & Exposure Classification

**Conclusion:** The supplied data supports a historical accounting-fraud case study, but not a recovery action. There is no identified claimant, contract, unpaid invoice, duty payment, or calculable claim, so the demand notice in Section 5 should not be sent.

| Classification | Assessment | Basis |
|---|---|---|
| **Immediate financial impact** | **$0.00 recoverable** | Supplied recovery is $0.00 and the waterfall is null. The $62,000,000 cutoff distortion is a reporting measure, not damages. |
| **Likelihood of recovery** | **Remote on the current record** | No claimant or legal basis has been identified, and the events are roughly 28 years old. |
| **Legal exposure: Sunbeam-era conduct** | **High historically, largely resolved** | SEC enforcement, shareholder litigation, and Chapter 11 appear to have run their course **[recall]**. |
| **Legal exposure: sender of a new demand** | **Material** | Risks include an unsupported claim, misidentifying the successor, and defamation. |

### Reconciliation of supplied inputs

| Check | Calculation | Result |
|---|---|---|
| Balance sheet | $2,210,000,000 + $630,000,000 | **Ties** to $2,840,000,000 |
| Accruals | -$710,000,000 - (-$118,000,000) | **Ties** to -$592,000,000 |
| Return on assets | -$710,000,000 / $2,840,000,000 | **-25.00%** |
| Non-cash share of net loss | $592,000,000 / $710,000,000 | **83.38%** |
| Leverage | $2,210,000,000 / $2,840,000,000 | **77.82%** liabilities to assets; 3.51x liabilities to equity |
| Sloan accrual ratio | -$592,000,000 / $2,840,000,000 | **-0.2085; does not tie** to the supplied 0.245 |
| Cutoff distortion | $62,000,000 against assets, equity, and net loss | **2.18%, 9.84%, and 8.73%** respectively |

### Data defects to resolve

1. **Sloan sign and size:** With negative accruals and a positive denominator, the ratio cannot be +0.245. An absolute value of 0.245 implies a denominator of $2,416,326,530.61, or opening assets of $1,992,653,061.22 if average assets were used.
2. **Filing period:** No fiscal year is given, and the accession number indicates a 1998 filing. A 1998 filing could not contain full-year FY1998 results, while a -$710,000,000 result does not match my recollection of restated FY1997 net income of about +$38.3M **[recall]**.
3. **Financial values:** I recall a 1998 net loss of about $898M and total assets of about $3.4B, which conflict with the supplied -$710M and $2.84B **[recall]**.
4. **Anachronistic standard:** ASC 606 took effect for public companies in annual periods beginning after December 15, 2017. It can serve as a modern comparison, but it did not govern Sunbeam's 1996â€“1998 accounting.
5. **Dechow F-Score:** The label "0.897 logit" has conflicting readings:
   - As a logit, it implies p = 0.7103 and F â‰ˆ 192.0.
   - As a probability, it implies F â‰ˆ 242.4.
   - As a scaled F-Score, it falls below the 1.00 baseline, indicating below-average risk.
6. **Identifiers:** The CIK and accession number are unverified, and `SEC_AAER_05` is not an SEC release number.
7. **Z3 field:** "SAT" is a solver result, not a formula. Its meaning depends on the assertion tested, so Section 4 states each one explicitly.

## 2. Core Forensic Anomaly Decomposition

The supplied M-Score of 3.91 cannot be decomposed because no two-year inputs were provided. The component values below are therefore left uncalculated rather than estimated.

The standard eight-variable model is:

`M = -4.84 + 0.920Â·DSRI + 0.528Â·GMI + 0.404Â·AQI + 0.892Â·SGI + 0.115Â·DEPI - 0.172Â·SGAI + 4.679Â·TATA - 0.327Â·LVGI`

Using signed TATA of -0.2085, its contribution is **-0.9753**. To reach 3.91, the other seven terms must total **9.7253**, compared with 2.3600 if every index equals 1.00. That leaves an excess of **7.3653**.

| Component | Reported value | Break-even if it alone explains the excess | Distortion to test |
|---|---|---|---|
| **DSRI** | Not computable | 9.01 | Bill-and-hold sales and extended terms inflate receivables relative to revenue. |
| **GMI** | Not computable | 14.95 | Reserve releases or misclassified costs can mask margin deterioration. |
| **AQI** | Not computable | 19.23 | 1998 acquisition goodwill may drive this mechanically **[recall]**. |
| **SGI** | Not computable | 9.26 | Pull-forward sales and acquired revenue can both inflate growth. |
| **DEPI** | Not computable | 65.05 | Restructuring write-downs can alter depreciation rates. |
| **SGAI** | Not computable | Impossible (-41.82) | Reserve releases can reduce SG&A, while the negative coefficient lowers M as SGAI rises. |
| **LVGI** | Not computable | Impossible (-21.52) | Acquisition debt raises LVGI, which also lowers M. |
| **TATA** | **-0.2085** from supplied data | Not applicable | Large non-cash charges drive the negative value and reduce M. |

### What the score can and cannot show

- **Implausibly large result:** If all seven indices stay within an illustrative 0â€“3 range, their maximum contribution is 8.577, below the 9.7253 required. The supplied M-Score therefore needs extreme inputs or a positive TATA. With TATA of +0.245, the requirement drops to 7.6036, which fits within that range.
- **Possible wrong period:** The alleged manipulation ran from about Q4 1996 through Q1 1998 **[recall]**. A score based on a later loss year may reflect write-offs and acquisitions more than the original misstatement.
- **Acquisition noise:** The 1998 acquisitions of Coleman, First Alert, and Signature Brands **[recall]** can distort AQI, SGI, and LVGI. A pro forma calculation would be needed to separate those effects.

### Accounting mechanisms

- **Bill-and-hold sales:** Revenue was allegedly recognized on goods that stayed under seller control or lacked a substantive customer-driven reason for the arrangement. The result would be overstated current-period revenue and receivables, followed by weaker later sales.
- **Cookie-jar reserves:** Excess restructuring reserves reduce income in the charge year, and later releases raise income without any operating improvement. This pattern can make a turnaround look stronger than it was.
- **Accelerated rebates and pull-forwards:** Incentives can shift future demand into the current period. Under-accruing rebates or returns would further overstate net revenue. The supplied record has no rebate schedule to test this.

### Governing standards

| Issue | Period standard | Modern comparison |
|---|---|---|
| Bill-and-hold | AAER No. 108 criteria **[recall]** | ASC 606-10-55-81 to 55-84 |
| Rebates and returns | SFAS 48 and revenue-recognition guidance of the period **[recall]** | ASC 606-10-32-5 to 32-9; 55-22 to 55-29 |
| Restructuring reserves | EITF 94-3 and SFAS 5 **[recall]** | ASC 420; ASC 450-20 |

## 3. Statutory & Commercial Recovery Basis

| Basis | Required elements | Application | Result |
|---|---|---|---|
| **UCC Â§ 2-717** | A buyer, damages from a breach, notice to the seller, and price still due under the same contract | No buyer, breach, or open invoice is identified. | **Not available** |
| **UCC Â§ 2-305** | A contract with an open or unsettled price term | Bill-and-hold and reserve issues are not open-price disputes, and no contract is supplied. | **Not available** |
| **19 U.S.C. Â§ 1313** | Duty-paid imports, a qualifying export or destruction, a proper claimant, and a timely claim | The record contains no entries, duties, or exports, and the general filing window is five years from import. | **Not available** |
| **Tax refund (IRC Â§Â§ 6511, 172)** | A taxpayer with standing, a refundable overpayment, and an open period | No taxpayer or return is identified, and the 1990s periods are presumptively closed. | **Not available** |
| **Securities claim (Exchange Act Â§ 10(b); Rule 10b-5)** | A purchaser or seller, scienter, reliance, loss causation, and a timely claim | 28 U.S.C. Â§ 1658(b) sets a two-year discovery limit and five-year repose period, and class resolution may also bind claimants. | **Presumptively barred** |
| **Bankruptcy distribution** | An allowed claim and an open distribution right | The February 2001 Chapter 11 case **[recall]** and 11 U.S.C. Â§ 1141(d) may have discharged remaining claims. | **Check the docket and plan** |

**Recovery calculation:** Claim base $0.00 Ã— any recovery rate = **$0.00**. The $62,000,000 figure should not be used as a claim amount without a claimant and proof of causation and loss.

## 4. Executable Z3 SMT Counterexample Proof

The script tests whether the inputs are internally consistent and whether the distortion alone establishes a recovery. It does not prove that fraud occurred or that any party is liable.

```python
#!/usr/bin/env python3
"""Sunbeam Corp (SEC_AAER_05) arithmetic and recovery checks.
Requires: pip install z3-solver
UNSAT means the tested violation is impossible under the stated constraints.
SAT means a witness exists.
"""
import sys
from z3 import *

MM = 1_000_000
ASSETS, LIABILITIES, EQUITY = 2840 * MM, 2210 * MM, 630 * MM
NET_INCOME, CFO, ACCRUALS = -710 * MM, -118 * MM, -592 * MM
CUTOFF_DISTORTION = 62 * MM
STATUTORY_RECOVERY = 0
SLOAN_CLAIM = Q(245, 1000)
M_SCORE_CLAIM = Q(391, 100)

results = []


def run(label, expected, *constraints):
    solver = Solver()
    solver.add(*constraints)
    actual = solver.check()
    passed = actual == expected
    results.append(passed)
    print(f"[{'PASS' if passed else 'FAIL'}] {label}: "
          f"got {actual}, expected {expected}")
    if actual == sat:
        print(f"       witness: {solver.model()}")


def beneish(indices, tata):
    dsri, gmi, aqi, sgi, depi, sgai, lvgi = indices
    return (Q(-484, 100) + Q(920, 1000) * dsri + Q(528, 1000) * gmi
            + Q(404, 1000) * aqi + Q(892, 1000) * sgi
            + Q(115, 1000) * depi - Q(172, 1000) * sgai
            + Q(4679, 1000) * tata - Q(327, 1000) * lvgi)


# Identities
a, l, e = Reals("assets liabilities equity")
run("T01 balance-sheet identity can be violated", unsat,
    a == ASSETS, l == LIABILITIES, e == EQUITY, a != l + e)

ni, cfo, acc = Reals("net_income cfo accruals")
run("T02 accrual identity can be violated", unsat,
    ni == NET_INCOME, cfo == CFO, acc == ACCRUALS, acc != ni - cfo)

roa = Real("roa")
run("T03 ROA differs from -1/4", unsat,
    roa * ASSETS == NET_INCOME, roa != Q(-1, 4))

# Sloan ratio
denominator, opening_assets = Reals("denominator opening_assets")
run("T04 signed Sloan = +0.245 for a positive denominator", unsat,
    denominator > 0, SLOAN_CLAIM * denominator == ACCRUALS)
run("T05 absolute Sloan = 0.245 on ending assets", unsat,
    denominator == ASSETS, SLOAN_CLAIM * denominator == -ACCRUALS)
run("T06 absolute Sloan = 0.245 on average assets", sat,
    denominator > 0, opening_assets > 0,
    SLOAN_CLAIM * denominator == -ACCRUALS,
    (opening_assets + ASSETS) / 2 == denominator)

# Beneish M-Score feasibility
indices = Reals("DSRI GMI AQI SGI DEPI SGAI LVGI")
signed_tata = Q(ACCRUALS, ASSETS)
all_ones = [index == 1 for index in indices]
box = [And(index >= 0, index <= 3) for index in indices]

run("T07 M = 3.91 with all indices at 1 and signed TATA", unsat,
    *all_ones, beneish(indices, signed_tata) == M_SCORE_CLAIM)
run("T08 M = 3.91 with indices in [0,3] and signed TATA", unsat,
    *box, beneish(indices, signed_tata) == M_SCORE_CLAIM)
run("T09 M = 3.91 with indices in [0,3] and TATA = +0.245", sat,
    *box, beneish(indices, SLOAN_CLAIM) == M_SCORE_CLAIM)

# Recovery bound
distortion, recovery, claim_base = Reals("distortion recovery claim_base")
run("T10 counterexample: distortion does not imply recovery", sat,
    distortion == CUTOFF_DISTORTION, recovery == STATUTORY_RECOVERY,
    Not(Implies(distortion > 0, recovery > 0)))
run("T11 supplied recovery covers the distortion", unsat,
    distortion == CUTOFF_DISTORTION, recovery == STATUTORY_RECOVERY,
    recovery >= distortion)
run("T12 nonzero recovery on a zero claim base", unsat,
    claim_base == 0, recovery >= 0, recovery <= claim_base, recovery != 0)

# ASC 606-10-55-83 criteria, used as a modern comparison only
substantive_reason, identified, ready, not_redirectable = Bools(
    "substantive_reason identified ready not_redirectable")
invoiced, recognizable = Bools("invoiced recognizable")
criteria = And(substantive_reason, identified, ready, not_redirectable)
run("T13 recognizable while a criterion is missing", unsat,
    recognizable == criteria, recognizable, Not(criteria))
run("T14 counterexample: invoicing does not imply recognition", sat,
    recognizable == criteria, invoiced, Not(recognizable))

print(f"\n{sum(results)}/{len(results)} checks matched expectations")
sys.exit(0 if all(results) else 1)
```

**Expected result, derived by hand and not yet executed:** 14/14 checks should match, with exit code 0.

| Checks | Expected | Meaning |
|---|---|---|
| T01â€“T03 | UNSAT | The balance sheet, accruals, and return on assets are internally consistent. |
| T04â€“T05 | UNSAT | The Sloan figure fails as a signed ratio and as an absolute ratio on ending assets. |
| T06 | SAT | The absolute figure works only with an assumed denominator of about $2.416B. |
| T07â€“T08 | UNSAT | The M-Score is not reachable with signed TATA under the stated index assumptions. |
| T09 | SAT | It becomes reachable in the 0â€“3 range only if TATA is +0.245. |
| T10 | SAT | **Key counterexample:** a $62,000,000 distortion can coexist with $0 recovery. |
| T11â€“T12 | UNSAT | The supplied recovery can't cover the distortion, and a zero claim base caps recovery at $0. |
| T13â€“T14 | UNSAT, SAT | All four bill-and-hold criteria are required, and an invoice alone doesn't establish recognition. |

The 0â€“3 range in T08 and T09 is an illustrative assumption, not a limit set by the Beneish model.

## 5. Actionable Legal Remediation & Demand Notice Template

**Do not send this notice as written.** With no claimant, contract, or claim amount, a demand would have no factual basis. The template can be used only if counsel completes every gate below.

### Release gates

- [ ] Claimant identity and standing are documented.
- [ ] The correct legal successor is confirmed. Sunbeam later became American Household, which Jarden acquired, and Jarden later combined with Newell **[recall]**.
- [ ] The bankruptcy discharge and plan have been reviewed.
- [ ] Limitations and repose have been analyzed.
- [ ] Contract, invoices, and damages records support the claim.
- [ ] Counsel has approved the factual statements and legal theory.

### Template

```text
DRAFT â€” NOT FOR DELIVERY UNTIL ALL RELEASE GATES ARE CLEARED

[DATE]

VIA [DELIVERY METHOD REQUIRED BY CONTRACT]

[VERIFIED LEGAL ENTITY]
Attn: [REGISTERED AGENT / GENERAL COUNSEL]
[VERIFIED ADDRESS]

Re: Notice of Claim and Demand: [CONTRACT NAME AND DATE]; [INVOICE NUMBERS]

To Whom It May Concern:

[CLAIMANT] ("Claimant") gives notice of the following claim against
[RESPONDENT] ("Respondent") under [CONTRACT SECTION] and [COUNSEL-CONFIRMED
LEGAL BASIS].

1. Background. [Specific, documented facts, limited to the parties' dealings.]

2. Breach. Respondent breached [SECTION] by [SPECIFIC ACT OR OMISSION].

3. Claim calculation.
   Documented damages:             $[AMOUNT]
   Less credits and payments:     ($[AMOUNT])
   Plus contractual interest:      $[AMOUNT]
   TOTAL DEMAND:                   $[AMOUNT]
   Supporting documents are listed in Schedule A.

4. Setoff. [INCLUDE ONLY IF COUNSEL CONFIRMS A UCC Â§ 2-717 RIGHT: Claimant
   intends to deduct $[AMOUNT] from the unpaid price under the same contract.]

5. Demand and cure. Within ten (10) calendar days after receipt of this
   notice, Respondent must [PAY $[AMOUNT] / PROVIDE THE SPECIFIED CURE].

6. Preservation. Please preserve all documents and data relating to this
   matter, including [SPECIFIC CATEGORIES].

7. Reservation of rights. Claimant reserves all rights and remedies. This
   notice is not a complete statement of the facts or of Claimant's claims.

Sincerely,

[AUTHORIZED SIGNATORY]
[TITLE / ORGANIZATION]
[ADDRESS]
[VERIFIED DIRECT PHONE]

Enclosure: Schedule A â€” Claim Calculation and Supporting Documents
```

If John Webb is confirmed as the signatory, use: John Webb, Principal, John Webb & Co., Louisville, KY, 502-693-2779. The current record does not show that John Webb or John Webb & Co. has a claim.

### Recommended remediation

1. Reclassify this file as a **case study** with $0.00 recovery unless a real claimant emerges.
2. Pull the original and restated filings, the AAER, and the bankruptcy plan to clear the **[recall]** items.
3. Recompute all scores for FY1996, FY1997, and FY1998, with and without acquisition effects.
4. Correct the pipeline so the Sloan sign, F-Score type, fiscal period, and period-appropriate GAAP are explicit fields.

## 6. Verification & Chain of Custody

### Current status

| Control | Status | Required action |
|---|---|---|
| **Source filing** | Not retrieved | Fetch the accession from EDGAR and confirm the filer, form, and period. |
| **SHA-256** | **Not computed; no hash is reported** | Hash the source filing, inputs, script, and this dossier. |
| **DuckDB** | Not run; version 2.0.0 LTS unconfirmed | Load the schema below and record the version actually used. |
| **Z3** | Not run | Execute the script and archive the output and solver version. |
| **TruLens: context relevance** | **Not evaluated** | No retrieved context exists to score. |
| **TruLens: groundedness** | **Not evaluated** | Score after primary sources are linked to the claims. |
| **TruLens: answer relevance** | **Not evaluated** | Score it in the live pipeline. |

### Hashing commands

```powershell
Get-FileHash .\source_filing.txt -Algorithm SHA256
Get-FileHash .\case_inputs.json -Algorithm SHA256
Get-FileHash .\sunbeam_z3_proof.py -Algorithm SHA256
Get-FileHash .\sunbeam_dossier.md -Algorithm SHA256
```

### DuckDB schema

```sql
CREATE TABLE case_inputs (
    case_id               VARCHAR PRIMARY KEY,
    entity_name           VARCHAR NOT NULL,
    ticker                VARCHAR,
    cik                   VARCHAR,
    accession_number      VARCHAR,
    fiscal_period_end     DATE,          -- required before release; absent from the input
    assets_usd            DECIMAL(18,2) NOT NULL,
    liabilities_usd       DECIMAL(18,2) NOT NULL,
    equity_usd            DECIMAL(18,2) NOT NULL,
    net_income_usd        DECIMAL(18,2) NOT NULL,
    cfo_usd               DECIMAL(18,2) NOT NULL,
    accruals_usd          DECIMAL(18,2) NOT NULL,
    cutoff_distortion_usd DECIMAL(18,2),
    recovery_usd          DECIMAL(18,2) NOT NULL,
    source_sha256         VARCHAR,
    loaded_at             TIMESTAMP DEFAULT current_timestamp
);

CREATE TABLE claim_ledger (
    claim_id            VARCHAR PRIMARY KEY,
    case_id             VARCHAR NOT NULL REFERENCES case_inputs (case_id),
    claim_text          VARCHAR NOT NULL,
    provenance          VARCHAR NOT NULL
        CHECK (provenance IN ('SUPPLIED', 'DERIVED', 'RECALL', 'PRIMARY_SOURCE')),
    verification_status VARCHAR NOT NULL
        CHECK (verification_status IN ('UNVERIFIED', 'VERIFIED', 'CONTRADICTED')),
    source_reference    VARCHAR,
    source_sha256       VARCHAR
);

-- Returns rows only when a filing identity or arithmetic check fails
SELECT case_id,
       assets_usd - liabilities_usd - equity_usd AS balance_gap,
       accruals_usd - (net_income_usd - cfo_usd) AS accrual_gap
FROM case_inputs
WHERE assets_usd <> liabilities_usd + equity_usd
   OR accruals_usd <> net_income_usd - cfo_usd
   OR fiscal_period_end IS NULL;
```

### Sign-off criteria

This dossier can be released only when all of the following are true:

- Every **[recall]** item is verified or removed.
- All input conflicts in Section 1 are resolved.
- The Z3 output and all hashes are archived.
- Any TruLens scores come from an actual run.
- Counsel has signed off on the legal analysis.