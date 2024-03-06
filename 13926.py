import random
def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def is_composite(a, d, n, s):
    x = mod_pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = mod_pow(x, 2, n)
        if x == n - 1:
            return False
    return True

def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1) if n > 3 else 2
        if is_composite(a, d, n, s):
            return False
    return True

def find_prime_factors(n):
    prime_factors = []
    if n % 2 == 0:
        prime_factors.append(2)
        while n % 2 == 0:
            n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            prime_factors.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def euler_phi(n):
    prime_factors = find_prime_factors(n)
    phi = n
    for p in prime_factors:
        phi -= phi // p
    return phi

n = int(input())
if(miller_rabin(n)):
    print(n-1)
else:
    print(euler_phi(n))
