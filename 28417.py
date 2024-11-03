import sys
input = sys.stdin.readline

t = int(input())
ans = 0
for i in range(t):
    li = list(map(int, input().split()))
    tmp = max(li[0], li[1])
    li = li[2:]
    li.sort(reverse=True)
    tmp = tmp + li[0] + li[1]
    ans = max(tmp,ans)
print(ans)