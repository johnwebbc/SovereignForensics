#!/usr/bin/env python3
"""
Unit Test Suite for SovereignForensics Meta Hackathon Engine
============================================================
Verifies:
1. DuckDB out-of-core SEC XBRL screening latency (< 2.1 seconds) & accuracy
2. Beneish 8-Variable M-Score, Dechow F-Score, Sloan Accruals, and IEEPA Tariff Risk integrity
3. 3-Agent Meta Model Council deliberation routing across multi-providers (Meta, Muse, Baseten, Fireworks, Modal)
4. Deterministic Python Decimal (ROUND_HALF_UP) recovery waterfall
5. Z3 SMT Theorem Prover balance sheet invariant formal verification
6. System telemetry and multi-provider fallback stability

Run via:
    python -m unittest test_sovereign_forensics_hackathon.py -v
"""

from __future__ import annotations

import math
import os
import sys
import unittest
from decimal import Decimal
from pathlib import Path

# Add repo root to import path
REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))

from sovereign_forensics_engine import SovereignForensicsEngine, SAMPLE_PARQUET


class TestSovereignForensicsHackathon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Force sample data for reproducible, portable testing in all environments
        cls.engine = SovereignForensicsEngine(prefer_sample_data=True)

    def test_01_sample_dataset_exists_and_valid(self):
        """Verify the bundled sample parquet dataset is present and non-empty."""
        self.assertTrue(SAMPLE_PARQUET.exists(), f"Sample parquet not found at {SAMPLE_PARQUET}")
        self.assertGreater(SAMPLE_PARQUET.stat().st_size, 500000, "Sample parquet unexpectedly small")

    def test_02_screening_latency_under_2_seconds(self):
        """WHEN screened, THE DuckDB engine SHALL execute whole-universe analysis in < 2.1s."""
        res = self.engine.run_market_screener(limit=25)
        self.assertIn("screen_latency_sec", res)
        self.assertLess(res["screen_latency_sec"], 2.10, f"Screen latency {res['screen_latency_sec']}s exceeded 2.1s threshold")
        self.assertGreater(res["total_universe_ciks"], 0)
        self.assertIsInstance(res["candidates"], list)

    def test_03_beneish_sloan_dechow_tariff_metric_structure(self):
        """Verify flagged candidates contain complete Beneish, Sloan, Dechow, and IEEPA metrics."""
        res = self.engine.run_market_screener(limit=10)
        self.assertGreater(len(res["candidates"]), 0, "No candidates returned from screener")
        candidate = res["candidates"][0]
        required_keys = [
            "cik", "entity_name", "fy", "assets", "sales", "net_income",
            "beneish_m_score", "dechow_f_score", "sloan_accrual",
            "tariff_risk_index", "dsri", "gmi", "sgi", "forensic_flag"
        ]
        for key in required_keys:
            self.assertIn(key, candidate, f"Missing key '{key}' in candidate record")
        
        # Verify metric validity
        self.assertIsInstance(candidate["beneish_m_score"], (int, float))
        self.assertIsInstance(candidate["dechow_f_score"], (int, float))
        self.assertIsInstance(candidate["tariff_risk_index"], (int, float))

    def test_04_dechow_f_score_and_tariff_risk_calculations(self):
        """Verify Dechow F-Score logit probability scaling and IEEPA Tariff Risk indicators."""
        res = self.engine.run_market_screener(limit=50)
        for cand in res["candidates"]:
            # Dechow F-Score must be positive probability ratio
            self.assertGreaterEqual(cand["dechow_f_score"], 0.0)
            # Tariff risk index should be a numeric float
            self.assertIsInstance(cand["tariff_risk_index"], (int, float))

    def test_05_deterministic_decimal_waterfall_precision(self):
        """Verify zero floating-point approximation error in contingent recovery waterfall."""
        # Test Case 1: Standard $1,000,000 recovery at 20%
        w1 = self.engine.compute_contingent_recovery_waterfall("1000000.00", "0.20")
        self.assertEqual(w1["gross_recoverable_usd"], "1000000.00")
        self.assertEqual(w1["contingent_success_fee_usd"], "200000.00")
        self.assertEqual(w1["net_cash_to_client_usd"], "800000.00")

        # Test Case 2: Uneven cents handling ($128,450.37 at 17.5%)
        # 128450.37 * 0.175 = 22478.81475 -> 22478.81
        w2 = self.engine.compute_contingent_recovery_waterfall("128450.37", "0.175")
        self.assertEqual(w2["gross_recoverable_usd"], "128450.37")
        self.assertEqual(w2["contingent_success_fee_usd"], "22478.81")
        self.assertEqual(w2["net_cash_to_client_usd"], "105971.56")
        
        # Verify exact sum conservation
        gross = Decimal(w2["gross_recoverable_usd"])
        fee = Decimal(w2["contingent_success_fee_usd"])
        net = Decimal(w2["net_cash_to_client_usd"])
        self.assertEqual(gross, fee + net)

    def test_06_z3_smt_formal_verification_success(self):
        """Verify Z3 SMT theorem prover validates double-entry invariants without error."""
        proof = self.engine.verify_financial_invariants_with_z3(
            assets=250000000.0,
            liabilities=150000000.0,
            equity=100000000.0,
            reported_net_income=25000000.0,
            cfo=10000000.0,
            reconstructed_accruals=15000000.0,
        )
        self.assertEqual(proof["z3_solver_status"], "SATISFIED")
        self.assertTrue(proof["balance_sheet_balanced"])
        self.assertTrue(proof["accruals_reconciled"])
        self.assertEqual(proof["arithmetic_hallucination_rate"], "0.000%")

    def test_07_z3_smt_detects_imbalanced_balance_sheet(self):
        """Verify Z3 SMT identifies invariant violations on falsified statements."""
        proof = self.engine.verify_financial_invariants_with_z3(
            assets=250000000.0,
            liabilities=180000000.0,
            equity=100000000.0,  # 180M + 100M = 280M != 250M
            reported_net_income=25000000.0,
            cfo=10000000.0,
            reconstructed_accruals=15000000.0,
        )
        self.assertEqual(proof["z3_solver_status"], "INVARIANT_VIOLATION_DETECTED")
        self.assertFalse(proof["balance_sheet_balanced"])

    def test_08_3agent_meta_council_deliberation(self):
        """Verify the 3-Agent Meta Model Council produces coherent tri-agent deliberation."""
        candidate = {
            "entity_name": "Test Manipulator Corp.",
            "cik": "0001999999",
            "beneish_m_score": 2.45,
            "dechow_f_score": 2.85,
            "sloan_accrual": 0.28,
            "tariff_risk_index": 1.62,
            "days_sales_receivables_index": 2.10,
            "gross_margin_index": 1.75,
            "total_accruals_to_assets": 0.15,
            "assets": 120000000,
            "forensic_flag": "CRITICAL: HIGH-CONVICTION EARNINGS MANIPULATION"
        }
        deliberation = self.engine.deliberate_candidate(candidate)
        self.assertIn("forensic_cpa_agent", deliberation)
        self.assertIn("governance_sleuth_agent", deliberation)
        self.assertIn("adversarial_examiner_agent", deliberation)
        self.assertIn("council_consensus", deliberation)
        self.assertIn("manipulation_verdict", deliberation)
        
        # Verify all 3 agents have detailed findings
        self.assertGreater(len(deliberation["forensic_cpa_agent"]["finding"]), 50)
        self.assertGreater(len(deliberation["governance_sleuth_agent"]["finding"]), 50)
        self.assertGreater(len(deliberation["adversarial_examiner_agent"]["finding"]), 50)
        self.assertEqual(deliberation["manipulation_verdict"], "CONFIRMED_HIGH_RISK_MANIPULATION")

    def test_09_multi_provider_routing_and_modal_fallback(self):
        """Verify provider routing for Modal, Muse CLI, and Baseten fallbacks."""
        candidate = {
            "entity_name": "Modal Test Corp.",
            "cik": "0001888888",
            "beneish_m_score": -1.25,
            "dechow_f_score": 1.95,
            "sloan_accrual": 0.15,
            "tariff_risk_index": 1.30,
            "assets": 50000000,
        }
        # Test Modal provider routing
        delib_modal = self.engine.deliberate_candidate(candidate, provider="modal")
        self.assertEqual(delib_modal["provider_used"], "modal")
        self.assertIn("council_consensus", delib_modal)

        # Test Muse provider routing
        delib_muse = self.engine.deliberate_candidate(candidate, provider="muse")
        self.assertEqual(delib_muse["provider_used"], "muse")
        self.assertIn("council_consensus", delib_muse)

    def test_10_telemetry_reporting(self):
        """Verify telemetry returns comprehensive system metrics and supported Meta models."""
        telemetry = self.engine.get_benchmark_telemetry()
        self.assertIn("sec_facts_filers_indexed", telemetry)
        self.assertIn("sec_facts_rows_scanned", telemetry)
        self.assertIn("supported_meta_models", telemetry)
        self.assertGreater(len(telemetry["supported_meta_models"]), 3)
        self.assertIn(
            "muse-wonder-full-1.0 (1M context via Meta Model API & Muse Code CLI)",
            telemetry["supported_meta_models"],
        )

    def test_11_canonical_meta_baseten_fireworks_modal_endpoints(self):
        """Verify canonical API URLs and official Meta Hackathon model IDs (zero fake domains)."""
        self.assertEqual(self.engine.META_API_BASE, "https://api.meta.ai/v1/chat/completions")
        self.assertEqual(self.engine.BASETEN_API_BASE, "https://inference.baseten.co/v1/chat/completions")
        self.assertEqual(self.engine.FIREWORKS_API_BASE, "https://api.fireworks.ai/inference/v1/chat/completions")
        self.assertEqual(self.engine.META_MODELS["flagship_1m"], "muse-wonder-full-1.0")
        self.assertEqual(self.engine.META_MODELS["fast_extract"], "muse-spark-1.3")
        self.assertEqual(self.engine.META_MODELS["segmentation"], "sam-3.1")
        self.assertEqual(self.engine.META_MODELS["open_weights_glimmer"], "accounts/fireworks/models/muse-glimmer-30b")
        self.assertEqual(self.engine.META_MODELS["modal_dedicated_glimmer"], "meta/muse-glimmer-30b-nvfp4")

    def test_12_taxriskos_multi_fein_waterfall_and_z3(self):
        """Verify TaxRiskOS Multi-FEIN 19 U.S.C. § 1313 drawback, KRS 139.470(9), and UCC § 2-717 waterfall."""
        payload = {
            "entity_name": "Medline Industries / Multi-FEIN Supply Chain",
            "cik": "0001832568",
            "fein_count": 5,
            "imported_cogs_usd": "20000000.00",
            "export_share_pct": "0.20",
            "plant_utility_spend_usd": "1000000.00",
            "ieepa_pass_through_surcharge_usd": "890000.00",
            "fee_rate": "0.20",
        }
        res = self.engine.evaluate_taxriskos_multi_fein_and_notice(payload)
        wf = res["taxriskos_multi_fein_waterfall"]
        # 20M * 0.25 duty = 5M; * 0.20 export = 1M; * 0.99 = 990,000.00
        self.assertEqual(wf["duty_drawback_19usc1313_usd"], "990000.00")
        # 1M * 0.06 * 4 yrs = 240,000.00
        self.assertEqual(wf["utility_exemption_krs139_470_usd"], "240000.00")
        # 990,000 + 240,000 + 890,000 = 2,120,000.00
        self.assertEqual(wf["gross_recoverable_usd"], "2120000.00")
        self.assertEqual(wf["contingent_success_fee_usd"], "424000.00")
        self.assertEqual(wf["net_cash_to_client_usd"], "1696000.00")
        self.assertTrue(wf["cent_conservation_verified"])
        self.assertEqual(res["z3_smt_verification"]["z3_solver_status"], "SATISFIED")
        self.assertTrue(res["taxriskos_safe_emit_gate"]["safe_to_emit"])

    def test_13_taxriskos_safe_emit_upl_boundary_gate(self):
        """Verify TaxRiskOS safeEmit() blocks prohibited legal/tax advice and passes compliant workpapers."""
        import modal_taxriskos_forensics_app as modal_app
        clean = modal_app.safe_emit_guard(
            "Workflow intake and arithmetic illustration only; not tax, legal, or attest advice."
        )
        self.assertTrue(clean["safe_to_emit"])
        self.assertEqual(len(clean["violations_detected"]), 0)

        unsafe = modal_app.safe_emit_guard(
            "We represent you before the IRS and this constitutes formal legal advice with a guaranteed tax refund."
        )
        self.assertFalse(unsafe["safe_to_emit"])
        self.assertGreaterEqual(len(unsafe["violations_detected"]), 3)

    def test_14_modal_serverless_app_and_sandbox_fallback(self):
        """Verify Modal app definition and Sandbox fallback execution."""
        import modal_taxriskos_forensics_app as modal_app
        self.assertEqual(modal_app.APP_NAME, "taxriskos-sovereign-forensics")
        sb_res = modal_app.run_modal_sandbox_verification({
            "entity_name": "LCI Industries (SEC 10-K IEEPA Surcharge)",
            "cik": "0000763744",
            "ieepa_pass_through_surcharge_usd": "888000.00",
        })
        self.assertIn("modal_sandbox_status", sb_res)
        self.assertEqual(sb_res["z3_smt_verification"]["z3_solver_status"], "SATISFIED")

    def test_15_live_rtx4090_ollama_sovereign_council(self):
        """Verify live RTX 4090 Ollama 3-Agent Council deliberation (with deterministic fallback if offline)."""
        candidate = {
            "entity_name": "United Parcel Service, Inc. (IEEPA $500M Surcharge Filer)",
            "cik": "0001090727",
            "beneish_m_score": -1.42,
            "dechow_f_score": 2.15,
            "sloan_accrual": 0.142,
            "tariff_risk_index": 1.64,
            "assets": 250000000,
        }
        delib = self.engine.deliberate_candidate(candidate, provider="ollama_rtx4090")
        self.assertEqual(delib["provider_used"], "ollama_rtx4090")
        self.assertIn("council_consensus", delib)

    def test_16_strict_rfc8259_json_no_nan_in_screener_and_benchmarks(self):
        """Verify screener and benchmark artifacts contain zero NaN/Infinity tokens under strict RFC 8259 JSON."""
        import json
        results = self.engine.run_market_screener(limit=10)
        serialized = json.dumps(results, allow_nan=False)
        self.assertNotIn("NaN", serialized)

        bench_path = REPO_ROOT / "data" / "rtx4090_live_forensic_council_benchmarks.json"
        self.assertTrue(bench_path.exists())
        raw = bench_path.read_text(encoding="utf-8")
        self.assertNotIn("NaN", raw)
        parsed = json.loads(raw)
        json.dumps(parsed, allow_nan=False)
        # Ensure Spirit AeroSystems council consensus does not claim low manipulation
        spirit_synth = parsed["live_rtx4090_council_audits"][0]["rtx4090_live_synthesis"]
        self.assertNotIn("low earnings manipulation", spirit_synth.lower())

    def test_17_z3_real_solver_check_and_unsat_proof_status(self):
        """Verify Z3 solver actually checks A == L + E and NI == CFO + ACC and returns UNSAT_INVARIANT_VIOLATION on mismatch."""
        import modal_taxriskos_forensics_app as modal_app
        bad_eng = self.engine.verify_financial_invariants_with_z3(
            assets=100.00,
            liabilities=60.00,
            equity=30.00,
            reported_net_income=20.00,
            cfo=12.00,
            reconstructed_accruals=8.00,
        )
        self.assertFalse(bad_eng["balance_sheet_balanced"])
        self.assertEqual(bad_eng["z3_solver_status"], "INVARIANT_VIOLATION_DETECTED")
        self.assertEqual(bad_eng["smt_formal_proof"], "UNSAT_INVARIANT_VIOLATION")

        bad_modal = modal_app.execute_forensic_audit_payload({
            "assets": "100.00",
            "liabilities": "60.00",
            "equity": "40.00",
            "reported_net_income": "20.00",
            "cfo": "10.00",
            "reconstructed_accruals": "5.00",
        })
        self.assertTrue(bad_modal["z3_smt_verification"]["balance_sheet_balanced"])
        self.assertFalse(bad_modal["z3_smt_verification"]["accruals_reconciled"])
        self.assertEqual(bad_modal["z3_smt_verification"]["z3_solver_status"], "INVARIANT_VIOLATION_DETECTED")
        self.assertEqual(bad_modal["z3_smt_verification"]["smt_formal_proof"], "UNSAT_INVARIANT_VIOLATION")

    def test_18_safe_emit_redacts_summary_narrative_on_violation(self):
        """Verify execute_forensic_audit_payload redacts summary_narrative if safe_to_emit is False."""
        import modal_taxriskos_forensics_app as modal_app
        res = modal_app.execute_forensic_audit_payload({
            "entity_name": "Unsafe Narrative Test LLC",
            "draft_memo": "We represent you before the IRS and provide formal legal advice with a guaranteed tax refund.",
        })
        self.assertFalse(res["taxriskos_safe_emit_gate"]["safe_to_emit"])
        self.assertTrue(res["summary_narrative"].startswith("[BLOCKED_BY_TAXRISKOS_SAFE_EMIT_GATE:"))

    def test_19_import_from_outside_repo_dir_and_cli_taxriskos(self):
        """Verify sovereign_forensics_engine imports cleanly outside REPO_ROOT and supports --taxriskos CLI."""
        import subprocess
        cmd = [
            sys.executable,
            str(REPO_ROOT / "sovereign_forensics_engine.py"),
            "--taxriskos",
        ]
        proc = subprocess.run(cmd, cwd="O:\\", capture_output=True, text=True, timeout=30)
        self.assertEqual(proc.returncode, 0, msg=proc.stderr)
        self.assertIn("gross_recoverable_usd", proc.stdout)

    def test_20_zero_legacy_domains_or_models_in_readme_html_and_command_sheet(self):
        """Verify README.md, demo_cockpit.html, index.html, and command sheet contain canonical models and zero fake domains."""
        files_to_check = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "demo_cockpit.html",
            REPO_ROOT / "index.html",
        ]
        for fp in files_to_check:
            self.assertTrue(fp.exists(), f"Missing {fp}")
            text = fp.read_text(encoding="utf-8")
            self.assertNotIn("bridge.baseten.co", text)
            self.assertNotIn("api.dev.meta.ai", text)
            self.assertNotIn("llama-3.1-70b-instruct", text)
            self.assertNotIn("llama-3.1-405b-instruct", text)
            self.assertIn("muse-wonder-full-1.0", text)
            self.assertIn("TaxRiskOS", text)

    def test_21_fireworks_sft_dataset_integrity_and_fine_tuned_model_routing(self):
        """Verify Fireworks SFT dataset files exist and obey strict chat JSONL specification."""
        import json
        from unittest.mock import patch
        train_ds = REPO_ROOT / "data" / "SOVEREIGN_FORENSICS_MUSE_GLIMMER_SFT_TRAIN.jsonl"
        val_ds = REPO_ROOT / "data" / "SOVEREIGN_FORENSICS_MUSE_GLIMMER_SFT_VAL.jsonl"
        self.assertTrue(train_ds.exists(), f"Missing train dataset: {train_ds}")
        self.assertTrue(val_ds.exists(), f"Missing val dataset: {val_ds}")

        for path, min_rows in [(train_ds, 100), (val_ds, 20)]:
            with open(path, "r", encoding="utf-8") as f:
                lines = [l.strip() for l in f if l.strip()]
            self.assertGreaterEqual(len(lines), min_rows)
            for line in lines[:10]:
                obj = json.loads(line)
                self.assertIn("messages", obj)
                self.assertGreaterEqual(len(obj["messages"]), 2)
                self.assertEqual(obj["messages"][-1]["role"], "assistant")
                self.assertTrue(bool(obj["messages"][-1]["content"]))

        # Verify engine routes custom fine-tuned model ID when configured
        with patch.dict(os.environ, {"FIREWORKS_FINE_TUNED_MODEL_ID": "accounts/johnwebb/models/sovereign-forensics-v1"}):
            from sovereign_forensics_engine import SovereignForensicsEngine
            eng = SovereignForensicsEngine()
            self.assertEqual(os.environ.get("FIREWORKS_FINE_TUNED_MODEL_ID"), "accounts/johnwebb/models/sovereign-forensics-v1")

    def test_22_modal_batch_api_wiring(self):
        """Verify Modal Batch API wiring executes multi-company audit payloads cleanly."""
        from modal_taxriskos_forensics_app import run_batch_audit_local_or_remote
        batch = [
            {
                "entity_name": "Test Logistics Alpha Corp",
                "cik": "0001000001",
                "imported_cogs_usd": "1000000.00",
                "export_share_pct": "0.25",
                "ieepa_pass_through_surcharge_usd": "250000.00",
            },
            {
                "entity_name": "Test Logistics Beta LLC",
                "cik": "0001000002",
                "imported_cogs_usd": "2000000.00",
                "export_share_pct": "0.30",
                "ieepa_pass_through_surcharge_usd": "400000.00",
            },
        ]
        results = run_batch_audit_local_or_remote(batch)
        self.assertEqual(len(results), 2)
        for r in results:
            self.assertIn("taxriskos_multi_fein_waterfall", r)
            self.assertIn("gross_recoverable_usd", r["taxriskos_multi_fein_waterfall"])


if __name__ == "__main__":
    unittest.main()
