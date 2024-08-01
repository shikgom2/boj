n,x = map(int, input().split())
li = list(map(int, input().split()))
ans = 2000
for i in range(n - 1):
    ans = min(ans, li[i] + li[i + 1])
print(ans * x)