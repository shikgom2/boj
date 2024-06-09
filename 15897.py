n = int(input())
ans = n
n -= 1
l = 1

while l <= n:
    k = n // l
    r = n // k
    ans += (r - l + 1) * k
    l = r + 1

print(ans)