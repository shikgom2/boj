import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ans = 0
cur = 0
for i in range(len(li)):
    if(li[i]):
        cur += 1
        ans = max(cur,ans)
    else:
        cur = 0

ans = max(cur, ans)
print(ans)