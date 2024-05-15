import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

def bfs(x, y):
    q = deque() 
    q.append([x,y])
    maps[y][x] = 0

    while(q):
        x, y = q.popleft()
        for i in range(len(dx)):
            d_x = x + dx[i]
            d_y = y + dy[i]

            if(0 <= d_x < w and 0 <= d_y < h and maps[d_y][d_x] == 1):
                q.append([d_x, d_y])
                maps[d_y][d_x] = 0

while(True):
    w,h = map(int, input().split())
    if(w == 0 and h == 0):
        break
    
    maps = []
    for i in range(h):
        maps.append(list(map(int, input().split())))
    
    ans = 0

    for i in range(h):
        for j in range(w):
            if(maps[i][j] == 1):
                bfs(j,i)
                ans += 1
    print(ans)