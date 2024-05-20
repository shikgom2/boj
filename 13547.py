import sys
input = sys.stdin.readline
from math import sqrt

mem = 100007

class Query:
    def __init__(self, l, r, k):
        self.l = l
        self.r = r
        self.k = k

    def __lt__(self, other):
        if self.l // sq == other.l // sq:
            return self.r > other.r
        return self.l // sq > other.l // sq

def add(g):
    global res, b
    b[g] += 1
    if b[g] == 1:
        res += 1

def sub(g):
    global res, b
    b[g] -= 1
    if b[g] == 0:
        res -= 1

n = int(input())
li = list(map(int, input().split()))
sq = int(sqrt(n))
m = int(input())
query = []

for _ in range(m):
    q1, q2 = map(int, input().split())
    query.append(Query(q1 - 1, q2 - 1, len(y)))

query.sort(reverse=True)

b = [0] * (mem * 11)
res = 0
s, e = 0, 0
add(li[0])
ans = [0] * m

for q in query:
    ns, ne = q.l, q.r
    for i in range(s, ns):
        sub(li[i])
    for i in range(s - 1, ns - 1, -1):
        add(li[i])
    for i in range(e + 1, ne + 1):
        add(li[i])
    for i in range(e, ne, -1):
        sub(li[i])
    s, e = ns, ne
    ans[q.k] = res

print(*ans, sep='\n')