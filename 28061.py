import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans = max(ans, li[i] - (n - i))
print(ans)