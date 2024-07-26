n = int(input())

ans = 10**10

for _ in range(n):
    a,b = map(int, input().split())
    if a <= b:
        ans = min(ans, b)

if ans != 10**10:
    print(ans)
else:
    print(-1)