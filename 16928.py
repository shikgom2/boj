import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

up = [0] * 101
down = [0] * 101

for _ in range(n):
    i,j = map(int, input().split())
    up[i] = j

for _ in range(m):
    i,j = map(int, input().split())
    down[i] = j

visited = [False] * 101
visited[1] = True

q = deque()
q.append(1)

ans = 0

while(q):
    cnt = len(q)
    ans += 1
    while(cnt):
        cnt -= 1
        now = q.popleft()

        if(now == 100):
            print(ans-1)
            exit()
        else:
            for i in range(1, 7):
                next = now + i

                if(next > 100):
                    continue
                
                if(up[next] or down[next]):
                    next = up[next] + down[next]

                if(visited[next]):
                    continue
                visited[next] = True
                q.append(next)
