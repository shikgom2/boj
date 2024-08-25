import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self):
        self.SZ = 1 << 17
        self.st = [self.Node() for _ in range(2 * self.SZ)]
        self.lazy = [0] * (2 * self.SZ)

    class Node:
        def __init__(self, mini=0, maxi=0):
            self.mini = mini
            self.maxi = maxi

    def op(self, a, b):
        return self.Node(min(a.mini, b.mini), max(a.maxi, b.maxi))

    def pass_lazy(self, u):
        if u < self.SZ:
            self.lazy[2 * u] += self.lazy[u]
            self.lazy[2 * u + 1] += self.lazy[u]
        self.st[u].mini += self.lazy[u]
        self.st[u].maxi += self.lazy[u]
        self.lazy[u] = 0

    def update(self, s, e, v, l=0, r=None, u=1):
        if r is None:
            r = self.SZ

        self.pass_lazy(u)
        if e <= l or r <= s:
            return
        if s <= l and r <= e:
            self.lazy[u] = v
            self.pass_lazy(u)
            return
        m = (l + r) // 2
        self.update(s, e, v, l, m, 2 * u)
        self.update(s, e, v, m, r, 2 * u + 1)
        self.st[u] = self.op(self.st[2 * u], self.st[2 * u + 1])


segment_tree = SegmentTree()

q = int(input())
for _ in range(q):
    p, x = map(int, input().split())
    segment_tree.update(0, p, -2 * x + 3)
    
    if segment_tree.st[1].maxi <= 0:
        print("<")
    elif segment_tree.st[1].mini >= 0:
        print(">")
    else:
        print("?")