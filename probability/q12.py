from util import N_simulations
import experiment
import probability

test_cases = [(5, 0.5), (7, 0.3), (10, 0.2), (2, 0.1)]


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

        for N in N_simulations:
            print(f'For N = {N}')
            binomial_simulation(n, p, N)
            print()

        print('-'*20)
