n = int(input())

ans = 300
for i in range(n):
    t, l = map(int, input().split())
    ans = min(ans, t + l)

print(ans)