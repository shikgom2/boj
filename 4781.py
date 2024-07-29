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

def unbounded_knapsack(max_weight, weights, values):
    n = len(weights)
    dp = [0 for x in range(max_weight + 1)]

    for w in range(max_weight + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[max_weight]

while(True):
    n,t = map(float, input().split())
    if(n == 0 and t == 0):
        break
    t *= 100
    t = int(t)

    li1 = []
    li2 = []
    for _ in range(int(n)):
        a,b= map(float, input().split())
        li1.append(int(a))
        li2.append(int(b*100))

    ans = unbounded_knapsack(t, li2, li1)
    print(ans)