import sys
input = sys.stdin.readline
import math


def get(x):
    if x == fa[x]:
        return x
    fa[x] = get(fa[x])
    return fa[x]

def merge(x, y):
    a = get(x)
    b = get(y)
    if a != b:
        L[b] = L[a] = min(L[a], L[b])
        R[b] = R[a] = max(R[a], R[b])
        U[b] = U[a] = max(U[a], U[b])
        D[b] = D[a] = min(D[a], D[b])
        fa[b] = a

class Pos:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.up = y + r
        self.down = y - r
        self.L = x - r
        self.R = x + r

# Initialize arrays
fa = list(range(1001))
L = [0] * 1001
R = [0] * 1001
U = [0] * 1001
D = [0] * 1001

n,m,k = map(int, input().split())

flag = 1
a = []

for i in range(1, k + 1):
    x, y, r = map(float, input().split())
    pos = Pos(x, y, r)
    a.append(pos)
    
    if x * x + y * y <= r * r or (x - n) ** 2 + (y - m) ** 2 <= r * r:
        flag = 0

    fa[i] = i
    L[i] = pos.L
    R[i] = pos.R
    U[i] = pos.up
    D[i] = pos.down

if not flag:
    print("N")
else:
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if i != j and math.sqrt((a[i - 1].x - a[j - 1].x) ** 2 + (a[i - 1].y - a[j - 1].y) ** 2) <= a[i - 1].r + a[j - 1].r:
                merge(i, j)

    for i in range(1, k + 1):
        root = get(i)
        if (L[root] < 1 and R[root] > n - 1) or (D[root] < 1 and U[root] > m - 1) or (R[root] > n - 1 and U[root] > m - 1) or (L[root] < 1 and D[root] < 1):
            flag = 0

    if not flag:
        print("N")
    else:
        print("S")

