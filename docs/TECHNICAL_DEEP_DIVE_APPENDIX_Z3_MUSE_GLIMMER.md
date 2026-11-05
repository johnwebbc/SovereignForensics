# SovereignForensics Technical Deep-Dive Appendix

**Status: reference architecture for hackathon documentation. The code has not been executed or checked against the SovereignForensics repository.**

## 0. Pre-Submission Verification

| Item | Status | Required evidence or action |
|---|---|---|
| Meta Muse Glimmer 30B | Unverified | Record model digest, license, and local runtime. If it only runs as a hosted service, it can't process confidential customs data. |
| DuckDB 2.0.0 LTS | Unverified | Record `duckdb.__version__` and confirm VARIANT syntax and shredding behavior. |
| Sub-second analytics over 1.1M rows | Unmeasured | Publish results from the benchmark in Â§2.4. |
| Z3 and TruLens APIs | Unverified | Pin versions and run the test matrix in Â§3.6. |
| Legal demand workflow | Requires counsel | Attorney review is required before any outward use. |

### Claim language

| Avoid | Use |
|---|---|
| "Z3 proves no manipulation" | "Z3 proves the M-Score stays below the configured screening threshold across the encoded input ranges." |
| "`sat` proves the recovery amount" | "The ledger is consistent, and `unsat` on the negated claim shows the ledger and policy model entail it." |
| "The LLM generates verified constraints" | "The LLM proposes conjectures, and a deterministic pipeline tests them against source-bound facts." |
| "Provably owed" | "Arithmetically verified under the stated facts and legal assumptions, pending counsel review." |

## System Architecture

```text
 SEC XBRL / 10-K / 10-Q                  CBP Form 7501 + liquidation data
          |                                         |
          v                                         v
 +-------------------+                    +-------------------+
 | Deterministic     |                    | Deterministic     |
 | XBRL parser       |                    | 7501 parser       |
 +---------+---------+                    +---------+---------+
           +-------------------+--------------------+
                               v
                 +----------------------------+
                 | DuckDB + Parquet evidence  |
                 | exact values + provenance  |
                 +------+--------------+------+
                        |              |
              narrative |              | fact ledger
                        v              |
              +------------------+     |
              | Glimmer 30B      |     |
              | (untrusted)      |     |
              +--------+---------+     |
                       | JSON IR       |
                       v               v
              +--------------------------------+
              | Pydantic validation + compiler |
              +---------------+----------------+
                              v
                     +------------------+
                     | Z3 obligations   |
                     +--------+---------+
                              |
                     +--------v---------+      +------------------+
                     | Release gate     |<-----| TruLens triad +  |
                     +--------+---------+      | numeric checks   |
                              |                +------------------+
                              v
                 +----------------------------+
                 | DRAFT package + evidence   |
                 +-------------+--------------+
                               v
                    Counsel review and decision
```

### Trust boundary

| Trusted after testing | Untrusted |
|---|---|
| Parsers, ledger, compiler, policy formulas, Z3 | Glimmer output, retrieved passages, TruLens judge scores |

**Core invariant: Glimmer can propose goals, but it can't add premises or numeric literals.** If it could add premises, it could assert the conclusion or create a contradiction that makes any goal pass.

## 1. The Mathematical Bridge

### 1.1 Formal model

Let:

- `D` be the source documents
- `L` be the ledger of facts extracted deterministically from `D`
- `P` be versioned policy parameters and templates
- `B(L)` be the bounds implied by each fact
- `C` be a conjecture proposed by Glimmer

A fact reported with rounding becomes an interval rather than a false point value:

```text
x âˆˆ [v - Î´, v + Î´]
Î´ = 0.5 Ã— 10^(-decimals)

Example: decimals = -6, so Î´ = $500,000
```

A conjecture is proved only when both conditions hold:

```text
SAT(B(L) âˆ§ P)                 the evidence model is consistent
UNSAT(B(L) âˆ§ P âˆ§ Â¬C)          no modeled counterexample exists
```

