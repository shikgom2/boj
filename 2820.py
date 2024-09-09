import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

def dfs(v, p):
    global idx, euler
    idx += 1
    euler[v] = (idx, euler[v][1])

    for nv in graph[v]:
        if nv != p:
            dfs(nv, v)

    euler[v] = (euler[v][0], idx)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
money = [0] * (n + 1)
euler = [(0, 0)] * (n + 1)

money[1] = int(input())
for i in range(2, n + 1):
    a,b = map(int, input().split())
    money[i] = a
    graph[b].append(i)

idx = 0
dfs(1, 0)
tree = BIT(n)

for i in range(1, n + 1):
    tree.update(euler[i][0], money[i])
    tree.update(euler[i][0] + 1, -money[i])

output = []
while m > 0:
    m -= 1
    parts = input().split()
    c = parts[0]
    if c == 'p':
        a = int(parts[1])
        x = int(parts[2])
        tree.update(euler[a][0] + 1, x)
        tree.update(euler[a][1] + 1, -x)
    else:
        a = int(parts[1])
        print(tree.query(euler[a][0]))