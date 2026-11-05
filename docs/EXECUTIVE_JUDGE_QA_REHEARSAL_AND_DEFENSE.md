# SovereignForensics: Executive Judge Q&A Rehearsal Packet

**Event:** Meta Global AI Developer Hackathon ($1,000,000 prize pool)
**Audience:** Technical judges, Meta partner engineers, legal/compliance evaluators
**Status:** Rehearsal draft. Every number below is taken from the SovereignForensics evidence pack as briefed. Re-run the benchmark harness on the demo machine before stage and replace any figure that drifts.

## Framing rules for every answer

- Open with the result, then the mechanism, then the proof. Judges remember the first sentence.
- Separate three claims that are easy to blur: what the LLM drafts, what Z3 proves, and what the statute enforces. The product's credibility rests on never letting one borrow authority from another.
- Quote measurement windows, not adjectives. "Zero arithmetic errors across the 2,400-row test corpus" beats "perfectly accurate."
- When a judge probes a limit, concede it in one sentence and show the guardrail. Defensiveness reads as concealment.

## The 15 questions

**Q1. "LLMs hallucinate. Why should I believe a 30B model got your numbers right?"**

*Judge intent and probe.* Tests whether the team understands that the model is not the source of truth. A follow-up will be "so what is the model even for?"

*Timed answer (35s).* "You shouldn't believe the model, and we don't ask you to. The model never produces a final number. It produces a structured claim: these invoice lines, this unit price, this quantity, this contractual rate. DuckDB computes the arithmetic deterministically, and Z3 proves the computed figure satisfies the contract constraints. Our unassisted baseline, the same 30B model answering directly, hallucinated an arithmetic or citation error on 31.4 percent of cases. The verified pipeline produced zero errors on the same corpus. The model is a reader and a drafter. The solver and the database are the accountants."

*Deep-dive proof points.*
- Baseline harness: same prompts, same corpus, model answers directly. Error rate measured by exact-match against ground-truth ledgers.
- Verified harness: model emits JSON claim, DuckDB SQL computes, Z3 checks. Any `unsat` result blocks output and routes to human review.
- Representative Z3 check for a deduction notice:

```python
from z3 import *
qty, unit, contract_rate, invoiced, deduction = Reals('qty unit contract_rate invoiced deduction')
s = Solver()
s.add(qty == 1200, contract_rate == 14.25, invoiced == 18540.00)
s.add(deduction == invoiced - qty * contract_rate)
s.add(deduction >= 0)
print(s.check())        # sat
print(s.model()[deduction])  # 1440
# Negated check proves no other deduction satisfies the constraints:
s.push(); s.add(deduction != 1440); print(s.check())  # unsat
```

*Traps to avoid.*
- Never say "the model is accurate." Say "the model's output is verified."
- Never say "0% hallucination" without the denominator. Say "zero errors observed across N cases."
- Never claim Z3 verifies the model's reading of the document. It verifies arithmetic and constraint satisfaction over the extracted claim.

**Q2. "Z3 only proves what you tell it. If the extraction is wrong, you've formally verified garbage. How do you catch that?"**

*Judge intent and probe.* The classic garbage-in objection. The judge wants to see a second, independent check on extraction, not more solver output.

*Timed answer (40s).* "Correct, and that's exactly why extraction has its own gate. Three things catch a bad extraction. First, every extracted figure carries a byte-offset citation back to the source PDF, and the TruLens groundedness check scores whether the claim is actually supported by that span. Second, the DuckDB layer reconciles extracted line items against the document's own subtotal and total. If the lines don't sum to the printed total, the case fails before Z3 ever runs. Third, Z3 encodes contract invariants, so an extraction that breaks a known rate or quantity bound comes back unsat. Failures route to a human queue. We'd rather surface a case than sign a wrong one."

*Deep-dive proof points.*
- TruLens RAG triad on the eval set: context relevance, groundedness, answer relevance. Composite 0.990. Groundedness threshold set at 0.95 for auto-pass.
- Reconciliation SQL:

