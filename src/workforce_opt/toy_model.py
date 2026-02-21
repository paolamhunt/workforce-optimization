from __future__ import annotations

from dataclasses import dataclass

from ortools.sat.python import cp_model


@dataclass(frozen=True)
class ToyProblem:
    # Demand per time slot (e.g., 4 slots in a day)
    demand: list[int]
    # Cost per employee per slot worked
    cost_per_shift: list[int]
    # Max shifts each employee can work
    max_shifts_per_employee: int


@dataclass(frozen=True)
class ToySolution:
    total_cost: int
    # assignments[e][t] in {0,1}
    assignments: list[list[int]]


def solve_toy(problem: ToyProblem) -> ToySolution:
    num_slots = len(problem.demand)
    num_employees = len(problem.cost_per_shift)

    model = cp_model.CpModel()

    # x[e,t] = 1 if employee e works slot t
    x: dict[tuple[int, int], cp_model.IntVar] = {}
    for e in range(num_employees):
        for t in range(num_slots):
            x[(e, t)] = model.NewBoolVar(f"x_e{e}_t{t}")

    # Coverage constraints: sum_e x[e,t] >= demand[t]
    for t in range(num_slots):
        model.Add(sum(x[(e, t)] for e in range(num_employees)) >= problem.demand[t])

    # Max shifts per employee: sum_t x[e,t] <= max_shifts
    for e in range(num_employees):
        model.Add(sum(x[(e, t)] for t in range(num_slots)) <= problem.max_shifts_per_employee)

    # Objective: minimize cost
    model.Minimize(
        sum(x[(e, t)] * problem.cost_per_shift[e] for e in range(num_employees) for t in range(num_slots))
    )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 5.0

    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError("No feasible solution found for toy problem.")

    assignments = []
    for e in range(num_employees):
        row = [int(solver.Value(x[(e, t)])) for t in range(num_slots)]
        assignments.append(row)

    total_cost = int(solver.ObjectiveValue())
    return ToySolution(total_cost=total_cost, assignments=assignments)