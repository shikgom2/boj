import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = list(map(str,input().split()))
    ans = float(a[0])
    for i in a:
        if i=='@':
            ans*=3
        elif i=='%':
            ans+=5
        elif i=='#':
            ans-=7
    print("%.2f" %ans)