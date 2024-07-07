import sys
input = sys.stdin.readline
import heapq

def deijkstra(start):
    dist = [INF for _ in range(n+1)]
    dist[start]=0
    heap = []
    heapq.heappush(heap, [0,start])
    while heap:
        weight,node = heapq.heappop(heap)
        
        if dist[node] < weight:
            continue
        
        for next, cost in graph[node]:
            if dist[next]>weight+cost:
                dist[next] = weight + cost
                heapq.heappush(heap,[dist[next],next])
    
    return dist

INF = 10**10
t = int(input())
for _ in range(t):
    n,m,k = map(int, input().split())
    s,g,h = map(int, input().split())
    
    graph = [[]for _ in range(n+1)]
    
    for _ in range(m):
        u,v,w = map(int, input().split())
        if (u==g and v==h) or (u==h and v==g):
            gToh = w
        graph[u].append([v,w])
        graph[v].append([u,w])
        
    res = {}
    for _ in range(k):
        res[int(input())]=1

    lis = deijkstra(s)
    lig = deijkstra(g)
    lih = deijkstra(h)

    ans = []
    for i in res:
        if ( lis[g] + gToh + lih[i] == lis[i] ) or ( lis[h] + gToh+ lig[i] == lis[i] ):
            ans.append(i)
                
    ans.sort()
    print(*ans)