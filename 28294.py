mod = 10**9 + 7

def solve(a, b):
    ret = 1
    while b:
        if b & 1:
            ret *= a
            if mod != -1:
                ret %= mod
        a *= a
        if mod != -1:
            a %= mod
        b >>= 1
    return ret

n, a = map(int, input().split())
ans = (solve(n, a + 1) * (n - 1)) % mod
ans = (ans - n * solve(n - 1, a + 1)) % mod
ans = (ans + n * solve(n - 1, a)) % mod

print(ans)