import sys
input = sys.stdin.readline 


# 1 -> 11 has two probality. 1,1 or 11
# hou about 11 -> 111 this probality has (1,1,1), (11, 1), (1, 11)

#how about over 26?
#25 is (2,5), (25) but 251 is (2,5,1), (25, 1) is has two probality it's same!

#check (i-2 + i-1) is ok, dp[i] = dp[i-2] + dp[i-1]
#else 


li = [" "] + list(map(int, input().rstrip()))
if(li[1] == 0):
    print(0)
    exit()

dp = [0] * 5001
dp[0] = 1
dp[1] = 1

mod = 10**6

for i in range(2, len(li)):
    if(li[i] != 0):
        dp[i] += dp[i-1] % mod
        
    if(li[i-1] * 10 + li[i] <= 26):
        dp[i] += dp[i-2] % mod

print(dp[len(li) - 1] % mod)