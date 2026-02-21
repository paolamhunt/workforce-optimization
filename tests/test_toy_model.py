from workforce_opt.toy_model import ToyProblem, solve_toy


def test_toy_model_meets_coverage_and_skill_constraints():
    problem = ToyProblem(
        demand=[1, 2],
        required_skill=[2, 3],
        cost_per_shift=[5, 6, 7],
        skill_per_employee=[2, 1, 2],
        max_shifts_per_employee=2,
        overtime_penalty_per_shift=50,
    )
    sol = solve_toy(problem)

    num_employees = len(problem.cost_per_shift)
    num_slots = len(problem.demand)

    for t in range(num_slots):
        covered = sum(sol.assignments[e][t] for e in range(num_employees))
        assert covered >= problem.demand[t]

        skill_covered = sum(sol.assignments[e][t] * problem.skill_per_employee[e] for e in range(num_employees))
        assert skill_covered >= problem.required_skill[t]