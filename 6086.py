from collections import deque

def bfs(rGraph, s, t, parent):
    visited = [False] * len(rGraph)
    queue = deque()
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        
        for ind, val in enumerate(rGraph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                
    return visited[t]

def edmondsKarp(graph, source, sink):
    rGraph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs(rGraph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        
        while(s != source):
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        v = sink
        
        while(v != source):
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]
            
    return max_flow

# Example usage
graph = [[0, 3, 0, 0, 0],
         [0, 0, 3, 0, 6],
         [0, 0, 0, 5, 0],
         [0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0]]
source = 0
sink = 4

print(edmondsKarp(graph, source, sink))