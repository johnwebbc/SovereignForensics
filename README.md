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
> **Live Web Cockpit:** [`index.html`](./index.html) / [`demo_cockpit.html`](./demo_cockpit.html)  
> **Modal Serverless & Z3 App:** [`modal_taxriskos_forensics_app.py`](./modal_taxriskos_forensics_app.py)  
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

---

## 4. Meta & Partner Technology Integration Matrix

| Component / Partner | Canonical Model / Endpoint | Hackathon Partner Credit | Role in SovereignForensics // TaxRiskOS |
| :--- | :--- | :--- | :--- |
| **Meta Model API & Muse Code CLI** | `https://api.meta.ai/v1/chat/completions` (`muse-wonder-full-1.0`, `muse-spark-1.3`, `sam-3.1`, `muse-image-1.0`, `muse-voice-transcribe-1.0`) | **$150 Meta Credits + Flat-Rate OAuth CLI** | 1M-context `Forensic CPA` 10-K ingestion (`muse-wonder-full-1.0`), fast `Governance Sleuth` (`muse-spark-1.3`), CBP Form 7501 OCR (`sam-3.1`), and visual brief synthesis (`muse-image-1.0`). |
| **Modal Serverless & Sandboxes** | `modal_taxriskos_forensics_app.py` (`@modal.fastapi_endpoint`, `modal.Sandbox`, `meta/muse-glimmer-30b-nvfp4`) | **$30 Starter Credit + $100 Grant** | Hosts scale-to-zero FastAPI forensic endpoint (`taxriskos-forensic-audit`), isolated Z3 SMT verification sandboxes, and sticky `Modal-Routing-Affinity-Key` prefix caching. |
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

### 5. Deploy to Modal Cloud & Execute Batch API (`$30` Free Credit — Scales to Zero)
```bash
python -m modal setup
python -m modal deploy modal_taxriskos_forensics_app.py

# High-throughput batch processing across multiple corporate filings:
python -c "from modal_taxriskos_forensics_app import run_batch_audit_local_or_remote; print(len(run_batch_audit_local_or_remote([{'entity_name': 'Test A', 'cik': '1', 'imported_cogs_usd': '100000', 'export_share_pct': '0.2', 'ieepa_pass_through_surcharge_usd': '25000'}])))"

# Serverless DuckDB + Parquet Data Warehouse with Volume persistence & GPU function:
python modal_sovereign_forensics_warehouse.py --local-smoke
python -m modal deploy modal_sovereign_forensics_warehouse.py
```

### 6. Run Full Automated Test Suite (`23/23` Passing)
```bash
python -m unittest test_sovereign_forensics_hackathon.py -v
```

### 7. Launch Interactive Web Cockpit
Open [`index.html`](./index.html) or [`demo_cockpit.html`](./demo_cockpit.html) in any browser to interact with the real-time screener, 3-Agent Meta Council, and TaxRiskOS Multi-FEIN Z3 calculator.

---

## 6. Verification & Test Suite (`23/23` Tests Passing)

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
----------------------------------------------------------------------
Ran 23 tests in 7.6s (OK)
```

---

## 7. License

This repository is licensed under the [MIT License](./LICENSE).  
Copyright (c) 2026 John Webb & Co. LLC / TaxRiskOS LLC. All rights reserved.
