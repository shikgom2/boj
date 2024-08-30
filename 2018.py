import sys
input = sys.stdin.readline

n = int(input())
l = 0
r = 0
ans = 0
while(True):
    if(r == n+1):
        break
    tmp = 0
    for i in range(l, r+1):
        tmp += i

    if(tmp == n):
        ans += 1
        r += 1
    elif(tmp > n):
        l += 1
    elif(tmp < n):
        r += 1

print(ans)