def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)

dp = [0] * 1001
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j:
            continue

        if gcd(i, j) == 1:
            cnt += 2
    dp[i] = dp[i-1] + cnt


t = int(input())
for _ in range(T):
    n = int(input())

    print(dp[n])