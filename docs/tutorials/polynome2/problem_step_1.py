from deephyper.problem import HpProblem

Problem = HpProblem()

Problem.add_dim("units", (1, 100))
Problem.add_dim("activation", ["N/A", "relu", "sigmoid", "tanh"])
Problem.add_dim("lr", (0.0001, 1.0))

Problem.add_starting_point(units=10, activation="N/A", lr=0.01)

if __name__ == "__main__":
    print(Problem)
