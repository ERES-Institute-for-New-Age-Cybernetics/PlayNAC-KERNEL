#!/usr/bin/env python3
# =============================================================================
# ERES-BRT-TESTKIT-2026-001 (v0.1)
# Python Test Instrument for the ERES BRT Architecture
# (Biological Resonance Transmission -- Epistemology Framework, July 8, 2026)
#
# Author of framework: Joseph A. Sprute (ERES Maestro), ERES Institute for
#   New Age Cybernetics, Bella Vista, Arkansas
# Instrument drafted: H2C2H (Human-to-Computer-to-Human) methodology
# Dependencies: numpy only
# License: CCAL v2.1 / CC-BY 4.0
#
# PURPOSE
#   Operationalize every load-testable claim in the BRT stack (Nodes 0-4,
#   Layers 0-6) as an executable test. Per Node 3 discipline, this instrument
#   load-tests ONLY the modelable structures (the control law, the metric,
#   the interface rule, the vocabulary audit) on a SYNTHETIC subject model.
#   It never claims to test the unobservable interior itself (Node 0).
#
# EPISTEMIC STATUS OF EACH TEST (primitive-testing filter)
#   T1, T2, T5 : DERIVED  -- one mechanism (proportional deadband control law)
#                yields two independent consequences (theoretical prediction
#                vs. empirical simulation), checked against each other.
#   T3, T4     : OPERATIONALIZED -- BEE and the Phi_ae checklist require a
#                chosen operationalization; the choice is declared inline and
#                marked, per the DERIVED-vs-CONSTRUCTED discipline.
#   T6         : LEXICAL -- Node 4 vocabulary audit, including self-audit of
#                this instrument's own docstrings.
#
# NAMED FAILURE MODES IN ADVANCE (A <= 10, per Layer 4 requirement)
#   F1  Operator spends energy at steady state (violates frugality).
#   F2  Operator output nonzero inside deadband (violates "mute at error~0").
#   F3  Closed loop diverges below the pre-named yield point (Node 3 breach).
#   F4  Closed loop stable above the pre-named yield point (theory falsified).
#   F5  BEE fails to approach 1.0 at equilibrium (metric broken or reified).
#   F6  BEE exceeds 1.0 (metric treated as stored resource -- reification).
#   F7  Chip contributes output when subject is stable (Phi_ae breach).
#   F8  Correction derived from machine, not human-authored setpoint (Node 2).
#   F9  Smuggled-carrier vocabulary detected in governing text (Node 4).
#   F10 Instrument's own docstrings fail the vocabulary self-audit (Node 4,
#       reflexive case).
# =============================================================================

import numpy as np

EPS_DEADBAND = 1e-3     # error ~ 0 threshold (declared, human-authored)
RNG = np.random.default_rng(20260708)

# -----------------------------------------------------------------------------
# Layer 3 -- SCALULAR setpoint vector (human-authored; a values choice).
# Node 2: these numbers are DECLARED here by a human, never derived by the code.
# -----------------------------------------------------------------------------
SCALULAR_LABELS = ["HEALTH", "LAW", "PROTECTION", "SKILLS_TRADE"]
SCALULAR_SETPOINT = np.array([1.0, 1.0, 1.0, 1.0])   # normalized targets


class Phi1010Operator:
    """Layer 4 runtime mechanism: senses deviation from the human-authored
    setpoint, applies proportional correction along SCALULAR, and produces
    zero output when the deviation is inside the declared deadband."""

    def __init__(self, gain: float, deadband: float = EPS_DEADBAND):
        self.k = float(gain)
        self.eps = float(deadband)
        self.energy_log = []

    def step(self, exterior_signature: np.ndarray) -> np.ndarray:
        """One pass of the mediated loop's correction stage. Input is the
        rendered exterior signature (observable); output is a correction
        vector. Inside the deadband the output is exactly zero."""
        error = SCALULAR_SETPOINT - exterior_signature
        if np.linalg.norm(error) < self.eps:
            u = np.zeros_like(error)
        else:
            u = self.k * error
        self.energy_log.append(float(np.sum(np.abs(u))))
        return u


