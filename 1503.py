n, s = map(int, input().split())
check = [0] * 1010

if(s != 0):
    li = list(map(int, input().split()))
    for i in li:
        check[i] = 1
else:
    li = []

ans = 10**10

for i in range(1, 1002):
    if(check[i] == 1):
        continue
    for j in range(1, 1002):
        if(check[j] == 1):
            continue
        for k in range(1, 1002):
            if(check[k] == 1):
                continue
            q = (i * j * k)
            if(abs(n - q) < ans): 
                ans = abs(n - q)
            if(n + 1 < q): 
                break

print(ans)