import sys
input = sys.stdin.readline
from math import sqrt

mem = 100007

class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

    def __lt__(self, other):
        if self.l // sq == other.l // sq:
            return self.r < other.r if (self.l // sq) % 2 == 0 else self.r > other.r
        return self.l // sq < other.l // sq

def add(x):
    global max_count
    freq[x] += 1
    cnt[freq[x]] += 1
    if freq[x] > max_count:
        max_count = freq[x]

def sub(x):
    global max_count
    cnt[freq[x]] -= 1
    if cnt[freq[x]] == 0 and max_count == freq[x]:
        max_count -= 1
    freq[x] -= 1

n,m = map(int, input().split())
li = list(map(int, input().split()))

sq = int(sqrt(n))
query = []

for i in range(m):
    q1, q2 = map(int, input().split())
    query.append(Query(q1 - 1, q2 - 1, i))

query.sort()

ans = [0] * m
freq = [0] * (max(li) + 1)
cnt = [0] * (n + 1)
max_count = 0

s, e = 0, 0
add(li[0])

for q in query:
    while e < q.r:
        e += 1
        add(li[e])
    while e > q.r:
        sub(li[e])
        e -= 1
    while s < q.l:
        sub(li[s])
        s += 1
    while s > q.l:
        s -= 1
        add(li[s])
    ans[q.idx] = max_count

for a in ans:
    print(a)