import sys
input = sys.stdin.readline

def mex(s):
    g = 0
    while g in s:
        g += 1
    return g

def get(n):
    if n <= INF:
        return f[n]
    idx = (n - 1) % 34 + 1
    return f[idx]


INF = 70
f = [0] * (INF + 1)

for n in range(3, INF + 1):
    s = set()
    for cut in range(2, n):
        left = f[cut - 1]
        right = f[n - cut]
        s.add(left ^ right)
    f[n] = mex(s)


n, m = map(int, input().split())
fn = get(n)
fm = get(m)

if fn != 0 and fm != 0:
    gnm = 1
else:
    gnm = fn + fm
if gnm == 0:
    print("hs")
else:
    print("sh")
