import sys
input = sys.stdin.readline

def dfs(start, v, left, right, visit):
    if visit[start]:
        return False

    visit[start] = True

    for next_node in v[start]:
        if right[next_node] == -1 or dfs(right[next_node], v, left, right, visit):
            left[start] = next_node
            right[next_node] = start
            return True

    return False

def dfs1(v, point, R, C):
    left = [-1] * (R * C + 1)
    right = [-1] * (R * C + 1)
    match_count = 0

    for i in range(len(point)):
        visit = [False] * (R * C + 1)
        if dfs(i, v, left, right, visit):
            match_count += 1

    return match_count // 2  # Each match is counted twice

n,m = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

number = [[0] * m for _ in range(n)]
Map = [list(input().strip()) for _ in range(n)]

point = []
v = [[] for _ in range(n*m + 1)]

cnt = 0
xcnt = 0

# Initialize number grid and point list
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'X':
            xcnt += 1
        number[i][j] = cnt
        point.append(cnt)
        cnt += 1

for i in range(n):
    for j in range(m):
        if Map[i][j] == 'X':
            continue
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= y < n and 0 <= x < m and Map[y][x] != 'X':
                v[number[i][j]].append(number[y][x])

two = dfs1(v, point, n, m)
one = n * m - 2 * two - xcnt

print(two + one)