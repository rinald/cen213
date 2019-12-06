from util import test_reps
import experiment
import probability

R = 10  # compute the first R probabilities

test_cases = [
    (3, 0.5),
    (4, 0.25),
    (5, 0.1),
    (6, 0.75),
    (7, 0.4)
]


def negative_binomial_simulation(r, p, N):
    for x in range(r, r+R):
        nx = 0
        for _ in range(N):
            if x == experiment.negative_binomial(r, p):
                nx += 1
        print(f'P(X = {x}) ~= {nx/N}')


if __name__ == '__main__':
    print(f'Showing only the first {R} probabilities.')
    print()
    for r, p in test_cases:
        print(f'For r={r}, p={p}')
        print()

        for x in range(r, r+R):
            print(f'P(X = {x}) = {probability.negative_binomial(r, p, x):.5f}')
        print('...')
        print()

        for N in test_reps:
            print(f'For N = {N}')
            negative_binomial_simulation(r, p, N)
            print('...')
            print()

        print('-'*20)