### 1.2 Source mappings

| Source | Example fields | Use |
|---|---|---|
| SEC XBRL | Concept, value, unit, period, accession number, filing date | Financial facts and Beneish inputs |
| 10-K/10-Q text | MD&A and note claims | Conjectures to test, never premises |
| CBP 7501 | Block 1 entry number, 23 importer number, 29A HTSUS number, 32A entered value, 33A HTSUS rate, 34 duty | Line-level duty facts |
| ACE data or CBP notice | Liquidation date and status | Protest timing, which the 7501 doesn't establish |

Confirm block mappings against the CBP instructions for the form version in the dataset.

### 1.3 Quantifier grounding

Glimmer can express a universal claim over a finite set of entry lines:

```text
âˆ€â„“ âˆˆ Lines(e): |duty_paid(â„“) - entered_value(â„“) Ã— rate_paid(â„“)| â‰¤ Ï„
```

The compiler expands it into a finite conjunction, which avoids quantifier-instantiation issues and normally returns a decisive result:

```text
Ï†(â„“1) âˆ§ Ï†(â„“2) âˆ§ ... âˆ§ Ï†(â„“n)
```

### 1.4 Intermediate representation

```python
# sovereignforensics/ir/models.py
from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Ref(Node):
    kind: Literal["ref"] = "ref"
    id: str


class Bin(Node):
    kind: Literal["bin"] = "bin"
    op: Literal["+", "-", "*", "/"]
    l: Expr
    r: Expr


class Abs(Node):
    kind: Literal["abs"] = "abs"
    x: Expr


Expr = Annotated[Ref | Bin | Abs, Field(discriminator="kind")]


class Cmp(Node):
    kind: Literal["cmp"] = "cmp"
    op: Literal["==", "<=", "<", ">=", ">"]
    l: Expr
    r: Expr


class ForAllLines(Node):
    kind: Literal["forall_lines"] = "forall_lines"
    entry: str
    body: Cmp


class Conjecture(Node):
    id: str
    formula: Annotated[Cmp | ForAllLines, Field(discriminator="kind")]
    source_span: str


class ConjectureSet(Node):
    conjectures: list[Conjecture]


Bin.model_rebuild()
Abs.model_rebuild()
Cmp.model_rebuild()
ForAllLines.model_rebuild()
Conjecture.model_rebuild()
ConjectureSet.model_rebuild()
```

The schema has no literal node, so constants must come from the ledger or versioned policy. Do not execute model-generated Python, and do not pass raw model-generated SMT-LIB directly to Z3.

### 1.5 Local model adapter

```python
# sovereignforensics/ir/extract.py
import os
from urllib.parse import urlparse

from openai import OpenAI

from sovereignforensics.ir.models import ConjectureSet

LOOPBACK = {"127.0.0.1", "localhost", "::1"}


def local_client() -> OpenAI:
    url = os.environ["SF_LOCAL_LLM_URL"]
    if urlparse(url).hostname not in LOOPBACK:
        raise RuntimeError("Confidential extraction requires a loopback endpoint")
    return OpenAI(base_url=url, api_key="local-no-key")


def propose(client: OpenAI, prompt: str) -> ConjectureSet:
    response = client.chat.completions.create(
        model=os.environ["SF_GLIMMER_ALIAS"],
        temperature=0,
        response_format={"type": "json_object"},
        messages=[{"role": "user", "content": prompt}],
    )
    return ConjectureSet.model_validate_json(response.choices[0].message.content)
```

### 1.6 Z3 compiler

