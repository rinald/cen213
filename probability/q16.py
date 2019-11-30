from util import N_simulations
import experiment
import probability

r = 5  # 5 heads
p = 0.5  # lands heads
A = 3  # as specified


def gambling_game(N):
    balance = 0

    for _ in range(N):
        x = experiment.negative_binomial(r, p)
        if x <= 7:
            balance += A-1
        elif x > 8:
            balance -= 1

    print(f'E(X) ~= {balance/N}')


if __name__ == '__main__':
    nbp = probability.negative_binomial

    # E(X) = 3*P(X<=7) + P(X=8) - 1
    mean = 3*sum(nbp(r, p, i) for i in range(5, 8)) + nbp(r, p, 8) - 1

    print(f'E(X) = {mean}')
    print()

    for N in N_simulations:
        print(f'For N = {N}')
        gambling_game(N)
        print()
