n,k = map(int, input().split())

arr = []
for _ in range(n):
    tmp = int(input())
    arr.append(tmp)

dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    for j in range(arr[i], k+1):
        if(dp[j - arr[i]]):
            dp[j] += dp[j-arr[i]]

print(dp[k])