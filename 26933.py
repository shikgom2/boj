import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    h, b, k = map(int, input().split())
    if b-h > 0:
        ans += (b-h)*k
print(ans)