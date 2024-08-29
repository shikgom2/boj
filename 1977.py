import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())

li = []
for i in range(101):
    check = i*i
    if(check >= n and check <= m):
        li.append(check)

if(len(li)):
    print(sum(li))
    print(min(li))
else:
    print(-1)