import sys
input = sys.stdin.readline 

n = int(input())
li = []
for _ in range(n):
    a,b = map(int, input().split())
    li.append((a,b))
li.sort()

ans = 0
s = 0
e = 0

for i in range(n):
    if(li[i][0] > e):
        ans += e - s
        s = li[i][0]
    if(e < li[i][1]):
        e = li[i][1]
        
ans += e - s
print(ans)