import cmath
import sys
input = sys.stdin.readline


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

a = [1] * 1000001

for i in range(2, 1000):
    if a[i]:
        for j in range(i*i, 1000001, i):
            a[j] = 0

li = [0] * 1000001
li1 = [0] * 1000001

for i in range(2, 1000001):
    if(a[i] == 1):
        if(i*2 <= 1000000):
            li1[2*i] = 1
        if(i%2 == 1):
            li[i] = 1

res = mul(li, li1)

N = int(input())
for _ in range(N):
    n = int(input())
    print(res[n])