import sys
input = sys.stdin.readline
import math

def dist(a, b, X, Y):
    dx = X[a] - X[b]
    dy = Y[a] - Y[b]
    return math.sqrt(dx * dx + dy * dy)

def solve(pos, last, n, X, Y, dp):
    if pos == n + 1:
        return dist(pos - 1, last, X, Y)

    if dp[pos][last] >= 0:
        return dp[pos][last]

    if last == 0:
        last = 1

    res = float('inf')
    res = min(res, solve(pos + 1, last, n, X, Y, dp) + dist(pos, pos - 1, X, Y))
    res = min(res, solve(pos + 1, pos - 1, n, X, Y, dp) + dist(pos, last, X, Y))

    dp[pos][last] = res
    return res

t = int(input())

for _ in range(t):
    n = int(input())

    X = [0] * 513
    Y = [0] * 513
    dp = [[-1] * 513 for _ in range(513)]

    for i in range(1, n + 1):
        X[i], Y[i] = map(int, input().split())

    X[0], Y[0] = X[1], Y[1]

    print(f"{solve(1, 1, n, X, Y, dp):.3f}")