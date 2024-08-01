a,b = map(int, input().split())
k,x = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    if k - x <= i <= k + x:
        ans += 1

if ans:
    print(ans)
else:
    print("IMPOSSIBLE")