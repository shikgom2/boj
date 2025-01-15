n = int(input())
ans = 0
for a in range(n + 1):
    for b in range(a, n + 1):
        ans += a + b
print(ans)