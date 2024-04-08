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

V = 40010
graph = [[] for _ in range(V+1)]
d = [0] * (V+1)

li = []
li1 = []
n, m = map(int, input().split())

for _ in range(n):
    a = int(input())
    li.append(a)

for _ in range(m):
    a = int(input())
    li1.append(a)

for i in range(len(li)):#tshirt
    for j in range(len(li1)):#kara
        if ((li1[j] >= li[i] * 0.5 and li1[j] <= li[i] * 0.75) or (li1[j] >= li[i] and li1[j] <= li[i] * 1.25)):
            graph[i+1].append(j+1)

#print(graph)

ans = 0
for i in range(1, n+1):
    c = [False] * (V+1)
    if dfs(i):
        ans += 1

print(ans)