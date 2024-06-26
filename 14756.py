import sys
input = sys.stdin.readline
from functools import reduce
import operator

MOD = 998244353
ROOT = 3
IROOT = pow(ROOT, MOD-2, MOD)

def NTT(v, inv):
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
        z = pow(ROOT if inv else IROOT, (MOD-1) // (2*k), MOD)
        i = 0
        while i < S:
            w = 1
            for j in range(k):
                even = v[i + j]
                odd = v[i + j + k] * w % MOD
                v[i + j] = (even + odd) % MOD
                v[i + j + k] = (even - odd + MOD) % MOD
                w = w * z % MOD
            i += k * 2
        k *= 2
    
    if inv:
        invS = pow(S, MOD-2, MOD)
        for i in range(S):
            v[i] = v[i] * invS % MOD

def mul(v, u):
    S = 2
    while S < len(v) + len(u):
        S *= 2
    vc = v + [0] * (S - len(v))
    uc = u + [0] * (S - len(u))
    NTT(vc, False)
    NTT(uc, False)
    for i in range(S):
        vc[i] = vc[i] * uc[i] % MOD
    NTT(vc, True)
    return vc

    
n, l, m, w = map(int, input().split())

sky = []
scope = []

for i in range(m):
    sky.append(list(map(int, input().split())))

vinvert = [[] for _ in range(m)]

for i in range(m):
    li = list(map(int, input().split()))
    scope.append(li)
    vinvert[i] = [li[l - j - 1] for j in range(l)]

convolution = []

for i in range(m):
    convolution.append(mul(sky[i], vinvert[i]))

ans = 0

for i in range(n - l + 1):
    s = 0
    for j in range(m):
        s += convolution[j][l + i - 1]
    if s > w:
        ans += 1

print(ans)