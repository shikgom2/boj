import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    want = int(input())

    #dp[i] = i원으로 만들수있는 경우의 수
    dp = [0] * (want + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(li[i], want+1):
            dp[j] += dp[j - li[i]]

    print(dp[want])