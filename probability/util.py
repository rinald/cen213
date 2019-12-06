from math import factorial
from random import random

test_reps = [10**i for i in range(3, 7)]


def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def bernoulli_trial(p):
    if p >= random():
        return True
    else:
        return False
