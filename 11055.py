import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

#dp n^2
dp = [0] * n

for i in range(n):
    cur = 0
    for j in range(i, n):
        if(cur <= li[j]):
            cur = li[j]
            dp[i] += cur
            print(f"UPDATE {i}, {cur}")

print(max(dp))