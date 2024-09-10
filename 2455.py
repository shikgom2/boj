import sys
input = sys.stdin.readline

ans = 0
cur = 0
for _ in range(4):
    a,b = map(int, input().split())
    cur = cur + b - a

    ans = max(ans, cur)
print(ans)