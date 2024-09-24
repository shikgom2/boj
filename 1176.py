import sys
input = sys.stdin.readline
sys.setrecursionlimit(155557)

def dfs(mask, last):
    if mask == (1 << n) - 1:
        return 1
    ret = 0
    for next_cow in graph[last]:
        bit = next_cow - 1
        if not (mask & (1 << bit)):
            ret += dfs(mask | (1 << bit), next_cow)
    return ret

n, m = map(int, input().split())
li = [0]

for _ in range(n):
    k = int(input())
    li.append(k)
    
graph = [[] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(1, n + 1):
            if i == 0:
                graph[i].append(j)
            else:
                if abs(li[i] - li[j]) > m:
                    graph[i].append(j)

print(dfs(0, 0))