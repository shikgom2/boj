import sys
input = sys.stdin.readline

n = int(input())

dp =[0] * (100050)

check = [0] * (1500000)
check[0] = 1

for i in range(1, n+1):
    tmp = dp[i-1] - i
    if(tmp < 0):
        tmp = dp[i-1] + i
    elif(check[tmp] == 1):
        tmp = dp[i-1] + i
    
    dp[i] = tmp

    check[tmp] = 1
    
print(dp[n])