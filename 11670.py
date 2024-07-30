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

V = 10000
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

n = int(input())
tmp = []
li = []
for i in range(n):
    a,b = map(int, input().split())
    #coordicate compression
    tmp.append((a,b))
    li.append(a*b)
    li.append(a-b)
    li.append(a+b)

li = set(li)
li = list(li)
li.sort()

for i in range(n):
    idx1 = li.index(tmp[i][0] + tmp[i][1])
    idx2 = li.index(tmp[i][0] - tmp[i][1])
    idx3 = li.index(tmp[i][0] * tmp[i][1])
    graph[i+1].append(idx1+1)
    graph[i+1].append(idx2+1)
    graph[i+1].append(idx3+1)

ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

if(ans != n):
    print("impossible")
else:
    ans=["" for i in range(n)]
    #tracking
    for i in range(n*3):
        if d[i+1]!=0:
            r=tmp[d[i+1]-1]
            if r[0]+r[1]==li[i]:
                ans[d[i+1]-1] = str(r[0])+" + "+str(r[1])+" = "+str(li[i])
            elif r[0]-r[1]==li[i]:
                ans[d[i+1]-1] = str(r[0])+" - "+str(r[1])+" = "+str(li[i])
            else:
                ans[d[i+1]-1] = str(r[0])+" * "+str(r[1])+" = "+str(li[i])

    for i in range(n):
        print(ans[i])