import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)

ans1 = 1
cur = li[0]
for i in range(1, n):
    if(li[i] > cur):
        cur = li[i]
        ans1 += 1

li.reverse()
ans2 = 1
cur = li[0]
for i in range(1, n):
    if(li[i] > cur):
        cur = li[i]
        ans2 += 1
print(ans1)
print(ans2)