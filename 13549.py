import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
q.append(N)
visited = [-1 for _ in range(100001)]
visited[N]=0

while q:
    s=q.popleft()
    if s == K:
        print(visited[s])
        break
    if 0 <= (s-1) < 100001 and visited[s-1]==-1:
        visited[s-1]=visited[s]+1
        q.append(s-1)
    if 0 <= (s*2) < 100001 and visited[s*2]==-1:
        visited[s*2]=visited[s]
        q.appendleft(s*2)
    if 0 <= (s+1) < 100001 and visited[s+1]==-1:
        visited[s+1]=visited[s]+1
        q.append(s+1)