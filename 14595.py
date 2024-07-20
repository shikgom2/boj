import sys
input = sys.stdin.readline 
from collections import defaultdict

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[max(a, b)] = min(a, b)

n = int(input())
parent = [i for i in range(n + 1)]

t = int(input())

range_dict = defaultdict(list)
for i in range(n + 1):
    range_dict[i] = [i, i]

for _ in range(t):
    a, b = map(int, input().split())

    pa = find(a)
    pb = find(b)

    if pa == pb:
        continue

    update = 0
    start, end = 0, 0
    if pa < pb:
        start = pa
        end = pb
        update = pa
    else:
        start = pb
        end = pa
        update = pb

    index = start

    while index <= end:
        parent[index] = update
        s, e = range_dict[index]
        index = e + 1

    range_dict[update] = [a, b]

ans = set()
for i in range(1, n + 1):
    ans.add(find(parent[i]))

print(len(ans))