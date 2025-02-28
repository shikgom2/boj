import sys
input = sys.stdin.readline

n, t = map(int, input().split())
li = []
for _ in range(n):
    x, h = map(int, input().split())
    li.append((x, h))
li.sort()

ans = 0
mx = -10**18
for i, (x, h) in enumerate(li):
    if i == 0:
        # 가장 왼쪽 나무는 그림자가 없음.
        mx = h + t * x
        continue
    y = mx - t * x
    if y > 0:
        ans += min(h, y)
    c = h + t * x
    if c > mx:
        mx = c
print(ans)
