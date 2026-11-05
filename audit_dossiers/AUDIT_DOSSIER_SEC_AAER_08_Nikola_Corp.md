# SovereignForensics // Forensic Audit Dossier & Statutory Recovery Action: Nikola Corp

| Field | Value |
|---|---|
| Case ID | SEC_AAER_08 |
| Target Entity | Nikola Corp (NKLA) |
| CIK | 0001731289 |
| Accession Number (as supplied) | 0001731289-21-000018 |
| Category | sec_accounting_restatement |
| Core Issue | Pre-order reservation revenue recognition claims; non-binding commercial truck letters of intent (LOIs) |
| Statutory Basis | ASC 606-10-25-1 (criteria for identifying a contract with a customer) |
| Formal Proof Status | SAT (counterexample to the recognition gate exists) |
| Dossier Date | 2026-11-04 |
| Classification | Draft-to-ready. No outward action taken. |

**Integrity notice before anything else.** Every number in this dossier is either (a) a packet input reproduced verbatim, (b) derived from packet inputs by arithmetic shown inline, or (c) public-record context explicitly labeled as outside the packet. Two packet inputs could not be reconciled with the supplied financials and are flagged rather than smoothed over: the Sloan accrual figure and the Dechow logit interpretation (see Â§2.4 and Â§2.5). The packet's $45,000,000 cutoff distortion is a modeled figure; it is not a number taken from a filed Nikola restatement, and this dossier does not represent it as such.

---

## 1. Executive Summary & Exposure Classification

### 1.1 Immediate Financial Impact

The packet asserts a $45,000,000 ASC 606 cutoff distortion arising from the treatment of non-binding reservations and LOIs as if they satisfied the contract-existence gate in ASC 606-10-25-1. Measured against the supplied balance sheet and income statement:

| Base | Supplied value | $45,000,000 as % of base | Computation |
|---|---|---|---|
| Total assets | $1,200,000,000 | 3.750% | 45,000,000 / 1,200,000,000 |
| Total equity | $850,000,000 | 5.294% | 45,000,000 / 850,000,000 |
| Net loss (absolute) | $690,000,000 | 6.522% | 45,000,000 / 690,000,000 |
| CFO (absolute) | $320,000,000 | 14.063% | 45,000,000 / 320,000,000 |

Under the conventional SAB 99 rule-of-thumb screen (5% of the relevant earnings base), the distortion clears the quantitative threshold on both the equity and net-loss bases. SAB 99 also makes clear that qualitative factors (masking a trend, affecting compliance with covenants, concealing an unlawful transaction, management compensation effects) can render even a sub-threshold amount material. All four qualitative factors are plausibly implicated where the distortion relates to the company's headline demand narrative.

**Pro forma restatement vector** (packet financials with the $45,000,000 reversed as a reduction to reported income and equity, with the offsetting entry to contract liability or reversal of a receivable; CFO unchanged because the reversal is a non-cash accrual adjustment):

| Line | As supplied | Adjustment | Pro forma |
|---|---|---|---|
| Assets | 1,200,000,000 | âˆ’45,000,000 (receivable reversal case) | 1,155,000,000 |
| Liabilities | 350,000,000 | 0 | 350,000,000 |
| Equity | 850,000,000 | âˆ’45,000,000 | 805,000,000 |
| Net income | âˆ’690,000,000 | âˆ’45,000,000 | âˆ’735,000,000 |
| CFO | âˆ’320,000,000 | 0 | âˆ’320,000,000 |
| Accruals (NI âˆ’ CFO) | âˆ’370,000,000 | âˆ’45,000,000 | âˆ’415,000,000 |

Identity check, pro forma: 350,000,000 + 805,000,000 = 1,155,000,000. Holds.
(If consideration was actually collected, the alternative entry is a $45,000,000 contract liability under ASC 606-10-25-7, leaving assets unchanged at $1,200,000,000 and lifting liabilities to $395,000,000; equity lands at $805,000,000 either way. Both branches are encoded in the Z3 proof in Â§4.)

### 1.2 Likelihood of Recovery

**Statutory Recovery Opportunity: $0.00, as supplied.** This is the correct answer, not a gap. ASC 606-10-25-1 is a recognition standard. It governs what may be booked; it confers no cause of action and no monetary remedy on any party. The three commercial recovery statutes named in the brief (UCC Â§ 2-717, UCC Â§ 2-305, 19 U.S.C. Â§ 1313) each require a fact pattern absent from this packet (see Â§3). Recovery, where it exists at all for a case of this type, flows through other channels:

- **Issuer-side**: clawback from responsible officers under SOX Â§ 304 and Exchange Act Rule 10D-1 (Dodd-Frank Â§ 954) on a restatement; indemnification and advancement disputes; D&O insurance.
- **Investor-side**: Exchange Act Â§ 10(b) / Rule 10b-5 private actions and SEC Fair Fund distributions.
- **Counterparty-side**: none on these facts. A non-binding LOI by definition creates no enforceable payment obligation to set off against.

None of these is a "statutory recovery" under the basis cited, so the figure stays at $0.00 and the Waterfall Distribution stays null.

### 1.3 Legal Exposure (Issuer)

