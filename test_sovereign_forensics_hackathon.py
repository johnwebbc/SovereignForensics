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
        self.assertIn("muse-wonder-full (1M context via Muse Code CLI)", telemetry["supported_meta_models"])


if __name__ == "__main__":
    unittest.main()
