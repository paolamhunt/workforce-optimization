from __future__ import annotations

from workforce_opt.toy_model import ToyProblem, solve_toy


def main() -> None:
    # Toy setup:
    # 4 time slots with demand requirements
    demand = [2, 3, 2, 1]

    # 5 employees with different shift costs
    cost_per_shift = [10, 12, 9, 11, 8]

    # each employee can work at most 2 slots
    problem = ToyProblem(demand=demand, cost_per_shift=cost_per_shift, max_shifts_per_employee=2)

    sol = solve_toy(problem)

    print("\nToy Workforce Optimization Solution")
    print("Demand per slot:", demand)
    print("Cost per employee:", cost_per_shift)
    print("Max shifts/employee:", problem.max_shifts_per_employee)
    print("\nAssignments (rows=employees, cols=time slots):")
    for i, row in enumerate(sol.assignments):
        print(f"  employee {i}: {row}")
    print("\nTotal cost:", sol.total_cost)


if __name__ == "__main__":
    main()