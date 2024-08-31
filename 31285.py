import sys
input = sys.stdin.readline

n,m = map(int, input().split())
m -= 1
v,p,s = map(int, input().split())
k = v+p+s
li = []

print("0", end=" ")

for i in range(n):
    a,b,c = map(int, input().split())
    s = a+b+c
    if(a+b+c > k):
        continue
    else:
        li.append((s, i+1))

if(m >= len(li)):
    for i in range(len(li)):
        print(li[i][1], end=" ")
else:
    li.sort(key= lambda x : x[0], reverse=True)
    ans = []

    for i in range(m):
        print(li[i][1], end=" ")