```python
# sovereignforensics/smt/compiler.py
import operator
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Mapping, Sequence

import z3

from sovereignforensics.ir.models import Abs, Bin, Cmp, ForAllLines, Ref

ARITH = {"+": operator.add, "-": operator.sub, "*": operator.mul}
COMPARE = {
    "==": operator.eq,
    "<=": operator.le,
    "<": operator.lt,
    ">=": operator.ge,
    ">": operator.gt,
}


@dataclass(frozen=True)
class Fact:
    value: Decimal
    delta: Decimal
    source: str


def q(value: Decimal) -> z3.ArithRef:
    fraction = Fraction(value)
    return z3.Q(fraction.numerator, fraction.denominator)


def xbrl_delta(decimals: int | None) -> Decimal:
    if decimals is None:
        return Decimal(0)
    return Decimal(5) * Decimal(10) ** (-decimals - 1)


class Compiler:
    def __init__(
        self,
        ledger: Mapping[str, Fact],
        lines: Mapping[str, Sequence[str]] | None = None,
    ):
        self.ledger = ledger
        self.lines = lines or {}
        self.vars: dict[str, z3.ArithRef] = {}
        self.bounds: list[z3.BoolRef] = []
        self.defined: list[z3.BoolRef] = []

    def bind(self, fact_id: str) -> z3.ArithRef:
        if fact_id not in self.vars:
            fact = self.ledger[fact_id]
            var = z3.Real(fact_id)
            self.vars[fact_id] = var
            self.bounds += [
                var >= q(fact.value - fact.delta),
                var <= q(fact.value + fact.delta),
            ]
        return self.vars[fact_id]

    def div(self, left: z3.ArithRef, right: z3.ArithRef) -> z3.ArithRef:
        self.defined.append(right != 0)
        return left / right

    def term(self, expr) -> z3.ArithRef:
        if isinstance(expr, Ref):
            return self.bind(expr.id)
        if isinstance(expr, Abs):
            value = self.term(expr.x)
            return z3.If(value >= 0, value, -value)
        if isinstance(expr, Bin):
            left, right = self.term(expr.l), self.term(expr.r)
            if expr.op == "/":
                return self.div(left, right)
            return ARITH[expr.op](left, right)
        raise TypeError(type(expr))

    def cmp(self, node: Cmp) -> z3.BoolRef:
        return COMPARE[node.op](self.term(node.l), self.term(node.r))

    def formula(self, node: Cmp | ForAllLines) -> z3.BoolRef:
        if isinstance(node, Cmp):
            return self.cmp(node)
        lines = self.lines[node.entry]
        if not lines:
            raise ValueError(f"Empty quantifier domain: {node.entry}")
        return z3.And([self.cmp(self._ground(node.body, line)) for line in lines])

    @staticmethod
    def _ground(body: Cmp, line: str) -> Cmp:
        return Cmp.model_validate_json(
            body.model_dump_json().replace("{line}", line)
        )
```

Exact rationals avoid binary floating-point errors. The `defined` list is necessary because Z3 treats division as a total function, leaving `x / 0` unconstrained. Without an explicit denominator check, a proof could rely on an undefined ratio.

## 2. DuckDB Columnar Engine

### 2.1 Storage layout

These figures reflect documented DuckDB behavior and should be rechecked against the pinned build:

```text
1,100,000 rows
   |
   +-- about 9 row groups at 122,880 rows each
         |
         +-- one column segment set per column
         |     +-- min/max metadata for pruning
         |     +-- compression selected per segment
         |
         +-- vectorized execution in batches of 2,048 values
               about 537 vectors for a full scan
```

Parquet scans use the same broad strategy:

```text
Query -> Partition pruning -> Row-group statistics -> Column projection
      -> Vectorized decode -> Filter -> Aggregate/Join -> Result
```

### 2.2 Schema

