import sys
input = sys.stdin.readline
ans=0
n = int(input())
for i in range(1, 501):
    for j in range(1, 501):
        if((i*i + n) == (j*j)):
            ans += 1
print(ans)