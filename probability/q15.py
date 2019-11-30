from util import N_simulations
import experiment
import probability

p = 0.3  # successful shot
b = 4  # total bullets


def sniper_simulation(N):
    shots = 0

    for _ in range(N):
        x = experiment.geometric(p)
        if x > b:
            x = b

        shots += x

    print(f'E(X) ~= {shots/N}')


if __name__ == '__main__':
    gp = probability.geometric

    # E(X) = 4 - 3*P(X=1) - 2*P(X=2) - P(X=3)
    mean = b + sum((i-b)*gp(p, i) for i in range(1, b))

    print(f'E(X) = {mean:.3f}')
    print()

    for N in N_simulations:
        print(f'For N = {N}')
        sniper_simulation(N)
        print()
