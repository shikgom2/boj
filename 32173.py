import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

prefix = [0] * (n+1)
prefix[0] = li[0]
for i in range(len(li)):
    prefix[i] = prefix[i-1] + li[i]

ans = 0
for i in range(n):
    ans = max(ans, li[i] - prefix[i-1])

print(ans)