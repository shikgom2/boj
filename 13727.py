import sys
input = sys.stdin.readline

mod = 10**9+7
lint = int

def ipow(x, p):
    ret = 1
    piv = x
    while p:
        if p & 1:
            ret = ret * piv % mod
        piv = piv * piv % mod
        p >>= 1
    return ret

def berlekamp_massey(x):
    ls, cur = [], []
    lf, ld = 0, 0

    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t = (t + 1 * x[i - j - 1] * cur[j]) % mod
        
        if (t - x[i]) % mod == 0:
            continue

        if not cur:
            cur = [0] * (i + 1)
            lf = i
            ld = (t - x[i]) % mod
            continue

        k = -(x[i] - t) * ipow(ld, mod - 2) % mod
        c = [0] * (i - lf - 1)
        c.append(k)
        for j in ls:
            c.append(-j * k % mod)
        
        if len(c) < len(cur):
            c += [0] * (len(cur) - len(c))
        
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % mod
        
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % mod
        
        cur = c
    
    for i in range(len(cur)):
        cur[i] = (cur[i] % mod + mod) % mod
    
    return cur

def get_nth(rec, dp, n):
    m = len(rec)
    s = [0] * m
    t = [0] * m
    s[0] = 1

    if m != 1:
        t[1] = 1
    else:
        t[0] = rec[0]

    def mul(v, w):
        m = len(v)
        t = [0] * (2 * m)

        for j in range(m):
            for k in range(m):
                t[j + k] += 1 * v[j] * w[k] % mod
                if t[j + k] >= mod:
                    t[j + k] -= mod
        
        for j in range(2 * m - 1, m - 1, -1):
            for k in range(1, m + 1):
                t[j - k] += t[j] * rec[k - 1] % mod
                if t[j - k] >= mod:
                    t[j - k] -= mod
        
        t = t[:m]
        return t

    while n:
        if n & 1:
            s = mul(s, t)
        t = mul(t, t)
        n >>= 1
    
    ret = 0
    for i in range(m):
        ret += 1 * s[i] * dp[i] % mod
    
    return ret % mod

def guess_nth_term(x, n):
    if n < len(x):
        return x[n]
    
    v = berlekamp_massey(x)
    if not v:
        return 0
    
    return get_nth(v, x, n)


n=int(input())
'''
v = [0,272,589185,930336768, 1545853411969, 2551276235535120, 4215052025641922305, 
     6962828841161217269760, 11502121570585083415761153, 19000667589592082076903397136,
     31387734017421172152812450818177, 51850272028503475884947837964718080]
'''
v = [1, 272, 589185, 930336768, 853401154, 217676188, 136558333, 415722813, 985269529, 791527976, 201836136, 382110354, 441223705, 661537677, 641601343, 897033284, 816519670, 365311407, 300643484, 936803543, 681929467, 462484986, 13900203, 657627114, 96637209, 577140657, 600647073, 254604056, 102389682, 811580173, 592550067, 587171680, 526467503, 265885773, 951722780, 219627841, 371508152, 283501391, 159234514, 439380999, 722868959, 125599834, 351398134, 456317548, 365496182, 614778702, 502680047, 193063685, 309004764, 743901785, 870955115, 312807829, 160375015, 691844624, 137034372, 350330868, 895680450, 282610535, 317897557, 28600551, 583305647, 539409363, 327406961, 627805385, 680183978, 681299085, 954964592, 743524009, 788048339, 699454626, 666369521]

ans = guess_nth_term(v, n)
print(ans)