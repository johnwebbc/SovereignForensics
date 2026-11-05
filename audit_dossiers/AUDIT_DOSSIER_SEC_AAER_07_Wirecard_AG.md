# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Wirecard AG

> **Status: draft, not publication-grade or ready to send.** The input record contains contradictions and unverified identifiers, and most M-Score components can't be computed from it. I ran no code, retrieval, hashing, DuckDB, or TruLens, and did not use Muse Glimmer. Non-input facts are from memory and need checking against primary sources. This is not legal advice, and qualified German and US counsel should review it.

## 1. Executive Summary & Exposure Classification

**Conclusion:** The Wirecard fraud allegations are well documented, but this record doesn't support a statutory recovery claim. The stated recovery of **$0.00** is the only supportable figure, and none of the suggested US commercial or customs theories fits.

| Area | Classification | Basis |
|---|---|---|
| **Immediate financial impact** | **$2.1B in unverified assets (30.9% of stated assets)** | If the full amount is removed from stated assets, equity falls from $1.9B to **-$0.2B**. This assumes the $6.8B includes the $2.1B. |
| **Likelihood of recovery** | **None identified on this record** | There is no claimant, contract, duty payment, or claim amount, and the waterfall is null. Any recovery would likely run through the German insolvency process or claims against third parties. |
| **Legal exposure** | **High for the underlying conduct; jurisdiction-specific** | The main forums are German criminal, insolvency, and securities proceedings. Any US claim faces extraterritoriality limits. |

### Input integrity

| Input | Finding | Status |
|---|---|---|
| Assets = liabilities + equity | $4.9B + $1.9B = $6.8B | **Reconciles** |
| Accruals = net income - CFO | -$1.2B - (-$0.4B) = -$0.8B | **Reconciles** |
| Sloan accrual anomaly of 0.331 | -$0.8B / $6.8B = **-0.1176**; the sign and size both conflict | **Fails** |
| ASC 606 cutoff distortion of $2.1B | This appears to be the roughly â‚¬1.9B of missing cash, not a revenue cutoff amount | **Mislabeled** |
| ASC 305 basis | Wirecard reported under IFRS, so IAS 7 is the closer cash standard | **Wrong framework** |
| Financials | They match no statements I can identify. Wirecard never issued audited FY2019 accounts, and FY2018 showed a net profit of about â‚¬347M. | **Source required** |
| Case ID, category, and accession number | I'm not aware of a Wirecard SEC AAER or restatement, or of Wirecard being an SEC-reporting issuer. | **Unverified** |
| Dechow value of 0.965 | As a logit, it implies P = 72.4% and a scaled F-Score of about 195.7. As a scaled score, it would be below average risk. | **Ambiguous** |
| Z3 result of "SAT" | No formula was supplied, and SAT means only that a set of constraints can be satisfied. | **Not evidence alone** |

**Lead to test:** $2.1B / 0.331 implies a denominator of about $6.344B. That would equal average assets if prior-year assets were about $5.889B, close to Wirecard's FY2018 total of about â‚¬5.9B. The 0.331 may therefore be the missing cash divided by average assets rather than a Sloan accrual measure, possibly with mixed currencies.

### Public-record context (verify before relying on it)

- **June 2020 collapse:** On June 18, Wirecard disclosed that about â‚¬1.9B in trustee accounts could not be confirmed. On June 22, it said the balances likely did not exist, and it filed for insolvency in Munich on June 25.
- **Forged confirmations:** Two Philippine banks, BDO and BPI, said documents naming them were not genuine. The Philippine central bank said the funds had not entered its financial system.
- **Earlier warning:** KPMG's April 2020 special audit report said it could not fully verify the third-party acquiring business.

## 2. Core Forensic Anomaly Decomposition

Beneish model: **M = -4.84 + 0.920 DSRI + 0.528 GMI + 0.404 AQI + 0.892 SGI + 0.115 DEPI - 0.172 SGAI + 4.679 TATA - 0.327 LVGI**

Only TATA can be calculated because the other seven indices need two years of line items. I have not estimated them.

| Component | Measures | Value | What to test at Wirecard |
|---|---|---|---|
| **DSRI** | Receivables relative to sales | Not computable | Balances due from third-party acquirers and trustees |
| **GMI** | Gross margin deterioration | Not computable | Margin mix between third-party and in-house processing |
| **AQI** | Share of non-current, non-PP&E assets | Not computable | Goodwill, intangibles, and acquisition accounting |
| **SGI** | Sales growth | Not computable | Share of growth from third-party partners |
| **DEPI** | Slowing depreciation | Not computable | Useful-life changes, especially for acquired assets |
| **SGAI** | SG&A relative to sales | Not computable | Whether overhead scaled with reported volume |
| **LVGI** | Change in leverage | Not computable | Debt raised despite large reported cash balances |
| **TATA** | Accruals relative to assets | **-0.1176** | Contributes **-0.5505** to the M-Score |

