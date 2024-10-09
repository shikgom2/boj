import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    global ans
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            if(weight[x] <= weight[node]):
                ans += (weight[node] - weight[x])
            dfs(node)
            
    
n = int(input())
#앞에 0을 추가하는 이유는 정점 인덱스 매칭시키기 편하기 위해서
weight = [0] + list(map(int, input().split())) 

graph = [[] for _ in range (n+1)]
for _ in range(n-1): #add graph
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)
ans = 0
dfs(1)
print(ans + weight[1])

