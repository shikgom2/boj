import sys
input = sys.stdin.readline
import math

res = []
def dfs(x):
    for i in range(len(graph[x])):
        t = graph[x][i]
        if c[t]:
            continue
        c[t] = True
        if d[t] == 0 or dfs(d[t]):
            d[t] = x

            if(x == 1):
                res.append(t)
            return True
    return False

#Get prime
n = 2001
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

N = int(input())
li = list(map(int, input().split()))

V = 2002
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)
         
for i in range(len(li)):
    for j in range(len(li)):
        if(i==j):
            continue
        else:
            if(array[li[i] + li[j]] == True):
                graph[i+1].append(j+1)

#print(graph)
ans = 0
for i in range(1, n + 1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1
#print(ans)


if(ans != N):
    print(-1)
else:
    res = sorted(res, reverse=True)
    for r in res:
        print(li[r-1], end=" ")