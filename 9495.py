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

n = int(input())
li = []
for _ in range(n):
    k = list(map(str, input().rstrip()))
    li.append(k)

V = 2501
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
cnt = 0
check = []
for i in range(n):
    for j in range(n):
        if(li[i][j] == 'o'):
            check.append(i * n + j + 1)
            for k in range(4):
                ni = i + dir[k][0]
                nj = j + dir[k][1]
                if(ni == -1 or nj == -1 or ni == n or nj == n):
                    continue
                if(li[ni][nj] == '.'):
                    graph[i * n + j + 1].append(ni * n + nj + 1)
        elif(li[i][j] == 'x'):
            cnt += 1
#print(graph)
ans = 0
for i in check:
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(n*n - ans  - cnt)