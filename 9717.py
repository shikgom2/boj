import sys
input = sys.stdin.readline
from collections import deque

def kdist(r, c):
    if r < c:
        return kdist(c, r)
    if r == c:
        if r % 3 == 0:
            return (r // 3) * 2
        else:
            return float('inf')
    if c == 0:
        if r % 4 == 0:
            return r // 2
        else:
            return float('inf')
    if r > 2 * c:
        return c + kdist(r - c * 2, 0)
    d = r - c
    return d + kdist(r - d * 2, c - d)

def check(p, N):
    return 1 <= p[0] <= N and 1 <= p[1] <= N

def solve(n, r1, c1, r2, c2):
    dist = {}
    dist[(r1, c1)] = 0
    q = deque([(r1, c1)])
    
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        t1 = q.popleft()
        cur = dist[t1]
        if cur > 25:
            break
        for i in range(8):
            t2 = (t1[0] + dx[i], t1[1] + dy[i])
            if not check(t2, n):
                continue
            if t2 not in dist:
                dist[t2] = cur + 1
                q.append(t2)
    
    ans = float('inf')
    for key, value in dist.items():
        t1 = value + kdist(abs(key[0] - r2), abs(key[1] - c2))
        if(t1 < ans):
            ans = t1 
    return ans

t = int(input())
for _ in range(t):
    n, r1, c1, r2, c2 = map(int, input().split())
    print(solve(n, r1, c1, r2, c2))