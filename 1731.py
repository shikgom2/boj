import sys
input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]

if li[1] - li[0] == li[2] - li[1]:
    diff = li[1] - li[0]
    ans = li[-1] + diff
else:
    r = li[1] // li[0]
    ans = li[-1] * r
    
print(ans)