```sql
CREATE TABLE xbrl_fact (
    fact_id       VARCHAR NOT NULL,
    cik           INTEGER NOT NULL,
    accession     VARCHAR NOT NULL,
    taxonomy      VARCHAR NOT NULL,
    concept       VARCHAR NOT NULL,
    unit          VARCHAR NOT NULL,
    period_start  DATE,
    period_end    DATE NOT NULL,
    form          VARCHAR NOT NULL,
    filed         DATE NOT NULL,
    val_num       DECIMAL(38, 4),
    decimals      INTEGER,
    src_sha256    VARCHAR NOT NULL,
    raw           VARIANT
);

CREATE TABLE cbp7501_line (
    entry_no       VARCHAR NOT NULL,
    line_no        INTEGER NOT NULL,
    hts_seq        INTEGER NOT NULL,
    importer_no    VARCHAR NOT NULL,
    entry_date     DATE NOT NULL,
    htsus          VARCHAR NOT NULL,
    entered_value  DECIMAL(18, 2) NOT NULL,
    rate_paid      DECIMAL(12, 8),
    duty_paid      DECIMAL(18, 2) NOT NULL,
    src_sha256     VARCHAR NOT NULL,
    src_page       INTEGER NOT NULL
);
```

`hts_seq` matters because one entry line can carry more than one HTSUS number, such as a Chapter 99 number and a base classification.

### 2.3 Shredded VARIANT for XBRL

XBRL facts have a stable core but sparse dimensions and extensions. Under the Parquet Variant model, commonly occurring paths can be stored as typed columns, with the remainder kept in the encoded variant:

```text
raw (VARIANT)
 |-- metadata            dictionary of field names
 |-- value               encoded data for unshredded paths
 `-- typed_value
      |-- segment        typed where shredded
      |-- scale          typed where shredded
      `-- frame          typed where shredded
```

Two rules keep this safe:

1. **Proof inputs come only from typed columns.** Z3 reads `val_num`, not a value extracted from `raw`.
2. **VARIANT holds sparse context only.** It preserves dimensions and source detail without forcing a very wide table.

Path-access and shredding syntax is omitted because it must be confirmed against the pinned DuckDB release.

### 2.4 Query and benchmark

This point-in-time query prevents later restatements from leaking into an earlier analysis. It filters on `period_end` because the `fy` field in SEC company facts describes the reporting filing, which can also contain comparative periods.

```sql
SELECT
    cik,
    concept,
    period_end,
    arg_max(val_num, filed)  AS val_num,
    arg_max(decimals, filed) AS decimals,
    arg_max(fact_id, filed)  AS fact_id
FROM read_parquet('lake/xbrl/filed_year=*/*.parquet', hive_partitioning = true)
WHERE cik = $cik
  AND filed <= $as_of
  AND period_end IN ($period_t, $period_p)
  AND concept IN (SELECT concept FROM beneish_concept_allowlist)
GROUP BY cik, concept, period_end;
```

Report the benchmark with the dataset hash, hardware, query text, and engine version:

```python
import math
import time

import duckdb


def bench(con, sql: str, params: dict, runs: int = 30) -> dict:
    con.execute(sql, params).fetchall()
    samples = []
    for _ in range(runs):
        started = time.perf_counter()
        rows = con.execute(sql, params).fetchall()
        samples.append(time.perf_counter() - started)
    samples.sort()
    return {
        "engine": duckdb.__version__,
        "rows_returned": len(rows),
        "p50_s": samples[math.ceil(0.50 * runs) - 1],
        "p95_s": samples[math.ceil(0.95 * runs) - 1],
    }
```

| Metric | Result |
|---|---|
| Dataset rows and SHA-256 | `MEASURE` |
| Hardware and thread count | `MEASURE` |
| Cold-run time | `MEASURE` |
| Warm p50 / p95 | `MEASURE` |

## 3. Formal Verification Workflow

### 3.1 What each solver result means

| Query | Result | Meaning | Gate action |
|---|---|---|---|
| `B âˆ§ P` | `sat` | Evidence model is consistent | Continue |
| `B âˆ§ P` | `unsat` | Facts or policies conflict | Block and report an unsat core |
| `B âˆ§ P âˆ§ Â¬C` | `unsat` | Claim is entailed by the model | Pass this obligation |
| `B âˆ§ P âˆ§ Â¬C` | `sat` | Z3 found a counterexample | Block and retain the model |
| Any query | `unknown` | Timeout or incomplete result | Block |

