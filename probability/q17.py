from util import bernoulli_trial, N_simulations


def coin_flip(N):
    p = 0.5

    flips = 0

    for _ in range(N):
        x = 0
        h = 0

        while h < 2:
            if bernoulli_trial(p):
                h += 1
            else:
                h = 0
            x += 1

        flips += x

    print(f'E(X) = {flips/N}')


if __name__ == '__main__':
    for N in N_simulations:
        print(f'For N = {N}')
        coin_flip(N)
        print()