| Exposure vector | Authority | Trigger on these facts |
|---|---|---|
| Books and records | Exchange Act Â§ 13(b)(2)(A) | Booking consideration on contracts that fail 606-10-25-1 |
| Internal accounting controls | Exchange Act Â§ 13(b)(2)(B) | Absence of a documented contract-existence gate before revenue entry |
| Periodic reporting | Exchange Act Â§ 13(a); Rules 12b-20, 13a-1, 13a-13 | Materially misstated periodic reports |
| Antifraud | Securities Act Â§ 17(a); Exchange Act Â§ 10(b), Rule 10b-5 | Scienter-based: knowing characterization of non-binding reservations as orders |
| Certifications | SOX Â§Â§ 302, 906 | False CEO/CFO certifications over misstated periods |
| Clawback | SOX Â§ 304; Rule 10D-1 | Triggered by any restatement, regardless of fault |

**Public-record context (outside the packet; included for calibration only).** The Commission announced settled charges against Nikola on 2021-12-21, with a $125,000,000 civil penalty, centered on misleading statements by the founder about products, technology, and the company's business prospects. The founder was separately convicted on securities and wire fraud counts in October 2022. An arbitration panel in 2023 awarded the company a recovery against the founder in connection with those statements. The company filed for Chapter 11 protection in February 2025. These facts shape the practical collectability picture but do not alter the packet's $0.00 statutory recovery under the 606 basis.

**Exposure classification: Tier 1 (Material / Antifraud-adjacent). Recovery classification: Nil on the cited basis.**

---

## 2. Core Forensic Anomaly Decomposition

### 2.1 Beneish M-Score, as supplied: 3.42

The eight-variable Beneish model:

```
M = âˆ’4.84 + 0.920Â·DSRI + 0.528Â·GMI + 0.404Â·AQI + 0.892Â·SGI
         + 0.115Â·DEPI âˆ’ 0.172Â·SGAI + 4.679Â·TATA âˆ’ 0.327Â·LVGI
```

Decision threshold: M > âˆ’1.78 flags a likely manipulator. The supplied value of 3.42 exceeds the threshold by 5.20 units. That is an extreme reading; in Beneish's calibration sample, scores above roughly 0 are rare even among confirmed manipulators.

**Component-level inputs are not in the packet.** Every ratio below needs prior-period comparatives (FY tâˆ’1), which were not supplied. This dossier therefore does not assign numeric values to individual components; doing so would be fabrication. What follows is the mechanism-level reading of each component against the Nikola fact pattern.

| Component | Formula | Why it matters here | Direction of distortion from the LOI issue |
|---|---|---|---|
| **DSRI** (Days Sales in Receivables Index) | (REC_t / SALES_t) / (REC_tâˆ’1 / SALES_tâˆ’1) | Booking consideration on non-binding LOIs creates receivables with no enforceable obligor. Receivables grow faster than real sales. | Upward. The single strongest 606-driven signal. |
| **GMI** (Gross Margin Index) | GM_tâˆ’1 / GM_t | For a pre-revenue or near-zero-revenue filer the denominator is unstable; the ratio can swing wildly on tiny revenue changes. | Unreliable. Flag as degenerate, not as evidence. |
| **AQI** (Asset Quality Index) | [1 âˆ’ (CA_t + PPE_t)/TA_t] / [1 âˆ’ (CA_tâˆ’1 + PPE_tâˆ’1)/TA_tâˆ’1] | Capitalized development and intangible-heavy balance sheets raise AQI. Not directly tied to the LOI issue. | Likely elevated for structural reasons; weak 606 signal. |
| **SGI** (Sales Growth Index) | SALES_t / SALES_tâˆ’1 | Recognizing $45,000,000 from reservations against a near-zero base produces a mathematically explosive SGI, which carries a 0.892 weight. | Strongly upward. Likely the dominant driver of a 3.42 reading. |
| **DEPI** (Depreciation Index) | Rate_tâˆ’1 / Rate_t | No link to the LOI issue. | Neutral. |
| **SGAI** (SG&A Index) | (SGA_t/SALES_t) / (SGA_tâˆ’1/SALES_tâˆ’1) | Negative weight. Inflated sales depress the index and reduce M, partly masking manipulation. | Downward (masking). |
| **LVGI** (Leverage Index) | (LTD_t + CL_t)/TA_t over prior | Supplied liabilities-to-assets is 350 / 1,200 = 0.2917. Prior period not supplied. | Indeterminate. |
| **TATA** (Total Accruals to Total Assets) | (NI âˆ’ CFO) / TA | Heaviest weight (4.679). Computed from packet: see Â§2.4. | Negative on the supplied numbers (see discussion). |

**Interpretive caution on M-Score for a pre-revenue filer.** DSRI, GMI, SGI, and SGAI all have revenue in a denominator. When period revenue is near zero, these indices are either undefined or dominated by numerical noise. A 3.42 M-Score for an entity at this stage should be read as "the model is screaming because its revenue-based inputs are degenerate," which is itself diagnostic: the only way to get a stable, large positive M for such a filer is to inject revenue that should not be there.

### 2.2 The Accounting Distortion in One Paragraph

A reservation or LOI that the counterparty may cancel without penalty is not a contract under ASC 606-10-25-1 because criterion (a) (parties approved and are committed to perform) fails on its face, and criterion (e) (collectability of substantially all consideration is probable) cannot be assessed when there is no obligation to pay. Under ASC 606-10-25-6, the entity must keep reassessing until the criteria are met. Under ASC 606-10-25-7, any consideration received before the criteria are met is a liability, not revenue, unless the entity has no remaining obligations and the consideration is nonrefundable, or the contract has been terminated. Treating such arrangements as "orders," "backlog," or recognized revenue misstates the top line, receivables, and equity, and it misrepresents demand to the market. That is the whole case.

### 2.3 Balance-Sheet and Cash-Flow Integrity Checks (packet inputs)

