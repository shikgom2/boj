import sys
input = sys.stdin.readline

def dfs(node, graph, visited, stack):
    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            dfs(next, graph, visited, stack)
    
    stack.append(node)



N, M = map(int, input().split())

graph = {}

# {1: [], 2: [], 3: [] ...}
for i in range(0, N):
    graph[i] = []

# {1: [2], 2: [4], 3: [5], 4: [] ...}
for _ in range(0, M):
    i = list(map(int, input().split()))
    
    for j in range(1, len(i)-1): 
        a = i[j]
        b = i[j+1]
        graph[a-1].append(b-1)

# {False, False, ... N개만큼} 
visited = [False for _ in range(0, N)]

stack = []
print(graph)
for i in range(0, N):
    if not visited[i]:
        dfs(i, graph, visited, stack)

print(stack)
while stack:
    print(stack.pop() + 1)