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

def palindrome(inp, b, odd):
    n = inp
    palin = inp
    if odd:
        n = n // b
        
    while (n > 0):
        palin = palin * b + (n % b)
        n = n // b
    return palin

def generate_palindrome(n):
    palin = []
    for j in range(2):
        i = 1
        while (palindrome(i, 10, j % 2) < n):
            palin.append(palindrome(i, 10, j % 2))
            i = i + 1
    return palin

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

n,m = map(int, input().split())
cnt = 0

palin = generate_palindrome(m+1)
for p in palin:
    if(p >= n and miller_rabin(p)):
            cnt += 1
print(cnt)
