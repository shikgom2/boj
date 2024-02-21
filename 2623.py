import sys
input = sys.stdin.readline

def dfs(node, graph, visited, recStack, stack):
    visited[node] = True
    recStack[node] = True

    for next in graph[node]:
        if not visited[next]:
            if dfs(next, graph, visited, recStack, stack):
                return True
        elif recStack[next]:
            return True

    stack.append(node)
    recStack[node] = False
    return False

N, M = map(int, input().split())

graph = {}

for i in range(0, N):
    graph[i] = []

for _ in range(0, M):
    i = list(map(int, input().split()))
    for j in range(1, len(i)-1): 
        a = i[j]
        b = i[j+1]
        graph[a-1].append(b-1)

visited = [False for _ in range(0, N)]
recStack = [False for _ in range(0, N)]

stack = []
cycle_detected = False
for i in range(0, N):
    if not visited[i]:
        if dfs(i, graph, visited, recStack, stack):
            cycle_detected = True
            break

if cycle_detected:
    print(0)
else:
    while stack:
        print(stack.pop() + 1)