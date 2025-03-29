import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

diff = [0] * (n + 2)

for _ in range(m):
    a, b, k = map(int, input().split())
    diff[a] += k
    diff[b+1] -= k

curr = 0
ans = []
for i in range(1, n+1):
    curr += diff[i]
    ans.append(li[i-1] + curr)

print(*ans)