import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.p = [-1] * n

    def gp(self, n):
        if self.p[n] < 0:
            return n
        self.p[n] = self.gp(self.p[n])
        return self.p[n]

    def merge(self, a, b, to_b=False):
        a = self.gp(a)
        b = self.gp(b)
        if a == b:
            return
        if not to_b and self.size(a) > self.size(b):
            a, b = b, a
        self.p[b] += self.p[a]
        self.p[a] = b

    def is_merged(self, a, b):
        return self.gp(a) == self.gp(b)

    def size(self, n):
        return -self.p[self.gp(n)]


n,m = map(int, input().split())

dsu = [DSU(m + 1) for _ in range(n)]

K = int(input())
stamps = []
for _ in range(K):
    H, W = map(int, input().split())
    s = [input().strip() for _ in range(H)]
    stamps.append((H, W, s))

ans = [['.'] * m for _ in range(n)]

Q = int(input())
queries = []
for _ in range(Q):
    t, y, x = map(int, input().split())
    queries.append((t - 1, y, x))

for i in range(Q - 1, -1, -1):
    t, start_y, start_x = queries[i]
    H, W, s = stamps[t]
    
    for y in range(start_y, start_y + H):
        l, r = start_x, start_x + W - 1
        x = l
        
        while x <= r:
            while dsu[y].gp(x) != x:
                x = dsu[y].gp(x)
            if x > r:
                break
            ans[y][x] = s[y - start_y][x - l]
            dsu[y].merge(x, x + 1, True)
            x = dsu[y].gp(x)

for row in ans:
    print(''.join(row))