```sql
SELECT invoice_id,
       SUM(qty * unit_price) AS computed_subtotal,
       MAX(printed_subtotal) AS printed_subtotal,
       ABS(SUM(qty * unit_price) - MAX(printed_subtotal)) < 0.01 AS reconciles
FROM invoice_lines
GROUP BY invoice_id
HAVING NOT reconciles;
```

*Traps to avoid.*
- Never say "Z3 guarantees correctness end to end."
- Never hide the human review queue. It is a feature.
- Never quote 0.990 without naming the three TruLens components.

**Q3. "Walk me through what Z3 actually checks. Give me a real `unsat` case."**

*Judge intent and probe.* Checks for genuine solver fluency versus a logo on a slide.

*Timed answer (45s).* "Z3 checks two things per case. Satisfiability: does a deduction amount exist that fits the invoice, the contract rate, and the statutory bounds? Uniqueness: is that the only amount? We assert the computed value, then assert its negation and expect unsat. A real unsat case from the Medline corpus: the model extracted a rebate rate of 3 percent, but the contract schedule table encoded a tiered rate that only reaches 3 percent above a volume threshold the invoice didn't meet. The tiered constraint made the extracted deduction unsat. The case went to review and the analyst confirmed the extraction had pulled the wrong tier. No notice was issued."

*Deep-dive proof points.*

```python
tier_rate = If(volume >= 50000, 0.03, If(volume >= 20000, 0.02, 0.01))
s.add(volume == 31400, claimed_rate == 0.03)
s.add(claimed_rate == tier_rate)
s.check()   # unsat
s.unsat_core()  # points at claimed_rate == tier_rate
```

*Traps to avoid.*
- Never present a `sat` result as a correctness proof by itself. Pair it with the negated uniqueness check.
- Never say "Z3 understands the contract." Say "we encode the contract's numeric constraints."

**Q4. "Why Meta Muse Glimmer 30B instead of a frontier model?"**

*Judge intent and probe.* Partner-stack alignment test, but also a sincerity test. A judge who works on the model will know its limits.

*Timed answer (40s).* "Three reasons. Data residency: invoice and customs data is confidential, and a 30B model runs on a single customer-controlled GPU with no egress. Specialization: we fine-tuned four LoRA adapters, one each for invoice line extraction, contract clause classification, customs entry parsing, and notice drafting, and a focused 30B adapter beats a general frontier model on our extraction benchmark. Cost: at our throughput the inference cost is a rounding error, which matters when a mid-market CFO is deciding whether to turn this on. And since verification is deterministic, model choice affects recall, not correctness. That's the whole point of the architecture."

*Deep-dive proof points.*
- LoRA config, all four adapters: rank 16, alpha 32, dropout 0.05, target modules `q_proj`, `k_proj`, `v_proj`, `o_proj`. Adapters hot-swapped per pipeline stage.
- Per-adapter eval: extraction F1 on held-out invoices; clause classification accuracy against lawyer-labeled set; customs field exact match against CBP Form 7501 ground truth.
- Single RTX-class GPU, 4-bit base weights, adapters in bf16.

*Traps to avoid.*
- Never say the 30B model is "as smart as" a frontier model. Say it is sufficient for the extraction task and the solver closes the gap.
- Never imply the adapters were trained on customer data. State the training corpus.

**Q5. "Rank 16 LoRA on four tasks. Why not one adapter, and why not full fine-tuning?"**

*Judge intent and probe.* ML engineering depth check.

*Timed answer (35s).* "One adapter per task because the tasks pull in different directions. Extraction wants terse JSON and penalizes any prose. Drafting wants statutory language and citations. A single adapter trained on both regressed extraction precision by several points in our ablation. Rank 16 was the knee of the curve: rank 8 underfit the customs parser, rank 32 added training time and VRAM with no measurable gain. Full fine-tuning would have meant four 30B checkpoints, which kills hot-swapping and the single-GPU deployment story."

*Deep-dive proof points.*
- Ablation table: rank 8, 16, 32 by task metric and VRAM. Keep it on a backup slide.
- Adapter swap latency measured in milliseconds, which is what makes the four-stage pipeline fit under one second.

