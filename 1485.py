def solve(x, y):
    d = []
    for i in range(4):
        for j in range(i):
            d.append((x[i] - x[j])**2 + (y[i] - y[j])**2)
    d.sort()
    return d[0] == d[1] == d[2] == d[3] and d[3] * 2 == d[4] == d[5]

t = int(input())
for _ in range(t):
    x, y = [], []
    for i in range(4):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    print(1 if solve(x, y) else 0)