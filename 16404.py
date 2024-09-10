import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5*2)

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

n,m = map(int, input().split())
li = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(1, n):
    graph[li[i]].append(i+1)

idx = 0
euler = [(0, 0)] * (n + 1)
dfs(1, 0)

tree = BIT(n+1)

for _ in range(m):
    li = list(map(int, input().split()))
    if(li[0] == 1):
        idx = li[1]
        tree.update(euler[idx][0], li[2])
        tree.update(euler[idx][1] + 1, -li[2])
    else:
        idx = li[1]
        print(tree.query(euler[idx][0]))