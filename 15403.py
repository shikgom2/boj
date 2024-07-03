import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

check = [[] for _ in range(n + 1)]

for i in range(len(li)):
    k = li[i]
    check[k].append(i)
for i in range(len(check)):
    check[i].reverse()

check.reverse()
li = [item for sublist in check for item in sublist]

ans = [0] * n

for i in range(len(li)):
    ans[li[i]] = i+1

print(*ans)