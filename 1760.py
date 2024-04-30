import sys
input = sys.stdin.readline

def dfs(x):
    for i in range(len(graph[x])):
        t = graph[x][i]
        if c[t]:
            continue
        c[t] = True
        if d[t] == 0 or dfs(d[t]):
            d[t] = x
            return True
    return False

V = 101
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 행 영역 별로 번호를 매긴다.
raw = [[0] * m for _ in range(n)]; ri = 0
is_open = False # 행이나 열이 이어지고 있는지 판별
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            if is_open:
                is_open = False
                ri += 1
        else:
            if not is_open:
                is_open = True
            raw[i][j] = ri
    if is_open:
        is_open = False
        ri += 1
#print(raw)

# 열 영역 별로 번호를 매긴다.
col = [[0] * m for _ in range(n)]; ci = 0
for j in range(m):
    for i in range(n):
        if matrix[i][j] == 2:
            if is_open:
                is_open = False
                ci += 1
        else:
            if not is_open:
                is_open = True
            col[i][j] = ci
    if is_open:
        is_open = False
        ci += 1

#print(col)

# 각 격자마다 빈 격자라면 행 영역에서 열 영역으로 이어지는 간선을 그래프에 추가
graph = [[] for _ in range(V+1)]
for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            graph[raw[i][j]+1].append(col[i][j]+1)

#print(graph)

ans = 0
for i in range(1, V + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)