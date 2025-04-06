import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

ans = n - 1
for c in range(n):
    cur = n - 1
    check = [False] * m
    for i in range(n):
        if i == c:
            continue
        cnt = 0
        idx = -1
        for j in range(m):
            if li[i][j]:
                cnt += 1
                idx = j
        if cnt == 0:
            cur -= 1
        elif cnt == 1:
            check[idx] = True
    ans = min(ans, cur - sum(check))
print(ans)