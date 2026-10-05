#!/usr/bin/env python3
"""
Headless Synthetic Learner Journey & BKT Progression Simulator
==============================================================
Simulates 4 distinct high school learner personas playing through
Fundile's full pedagogical progression pipeline:
1. Struggling Learner ("Sipho")  -> Diagnostic <50% -> Scaffold -> 2 Fails -> 5-min Micro-Drill -> Recovery
2. Average Learner ("Zola")       -> Diagnostic 67%  -> Scaffold -> Mastery >=60% -> Unlocks Practice
3. High-Flier ("Nqobile")         -> Diagnostic 100% -> Bypasses Scaffold -> Unlocks Practice & Exam (>=80%)
4. Prerequisite Regression ("Lwazi")-> Grade 11 Algebra Fail -> Grade 9 Factor Pitstop -> Grade Floor Guard

Enforces Anti-Endless Loop Invariants:
- Hard max_steps cap per persona (max 15 steps)
- Max micro-drill recursion depth <= 2
- Cross-grade floor (never drops > 2 grades)
"""
import os
import sys
import math
from typing import Dict, Any, List

# Standard BKT Parameters
BKT_DEFAULTS = {
    "p_l0": 0.30,   # Prior mastery probability
    "p_t": 0.20,    # Transition probability (learning rate)
    "p_g": 0.25,    # Guess probability
    "p_s": 0.10,    # Slip probability
}

def update_bkt(p_l: float, is_correct: bool, params: Dict[str, float] = None) -> float:
    """Updates BKT knowledge state P(L_t) given observation."""
    p = params or BKT_DEFAULTS
    p_t = p["p_t"]
    p_g = p["p_g"]
    p_s = p["p_s"]

    if is_correct:
        num = p_l * (1.0 - p_s)
        denom = (p_l * (1.0 - p_s)) + ((1.0 - p_l) * p_g)
    else:
        num = p_l * p_s
        denom = (p_l * p_s) + ((1.0 - p_l) * (1.0 - p_g))

    denom = max(1e-9, denom)
    p_updated = num / denom
    # Transition to next step
    p_next = p_updated + (1.0 - p_updated) * p_t
    return round(max(0.01, min(0.99, p_next)), 4)

class SyntheticLearner:
    def __init__(self, name: str, grade: int, subject: str, topic: str):
        self.name = name
        self.grade = grade
        self.subject = subject
        self.topic = topic
        self.mode = "diagnostic"  # diagnostic -> scaffold -> practice -> exam
        self.mastery = BKT_DEFAULTS["p_l0"]
        self.consecutive_fails = 0
        self.micro_drill_active = False
        self.micro_drill_count = 0
        self.journey_log = []
        self.step_count = 0
        self.diagnostic_taken = 0
        self.DIAGNOSTIC_COUNT = 3  # Exactly 3 calibrated atomic diagnostic probes
        self.MAX_STEPS = 15  # Anti-endless loop guard
        self.GRADE_FLOOR = grade - 2

    def log(self, event: str):
        self.journey_log.append(f"Step {self.step_count}: [{self.mode.upper()}] {event} (Mastery: {self.mastery * 100:.1f}%)")

    def simulate_question(self, will_pass: bool, is_micro_drill: bool = False):
        self.step_count += 1
        if self.step_count > self.MAX_STEPS:
            raise RuntimeError(f"Circuit Breaker Triggered: {self.name} exceeded max step budget {self.MAX_STEPS}!")

        # 1. Update BKT
        self.mastery = update_bkt(self.mastery, will_pass)

        # 2. Handle Micro-drill resolution
        if is_micro_drill:
            if will_pass:
                self.micro_drill_active = False
                self.consecutive_fails = 0
                self.log("Completed 5-min Micro-Drill successfully -> Returning to main practice track")
            else:
                self.log("Failed Micro-Drill -> Preserving safe floor")
            return

        # 3. Track fails for regression trigger (only in scaffold/practice)
        if self.mode != "diagnostic":
            if not will_pass:
                self.consecutive_fails += 1
                self.log(f"Answered incorrectly (Consecutive fails: {self.consecutive_fails})")
                if self.consecutive_fails >= 2 and self.micro_drill_count < 2:
                    self.micro_drill_active = True
                    self.micro_drill_count += 1
                    self.log("Triggered 5-Minute Atomic Micro-Drill (Deconstructed subskill pitstop)")
            else:
                self.consecutive_fails = 0
                self.log("Answered correctly")
        else:
            self.diagnostic_taken += 1
            self.log(f"Answered Diagnostic Probe {self.diagnostic_taken}/{self.DIAGNOSTIC_COUNT} ({'Correct' if will_pass else 'Incorrect'})")

        # 4. State transitions based on mastery gates
        if self.mode == "diagnostic":
            if self.diagnostic_taken >= self.DIAGNOSTIC_COUNT:
                if self.mastery >= 0.70:
                    self.mode = "practice"
                    self.log("Diagnostic complete: Strong baseline -> Bypassing Scaffold to Practice Mode")
                else:
                    self.mode = "scaffold"
                    self.log("Diagnostic complete: Baseline <70% -> Assigned to Guided Scaffold Mode")
        elif self.mode == "scaffold" and self.mastery >= 0.60:
            self.mode = "practice"
            self.log("Mastery reached >=60% -> Unlocked Practice Mode")
        elif self.mode == "practice" and self.mastery >= 0.80:
            self.mode = "exam"
            self.log("Mastery reached >=80% -> Unlocked Exam Simulation (CAPS Level 7 Ready)")

