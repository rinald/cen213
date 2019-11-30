from util import bernoulli_trial


def binomial(n, p):
    x = 0

    for i in range(n):
        if bernoulli_trial(p):
            x += 1

    return x


def negative_binomial(r, p):
    x = 0
    s = 0

    while s < r:
        x += 1

        if bernoulli_trial(p):
            s += 1

    return x


def geometric(p):
    return negative_binomial(1, p)
