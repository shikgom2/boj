n,m = map(int, input().split())
ans = 0
for i in range(1, n+1):
    t = i

    while(True):
        if(t%10 == m):
            ans += 1
        t = t // 10

        if(t == 0):
            break

print(ans)