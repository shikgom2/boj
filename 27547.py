import sys
input = sys.stdin.readline

def solve(d, k, o, r):
    x = d * d + k * k + o * o + r * r
    x += 7 * min(k//2, r, o//2, d)
    return x

n, m = map(int, input().split())
s = input().rstrip()

d = 0
k = 0
o = 0
r = 0

for si in s:
    if si == 'd':
        d += 1
    elif si == 'k':
        k += 1
    elif si == 'o':
        o += 1
    else:
        r += 1

ans = solve(d, k, o, r)

for D in range (m + 1):
    for K in range (m + 1):
        for O in range (m + 1):
            for R in range (m + 1):
                if D + K + O + R <= m:
                    ans2 = solve(d + D, k + K, o + O, r + R)
                    ans = max(ans, ans2)

print(ans)
