import sys
sys.setrecursionlimit(10 ** 5)

def dp(n, m, dir):
    #Out of Range
    if n < 0 or m < 0 or n >= a or m >= b:
        return -999999999 
    
    #1*1
    if n == (a-1) and m == (b-1):
        return cost[n][m]
    
    #Exist
    if memo[dir][n][m] is not None:
        return memo[dir][n][m]
    
    temp = -999999999
    #before moved down
    if dir == 0:
        temp = max(dp(n+1, m, 0), dp(n, m-1, 1), dp(n, m+1, 2)) + cost[n][m]
    #before moved left
    elif dir == 1:
        temp = max(dp(n+1, m, 0), dp(n, m -1, 1)) + cost[n][m]
    #before moved right
    elif dir == 2:
        temp = max(dp(n+1, m, 0), dp(n, m+1, 2)) + cost[n][m]
    
    memo[dir][n][m] = temp
    return temp

a, b = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(a)]
memo = [[[None] * b for _ in range(a)] for _ in range(3)]

print(dp(0, 0, 0))