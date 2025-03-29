import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split())
    grid = [[0] * W for _ in range(H)]
    for _ in range(O):
        x, y, L = map(int, input().split())
        grid[x - 1][y - 1] = L

    start = (Xs - 1, Ys - 1)
    dest = (Xe - 1, Ye - 1)

    dist = [[float('inf')] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0

    dq = deque()
    dq.append((start[0], start[1], 0))
    found = False

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while dq:
        x, y, moves = dq.popleft()
        if (x, y) == dest:
            found = True
            break
        if moves >= F:
            continue
        cur = grid[x][y]
        pow = F - moves
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                nei = grid[nx][ny]
                if nei > cur:
                    required = nei - cur
                    if pow < required:
                        continue
                new_moves = moves + 1
                if (nx, ny) != dest and new_moves >= F:
                    continue
                if new_moves < dist[nx][ny]:
                    dist[nx][ny] = new_moves
                    dq.append((nx, ny, new_moves))
    
    print("잘했어!!" if found else "인성 문제있어??")
