import sys
input = sys.stdin.readline
from collections import defaultdict


def coordinate_decomp(li):
    temp = sorted(li)
    value_to_index = {v: i for i, v in enumerate(temp)}
    decomp = [value_to_index[v] for v in li]
    return decomp

n,m = map(int, input().split())
li = defaultdict(int)
ans = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    t = coordinate_decomp(tmp)
    t = tuple(t)
    li[t] += 1
ans = 0

for i in li.values():
    ans += (i * (i-1)) // 2
print(ans)