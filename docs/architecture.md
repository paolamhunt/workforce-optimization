# Solver Architecture

Input Parameters:
- Demand per slot
- Skill requirements
- Employee costs
- Overtime penalty

Decision Variables:
- Binary assignment x[e,t]
- Overtime variables

Constraints:
- Coverage
- Skill coverage
- Soft max shifts

Objective:
Minimize base cost + overtime penalties