class Input:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.a = []
        self.b = []

    def read(self):
        try:
            self.n, self.m = map(int, input().split())
            for _ in range(self.n):
                c, t, x = input().split()
                t = int(t)
                x = int(x) * (1 if c == '+' else -1)
                self.a.append((t, x))
            self.b = list(map(int, input().split())) 
            return True
        except EOFError:
            return False

def solve(n, m, a, b):
    c = [(b[i], i) for i in range(m)]
    sum_values = 0
    t = []

    for i in range(n):
        sum_values += a[i][1]
        t.append((a[i][0], sum_values))

    c.sort(reverse=True) 
    ans = [0] * m
    w = [(0, 0)] * m 

    for i in range(n - 1):
        left, right = -1, m
        while left + 1 < right:
            middle = (left + right) // 2
            if t[i][1] + c[middle][0] < 0:
                right = middle
            else:
                left = middle

        if right < m:
            dt = t[i + 1][0] - t[i][0]
            w[right] = (w[right][0] - (t[i][1] + c[right][0]) * dt, w[right][1] + dt)

    for i in range(m):
        if i > 0:
            w[i] = (w[i][0] + (c[i - 1][0] - c[i][0]) * w[i - 1][1] + w[i - 1][0], w[i][1] + w[i - 1][1])

        ans[c[i][1]] = -1 if -sum_values > c[i][0] else w[i][0]

    return ans

inp = Input()
if inp.read():
    result = solve(inp.n, inp.m, inp.a, inp.b)
    for res in result:
        if res < 0:
            print("INFINITY")
        else:
            print(res)
