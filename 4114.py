import sys
input = sys.stdin.readline
import collections import deque

def solve():    
    while True:
        N, K = map(int, input().split())
        if N == 0 and K == 0:
            return
        
        troops = [0]*N
        adj = [[] for _ in range(N)]
        
        for i in range(N):
            li = list(map(int, input().split()))
            troops[i] = T
            for i in li:
                adj[i].append(i)
        
        sumTroops = [0]*N
        for v in range(N):
            s = troops[v]
            for i in adj[v]:
                s += troops[i]
            sumTroops[v] = s
        
        inHeart = [True]*N
        queue = deque()
        
        for v in range(N):
            if sumTroops[v] < K:
                queue.append(v)
        
        while queue:
            v = queue.popleft()
            if inHeart[v]:
                inHeart[v] = False
                for i in adj[v]:
                    if inHeart[i]:
                        sumTroops[i] -= troops[v]
                        if sumTroops[i] < K:
                            queue.append(i)
        
        h = [v for v in range(N) if inHeart[v]]
        size = len(h)
        ans = sum(troops[v] for v in h)
        
        print(size, ans)

solve()