| Check | Computation | Result |
|---|---|---|
| Accounting identity | 350,000,000 + 850,000,000 = 1,200,000,000 | Holds |
| Accrual identity | âˆ’690,000,000 âˆ’ (âˆ’320,000,000) = âˆ’370,000,000 | Holds; matches supplied accruals |
| Cash conversion | CFO / NI = (âˆ’320) / (âˆ’690) = 0.4638 | Loss is 53.6% non-cash |
| Liabilities / Assets | 350 / 1,200 = 0.2917 | Low leverage |
| Equity / Assets | 850 / 1,200 = 0.7083 | Equity-funded loss absorber |

### 2.4 Sloan Accrual Anomaly: supplied 0.198 â€” DOES NOT RECONCILE

Sloan's accrual ratio is total accruals scaled by total assets (Sloan 1996 uses average total assets; the packet supplies only one balance sheet, so ending assets are used):

```
Accruals / Total Assets = âˆ’370,000,000 / 1,200,000,000 = âˆ’0.30833
```

The packet states 0.198. The supplied financials produce âˆ’0.308 (absolute 0.308). The difference cannot be explained by sign convention alone; |âˆ’0.308| â‰  0.198. Possible explanations, none verifiable from the packet: use of average assets with a prior-period denominator about 1.87 billion; use of operating accruals (excluding non-operating items) rather than NI âˆ’ CFO; or a transcription error upstream. **Treatment:** this dossier carries both values, labels 0.198 as "supplied, unreconciled," and uses âˆ’0.308 for any computation that depends on the ratio. This discrepancy is itself an evidentiary item and is encoded as an explicit check in Â§4.

Note the direction: a large *negative* accrual ratio is unusual for a revenue-inflation case (which typically pushes accruals positive). On the supplied numbers, the $45,000,000 distortion is small relative to a $370,000,000 negative accrual swing dominated by non-cash charges. The 606 issue is material to the narrative and to equity, but it is not the dominant driver of the accrual profile. Honest forensic work says so.

### 2.5 Dechow F-Score: supplied 0.814, labeled "logit"

Dechow, Ge, Larson & Sloan (2011) produce a predicted value from a logit, convert it to a probability, then scale by the unconditional misstatement rate (0.0037) to get an F-Score, where F > 1.0 means above-normal risk.

- If 0.814 is the **logit predicted value**: implied probability = 1 / (1 + e^(âˆ’0.814)) = 1 / (1 + 0.4431) = 0.6930. Scaled F-Score = 0.6930 / 0.0037 â‰ˆ 187. That is not a sensible F-Score; it implies the label is wrong.
- If 0.814 is the **F-Score itself**: it is *below* 1.0, meaning below-average misstatement risk, which contradicts the M-Score and the case category.
- If 0.814 is the **probability**: F-Score â‰ˆ 220, again non-sensible.

**Treatment:** the F-Score input is unusable as supplied. It is retained in the ledger as "supplied, interpretation unresolved" and given zero weight in the conclusion. The conclusion rests on the 606 analysis and the M-Score mechanism, not on the F-Score.

---

## 3. Statutory & Commercial Recovery Basis

### 3.1 Governing Recognition Standard: ASC 606-10-25-1

An entity shall account for a contract with a customer only when all of the following criteria are met:

| Criterion | Text (paraphrased) | Status for a non-binding reservation / LOI |
|---|---|---|
| (a) | Parties have approved the contract and are committed to perform their respective obligations | **Fails.** A reservation cancellable at will without penalty evidences no commitment. |
| (b) | Entity can identify each party's rights regarding goods or services to be transferred | Weak. Specifications, quantities, and delivery dates in LOIs are typically indicative, not fixed. |
| (c) | Entity can identify the payment terms | Weak-to-fails. "Price to be negotiated" is a hallmark of LOIs. |
| (d) | Contract has commercial substance | Arguably met for a bona fide fleet customer; not sufficient alone. |
| (e) | It is probable the entity will collect substantially all the consideration | **Fails.** Collectability cannot be probable where payment is not owed. |

Supporting provisions:
- **ASC 606-10-25-6**: if criteria are not met at inception, continue to assess; recognize only when met.
- **ASC 606-10-25-7**: consideration received before criteria are met is recognized as revenue only when (a) no remaining obligations and substantially all consideration received and nonrefundable, or (b) contract terminated and consideration nonrefundable. Otherwise, **liability**.
- **ASC 606-10-25-8**: the liability represents the obligation to transfer goods or refund consideration.
- **ASC 606-10-50**: disclosure of remaining performance obligations ("backlog") is limited to *contracts* within scope; non-binding reservations do not belong in the RPO disclosure.
- **ASC 250-10-45-23 and -24**: correction of an error in previously issued financial statements requires restatement.
- **SAB 99 (SAB Topic 1.M)** and **SAB 108**: materiality assessment and the dual (rollover/iron-curtain) method.

### 3.2 UCC Â§ 2-717 (Deduction of Damages from the Price)

Text: a buyer, on notifying the seller of an intention to do so, may deduct all or any part of the damages resulting from any breach of the contract from any part of the price still due under the same contract.

Prerequisites: (1) a contract for sale of goods under Article 2; (2) a breach by the seller; (3) price still due under *that same* contract; (4) notice.

Application: **Inapplicable.** The arrangements at issue are, by the packet's own description, non-binding. There is no "contract" in the Article 2 sense, no price due, and no breach to measure. A fleet customer holding a cancellable reservation has nothing to set off against, and Nikola has no price to set off from. Â§ 2-717 cannot generate recovery for any party. This is consistent with the $0.00 supplied figure.

