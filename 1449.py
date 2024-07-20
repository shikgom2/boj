import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().split()))

li.sort()

s = li[0]
ans = 0
for i in range(1, n):
    if(m <= li[i] - s):
        ans += 1
        s = li[i]

print(ans+1)