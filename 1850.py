def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x


n, m = map(int, input().split())

ans = gcd(max(n,m), min(n,m))

for _ in range(ans):
    print(1, end="")