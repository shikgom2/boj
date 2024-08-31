import sys
input = sys.stdin.readline

n,k,m=map(int, input().split())
#first out : n mod k

ans = 0
out = 0
if(k%n):
    out = k%n
else:
    out = n

while(True):
    ans += 1

    if(out == m):
        break
    if(m - out > 0):
        m -= out
        n -= 1
        if(k % n):
            out = k%n
        else:
            out  = n
    else:
        m -= out
        m += n
        n -= 1
        if(k % n):
            out = k%n
        else:
            out = n
print(ans)