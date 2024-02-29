def bfs():
    queue = [1]
    parents = [0 for _ in range(len(tree))]
    while len(queue) > 0:
        parent = queue.pop()
        for v in tree[parent]:
            if not visited[v]:
                parents[v] = parent
                queue.append(v)
                visited[v] = True
    return parents

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for i in range(N-1):
    u, v = list(map(int, input().split()))
    tree[u].append(v)
    tree[v].append(u)
parents = bfs()
for i in range(2, N+1):
    print(parents[i])