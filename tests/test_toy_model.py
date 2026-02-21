from workforce_opt.toy_model import ToyProblem, solve_toy


def test_toy_model_meets_coverage_constraints():
    problem = ToyProblem(demand=[1, 2], cost_per_shift=[5, 6, 7], max_shifts_per_employee=2)
    sol = solve_toy(problem)

    # Check coverage: sum employees working each slot >= demand
    for t, d in enumerate(problem.demand):
        covered = sum(sol.assignments[e][t] for e in range(len(problem.cost_per_shift)))
        assert covered >= d