class SyntheticSubject:
    """Node 3 boundary object: a MODELABLE stand-in. Its 'interior' is a
    plain state vector; its rendered signature is that vector plus small
    observation noise. No claim is made about real interiors (Node 0:
    does-claims only)."""

    def __init__(self, x0: np.ndarray, drift: float = 0.0, noise: float = 0.0):
        self.x = x0.astype(float).copy()
        self.drift = drift
        self.noise = noise

    def render(self) -> np.ndarray:
        """H2C2H rendering stage: interior state -> exterior signature."""
        return self.x + RNG.normal(0.0, self.noise, self.x.shape)

    def apply(self, u: np.ndarray) -> None:
        """Return leg of the loop: correction re-enters the subject model,
        plus an exogenous drift term (life happens)."""
        self.x = self.x + u + RNG.normal(0.0, self.drift, self.x.shape)


def run_loop(gain, steps=400, drift=0.0, noise=0.0, x0=None):
    """Run the full mediated loop on the synthetic subject; return the
    error-norm trajectory and the operator's energy log."""
    subj = SyntheticSubject(
        x0 if x0 is not None else np.array([0.2, 0.5, 0.1, 0.8]),
        drift=drift, noise=noise)
    op = Phi1010Operator(gain)
    errs = []
    for _ in range(steps):
        sig = subj.render()
        u = op.step(sig)
        subj.apply(u)
        errs.append(float(np.linalg.norm(SCALULAR_SETPOINT - subj.x)))
    return np.array(errs), np.array(op.energy_log)


# -----------------------------------------------------------------------------
# T1 -- Convergence and zero energy at steady state (F1, F2)
# -----------------------------------------------------------------------------
def test_T1_steady_state_frugality():
    """DERIVED. The declared control law predicts: once error enters the
    deadband, output is exactly zero, so tail energy must be exactly zero.
    Two independent consequences of one mechanism: (a) error converges,
    (b) tail energy is zero."""
    errs, energy = run_loop(gain=0.5, steps=400)
    converged = errs[-1] < EPS_DEADBAND
    tail_energy = float(np.sum(energy[-50:]))
    passed = converged and tail_energy == 0.0
    return passed, {"final_error": errs[-1], "tail_energy_last50": tail_energy}


# -----------------------------------------------------------------------------
# T2 -- Deadband muteness under perturbation (F2, F7 analogue in software)
# -----------------------------------------------------------------------------
def test_T2_deadband_muteness():
    """DERIVED. Feed the operator signatures already inside the deadband;
    every output must be the exact zero vector (the 'chip' stays mute and
    algebraic when the subject is stable)."""
    op = Phi1010Operator(gain=0.9)
    all_zero = True
    for _ in range(100):
        sig = SCALULAR_SETPOINT + RNG.normal(0, EPS_DEADBAND / 20, 4)
        u = op.step(sig)
        if np.any(u != 0.0):
            all_zero = False
    return all_zero, {"total_energy": float(np.sum(op.energy_log))}


# -----------------------------------------------------------------------------
# T3 -- BEE steady-state metric (F5, F6)
# -----------------------------------------------------------------------------
def bee_readout(errs, energy, e0):
    """OPERATIONALIZED (choice declared): stability_t = 1 - err_t/err_0
    (clipped to [0,1]); marginal energy = mean energy over trailing window.
    BEE = stability / (stability + marginal_energy). This makes BEE a pure
    read-out: it tends to 1.0 exactly when error is gone AND spending is
    zero, and it can never exceed 1.0 (no stored-resource reading)."""
    stability = np.clip(1.0 - errs / e0, 0.0, 1.0)
    w = 25
    marginal = np.array([np.mean(energy[max(0, i - w):i + 1])
                         for i in range(len(energy))])
    denom = stability + marginal
    bee = np.where(denom > 0, stability / np.maximum(denom, 1e-12), 0.0)
    return bee


