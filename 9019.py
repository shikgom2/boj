import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    q = deque([s])
    visit = [False] * 10001
    parent = [None] * 10001
    op = [''] * 10001

    visit[s] = True
    while q:
        dx = q.popleft()
        if dx == e:
            break

        # D operation
        tmp = (dx * 2) % 10000
        if not visit[tmp]:
            visit[tmp] = True
            parent[tmp] = dx
            op[tmp] = 'D'
            q.append(tmp)

        # S operation
        tmp = (dx - 1) % 10000
        if not visit[tmp]:
            visit[tmp] = True
            parent[tmp] = dx
            op[tmp] = 'S'
            q.append(tmp)

        # L operation
        tmp = (dx % 1000) * 10 + dx // 1000 
        if not visit[tmp]:
            visit[tmp] = True
            parent[tmp] = dx
            op[tmp] = 'L'
            q.append(tmp)

        # R operation
        tmp = (dx % 10) * 1000 + dx // 10 
        if not visit[tmp]:
            visit[tmp] = True
            parent[tmp] = dx
            op[tmp] = 'R'
            q.append(tmp)

    result = ''
    current = e
    while current != s:
        result = op[current] + result
        current = parent[current]
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = bfs(n, m)
    print(ans)
