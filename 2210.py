import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y, comb):
    if(len(comb) == 6):
        ans.append(comb)
        return
    
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if(0 <= nx and nx < 5 and 0 <= ny and ny < 5):
                dfs(nx, ny, comb + li[nx][ny])
li = []
ans = []

for _ in range(5):
    s = list(map(str, input().split()))
    li.append(s)

for i in range(5):
    for j in range(5):
        dfs(i,j, li[i][j])

ans = set(ans)
print(len(ans))