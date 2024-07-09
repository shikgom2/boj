import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            if (li[nx][ny] == '1') and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt
                
i,j = map(int, input().split())
li = []
for _ in range(i):
    s = input().rsplit()
    li.append(s)
visited = [[False] * len(li[0]) for _ in range(len(li))]

ans = 0
ans1 = 0
for i in range(len(li)):
    for j in range(len(li[0])):
        if(li[i][j] == '1' and visited[i][j] == False):
            ans += 1
            ans1 = max(ans1, bfs(i, j, li, visited))

print(ans)
print(ans1)
    