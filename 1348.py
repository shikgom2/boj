import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

def dfs(x):
    for i in range(len(graph[x])):
        t, dist = graph[x][i]
        if visited[t]:
            continue
        visited[t] = True
        if q[t] == -1 or dfs(q[t]):
            q[t] = x
            return True
    return False

def bfs(x):
    ch = [[-1 for _ in range(c)] for _ in range(r)]
    ch[car_list[x][0]][car_list[x][1]] = 0
    queue = deque([[car_list[x][0], car_list[x][1], 0]])
    
    while queue:
        y = queue.popleft()
        for i in range(4):
            nx = y[1] + dx[i]
            ny = y[0] + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if maps[ny][nx] == 'X':
                continue
            if ch[ny][nx] != -1:
                continue
            ch[ny][nx] = y[2] + 1
            queue.append([ny, nx, y[2] + 1])
    
    for i in range(len(park_list)):
        distances[x].append(ch[park_list[i][0]][park_list[i][1]])

def inp(limit):
    graph = [[] for _ in range(car_count + 1)]
    for i in range(car_count):
        for j in range(len(distances[i])):
            if distances[i][j] != -1 and distances[i][j] <= limit:
                graph[i + 1].append((j + 1, distances[i][j]))
    return graph

def pr(graph):
    global visited, q
    q = [-1] * (len(park_list) + 1)
    cnt = 0
    for i in range(car_count):
        visited = [False] * (len(park_list) + 1)
        if dfs(i + 1):
            cnt += 1
    return cnt == car_count

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
car_list = []
park_list = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
distances = [[] for _ in range(10001)]

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'C':
            car_list.append([i, j])
        elif maps[i][j] == 'P':
            park_list.append([i, j])

car_count = len(car_list)
park_count = len(park_list)

if car_count == 0:
    print(0)
    exit()
if car_count > park_count:
    print(-1)
    exit()

for i in range(car_count):
    bfs(i)

left = 0
right = 3000
ans = -1

while left <= right:
    mid = (left + right) // 2
    graph = inp(mid)
    if pr(graph):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)