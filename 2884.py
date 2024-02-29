n,m = map(int, input().split())

res = (n*60) + m
res -= 45
if(res < 0):
    res += (60 * 24)
print(f"{res//60} {res%60}")