### What the 4.95 score requires

- **Neutral baseline:** With the other seven indices at 1.0 and TATA at -0.1176, M = **-3.03**.
- **Gap to explain:** The reported score is **7.98 points** higher, and the seven non-TATA terms must total **10.34**.
- **Single-index illustration:** If DSRI alone closed the gap, it would need to be about **9.67**. If SGI alone did, it would need to be about **9.95**.
- **Minimum extreme value:** At least one positively weighted index must be **at least 3.617** if all indices are non-negative.

The score is mathematically possible, but it can't be accepted without the underlying indices.

### Accounting distortion

The core allegation is fabricated cash rather than an ordinary buildup of accruals. If fictitious revenue is matched by fictitious cash, accrual measures can look normal or even negative. That makes **direct cash confirmation** the decisive test, not the M-Score, F-Score, or Sloan ratio.

| Control test | Evidence needed |
|---|---|
| Existence of cash | Confirmations obtained and controlled directly by the auditor, per ISA 505 and ISA 500 |
| Restricted cash | Trust terms, access rights, and IAS 7 disclosure of balances not available for use |
| Partner activity | Merchant-level transaction data, settlement files, and processor records |
| Fraud risk | ISA 240 procedures covering management override and document authenticity |

## 3. Statutory & Commercial Recovery Basis

| Theory | Requires | Assessment |
|---|---|---|
| **UCC Â§ 2-717** | A buyer deducting damages from the price due under the same contract for goods | **Not applicable on this record** |
| **UCC Â§ 2-305** | A contract for the sale of goods with an open price term | **Not applicable** |
| **19 U.S.C. Â§ 1313** | Qualifying imported merchandise, paid duties, and a drawback claim | **Not applicable** |
| **Tax code** | An identified taxpayer, tax year, and loss or refund position | **Cannot be assessed** |

### Paths counsel could evaluate

| Path | Potential claimant | Key issue |
|---|---|---|
| **German insolvency claim (Â§Â§ 174 ff. InsO)** | Creditors | Filing status, deadlines, and ranking |
| **Insolvency setoff (Â§Â§ 94-96 InsO)** | Merchants or counterparties with mutual claims | Contract terms and whether setoff rights survive |
| **German capital-markets and tort claims (Â§Â§ 97-98 WpHG; Â§Â§ 823(2), 826 BGB)** | Investors | Reliance, causation, defendants, limitation periods, and ranking of shareholder claims |
| **Auditor claims (Â§ 323 HGB, Â§ 826 BGB, KapMuG)** | The estate or investors | Standing, liability limits, and status of the model case |
| **US securities claims (Â§ 10(b), Rule 10b-5)** | ADR purchasers | Whether the transaction was domestic under *Morrison v. National Australia Bank*, 561 U.S. 247 (2010), and *Stoyas v. Toshiba*, 896 F.3d 933 (9th Cir. 2018) |

Any recovery depends on claimant-specific evidence, including trade records, contracts, filed claims, and the current estate distribution position.

## 4. Executable Z3 SMT Counterexample Proof

Install with `pip install z3-solver`. I have not run this script. It should print `PASS` for every check and exit with code 0.

