import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a

n,m = map(int, input().split())
graph = []

for _ in range(n):
    s = list(map(str, input().rstrip()))
    graph.append(s)

#dfs brute force -> 1000 * 1000 * 1000 n^3 TLE.
#n^2 dsu + check n

parent = [i for i in range(n*m)]

for i in range(n):
    for j in range(m):
        #think 2-dim graph to 1-dim
        idx = i * m + j
        if(graph[i][j] == 'D'):
            union(idx, idx + m)
        elif(graph[i][j] == 'U'):
            union(idx, idx - m)
        elif(graph[i][j] == 'R'):
            union(idx, idx + 1)
        elif(graph[i][j] == 'L'):
            union(idx, idx - 1)

li = []
for i in range(n*m):
    li.append(find(i))

#print(li)
li = set(li)
print(len(li))