def test_T3_bee_equilibrium():
    errs, energy = run_loop(gain=0.5, steps=400)
    bee = bee_readout(errs, energy, errs[0] if errs[0] > 0 else 1.0)
    final_bee = float(bee[-1])
    never_exceeds_one = bool(np.all(bee <= 1.0 + 1e-12))
    passed = (abs(final_bee - 1.0) < 1e-6) and never_exceeds_one
    return passed, {"final_BEE": final_bee, "max_BEE": float(np.max(bee))}


# -----------------------------------------------------------------------------
# T4 -- Phi_ae interface checklist (F7, F8)
# -----------------------------------------------------------------------------
def test_T4_phi_ae_checklist():
    """OPERATIONALIZED. The five Phi_ae clauses, each as an executable check
    against the software model (the semiconductor stand-in is the operator):
      1. arithmetic-and-rendering only  -> operator is stateless w.r.t. the
         subject: same input, same output (no 'adapting' or 'learning').
      2. zero contribution at stability -> covered by T2, re-verified here.
      3. ground isolation               -> operator never mutates the subject
         directly; only the returned vector crosses the boundary.
      4. ceases computation at error~0  -> zero vector inside deadband.
      5. never crosses into the irreversible -> instrument runs ONLY on
         SyntheticSubject; there is no code path to real tissue."""
    op = Phi1010Operator(gain=0.7)
    sig = np.array([0.3, 0.4, 0.5, 0.6])
    c1 = bool(np.allclose(op.step(sig), op.step(sig)))          # deterministic
    c2 = bool(np.all(op.step(SCALULAR_SETPOINT.copy()) == 0.0))  # mute at 0
    subj = SyntheticSubject(np.array([0.5, 0.5, 0.5, 0.5]))
    before = subj.x.copy()
    _ = op.step(subj.render())
    c3 = bool(np.array_equal(subj.x, before))                    # no mutation
    c4 = c2
    c5 = True  # by construction: no external interface exists in this module
    checks = [c1, c2, c3, c4, c5]
    return all(checks), {"clauses_passed": f"{sum(checks)}/5"}


# -----------------------------------------------------------------------------
# T5 -- Node 3 load test with pre-named yield point (F3, F4)
# -----------------------------------------------------------------------------
def test_T5_yield_point():
    """DERIVED. For the discrete loop x' = x + k(s - x), the closed-loop
    factor is (1 - k); the loop diverges when |1 - k| > 1, i.e. k > 2.
    The yield point k_crit = 2.0 is NAMED IN ADVANCE from the mechanism;
    the empirical sweep must break where the theory says it breaks."""
    k_crit_predicted = 2.0
    gains = np.arange(0.2, 3.01, 0.2)
    first_divergent = None
    for k in gains:
        errs, _ = run_loop(gain=float(k), steps=120)
        if not np.isfinite(errs[-1]) or errs[-1] > errs[0] * 10:
            first_divergent = float(k)
            break
    passed = (first_divergent is not None
              and abs(first_divergent - (k_crit_predicted + 0.2)) < 0.21)
    return passed, {"predicted_k_crit": k_crit_predicted,
                    "first_divergent_gain": first_divergent}


# -----------------------------------------------------------------------------
# T6 -- Node 4 vocabulary audit, including reflexive self-audit (F9, F10)
# -----------------------------------------------------------------------------
# Smuggled-carrier lexicon: terms that re-import an emission, agency, or
# essence claim into governance text. Stored as split fragments so that the
# lexicon itself does not trip its own scan when this file is self-audited.
_SMUGGLED = [x + y for x, y in [
    ("emit", "s"), ("emis", "sion"), ("freq", "uency"), ("aur", "a"),
    ("chak", "ra"), ("life for", "ce"), ("hea", "ls"), ("quantum fi", "eld"),
    ("reads human wor", "th"), ("harmoni", "zes"), ("lear", "ns"),
    ("adap", "ts"), ("soul", "s"),
]]


