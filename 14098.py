import sys
input = sys.stdin.readline

n = int(input())

dir = dict()

for i in range(n):
    s = input().rstrip()
    dir[s] = i

li = []
for i in range(n):
    s = input().rstrip()
    li.append(s)

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if(dir[li[i]] > dir[li[j]]):
            ans += 1
            break
print(ans)