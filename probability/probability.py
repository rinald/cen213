from util import choose


def binomial(n, p, x):
    return choose(n, x)*p**x*(1-p)**(n-x)


def negative_binomial(r, p, x):
    return choose(x-1, r-1)*p**r*(1-p)**(x-r)


def geometric(p, x):
    return negative_binomial(1, p, x)


def hypergeometric(N, k, n, x):
    return choose(k, x)*choose(N-k, n-x)/choose(N, n)
