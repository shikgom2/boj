def sieve(n):
    """Generate all prime numbers less than or equal to n."""
    prime = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n+1) if prime[p]]

def find_two_primes(primes, n):
    """Find two prime numbers that sum up to n."""
    i, j = 0, len(primes) - 1
    while i <= j:
        if primes[i] + primes[j] == n:
            return primes[i], primes[j]
        elif primes[i] + primes[j] < n:
            i += 1
        else:
            j -= 1
    return -1, -1

def solve(n):
    primes = sieve(n)  # Generate primes up to n
    if n < 8:
        return -1
    if n % 2 == 0:
        a, b = 2, 2
        n -= 4
    else:
        a, b = 2, 3
        n -= 5
    c, d = find_two_primes(primes, n)
    if c == -1:
        return -1
    return a, b, c, d

n = int(input())
result = solve(n)
if result == -1:
    print(result)
else:
    print(*result)