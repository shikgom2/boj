import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = [0]*1001
ans = 0
for i in map(int, input().split()):
    for v in range(i,n+1,i):
        if(li[v]):
            continue		
        ans+=v
        li[v]=1
print(ans)