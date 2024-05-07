import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    t = int(input())
    li.append((t, i))

li = sorted(li)
ans = 0
for i in range(n):
    ans = max(ans, li[i][1]-i)

print(ans+1)