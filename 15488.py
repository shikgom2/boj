import sys
input = sys.stdin.readline

n, x, y, k = map(int, input().split())
dp = [[0 for _ in range(n)] for _ in range(n) ]
dp[y-1][x-1] = 1

#knight directions
dy = [2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

#k operation
for _ in range(k):
    #set temp map
    temp = [[0 for _ in range(n)] for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            for d in range(8):
                ny, nx = i + dy[d], j + dx[d]
                #if knight's move is within the map
                if(0 <= ny < n and 0 <= nx < n):
                    temp[ny][nx] += dp[i][j] * 0.125
                    
    dp = temp

ans = 0
for i in range(n): 
    ans += sum(dp[i])
print(ans)