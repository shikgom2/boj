import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited, team):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    
    ans = 1
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if li[nx][ny] and not visited[nx][ny] and li[nx][ny] == team:
                q.append((nx, ny))
                ans += 1
                visited[nx][ny] = True
    return ans

i,j = map(int, input().split())
li = []
for _ in range(j):
    s = input().rstrip()
    li.append(s)

visited = [[False] * len(li[0]) for _ in range(len(li))]

ans1 = 0
ans2 = 0 
for i in range(len(li)):
    for j in range(len(li[0])):
        if li[i][j] and not visited[i][j]:
            if(li[i][j] == 'W'):
                ans = bfs(i, j, li, visited, 'W')
                ans1 = ans1 + ans * ans
            else:
                ans = bfs(i, j, li, visited, 'B')
                ans2 = ans2 + ans * ans

print(ans1, ans2)