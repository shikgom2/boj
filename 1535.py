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

n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

print(knapsack(99, li1, li2))