n=int(input())
dp = [-1] * 1001
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, 1001):
    tmp = [0] * 1001
    for j in range(i//2 + 1):
        left = j
        right = (i - 2) - j
        tmp[dp[left] ^ dp[right]] = 1

    for k in range(i):
        if tmp[k] == 0:
            dp[i] = k
            break
if(dp[n] == 0):
    print(2)
else:
    print(1)