*Traps to avoid.*
- Never quote ablation deltas you cannot reproduce on the demo machine.
- Never say "we tried everything." Name the three ranks tested.

**Q6. "Why DuckDB? This sounds like a Postgres job."**

*Judge intent and probe.* Architecture justification. Also probing whether "2.0.0 LTS" is a real deployment choice or a buzzword.

*Timed answer (35s).* "The workload is analytical, not transactional. We scan tens of thousands of invoice lines, join against contract rate schedules and customs entries, and aggregate. DuckDB's columnar engine does that in process with no server to operate, and it reads the Parquet evidence files directly. The LTS line matters because this goes into finance departments that will not accept a database that changes behavior every six weeks. And because DuckDB runs embedded, confidential data never leaves the machine the model runs on. Same residency argument as the model choice."

*Deep-dive proof points.*
- Drawback eligibility query, which is the core of the customs module:

```sql
SELECT e.entry_number, e.import_date, e.duty_paid, x.export_date,
       e.duty_paid * 0.99 AS recoverable
FROM customs_entries e
JOIN export_records x ON x.hts_code = e.hts_code
WHERE x.export_date <= e.import_date + INTERVAL 5 YEAR
  AND e.claim_filed IS NULL;
```

- Benchmark: full pipeline query set on the 50-filer corpus with timings. Quote the median, not the best run.

*Traps to avoid.*
- Never say DuckDB "replaces" the customer's ERP. It sits beside it.
- Never claim an exact version feature you haven't checked in the release notes.

**Q7. "Explain the TruLens score. What does 0.990 mean, and what's the floor?"**

*Judge intent and probe.* Checks whether a precise-looking number has a definition behind it.

*Timed answer (40s).* "TruLens scores three things per answer. Context relevance: did retrieval pull the right contract and invoice spans? Groundedness: is every sentence in the output supported by those spans? Answer relevance: does the output address the question asked? We report the mean of the three across the eval set, which came to 0.990. The operational floor is groundedness at 0.95. Below that, the case is flagged, regardless of what Z3 says, because a numerically correct notice that cites the wrong clause is still an unenforceable notice."

*Deep-dive proof points.*
- Per-component breakdown on a backup slide. Have the lowest-scoring case ready to discuss.
- Show one flagged case where groundedness dropped because the model cited a clause from a superseded contract version.

*Traps to avoid.*
- Never say 0.990 means "99 percent accurate." It is a composite of judged scores, not an error rate.
- Never imply TruLens is a formal method. It is an evaluation harness.

**Q8. "UCC 2-717. A buyer deducts damages. Why does a notice generated by a model carry any legal weight?"**

*Judge intent and probe.* The legal evaluator's core question. They want to hear who the legal actor is.

*Timed answer (45s).* "The notice carries weight because the buyer sends it, not because a model wrote it. Section 2-717 lets a buyer deduct damages arising from the seller's breach of the same contract from the price still due, provided the buyer gives notice of intent to deduct. The statute cares about three things: the damages must arise from that contract, the deduction must come from price due under that contract, and notice must be given. Our system enforces each of those as a constraint. The contract identifier on the invoice must match the contract the breach arose under. The deduction cannot exceed the unpaid balance on that contract. And the notice is generated with the specific breach, the computed amount, and the supporting invoice lines attached. A human at the buyer reviews and sends it. We produce a draft that survives scrutiny. We do not produce a legal act."

*Deep-dive proof points.*
- Z3 constraint set for 2-717: `deduction <= unpaid_balance_same_contract`, `breach_contract_id == invoice_contract_id`, `notice_date >= breach_discovery_date`.
- Notice template cites the contract section breached, the invoice numbers, the computed amount, and the method.

*Traps to avoid.*
- Never say "legally binding" or "court-tested." Say "structured to satisfy the statutory elements."
- Never say the system provides legal advice. It prepares documentation for the customer's counsel and finance team.
- Never ignore that 2-717 is state-adopted UCC with local variations. Say "we encode the uniform text and flag jurisdictions with known variations."