**`sat` alone can't validate a recovery amount.** If the claim or a rate is under-constrained, Z3 can return `sat` for a wrong number by choosing a convenient assignment.

### 3.2 Discharge procedure

```python
# sovereignforensics/smt/gate.py
from dataclasses import dataclass

import z3

from sovereignforensics.smt.compiler import Compiler


@dataclass(frozen=True)
class Verdict:
    status: str
    smt2: str
    model: str | None = None


def _solve(assertions, timeout_ms: int):
    solver = z3.Solver()
    solver.set("timeout", timeout_ms)
    solver.add(assertions)
    return solver.check(), solver


def discharge(c: Compiler, goal: z3.BoolRef, timeout_ms: int = 30_000) -> Verdict:
    result, solver = _solve(c.bounds, timeout_ms)
    if result != z3.sat:
        status = "INCONSISTENT" if result == z3.unsat else "UNKNOWN"
        return Verdict(status, solver.to_smt2())

    result, solver = _solve(
        [*c.bounds, z3.Not(z3.And(c.defined))],
        timeout_ms,
    )
    if result != z3.unsat:
        status = "UNDEFINED" if result == z3.sat else "UNKNOWN"
        return Verdict(status, solver.to_smt2())

    result, solver = _solve([*c.bounds, *c.defined, z3.Not(goal)], timeout_ms)
    if result == z3.unsat:
        return Verdict("PROVED", solver.to_smt2())
    if result == z3.sat:
        return Verdict("REFUTED", solver.to_smt2(), str(solver.model()))
    return Verdict("UNKNOWN", solver.to_smt2())
```

### 3.3 Beneish M-Score bound

The eight-factor model is:

```text
M = -4.84 + 0.920Â·DSRI + 0.528Â·GMI + 0.404Â·AQI + 0.892Â·SGI
    + 0.115Â·DEPI - 0.172Â·SGAI + 4.679Â·TATA - 0.327Â·LVGI
```

The proof obligation asks whether any value in the reported rounding ranges reaches the threshold:

```text
Prove:  âˆ€x âˆˆ B(L): M(x) < -1.78
Query:  B(L) âˆ§ defined(M) âˆ§ M(x) â‰¥ -1.78
Pass:   unsat
```

```python
# sovereignforensics/smt/beneish.py
from dataclasses import dataclass

import z3

from sovereignforensics.smt.compiler import Compiler


@dataclass(frozen=True)
class Period:
    rec: z3.ArithRef
    sales: z3.ArithRef
    cogs: z3.ArithRef
    ca: z3.ArithRef
    ppe: z3.ArithRef
    ta: z3.ArithRef
    dep: z3.ArithRef
    sga: z3.ArithRef
    ltd: z3.ArithRef
    cl: z3.ArithRef
    ni: z3.ArithRef
    cfo: z3.ArithRef


def period(c: Compiler, prefix: str) -> Period:
    return Period(**{
        name: c.bind(f"{prefix}:{name}")
        for name in Period.__dataclass_fields__
    })


def m_score(c: Compiler, t: Period, p: Period) -> z3.ArithRef:
    d = c.div
    dsri = d(d(t.rec, t.sales), d(p.rec, p.sales))
    gmi = d(d(p.sales - p.cogs, p.sales), d(t.sales - t.cogs, t.sales))
    aqi = d(1 - d(t.ca + t.ppe, t.ta), 1 - d(p.ca + p.ppe, p.ta))
    sgi = d(t.sales, p.sales)
    depi = d(d(p.dep, p.dep + p.ppe), d(t.dep, t.dep + t.ppe))
    sgai = d(d(t.sga, t.sales), d(p.sga, p.sales))
    lvgi = d(d(t.ltd + t.cl, t.ta), d(p.ltd + p.cl, p.ta))
    tata = d(t.ni - t.cfo, t.ta)
    return (
        z3.Q(-484, 100)
        + z3.Q(920, 1000) * dsri
        + z3.Q(528, 1000) * gmi
        + z3.Q(404, 1000) * aqi
        + z3.Q(892, 1000) * sgi
        + z3.Q(115, 1000) * depi
        - z3.Q(172, 1000) * sgai
        + z3.Q(4679, 1000) * tata
        - z3.Q(327, 1000) * lvgi
    )


def below_threshold(
    c: Compiler,
    t: Period,
    p: Period,
    threshold: z3.ArithRef = z3.Q(-178, 100),
) -> z3.BoolRef:
    return m_score(c, t, p) < threshold
```

