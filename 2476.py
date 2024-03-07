N = int(input())
res = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        res = max(res, 10000 + a * 1000)
    elif a == b:
        res = max(res, 1000 + a * 100)
    elif b == c:
        res = max(res, 1000 + b * 100)
    elif c == a:
        res = max(res, 1000 + c * 100)
    else:
        res = max(res, max(a, b, c) * 100)
print(res)