dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

def dfs(curx, cury, cnt, dir):
    if cnt == len(s):
        return True
    nx = curx + dx[dir]
    ny = cury + dy[dir]
    if(nx < 0 or ny < 0 or nx >= n or ny >= m):
        return False
    if arr[nx][ny] == s[cnt]:
        return dfs(nx, ny, cnt + 1, dir)
    return False

def check(curx, cury):
    for i in range(8):
        if dfs(curx, cury, 1, i):
            return True
    return False

s = input()
n ,m = map(int, input().split())
arr = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == s[0]:
            if check(i, j):
                print(1)
                exit()

print(0)