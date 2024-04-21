n, k = map(int, input().split())
a = list(map(int, input().split()))
li = []
for i in range(1, n):
    li.append(a[i]-a[i-1])

li.sort()

ans = 0
for i in range(n-k):
    ans += li[i]
    
print(ans)