### 3.3 UCC Â§ 2-305 (Open Price Term)

Text: parties may conclude a contract for sale even though price is not settled, in which case price is a reasonable price at the time for delivery, provided the parties *so intend*. Under Â§ 2-305(4), where the parties intend not to be bound unless price is fixed or agreed, and it is not, there is no contract.

Application: **Inapplicable, and affirmatively adverse to recognition.** Â§ 2-305 could in principle rescue a contract that is silent on price. It cannot rescue one where the parties expressly intend not to be bound. A non-binding LOI is the textbook Â§ 2-305(4) case: no contract. That conclusion dovetails with ASC 606-10-25-1(a): the accounting and the commercial-law analysis reach the same answer by independent routes, which strengthens the finding.

### 3.4 19 U.S.C. Â§ 1313 (Drawback)

Text: refund of up to 99% of duties, taxes, and fees paid on imported merchandise that is subsequently exported or destroyed, or used to manufacture exported articles (Â§ 1313(a), (b), (j)).

Prerequisites: duties actually paid on imports; exportation or destruction within five years; a filed drawback claim with CBP under 19 C.F.R. Part 190.

Application: **Inapplicable on the packet record.** No import entries, duty payments, or exportations are supplied. Drawback is a customs refund mechanism; it has no bearing on revenue recognition for domestic reservations. Carried at $0.00. (If a separate customs-side review identifies duty-paid imported components later exported in finished vehicles, that is a distinct workstream with its own evidence chain, not part of this dossier.)

### 3.5 Tax Code Touchpoints

- **IRC Â§ 451(b)**: for accrual taxpayers with an applicable financial statement, revenue is includible no later than when recognized in the AFS. Over-recognition for book purposes can therefore accelerate taxable income. For a loss company, the practical effect is a reduced NOL carryforward under Â§ 172, not a current cash tax cost. A restatement that reverses $45,000,000 of book revenue would, if the tax return followed book, restore up to $45,000,000 of NOL. That is a tax-attribute correction, not a "recovery," and is carried outside the $0.00 statutory figure.
- **IRC Â§ 451(c)**: advance payments may be deferred for one year; refundable reservation deposits generally are not "advance payments" and are excluded from income until the refund right lapses. This again confirms liability treatment, mirroring ASC 606-10-25-7.

### 3.6 Where Recovery Actually Lives (for completeness; not the cited basis)

| Channel | Authority | Claimant | Notes |
|---|---|---|---|
| Executive clawback | SOX Â§ 304; Exchange Act Rule 10D-1 | Issuer | Rule 10D-1 is no-fault; triggers on any required restatement of incentive-based compensation metrics. |
| Fair Fund | Sarbanes-Oxley Â§ 308 | Harmed investors via SEC | Dependent on Commission action. |
| Private 10b-5 | Exchange Act Â§ 10(b); PSLRA | Investors | Requires scienter, loss causation. |
| Indemnification / insurance | Charter, bylaws, D&O policy | Issuer | Fact-specific. |

**Recovery conclusion: $0.00 under ASC 606-10-25-1, UCC Â§ 2-717, UCC Â§ 2-305, and 19 U.S.C. Â§ 1313. Waterfall: null. The packet figures are confirmed, not merely accepted.**

---

## 4. Executable Z3 SMT Counterexample Proof

Self-contained. Requires `pip install z3-solver`. Integer arithmetic in whole USD throughout; percentages are cross-multiplied to avoid rationals. Every proof prints its own verdict and the script exits non-zero on any failure.

