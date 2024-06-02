mod = 10007

def solve(s, e, dp):
    if(s > e):
        return 0
    if(s == e):
        return 1

    if(dp[s][e] != -1):
        return dp[s][e]

    dp[s][e] = (solve(s, e - 1, dp) + solve(s + 1, e, dp)) % mod
    dp[s][e] -= solve(s + 1, e - 1, dp)
    if(dp[s][e] < 0):
        dp[s][e] += mod

    if(s1[s] == s1[e]):
        dp[s][e] = (dp[s][e] + solve(s + 1, e - 1, dp) + 1) % mod

    return dp[s][e] % mod

s1 = input()
dp = [[-1] * 1001 for _ in range(1001)]
ans = solve(0, len(s1) - 1, dp)
print(ans)

