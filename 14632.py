import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [['.' for _ in range(m)] for _ in range(n)]

k = int(input())
cnt = []

for _ in range(k):
    h, w = map(int, input().split())
    stamp = [input().strip() for _ in range(h)]
    pos = []
    for i in range(h):
        for j in range(w):
            if stamp[i][j] != '.':
                pos.append((i, j, stamp[i][j]))
    cnt.append(pos)

q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

visited = [[False]*m for _ in range(n)]

for c, x, y in reversed(queries):
    pos = cnt[c - 1]
    for i, j, ch in pos:
        gx, gy = x + i, y + j
        if 0 <= gx < n and 0 <= gy < m and not visited[gx][gy]:
            graph[gx][gy] = ch
            visited[gx][gy] = True

for row in graph:
    print(''.join(row))
