import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

size = len(matrix)
prefix_sum = [[0] * (size + 1) for _ in range(size + 1) ]
for i in range(1, size + 1):
    for j in range(1, size + 1):
        prefix_sum[i][j] = matrix[i - 1][j - 1]  + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i -1][j - 1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2]  + prefix_sum[x1 -1][y1 -1] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2])
