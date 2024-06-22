n, a, b = map(int, input().split())
ans = 0

while(a != b):
    a -= (a//2)
    b -= (b//2)
    ans += 1
print(ans)