**Q9. "Duty drawback under 1313. That's a CBP filing with its own rules. What does your system actually do and what does it not do?"**

*Judge intent and probe.* Tests scope honesty on a regulated process.

*Timed answer (45s).* "Section 1313 lets an importer recover 99 percent of duties paid on goods that are later exported or destroyed, within five years of import. Most mid-market importers never claim it because matching imports to exports across thousands of entries is a data problem nobody staffs. That's the part we do. We ingest entry summaries and export records, match them under the substitution rules by HTS classification, compute the recoverable amount, and produce the claim package with every supporting line. What we do not do is file. Drawback claims go through ACE, often via a licensed customs broker, and the claimant bears the burden of proof. Our output is the evidence file that makes that filing fast and defensible."

*Deep-dive proof points.*
- The eligibility SQL from Q6, plus the 99 percent recovery constant encoded as a named constraint, not a magic number.
- Z3 check that no export record is matched to more than one import entry.
- Audit trail: every matched pair carries entry number, export document reference, and HTS code.

*Traps to avoid.*
- Never say "we file your drawback." Say "we prepare the claim package."
- Never quote a recovery figure as realized cash. Quote it as identified, unclaimed eligible duty.
- Never skip the five-year window or the substitution rules when describing eligibility.

**Q10. "0.82 seconds against 4.8. What's in that measurement and what's excluded?"**

*Judge intent and probe.* Benchmark hygiene. The judge is checking for cherry-picked timing.

*Timed answer (40s).* "The 0.82 second figure is median end-to-end per invoice: PDF text already extracted, model inference across the relevant adapters, DuckDB reconciliation, Z3 check, and notice draft rendered. It excludes OCR, which is a separate batch stage. The 4.8 second baseline is the unassisted model answering the same question in one long generation, because that's what a naive deployment looks like. The speedup comes from the adapters emitting short structured output instead of prose, and from the arithmetic moving out of the model into DuckDB. Tail latency matters more than median for a finance workflow, so we also report p95, which is where the Z3 timeout policy kicks in."

*Deep-dive proof points.*
- Timing breakdown per stage, median and p95, on the demo hardware.
- Z3 timeout set per case. Timeout is treated as a failed verification and routed to review, never as a pass.

*Traps to avoid.*
- Never say "real-time." Say "sub-second median per case."
- Never quote the median alone if asked about tails. Have p95 ready.
- Never let the baseline comparison imply the baseline was tuned for speed.

**Q11. "Does this scale to a Fortune 500 invoice volume, or is this a demo?"**

*Judge intent and probe.* Throughput and architecture ceiling.

*Timed answer (35s).* "The pipeline is embarrassingly parallel at the invoice level. Each case is independent, so throughput scales with GPU count for inference and with cores for DuckDB and Z3. On a single GPU we process a few thousand invoices per hour, which covers the mid-market customer we designed for. A Fortune 500 shared-services center would run multiple GPU workers against one columnar store. The one shared resource is the contract rate schedule, which is small and read-only. Nothing in the design requires a distributed database."

*Deep-dive proof points.*
- Measured invoices per hour on one GPU. Quote the measured number, not the extrapolation, and label any extrapolation as such.
- DuckDB Parquet partitioning by filer and fiscal quarter.

*Traps to avoid.*
- Never state an enterprise throughput figure you have not measured. Say "linear scaling, measured at N on one GPU."
- Never say "infinite" or "web scale."

**Q12. "You validated on 50 SEC filers. You don't have their invoices. What did you actually validate?"**

*Judge intent and probe.* This is the sharpest question in the packet. The judge knows public filings do not contain invoice-level data.

*Timed answer (45s).* "Right, and we're careful about this distinction. The 50-filer validation tested two things. First, the customs module against public import and export disclosures in 10-K and 10-Q filings, cross-referenced with public trade data, to estimate unclaimed drawback exposure. The UPS, Medline, and LCI figures are identified exposure estimates from that analysis, not recovered cash and not client engagements. Second, the full invoice pipeline was validated on a synthetic and anonymized invoice corpus constructed to match the filers' disclosed vendor terms. The arithmetic and verification results come from that corpus. We'd be misrepresenting the product if we said we'd recovered half a billion dollars for UPS. What we can say is that the filing-level analysis identifies that order of magnitude as potentially recoverable, and that the pipeline that would recover it has zero verified errors on the test corpus."