```python
#!/usr/bin/env python3
"""
SovereignForensics // SEC_AAER_08 // Nikola Corp (CIK 0001731289)
Z3 SMT verification of (1) packet arithmetic invariants,
(2) ASC 606-10-25-1 contract-existence gate counterexample (SAT),
(3) $0.00 statutory recovery bound (UNSAT of any positive recovery),
(4) SAB 99 materiality of the $45,000,000 cutoff distortion,
(5) Sloan accrual reconciliation failure (documented, not suppressed).
"""
from z3 import (Solver, Int, Bool, Implies, And, Or, Not, sat, unsat,
                IntVal, BoolVal)
import sys

FAILURES = []

def report(label, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f"  -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(label)

# -------------------------------------------------------------------
# Packet inputs (whole USD). Reproduced verbatim from SEC_AAER_08.
# -------------------------------------------------------------------
P_ASSETS      = 1_200_000_000
P_LIABILITIES =   350_000_000
P_EQUITY      =   850_000_000
P_NET_INCOME  =  -690_000_000
P_CFO         =  -320_000_000
P_ACCRUALS    =  -370_000_000
P_DISTORTION  =    45_000_000
P_RECOVERY    =             0
P_SLOAN_SUPPLIED_X1000 = 198       # 0.198 supplied, scaled x1000

# ===================================================================
# PROOF 1: Packet invariants are jointly satisfiable and the supplied
#          values are the UNIQUE model under the identities.
# ===================================================================
assets, liab, equity = Int('assets'), Int('liabilities'), Int('equity')
ni, cfo, accr = Int('net_income'), Int('cfo'), Int('accruals')

s1 = Solver()
s1.add(assets == P_ASSETS, liab == P_LIABILITIES, equity == P_EQUITY,
       ni == P_NET_INCOME, cfo == P_CFO, accr == P_ACCRUALS)
s1.add(assets == liab + equity)        # A = L + E
s1.add(accr == ni - cfo)               # Accruals = NI - CFO
r1 = s1.check()
report("P1 packet invariants satisfiable (A=L+E, Accr=NI-CFO)", r1 == sat)

# Uniqueness: fix A, L, NI, CFO; show equity and accruals are forced.
s1u = Solver()
e2, a2 = Int('equity_alt'), Int('accruals_alt')
s1u.add(P_ASSETS == P_LIABILITIES + e2, a2 == P_NET_INCOME - P_CFO)
s1u.add(Or(e2 != P_EQUITY, a2 != P_ACCRUALS))
report("P1u equity/accruals uniquely determined by identities",
       s1u.check() == unsat)

# ===================================================================
# PROOF 2: ASC 606-10-25-1 gate.  Recognition is permitted ONLY IF all
#          five criteria hold.  Given the LOI fact pattern (criterion
#          (a) commitment fails, (e) collectability fails), the
#          assertion "revenue was recognized" is a COUNTEREXAMPLE to
#          the gate.  Expected: SAT  (the violation is realizable).
# ===================================================================
crit_a = Bool('c_a_approved_and_committed')
crit_b = Bool('c_b_rights_identifiable')
crit_c = Bool('c_c_payment_terms_identifiable')
crit_d = Bool('c_d_commercial_substance')
crit_e = Bool('c_e_collectability_probable')
recognized = Bool('revenue_recognized_on_reservations')
lois_nonbinding = Bool('lois_are_nonbinding')
gate = And(crit_a, crit_b, crit_c, crit_d, crit_e)

s2 = Solver()
# Fact pattern from the packet
s2.add(lois_nonbinding == True)
s2.add(Implies(lois_nonbinding, Not(crit_a)))   # no commitment
s2.add(Implies(lois_nonbinding, Not(crit_e)))   # nothing owed => not probable
s2.add(recognized == True)                      # what the books did
# The counterexample: recognition occurred AND the gate was not met.
s2.add(Not(gate))
r2 = s2.check()
report("P2 ASC 606-10-25-1 counterexample (recognized AND NOT gate)",
       r2 == sat, f"solver={r2}")
if r2 == sat:
    m = s2.model()
    print("      model: crit_a =", m[crit_a], "| crit_e =", m[crit_e],
          "| recognized =", m[recognized])

# Contrapositive: under the same facts, "recognized AND gate" is UNSAT.
s2c = Solver()
s2c.add(lois_nonbinding == True,
        Implies(lois_nonbinding, Not(crit_a)),
        Implies(lois_nonbinding, Not(crit_e)),
        recognized == True, gate)
report("P2c no model exists in which recognition was compliant",
       s2c.check() == unsat)

# ===================================================================
# PROOF 3: Pro forma restatement vectors (both 606-10-25-7 branches).
#          Branch R: receivable reversal (assets fall).
#          Branch L: contract liability (liabilities rise).
#          Equity falls by exactly the distortion in both branches.
# ===================================================================
d = IntVal(P_DISTORTION)
pf_assets_R, pf_liab_R, pf_eq_R = Int('pfA_R'), Int('pfL_R'), Int('pfE_R')
pf_assets_L, pf_liab_L, pf_eq_L = Int('pfA_L'), Int('pfL_L'), Int('pfE_L')
pf_ni, pf_accr = Int('pf_ni'), Int('pf_accr')

s3 = Solver()
s3.add(pf_assets_R == P_ASSETS - d, pf_liab_R == P_LIABILITIES,
       pf_eq_R == P_EQUITY - d,
       pf_assets_R == pf_liab_R + pf_eq_R)
s3.add(pf_assets_L == P_ASSETS, pf_liab_L == P_LIABILITIES + d,
       pf_eq_L == P_EQUITY - d,
       pf_assets_L == pf_liab_L + pf_eq_L)
s3.add(pf_ni == P_NET_INCOME - d, pf_accr == pf_ni - P_CFO)
s3.add(pf_eq_R == pf_eq_L)              # equity effect branch-invariant
s3.add(pf_eq_R == 805_000_000, pf_ni == -735_000_000,
       pf_accr == -415_000_000, pf_assets_R == 1_155_000_000,
       pf_liab_L == 395_000_000)
report("P3 pro forma vectors reconcile in both 606-10-25-7 branches",
       s3.check() == sat)

# ===================================================================
# PROOF 4: SAB 99 quantitative materiality.  Show the NEGATION
#          (distortion < 5% of |NI| OR < 5% of equity) is UNSAT.
#          Cross-multiplied integer form: 100*D >= 5*BASE.
# ===================================================================
s4 = Solver()
s4.add(Or(100 * d < 5 * IntVal(abs(P_NET_INCOME)),
          100 * d < 5 * IntVal(P_EQUITY)))
report("P4 distortion >= 5% of BOTH |NI| and equity (negation UNSAT)",
       s4.check() == unsat,
       f"100*45,000,000=4,500,000,000 vs 5*690,000,000=3,450,000,000 "
       f"and 5*850,000,000=4,250,000,000")

# ===================================================================
# PROOF 5: Statutory recovery bound.  Each named basis requires a
#          predicate absent from the packet.  Any model with
#          recovery > 0 is UNSAT.
# ===================================================================
recovery = Int('statutory_recovery_usd')
art2_contract      = Bool('ucc_article2_contract_exists')
price_due          = Bool('price_still_due_same_contract')
seller_breach      = Bool('seller_breach')
intent_to_be_bound = Bool('parties_intend_to_be_bound')
duty_paid_import   = Bool('duty_paid_import_exists')
export_or_destroy  = Bool('exported_or_destroyed_within_5y')

ucc_2_717 = And(art2_contract, price_due, seller_breach)
ucc_2_305 = And(art2_contract, intent_to_be_bound)
usc_1313  = And(duty_paid_import, export_or_destroy)
asc_606   = BoolVal(False)   # recognition standard: never a recovery basis

s5 = Solver()
# Packet facts: LOIs non-binding => no Article 2 contract, no intent;
# no customs record supplied.
s5.add(art2_contract == False, intent_to_be_bound == False,
       duty_paid_import == False)
s5.add(Implies(recovery > 0, Or(ucc_2_717, ucc_2_305, usc_1313, asc_606)))
s5.add(recovery > 0)
report("P5 any positive statutory recovery is UNSAT on packet facts",
       s5.check() == unsat)

s5b = Solver()
s5b.add(recovery == P_RECOVERY, recovery >= 0)
report("P5b supplied recovery $0.00 is consistent", s5b.check() == sat)

# ===================================================================
# PROOF 6: Sloan accrual reconciliation.  The supplied 0.198 does NOT
#          equal accruals/assets from the packet.  This check is
#          expected to FAIL-to-reconcile and is reported as such; it
#          is an evidentiary flag, not a script error.
# ===================================================================
# accruals/assets = -370,000,000 / 1,200,000,000 = -0.30833...
# Integer test of |accr| * 1000 == 198 * assets:
#   370,000,000,000 vs 237,600,000,000  -> not equal.
s6 = Solver()
s6.add(IntVal(abs(P_ACCRUALS)) * 1000 == IntVal(P_SLOAN_SUPPLIED_X1000)
       * IntVal(P_ASSETS))
sloan_matches = (s6.check() == sat)
print(f"[INFO] P6 Sloan supplied=0.198 | computed=-0.30833 | "
      f"reconciles={sloan_matches}  (flagged, see dossier Â§2.4)")
# Document the computed value is exactly -37/120.
s6b = Solver()
s6b.add(IntVal(P_ACCRUALS) * 120 == IntVal(-37) * IntVal(P_ASSETS))
report("P6b computed Sloan ratio equals -37/120 exactly", s6b.check() == sat)

# -------------------------------------------------------------------
print("\nFORMAL VERDICT:",
      "SAT -- counterexample to ASC 606-10-25-1 gate is realizable; "
      "recovery bound = $0.00 proven; materiality proven."
      if not FAILURES else f"VERIFICATION FAILED: {FAILURES}")
sys.exit(0 if not FAILURES else 1)
```

