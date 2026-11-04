### Benchmark Architecture & Scope

The benchmark runs **50 adjudicated cases** through four stack configurations under identical prompts, identical source filings, and identical grading rubrics. Every case is scored on three independent axes: numerical accuracy against a CPA-reviewed ground truth, a Z3 SMT proof of the recovery or distortion arithmetic, and compliance with the UPL / `safeEmit` output gate.

| Cohort | Cases | Source corpus | Primary exposure |
| :--- | :---: | :--- | :--- |
| SEC 10-K accounting restatements | 20 | Form 10-K / 10-K/A, Item 4.02 and 4.01 8-Ks | ASC 606 cutoff and restatement distortion |
| SEC 10-K IEEPA / Section 301 tariff surcharge | 15 | Form 10-K, customs and trade disclosures | Tariff pass-through, drawback, and overcharge recovery |
| Multi-FEIN statutory tax / Kovel controversies | 15 | State and federal statutory filings | Excise, sales/use, and fuel-credit recovery under privilege controls |
| **Total** | **50** | | |

### Executive Summary

| Metric | Result |
| :--- | :--- |
| Cases evaluated | **50** (20 + 15 + 15) |
| Total identified recovery opportunity | **$1,228,800,000.00** |
| Total identified ASC 606 cutoff / restatement distortion | **$15,582,000,000.00** |
| Z3 SMT proof soundness | **50/50 cases (100.0%)**, every negated claim returned `unsat` |
| Accuracy, full neuro-symbolic stack | **100.0%** (50/50) |
| Arithmetic error rate, full neuro-symbolic stack | **0.000%** |
| UPL / `safeEmit` compliance | **100.0%** |

The gap between the neuro-symbolic stack and the unverified baseline is structural. Language models produce plausible figures but cannot prove them. In this design the model proposes, DuckDB computes, and Z3 refutes. No figure reaches output unless the negation of its claim is unsatisfiable.

### 4-Stack Comparative Benchmark Matrix

| Stack Architecture | Accuracy | Math Error Rate | Z3 SMT Verified | Median Latency | UPL / safeEmit Compliance | Marginal Cost |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SovereignForensics Neuro-Symbolic Stack** (Meta `muse-wonder-full-1.0` 1M + Fireworks `muse-glimmer-30b` LoRA SFT + Baseten NVFP4 + SAM-3.1 + DuckDB + Z3 SMT) | **100.0%** (50/50) | **0.000%** | **100.0%** (50/50 SAT) | **0.84s** | **100.0%** | **$0.00** |
| **Fireworks muse-glimmer-30b LoRA SFT** (Standalone Cloud API) | 94.0% (47/50) | 2.40% | 0.0% (Unverified) | 1.12s | 96.0% | $0.0004 |
| **Base muse-glimmer-30b** (Pre-SFT Zero-Shot) | 82.0% (41/50) | 8.70% | 0.0% (Unverified) | 1.15s | 82.0% | $0.0004 |
| **Unverified Generic Cloud LLM Baseline** (No DuckDB / No Z3 SMT) | 64.0% (32/50) | 23.80% | 0.0% (0/50 Proofs) | 4.85s | 48.0% | $0.0150 |

**Reading the matrix.**
- LoRA SFT lifts accuracy from 82.0% to 94.0% and cuts the error rate from 8.70% to 2.40%.
- Only the addition of DuckDB deterministic computation and Z3 refutation closes the remaining gap to 0.000%.
- The full stack is also the fastest configuration, at 0.84s median latency against 4.85s for the generic baseline.
- Compliance falls from 100.0% to 48.0% across the stack ladder. Without a deterministic output gate, a model drifts into legal conclusions that cross the UPL boundary.

---

### Feature 4 Deep-Dive Case Study Teardowns

**Proof convention.** Each case below encodes its governing arithmetic as an SMT-LIB assertion set. The *negation* of the claim is asserted, and `unsat` proves the claim holds for every admissible input. The snippets are minimal reproductions of the constraint structure.

#### Case Study 1: United Parcel Service (UPS), CIK 0001090727

**$500,000,000 Tariff Surcharge Pass-Through Escrow & Duty Drawback**

| Element | Detail |
| :--- | :--- |
| Exposure | $500,000,000 in tariff-driven surcharges held in a pass-through escrow position |
| Drawback authority | 19 U.S.C. § 1313 (drawback capped at 99% of duties paid) |
| Contract recovery | UCC § 2-717 (deduction of damages from price due) |
| Forum | Court of International Trade, 28 U.S.C. § 1581(i) (residual jurisdiction) |

**Forensic finding.** The escrow balance is recoverable by customers only to the extent that duties were actually paid and not already refunded through drawback. The statutory 99% ceiling bounds the drawback leg. Any claim above that ceiling is mathematically unsupportable.

```smt2
; Drawback cap: R <= 99% of duties paid D (19 U.S.C. § 1313)
(declare-const D Int)
(declare-const R Int)
(assert (= D 500000000))
(assert (>= R 0))
(assert (<= (* 100 R) (* 99 D)))
; Negated claim: "drawback can exceed $495,000,000"
(assert (> R 495000000))
(check-sat)   ; => unsat  (claim R <= 495,000,000 proven)
```

#### Case Study 2: Medline Industries & Hospital GPO Network, CIK 0001861750

**$89,000,000 Healthcare PPE Tariff Overcharge Recovery**

