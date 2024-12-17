import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for qqq in range(1, t+1):

    h, w, s, n = map(int, input().split())

    grid = [[False for _ in range(w)] for _ in range(h)]

    for _ in range(n):
        route = map(str, input().rstrip())
        
        r, c = h-1, 0
        grid[r][c] = True
        for move in route:
            if move == 'u':
                r -= 1
            elif move == 'd':
                r += 1
            elif move == 'l':
                c -= 1
            elif move == 'r':
                c += 1
            grid[r][c] = True

    visited = [[False for _ in range(w)] for _ in range(h)]
    ans = 0

    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    for r in range(h):
        for c in range(w):
            if not grid[r][c] and not visited[r][c]:
                queue = deque()
                queue.append((r,c))
                visited[r][c] = True
                size = 1
                while queue:
                    current_r, current_c = queue.popleft()
                    for dr, dc in dir:
                        nr, nc = current_r + dr, current_c + dc
                        if 0 <= nr < h and 0 <= nc < w:
                            if not grid[nr][nc] and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                                size += 1
                if size >= s:
                    ans += 1
    print(f"Data Set {qqq}:")
    print(ans)
    print()
