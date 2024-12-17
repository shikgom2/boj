import sys
input = sys.stdin.readline
from collections import deque

A, B, C = map(int, input().split())

visited = [[False]*(B+1) for _ in range(A+1)]

can = set()

q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    a, b = q.popleft()
    c = C - a - b

    if a == 0:
        can.add(c)
    move = min(a, B - b)  
    na, nb = a - move, b + move
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # a -> c
    move = min(a, C - c)  
    na, nb = a - move, b
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # b -> a
    move = min(b, A - a)  
    na, nb = a + move, b - move
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # b -> c
    move = min(b, C - c)
    na, nb = a, b - move
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # c -> a
    move = min(c, A - a)
    na, nb = a + move, b
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # c -> b
    move = min(c, B - b)
    na, nb = a, b + move
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

ans = sorted(list(can))
print(' '.join(map(str, ans)))
