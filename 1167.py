import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [-1] * (N+1)
    queue = deque([start])
    visited[start] = 0
    max_dist = [0,0]

    while queue:
        node = queue.popleft()

        for adj, weight in graph[node]:
            if visited[adj] == -1:
                visited[adj] = visited[node] + weight
                queue.append(adj)
                if visited[adj] > max_dist[1]:
                    max_dist = adj, visited[adj]    
    
    return max_dist

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    data = list(map(int, input().split()))
    for i in range(1, len(data) - 2 , 2):
        graph[data[0]].append([data[i], data[i+1]])

node, dist = bfs(1)
result = bfs(node)
print(result[1])