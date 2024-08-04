import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))

flag = True
cur = li[0]
ans = 0
for i in range(1, len(li)):
    if(li[i] > cur):
        cur = li[i]
    elif(li[i] + m > cur):
        cur = li[i] + m
        ans += 1
    else:
        flag = False
        break

if(flag):
    print(ans)
else:
    print(-1)