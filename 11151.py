import sys
input = sys.stdin.readline
from itertools import combinations

t = int(input())
idx = 1
for _ in range(t):
    n = int(input())
    req_w, req_c, req_f = map(int, input().split())
    li = []
    for _ in range(n):
        w, c, f = map(int, input().split())
        li.append((w, c, f))
    
    ans = None
    for k in range(1, n + 1):
        for comb in combinations(li, k):
            sum_w = sum(r[0] for r in comb)
            sum_c = sum(r[1] for r in comb)
            sum_f = sum(r[2] for r in comb)
            if sum_w >= req_w and sum_c >= req_c and sum_f >= req_f:
                ans = k
                break
        if ans is not None:
            break
    
    if ans is None:
        print("game over")
    else:
        print(ans)

