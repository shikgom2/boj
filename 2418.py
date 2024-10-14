import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y, step):
    if dp[x][y][step] != -1:
        return dp[x][y][step]
    
    if grid[x][y] == target[l - 1] and step == l - 1:
        dp[x][y][step] = 1
        return dp[x][y][step]
    
    dp[x][y][step] = 0
    
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= h or ty < 0 or ty >= w:
            continue
        
        if grid[tx][ty] == target[step + 1]:
            dp[x][y][step] += dfs(tx, ty, step + 1)

    return dp[x][y][step]

h, w, l = map(int, input().split())
grid = [input().strip() for _ in range(h)]
target = input().strip()

dp = [[[-1] * l for _ in range(w)] for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == target[0]:
            ans += dfs(i, j, 0)

print(ans)
