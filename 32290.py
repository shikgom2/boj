import sys
input = sys.stdin.readline 


l,r,x = map(int, input().split())
li = []

for i in range(l, r+1, 1):
    li.append(i | x)

li.sort()

cur = 0
for i in range(max(li)):
    if(li[cur] != i):
        print(i)
        exit()
    else:
        cur += 1

print(max(li) + 1)