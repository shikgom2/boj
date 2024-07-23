import sys
input = sys.stdin.readline
n, m = map(int, input().split())

li = []
for _ in range(n):
    s = list(map((int, input().split())))
    li.append(s)

prefix_sum = [[0] * (len(li) + 1) for _ in range(len(li) + 1) ]
for i in range(1, len(li) + 1):
    for j in range(1, len(li) + 1):
        prefix_sum[i][j] = li[i - 1][j - 1]  + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i -1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] + prefix_sum[x1 -1][y1 -1] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2])