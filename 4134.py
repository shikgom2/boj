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

n = int(input())
for _ in range(n):
    k = int(input())
    while(True):
        if(miller_rabin(k)):
            print(k)
            break
        else:
            k += 1