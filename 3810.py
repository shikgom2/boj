import sys
input = sys.stdin.readline
from collections import deque

class HopcroftKarp:
    def __init__(self, left_size, right_size):
        self.left_size = left_size
        self.right_size = right_size
        self.graph = [[] for _ in range(left_size + 1)]
        self.pair_left = [0] * (left_size + 1)
        self.pair_right = [0] * (right_size + 1)
        self.dist = [0] * (left_size + 1)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self):
        queue = deque()
        for u in range(1, self.left_size + 1):
            if self.pair_left[u] == 0:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        self.dist[0] = float('inf')

        while queue:
            u = queue.popleft()
            if u != 0:
                for v in self.graph[u]:
                    if self.dist[self.pair_right[v]] == float('inf'):
                        self.dist[self.pair_right[v]] = self.dist[u] + 1
                        queue.append(self.pair_right[v])

        return self.dist[0] != float('inf')

    def dfs(self, u):
        if u != 0:
            for v in self.graph[u]:
                if self.dist[self.pair_right[v]] == self.dist[u] + 1:
                    if self.dfs(self.pair_right[v]):
                        self.pair_left[u] = v
                        self.pair_right[v] = u
                        return True
            self.dist[u] = float('inf')
            return False
        return True

    def max_matching(self):
        matching = 0
        while self.bfs():
            for u in range(1, self.left_size + 1):
                if self.pair_left[u] == 0:
                    if self.dfs(u):
                        matching += 1
        return matching


t = int(input())
for _ in range(t):
    while True:
        line = input()
        if line.strip() == '':
            continue
        else:
            break

    if line.strip() == '':
        continue

    YX = line.strip().split()
    Y = int(YX[0])
    X = int(YX[1])

    # Initialize grid
    grid = [['.' for _ in range(X + 1)] for _ in range(Y + 1)]  # 1-based indexing

    P_line = input()
    while P_line.strip() == '':
        P_line = input()
    P = int(P_line.strip())

    points = []
    for _ in range(P):
        point_line = input().strip()
        while point_line == '':
            point_line = input().strip()
        py, px = map(int, point_line.split())
        points.append((py, px))

    W_line = input()
    while W_line.strip() == '':
        W_line = input()
    W = int(W_line.strip())

    for _ in range(W):
        obstacle_line = input().strip()
        while obstacle_line == '':
            obstacle_line = input().strip()
        wy, wx = map(int, obstacle_line.split())
        grid[wy][wx] = '#'  # Mark obstacle

    h = [[0 for _ in range(X + 1)] for _ in range(Y + 1)]
    h_id = 0
    for y in range(1, Y + 1):
        current_h = None
        for x in range(1, X + 1):
            if grid[y][x] == '#':
                current_h = None
            else:
                if current_h is None:
                    h_id += 1
                    current_h = h_id
                h[y][x] = current_h

    v = [[0 for _ in range(X + 1)] for _ in range(Y + 1)]
    v_id = 0
    for x in range(1, X + 1):
        current_v = None
        for y in range(1, Y + 1):
            if grid[y][x] == '#':
                current_v = None
            else:
                if current_v is None:
                    v_id += 1
                    current_v = v_id
                v[y][x] = current_v

    hk = HopcroftKarp(h_id, v_id)
    for (py, px) in points:
        h_seg = h[py][px]
        v_seg = v[py][px]
        if h_seg == 0 or v_seg == 0:
            continue
        hk.add_edge(h_seg, v_seg)

    ans = hk.max_matching()
    print(ans)
