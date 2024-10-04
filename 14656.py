import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in range(n):
    if(li[i] != i+1):
        ans +=1
print(ans)