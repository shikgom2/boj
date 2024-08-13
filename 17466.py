n,m = map(int, input().split())

ans = 1


for i in range(n, 0, -1):
    ans *= i
    ans %= m
    if(ans == 0):
        break

print(ans)