**Sanity vector:** when all seven indexes equal 1 and `TATA = 0`, `M = -2.48`.

**Limits:**

- The M-Score is a statistical screen, so a score below the threshold does not establish non-manipulation, and a score above it does not establish fraud.
- Variable intervals make the problem nonlinear, so Z3 may return `unknown`, which blocks release.
- Quarterly results need a separately validated trailing-twelve-month method because the original model isn't a direct 10-Q test.
- Financial firms and other poor-fit sectors should be marked out of scope.

### 3.4 Recovery verification

For ad valorem lines:

```text
owed(â„“)   = entered_value(â„“) Ã— correct_rate(â„“)
refund(â„“) = duty_paid(â„“) - owed(â„“)
R         = Î£ refund(â„“)
```

```python
# sovereignforensics/smt/recovery.py
import z3

from sovereignforensics.smt.compiler import Compiler


def recovery_goals(
    c: Compiler,
    lines: list[str],
    claim_id: str,
    tolerance_id: str,
    protest_day_id: str,
    liquidation_day_id: str,
    protest_window_id: str,
) -> dict[str, z3.BoolRef]:
    if not lines:
        raise ValueError("Recovery claim has no entry lines")

    paid = [c.bind(f"{line}:duty_paid") for line in lines]
    owed = [
        c.bind(f"{line}:entered_value") * c.bind(f"{line}:correct_rate")
        for line in lines
    ]
    refunds = [line_paid - line_owed for line_paid, line_owed in zip(paid, owed)]
    total = z3.Sum(refunds)
    claim = c.bind(claim_id)
    tolerance = c.bind(tolerance_id)
    difference = claim - total

    return {
        "claim_matches_ledger": z3.And(
            difference <= tolerance,
            -difference <= tolerance,
        ),
        "claim_not_above_paid": claim <= z3.Sum(paid),
        "line_refunds_non_negative": z3.And([r >= 0 for r in refunds]),
        "protest_timely": (
            c.bind(protest_day_id)
            <= c.bind(liquidation_day_id) + c.bind(protest_window_id)
        ),
    }
```

**Synthetic example:**

| Line | Entered value | Duty paid | Correct rate | Owed | Refund |
|---|---:|---:|---:|---:|---:|
| 1 | $100,000 | $25,000 | 10% | $10,000 | $15,000 |
| 2 | $40,000 | $10,000 | 25% | $10,000 | $0 |
| **Total** | | | | | **$15,000** |

With a $0.01 tolerance, a $15,000 claim proves `claim_matches_ledger`, while a $15,500 claim returns `REFUTED`.

**The solver doesn't decide:**

- Whether `correct_rate`, the HTS classification, country of origin, or valuation is legally correct
- Whether a protest, post-summary correction, drawback claim, or other remedy is the right route
- Whether the claimant has standing or the entry has reached finality
- How specific or compound duties, fees, and interest apply unless they are explicitly modeled

For a protestable customs decision, 19 U.S.C. Â§ 1514 generally sets a 180-day window after liquidation, and the filing is a protest rather than a demand letter. Counsel should confirm the remedy and deadline for each claim. Store the window as a versioned policy fact.

### 3.5 Release flow

