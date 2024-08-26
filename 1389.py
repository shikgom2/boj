import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] * (n+1)]

for _ in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)