import sys
input = sys.stdin.readline

n,t = map(int, input().split())
li = list(map(int, input().split()))

d = [0] * (n+ 1)
p = [0] * (n + 1)

for i in range(1, n):
    d[i] = li[i - 1] + li[i]
    p[i] = p[i - 1] + d[i]

ans = 0
t //= 2
for i in range(1, n):
    if i <= t:
        ans = max(ans, p[i - 1] + d[i] * (t + 1 - i))

print(ans)