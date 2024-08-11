import sys
input = sys.stdin.readline

li = list(map(str, input().rstrip()))
ans=10

for i in range(len(li)):
    if i==0:
       continue
    if li[i-1]==li[i]:
        ans += 5
    else:
        ans +=10
print(ans)