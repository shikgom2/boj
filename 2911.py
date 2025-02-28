import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []

for _ in range(n):
    p, c = map(int, input().split())
    li.append((p, c))

li.sort(key=lambda x: x[0])

ans = li[0][1]
for i in range(1, n):
    ans += max(0, li[i][1] - li[i-1][1])

print(ans)
