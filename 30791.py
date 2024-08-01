a, b, c, d, e = map(int, input().split())
ans = 0
if a - 1000 <= b:
    ans += 1
if a - 1000 <= c:
    ans += 1
if a - 1000 <= d:
    ans += 1
if a - 1000 <= e:
    ans += 1

print(ans)