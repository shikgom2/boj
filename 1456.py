import sys
input = sys.stdin.readline

def generate(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def solve(a,b):
    m = int(b**0.5) + 1
    primes = generate(m)
    count = 0

    for p in primes:
        x = p * p
        while True:
            if x > b:
                break
            if x >= a:
                count += 1
            if x > b // p:
                break
            x *= p
    return count

a,b = map(int, input().split())
print(solve(a, b))

