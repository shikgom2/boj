import sys
input = sys.stdin.readline

n, m = map(int, input().split())

costs = [
    [10, 8, 7, 5, 1],
    [8, 6, 4, 3, 1],
    [7, 4, 3, 2, 1],
    [5, 3, 2, 2, 1],
    [1, 1, 1, 1, 0]
]

li = []
for _ in range(n):
    s = list(input().strip())
    for i in range(len(s)):
        if s[i] == 'F':
            s[i] = 'E'
    li.append(s)

size = n * m
max_size = size // 2

# Create cost matrix
cost_matrix = [[0]*max_size for _ in range(max_size)]
left_nodes = []
right_nodes = {}
idx_left = 0
idx_right = 0
node_idx = {}
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 1:
            node_idx[(i,j)] = idx_left
            idx_left += 1
        else:
            right_nodes[(i,j)] = idx_right
            idx_right += 1

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 1:
            u = node_idx[(i,j)]
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if (ni, nj) in right_nodes:
                        v = right_nodes[(ni, nj)]
                        a = ord(li[i][j]) - ord('A')
                        b = ord(li[ni][nj]) - ord('A')
                        cost = costs[a][b]
                        cost_matrix[u][v] = cost

# Apply the Hungarian Algorithm
def hungarian(matrix):
    n = len(matrix)
    m = len(matrix[0]) if matrix else 0
    u = [0]* (n + 1)
    v = [0]* (m + 1)
    p = [0]* (m + 1)
    way = [0]* (m + 1)
    for i in range(1, n +1):
        p[0] = i
        minv = [float('inf')] * (m +1)
        used = [False]* (m +1)
        j0 = 0
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float('inf')
            j1 = -1
            for j in range(1, m +1):
                if not used[j]:
                    cur = -matrix[i0 -1][j -1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(m +1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    ans = -v[0]
    return ans

max_cost = hungarian(cost_matrix)
print(max_cost * -1)
