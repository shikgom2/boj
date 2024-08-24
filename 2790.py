import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)

li.sort()
val = []
cur = n
for i in range(len(li)):
    val.append(li[i] + cur)
    cur -= 1

points = max(val)
ans = 0
for i in range(len(li)):
    if(li[i] + n >= points):
        ans += 1
print(ans)