import sys
input = sys.stdin.readline

n,k = map(int, input().split())

li = []
for _ in range(n):
    a = int(input())
    li.append(a)

ans = 0
nz_cnt = 0
cnt = {}

j = 0
for i in range(n):
    if li[i] not in cnt:
        cnt[li[i]] = 0
    if cnt[li[i]] == 0:
        nz_cnt += 1
    cnt[li[i]] += 1

    while nz_cnt > k + 1:
        cnt[li[j]] -= 1
        if cnt[li[j]] == 0:
            nz_cnt -= 1
        j += 1

    ans = max(ans, cnt[li[i]])

print(ans)