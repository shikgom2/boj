import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node):
    dp[node] = 1
    
    for next in graph[node] :
        if dp[next] == -1 :
            dp[node] += dfs(next)
    
    return dp[node]

n, r, q = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

dp = [-1 for _ in range(n+1)]

dfs(r)

sol = []
for _ in range(q) :
    k = int(input())
    print(dp[k])