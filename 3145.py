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

m = [[] for _ in range(51)]

i, j = map(int, input().split())

for a in range(i):
    m[a] = list(map(str, input().strip()))


idx = 1
name = []
tmp = ""
for a in range(j):
    for b in range(i):
        if(m[b][a] != '.' and m[b][a] != 'x'):
            while(m[b][a] != '.'):
                tmp = str(tmp) + str(m[b][a])
                m[b][a] = str(idx)
                a+=1
                if(a == j-1):
                    name.append(tmp)
                    idx += 1
                    break
            idx += 1
print(name)
print(m)
''' 
ans = 0
for i in range(1, n+ 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)
'''