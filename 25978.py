def f(n, cnt, sum_matrix):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cnt[i][j] += cnt[i - 1][j] + cnt[i][j - 1] - cnt[i - 1][j - 1]
            sum_matrix[i][j] += sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + cnt[i][j]

n, m = map(int, input().split())

sum_matrix = [[0] * (n + 1) for _ in range(n + 1)]
cnt = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        sum_matrix[i][j] = row[j - 1]

flag = 0

for _ in range(m):
    inputs = list(map(int, input().split()))
    o = inputs[0]
    y1 = inputs[1] + 1
    x1 = inputs[2] + 1
    y2 = inputs[3] + 1
    x2 = inputs[4] + 1
    
    if o & 1:
        k = inputs[5]
        cnt[y1][x1] += k
        if y2 + 1 <= n and x2 + 1 <= n:
            cnt[y2 + 1][x2 + 1] += k
        if x2 + 1 <= n:
            cnt[y1][x2 + 1] -= k
        if y2 + 1 <= n:
            cnt[y2 + 1][x1] -= k
    else:
        if not flag:
            flag = 1
            f(n, cnt, sum_matrix)
        ans = sum_matrix[y2][x2] - sum_matrix[y2][x1 - 1] - sum_matrix[y1 - 1][x2] + sum_matrix[y1 - 1][x1 - 1]
        print(ans)
