import pytest

import numpy as np

from deephyper.evaluator import RunningJob
from deephyper.problem import HpProblem
from deephyper.search.hps import CBO
from deephyper.stopper import SuccessiveHalvingStopper


def run(job: RunningJob) -> dict:

    assert isinstance(job.stopper, SuccessiveHalvingStopper)

    max_budget = 50
    objective_i = 0

    for budget_i in range(1, max_budget + 1):
        objective_i += job["x"]

        job.record(budget_i, objective_i)
        if job.stopped():
            break

    return {
        "objective": job.objective,
        "metadata": {"budget": budget_i, "stopped": budget_i < max_budget},
    }


@pytest.mark.fast
@pytest.mark.hps
def test_successive_halving_stopper(tmp_path):

    # define the variable you want to optimize
    problem = HpProblem()
    problem.add_hyperparameter((0.0, 10.0), "x")

    stopper = SuccessiveHalvingStopper(max_steps=50, reduction_factor=3)
    search = CBO(
        problem,
        run,
        surrogate_model="DUMMY",
        stopper=stopper,
        random_state=42,
        log_dir=tmp_path,
    )

    results = search.search(max_evals=30)

    assert "m:budget" in results.columns
    assert "m:stopped" in results.columns
    assert "p:x" in results.columns
    assert "objective" in results.columns

    budgets = np.sort(np.unique(results["m:budget"].to_numpy())).tolist()
    assert budgets == [1, 3, 9, 50]


def run_with_failures(job: RunningJob) -> dict:

    assert isinstance(job.stopper, SuccessiveHalvingStopper)

    max_budget = 50
    objective_i = 0
    print("job.id", job.id)
    for budget_i in range(1, max_budget + 1):
        objective_i += job["x"]

        if int(job.id.split(".")[1]) % 2 == 0:
            objective_i = "F"

        job.record(budget_i, objective_i)
        if job.stopped():
            break

    return {
        "objective": job.objective,
        "metadata": {"budget": budget_i, "stopped": budget_i < max_budget},
    }


@pytest.mark.fast
@pytest.mark.hps
def test_successive_halving_stopper_with_failing_evaluations(tmp_path):

    # define the variable you want to optimize
    problem = HpProblem()
    problem.add_hyperparameter((0.0, 10.0), "x")

    stopper = SuccessiveHalvingStopper(max_steps=50, reduction_factor=3)
    search = CBO(
        problem,
        run_with_failures,
        surrogate_model="DUMMY",
        stopper=stopper,
        random_state=42,
        log_dir=tmp_path,
    )

    results = search.search(max_evals=30)

    print(results)
    # assert "m:budget" in results.columns
    # assert "m:stopped" in results.columns
    # assert "p:x" in results.columns
    # assert "objective" in results.columns

    # budgets = np.sort(np.unique(results["m:budget"].to_numpy())).tolist()
    # assert budgets == [1, 3, 9, 50]


if __name__ == "__main__":
    # test_successive_halving_stopper(tmp_path=".")
    test_successive_halving_stopper_with_failing_evaluations(tmp_path=".")
