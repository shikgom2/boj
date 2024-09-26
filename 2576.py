import sys
input = sys.stdin.readline 

li = []
for _ in range(7):
    k=int(input())
    if(k%2):
        li.append(k)

if(len(li)):
    print(sum(li))
    print(min(li))
else:
    print(-1)