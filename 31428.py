i=int(input())
li=list(map(str, input().split()))
s=input()
cnt =0
for i in li:
    if(s==i):
        cnt += 1
print(cnt)