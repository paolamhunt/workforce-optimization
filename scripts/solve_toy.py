from __future__ import annotations

from workforce_opt.toy_model import ToyProblem, solve_toy


def main() -> None:
    # 4 time slots with headcount demand
    demand = [2, 3, 2, 1]

    # Minimum total skill per slot (scalar skill coverage)
    required_skill = [6, 8, 6, 3]

    # 5 employees with different costs and skills
    cost_per_shift = [10, 12, 9, 11, 8]
    skill_per_employee = [3, 2, 3, 2, 1]

    problem = ToyProblem(
        demand=demand,
        required_skill=required_skill,
        cost_per_shift=cost_per_shift,
        skill_per_employee=skill_per_employee,
        max_shifts_per_employee=2,
        overtime_penalty_per_shift=50,
    )

    sol = solve_toy(problem)

    print("\nToy Workforce Optimization Solution (skill + overtime penalty)")
    print("Demand per slot:", demand)
    print("Required skill per slot:", required_skill)
    print("Cost per employee:", cost_per_shift)
    print("Skill per employee:", skill_per_employee)
    print("Soft max shifts/employee:", problem.max_shifts_per_employee)
    print("Overtime penalty per extra shift:", problem.overtime_penalty_per_shift)

    print("\nAssignments (rows=employees, cols=time slots):")
    for i, row in enumerate(sol.assignments):
        print(f"  employee {i}: {row}  overtime={sol.overtime_by_employee[i]}")

    print("\nTotal cost:", sol.total_cost)


if __name__ == "__main__":
    main()