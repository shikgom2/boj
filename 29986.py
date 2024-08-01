n,h = map(int, input().split())

li = list(map(int, input().split()))
ans = 0
for i in li:
    if i <= h:
        ans += 1

print(ans)