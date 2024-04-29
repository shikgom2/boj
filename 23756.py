n = int(input())
k = int(input())
ans = 0
for _ in range(n):
    a = int(input())
    ans = ans + min(abs(k-a), 360-k+a, k+360-a)
    k = a
print(ans)