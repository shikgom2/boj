import sys
input = sys.stdin.readline

n = int(input())
n += 4

grundy = [0] * (n + 1)
dp = [False] * (n + 1)

max_val = 0

for i in range(2, n + 1):
    dp = [False] * (n + 1)
    for j in range(2, i - 2):
        dp[grundy[j] ^ grundy[i - 1 - j]] = True
    j = 0
    while dp[j]:
        j += 1
    grundy[i] = j
    max_val = max(max_val, j)

print("1" if grundy[n] > 0 else "2")