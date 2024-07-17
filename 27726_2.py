import sys
input = sys.stdin.readline
from collections import defaultdict
    
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1

def dsu(n, edges):
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a - 1, b - 1)
    return [uf.find(i) for i in range(n)]

def solve(n, edges1, edges2, edges3):
    comp1 = dsu(n, edges1)
    comp2 = dsu(n, edges2)
    comp3 = dsu(n, edges3)

    for i in range(len(comp1)):
        comp1[i] += 1

    for i in range(len(comp2)):
        comp2[i] += 1
        
    for i in range(len(comp3)):
        comp3[i] += 1

    li = defaultdict(list)
    for i in range(n):
        tuple_key = (comp1[i], comp2[i], comp3[i])
        li[tuple_key].append(i + 1)

    awesome = []
    for group in li.values():
        if len(group) > 1:
            s = sorted(group)
            awesome.append(s)

    awesome.sort(key=lambda x : x[0])
    return awesome

n = int(input())
m1, m2, m3 = map(int, input().split())

li1 = []
for _ in range(m1):
    a,b = map(int, input().split())
    li1.append((a,b))

li2 = []
for _ in range(m2):
    a,b = map(int, input().split())
    li2.append((a,b))

li3 = []
for _ in range(m1):
    a,b = map(int, input().split())
    li3.append((a,b))

ans = solve(n, li1, li2, li3)

print(len(ans))
for s in ans:
    print(" ".join(map(str, s)))
