import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())
maps = [[[] for _ in range(c)] for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    maps[x-1][y-1].append([z, s, d-1])

ans = 0

for i in range(c):
    #catch shark
    for j in range(r):
        if maps[j][i]: #shark is exist
            value = maps[j][i][0]
            ans += value[0]
            maps[j][i].remove(value)
            break

    #move shark
    tmp = [[[] for _ in range(c)] for _ in range(r)]
    for j in range(r):
        for k in range(c):
            #has shark in map
            if maps[j][k]:
                z, s, d = maps[j][k][0]
                x, y = j, k
                s_count = s
                #move shark
                while s_count > 0:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        if d in [0, 2]:
                            d += 1
                        elif d in [1, 3]:
                            d -= 1
                        continue
                    x, y = nx, ny
                    s_count -= 1
                tmp[x][y].append([z, s, d])

    #update map
    for j in range(r):
        for k in range(c):
            maps[j][k] = tmp[j][k]

    #eat shark
    for j in range(r):
        for k in range(c):
            if len(maps[j][k]) >= 2:
                maps[j][k].sort(reverse=True)
                while len(maps[j][k]) >= 2:
                    maps[j][k].pop()

print(ans)
