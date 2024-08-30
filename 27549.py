import sys
input = sys.stdin.readline
from collections import defaultdict

MOD = 10**9 + 7
pr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

class Mat:
    def __init__(self, n):
        self.n = n
        self.m = [[0] * n for _ in range(n)]
    
    def pov(self):
        for i in range(self.n):
            self.m[i].append(0)
        self.m.append([0] * (self.n + 1))
        self.n += 1

    def __mul__(self, other):
        ret = Mat(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    ret.m[i][j] = add(ret.m[i][j], mult(self.m[i][k], other.m[k][j]))
        return ret

    def pot(self, a):
        ret = Mat(self.n)
        for i in range(self.n):
            ret.m[i][i] = 1
        tr = self
        while a:
            if a & 1:
                ret = ret * tr
            tr = tr * tr
            a >>= 1
        return ret

def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    if a < 0:
        a += MOD
    return a

def mult(a, b):
    return (a * b) % MOD

def pot(a, b):
    ret = 1
    while b:
        if b & 1:
            ret = mult(ret, a)
        a = mult(a, a)
        b >>= 1
    return ret

def dij(a, b):
    return mult(a, pot(b, MOD - 2))

n, ind = 0, 1
saz = {}
kom = []

def rek(zad, ost, op):
    global ind
    if not ost:
        trh = 1
        m = len(kom)
        for i in range(m):
            trh *= pr[kom[i]]
        if trh not in saz:
            saz[trh] = ind
            ind += 1
            op.pov()
        for i in range(m):
            for j in range(m):
                noh = trh
                if i != j:
                    noh //= pr[kom[i]] * pr[kom[j]]
                    noh *= pr[kom[i] - 1] * pr[kom[j] + 1]
                if noh not in saz:
                    saz[noh] = ind
                    ind += 1
                    op.pov()
                op.m[saz[noh] - 1][saz[trh] - 1] = add(op.m[saz[noh] - 1][saz[trh] - 1], dij(mult(kom[i], kom[j]), mult(n, n)))
        return
    
    for i in range(zad, ost // 2 + 1):
        kom.append(i)
        rek(i, ost - i, op)
        kom.pop()
    
    kom.append(ost)
    rek(ost, 0, op)
    kom.pop()

m = 0
t = 0
n, t, m = map(int, input().split())
op = Mat(0)
rek(1, n, op)
op = op.pot(t)
ans = 0
for p, index in saz.items():
    tr = 0
    for i in range(1, n + 1):
        while p % pr[i] == 0:
            p //= pr[i]
            tr += 1
    if tr >= m:
        ans = add(ans, op.m[index - 1][saz[1 << n] - 1])

print(ans)
