import sys
input = sys.stdin.readline
from collections import deque


n = int(input())

dp = [None] * (n+1)
dp[0] = (0, 0)

q = deque()
q.append((0, 0, 0))

while q:
    h, d, w = q.popleft()
    for nw, nh in [(1, h + 1), (3, h * 3), (5, h * h)]:
        nd = d + 1
        nw = w + nw
        
        if nh > n:
            continue
        
        if dp[nh] is None or nd < dp[nh][0] or (nd == dp[nh][0] and nw < dp[nh][1]):
            dp[nh] = (nd, nw)
            q.append((nh, nd, nw))

print(dp[n][0], dp[n][1])
