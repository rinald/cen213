from util import test_reps
import experiment
import probability

test_cases = [
    (5, 0.5),
    (5, 0.75),
    (10, 0.25),
    (10, 0.65),
    (15, 0.15),
    (15, 0.85)
]


def binomial_simulation(n, p, N):
    for x in range(n+1):
        nx = 0
        for _ in range(N):
            if x == experiment.binomial(n, p):
                nx += 1
        print(f'P(X = {x}) ~= {nx/N}')


if __name__ == '__main__':
    for n, p in test_cases:
        print(f'For n={n}, p={p}')
        print()

        for x in range(n+1):
            print(f'P(X = {x}) = {probability.binomial(n, p, x):.5f}')
        print()

        for N in test_reps:
            print(f'For N = {N}')
            binomial_simulation(n, p, N)
            print()

        print('-'*20)
