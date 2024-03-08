from collections import deque

def dfs(x, y, cnt, w, h, map, visited):
    if x < 0 or y < 0 or x >= w or y >= h or cnt <= 0 or map[y][x] <= -1:
        return
    if visited[y][x] >= cnt:
        return
    visited[y][x] = cnt
    map[y][x] = cnt
    dfs(x+1, y, cnt-1, w, h, map, visited)
    dfs(x, y+1, cnt-1, w, h, map, visited)
    dfs(x-1, y, cnt-1, w, h, map, visited)
    dfs(x, y-1, cnt-1, w, h, map, visited)

def is_on(x, y, w, h, map):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    if map[y][x] >= 2:
        return True
    else:
        return False

w, h = map(int, input().split())
n = int(input())
map = [[-1 for _ in range(w)] for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
block = deque()
lamp = deque()

for _ in range(n):
    s, x, y = input().split()
    x, y = int(x), int(y)
    if s == "redstone_dust":
        map[y][x] = 0
    elif s == "redstone_block":
        map[y][x] = 15
        block.append((x, y))
    elif s == "redstone_lamp":
        map[y][x] = -2
        lamp.append((x, y))

while block:
    x, y = block.popleft()
    visited[y][x] = 15
    dfs(x+1, y, 15, w, h, map, visited)
    dfs(x-1, y, 15, w, h, map, visited)
    dfs(x, y+1, 15, w, h, map, visited)
    dfs(x, y-1, 15, w, h, map, visited)

flag = True
while lamp:
    x, y = lamp.popleft()
    if not is_on(x+1, y, w, h, map) and not is_on(x, y+1, w, h, map) and not is_on(x-1, y, w, h, map) and not is_on(x, y-1, w, h, map):
        print("failed")
        flag = False
        break
if flag:
    print("success")
