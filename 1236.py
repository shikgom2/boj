n,m  = map(int, input().split())

li = []
for _ in range(n):
    s = input().strip()
    li.append(s)

x = [0] * m
y = [0] * n

for i in range(n):
    for j in range(m):
        if li[i][j] == 'X':
            x[j] += 1
            y[i] += 1

row = sum(1 for i in range(n) if y[i] == 0)
col = sum(1 for j in range(m) if x[j] == 0)

print(max(row, col))