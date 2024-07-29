import sys
input = sys.stdin.readline

def knapsack(max_weight, weights, values):
    n = len(weights)
    dp = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][max_weight]

n,t = map(int, input().split())
li1 = []
li2 = []
for _ in range(n):
    a,b= map(int, input().split())
    li1.append(a)
    li2.append(b)

ans = knapsack(t, li1, li2)
print(sum(li2) - ans)