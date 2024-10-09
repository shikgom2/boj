import sys
input = sys.stdin.readline 

n = int(input())
ans=0
for _ in range(n):
    k=int(input())
    if(k%2):
        ans+=1
print(ans)