import cmath
import sys
input = sys.stdin.readline

def FFT(v, inv):
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
        angle = -cmath.pi / k if inv else cmath.pi / k
        w = complex(cmath.cos(angle), cmath.sin(angle))
        i = 0
        while i < S:
            z = complex(1, 0)
            for j in range(k):
                even = v[i + j]
                odd = v[i + j + k]
                v[i + j] = even + z * odd
                v[i + j + k] = even - z * odd
                z *= w
            i += k * 2
        k *= 2

    if inv:
        for i in range(S):
            v[i] /= S

def mul(v, u):
    vc = [complex(x, 0) for x in v]
    uc = [complex(x, 0) for x in u]
    S = 2
    while S < len(v) + len(u):
        S *= 2
    vc += [complex(0, 0)] * (S - len(vc))
    uc += [complex(0, 0)] * (S - len(uc))
    
    FFT(vc, False)
    FFT(uc, False)
    
    for i in range(S):
        vc[i] *= uc[i]
    FFT(vc, True)
    
    w = [round(vc[i].real) for i in range(S)]
    return w

n = int(input())
li = list(map(int, input().split()))
h1 = [0] * 60001
for i in li:
    h1[i+30000] = 1

n = int(input())
li2 = list(map(int, input().split()))
h2 = [0] * 60001
for i in li2:
    h2[i+30000] = 1

n = int(input())
li3 = list(map(int, input().split()))
h3 = [0] * 60001
for i in li3:
    h3[i+30000] = 1

res = mul(h1, h3)

ans = 0
for i in range(60001):
    ans += h2[i] * res[2*i]

print(ans)