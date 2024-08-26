import sys
input = sys.stdin.readline

ans = 0
for i in range(8):
    li = list(map(str, input().rstrip()))
    if i%2!=0:
        for j in range(8):
            if j%2!=0 and li[j]=='F':
                ans+=1
    else:
        for k in range(8):
            if k%2==0 and li[k]=='F':
                ans+=1
print(ans)