from collections import deque

def bfs(x, y, li, visited):
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    e = len(li)
    v = len(li[0])
    
    ans = 1
    while q:
        x, y, z = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= e or ny < 0 or ny >= v:
                continue

            #print(nx, ny)

            if(nx == (e-1) and ny == (v-1)):
                print(z+1)
                exit()

            if (li[nx][ny]== '1') and not visited[nx][ny]:
                q.append((nx, ny, z+1))
                visited[nx][ny] = True
                
                
i,j = map(int, input().split())
li = []
for _ in range(i):
    s = input().strip()
    s = list(s)
    li.append(s)

visited = [[False] * len(li[0]) for _ in range(len(li))]

for i in range(len(li)):
    for j in range(len(li[0])):
        if (li[i][j]== '1') and not visited[i][j]:
                ans = bfs(i, j, li, visited)