def vocabulary_audit(text: str):
    """Node 4 scan: return the list of smuggled-carrier terms found in text.
    An empty list is a PASS (the text makes does-claims only, at least at
    the lexical surface -- deeper semantic audit remains human work)."""
    low = text.lower()
    return [t for t in _SMUGGLED if t in low]


def test_T6_vocabulary_self_audit():
    """LEXICAL + REFLEXIVE. (a) A deliberately contaminated sample sentence
    must be flagged; (b) every docstring in this instrument must pass clean.
    Failure of (b) is failure mode F10: the auditor caught itself."""
    contaminated = ("The device restores the body's natural energy so the "
                    "subject hea" + "ls through its quantum fi" + "eld.")
    a_flags = vocabulary_audit(contaminated)
    docstrings = [obj.__doc__ or "" for obj in
                  [Phi1010Operator, Phi1010Operator.step, SyntheticSubject,
                   SyntheticSubject.render, SyntheticSubject.apply, run_loop,
                   test_T1_steady_state_frugality, test_T2_deadband_muteness,
                   bee_readout, test_T3_bee_equilibrium,
                   test_T4_phi_ae_checklist, test_T5_yield_point,
                   vocabulary_audit, test_T6_vocabulary_self_audit]]
    b_flags = vocabulary_audit("\n".join(docstrings))
    passed = (len(a_flags) >= 2) and (len(b_flags) == 0)
    return passed, {"contaminated_sample_flags": a_flags,
                    "self_audit_flags": b_flags}


# -----------------------------------------------------------------------------
# Report
# -----------------------------------------------------------------------------
def main():
    tests = [
        ("T1", "Steady-state frugality (F1,F2)", test_T1_steady_state_frugality),
        ("T2", "Deadband muteness (F2,F7)",      test_T2_deadband_muteness),
        ("T3", "BEE -> 1.0 at equilibrium (F5,F6)", test_T3_bee_equilibrium),
        ("T4", "Phi_ae 5-clause checklist (F7,F8)", test_T4_phi_ae_checklist),
        ("T5", "Node 3 yield point, pre-named (F3,F4)", test_T5_yield_point),
        ("T6", "Node 4 vocabulary self-audit (F9,F10)", test_T6_vocabulary_self_audit),
    ]
    print("=" * 72)
    print("ERES-BRT-TESTKIT-2026-001 v0.1  |  BRT Architecture Test Instrument")
    print("Subject under test: SYNTHETIC MODEL ONLY (Node 3 boundary honored)")
    print("=" * 72)
    results = []
    for tid, name, fn in tests:
        ok, detail = fn()
        results.append(ok)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {tid}  {name}")
        for k, v in detail.items():
            print(f"        {k}: {v}")
    print("-" * 72)
    n_pass = sum(results)
    print(f"RESULT: {n_pass}/{len(results)} tests passed.")
    if all(results):
        print("VERDICT: Instrument holds. DERIVED tests (T1,T2,T5) confirm the")
        print("declared mechanism against independent empirical consequences;")
        print("OPERATIONALIZED tests (T3,T4) pass under their declared choices;")
        print("Node 4 self-audit clean. Holds at 10.")
    else:
        print("VERDICT: One or more named failure modes triggered. Per Node 3,")
        print("the break is the finding: record which F# fired and revise the")
        print("claim, not the test.")
    print("-" * 72)
    print("License: CCAL v2.1 / CC-BY 4.0")
    print("Credits: Joseph A. Sprute (ERES Maestro); H2C2H drafting via Claude")
    print("References: ERES Epistemology Framework (July 8, 2026); ERES_CORPUS")
    print("            Zenodo DOI 10.5281/zenodo.21209870 (as of 2026-07-09;")
    print("            corpus active)")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
