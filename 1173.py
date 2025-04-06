import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
else:
    cur = m
    ex = 0
    ans = 0

    while ex < N:
        if cur + T <= M:
            cur += T
            ex += 1
        else:
            cur = max(m, cur - R)
        ans += 1

    print(ans)
