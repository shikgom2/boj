import sys
input = sys.stdin.readline

n,m =map(int, input().split())

ans = 0
if(n % 2 == 0):
    n += 1
    ans += 1

if(m % 2):
    m -= 1
    ans += 1

for i in range(n, m, 2):
    ans += 1
print(ans)