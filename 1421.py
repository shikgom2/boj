import sys
input = sys.stdin.readline 

n, c, w = map(int, input().split())

li = []
for _ in range(n):
    k = int(input())
    li.append(k)

ans = 0
for i in range(1, max(li)+1):
    s = 0
    for j in range(len(li)):
        
        q, r = divmod(li[j], i)
        if(r >= 1):
            money = q * c
        else:
            money = (q-1) * c
        
        res = (q * i * w) - money
        if(res < 0):
            continue
        s += res

    ans = (max(ans, s))
print(ans)