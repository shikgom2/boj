def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, n+1) if prime[p]]
    return primes

def solve(n):
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)

    if n in prime_set:
        return [n, 0, 0, 0]
    if n < 8:
        return -1

    if n % 2 == 0:
        primes_start = [2, 2]
    else:
        primes_start = [2, 3]
    remainder = n - sum(primes_start)

    for i in range(len(primes)):
        if primes[i] > remainder:
            break
        other_prime = remainder - primes[i]
        if other_prime in prime_set:
            return primes_start + [primes[i], other_prime]

    return -1

n=int(input())
solve(n)