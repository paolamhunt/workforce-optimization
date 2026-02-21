# Workforce Optimization (Constraint-Based Scheduling)

A production-structured optimization project that converts demand requirements into a feasible, cost-minimizing staffing plan using OR-Tools (CP-SAT).

This repository is intentionally designed to demonstrate senior applied data science capabilities:

- Mathematical formulation of a decision problem  
- Hard vs. soft constraints  
- Cost tradeoff modeling  
- Reproducible project structure  
- Automated testing and CI  

---

## Problem Overview

We solve a simplified workforce scheduling problem.

**Given:**

- Demand per time slot  
- Cost per employee per shift  
- A target maximum number of shifts per employee  

**We decide:**

- Which employees work which time slots  

**Objective:**

Minimize total staffing cost while meeting coverage requirements and penalizing overtime.

---

## Model Formulation (Toy Version)

### Decision Variables

- `x[e,t] ∈ {0,1}`  
  1 if employee `e` works time slot `t`  

- `overtime[e] ≥ 0`  
  Number of shifts beyond the soft maximum  

---

### Hard Constraints

- Coverage:  
  `sum_e x[e,t] >= demand[t]`

---

### Soft Constraint

- Soft maximum shifts per employee  
  Overtime is allowed but penalized in the objective  

---

### Objective

Minimize:

Base Shift Cost  
+ (Overtime Penalty × Overtime Shifts)

This structure mirrors real workforce planning problems where hard infeasibility is avoided but excess load is costly.

---

## Project Structure

workforce-optimization/

- src/workforce_opt/
  - toy_model.py
- scripts/
  - solve_toy.py
- tests/
  - test_toy_model.py
- Makefile
- pyproject.toml
- .github/workflows/ci.yml

The project uses a `src` layout, proper packaging, and CI enforcement.

---

## Quickstart

1. Create environment and install:

make install

2. Solve the toy model:

make solve

You should see:

- Demand per slot  
- Employee assignments  
- Overtime per employee  
- Total cost  

---

## Sensitivity: Overtime Penalty

This model treats the maximum shifts per employee as a soft constraint via an overtime penalty.

You can experiment by modifying `overtime_penalty_per_shift` in `scripts/solve_toy.py`.

Behavior changes as follows:

- Penalty = 0  
  The optimizer overloads the cheapest employees  

- Moderate penalty (e.g., 50)  
  Balances cost efficiency and workload distribution  

- High penalty (e.g., 200+)  
  Strongly discourages overtime and spreads assignments  

This demonstrates how objective coefficients encode business tradeoffs.

---

## Why This Matters

Workforce optimization problems in production systems require:

- Clear constraint modeling  
- Tradeoff-aware objectives  
- Feasibility handling via soft penalties  
- Transparent decision logic  

This repository demonstrates those principles in a minimal but production-structured form.

## Design Decisions

### Why CP-SAT?

CP-SAT (OR-Tools) handles mixed integer problems efficiently and supports complex constraints while remaining production-ready.

### Why treat overtime as a soft constraint?

Real-world systems cannot always strictly enforce maximum shifts. 
By modeling overtime as a penalized variable, the model remains feasible while encoding business preferences in the objective.

### Why add skill-based coverage?

Operational scheduling often requires role or skill coverage, not just headcount. 
A scalar skill constraint demonstrates how richer constraints can be layered without restructuring the solver.

### Why keep the model small?

The goal is clarity of formulation, not scale. 
This repo demonstrates constraint modeling discipline and tradeoff thinking in a minimal but realistic form.