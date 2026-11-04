# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Enron Corp

> **Status: working draft, not ready for publication or delivery.**
> - **No recovery claim:** the $0.00 recovery figure holds, so there is nothing to demand.
> - **Metrics that fail:** the supplied M-Score (4.82) and Sloan figure (0.284) don't reconcile with the financials. My recomputed values are about **-0.56** and **-0.058**.
> - **Not run:** this was written by Claude without the Muse, DuckDB, Z3, or TruLens stack, and I had no execution tools in this session. The Z3 script is untested, and I didn't open any filing or check any citation against a source. Items marked **[verify]** come from memory.
> - **Legal review:** this isn't legal advice, and I'm not counsel.

## 1. Executive Summary & Exposure Classification

| Classification | Finding |
|---|---|
| **Immediate Financial Impact** | **$0.00 recoverable.** The unsourced $1.24B distortion is a historical accounting measure, not a claim amount. |
| **Likelihood of Recovery** | **Remote to none.** New 10b-5 claims are time-barred, and the equity was cancelled in bankruptcy **[verify]**. |
| **Legal Exposure** | **Enron's historical exposure was severe but has been resolved or expired. The live risk is sending an unsupported demand.** |

### Input reconciliation

| Input | Result | Finding |
|---|---|---|
| Assets = liabilities + equity | **Ties** | $54,033M + $11,470M = $65,503M. Liabilities include minority interests and preferred securities **[verify]**. |
| Accruals = net income âˆ’ CFO | **Ties** | $979M âˆ’ $4,779M = âˆ’$3,800M |
| Beneish M-Score: 4.82 | **Fails** | Recomputes to about âˆ’0.56. It still exceeds the âˆ’1.78 flag, but 4.82 would need accruals of about 109% of assets (about $71.5B). |
| Sloan accruals: 0.284 | **Fails** | âˆ’0.058 on ending assets or âˆ’0.077 on average assets. A value of 0.284 implies +$18.6B on ending assets, and the sign is also wrong. |
| Dechow F-Score logit: 0.942 | **Ambiguous** | As a logit, it implies about 72% probability, which is implausibly high. As a scaled F-Score, it sits below the 1.00 baseline, so it wouldn't flag Enron. |
| ASC 606 distortion: $1.24B | **Mislabeled and unsourced** | ASC 606 didn't exist in 2000. The closest figure I know is the $1.2B equity reduction disclosed in 2001 **[verify]**. |
| ASC 810 basis | **Anachronistic** | The period standards are listed below. |
| Z3 result: "SAT" | **Not a proof** | SAT only means a satisfying model exists. A proof needs the claim's negation to return UNSAT. |
| Accession number | **Unverified** | The CIK matches my recollection, but I couldn't confirm this accession number or which filing it refers to. |
| Waterfall: null | **Consistent** | With $0 recoverable, there is nothing to distribute. |

For scale, $1.24B would equal 126.7% of net income, 10.8% of equity, and 1.9% of assets. These ratios don't validate the figure.

## 2. Core Forensic Anomaly Decomposition

No Beneish components were supplied, so I rebuilt them from my recollection of the FY2000 10-K **[verify]**. The recalled figures foot to reported totals, including $65,503M and $54,033M, but need checking against the filing.

| $M | FY2000 | FY1999 |
|---|---|---|
| Revenue | 100,789 | 40,112 |
| Cost of gas, electricity, metals, and other products | 94,517 | 34,761 |
| Operating expenses (SG&A proxy) | 3,184 | 3,045 |
| Depreciation and amortization | 855 | 870 |
| Trade receivables | 10,396 | 3,030 |
| Current assets | 30,381 | 7,255 |
| Net PP&E | 11,743 | 10,681 |
| Current liabilities | 28,406 | 6,759 |
| Long-term debt | 8,550 | 7,151 |
| Total assets | 65,503 | 33,381 |

| Component | Value | Coefficient | Contribution | What it shows |
|---|---|---|---|---|
| **DSRI** | 1.365 | 0.920 | +1.256 | Receivables grew faster than revenue, though gas and power prices and gross trading volume also played a part. |
| **GMI** | 2.144 | 0.528 | +1.132 | Gross margin fell from 13.3% to 6.2%, consistent with gross reporting of merchant activity. |
| **AQI** | 0.771 | 0.404 | +0.312 | This looks benign because mark-to-market assets in current assets count as "hard" assets. |
| **SGI** | 2.513 | 0.892 | +2.241 | This is the largest driver, as revenue grew 151%. |
| **DEPI** | 1.110 | 0.115 | +0.128 | The depreciation rate slowed modestly. |
| **SGAI** | 0.416 | âˆ’0.172 | âˆ’0.072 | Enron had no SG&A line, so this uses a proxy and is low-confidence. |
| **LVGI** | 1.354 | âˆ’0.327 | âˆ’0.443 | Reported leverage rose, but the ratio misses unconsolidated SPE debt. |
| **TATA** | âˆ’0.058 | 4.679 | âˆ’0.271 | Negative accruals lower the score, which is the main blind spot. |
| **Intercept** | | | âˆ’4.840 | |
| **M-Score** | | | **â‰ˆ âˆ’0.557** | Above âˆ’1.78, so it flags likely manipulation. |

