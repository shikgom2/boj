from collections import deque

n = int(input())
li = list(map(int, input().split()))
s, e = map(int, input().split())

visited = [0] * (n+1)
q = deque()
q.append((s,1))
visited[s] = 1

while (q):
    x, y = q.popleft()
    cur = li[x-1]
    dx = x
    while(True):
        #print(q)

        dx = dx + cur
        
        if(dx == e):
            print(y)
            exit()

        if(dx > n):
            break

        if(visited[dx] == 0):
            visited[dx] = 1
            q.append((dx, y+1))
print(-1)