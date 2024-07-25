import sys
input = sys.stdin.readline

n,m=map(int, input().split())
ans = 0
cur = m
for i in range(m):
    ans += cur
    cur /= 2

if(ans > n):
    print("TAK")
else:
    print("NIE")