Using a balance-sheet approximation of TATA (about +0.003) moves the score to about âˆ’0.27, so the conclusion doesn't change.

### How the distortions worked

- **SPE debt:** Period rules relied on ARB 51, SFAS 94, and the SPE guidance in EITF 90-15 and Topic D-14, including the 3% outside-equity test. Chewco's failure of that test led to retroactive consolidation of JEDI **[verify]**.
- **Restatement:** The November 2001 8-K reduced 2000 net income by about $132M, raised debt by about $628M, and cut equity by about $1.2B **[verify]**.
- **Mark-to-market revenue:** EITF 98-10 brought estimated future contract gains into current earnings, often with management-built curves for illiquid contracts. Gross presentation also inflated revenue, and EITF 02-3 later curtailed both practices.
- **Operating cash flow:** The $4,779M CFO makes accruals look conservative, but prepay structures reportedly disguised financing as operations **[verify]**. Customer deposits also rose by $4,233M, or $1,881M net of deposits Enron posted. That net amount is 39% of CFO if it all ran through operating cash flow **[verify]**.
- **Scale:** The Batson examiner's report adjusted 2000 net income from about $979M to about $42M, and debt from about $10.2B to about $22.1B **[verify]**.

**Key takeaway:** The accrual screens point the wrong way because the cash flow number itself was compromised. CFO should be rebuilt before accruals are used as evidence of earnings quality.

## 3. Statutory & Commercial Recovery Basis

| Basis | Applies? | Analysis |
|---|---|---|
| **UCC Â§ 2-717** | No | Requires a buyer deducting damages from the price still due under the same goods contract. No such contract is in the record. |
| **UCC Â§ 2-305** | No | Addresses open price terms in a sale of goods, not securities or financial reporting. |
| **19 U.S.C. Â§ 1313** | No | Covers duty drawback, and the record shows no import, duty payment, or export. |
| **15 U.S.C. Â§ 78j(b) / Rule 10b-5** | Substantively relevant, but barred | See the barriers below. |
| **26 U.S.C. Â§ 165(g) / Â§ 6511(d)(1)** | Almost certainly expired | A former holder's worthless-security refund claim has a seven-year window, which would have closed around 2009 for a 2001 loss year **[verify]**. |

### Barriers to a new 10b-5 claim

1. **Repose:** 28 U.S.C. Â§ 1658(b) sets outer limits of two years from discovery and five years from the violation. The last plausible violation was in 2001, so repose ran around 2006. *CalPERS v. ANZ Securities* (2017) rejects American Pipe tolling of the parallel Securities Act repose period.
2. **Standing:** *Blue Chip Stamps* (1975) limits private plaintiffs to actual purchasers or sellers, and no claimant is identified here.
3. **Elements:** A claimant would still have to meet *Tellabs* on scienter and *Dura* on loss causation. *Stoneridge* and *Janus* narrow the secondary-defendant theories.
4. **Bankruptcy:** Case No. 01-16034 (Bankr. S.D.N.Y.) had a 2002 bar date and a plan effective in 2004 **[verify]**. 11 U.S.C. Â§ 510(b) subordinates securities-fraud damage claims.
5. **Prior resolution:** *In re Enron Corp. Securities Litigation* (MDL 1446, S.D. Tex.) produced about $7.2B in settlements **[verify]**. Any eligible class member's rights ran through that process.

The remaining practical check is whether a specific former holder has undistributed settlement funds or unclaimed property. That would be a records inquiry, not a demand.

## 4. Executable Z3 SMT Counterexample Proof

The script checks the arithmetic and tests the supplied metrics against it. It can't prove fraud or establish the law: the recovery check only shows what follows from the repose rule as encoded, and the FY2000 inputs still need verifying.

