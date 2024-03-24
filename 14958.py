import cmath

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

n,m = map(int, input().split())
li = list(map(str, input().strip()))
li2 = list(map(str, input().strip()))
li2.reverse()

rps1 = [0] * n
rps2 = [0] * m
result = [0] * (n+m-1)

#rock vs paper
for a in range(n):
    if(li[a] == 'R'):
        rps1[a] = 1
    else:
        rps1[a] = 0

for a in range(m):
    if(li2[a] == 'P'):
        rps2[a] = 1
    else:
        rps2[a] = 0

#print(rps1)
#print(rps2)
res = mul(rps1, rps2)
#print(res)
for a in range(n+m-1):
    result[a] += res[a]

#paper vs scissors
rps1 = [0] * n
rps2 = [0] * m

for a in range(n):
    if(li[a] == 'P'):
        rps1[a] = 1
    else:
        rps1[a] = 0

for a in range(m):
    if(li2[a] == 'S'):
        rps2[a] = 1
    else:
        rps2[a] = 0

res = mul(rps1, rps2)

for a in range(n+m-1):
    result[a] += res[a]

#scissors vs rock
rps1 = [0] * n
rps2 = [0] * m
for a in range(n):
    if(li[a] == 'S'):
        rps1[a] = 1
    else:
        rps1[a] = 0

for a in range(m):
    if(li2[a] == 'R'):
        rps2[a] = 1
    else:
        rps2[a] = 0

res = mul(rps1, rps2)

for a in range(n+m-1):
    result[a] += res[a]

ans = 0
for i in range(m-1, n+m-1):
    ans = max(ans, result[i])
print(ans)