def list_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    d = 2
    while d * d <= n:
        if is_prime[d]:
            for i in range(2 * d, n + 1, d):
                is_prime[i] = False
        d += 1
    return [i for i in range(n + 1) if is_prime[i]]

list_primes(100)
