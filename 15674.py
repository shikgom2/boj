import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(h):
    if h == -1 or par[h] == h:
        return h
    par[h] = find(par[h])
    return par[h]

def mincost(x):
    x = find(x)
    ex = find(enemy[x])
    l = a[x]
    r = b[x]
    if ex != -1:
        l += b[ex]
        r += a[ex]
    return min(l, r)

def merge(x, y):
    par[x] = y
    a[y] += a[x]
    b[y] += b[x]

def make_friend(x, y):
    global res
    x = find(x)
    y = find(y)
    if x == y:
        return
    ex = find(enemy[x])
    ey = find(enemy[y])
    res -= mincost(x) + mincost(y)
    merge(x, y)
    if ex > ey:
        ex, ey = ey, ex
    if ex != -1:
        merge(ex, ey)
    if ey != -1:
        enemy[ey] = y
    enemy[y] = ey
    res += mincost(x)

def make_enemy(x, y):
    global res
    x = find(x)
    y = find(y)
    ex = find(enemy[x])
    ey = find(enemy[y])
    if x == ey or y == ex:
        return
    res -= mincost(x) + mincost(y)
    if ex != -1:
        merge(ex, y)
    if ey != -1:
        merge(ey, x)
    enemy[x] = y
    enemy[y] = x
    res += mincost(x)

n, d = map(int, sys.stdin.readline().split())
a = [0] * (n + 1)
b = [0] * (n + 1)
par = list(range(n + 1))
enemy = [-1] * (n + 1)
aa = [0] * (n + 1)
bb = [0] * (n + 1)
res = 0

for i in range(1, n + 1):
    a[i], b[i] = map(int, sys.stdin.readline().split())
    aa[i] = a[i]
    bb[i] = b[i]
    res += mincost(i)

for _ in range(d):
    x, y, z = map(int, input().split())
    if x:
        make_enemy(y, z)
    else:
        make_friend(y, z)

print(res)
q = int(input())
for _ in range(q):
    x, y, z = map(int, input().split())
    if x == 0:
        make_friend(y, z)
    elif x == 1:
        make_enemy(y, z)
    elif x == 2:
        res -= mincost(y)
        curr = find(y)
        a[curr] += -aa[y] + z
        aa[y] = z
        res += mincost(y)
    else:
        res -= mincost(y)
        curr = find(y)
        b[curr] += -bb[y] + z
        bb[y] = z
        res += mincost(y)
    print(res)