import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

n = int(input())

graph = []
parent = [i for i in range(n + 1)]
ans = 0
check = []
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        if(li[j] > 0):
            graph.append((max(i,j), min(i,j), li[j])) #build
        
        #if already built, union and add weight
        mi = max(i,j)
        mj = min(i,j)
        if(li[j] < 0 and (mi,mj) not in check):
            union(mi,mj)
            ans += (li[j] * - 1)
            check.append((mi, mj))

graph = set(graph)
graph = list(graph)
graph.sort(key=lambda x:x[2])
cnt = 0
check = []

for i in range(len(graph)):
    x = graph[i][0]
    y = graph[i][1]
    z = graph[i][2]
    if find(x) != find(y):
        union(x, y)
        ans = ans + z
        check.append((x,y))
        cnt += 1
    
print(ans, cnt)
for i in range(len(check)):
    print(min(check[i][0]+1, check[i][1]+1), max(check[i][0]+1, check[i][1]+1))