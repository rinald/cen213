from util import test_reps
import experiment
import probability

n = 3  # 3 rolls
p = 1/6  # die lands on 5

# Net income after playing 1 game
net_income = {
    0: -1,
    1: 1,
    2: 2,
    3: 3
}


def gambling_game(N):
    balance = 0

    for _ in range(N):
        x = experiment.binomial(n, p)
        balance += net_income[x]

    print(f'E(X) ~= {balance/N}')


if __name__ == '__main__':
    bp = probability.binomial

    # E(X) = -P(X=0) + P(X=1) + 2*P(X=2) + 3*P(X=3)
    mean = sum(j*bp(n, p, i) for i, j in net_income.items())

    print(f'E(X) = {mean}')
    print()

    for N in test_reps:
        print(f'For N = {N}')
        gambling_game(N)
        print()
