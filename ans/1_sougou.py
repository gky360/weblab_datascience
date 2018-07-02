import numpy as np


def list_primes(n):
    is_prime = np.ones(n + 1, dtype=np.bool)
    is_prime[[0, 1]] = False
    d = 2
    while d * d <= n:
        if is_prime[d]:
            is_prime[range(2 * d, n + 1, d)] = False
        d += 1
    return np.arange(n + 1)[is_prime]

list_primes(100)
