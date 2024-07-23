import sys
input = sys.stdin.readline
n =int(input())
 
dp=[0] * 101
dp[1]=2
dp[2]=4
 
cur=3
for i in range(3, n+1):
    dp[i]=dp[i-1] + cur
    if i%3!=0:
        cur+=1

print(dp[n])
