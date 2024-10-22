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
    
t = int(input())
for _ in range(t):
    n,m,p,q = map(int, input().split())
    graph = []
    parent = [i for i in range(n + 1)]
    
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph.append((a,b,c))
        
    graph.sort(key=lambda x:x[2])

    flag = False
    for i in range(len(graph)):
        x,y,z = graph[i][0], graph[i][1], graph[i][2]
        if find(x) != find(y):
            union(x, y)
            if(max(p,q) == max(x,y) and min(p,q) == min(x,y)):
                flag = True
                break
        
    if flag:
        print("YES")
    else:
        print("NO")
