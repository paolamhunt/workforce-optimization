from __future__ import annotations

from workforce_opt.toy_model import ToyProblem, solve_toy


def main() -> None:
    # Toy setup:
    demand = [2, 3, 2, 1]
    cost_per_shift = [10, 12, 9, 11, 8]

    # Soft max shifts: allow exceeding, but penalize
    problem = ToyProblem(
        demand=demand,
        cost_per_shift=cost_per_shift,
        max_shifts_per_employee=2,
        overtime_penalty_per_shift=50,
    )

    sol = solve_toy(problem)

    print("\nToy Workforce Optimization Solution (with overtime penalty)")
    print("Demand per slot:", demand)
    print("Cost per employee:", cost_per_shift)
    print("Soft max shifts/employee:", problem.max_shifts_per_employee)
    print("Overtime penalty per extra shift:", problem.overtime_penalty_per_shift)

    print("\nAssignments (rows=employees, cols=time slots):")
    for i, row in enumerate(sol.assignments):
        print(f"  employee {i}: {row}  overtime={sol.overtime_by_employee[i]}")

    print("\nTotal cost:", sol.total_cost)


if __name__ == "__main__":
    main()