| Element | Detail |
| :--- | :--- |
| Exposure | $89,000,000 in tariff-driven PPE overcharges across a hospital GPO network |
| Price mechanics | UCC § 2-305 (open price term) and § 2-717 (setoff of damages against price) |
| Regulatory constraint | 42 C.F.R. § 1001.952(d), Anti-Kickback safe harbor treatment of the recovery flow |

**Forensic finding.** Recovery distribution to GPO members must be fully conserved, with no residual that could be characterized as remuneration outside the safe harbor. The proof below shows that member recoveries plus the administrative fee exactly exhaust the $89M, and that the fee cap forces a minimum member pass-through.

```smt2
; Conservation: members + GPO fee = recovery; fee capped at 3% (modeled written-agreement parameter)
(declare-const members Int)
(declare-const fee Int)
(assert (>= members 0))
(assert (>= fee 0))
(assert (= (+ members fee) 89000000))
(assert (<= (* 100 fee) (* 3 89000000)))
; Negated claim: "members receive less than $86,330,000"
(assert (< members 86330000))
(check-sat)   ; => unsat
```

#### Case Study 3: Super Micro Computer (SMCI), CIK 0001375365

**ASC 606 Revenue Recognition Cutoff & Auditor Resignation**

| Indicator | Value | Interpretation |
| :--- | :--- | :--- |
| Beneish M-Score | **3.68** | Far above the −1.78 manipulation threshold (8-variable model) |
| Dechow F-Score | **0.841** | Model output as computed by the stack |
| ASC 606 cutoff distortion | **$580,000,000** | Revenue recognized ahead of the control-transfer date |
| Trigger event | **Item 4.01 8-K** | Independent auditor resignation |

**Forensic finding.** Under ASC 606-10-25-30, revenue is recognized when control transfers, not when an order is booked or goods are staged. A $580M cutoff distortion combined with an M-Score roughly 5.46 points above the threshold, followed by an Item 4.01 auditor change, is a convergent red-flag pattern that warrants escalation.

```smt2
; Beneish threshold test (Reals)
(declare-const m Real)
(assert (= m 3.68))
; Negated claim: "M-Score is at or below the -1.78 manipulation threshold"
(assert (<= m (- 1.78)))
(check-sat)   ; => unsat  (M > -1.78 proven; margin = 5.46)
```

#### Case Study 4: Commonwealth Mfg & Cold-Chain Fleet

**Multi-FEIN Energy and Fuel Excise Recovery: $3,600,000**

| Element | Detail |
| :--- | :--- |
| Kentucky sales/use leg | KRS 139.470(9), energy-use exemption on manufacturing inputs |
| Federal fuel leg | IRC § 6427(l), refund for nontaxable-use diesel fuel |
| Entity structure | Multiple FEINs; recovery must not double-count across entities |
| Privilege architecture | Kovel arrangement, with analysis performed under an accountant-of-counsel engagement (*United States v. Heppner*) |

**Forensic finding.** Across the FEIN group, the state and federal legs must sum to exactly $3,600,000 with no overlap. Privilege is preserved by routing all work product through the Kovel engagement and gating every output through `safeEmit`, so no legal conclusion is emitted to the client directly.

```smt2
; Cross-FEIN conservation: state leg + federal leg = $3.6M, no negative legs
(declare-const ky Int)
(declare-const fed Int)
(assert (>= ky 0))
(assert (>= fed 0))
(assert (= (+ ky fed) 3600000))
; Negated claim: "either leg alone exceeds the total recovery"
(assert (or (> ky 3600000) (> fed 3600000)))
(check-sat)   ; => unsat
```

---

### Reproducibility

- All 50 proofs are re-executable from the case ledger. Each case stores its source filing hash, the DuckDB query that produced the inputs, and the SMT-LIB file.
- A case counts as passing only if the negated claim returns `unsat`. Any `sat` or `unknown` result blocks emission through `safeEmit`.
- Latency is measured end to end, including DuckDB execution and Z3 solve time. Marginal cost is per-case inference spend excluding fixed infrastructure.

---

**Notes before you publish** (not part of the README text):

1. **Figures are as you supplied them.** I did not verify the benchmark numbers, the $500M / $89M / $580M / $3.6M amounts, or the Medline CIK against filings. The SMT snippets encode your stated figures and statutory caps. The Medline 3% fee and the Commonwealth state/federal split are placeholders, since you gave no inputs for them.
2. **Dechow F-Score 0.841.** F-Scores are usually read relative to 1.0, where above 1.0 means elevated risk. A 0.841 reads as below-average risk and sits oddly beside the 3.68 M-Score. I left it as "model output," but judges may question it, so confirm the scaling.
3. **42 C.F.R. § 1001.952(d)** is the personal-services/management-contracts safe harbor. The GPO safe harbor is § 1001.952(j). Verify which one you intend.
4. ***United States v. Heppner*** is, to my knowledge, a recent ruling about AI-generated material and privilege. It may cut against a privilege shield rather than support one. The foundational Kovel authority is *United States v. Kovel*, 296 F.2d 918 (2d Cir. 1961). Check the citation before submission.
5. **KRS 139.470(9)** should be checked against the current statute text.
6. You asked for output starting at `### Benchmark Architecture & Scope`, so the `## 3.5. ...` heading is omitted. Add it above when embedding.
