import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ans = None
idx = None
for i in range(1, n + 1):
    p, k, c = map(int, input().split())
    pay = (q - 1) // k
    add = c * (pay * (pay + 1) // 2)
    total = p + add
    
    if ans is None or total < ans:
        ans = total
        idx = i

print(idx, ans)
