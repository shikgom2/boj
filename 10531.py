from math import cos, sin
from functools import reduce
import operator
MOD = 998244353
ROOT = 3

def modpow(base, exp, mod=MOD):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def NTT(v, inv=False):
    S = len(v)
    j = 0
    for i in range(1, S):
        bit = S // 2
        while j >= bit:
            j -= bit
            bit //= 2
        j += bit
        if i < j:
            v[i], v[j] = v[j], v[i]

    k = 1
    while k < S:
        angle = modpow(ROOT, (MOD - 1) // (2 * k))
        if inv:
            angle = modpow(angle, MOD - 2)
        i = 0
        while i < S:
            z = 1
            for j in range(k):
                even = v[i + j]
                odd = v[i + j + k] * z
                v[i + j] = (even + odd) % MOD
                v[i + j + k] = (even - odd) % MOD
                z = (z * angle) % MOD
            i += k * 2
        k *= 2

    if inv:
        n_inv = modpow(S, MOD - 2)
        for i in range(S):
            v[i] = (v[i] * n_inv) % MOD

def mul(v, u):
    S = 1
    while S < 2 * max(len(v), len(u)):
        S <<= 1
    v += [0] * (S - len(v))
    u += [0] * (S - len(u))

    NTT(v, False)
    NTT(u, False)
    for i in range(S):
        v[i] = (v[i] * u[i]) % MOD
    NTT(v, True)

    return v[:len(v) + len(u) - 1]

m = int(input())
li = [0] * 200001
li[0] = 1
for _ in range(m):
    i = int(input())
    li[i] = 1
t = li
res = mul(li, t)

n = int(input())
cnt=0
for _ in range(n):
    i = int(input())
    if(res[i]):
        cnt += 1

print(cnt)