from collections import deque

def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False]*M for _ in range(N)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    def bfs(start_i, start_j):
        queue = deque()
        queue.append((start_i, start_j))
        visited[start_i][start_j] = True

        current_height = grid[start_i][start_j]
        is_peak = True

        connected_cells = [(start_i, start_j)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] > current_height:
                        is_peak = False
                    if not visited[nr][nc] and grid[nr][nc] == current_height:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        connected_cells.append((nr, nc))

        return is_peak

    peak_count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if bfs(i, j):
                    peak_count += 1

    print(peak_count)
solve()