```python
#!/usr/bin/env python3
"""Enron FY2000 metric reconciliation. Requires: pip install z3-solver"""
import sys
from fractions import Fraction as F

from z3 import And, If, Implies, Int, Not, Q, Real, Solver, sat, unsat

# Supplied case inputs, $M
ASSETS, LIAB, EQUITY = 65503, 54033, 11470
NI, CFO, ACCRUALS = 979, 4779, -3800
PRIOR_ASSETS = 33381

# Recalled from the FY2000 10-K; verify against the filing
CUR = dict(rev=100789, cogs=94517, opex=3184, dep=855, ar=10396,
           ca=30381, ppe=11743, cl=28406, ltd=8550, ta=ASSETS)
PRI = dict(rev=40112, cogs=34761, opex=3045, dep=870, ar=3030,
           ca=7255, ppe=10681, cl=6759, ltd=7151, ta=PRIOR_ASSETS)


def R(x):
    x = F(x)
    return Q(x.numerator, x.denominator)


def margin(d):
    return F(d["rev"] - d["cogs"], d["rev"])


def asset_quality(d):
    return 1 - F(d["ca"] + d["ppe"], d["ta"])


def dep_rate(d):
    return F(d["dep"], d["dep"] + d["ppe"])


def leverage(d):
    return F(d["cl"] + d["ltd"], d["ta"])


DSRI = F(CUR["ar"], CUR["rev"]) / F(PRI["ar"], PRI["rev"])
GMI = margin(PRI) / margin(CUR)
AQI = asset_quality(CUR) / asset_quality(PRI)
SGI = F(CUR["rev"], PRI["rev"])
DEPI = dep_rate(PRI) / dep_rate(CUR)
SGAI = F(CUR["opex"], CUR["rev"]) / F(PRI["opex"], PRI["rev"])
LVGI = leverage(CUR) / leverage(PRI)
TATA = F(ACCRUALS, ASSETS)

M_EX_TATA = (F("-4.84") + F("0.92") * DSRI + F("0.528") * GMI
             + F("0.404") * AQI + F("0.892") * SGI + F("0.115") * DEPI
             - F("0.172") * SGAI - F("0.327") * LVGI)
M = M_EX_TATA + F("4.679") * TATA

results = []


def prove(label, claim):
    s = Solver()
    s.add(Not(claim))
    ok = s.check() == unsat
    results.append(ok)
    print(f"{'PROVED' if ok else 'FAILED'}  {label}")


def witness(label, *constraints):
    s = Solver()
    s.add(*constraints)
    ok = s.check() == sat
    results.append(ok)
    print(f"{'SAT   ' if ok else 'FAILED'}  {label}")
    return s.model() if ok else None


print(f"Computed M-Score: {float(M):.4f}")

prove("Assets = liabilities + equity", R(ASSETS) == R(LIAB) + R(EQUITY))
prove("Accruals = net income - CFO", R(ACCRUALS) == R(NI) - R(CFO))

m = Real("m")
prove("Computed M-Score differs from supplied 4.82",
      Implies(m == R(M), m != R("4.82")))
prove("Computed M-Score exceeds the -1.78 flag",
      Implies(m == R(M), m > R("-1.78")))

s_end, s_avg = Real("s_end"), Real("s_avg")
prove("Sloan on ending assets differs from 0.284",
      Implies(s_end == R(F(ACCRUALS, ASSETS)), s_end != R("0.284")))
prove("Sloan on average assets differs from 0.284",
      Implies(s_avg == R(F(ACCRUALS * 2, ASSETS + PRIOR_ASSETS)),
              s_avg != R("0.284")))

# Counterexample: the TATA needed to make M-Score 4.82, other inputs fixed
t = Real("t")
model = witness("TATA required for M-Score = 4.82",
                R(M_EX_TATA) + R("4.679") * t == R("4.82"))
if model is not None:
    required = F(model[t].as_fraction())
    print(f"        TATA = {float(required):.4f}; "
          f"implied accruals = ${float(required * ASSETS):,.0f}M")

# Consolidating SPE debt raises leverage but leaves the identity intact
d = Real("d")
A, L = R(ASSETS), R(LIAB)
prove("For any added debt > 0, equity is unchanged and leverage rises",
      Implies(d > 0, And((A + d) - (L + d) == A - L,
                         (L + d) * A > L * (A + d))))

# Encodes the repose assumption only; it does not establish the law
last_violation, filed = Int("last_violation"), Int("filed")
claim = Real("claim")
recovery = If(filed - last_violation <= 5, claim, R(0))
prove("With last violation <= 2001 and filing >= 2026, recovery = 0",
      Implies(And(last_violation <= 2001, filed >= 2026, claim >= 0),
              recovery == 0))
witness("Counterfactual: a 2004 filing could have had nonzero recovery",
        last_violation == 2001, filed == 2004, claim > 0, recovery > 0)

sys.exit(0 if all(results) else 1)
```