**Expected output on a clean run:**

```
[PASS] P1 packet invariants satisfiable (A=L+E, Accr=NI-CFO)
[PASS] P1u equity/accruals uniquely determined by identities
[PASS] P2 ASC 606-10-25-1 counterexample (recognized AND NOT gate)  -- solver=sat
      model: crit_a = False | crit_e = False | recognized = True
[PASS] P2c no model exists in which recognition was compliant
[PASS] P3 pro forma vectors reconcile in both 606-10-25-7 branches
[PASS] P4 distortion >= 5% of BOTH |NI| and equity (negation UNSAT)  -- 100*45,000,000=4,500,000,000 vs 5*690,000,000=3,450,000,000 and 5*850,000,000=4,250,000,000
[PASS] P5 any positive statutory recovery is UNSAT on packet facts
[PASS] P5b supplied recovery $0.00 is consistent
[INFO] P6 Sloan supplied=0.198 | computed=-0.30833 | reconciles=False  (flagged, see dossier Â§2.4)
[PASS] P6b computed Sloan ratio equals -37/120 exactly

FORMAL VERDICT: SAT -- counterexample to ASC 606-10-25-1 gate is realizable; recovery bound = $0.00 proven; materiality proven.
```

The script has not been executed in this session (no tools were invoked). The expected output above is derived by hand from the constraints; run it before relying on it.

---

## 5. Actionable Legal Remediation & Demand Notice Template

Because the statutory recovery under the cited basis is $0.00, the correct instrument is not a monetary demand. It is a **Notice of Accounting Deficiency, Demand for Restatement Assessment, and Litigation Hold**, served on the issuer's Audit Committee with a 10-day cure period. The claim-calculation block is populated with the packet figures and expressly states the nil recovery so that no reader can mistake the notice for a collection letter.

---

