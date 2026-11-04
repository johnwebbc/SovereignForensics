# SovereignForensics // TaxRiskOS: Autonomous Market-Wide Accounting Manipulation & Statutory Recovery Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.14+](https://img.shields.io/badge/Python-3.14%2B-brightgreen.svg)](https://python.org)
[![DuckDB Screener: 0.663s](https://img.shields.io/badge/DuckDB_Screen-0.663s-ffaa00.svg)](https://duckdb.org)
[![Meta Model Stack](https://img.shields.io/badge/Meta_Stack-muse--wonder--full--1.0_%7C_muse--spark--1.3_%7C_muse--glimmer--30b_%7C_sam--3.1-0081FB.svg)](https://api.meta.ai)
[![Z3 Formal Proof](https://img.shields.io/badge/SMT_Proof-Z3_0.0%25_Hallucination-purple.svg)](https://github.com/Z3Prover/z3)
[![Status: Hackathon Flagship](https://img.shields.io/badge/Meta_Global_Hackathon-Flagship_Submission-success.svg)](https://cerebralvalley.ai/e/meta-ai-developer-hackathon)

> **Meta Global AI Developer Hackathon Submission (`Application ID: b55d2cdb-9d50-4751-a7dc-9505f2f7e4d4`)**  
> **Tracks:** Startups Track ($500K) & Indie Developer Track ($500K)  
> **Themes:** *Push the Frontier* & *Build for Your World*  
> **Live Web Cockpit (Modal Cloud):** [https://johnwebbc--sovereign-forensics-warehouse-fastapi-warehouse-app.us-east.modal.run](https://johnwebbc--sovereign-forensics-warehouse-fastapi-warehouse-app.us-east.modal.run)  
> **Live Z3 SMT Audit API (Modal Cloud):** [https://johnwebbc--taxriskos-forensic-audit.us-east.modal.run](https://johnwebbc--taxriskos-forensic-audit.us-east.modal.run)  
> **Interactive Local Cockpit:** [`index.html`](./index.html) / [`demo_cockpit.html`](./demo_cockpit.html)  
> **Modal Warehouse & Z3 Apps:** [`modal_sovereign_forensics_warehouse.py`](./modal_sovereign_forensics_warehouse.py) & [`modal_taxriskos_forensics_app.py`](./modal_taxriskos_forensics_app.py)  
> **Narrated 3-Minute Demo Video:** [`SOVEREIGN_FORENSICS_META_HACKATHON_3MIN_DEMO.mp4`](./SOVEREIGN_FORENSICS_META_HACKATHON_3MIN_DEMO.mp4)

---

## 1. Executive Summary & Problem-Solution Fit

### The Problem: Financial Misstatement, Supply-Chain Tariff Trapping & The LLM Hallucination Blindspot
Corporate accounting manipulation, earnings smoothing, and unrefunded supply-chain pass-through surcharges destroy hundreds of billions of dollars in enterprise value each year. Today, forensic accounting and statutory tax/customs recovery remain slow, manual crafts: forensic CPAs, short-sellers, and corporate tax controversy counsel (*Kovel* `26 U.S.C. § 7525`) spend weeks reading 100+ page SEC 10-K filings, digging through obscure footnotes, and reconciling multi-FEIN trial balances. Meanwhile, generic cloud LLMs hallucinate calculations, invent invalid statutory citations, and risk waiving attorney-client privilege (*United States v. Heppner*, S.D.N.Y. Feb. 2026) or crossing unauthorized practice of law boundaries (`KRS 325.380(4)-(5)` / `AICPA ET § 1.295`).

### The Solution: SovereignForensics // TaxRiskOS
**SovereignForensics // TaxRiskOS** unifies sub-second out-of-core columnar analytics with **Meta's frontier reasoning & multimodal model stack** and an air-gapped **deterministic Z3 SMT + `Decimal` verification plane**:

1. **Sub-Second Market-Wide Screener (`0.663s`):** DuckDB scans SEC EDGAR XBRL facts across **15,203 US public companies (`16,331,263` XBRL facts)** in **0.663 seconds**, evaluating Balance Sheet Invariants, the **Beneish 8-Variable M-Score**, **Dechow F-Score Logit Model**, **Sloan Accrual Anomaly**, and **IEEPA / Section 301 Tariff Pass-Through Distortion (`ITSI`)**.
2. **3-Agent Meta Model Council + Multimodal Stack:** A specialized council powered by official Meta Hackathon models investigates flagged outliers across all partner clouds and local hardware:
   - **Agent 1 — Forensic CPA Agent (`muse-wonder-full-1.0` / `muse-wonder-1.0` 1M context via Meta Model API & Muse Code CLI):** Audits `ASC 606` revenue recognition footnotes, PCAOB Critical Audit Matters (CAMs), and unbilled contract assets in a single 1M-token pass.
   - **Agent 2 — Governance & Footnote Sleuth (`muse-spark-1.3` & `meta/muse-glimmer-30b-nvfp4` on Baseten):** Cross-checks Form 8-K Item 4.01 auditor resignations and customer tariff pass-through liabilities (such as **UPS's `$500M`**, **Medline's `$89M`**, and **LCI Industries' `$88.8M`** reserves).
   - **Agent 3 — Adversarial Cross-Examiner & Multimodal Verifier (`accounts/fireworks/models/muse-glimmer-30b` SFT on Fireworks AI, `meta/muse-glimmer-30b-nvfp4` on Modal Serverless GPU, `sam-3.1` for CBP Form 7501 / 10-K table segmentation, `muse-image-1.0` for forensic infographic synthesis, `muse-voice-transcribe-1.0` for earnings call transcription, and local `NVIDIA RTX 4090` 24GB VRAM Ollama execution):** Stress-tests manipulation hypotheses against management defenses to eliminate false positives.
3. **TaxRiskOS Deterministic `Decimal` (`ROUND_HALF_UP`) + Z3 SMT Theorem Prover + `safeEmit()` UPL Gate:** Replaces generative arithmetic with formal theorem proving (`Assets == Liabilities + Equity`, `NetIncome == CFO + Accruals`, `Gross == Fee + Net`, `Fee <= Cap`), delivering **0.000% arithmetic hallucination** on Multi-FEIN statutory recovery waterfalls (**`19 U.S.C. § 1313` Duty Drawback + `KRS 139.470(9)` Manufacturing Utility Exemption + `UCC § 2-717` Bilateral Tariff Setoff + `IRC § 6427` Fuel Excise**) and enforcing `safeEmit()` compliance before any workpaper is emitted.
4. **Institutional Evidence Scale:** Backed by **15,203 screened public filers**, **6,685 real pre-computed `muse-wonder-full-1.0` / `muse-wonder-1.0` forensic briefs (`51.38M` words / `335.38 MB`)**, and a `120`-row ChatML SFT dataset (`muse_glimmer_tariff_tax_sft_dataset.jsonl`).

---

## 2. Dual-Plane System Architecture

```
                         SOVEREIGNFORENSICS // TAXRISKOS DUAL-PLANE ARCHITECTURE
                         =======================================================

   [ Plane A: High-Throughput Analytics & Z3 Proof ]       [ Plane B: 3-Agent Meta Model Council ]
   
   +-------------------------------------------------------+     +----------------------------------------------+
   | 15,203 SEC EDGAR Public Filers (16.33M XBRL Facts)    |     | Agent 1: Forensic CPA Auditor                |
   | DuckDB Out-of-Core Columnar Screener (0.663s Latency) | --> | Meta Muse Code (muse-wonder-full-1.0 1M ctx) |
   | - Balance Sheet Invariant: |Assets - (Liab + Equity)| |     | ASC 606 Cutoff & Journal Reconstruction      |
   | - Beneish 8-Variable M-Score (DSRI, GMI, AQI, etc.)  |     +----------------------------------------------+
   | - Dechow F-Score Logit Misstatement Multiplier        |                            |
   | - Sloan Accrual Decoupling & IEEPA Tariff Risk Index  |                            v
   +-------------------------------------------------------+     +----------------------------------------------+
                               |                                 | Agent 2: Governance & Footnote Sleuth        |
                               v                                 | Meta Muse Spark (muse-spark-1.3) &           |
   +-------------------------------------------------------+     | Baseten Dedicated (meta/muse-glimmer-30b)    |
   | TaxRiskOS Deterministic Z3 SMT & Decimal Engine       |     | Item 4.01 Drops & IEEPA Pass-Through Reserve |
   | - Z3 SMT Prover (A == L + E, NI == CFO + ACC, SAT)    |     +----------------------------------------------+
   | - Multi-FEIN 19 U.S.C. § 1313 (99% Duty Drawback)     |                            |
   | - KRS 139.470(9) Utility + UCC § 2-717 Tariff Setoff  |                            v
   | - safeEmit() UPL Boundary Gate (KRS 325.380(4)-(5))   | <-- | Agent 3: Adversarial Cross-Examiner          |
   +-------------------------------------------------------+     | Fireworks SFT (muse-glimmer-30b) + Modal $30 |
                               |                                 | Serverless + SAM 3.1 + Muse Image + RTX 4090 |
                               v                                 +----------------------------------------------+
               [ Z3-CERTIFIED FORENSIC & TAXRISKOS DOSSIER ]
```

---

## 2.5. Closed-Loop Formal-Verification Self-Taught Reasoner (STaR-Z3) Recursive Self-Improvement Pipeline

SovereignForensics bridges frontier reasoning models with deterministic formal methods to achieve **autonomous recursive self-improvement (RSI)**:
- **Execution-Verified Distillation:** Every forensic analysis and multi-FEIN recovery schedule drafted by `Muse Wonder 1.0` or `Claude Opus 5.5` is submitted to the **Z3 SMT Solver & Decimal Kernel**.
- **DuckDB 2.0.0 `CREATE TRIGGER` Ingestion:** When the Z3 SMT proof evaluates to `SATISFIED` (`0.000%` arithmetic hallucination, exact balance sheet conservation, statutory fee cap compliance), a DuckDB 2.0.0 database trigger automatically routes the full reasoning trace into our JSONL distillation ledger (`sovereign_rsi_gold_traces.duckdb`).
- **Continuous 5-Minute B200 SFT Retraining:** The verified reasoning traces automatically expand our 4 specialized training corpora (`sovereign_forensics_sec_aaer`, `sovereign_forensics_ieepa_tariff`, `sovereign_forensics_duckdb200_sql`, and `sovereign_forensics_dlai_rag_triad`), triggering continuous serverless fine-tuning of `Muse Glimmer 30B` on Fireworks AI B200 hardware at `$0.00` cost.
- **Autonomous Flywheel:** The system gets smarter, faster, and more rigorous with every audited SEC filing—yielding an autonomous recursive self-improvement flywheel without manual prompt engineering or synthetic hallucinations.

---

## 3. Mathematical, Econometric & Statutory Foundations

### A. Beneish 8-Variable M-Score
$$\text{M-Score} = -4.84 + 0.920 \cdot \text{DSRI} + 0.528 \cdot \text{GMI} + 0.404 \cdot \text{AQI} + 0.892 \cdot \text{SGI} + 0.115 \cdot \text{DEPI} - 0.172 \cdot \text{SGAI} + 4.037 \cdot \text{TATA} + 0.0327 \cdot \text{LVGI}$$
- **Threshold:** $\text{M-Score} > -1.78$ indicates a high probability of accounting manipulation.

### B. Dechow et al. F-Score (2011)
$$\text{Log-odds} = -7.383 + 0.037 \cdot \text{rsst\_acc} + 0.767 \cdot \text{ch\_rec} + 0.532 \cdot \text{ch\_inv} + 0.223 \cdot \text{soft\_assets} + 0.775 \cdot \text{ch\_cs} - 0.329 \cdot \text{ch\_roa} + 0.615 \cdot \text{issue}$$
$$\text{F-Score} = \frac{1 / (1 + e^{-\text{Log-odds}})}{0.0037}$$
- **Threshold:** $\text{F-Score} > 1.00$ indicates elevated misstatement risk; $\text{F-Score} > 2.45$ indicates severe accounting fraud probability.

### C. Sloan Accrual Anomaly & IEEPA Tariff Risk Index (`ITSI`)
$$\text{Accrual Ratio} = \frac{\text{Net Income} - \text{CFO}}{(\text{Assets}_t + \text{Assets}_{t-1}) / 2.0}, \quad \text{Tariff Risk Index} = \text{ITSI} \times \text{GMI}$$

### D. TaxRiskOS Multi-FEIN Statutory Recovery Waterfall (`Decimal` `ROUND_HALF_UP`)
- **`19 U.S.C. § 1313` Duty Drawback:** $99\%$ statutory refund on imported merchandise/inputs subsequently exported.
- **`KRS 139.470(9)` Utility Exemption:** $6\%$ manufacturing plant utility sales tax refund across a 4-year lookback.
- **`UCC § 2-717` / `§ 2-305` Bilateral Tariff Setoff:** Direct deduction of unrefunded IEEPA / Section 301 pass-through surcharges on active supply contracts (**UPS `$147.68M` gross / `$118.14M` net**, **Medline `$54.13M` gross / `$43.30M` net**, **LCI Industries `$47.55M` gross / `$38.04M` net**).

## 3.5. 50-Case Meta Partner Stack Forensic Benchmark & Real SEC Case Studies

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

---

## 4. Meta & Partner Technology Integration Matrix

| Component / Partner | Canonical Model / Endpoint | Hackathon Partner Credit | Role in SovereignForensics // TaxRiskOS |
| :--- | :--- | :--- | :--- |
| **Meta Model API & Muse Code CLI** | `https://api.meta.ai/v1/chat/completions` (`muse-wonder-full-1.0`, `muse-spark-1.3`, `sam-3.1`, `muse-image-1.0`, `muse-voice-transcribe-1.0`) | **$150 Meta Credits + Flat-Rate OAuth CLI** | 1M-context `Forensic CPA` 10-K ingestion (`muse-wonder-full-1.0`), fast `Governance Sleuth` (`muse-spark-1.3`), CBP Form 7501 OCR (`sam-3.1`), and visual brief synthesis (`muse-image-1.0`). |
| **Modal Serverless & Sandboxes** | `modal_taxriskos_forensics_app.py` (`@modal.fastapi_endpoint`, `modal.Sandbox`, `meta/muse-glimmer-30b-nvfp4`) | **$30 Starter Credit + $100 Grant** | Hosts scale-to-zero FastAPI forensic endpoint (`taxriskos-forensic-audit`), isolated Z3 SMT verification sandboxes, sticky `Modal-Routing-Affinity-Key` prefix caching, `enable_memory_snapshot=True` cold-start acceleration, DLAI Pro `sc-landingai` coordinate-grounded bounding-box provenance (`grounding_bbox`), and `modal-labs/devlooper` self-verifying sandbox execution. |
| **Fireworks AI** | `https://api.fireworks.ai/inference/v1/chat/completions` (`accounts/fireworks/models/muse-glimmer-30b`) | **$50 `MetaGlimmer50` + Free B200 SFT** | Serverless LoRA SFT fine-tuning on 120 verified tariff/tax ChatML cases + high-TPS `Adversarial Cross-Examiner` inference. |
| **Baseten** | `https://inference.baseten.co/v1/chat/completions` (`meta/muse-glimmer-30b-nvfp4` + 10 Free Sandboxes) | **$50 Credit + 10 Free Sandboxes** | High-throughput concurrent footnote & Form 8-K Item 4.01 governance screening across flagged public filers. |
| **Local NVIDIA RTX 4090 (24GB)** | `http://127.0.0.1:11434/api/chat` (`huihui-qwen3-30b-a3b-abliterated:latest` + 13 local models) | **$0.00 Sovereign Local Metal** | Air-gapped *United States v. Heppner*-compliant local 3-Agent Council synthesis at `166.1 tok/s` (`4.395s` end-to-end). |

---

## 5. Quickstart & Installation

```bash
git clone https://github.com/johnwebbc/SovereignForensics.git
cd SovereignForensics
pip install -r requirements.txt
```

### 1. Run Market-Wide DuckDB Screener (`0.663s` across `15,203` CIKs)
```bash
python sovereign_forensics_engine.py --screen --limit 10
```

### 2. Run 3-Agent Meta Model Council Deliberation (Auto / Modal / Fireworks / Baseten / Local RTX 4090)
```bash
python sovereign_forensics_engine.py --council "Spirit AeroSystems" --provider ollama_rtx4090
```

### 3. Run TaxRiskOS Multi-FEIN Waterfall + Z3 SMT Proof + `safeEmit()` Audit
```bash
python sovereign_forensics_engine.py --taxriskos --json
python modal_taxriskos_forensics_app.py --local-smoke
```

#### 4. Fireworks AI Muse Glimmer 30B Free SFT & Fine-Tuned Model Routing
Supervised Fine-Tuning on `accounts/fireworks/models/muse-glimmer-30b` is **100% free through November 30, 2026** on Fireworks B200 GPUs.
```bash
# Validate and view dataset (200 train / 40 val rows)
python -c "from pathlib import Path; print(Path('data/SOVEREIGN_FORENSICS_MUSE_GLIMMER_SFT_TRAIN.jsonl').stat().st_size)"

# Route engine queries to custom fine-tuned LoRA model
export FIREWORKS_FINE_TUNED_MODEL_ID="accounts/<account>/models/sovereign-forensics-muse-glimmer-30b-v1"
python sovereign_forensics_engine.py --provider fireworks
```

#### 5. Deploy to Modal Cloud & Execute Batch API (`$30` Free Credit — Scales to Zero)
```bash
python -m modal setup
python -m modal deploy modal_taxriskos_forensics_app.py

# High-throughput batch processing across multiple corporate filings:
python -c "from modal_taxriskos_forensics_app import run_batch_audit_local_or_remote; print(len(run_batch_audit_local_or_remote([{'entity_name': 'Test A', 'cik': '1', 'imported_cogs_usd': '100000', 'export_share_pct': '0.2', 'ieepa_pass_through_surcharge_usd': '25000'}])))"

# Serverless DuckDB + Parquet Data Warehouse with Volume persistence & GPU function:
# Uses enable_memory_snapshot=True, DLAI sc-landingai coordinate grounding bbox provenance,
# and modal-labs/devlooper self-verifying sandbox execution:
python modal_sovereign_forensics_warehouse.py --local-smoke
python -m modal deploy modal_sovereign_forensics_warehouse.py
```

### 6. Run Full Automated Test Suite (`24/24` Passing)
```bash
python -m unittest test_sovereign_forensics_hackathon.py -v
```

### 7. Launch Interactive Web Cockpit
Open [`index.html`](./index.html) or [`demo_cockpit.html`](./demo_cockpit.html) in any browser to interact with the real-time screener, 3-Agent Meta Council, and TaxRiskOS Multi-FEIN Z3 calculator.

---

## 6. Verification & Test Suite (`24/24` Tests Passing)

```
test_01_sample_dataset_exists_and_valid ........................................ [PASS]
test_02_screening_latency_under_2_seconds ...................................... [PASS] (0.663s)
test_03_beneish_sloan_dechow_tariff_metric_structure ........................... [PASS]
test_04_dechow_f_score_and_tariff_risk_calculations ............................ [PASS]
test_05_deterministic_decimal_waterfall_precision .............................. [PASS] ($0.00 drift)
test_06_z3_smt_formal_verification_success ..................................... [PASS] (SATISFIED)
test_07_z3_smt_detects_imbalanced_balance_sheet ................................ [PASS] (UNSAT_INVARIANT_VIOLATION)
test_08_3agent_meta_council_deliberation ....................................... [PASS]
test_09_multi_provider_routing_and_modal_fallback .............................. [PASS]
test_10_telemetry_reporting .................................................... [PASS]
test_11_canonical_meta_baseten_fireworks_modal_endpoints ....................... [PASS]
test_12_taxriskos_multi_fein_waterfall_and_z3 .................................. [PASS]
test_13_taxriskos_safe_emit_upl_boundary_gate .................................. [PASS]
test_14_modal_serverless_app_and_sandbox_fallback .............................. [PASS]
test_15_live_rtx4090_ollama_sovereign_council .................................. [PASS]
test_16_strict_rfc8259_json_no_nan_in_screener_and_benchmarks .................. [PASS]
test_17_z3_real_solver_check_and_unsat_proof_status ............................ [PASS]
test_18_safe_emit_redacts_summary_narrative_on_violation ....................... [PASS]
test_19_import_from_outside_repo_dir_and_cli_taxriskos ......................... [PASS]
test_20_zero_legacy_domains_or_models_in_readme_html_and_command_sheet ......... [PASS]
test_21_fireworks_sft_dataset_integrity_and_fine_tuned_model_routing ........... [PASS]
test_22_modal_batch_api_wiring ................................................. [PASS]
test_23_modal_duckdb_parquet_warehouse_and_z3_verification .................... [PASS]
test_24_dlai_landingai_grounding_bbox_and_devlooper_sandbox .................... [PASS]
----------------------------------------------------------------------
Ran 24 tests in 3.5s (OK)
```

---

## 7. License

This repository is licensed under the [MIT License](./LICENSE).  
Copyright (c) 2026 John Webb & Co. LLC / TaxRiskOS LLC. All rights reserved.
