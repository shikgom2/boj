import sys
input = sys.stdin.readline 
from itertools import permutations

mod = 998244353

def add(a, b):
    a += b
    if a >= mod:
        a -= mod
    return a

def prod(a, b):
    return a * b % mod

def make_line(n, maxk, inv):
    res = [0] * (maxk + 1)
    res[0] = 1
    for i in range(1, maxk + 1):
        res[i] = prod(res[i - 1], prod(inv[i], n - i + 1))
    return res

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x = sum(1 for a in map(int, x) if a > 0)
y = sum(1 for b in map(int, y) if b > 0)

inv = [0] * (n + 1)
inv[1] = 1
for i in range(2, n + 1):
    inv[i] = prod(inv[mod % i], mod - mod // i)

ca = make_line(x, n, inv)
cb = make_line(y, n, inv)
cna = make_line(n - x, n, inv)
cnb = make_line(n - y, n, inv)

ans = 0
for k in range(min(x, y) + 1):
    ans = add(ans, prod(prod(ca[k], cb[k]), prod(cnb[x - k], cna[y - k])))

print(ans)