```
                     NOTICE OF ACCOUNTING DEFICIENCY,
          DEMAND FOR RESTATEMENT ASSESSMENT, AND LITIGATION HOLD

VIA: Certified Mail (Return Receipt) and Electronic Delivery
DATE: [__________], 2026
REFERENCE: SEC_AAER_08 / CIK 0001731289 / Accession 0001731289-21-000018

TO:   Chair, Audit Committee of the Board of Directors
      Nikola Corporation
      [Registered agent / principal executive office address]
      cc: Chief Financial Officer; General Counsel; Independent Registered
          Public Accounting Firm (engagement partner)

FROM: [Counsel of Record / Authorized Representative]
      [Firm]
      [Address]

RE:   Recognition of Consideration on Non-Binding Reservations and
      Letters of Intent in Contravention of ASC 606-10-25-1

1. NATURE OF THE DEFICIENCY

   The undersigned has completed a forensic review of the periodic
   reports referenced above. The review identifies the recognition of
   consideration, receivables, and/or reported "orders" or "backlog"
   arising from reservations and letters of intent that, by their
   terms, were cancellable by the counterparty without penalty and
   contained no enforceable payment obligation.

   Such arrangements fail ASC 606-10-25-1(a) (approval and commitment)
   and ASC 606-10-25-1(e) (collectability probable). Under ASC
   606-10-25-6 and 606-10-25-7, no revenue may be recognized and any
   consideration received must be carried as a liability until the
   criteria are met. Inclusion of such arrangements in remaining
   performance obligation disclosures under ASC 606-10-50 is likewise
   improper.

2. CLAIM CALCULATION

   Measured cutoff distortion (modeled):           $ 45,000,000.00
   Reported total equity:                          $850,000,000.00
   Distortion as % of equity:                              5.294 %
   Reported net loss:                             ($690,000,000.00)
   Distortion as % of |net loss|:                          6.522 %
   SAB 99 quantitative threshold (5%):                   EXCEEDED

   Pro forma equity after correction:              $805,000,000.00
   Pro forma net loss after correction:           ($735,000,000.00)

   Statutory recovery demanded under
   ASC 606-10-25-1 / UCC 2-717 / UCC 2-305 /
   19 U.S.C. 1313:                                 $          0.00

   This notice does not demand payment. It demands corrective action.

3. DEMAND

   Within TEN (10) calendar days of receipt, the Audit Committee shall:

   (a) Confirm in writing that an ASC 250-10-45 error assessment has
       been commenced with respect to the matters above;
   (b) Produce the contract-existence analysis (ASC 606-10-25-1
       memorandum) supporting each reservation or LOI included in
       revenue, receivables, or RPO disclosure for the affected
       periods, or confirm that no such memorandum exists;
   (c) Confirm whether the independent auditor has been notified and
       whether an Item 4.02 Form 8-K (Non-Reliance on Previously
       Issued Financial Statements) determination is under evaluation;
   (d) Confirm that the incentive-compensation recovery policy adopted
       under Exchange Act Rule 10D-1 has been reviewed for
       applicability to any resulting restatement;
   (e) Identify the officer responsible for the ASC 606 recognition
       determination for the affected periods.

4. LITIGATION HOLD

   Effective immediately, preserve all documents, communications,
   electronically stored information, reservation and deposit ledgers,
   LOI drafts and executed versions, CRM and order-management system
   records, auditor workpapers in the Company's possession, and
   board/committee materials relating to reservations, orders, backlog,
   LOIs, and revenue recognition for fiscal years [____] through [____].
   Suspend any automatic deletion or rotation affecting such records.

5. CURE PERIOD AND CONSEQUENCE

   Failure to respond substantively within the 10-day period will be
   treated as a refusal to cure. The undersigned reserves all rights,
   including referral of this matter to the Company's independent
   auditor, the Public Company Accounting Oversight Board, and the
   Division of Enforcement of the U.S. Securities and Exchange
   Commission, and the commencement or support of any proceeding
   available at law or in equity.

6. RESERVATION OF RIGHTS

   Nothing herein waives any right, claim, or remedy. This notice is
   delivered without prejudice and is not an admission of any fact by
   the sender.

   ______________________________
   [Name], [Title]
   [Firm]
   [Bar No., if applicable]
   [Phone] | [Email]
```

---

**Delivery mechanics (for John).** This template is draft-to-ready only. Before any service: (1) confirm standing to send (shareholder, counterparty, counsel of record, or whistleblower route under Exchange Act Â§ 21F, which has its own form and confidentiality rules); (2) replace the modeled $45,000,000 with a figure traceable to source documents, or restate the notice as a demand for the Company to quantify; (3) route through licensed counsel. The send button is John's.

**Prepared by:**
John Webb & Co.
Louisville, KY
Direct: 502-693-2779

---

## 6. Verification & Chain of Custody

### 6.1 SHA-256 Integrity Manifest

Hashes were not computed in this session (no tools invoked). The manifest below is populated by running the command shown; do not accept any hash that was typed rather than generated.

| Artifact | Path | SHA-256 |
|---|---|---|
| Packet inputs (JSON) | `evidence/SEC_AAER_08/packet.json` | `[compute]` |
| Z3 verification script | `evidence/SEC_AAER_08/z3_proof.py` | `[compute]` |
| Z3 run log | `evidence/SEC_AAER_08/z3_proof.log` | `[compute]` |
| This dossier | `evidence/SEC_AAER_08/dossier.md` | `[compute]` |
| Filing (if retrieved) | `evidence/SEC_AAER_08/0001731289-21-000018/` | `[compute per file]` |

```powershell
Get-ChildItem -Recurse -File evidence\SEC_AAER_08 |
  Get-FileHash -Algorithm SHA256 |
  Select-Object Hash, Path |
  Export-Csv evidence\SEC_AAER_08\MANIFEST.sha256.csv -NoTypeInformation
```

Retrieval of the accession is a public-URL fetch; route it through the `local_cpu_research_v4` evidence runner so the raw bytes, fetch timestamp, and hash land in the claim ledger together.

### 6.2 DuckDB 2.0.0 LTS Schema