```python
from fractions import Fraction
import math

from z3 import *

# USD millions, exact values from the input record
A, L, E = RealVal(6800), RealVal(4900), RealVal(1900)
NI, CFO, ACC = RealVal(-1200), RealVal(-400), RealVal(-800)
V = RealVal(2100)
REPORTED_SLOAN = Q(331, 1000)
TATA = Q(-2, 17)
results = []


def run(name, expected, *constraints):
    s = Solver()
    s.add(*constraints)
    result = s.check()
    passed = result == expected
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'} | {name} | got={result} expected={expected}")
    if result == sat:
        print(f"       model: {s.model()}")


# Accounting identities: unsat means no violation exists
run("Assets = liabilities + equity", unsat, A != L + E)
run("Accruals = net income - CFO", unsat, ACC != NI - CFO)

# Sloan checks
r, D, P = Reals("r D P")
run("Accruals / ending assets = -2/17", unsat, r * A == ACC, r != TATA)
run("No positive denominator yields +0.331", unsat, D > 0, ACC == REPORTED_SLOAN * D)
run(
    "No non-negative prior assets yield |accruals| / average assets = 0.331",
    unsat,
    P >= 0,
    -ACC == REPORTED_SLOAN * (A + P) / 2,
)

# Assumes the unverified balance is included in stated assets
adjusted_equity = A - V - L
run("Adjusted equity = -200", unsat, adjusted_equity != -200)
run("Adjusted equity cannot be non-negative", unsat, adjusted_equity >= 0)

# Cash counterexample: confirmed = 0 is an evidentiary input, not a Z3 finding
recognized, confirmed = Reals("recognized confirmed")
run(
    "Counterexample: recognized cash exceeds confirmed cash",
    sat,
    recognized == V,
    confirmed == 0,
    recognized > confirmed,
)

# Beneish feasibility
DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI = indices = Reals("DSRI GMI AQI SGI DEPI SGAI LVGI")
M = (
    RealVal("-4.84")
    + RealVal("0.92") * DSRI
    + RealVal("0.528") * GMI
    + RealVal("0.404") * AQI
    + RealVal("0.892") * SGI
    + RealVal("0.115") * DEPI
    - RealVal("0.172") * SGAI
    + RealVal("4.679") * TATA
    - RealVal("0.327") * LVGI
)


def bounded(upper):
    return And([And(x >= 0, x <= RealVal(upper)) for x in indices])


run("M = 4.95 is impossible if all indices <= 3.60", unsat, bounded("3.60"), M == RealVal("4.95"))
run("M = 4.95 is feasible if all indices <= 3.62", sat, bounded("3.62"), M == RealVal("4.95"))

# Recovery bound: eligibility flags encode the legal conclusions in Section 3
ucc_2717, ucc_2305, drawback = Bools("ucc_2717 ucc_2305 drawback")
a1, a2, a3 = Reals("a1 a2 a3")
recovery = (
    If(ucc_2717, a1, RealVal(0))
    + If(ucc_2305, a2, RealVal(0))
    + If(drawback, a3, RealVal(0))
)
run(
    "Recovery cannot exceed 0 under the three ineligible theories",
    unsat,
    a1 >= 0,
    a2 >= 0,
    a3 >= 0,
    Not(ucc_2717),
    Not(ucc_2305),
    Not(drawback),
    recovery > 0,
)

# Non-linear and reporting values calculated outside Z3
neutral_m = Fraction("-2.48") + Fraction("4.679") * Fraction(-2, 17)
gap = Fraction("4.95") - neutral_m
probability = math.exp(0.965) / (1 + math.exp(0.965))
print(f"Neutral M-Score: {float(neutral_m):.4f}")
print(f"Gap to reported M-Score: {float(gap):.4f}")
print(f"Single-index DSRI: {1 + float(gap / Fraction('0.92')):.2f}")
print(f"Single-index SGI: {1 + float(gap / Fraction('0.892')):.2f}")
print(f"F-Score probability if 0.965 is a logit: {probability:.4f}")
print(f"Scaled F-Score: {probability / 0.0037:.1f}")

raise SystemExit(0 if all(results) else 1)
```

**What this proves:** The arithmetic is internally consistent or inconsistent as labeled, and the reported Sloan value can't be derived from the supplied accruals using a positive denominator or average assets.

**What this doesn't prove:** It doesn't establish fraud, intent, the authenticity of documents, or legal liability. Those conclusions depend on evidence and the legal judgments encoded as inputs.

## 5. Actionable Legal Remediation & Demand Notice Template

**Do not send this as written.** It needs an identified claimant, a documented amount, and counsel's review. A 10-day cure demand also has limited force against an insolvent company because claims generally must proceed through the insolvency process. The template therefore uses the 10 days as a requested response period and does not assert a payment default.

---

**[CLAIMANT LETTERHEAD]**

**Date:** [DATE]
**Via:** [DELIVERY METHOD CONFIRMED BY COUNSEL]

**To:** Insolvency Administrator, Wirecard AG (in insolvency)
[CURRENT NAME AND ADDRESS, VERIFIED FROM THE COURT OR ADMINISTRATOR RECORD]

**Re: Notice of Claim, Preservation Request, and Reservation of Rights**
**Claimant:** [LEGAL NAME]
**Claim or reference number:** [NUMBER, IF ANY]

Dear [NAME]:

We submit this notice on behalf of [CLAIMANT] regarding [CONTRACT, SECURITIES PURCHASE, OR OTHER LEGAL RELATIONSHIP].

**1. Basis of claim.** [CLAIMANT] asserts a claim based on [FACTS AND COUNSEL-APPROVED LEGAL BASIS]. Supporting documents are listed in Schedule A.

**2. Claim calculation.**

