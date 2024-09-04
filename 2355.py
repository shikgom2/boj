import sys
input = sys.stdin.readline

a,b =map(int ,input().split())
n = max(a,b)
m = min(a,b)

print((((n + 1) * n) // 2) - (((m - 1) * m) // 2))