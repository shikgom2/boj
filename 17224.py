import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
li = []
for _ in range(a):
    n,m= map(int, input().split())
    li.append([n,m,0])

ans = 0
li.sort(key=lambda x: x[1])

for i in range(len(li)):
    if(c == 0):
        break
    
    if(li[i][1] <= b):
        c -= 1 
        ans += 140
        li[i][2] = 1


for i in range(len(li)):
    if(c == 0):
        break
    
    if(li[i][0] <= b and li[i][2] == 0):
        c -= 1
        ans += 100
        li[i][2] = 1
        
print(ans)