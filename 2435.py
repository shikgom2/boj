import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))

g_Sums = [0] * (n + 1)

for i in range(1, n + 1):
    temp = li[i-1]
    g_Sums[i] = g_Sums[i - 1] + temp

ans = float('-inf')
for i in range(n - k + 1):
    cur = g_Sums[i + k] - g_Sums[i]
    if ans < cur:
        ans = cur

print(ans)