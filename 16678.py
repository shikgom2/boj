import sys
input = sys.stdin.readline 

n = int(input())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)
li.sort()
idx = 1
ans = 0
for i in range(n):
    if(li[i] >= idx):
        ans += (li[i] - idx)
        idx += 1
print(ans)