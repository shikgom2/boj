import sys
input = sys.stdin.readline
from collections import deque
    
t = int(input())
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    if sx == ex and sy == ey:
        print(0)
        continue

    board = [[-1] * l for _ in range(l)]
    board[sx][sy] = 0
    
    q = deque()
    q.append((sx, sy))
    
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                if nx == ex and ny == ey:
                    print(board[nx][ny])
                    q.clear()
                    break
                q.append((nx, ny))
