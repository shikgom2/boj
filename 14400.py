import sys
input = sys.stdin.readline

n = int(input())

li=[]
for _ in range(n):
    a, b= map(int, input().split())
    li.append((a,b))

li.sort(key=lambda x:x[0])
x=li[len(li)//2][0]
li.sort(key=lambda x:x[1])
y=li[len(li)//2][1]
ans=0
for i in range(n):
    ans += (abs(x-li[i][0])+abs(y-li[i][1]))

print(ans)