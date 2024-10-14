import sys
input = sys.stdin.readline

a,b,c =map(int, input().split())
n = int(input())

ans = 0
for _ in range(n):
    tmp = 0
    for i in range(3):
        d,e,f=  map(int, input().split())
        tmp += a*d + b*e + c*f
    
    ans = max(tmp, ans)
print(ans)