```sql
CREATE SCHEMA IF NOT EXISTS forensics;

CREATE TABLE forensics.packet_inputs (
  case_id            VARCHAR NOT NULL,
  cik                VARCHAR NOT NULL,
  ticker             VARCHAR,
  accession          VARCHAR,
  category           VARCHAR,
  assets_usd         DECIMAL(20,2) NOT NULL,
  liabilities_usd    DECIMAL(20,2) NOT NULL,
  equity_usd         DECIMAL(20,2) NOT NULL,
  net_income_usd     DECIMAL(20,2) NOT NULL,
  cfo_usd            DECIMAL(20,2) NOT NULL,
  accruals_usd       DECIMAL(20,2) NOT NULL,
  beneish_m          DECIMAL(8,4),
  dechow_f_supplied  DECIMAL(8,4),
  sloan_supplied     DECIMAL(8,4),
  distortion_usd     DECIMAL(20,2),
  recovery_usd       DECIMAL(20,2),
  statutory_basis    VARCHAR,
  ingested_at        TIMESTAMPTZ DEFAULT now(),
  packet_sha256      VARCHAR,
  PRIMARY KEY (case_id, accession),
  CHECK (assets_usd = liabilities_usd + equity_usd),
  CHECK (accruals_usd = net_income_usd - cfo_usd)
);

CREATE TABLE forensics.derived_metrics (
  case_id            VARCHAR NOT NULL,
  metric             VARCHAR NOT NULL,
  value              DECIMAL(20,6),
  numerator_usd      DECIMAL(20,2),
  denominator_usd    DECIMAL(20,2),
  source             VARCHAR,          -- 'packet' | 'derived' | 'public_record'
  reconciles         BOOLEAN,
  note               VARCHAR,
  PRIMARY KEY (case_id, metric)
);

CREATE TABLE forensics.z3_proof_log (
  case_id            VARCHAR NOT NULL,
  proof_id           VARCHAR NOT NULL,   -- P1, P1u, P2, P2c, P3, P4, P5, P5b, P6, P6b
  expected           VARCHAR NOT NULL,   -- 'sat' | 'unsat'
  observed           VARCHAR,
  passed             BOOLEAN,
  model_json         JSON,
  script_sha256      VARCHAR,
  run_at             TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (case_id, proof_id, run_at)
);

CREATE TABLE forensics.chain_of_custody (
  case_id            VARCHAR NOT NULL,
  artifact_path      VARCHAR NOT NULL,
  sha256             VARCHAR NOT NULL,
  fetched_from       VARCHAR,
  fetched_at         TIMESTAMPTZ,
  recorded_by        VARCHAR,
  PRIMARY KEY (case_id, artifact_path, sha256)
);

-- Seed: packet row
INSERT INTO forensics.packet_inputs VALUES (
  'SEC_AAER_08','0001731289','NKLA','0001731289-21-000018',
  'sec_accounting_restatement',
  1200000000.00, 350000000.00, 850000000.00,
  -690000000.00, -320000000.00, -370000000.00,
  3.4200, 0.8140, 0.1980, 45000000.00, 0.00,
  'ASC 606-10-25-1', now(), NULL
);

-- Seed: derived metrics (all values reproduced in dossier body)
INSERT INTO forensics.derived_metrics VALUES
 ('SEC_AAER_08','distortion_pct_assets',   0.037500, 45000000, 1200000000,'derived', TRUE, NULL),
 ('SEC_AAER_08','distortion_pct_equity',   0.052941, 45000000,  850000000,'derived', TRUE, 'SAB 99 5% exceeded'),
 ('SEC_AAER_08','distortion_pct_abs_ni',   0.065217, 45000000,  690000000,'derived', TRUE, 'SAB 99 5% exceeded'),
 ('SEC_AAER_08','sloan_computed',         -0.308333,-370000000,1200000000,'derived', FALSE,'supplied 0.198 does not reconcile'),
 ('SEC_AAER_08','cfo_to_ni',               0.463768,-320000000,-690000000,'derived', TRUE, NULL),
 ('SEC_AAER_08','liab_to_assets',          0.291667, 350000000, 1200000000,'derived', TRUE, NULL),
 ('SEC_AAER_08','dechow_prob_if_logit',    0.693000, NULL, NULL,'derived', FALSE,'label ambiguous; zero weight');
```

The two `CHECK` constraints on `packet_inputs` make the DuckDB layer reject any future packet whose identities fail, which is the cheapest arithmetic-hallucination guard available.

### 6.3 TruLens RAG Triad Evaluation

| Dimension | Definition | Self-assessment | Basis |
|---|---|---|---|
| **Groundedness** | Every claim in the answer is supported by retrieved context | High for packet-derived figures (all shown with arithmetic). Explicitly reduced for M-Score components (not computed; mechanism only), F-Score (unresolved), and public-record context (labeled, not retrieved this session). | Flags in Â§2.1, Â§2.4, Â§2.5, Â§1.3 |
| **Context Relevance** | Retrieved context is relevant to the question | Moderate. The packet is internally sufficient for the 606 analysis but lacks prior-period comparatives needed for Beneish components and lacks any customs or Article 2 facts for the named recovery statutes. | Â§2.1, Â§3.2 to Â§3.4 |
| **Answer Relevance** | The answer addresses the question asked | High. All six requested sections delivered. The $0.00 recovery was confirmed by proof rather than restated. | Â§1 to Â§6 |

Formal TruLens scoring requires an instrumented run with retrieval traces; the values above are analyst assessments and should be replaced by measured scores before the dossier is marked final.

### 6.4 Open Items Before "Final" Status

1. Execute `z3_proof.py` and attach the log; populate `z3_proof_log`.
2. Retrieve and hash accession 0001731289-21-000018; confirm it is the filing the packet intends (the accession-to-form mapping was not verified in this session).
3. Resolve the Sloan 0.198 provenance with whoever produced the packet.
4. Resolve whether 0.814 is a logit, probability, or F-Score.
5. Obtain FY tâˆ’1 comparatives if a numeric Beneish decomposition is required.
6. Route the Â§5 notice through licensed counsel before any service.

---

*End of dossier. Draft-to-ready; no outward action taken.*