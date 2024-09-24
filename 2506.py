import sys
input = sys.stdin.readline

ans =0 
n = int(input())
li = list(map(int, input().split()))

cur = 0

for i in range(n):
    if(li[i]):
        cur += 1
        ans += cur
    else:
        cur = 0
print(ans)