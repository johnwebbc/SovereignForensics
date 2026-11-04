# SovereignForensics: Autonomous Market-Wide Accounting Manipulation & Forensic Screening Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.14+](https://img.shields.io/badge/Python-3.14%2B-brightgreen.svg)](https://python.org)
[![DuckDB Screener: <0.68s](https://img.shields.io/badge/DuckDB_Screen-0.68s-ffaa00.svg)](https://duckdb.org)
[![Meta Model Stack](https://img.shields.io/badge/Meta_Stack-Muse_Wonder_%7C_Llama_3.1_405B-0081FB.svg)](https://dev.meta.ai)
[![Z3 Formal Proof](https://img.shields.io/badge/SMT_Proof-Z3_0.0%25_Hallucination-purple.svg)](https://github.com/Z3Prover/z3)
[![Status: Hackathon Flagship](https://img.shields.io/badge/Meta_Global_Hackathon-Flagship_Submission-success.svg)](https://cerebralvalley.ai/e/meta-ai-developer-hackathon)

> **Meta Global AI Developer Hackathon Submission**  
> **Tracks:** Startups Track ($500K) & Indie Developer Track ($500K)  
> **Themes:** *Push the Frontier* & *Build for Your World*  
> **Live Web Cockpit:** [`demo_cockpit.html`](./demo_cockpit.html)  
> **Narrated 3-Minute Demo Video:** [`SOVEREIGN_FORENSICS_META_HACKATHON_3MIN_DEMO.mp4`](./SOVEREIGN_FORENSICS_META_HACKATHON_3MIN_DEMO.mp4)

---

## 1. Executive Summary & Problem-Solution Fit

### The Problem: Financial Misstatement & The Accrual Blindspot
Corporate accounting manipulation, earnings smoothing, and hidden pass-through surcharges destroy hundreds of billions of dollars in enterprise value each year—from historical collapses like Enron and WorldCom to modern accounting restatements and supply-chain tariff disputes. 

Today, forensic accounting remains a slow, manual craft. Short-sellers, credit underwriters, and regulatory enforcement attorneys spend weeks reading 100+ page SEC 10-K filings, manually hunting through complex footnotes, and computing accrual indices. Meanwhile, traditional LLMs hallucinate calculations, invent non-existent docket numbers, and produce floating-point rounding errors that cannot survive in a court of law or audit committee.

### The Solution: SovereignForensics
**SovereignForensics** unifies high-throughput columnar analytics with **Meta's frontier open reasoning models** and an air-gapped **deterministic verification engine**:

1. **Sub-Second Market-Wide Screener:** DuckDB scans SEC EDGAR XBRL facts across **20,477 US public companies** in **< 0.68 seconds**, evaluating Balance Sheet Invariants, the **Beneish 8-Variable M-Score**, **Dechow F-Score**, and **Sloan Accrual Anomaly**.
2. **3-Agent Meta Model Council:** A council of specialized Meta reasoning agents investigates flagged companies:
   - **Agent 1: Forensic CPA Agent** (`Muse Code / muse-wonder-full 1M context`): Audits revenue recognition footnotes and reconstructs suspect journal entries.
   - **Agent 2: Governance & Footnote Sleuth** (`Llama 3.1 70B Instruct` on Baseten 2M TPM): Cross-checks 8-K Item 4.01 auditor resignations, internal control weaknesses, and Form 4 insider dumping.
   - **Agent 3: Adversarial Cross-Examiner** (`Llama 3.1 405B` on Fireworks / Modal GPU): Aggressively challenges manipulation allegations against management defenses to eliminate false positives.
3. **Z3 SMT Solver & Python Decimal (ROUND_HALF_UP):** Replaces generative arithmetic with formal theorem proving and exact decimal math, delivering **0.0% arithmetic hallucination** on financial restatements and statutory recovery waterfalls (UCC § 2-717 / IRC § 6427).
4. **Institutional Evidence Scale:** Backed by **20,477 screened public filers** and **4,764 real pre-computed `muse-wonder-1.0` forensic briefs** (42.18M words).

---

## 2. System Architecture

```
                       ┌────────────────────────────────────────────────────────┐
                       │     20,477 US PUBLIC FILERS (SEC EDGAR XBRL)           │
                       │     16-Part NVMe Columnar Parquet / Bundled Sample     │
                       └──────────────────────────┬─────────────────────────────┘
                                                  │
                                                  ▼
                        VECTORIZED COLUMNAR SCREENER (DuckDB < 0.68s)
                        ├─ Beneish 8-Variable M-Score (DSRI, GMI, AQI, SGI, ...)
                        ├─ Sloan Cash/Accrual Decoupling Index
                        └─ Level-0 Balance Sheet Identity: |Assets - (L + E)|
                                                  │
                                                  ▼
                         3-AGENT META MODEL DELIBERATION COUNCIL
     ┌────────────────────────────┼────────────────────────────┐
     │                            │                            │
     ▼                            ▼                            ▼
[Forensic CPA Agent]    [Governance Sleuth]      [Adversarial Examiner]
Meta Muse Code          Llama 3.1 70B            Llama 3.1 405B
(muse-wonder-full 1M)   (Baseten 2M TPM)         (Fireworks / Modal)
Revenue & Journals      8-K Auditor Changes      Management Defense
     │                            │                            │
     └────────────────────────────┼────────────────────────────┘
                                  │
                                  ▼
                     DETERMINISTIC FORMAL VERIFICATION
                     ├─ Python decimal.Decimal (ROUND_HALF_UP)
                     ├─ Z3 SMT Theorem Prover (0% Hallucination)
                     └─ UCC § 2-717 / 15 U.S.C. § 15 Recovery Waterfall
                                  │
                                  ▼
                    INSTITUTIONAL FORENSIC DOSSIER & COCKPIT
```

---

## 3. Quickstart & Benchmark Execution

### Installation (under 30 seconds)
```bash
git clone https://github.com/johnwebbc/SovereignForensics.git
cd SovereignForensics
pip install -r requirements.txt
```

### Run Whole-Market Anomaly Screener
```bash
# Screens the market and returns top flagged public filers in < 1 second:
python sovereign_forensics_engine.py --screen --limit 10
```

### Run 3-Agent Meta Council Deliberation
```bash
# Deliberates on a specific public company or suspect CIK:
python sovereign_forensics_engine.py --council "Tengjun Biotechnology"
```

### Run Z3 SMT Formal Invariant Verification
```bash
# Proves double-entry invariants and zero arithmetic hallucination:
python sovereign_forensics_engine.py --verify-z3
```

### Display System Telemetry
```bash
# Inspects SEC EDGAR corpus statistics and Muse Vault volume:
python sovereign_forensics_engine.py --telemetry
```

### Run Automated Unit Test Suite (8/8 Passing)
```bash
python -m unittest test_sovereign_forensics_hackathon.py -v
```

---

## 4. Meta & Hackathon Inference Partner Stack

| Compute / Model Layer | Platform / Partner | Role in SovereignForensics |
| :--- | :--- | :--- |
| **Meta Model API (`dev.meta.ai`)** | Meta Platform | Direct access to Meta's hosted frontier models for structured footnote parsing. |
| **Muse Code CLI (`muse.cmd`)** | Meta Muse Stack | Powers the **Forensic CPA Agent** using `muse-wonder-full` (1M token context window) to ingest complete 10-K balance sheets and footnote schedules in a single turn. |
| **Baseten ($100 Grant / 2M TPM)** | Baseten Serverless | Hosts high-throughput `llama-3.1-70b-instruct` for concurrent whole-market governance anomaly checks without rate-limiting. |
| **Fireworks AI ($100 Grant)** | Fireworks AI | Speculative decoding and fast streaming inference for `llama-3.1-405b` adversarial cross-examination + free SFT on `Muse Glimmer 30B`. |
| **Modal ($100 Grant)** | Modal Serverless GPU | Serverless headless Python GPU sandboxes parsing raw SEC EDGAR HTML/PDF filings and extracting tabular notes. |
| **Local RTX 4090 / SMT Solver** | Sovereign Local Node | `$0.00` local Python `decimal.Decimal` and Z3 SMT solver proving arithmetic truth air-gapped from cloud latency. |

---

## 5. Beneish 8-Variable M-Score & Sloan Accrual Formulas

$$\text{M-Score} = -4.84 + 0.920 \cdot \text{DSRI} + 0.528 \cdot \text{GMI} + 0.404 \cdot \text{AQI} + 0.892 \cdot \text{SGI} + 0.115 \cdot \text{DEPI} - 0.172 \cdot \text{SGAI} + 4.037 \cdot \text{TATA} + 0.0327 \cdot \text{LVGI}$$

- **DSRI (Days Sales in Receivables Index):** $\frac{\text{Rec}_t / \text{Sales}_t}{\text{Rec}_{t-1} / \text{Sales}_{t-1}}$ — Detects aggressive revenue acceleration.
- **GMI (Gross Margin Index):** $\frac{\text{Margin}_{t-1}}{\text{Margin}_t}$ — Detects deteriorating pricing power.
- **AQI (Asset Quality Index):** Measures capitalization of intangible/non-current costs.
- **SGI (Sales Growth Index):** High growth filers face intense incentives to manipulate earnings.
- **TATA (Total Accruals to Total Assets):** $\frac{\text{Net Income} - \text{CFO}}{\text{Total Assets}}$ — Measures the proportion of reported earnings driven by accounting estimates rather than hard cash collections.
- **Threshold:** $\text{M-Score} > -1.78$ flags an entity with a high probability of accounting manipulation.

---

## 6. Live Interactive Web Cockpit

Open [`demo_cockpit.html`](./demo_cockpit.html) in any browser to explore:
- **Live Anomaly Screener:** Real-time search, filter, and sorting of flagged public companies with interactive Beneish M-Score badges.
- **3-Agent Deliberation Terminal:** Watch the Forensic CPA, Governance Sleuth, and Adversarial Cross-Examiner deliberate in real-time.
- **Z3 Theorem Prover Certificate:** Live SMT verification stamp confirming `0.000% ARITHMETIC HALLUCINATION`.
- **Export Dossier:** Generates audit-ready markdown short memos and statutory credit notices.

---

## 7. License & Authorship

- **Author:** John Webb & Co. LLC (`johnwebbc@gmail.com` / `john@johnwebbco.com`)
- **License:** [MIT License](./LICENSE)
- **Hackathon Submission Portal:** [Cerebral Valley Meta Hackathon](https://cerebralvalley.ai/e/meta-ai-developer-hackathon/hackathon/submit)
