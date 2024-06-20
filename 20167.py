def go(x, s, e):
    global ans
    if x == n:
        ans = max(ans, e)
        return
    go(x + 1, 0, e)
    if s + li[x] >= k:
        go(x + 1, 0, e + s + li[x] - k)
    else:
        go(x + 1, s + li[x], e)

n,k = map(int, input().split())
li = list(map(int, input().split()))

ans = 0
go(0, 0, 0)
print(ans)