| Item | Amount | Currency | Evidence |
|---|---|---|---|
| Principal | [AMOUNT] | [CURRENCY] | [EXHIBIT] |
| Interest, if permitted | [AMOUNT] | [CURRENCY] | [CALCULATION] |
| Less payments or setoffs | ([AMOUNT]) | [CURRENCY] | [EXHIBIT] |
| **Total claimed** | **[AMOUNT]** | **[CURRENCY]** | |

**3. Requested action.** Within **10 calendar days** of receipt, please:

a. Confirm receipt of this notice.
b. Confirm whether [CLAIMANT]'s claim is on file, and its current status.
c. Identify any further filing or supporting documents required.
d. State whether the estate disputes any setoff asserted in Schedule A.

**4. Preservation.** Please preserve records relevant to this claim, including [CONTRACT, SETTLEMENT, TRUST, BANK CONFIRMATION, AND COMMUNICATION RECORDS].

**5. Reservation of rights.** This notice does not waive any right, remedy, or defense. Nothing in it is intended to violate any stay, enforcement restriction, or claims procedure that applies in the insolvency proceeding.

Sincerely,

**John Webb**
Principal, John Webb & Co.
Louisville, KY
502-693-2779
On behalf of: [CLAIMANT, IF AUTHORIZED]

**Schedule A:** [SUPPORTING DOCUMENTS AND SETOFF DETAILS]

---

## 6. Verification & Chain of Custody

### Verification status

| Control | Status | Required action |
|---|---|---|
| **SHA-256 integrity** | **Not generated** | Hash the final dossier and each source file after freezing them |
| **DuckDB 2.0.0 LTS** | **Not run; version unverified** | Confirm the installed version, then load the schema and source data |
| **Z3 proof** | **Not run** | Run the script and archive its output and solver version |
| **TruLens context relevance** | **Not evaluated** | Requires a retrieval run and source corpus |
| **TruLens groundedness** | **Not evaluated** | Requires claim-to-source mapping |
| **TruLens answer relevance** | **Not evaluated** | Requires a configured evaluation run |
| **Identifiers and filing** | **Unverified** | Check the CIK and accession number against EDGAR |
| **Legal authorities** | **Not cite-checked** | Have counsel confirm current text, case status, and deadlines |

### Hash commands

```powershell
Get-FileHash .\wirecard_dossier.md -Algorithm SHA256
Get-FileHash .\wirecard_z3_proof.py -Algorithm SHA256
Get-FileHash .\wirecard_z3_output.txt -Algorithm SHA256
```

### DuckDB schema

```sql
CREATE TABLE IF NOT EXISTS source_documents (
    document_id        VARCHAR PRIMARY KEY,
    case_id            VARCHAR NOT NULL,
    title              VARCHAR NOT NULL,
    publisher          VARCHAR,
    source_url         VARCHAR,
    accession_number   VARCHAR,
    retrieved_at       TIMESTAMPTZ NOT NULL,
    sha256             VARCHAR NOT NULL CHECK (length(sha256) = 64),
    verification_state VARCHAR NOT NULL
        CHECK (verification_state IN ('UNVERIFIED', 'VERIFIED', 'REJECTED'))
);

CREATE TABLE IF NOT EXISTS financial_inputs (
    case_id        VARCHAR NOT NULL,
    fiscal_period  VARCHAR NOT NULL,
    metric         VARCHAR NOT NULL,
    amount         DECIMAL(20, 2) NOT NULL,
    currency       VARCHAR NOT NULL,
    document_id    VARCHAR REFERENCES source_documents (document_id),
    source_locator VARCHAR,
    PRIMARY KEY (case_id, fiscal_period, metric, currency)
);

CREATE TABLE IF NOT EXISTS verification_runs (
    run_id         VARCHAR PRIMARY KEY,
    case_id        VARCHAR NOT NULL,
    tool_name      VARCHAR NOT NULL,
    tool_version   VARCHAR NOT NULL,
    check_name     VARCHAR NOT NULL,
    expected       VARCHAR,
    actual         VARCHAR,
    passed         BOOLEAN,
    artifact_sha256 VARCHAR CHECK (length(artifact_sha256) = 64),
    executed_at    TIMESTAMPTZ NOT NULL
);
```

### Required before release

1. Identify the source of each financial input, including its period and currency.
2. Correct or remove the 0.331 Sloan value and the ASC 606 and ASC 305 labels.
3. Replace or remove the SEC case ID, category, and accession number if they can't be verified.
4. Calculate the seven missing Beneish indices from source data and define the Dechow value's scale.
5. Identify a claimant and a documented claim, or remove the notice from the package.
6. Run the Z3, hashing, DuckDB, and TruLens steps, then record the actual results here.