**Expected result, calculated by hand:** every check passes, with an M-Score of about âˆ’0.557, required TATA of about 1.091, and implied accruals of about $71.5B.

## 5. Actionable Legal Remediation & Demand Notice Template

**Do not send this notice on the current record.** It has no claimant, no contract, and a $0.00 claim, and a 10-day cure period has no statutory basis under Rule 10b-5. Asserting this claim could expose the sender to legal and credibility risk.

### Remediation path

1. Correct the case record using the reconciliation in Section 1.
2. Mark the matter as a historical case study or a no-claim file.
3. If a real former holder exists, gather their trade records and check settlement and unclaimed-property sources.
4. Have licensed counsel confirm any remaining avenue before anyone contacts a third party.

### Template, for use only if counsel identifies a viable claim

```text
DRAFT - NOT FOR DELIVERY - REQUIRES COUNSEL REVIEW

[DATE]

VIA [DELIVERY METHOD]
[VERIFIED RECIPIENT]
[VERIFIED ADDRESS]

Re: Notice of Claim and Demand - [CLAIMANT] - [MATTER REFERENCE]

To whom it may concern:

This notice is sent on behalf of [CLAIMANT] regarding [SPECIFIC TRANSACTION
OR CONTRACT], dated [DATE].

1. Basis of claim. [Facts, documents, and the legal basis confirmed by counsel,
   including why the claim is timely and not barred, released, or discharged.]

2. Claim calculation.
   [Documented loss or amount due]      $[AMOUNT]
   [Credits, offsets, or recoveries]   ($[AMOUNT])
   Total demanded                       $[AMOUNT]

3. Demand. Please pay or otherwise cure the amount above within ten (10) days of
   receipt, by [DATE], or respond in writing with any basis for dispute.
   [Include only if counsel confirms a cure period applies.]

4. Preservation. Please preserve all documents and data relating to this matter.

5. Reservation of rights. This notice does not waive any right or remedy, all of
   which are reserved.

Sincerely,

[COUNSEL OF RECORD OR AUTHORIZED SIGNATORY]
```

If John signs as an authorized representative rather than through counsel, use this block after counsel confirms that role is appropriate:

```text
John Webb
Principal, John Webb & Co.
Louisville, KY
502-693-2779
```

## 6. Verification & Chain of Custody

| Control | Status | Required action |
|---|---|---|
| **SHA-256 integrity** | **Not generated** | Hash the final dossier and each source file. I didn't invent placeholder hashes. |
| **DuckDB table** | **Schema not run** | I can't confirm "DuckDB 2.0.0 LTS" from this session, so test the schema on the installed version. |
| **Z3 proof** | **Not run** | Run the script and save its output and exit code. |
| **TruLens RAG triad** | **Not run, no scores** | Context relevance, groundedness, and answer relevance need a real retrieval corpus and a TruLens run. |
| **Source verification** | **Open** | Clear each **[verify]** item against the 10-K, November 2001 8-K, Powers Report, Batson reports, and the court record. |

**Generate the hashes in PowerShell:**

```powershell
Get-FileHash -Algorithm SHA256 .\dossier.md, .\enron_z3_proof.py, .\source_filing.htm
```

**DuckDB schema:**

```sql
CREATE TABLE forensic_case (
    case_id            VARCHAR PRIMARY KEY,
    entity             VARCHAR NOT NULL,
    cik                VARCHAR NOT NULL,
    accession_number   VARCHAR,
    accession_verified BOOLEAN NOT NULL DEFAULT FALSE,
    recovery_usd       DECIMAL(18,2) NOT NULL DEFAULT 0
);

CREATE TABLE metric_reconciliation (
    case_id        VARCHAR NOT NULL REFERENCES forensic_case (case_id),
    metric         VARCHAR NOT NULL,
    supplied_value DOUBLE,
    computed_value DOUBLE,
    status         VARCHAR NOT NULL
        CHECK (status IN ('TIES', 'FAILS', 'AMBIGUOUS', 'UNVERIFIED')),
    source_ref     VARCHAR,
    PRIMARY KEY (case_id, metric)
);

CREATE TABLE custody_log (
    artifact    VARCHAR NOT NULL,
    sha256      CHAR(64) NOT NULL,
    recorded_at TIMESTAMPTZ NOT NULL,
    recorded_by VARCHAR NOT NULL,
    source_url  VARCHAR,
    PRIMARY KEY (artifact, sha256)
);
```

**Release gate:** before publishing, clear all **[verify]** items, record a passing Z3 run, log real hashes, and get counsel's sign-off on Sections 3 and 5. Also trace the supplied 4.82, 0.284, 0.942, and $1.24B values to their source, because the first two fail against the financials and the others are unsupported.