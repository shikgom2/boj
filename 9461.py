mod = 10*100

def ipow(x, p):
    ret, piv = 1, x
    while p:
        if p & 1:
            ret = ret * piv % mod
        piv = piv * piv % mod
        p >>= 1
    return ret

def berlekamp_massey(x):
    ls, cur = [], []
    lf = ld = 0
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t = (t + x[i-j-1] * cur[j]) % mod
        if (t - x[i]) % mod == 0:
            continue
        if not cur:
            cur = [0] * (i+1)
            lf = i
            ld = (t - x[i]) % mod
            continue
        k = -(x[i] - t) * ipow(ld, mod - 2) % mod
        c = [0] * (i - lf - 1) + [k]
        c += [-j * k % mod for j in ls]
        if len(c) < len(cur):
            c += [0] * (len(cur) - len(c))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % mod
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % mod
        cur = c
    return [i % mod for i in cur]

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
        t = [0] * (2 * m)
        for j in range(m):
            for k in range(m):
                t[j+k] = (t[j+k] + v[j] * w[k]) % mod
        for j in range(2*m-1, m-1, -1):
            for k in range(1, m+1):
                t[j-k] = (t[j-k] + t[j] * rec[k-1]) % mod
        return t[:m]

    while n:
        if n & 1:
            s = mul(s, t)
        t = mul(t, t)
        n >>= 1

    ret = sum(s[i] * dp[i] % mod for i in range(m)) % mod
    return ret

def guess_nth_term(x, n):
    if n < len(x):
        return x[n]
    v = berlekamp_massey(x)
    if not v:
        return 0
    return get_nth(v, x, n)

t = int(input())
for _ in range(t):
    n = int(input())
    print(guess_nth_term([1, 1, 1, 2, 2, 3, 4, 5, 7, 9,12, 16,21], n-1))