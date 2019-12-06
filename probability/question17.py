from util import bernoulli_trial, test_reps

# Simulate the random experiment of flipping
# a coin until we get two heads in a row


def two_heads_simulation(N):
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

    print(f'E(X) ~= {flips/N}')


if __name__ == '__main__':
    print('E(X) = 6')
    print()
    for N in test_reps:
        print(f'For N = {N}')
        two_heads_simulation(N)
        print()
