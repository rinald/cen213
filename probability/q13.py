from util import N_simulations
import experiment
import probability

test_cases = [(3, 0.5), (4, 0.25), (6, 0.75), (2, 0.1)]


def negative_binomial_simulation(r, p, N):
    for x in range(r, r+5):
        nx = 0
        for _ in range(N):
            if x == experiment.negative_binomial(r, p):
                nx += 1
        print(f'P(X = {x}) ~= {nx/N}')


if __name__ == '__main__':
    for r, p in test_cases:
        print(f'For r={r}, p={p}')
        print()

        for x in range(r, r+5):
            print(f'P(X = {x}) = {probability.negative_binomial(r, p, x):.5f}')
        print()

        for N in N_simulations:
            print(f'For N = {N}')
            negative_binomial_simulation(r, p, N)
            print()

        print('-'*20)