```text
Load ledger facts
      |
      v
Bounds satisfiable? ----- no ----> BLOCK: INCONSISTENT + unsat core
      | yes
      v
All denominators nonzero? -- no -> BLOCK: UNDEFINED
      | yes
      v
Negated goal unsat? ------ sat --> BLOCK: REFUTED + counterexample
      |         \--------- unknown -> BLOCK: UNKNOWN
      | unsat
      v
TruLens and numeric checks pass? -- no -> BLOCK: manual review
      | yes
      v
Generate DRAFT + evidence bundle
      |
      v
Counsel reviews and decides
```

```python
# sovereignforensics/package/release.py
from sovereignforensics.smt.gate import Verdict


def may_render_draft(
    verdicts: dict[str, Verdict],
    triad_passed: bool,
    numbers_grounded: bool,
) -> bool:
    return (
        bool(verdicts)
        and all(v.status == "PROVED" for v in verdicts.values())
        and triad_passed
        and numbers_grounded
    )
```

Each evidence bundle should contain:

- Source document SHA-256 hashes and page or accession references
- The ledger snapshot and policy version
- Every SMT-LIB query, verdict, and counterexample
- Z3, DuckDB, and TruLens versions
- Model digest, prompt hash, and TruLens record ID
- A named counsel-review field, left blank until completed

### 3.6 Required test matrix

| Test | Input | Expected result |
|---|---|---|
| Neutral Beneish vector | All indexes 1, `TATA = 0` | `M = -2.48` |
| Threshold breach | `TATA = 0.20` | `REFUTED` |
| Rounding sensitivity | Point value passes, interval crosses threshold | `REFUTED` |
| Zero denominator | Prior-period sales range includes 0 | `UNDEFINED` |
| Contradictory facts | Same fact ID with conflicting source values | Ingestion or `INCONSISTENT` failure |
| Tampered claim | Add $500 to claim | `REFUTED` |
| Late protest | Protest day outside policy window | `REFUTED` |
| Solver timeout | Very small timeout on a nonlinear query | `UNKNOWN`, blocked |
| Hostile IR | Literal or unknown field | Pydantic rejection |
| Unknown fact | Reference missing from ledger | `KeyError`, blocked |
| Empty quantifier | Entry with no lines | `ValueError`, blocked |
| Nonlocal endpoint | Remote LLM URL | Startup failure |

## 4. TruLens RAG Triad Telemetry

The triad measures narrative retrieval quality, while Z3 tests formal claims. A high TruLens score can't override a failed proof, and a successful proof doesn't show that the surrounding narrative is well grounded.

```text
             +----------------------+
             |    Query q           |
             +---+--------------+---+
                 |              |
 Context         |              | Answer
 Relevance       |              | Relevance
                 v              v
      +----------------+   +----------+
      | Contexts C     |-->| Answer a |
      +----------------+   +----------+
              Groundedness
```

### 4.1 Metrics

For judge functions that return scores in `[0,1]`:

**Context relevance** measures whether the retrieved passages fit the question:

```text
CR(q, C) = (1 / |C|) Ã— Î£ f_cr(q, c_i)
```

**Groundedness** measures whether each answer statement is supported by at least one passage:

```text
G(a, C) = (1 / |S(a)|) Ã— Î£ max f_g(s_j, c_i)
                          i
```

**Answer relevance** measures whether the response addresses the question:

```text
AR(q, a) = f_ar(q, a)
```

The gate should require every metric to pass, since a high average can hide one serious failure:

```text
PASS = CR â‰¥ Ï„_cr âˆ§ G â‰¥ Ï„_g âˆ§ AR â‰¥ Ï„_ar
```

**Illustrative example:**

```text
Context scores:      0.9, 0.8, 0.2, 0.1   -> CR = 0.50
Statement supports:  1.0, 0.9, 0.2        -> G  = 0.70
Answer relevance:    0.9                  -> AR = 0.90

With Ï„_cr = 0.70, Ï„_g = 0.90, Ï„_ar = 0.80:
Result = BLOCK
```

