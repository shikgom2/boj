import random
import sys
sys.setrecursionlimit(10**6)

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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(x, c, n):
    return (x*x + c) % n

def pollard_rho(n):
    if miller_rabin(n): 
        return n
    if n == 1: 
        return 1
    if n%2 == 0: 
        return 2
    x, c, d = random.randrange(2,n), random.randrange(1,n),1
    y = x
    while d == 1:
        x = ((x**2%n)+c)%n
        y = ((y**2%n)+c)%n
        y = ((y**2%n)+c)%n
        d = gcd(n,abs(x-y))

        if d == n: 
            return pollard_rho(n)
    if miller_rabin(d): 
        return d
    else: 
        return pollard_rho(d)


n = int(input())
li = []
while n != 1:
    f = int(pollard_rho(n))
    li.append(f)
    n //= f

li.sort()   
for l in li:
    print(l)