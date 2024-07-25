import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    ans = b+c+d
    if(ans >= 55 and b>=11 and c>=8 and d>=12):
        print(a,ans,"PASS")
    else:
        print(a, ans, "FAIL")