import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

ans = [0] * n
for i in range(n):
    r = li[i] - 1
    ans[r] = r - i

for r in ans:
    print(r)