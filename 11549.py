import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(len(li)):
    if(n == li[i]):
        ans += 1
print(ans)