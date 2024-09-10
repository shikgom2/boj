import sys
input = sys.stdin.readline 
from collections import deque
sys.setrecursionlimit(10**5*4)

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
		
		
    def update(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
		
	#get 0~i prefix sum
    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res
    
    #get l~r query    
    def query_range(self, l, r):
        return self.query(r) - self.query(l - 1)

def dfs(v):
    global idx
    left[v] = idx
    idx += 1
    for u in graph[v]:
        if left[u] == -1:
            depth[u] = depth[v] + 1
            dfs(u)
    right[v] = idx - 1

n, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

left = [-1] * (n + 1)
right = [-1] * (n + 1)
depth = [0] * (n + 1)
idx = 1

depth[c] = 1
dfs(c)

#print(left, right, depth)

q = int(input())
tree = BIT(n + 1)

for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        tree.update(left[b], 1)
    else:
        print(tree.query_range(left[b], right[b]) * depth[b])