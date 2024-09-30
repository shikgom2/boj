import sys

def hungarian(matrix, n, m):
    u = [0] * (n + 1)
    v = [0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)
    
    for i in range(1, n + 1):
        p[0] = i
        minv = [float('inf')] * (m + 1)
        used = [False] * (m + 1)
        j0 = 0
        i0 = i
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = float('inf')
            j1 = 0
            for j in range(1, m + 1):
                if not used[j]:
                    cur = matrix[i0-1][j-1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(0, m + 1):
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
    
    # Total cost
    cost = -v[0]
    # Matching
    matching = [0] * n
    for j in range(1, m + 1):
        if p[j] != 0:
            matching[p[j]-1] = j-1
    return cost, matching

def main():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    # Read the grid and replace 'F' with 'E'
    grid = []
    for _ in range(n):
        row = list(sys.stdin.readline().strip())
        row = ['E' if c == 'F' else c for c in row]
        grid.append(row)
    
    # Define the costs
    costs = [
        [10, 8, 7, 5, 1],
        [8, 6, 4, 3, 1],
        [7, 4, 3, 2, 1],
        [5, 3, 2, 2, 1],
        [1, 1, 1, 1, 0]
    ]
    
    # Identify workers and jobs based on (i + j) % 2
    workers = []
    jobs = []
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 1:
                workers.append((i, j))
            else:
                jobs.append((i, j))
    
    num_workers = len(workers)
    num_jobs = len(jobs)
    
    # Initialize the cost matrix with high values
    size = max(num_workers, num_jobs)
    cost_matrix = [[1000] * size for _ in range(size)]
    
    for w in range(num_workers):
        i, j = workers[w]
        for d in range(4):
            ni = i + [-1, 0, 1, 0][d]
            nj = j + [0, 1, 0, -1][d]
            if 0 <= ni < n and 0 <= nj < m:
                try:
                    j_idx = jobs.index((ni, nj))
                    a = ord(grid[i][j]) - ord('A')
                    b = ord(grid[ni][nj]) - ord('A')
                    cost_matrix[w][j_idx] = -costs[a][b]  # Negative for minimization
                except ValueError:
                    continue
    
    # Pad the cost matrix if necessary
    for row in cost_matrix:
        while len(row) < size:
            row.append(1000)
    while len(cost_matrix) < size:
        cost_matrix.append([1000] * size)
    
    min_cost, matching = hungarian(cost_matrix, size, size)
    
    print(-min_cost)

if __name__ == "__main__":
    main()
