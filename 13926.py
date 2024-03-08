import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (mod_pow(x, 2, n) + c) % n
        y = (mod_pow(y, 2, n) + c) % n
        y = (mod_pow(y, 2, n) + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)
    return d

def find_prime_factors(n):
    prime_factors = []
    factors = [n]
    while factors:
        f = factors.pop()
        if miller_rabin(f):
            prime_factors.append(f)
        else:
            divisor = pollards_rho(f)
            factors.append(divisor)
            factors.append(f // divisor)
    return list(set(prime_factors))

def euler_phi(n):
    prime_factors = find_prime_factors(n)
    phi = n
    for p in prime_factors:
        phi -= phi // p
    return phi

n = int(input())
if(n==1):
    print(1)
elif(miller_rabin(n)):
    print(n-1)
else:
    print(euler_phi(n))