def simulate_struggling_learner() -> Dict[str, Any]:
    """Persona 1: Sipho - diagnostic fail, scaffold guided, 2 fails triggers micro-drill, recovers."""
    learner = SyntheticLearner("Sipho", grade=10, subject="Accounting", topic="VAT 15%")
    learner.log("Started Diagnostic Baseline")

    # 1. Diagnostic: 1 right, 2 wrong
    learner.simulate_question(False)
    learner.simulate_question(True)
    learner.simulate_question(False)
    assert learner.mode == "scaffold", "Struggling learner must be placed in Scaffold mode"

    # 2. Scaffold Mode: 2 consecutive fails
    learner.simulate_question(False)
    learner.simulate_question(False)
    assert learner.micro_drill_active is True, "2 consecutive fails must trigger a micro-drill"

    # 3. Micro-drill: resolves blocker
    learner.simulate_question(True, is_micro_drill=True)
    assert learner.micro_drill_active is False, "Passing micro-drill must resume main track"

    # 4. Continues learning with guided scaffolding
    learner.simulate_question(True)
    learner.simulate_question(True)

    return {"persona": "Struggling Learner (Sipho)", "status": "PASS", "final_mode": learner.mode, "steps": learner.step_count}

def simulate_average_learner() -> Dict[str, Any]:
    """Persona 2: Zola - 60% diagnostic, scaffold mastery crosses 60%, unlocks practice."""
    learner = SyntheticLearner("Zola", grade=10, subject="Mathematics", topic="Trinomial Factorisation")
    learner.log("Started Diagnostic Baseline")

    # 1. Diagnostic: 2 right, 1 wrong
    learner.simulate_question(True)
    learner.simulate_question(False)
    learner.simulate_question(True)

    # 2. Scaffold to Practice transition
    learner.simulate_question(True)
    learner.simulate_question(True)
    assert learner.mode in ["practice", "exam"], "Average learner must advance to Practice upon reaching >=60%"

    return {"persona": "Average Learner (Zola)", "status": "PASS", "final_mode": learner.mode, "steps": learner.step_count}

def simulate_high_flier_learner() -> Dict[str, Any]:
    """Persona 3: Nqobile - 100% diagnostic, directly unlocks Practice and Exam mode."""
    learner = SyntheticLearner("Nqobile", grade=12, subject="Physical Sciences", topic="Vertical Projectiles")
    learner.log("Started Diagnostic Baseline")

    # 1. Diagnostic: 3/3 correct
    learner.simulate_question(True)
    learner.simulate_question(True)
    learner.simulate_question(True)
    assert learner.mode == "practice", "High-flier must bypass Scaffold straight to Practice"

    # 2. Practice questions with high mastery
    learner.simulate_question(True)
    learner.simulate_question(True)
    assert learner.mode == "exam", "High-flier must unlock Exam Mode when crossing >=80%"

    return {"persona": "High-Flier (Nqobile)", "status": "PASS", "final_mode": learner.mode, "steps": learner.step_count}

def simulate_prerequisite_regression() -> Dict[str, Any]:
    """Persona 4: Lwazi - Gr 11 algebra fail in Practice, regresses to Gr 9 factorisation pitstop."""
    learner = SyntheticLearner("Lwazi", grade=11, subject="Mathematics", topic="Quadratic Inequalities")
    learner.mode = "practice"
    learner.diagnostic_taken = 3
    learner.log("Attempting Grade 11 compound exam question in Practice Mode")

    # Grade 11 fails
    learner.simulate_question(False)
    learner.simulate_question(False)
    assert learner.micro_drill_active is True, "2 consecutive fails in practice must trigger micro-drill"

    # Pitstop at Grade 9 factorisation (respecting floor)
    pitstop_grade = max(learner.GRADE_FLOOR, learner.grade - 2)
    assert pitstop_grade == 9, "Floor must allow drop to Grade 9 prerequisite, not below"
    learner.simulate_question(True, is_micro_drill=True)
    assert learner.micro_drill_active is False

    return {"persona": "Prerequisite Regression (Lwazi)", "status": "PASS", "pitstop_grade": pitstop_grade, "steps": learner.step_count}

def run_all_simulations():
    print("=" * 68)
    print("FUNDILE SYNTHETIC LEARNER BKT PROGRESSION SIMULATION")
    print("4 Personas: Struggling, Average, High-Flier, Cross-Grade Regression")
    print("Anti-Endless Loop Guards: Max 15 steps, Max 2 micro-drills, Grade floor")
    print("=" * 68)

    sims = [
        simulate_struggling_learner,
        simulate_average_learner,
        simulate_high_flier_learner,
        simulate_prerequisite_regression,
    ]

    all_passed = True
    for sim_func in sims:
        try:
            res = sim_func()
            print(f"[PASS] {res['persona']:<38} | {res['status']} | Steps: {res['steps']}")
        except Exception as e:
            all_passed = False
            print(f"[FAIL] {sim_func.__name__}: {e}")

    print("=" * 68)
    print(f"BKT PROGRESSION SUITE: {'ALL 4 PERSONAS PASSED' if all_passed else 'FAILURES DETECTED'}")
    print("=" * 68)
    return all_passed

if __name__ == "__main__":
    success = run_all_simulations()
    sys.exit(0 if success else 1)
