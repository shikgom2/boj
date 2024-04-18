import sys
input = sys.stdin.readline

mod = 998244353
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

def precompute(max_n):
    # Initialize counts
    valid_counts = [0] * (max_n + 1)
    
    # Calculate for each modulus m
    for m in range(1, max_n + 1):
        count = 0
        # Dictionary to count occurrences of (a, b)
        pairs_count = {}
        
        # Check all pairs (x, y) modulo m
        for x in range(m):
            for y in range(m):
                a = (x * x + y * y) % m
                b = (x * y) % m
                # Use a tuple (a, b) to count occurrences modulo m
                if (a, b) in pairs_count:
                    pairs_count[(a, b)] += 1
                else:
                    pairs_count[(a, b)] = 1

        # Sum all unique (a, b) combinations
        count = len(pairs_count)
        
        # Store the result for this m
        valid_counts[m] = count
    
    return valid_counts

def solve(test_cases, max_n):
    valid_counts = precompute(max_n)
    
    results = []
    for n in test_cases:
        result = sum(valid_counts[1:n+1]) % mod
        results.append(result)
    
    return results

li = []
for i in range(1,101):
    li.append(i)

max_n = max(li)

res = solve(li, max_n)

t = int(input())
for _ in range(t):
    i = int(input())
    ans = guess_nth_term(res, i-1)
    print(ans)
