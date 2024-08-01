n = int(input())
ans = 0
for _ in range(n):
    h, w = map(int, input().split())
    ans = max(ans, h * w)
print(ans)