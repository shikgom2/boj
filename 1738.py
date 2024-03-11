import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(s):
    dist[s] = 0
    for i in range(v):
        for j in range(e):
            cur = edges[j][1]
            next_node = edges[j][2]
            cost = edges[j][0]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                predecessor[next_node] = cur
                if i == v - 1:
                    return True
    return False

def print_paths():
    destination = v 
    if dist[destination] == INF:
        return
    
    path = []
    while destination != -1:
        path.append(destination)
        destination = predecessor[destination]
    
    path = path[::-1]

    if path[0] != 1:
        print("123") 
    else:
        for p in path:
            print(p, end = " ")


v, e = map(int, input().split())
edges = []
dist = [INF] * (v + 1)
predecessor = [-1] * (v + 1)

for _ in range(e):
    x, y, z = map(int, input().split())
    edges.append((-z, x, y))

if bellman_ford(1):
    print("-1")
else:
    print_paths()