These thresholds are placeholders. Calibrate them on a labeled set of filings and customs narratives, then record the judge model and version. Scores from different judges aren't directly comparable.

### 4.2 Instrumentation

```python
# sovereignforensics/telemetry/trulens_triad.py
import os

import numpy as np
from trulens.apps.app import TruApp, instrument
from trulens.core import Feedback, Select, TruSession
from trulens.providers.litellm import LiteLLM


class ForensicRag:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    @instrument
    def retrieve(self, query: str) -> list[str]:
        return self.retriever(query)

    @instrument
    def query(self, query: str) -> str:
        return self.generator(query, self.retrieve(query))


def build_recorder(app: ForensicRag) -> TruApp:
    TruSession()
    provider = LiteLLM(
        model_engine=os.environ["SF_JUDGE_ALIAS"],
        api_base=os.environ["SF_LOCAL_JUDGE_URL"],
    )
    contexts = Select.RecordCalls.retrieve.rets

    context_relevance = (
        Feedback(
            provider.context_relevance_with_cot_reasons,
            name="Context Relevance",
        )
        .on_input()
        .on(contexts[:])
        .aggregate(np.mean)
    )
    groundedness = (
        Feedback(
            provider.groundedness_measure_with_cot_reasons,
            name="Groundedness",
        )
        .on(contexts.collect())
        .on_output()
    )
    answer_relevance = (
        Feedback(provider.relevance_with_cot_reasons, name="Answer Relevance")
        .on_input()
        .on_output()
    )

    return TruApp(
        app,
        app_name="SovereignForensics",
        app_version=os.environ["SF_BUILD_SHA"],
        feedbacks=[context_relevance, groundedness, answer_relevance],
    )
```

The judge should use the same loopback guard as extraction when records contain confidential data. TruLens selector APIs have changed across releases, so test this module against the pinned version.

### 4.3 Deterministic numeric groundedness

TruLens groundedness is a model judgment, so legal draft numbers need a stricter check:

```text
For every number n in the draft:
  1. n must resolve to a ledger fact ID or a PROVED derived value
  2. Rendered value must exactly match that source after declared formatting
  3. Any unmatched number blocks release
```

Render financial values from verified data rather than letting the model type them. Use the model for surrounding prose only, then apply this check to the finished draft.

## 5. End-to-End Sequence

```text
Parser      DuckDB      Glimmer     Compiler     Z3      TruLens    Counsel
  |            |           |            |         |          |          |
  |--facts---->|           |            |         |          |          |
  |            |--text---->|            |         |          |          |
  |            |<--IR------|            |         |          |          |
  |            |--ledger + IR---------->|         |          |          |
  |            |           |            |--SMT--->|          |          |
  |            |           |            |<-verdict|          |          |
  |            |--contexts + draft answer------------------->|          |
  |            |<-----------------------------triad scores---|          |
  |            |--PASS: draft + evidence bundle----------------------->|
  |            |           |            |         |          | decision |
```

## 6. Assurance Summary

| Layer | Provides | Doesn't provide |
|---|---|---|
| Deterministic parsing | Traceable, typed facts | Proof that the source filing is true |
| DuckDB | Fast, reproducible queries | Legal or accounting validity |
| Glimmer | Candidate claims and concept mappings | Trusted facts or proof |
| Z3 | Sound results for the encoded formulas, subject to solver correctness | Correct real-world modeling or legal entitlement |
| Beneish | A statistical manipulation screen | A finding of fraud or innocence |
| TruLens | Judged retrieval and answer quality | Formal proof or factual certainty |
| Counsel | Legal judgment and the decision to act | Automated assurance |

**The defensible system claim is:** SovereignForensics binds claims to source evidence, blocks release when formal checks or grounding checks fail, and gives counsel a reproducible record for review.