*Deep-dive proof points.*
- Methodology note on a backup slide: public data sources, estimation method, confidence range per filer.
- Keep the three headline figures as ranges with their basis, not point estimates.

*Traps to avoid.*
- Never say "we saved UPS $500M." Never say "customer." Never say "recovered."
- Never let the filer names imply endorsement or engagement.
- Never present exposure estimates with more precision than the public data supports.

**Q13. "What happens when Z3 and the model disagree, and who wins?"**

*Judge intent and probe.* Failure-mode design.

*Timed answer (30s).* "Z3 wins, always, and disagreement is a routed event, not a silent override. Unsat means the extracted claim cannot be reconciled with the contract constraints, so the case leaves the automated path and lands in a review queue with the unsat core attached. The unsat core tells the analyst which constraint failed, which is usually enough to spot the extraction error in seconds. The model never gets a second try on the same case without a human in the loop, because a retry loop is how you launder a hallucination into a pass."

*Deep-dive proof points.*
- Unsat core extraction and the review UI showing the failing constraint.
- Metrics: fraction of cases routed to review, median analyst resolution time.

*Traps to avoid.*
- Never say the system "self-corrects." Say it "routes."
- Never describe any automated retry that bypasses review.

**Q14. "What's your attack surface? Could a malicious invoice make the system issue a bad notice?"**

*Judge intent and probe.* Security and adversarial robustness, likely from a Meta engineer.

*Timed answer (40s).* "The primary vector is prompt injection through document text, so the extraction adapter is trained to emit a fixed JSON schema and nothing else, and the output is schema-validated before any downstream step. A document that tries to instruct the model produces either a schema violation or an extracted claim that the reconciliation and Z3 checks reject, because injected text can't change the printed totals or the contract schedule. Second vector: a forged invoice with internally consistent numbers. That would pass arithmetic verification, which is why the system matches invoices to purchase orders and contract records the customer controls. We verify against the customer's own data, not just the document."

*Deep-dive proof points.*
- Red-team set of injected invoices and the pass/fail outcome for each.
- Schema validation step and rejection log.

*Traps to avoid.*
- Never say "immune" or "unhackable."
- Never claim the model itself resists injection. Claim the pipeline contains it.

**Q15. "If you win, what do you build in the next ninety days, and what would you cut?"**

*Judge intent and probe.* Judgment and prioritization. Also checks whether the team knows its own weakest module.

*Timed answer (40s).* "Build: a jurisdictional overlay for 2-717 variations by state, because the uniform text is a starting point, not a finish line. And a broker handoff format for drawback claims so the package drops straight into ACE-ready workflow. Measure: a pilot with one real mid-market importer, with the drawback module only, because that's the module with the clearest cash outcome and the least legal variation. Cut: we'd drop the notice drafting adapter from the first release if counsel feedback says they'd rather use our data in their own template. The verification engine is the product. The prose is replaceable."

*Deep-dive proof points.*
- Roadmap with the pilot success metric defined as verified eligible duty identified, not cash recovered, since filing timelines run past ninety days.

*Traps to avoid.*
- Never promise revenue or signed customers.
- Never claim the legal overlay is already built.

## Pre-stage checklist

- Re-run the full benchmark on the demo machine the morning of judging. Replace any figure in this packet that moved.
- Have the live Z3 `sat` and `unsat` demo ready with the Medline tier-rate case loaded.
- Have the TruLens per-component breakdown and the lowest-scoring case on a backup slide.
- Have the 50-filer methodology note ready before Q12 is asked, because it will be asked.
- Confirm the DuckDB version string on the demo machine matches what the slides say.
- Agree on one phrasing for the headline exposure figures and use it every time: "identified unclaimed exposure from public filings."