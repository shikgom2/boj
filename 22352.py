import sys
input = sys.stdin.readline

def dfs(i, j, id):
    visited[i][j] = id
    val = graph[i][j]
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        x, y = i+dx, j+dy
        if 0<=x<n and 0<=y<m and visited[x][y]==-1 and graph[x][y]==val:
            dfs(x, y, id)

n,m = map(int, input().split())
graph = []

for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

check = []
for _ in range(n):
    li = list(map(int ,input().split()))
    check.append(li)

visited = [[-1]*m for _ in range(n)]
id = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            dfs(i,j,id)
            id +=1

for a in range(id):
    tmp = None
    can = True
    for i in range(n):
        for j in range(m):
            if(visited[i][j] == a):
                if tmp is None:
                    tmp = check[i][j]
                elif check[i][j] !=tmp:
                    can = False
                    break
    if not can:
        continue

    can = True
    for i in range(n):
        for j in range(m):
            if(visited[i][j] != a):
                if(check[i][j] != graph[i][j]):
                    can=False
                    break
        if not can:
            break

    if can:
        print("YES")
        exit()
print("NO")