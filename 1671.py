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

V = 51
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)


n = int(input())
li = []
for idx in range(1, n+1):
    i,j,k = map(int, input().split())
    li.append((i,j,k,idx))

for i in range(len(li)):
    for j in range(len(li)):
        if(i != j and li[i][0] == li[j][0] and li[i][1] == li[j][1] and li[i][2] == li[j][2]):
            if(li[i][3] > li[j][3]):
                graph[i+1].append(j+1)
        elif(i != j and li[i][0] >= li[j][0] and li[i][1] >= li[j][1] and li[i][2] >= li[j][2]):
            graph[i+1].append(j+1)

ans = 0
#print(graph)
for _ in range(2):
    for i in range(1, n + 1):
        c = [False] * (V+1)
        if dfs(i):
            ans += 1
print(n - ans)